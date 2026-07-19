from app.agents.judge import JudgeAgent
from app.core.arena import Arena

from app.agents.architect import ArchitectAgent
from app.agents.backend import BackendAgent
from app.agents.security import SecurityAgent
from app.providers.gemini_provider import GeminiProvider


arena = Arena()

provider = GeminiProvider()

arena.register_agent(ArchitectAgent(provider))
arena.register_agent(BackendAgent(provider))
arena.register_agent(SecurityAgent(provider))
arena.register_agent(JudgeAgent(provider))

state = arena.solve(
    "Design a secure backend API architecture"
)

print()

print("\n" + "=" * 60)
print("FINAL ANSWER")
print("=" * 60)
print(state["final_answer"])