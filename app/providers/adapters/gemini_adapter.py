from google.genai import types

from app.providers.adapters.base_adapter import BaseToolAdapter


class GeminiToolAdapter(BaseToolAdapter):

    def build(self, tools) -> list:

        declarations = []

        for tool in tools:

            schema = tool.schema

            declarations.append(
                types.FunctionDeclaration(
                    name=schema["name"],
                    description=schema["description"],
                    parameters=schema["parameters"],
                )
            )

        return declarations