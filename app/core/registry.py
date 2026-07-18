from typing import List

from agents.base_agent import BaseAgent


class AgentRegistry:
    """
    Stores and discovers agents.
    """

    def __init__(self):
        self._agents: List[BaseAgent] = []

    def register(self, agent: BaseAgent):

        self._agents.append(agent)

    def get_all(self):

        return self._agents

    def get_by_capability(self, capability: str):

        return [
            agent
            for agent in self._agents
            if capability.lower()
            in [c.lower() for c in agent.capabilities]
        ]

    def get_matching_agents(self, capabilities: List[str]):

        matched = []

        for capability in capabilities:

            matched.extend(self.get_by_capability(capability))

        # Remove duplicates

        unique = []

        seen = set()

        for agent in matched:

            if agent.name not in seen:

                unique.append(agent)

                seen.add(agent.name)

        return unique