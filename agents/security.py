from agents.base_agent import BaseAgent
from core.state import ArenaState

class SecurityAgent(BaseAgent):

    def __init__(self):

        super().__init__(

            name="Security",

            role="Security Engineer",

            capabilities=[
                "security",
                "authentication",
            ],
        )

    def execute(self, state: ArenaState) -> ArenaState:

        reasoning = state.get("reasoning", {})

        reasoning[self.name] = """
        OAuth2 + JWT should secure all APIs.
        """

        state["reasoning"] = reasoning

        return state