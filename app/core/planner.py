import json

from app.providers.gemini_provider import GeminiProvider

class Planner:

    def __init__(self):

        self.provider = GeminiProvider()
        
    def plan(self, query, available_agents):

        prompt = f"""
You are the planning agent for an AI software engineering team.

Available experts:

{available_agents}

User request:

{query}

Your job is to decide which experts are required.

Return ONLY a JSON array containing the expert names.

Example:

["Architect", "Backend"]

Do not explain.
Return only valid JSON.
"""

        response = self.provider.generate(prompt)

        print("Planner Response:", response)

        try:
            return json.loads(response)

        except Exception:

            return []

    