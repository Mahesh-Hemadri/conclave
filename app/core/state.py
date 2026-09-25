from typing import TypedDict, Dict, List


class ArenaState(TypedDict):
    """
    Shared state flowing through the entire reasoning graph.
    """

    # User input
    user_query: str

    # Planner output
    selected_experts: List[str]

    # Selected agents
    selected_agents: List[str]

    # Individual agent reasoning
    reasoning: Dict[str, str]
    
    execution_history: List[Dict]

    # Final synthesized answer
    final_answer: str