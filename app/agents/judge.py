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

You have received responses from multiple experts.

Your responsibilities:

- Merge the responses.
- Remove duplicate information.
- Resolve any conflicting recommendations.
- Organize the answer into clear sections.
- Produce a professional final recommendation.

Expert Responses:

{state["reasoning"]}

Return only the final answer.
"""

        state["final_answer"] = self.provider.generate(prompt)

        return state