from abc import ABC, abstractmethod

from app.core.state import ArenaState
from app.models.agent import AgentMetadata


class BaseAgent(ABC):
    """
    Base class for every Conclave agent.
    """

    def __init__(self, metadata: AgentMetadata):
        self.metadata = metadata

    @property
    def name(self):
        return self.metadata.name

    @property
    def role(self):
        return self.metadata.role

    @property
    def capabilities(self):
        return self.metadata.capabilities

    @abstractmethod
    def execute(self, state: ArenaState) -> ArenaState:
        pass

    def __repr__(self):
        return f"{self.name} ({self.role})"