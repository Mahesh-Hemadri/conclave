from app.agents.base_agent import BaseAgent

from app.core.state import ArenaState
from app.models.agent import AgentMetadata
from app.utils.prompt_loader import PromptLoader
from app.providers.request import ProviderRequest


class BackendAgent(BaseAgent):

    def __init__(self,provider, tool_executor = None):
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
            provider,
            tool_executor
        )

    def execute(self, state):

        template = PromptLoader.load("backend.md")

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