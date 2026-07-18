from abc import ABC, abstractmethod

from app.core.state import ArenaState
from app.models.agent import AgentMetadata
from app.providers.base_provider import BaseProvider


class BaseAgent(ABC):

    def __init__(
        self,
        metadata: AgentMetadata,
        provider: BaseProvider,
    ):
        self.metadata = metadata
        self.provider = provider

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