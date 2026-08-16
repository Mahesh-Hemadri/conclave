from app.agents.base_agent import BaseAgent
from app.models.agent import AgentMetadata
from app.utils.prompt_loader import PromptLoader
from app.core.state import ArenaState
from app.providers.request import ProviderRequest


class ArchitectAgent(BaseAgent):

    def __init__(self, provider, tool_executor = None):

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
            provider,
            tool_executor
        )

    def execute(self, state):
        template = PromptLoader.load("architect.md")

        prompt = template.format(
            query=state["user_query"]
        )

        request = ProviderRequest(
            prompt=prompt
        )

        response = self.provider.generate(request)

        reasoning = state.get("reasoning", {})

        reasoning[self.name] = response.text

        state["reasoning"] = reasoning

        return state

       