from typing import List

from app.runners.base_runner import BaseRunner
from app.core.state import ArenaState
from app.agents.base_agent import BaseAgent


class ParallelRunner(BaseRunner):

    def run(
        self,
        state: ArenaState,
        agents: List[BaseAgent]
    ) -> ArenaState:

        # Placeholder until we implement true parallel execution
        raise NotImplementedError("ParallelRunner is not implemented yet.")