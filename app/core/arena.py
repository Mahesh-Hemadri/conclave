from app.core.registry import AgentRegistry
from app.core.planner import Planner
from app.core.state import ArenaState
from app.engine.execution import ExecutionEngine

class Arena:

    def __init__(self):

        self.registry = AgentRegistry()

        self.planner = Planner()
        self.engine = ExecutionEngine()

    def register_agent(self, agent):

        self.registry.register(agent)

    from app.core.state import ArenaState


    def solve(self, query):

        required = self.planner.plan(query)

        agents = self.registry.get_matching_agents(required)

        state: ArenaState = {

            "user_query": query,

            "required_capabilities": required,

            "selected_agents": [a.name for a in agents],

            "reasoning": {},

            "final_answer": "",
        }

        state = self.engine.run(
            state,
            agents
        )

        return state