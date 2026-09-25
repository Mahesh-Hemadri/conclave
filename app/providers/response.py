from dataclasses import dataclass
from typing import Optional


@dataclass
class ProviderResponse:

    text: str

    tool_call: Optional[dict] = None