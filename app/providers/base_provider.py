from abc import ABC, abstractmethod
from app.providers.request import ProviderRequest
from app.providers.response import ProviderResponse


class BaseProvider(ABC):

    @abstractmethod
    def generate(
        self,
        request: ProviderRequest
    ) -> ProviderResponse:
        pass