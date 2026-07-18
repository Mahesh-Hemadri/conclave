from app.agents.base_agent import BaseAgent
from app.core.state import ArenaState
from app.models.agent import AgentMetadata


class JudgeAgent(BaseAgent):

    def __init__(self, provider):

        super().__init__(
            AgentMetadata(
                name="Judge",
                role="AI Judge",
                description="Synthesizes all agent responses.",
                capabilities=["judge"],
            ),
            provider
        )

    def execute(self, state):

        prompt = f"""
You are the Lead Software Architect.

Combine the following expert opinions into ONE final recommendation.

{state["reasoning"]}
"""

        state["final_answer"] = self.provider.generate(prompt)

        return state