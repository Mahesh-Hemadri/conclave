from app.agents.base_agent import BaseAgent

from app.core.state import ArenaState
from app.models.agent import AgentMetadata


class BackendAgent(BaseAgent):

    def __init__(self,provider):
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
            ),
            provider
        )

    def execute(self, state):

        prompt = f"""
    You are a Senior Backend Engineer.

    User Request:
    {state["user_query"]}

    Design the backend APIs.

    Discuss:

    - REST APIs
    - Database
    - Services
    - Scalability

    Maximum 200 words.
    """

        reasoning = state.get("reasoning", {})

        reasoning[self.name] = self.provider.generate(prompt)

        state["reasoning"] = reasoning

        return state