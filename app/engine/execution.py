from typing import List
import time
from app.runners.sequential_runner import SequentialRunner
from app.agents.base_agent import BaseAgent
from app.core.state import ArenaState


class ExecutionEngine:
    """
    Executes agents and maintains the shared reasoning state.
    """
    def __init__(self):

        self.runner = SequentialRunner()
    

    def run(
        self,
        state: ArenaState,
        agents: List[BaseAgent]
    ) -> ArenaState:

        print("\nExecution Started\n")

        state = self.runner.run(
            state,
            agents
        )

        print("\nExecution Finished\n")

        return state