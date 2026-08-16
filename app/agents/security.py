from app.agents.base_agent import BaseAgent

from app.core.state import ArenaState
from app.models.agent import AgentMetadata
from app.utils.prompt_loader import PromptLoader
from app.providers.request import ProviderRequest


class SecurityAgent(BaseAgent):

    def __init__(self, provider, tool_executor = None):

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
            provider,   
            tool_executor
        )

    def execute(self, state):

        template = PromptLoader.load("security.md")

        prompt = template.format(
            query=state["user_query"]
        )

        reasoning = state.get("reasoning", {})

        request = ProviderRequest(
            prompt=prompt
        )

        response = self.provider.generate(request)

        reasoning[self.name] = response.text

        state["reasoning"] = reasoning

        return state