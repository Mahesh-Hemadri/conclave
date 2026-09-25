from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):

    @property
    @abstractmethod
    def schema(self) -> dict:
        pass

    @abstractmethod
    def run(self, *args, **kwargs) -> Any:
        pass