from agents.base_agent import BaseAgent
from core.state import ArenaState

class BackendAgent(BaseAgent):

    def __init__(self):

        super().__init__(

            name="Backend",

            role="Backend Engineer",

            capabilities=[
                "backend",
                "api",
                "database",
            ],
        )

    def execute(self, state: ArenaState) -> ArenaState:

        reasoning = state.get("reasoning", {})

        reasoning[self.name] = """
        FastAPI is recommended for backend APIs.
        """

        state["reasoning"] = reasoning

        return state