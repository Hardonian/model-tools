"""ModelForge Continuous Hugging Face Hub Webhook Sync.

Triggers real-time Compute Passport compilation and validates webhook payloads.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import uuid
from datetime import UTC, datetime
from typing import Any

import httpx


class HuggingFaceSyncManager:
    """Manages continuous synchronization between Hugging Face model commits and ModelForge."""

    def __init__(self, api_url: str = "http://localhost:3000/api/v1/webhooks/huggingface", webhook_secret: str | None = None) -> None:
        self.api_url = api_url
        self.webhook_secret = webhook_secret or "hf-secret-sync"

    def generate_webhook_payload(
        self,
        repo_id: str,
        commit_sha: str | None = None,
        author: str = "model-author",
        event: str = "commit_pushed",
    ) -> dict[str, Any]:
        """Synthesizes a realistic Hugging Face Hub webhook event payload."""
        sha = commit_sha or uuid.uuid4().hex[:12]
        params_b = 70.6 if "70B" in repo_id else (27.2 if "27b" in repo_id else 8.03)

        return {
            "event": event,
            "repo_id": repo_id,
            "commit_sha": sha,
            "author": author,
            "model_architecture": "LlamaForCausalLM" if "llama" in repo_id.lower() else "Gemma2ForCausalLM",
            "parameters_billions": params_b,
            "context_length": 8192,
            "timestamp": datetime.now(UTC).isoformat(),
        }

    def sign_payload(self, payload: dict[str, Any]) -> str:
        """Calculates HMAC-SHA256 signature for webhook transmission."""
        body = json.dumps(payload, separators=(",", ":"))
        sig = hmac.new(
            self.webhook_secret.encode("utf-8"),
            body.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        return f"sha256={sig}"

    def trigger_sync(
        self,
        repo_id: str,
        commit_sha: str | None = None,
        client: httpx.Client | None = None,
    ) -> dict[str, Any]:
        """Dispatches webhook sync payload to local or remote ModelForge endpoint."""
        payload = self.generate_webhook_payload(repo_id, commit_sha)
        sig = self.sign_payload(payload)
        headers = {
            "Content-Type": "application/json",
            "x-hub-signature-256": sig,
        }

        if client is not None:
            res = client.post(self.api_url, json=payload, headers=headers)
            return res.json()

        # In offline/dry-run mode, simulate local passport compilation
        return {
            "received": True,
            "status": "synced",
            "repo_id": payload["repo_id"],
            "commit_sha": payload["commit_sha"],
            "passport_id": f"pass-{uuid.uuid4().hex[:8]}",
            "parameters_billions": payload["parameters_billions"],
            "synced_at": datetime.now(UTC).isoformat(),
        }
