# model-tools — Architecture

> Part of the [Hardonia Platform](https://github.com/Hardonian/Hardonian).

## Position in the Platform

```
┌─────────────────────────────────────────────────────────────────┐
│                        HARDONIA PLATFORM                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  AUTOPILOT   │  │ AGENT-INFRA │  │ AGENT-EDGE  │             │
│  │             │  │             │  │             │             │
│  │             │  │ control-    │  │ mesh-edge/  │             │
│  │             │  │  plane/     │  │ pcap/       │             │
│  │             │  │ mission-    │  │             │             │
│  │             │  │  ledger/    │  └─────────────┘             │
│  │             │  │ agent-mesh/ │                               │
│  │             │  │ mcpwall/    │                               │
│  └──────┬──────┘  └──────┬──────┘                               │
│         │                │                                      │
│         └────────────────┤                                      │
│                    ┌─────▼─────┐                               │
│                    │ MODEL-    │                               │
│                    │ TOOLS     │                               │
│                    │ ◄── THIS  │                               │
│                    │ model-    │                               │
│                    │  forge/   │                               │
│                    │ inference-│                               │
│                    │  api/     │                               │
│                    │ ollama-   │                               │
│                    │  router/  │                               │
│                    └───────────┘                               │
├─────────────────────────────────────────────────────────────────┤
│  COMMERCIAL LAYER                                               │
│  hardonia-store · comfyui-workflow-packs · content-repo          │
└─────────────────────────────────────────────────────────────────┘
```

## What model-tools does

AI model infrastructure — selection, inference, and GPU routing:

| Component | Language | Role |
|---|---|---|
| **model-forge** | TypeScript | Compute intelligence — optimal model + accelerator + runtime selection |
| **inference-api** | Python | OpenAI-compatible LLM inference gateway with multi-GPU routing |
| **ollama-router** | Python | Self-optimizing VRAM-fit model routing across GPUs |

## Dependencies on sibling repos

| Dependency | Via | What it provides |
|---|---|---|
| [autopilot](https://github.com/Hardonian/autopilot) | growth | Content generation requests served by inference-api |
| [agent-infra](https://github.com/Hardonian/agent-infra) | control-plane | Inference workload orchestration via control-plane |

## Internal dependencies

```
model-forge ──→ ollama-router  (GPU routing for selected configs)
inference-api ──→ ollama-router  (model serving via router)
```

## Sibling repos

- [autopilot](https://github.com/Hardonian/autopilot) — ops, finops, growth, support
- [agent-infra](https://github.com/Hardonian/agent-infra) — control-plane, mission-ledger, agent-mesh, mcpwall
- [agent-edge](https://github.com/Hardonian/agent-edge) — mesh-edge, pcap
