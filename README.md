# Conclave

> An extensible multi-agent reasoning framework built with LangGraph and Gemini.

Conclave is an actively developed AI orchestration project exploring how multiple specialized LLM agents can collaborate to solve complex software-engineering tasks.

Instead of relying on a single LLM call, Conclave separates **planning, specialist execution, tool use, and final synthesis** into distinct components.

## Architecture

```text
                         USER QUERY
                             │
                             ▼
                    ┌─────────────────┐
                    │     PLANNER     │
                    │                 │
                    │ Determines which│
                    │ specialists are │
                    │    required     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ AGENT REGISTRY  │
                    │                 │
                    │ Selects agents  │
                    │ based on plan   │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌───────────┐  ┌───────────┐  ┌───────────┐
        │ Architect │  │  Backend  │  │ Security  │
        │   Agent   │  │   Agent   │  │   Agent   │
        └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                    ┌─────────────────┐
                    │ EXECUTION ENGINE│
                    │                 │
                    │ Coordinates     │
                    │ agent execution │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      JUDGE      │
                    │                 │
                    │ Synthesizes and │
                    │ reviews agent   │
                    │    outputs      │
                    └────────┬────────┘
                             │
                             ▼
                       FINAL ANSWER