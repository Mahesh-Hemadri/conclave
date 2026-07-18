from app.agents.base_agent import BaseAgent
from app.core.state import ArenaState
from app.models.agent import AgentMetadata


class SecurityAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            AgentMetadata(
                name="Security",
                role="Security Engineer",
                description="Reviews system security.",
                capabilities=[
                    "security",
                    "authentication",
                ],
                priority=10,
                confidence=0.95,
                provider="gemini",
            )
        )

    def execute(self, state: ArenaState) -> ArenaState:

        reasoning = state.get("reasoning", {})

        reasoning[self.name] = (
            "OAuth2 + JWT should secure the APIs."
        )

        state["reasoning"] = reasoning

        return state