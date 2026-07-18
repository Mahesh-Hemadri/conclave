from app.agents.base_agent import BaseAgent
from app.models.agent import AgentMetadata
from app.core.state import ArenaState


class ArchitectAgent(BaseAgent):

    def __init__(self):

        super().__init__(

            AgentMetadata(

                name="Architect",

                role="Software Architect",

                description="Designs scalable software systems.",

                capabilities=[
                    "architecture",
                    "system design",
                    "scalability",
                ],

                priority=10,

                confidence=0.95,

                provider="gemini",
            )
        )

    def execute(
        self,
        state: ArenaState,
    ) -> ArenaState:

        reasoning = state.get("reasoning", {})

        reasoning[self.name] = (
            "Recommended a Microservices architecture."
        )

        state["reasoning"] = reasoning

        return state