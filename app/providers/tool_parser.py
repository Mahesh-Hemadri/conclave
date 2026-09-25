import json


class ToolParser:

    @staticmethod
    def parse(text: str):

        try:

            data = json.loads(text)

            if (
                isinstance(data, dict)
                and "tool" in data
                and "arguments" in data
            ):
                return data

        except Exception:
            pass

        return None