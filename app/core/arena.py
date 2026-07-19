from app.agents.judge import JudgeAgent
from app.core.registry import AgentRegistry
from app.core.planner import Planner
from app.core.state import ArenaState
from app.engine.execution import ExecutionEngine
from app.providers.gemini_provider import GeminiProvider



class Arena:

    def __init__(self):

        self.registry = AgentRegistry()

        self.planner = Planner()
        self.engine = ExecutionEngine()
        provider = GeminiProvider()

        self.judge = JudgeAgent(provider)

    def register_agent(self, agent):

        self.registry.register(agent)

    


    def solve(self, query):

        available = self.registry.available_agents()

        required = self.planner.plan(
            query,
            available
        )

        agents = self.registry.get_selected_agents(required)

        state: ArenaState = {

            "user_query": query,

            "selected_experts": required,

            "selected_agents": [a.name for a in agents],

            "reasoning": {},

            "final_answer": "",
        }

        state = self.engine.run(
            state,
            agents
        )

        state = self.judge.execute(state)

        return state
    