from dataclasses import dataclass


@dataclass
class AgentResult:
    """
    Represents the output produced by a single expert agent.
    """

    agent_name: str
    reasoning: str
    duration: float