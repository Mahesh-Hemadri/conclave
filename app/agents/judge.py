from app.agents.base_agent import BaseAgent
from app.core.state import ArenaState
from app.models.agent import AgentMetadata
from app.providers import request
from app.utils.prompt_loader import PromptLoader
from app.providers.request import ProviderRequest

class JudgeAgent(BaseAgent):

    def __init__(self, provider, tool_executor = None):

        super().__init__(
            AgentMetadata(
                name="Judge",
                role="AI Judge",
                description="Synthesizes all agent responses.",
                capabilities=["judge"],
            ),
            provider,
            tool_executor
        )

    def execute(self, state):

        template = PromptLoader.load("judge.md")

        prompt = template.format(
            reasoning=state["reasoning"]
        )
        request = ProviderRequest(
            prompt=prompt
        )

        response = self.provider.generate(request)

        state["final_answer"] = response.text

        return state