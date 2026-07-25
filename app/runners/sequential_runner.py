from typing import List
import time

from app.runners.base_runner import BaseRunner
from app.core.state import ArenaState
from app.agents.base_agent import BaseAgent


class SequentialRunner(BaseRunner):

    def run(
        self,
        state: ArenaState,
        agents: List[BaseAgent]
    ) -> ArenaState:

        for agent in agents:

            print(f"Running {agent.name}")

            start = time.perf_counter()

            state = agent.execute(state)

            duration = time.perf_counter() - start

            print(f"{agent.name} finished in {duration:.2f} seconds")

            state["execution_history"].append(
                {
                    "agent": agent.name,
                    "duration": round(duration, 2)
                }
            )

        return state