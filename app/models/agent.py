from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class AgentMetadata:
    """
    Metadata describing an AI agent.
    """

    name: str
    role: str
    description: str

    capabilities: List[str]

    priority: int = 1

    confidence: float = 1.0

    provider: str = "gemini"

    prompt: Optional[str] = None

    tools: List[str] = field(default_factory=list)