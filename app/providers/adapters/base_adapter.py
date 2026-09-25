from abc import ABC, abstractmethod


class BaseToolAdapter(ABC):

    @abstractmethod
    def build(self, tools) -> list:
        """
        Convert Conclave tools into
        provider-specific tool declarations.
        """
        pass