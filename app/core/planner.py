class Planner:

    """
    Decides what capabilities
    are required.
    """

    def plan(self, query: str):

        query = query.lower()

        capabilities = []

        if "architecture" in query:

            capabilities.append("architecture")

        if "api" in query:

            capabilities.append("backend")

        if "security" in query:

            capabilities.append("security")

        return capabilities