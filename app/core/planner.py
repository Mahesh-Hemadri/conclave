import json

from app.providers.gemini_provider import GeminiProvider

class Planner:

    def __init__(self):

        self.provider = GeminiProvider()
        
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

        prompt = f"""
You are the planning agent for an AI software engineering team.

Available experts:

{agent_context}

User request:

{query}

Your task is to decide which experts are needed.

Return ONLY a JSON array.

Example:

["Architect","Backend"]

Return only JSON.
"""

        response = self.provider.generate(prompt)

        print("Planner Response:", response)

        try:
            return json.loads(response)

        except Exception:

            return []

    