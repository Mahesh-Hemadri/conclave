import json

from app.providers.request import ProviderRequest
from app.utils.prompt_loader import PromptLoader
class Planner:

    def __init__(self, provider):

        self.provider = provider
        
    def format_agents(self, available_agents):

        formatted = []

        for agent in available_agents:

            formatted.append(
                f"""
    Expert: {agent['name']}
    Role: {agent['role']}
    Description: {agent['description']}
    """
            )

        return "\n".join(formatted)
        
    def plan(self, query, available_agents):
        agent_context = self.format_agents(available_agents)

        template = PromptLoader.load("planner.md")

        prompt = template.format(
            available_agents=agent_context,
            query=query
        )

        request = ProviderRequest(
            prompt=prompt
        )

        response = self.provider.generate(request)

        print("Planner Response:", response.text)

        try:
            return json.loads(response.text)

        except Exception:

            return []

    