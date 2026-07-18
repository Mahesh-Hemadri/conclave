from app.agents.base_agent import BaseAgent
from app.core.state import ArenaState
from app.models.agent import AgentMetadata


class BackendAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            AgentMetadata(
                name="Backend",
                role="Backend Engineer",
                description="Designs backend services and REST APIs.",
                capabilities=[
                    "backend",
                    "api",
                    "database",
                ],
                priority=8,
                confidence=0.90,
                provider="gemini",
            )
        )

    def execute(self, state: ArenaState) -> ArenaState:

        reasoning = state.get("reasoning", {})

        reasoning[self.name] = (
            "FastAPI is recommended for backend APIs."
        )

        state["reasoning"] = reasoning

        return state