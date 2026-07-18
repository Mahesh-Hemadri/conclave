from agents.base_agent import BaseAgent
from core.state import ArenaState

class ArchitectAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            name="Architect",

            role="Software Architect",

            capabilities=[
                "architecture",
                "system design",
                "scalability",
            ],
        )

    def execute(self, state: ArenaState) -> ArenaState:

        reasoning = state.get("reasoning", {})

        reasoning[self.name] = """
        I recommend a Microservices Architecture
        using API Gateway and Event Driven Communication.
        """

        state["reasoning"] = reasoning

        return state