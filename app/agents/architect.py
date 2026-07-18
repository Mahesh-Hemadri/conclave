from app.agents.base_agent import BaseAgent
from app.models.agent import AgentMetadata
from app.core.state import ArenaState


class ArchitectAgent(BaseAgent):

    def __init__(self, provider):

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
            ),
            provider
        )

    def execute(self, state):

        prompt = f"""
    You are a Principal Software Architect.

    User Request:
    {state["user_query"]}

    Provide ONLY architecture recommendations.

    Maximum 200 words.
    """

        reasoning = state.get("reasoning", {})

        reasoning[self.name] = self.provider.generate(prompt)

        state["reasoning"] = reasoning

        return state