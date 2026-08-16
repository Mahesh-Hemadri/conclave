from app.tools.base_tool import BaseTool


class ToolRegistry:

    def __init__(self):

        self.tools = {}

    def register(self, tool: BaseTool):

        self.tools[
            tool.schema["name"]
        ] = tool

    def get(self, name: str):

        return self.tools.get(name)
    
    def all(self):
        return list(self.tools.values())

    def available(self):

        return list(self.tools.keys())

    def schemas(self):

        return [
            tool.schema
            for tool in self.tools.values()
        ]