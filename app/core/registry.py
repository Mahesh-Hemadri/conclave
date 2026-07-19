from typing import List

from app.agents.base_agent import BaseAgent


class AgentRegistry:
    """
    Stores and discovers agents.
    """

    def __init__(self, provider=None):
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

    def get_matching_agents(self, agent_names: List[str]):

        matched = []

        for agent in self._agents:

            if agent.name.lower() in [name.lower() for name in agent_names]:
                matched.append(agent)

        return matched
    
    def available_capabilities(self):

        capabilities = set()

        for agent in self._agents:

            capabilities.update(agent.capabilities)

        return sorted(capabilities)
    
    def available_agents(self):

        agents = []

        for agent in self._agents:

            agents.append(
                {
                    "name": agent.name,
                    "role": agent.role,
                    "description": agent.metadata.description,
                }
            )

        return agents