class ToolExecutor:

    def __init__(self, registry):

        self.registry = registry

    def execute(self, tool_call: dict):

        tool_name = tool_call["tool"]

        arguments = tool_call["arguments"]

        tool = self.registry.get(tool_name)

        if tool is None:

            raise ValueError(
                f"Unknown tool: {tool_name}"
            )

        return tool.run(
            **arguments
        )