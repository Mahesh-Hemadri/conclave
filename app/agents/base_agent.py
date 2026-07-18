from abc import ABC, abstractmethod
from typing import List

from core.state import ArenaState


class BaseAgent(ABC):
    """
    Base class for every agent inside Conclave.
    """

    def __init__(
        self,
        name: str,
        role: str,
        capabilities: List[str],
    ):
        self.name = name
        self.role = role
        self.capabilities = capabilities

    @abstractmethod
    def execute(self, state: ArenaState) -> ArenaState:
        """
        Execute the agent's reasoning.

        Must return a dictionary that updates the shared state.
        """
        pass

    def __repr__(self):
        return f"{self.name} ({self.role})"