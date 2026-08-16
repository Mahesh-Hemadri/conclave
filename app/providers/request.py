from dataclasses import dataclass
from typing import Optional


@dataclass
class ProviderRequest:

    prompt: str

    system_prompt: Optional[str] = None

    tools: Optional[list] = None

    temperature: float = 0.2

    max_tokens: int = 2048