# model-tools

**AI model tooling: inference gateway, GPU router, and model selection.**

A unified monorepo consolidating Hardonian's AI model infrastructure — from choosing the right model+hardware config, to routing inference across GPUs, to serving a production OpenAI-compatible API.

---

## Subprojects

### [`model-forge/`](model-forge/) — ModelForge ⚡
**Compute intelligence for AI deployment.**

Given an AI model, revision, workload, latency target, and cost constraint, ModelForge compiles the optimal model + accelerator + runtime + precision + serving topology. TypeScript/Node.js (pnpm monorepo).

- [Full README](model-forge/README.md)
- [Roadmap](model-forge/ROADMAP.md)

### [`inference-api/`](inference-api/) — LLM Inference API
**Production-ready local LLM inference gateway.**

OpenAI-compatible endpoints (`/v1/chat/completions`, `/v1/completions`, `/v1/models`), multi-GPU routing, load balancing, auth, rate limiting, and Prometheus metrics. Python (FastAPI + uv).

- [Full README](inference-api/README.md)
- [API Docs](inference-api/API.md)

### [`ollama-router/`](ollama-router/) — Ollama GPU Router
**Self-optimizing VRAM-fit model routing across GPUs.**

A thin FastAPI proxy that routes client requests to the correct GPU by VRAM requirement. One endpoint for all your local models — routed to the right GPU, automatically. Python (FastAPI + uv).

- [Full README](ollama-router/README.md)
- [Bootstrap Guide](ollama-router/BOOTSTRAP.md)

---

## Repository Layout

```
model-tools/
├── model-forge/        # TypeScript (pnpm) — model selection & compute intelligence
│   ├── apps/           # web, HF Space
│   ├── packages/       # core libraries
│   └── package.json
├── inference-api/      # Python (uv) — LLM inference gateway
│   ├── app/            # FastAPI application
│   ├── tests/
│   └── pyproject.toml
├── ollama-router/      # Python (uv) — GPU-aware Ollama proxy
│   ├── app/            # FastAPI application
│   ├── tests/
│   └── pyproject.toml
└── README.md           # ← you are here
```

Each subdirectory is an independent project with its own build system, tests, and documentation. They can be used standalone or together as a complete AI inference stack.

## Getting Started

Each subproject has its own setup instructions — see the linked READMEs above. In general:

```bash
# ModelForge (TypeScript)
cd model-forge && pnpm install

# Inference API (Python)
cd inference-api && uv sync && uv run python main.py

# Ollama Router (Python)
cd ollama-router && uv sync && uv run uvicorn app.main:app
```


## Related Repos

### Platform Monorepos
- [autopilot](https://github.com/Hardonian/autopilot) — ops, finops, growth, support
- [agent-infra](https://github.com/Hardonian/agent-infra) — control-plane, mission-ledger, agent-mesh, mcpwall
- [agent-edge](https://github.com/Hardonian/agent-edge) — mesh-edge, pcap

### Commercial
- [hardonia-store](https://github.com/Hardonian/hardonia-store) — storefront
- [comfyui-workflow-packs](https://github.com/Hardonian/comfyui-workflow-packs) — ComfyUI workflow products
- [content-repo](https://github.com/Hardonian/content-repo) — blog posts and email sequences

## License

Each subproject retains its original license. See `LICENSE` files in each directory.

---

*Consolidated from [ModelForge](https://github.com/Hardonian/ModelForge), [llm-inference-api](https://github.com/Hardonian/llm-inference-api), and [ollama-router](https://github.com/Hardonian/ollama-router).*
