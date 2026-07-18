from app.agents.base_agent import BaseAgent

from app.core.state import ArenaState
from app.models.agent import AgentMetadata


class SecurityAgent(BaseAgent):

    def __init__(self, provider):

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
            ),
            provider
        )

    def execute(self, state):

        prompt = f"""
    You are a Senior Security Engineer.

    User Request:

    {state["user_query"]}

    Review the solution.

    Suggest:

    - Authentication
    - Authorization
    - Encryption
    - API Security

    Maximum 200 words.
    """

        reasoning = state.get("reasoning", {})

        reasoning[self.name] = self.provider.generate(prompt)

        state["reasoning"] = reasoning

        return state