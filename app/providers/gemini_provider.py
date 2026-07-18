import os

from dotenv import load_dotenv
from google import genai

from app.providers.base_provider import BaseProvider

load_dotenv()


class GeminiProvider(BaseProvider):

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = os.getenv(
            "GEMINI_MODEL",
            "gemini-3.5-flash"
        )

    def generate(self, prompt: str) -> str:

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text or "Error: No response from Gemini API."