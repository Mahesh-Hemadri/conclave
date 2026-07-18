from typing import List

from app.agents.base_agent import BaseAgent
from app.core.state import ArenaState


class ExecutionEngine:
    """
    Executes agents and maintains the shared reasoning state.
    """

    def run(
        self,
        state: ArenaState,
        agents: List[BaseAgent]
    ) -> ArenaState:

        print("\nExecution Started\n")

        for agent in agents:

            print(f"Running {agent.name}")

            state = agent.execute(state)

        print("\nExecution Finished\n")

        return state