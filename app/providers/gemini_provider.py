import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from app.providers.adapters.gemini_adapter import GeminiToolAdapter
from app.providers.base_provider import BaseProvider
from app.providers.request import ProviderRequest
from app.providers.response import ProviderResponse


load_dotenv()


class GeminiProvider(BaseProvider):

    def __init__(self, tool_registry, tool_executor):

        self.tool_registry = tool_registry
        self.tool_executor = tool_executor
        self.tool_adapter = GeminiToolAdapter()

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = os.getenv(
            "GEMINI_MODEL",
            "gemini-3.5-flash"
        )

    def generate(self, request: ProviderRequest) -> ProviderResponse:

        tool_declarations = self.tool_adapter.build(
            self.tool_registry.all()
        )

        config = types.GenerateContentConfig(
            tools=[
                types.Tool(
                    function_declarations=tool_declarations
                )
            ]
        )

        # Use a generic list here because Gemini accepts
        # multiple content types during the tool-calling loop.
        contents: list = [
            request.prompt
        ]

        max_tool_rounds = 5

        for _ in range(max_tool_rounds):

            response = self.client.models.generate_content(
                model=self.model,
                contents=contents,
                config=config
            )

            print("\nGemini Response:")
            print(response.text)

            if not response.candidates:
                return ProviderResponse(
                    text="Error: Gemini returned no candidates.",
                    tool_call=None
                )

            candidate = response.candidates[0]

            if candidate.content is None:
                return ProviderResponse(
                    text=response.text or "",
                    tool_call=None
                )

            model_content = candidate.content

            if not model_content.parts:
                return ProviderResponse(
                    text=response.text or "",
                    tool_call=None
                )

            function_calls = []

            for part in model_content.parts:

                if part.function_call is not None:
                    function_calls.append(
                        part.function_call
                    )

            # No function call means Gemini has produced
            # the final answer.
            if not function_calls:

                return ProviderResponse(
                    text=response.text or "",
                    tool_call=None
                )

            # Preserve Gemini's function-call message.
            contents.append(
                model_content
            )

            function_response_parts = []

            for function_call in function_calls:

                tool_name = function_call.name

                arguments = dict(
                    function_call.args
                )

                

                tool_call = {
                    "tool": tool_name,
                    "arguments": arguments
                }

                try:

                    tool_result = self.tool_executor.execute(
                        tool_call
                    )

                except Exception as exc:

                    tool_result = {
                        "error": str(exc)
                    }

                print(
                    f"Tool Result: {tool_result}"
                )

                function_response_parts.append(
                    types.Part.from_function_response(
                        name=tool_name,
                        response={
                            "result": tool_result
                        }
                    )
                )

            # Send the tool results back to Gemini.
            contents.append(
                types.Content(
                    role="user",
                    parts=function_response_parts
                )
            )

        return ProviderResponse(
            text="Error: Maximum tool-calling rounds exceeded.",
            tool_call=None
        )