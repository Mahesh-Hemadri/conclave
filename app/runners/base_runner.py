from abc import ABC, abstractmethod
from typing import List

from app.core.state import ArenaState
from app.agents.base_agent import BaseAgent


class BaseRunner(ABC):

    @abstractmethod
    def run(
        self,
        state: ArenaState,
        agents: List[BaseAgent]
    ) -> ArenaState:
        """
        Execute the provided agents using the runner's strategy.
        """
        pass