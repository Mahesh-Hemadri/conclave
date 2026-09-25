from typing import Any

from app.tools.base_tool import BaseTool


class CalculatorTool(BaseTool):

    @property
    def schema(self):

        return {
            "name": "calculator",
            "description": "Performs arithmetic calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Arithmetic expression to evaluate."
                    }
                },
                "required": [
                    "expression"
                ]
            }
        }

    def run(self, expression: str, **kwargs) -> Any:

        try:
            return eval(expression)

        except Exception as e:
            return str(e)