from app.agents.judge import JudgeAgent
from app.core.registry import AgentRegistry
from app.core.planner import Planner
from app.core.state import ArenaState
from app.engine.execution import ExecutionEngine
from app.providers.gemini_provider import GeminiProvider
from app.tools.registry import ToolRegistry
from app.tools.executor import ToolExecutor
from app.tools.calculator import CalculatorTool



class Arena:

    def __init__(self):

        self.registry = AgentRegistry()

        # Tool infrastructure
        self.tool_registry = ToolRegistry()

        self.tool_registry.register(
            CalculatorTool()
        )

        self.tool_executor = ToolExecutor(
            self.tool_registry
        )

        # Shared LLM provider
        self.provider = GeminiProvider(
            self.tool_registry,
            self.tool_executor
        )

        # Core components
        self.planner = Planner(
            self.provider
        )

        self.engine = ExecutionEngine()

        # Judge
        self.judge = JudgeAgent(
            self.provider
        )

    def register_agent(self, agent):

        self.registry.register(agent)

    


    def solve(self, query):

        available = self.registry.available_agents()

        required = self.planner.plan(
            query,
            available
        )

        # Handle planner failure explicitly
        if not required:
            return {
                "user_query": query,
                "selected_experts": [],
                "selected_agents": [],
                "reasoning": {},
                "execution_history": [],
                "final_answer": "Unable to generate a valid execution plan."
            }

        agents = self.registry.get_selected_agents(required)

        state: ArenaState = {

            "user_query": query,

            "selected_experts": required,

            "selected_agents": [a.name for a in agents],

            "reasoning": {},
            
            "execution_history": [],

            "final_answer": "",
        }

        state = self.engine.run(
            state,
            agents
        )

        state = self.judge.execute(state)

        return state