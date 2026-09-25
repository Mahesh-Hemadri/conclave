from app.core.arena import Arena

from app.agents.architect import ArchitectAgent
from app.agents.backend import BackendAgent
from app.agents.security import SecurityAgent

arena = Arena()

arena.register_agent(ArchitectAgent(arena.provider))
arena.register_agent(BackendAgent(arena.provider))
arena.register_agent(SecurityAgent(arena.provider))

state = arena.solve(
    "Design a secure backend API architecture"
)

print()

print("\n" + "=" * 60)
print("FINAL ANSWER")
print("=" * 60)
print(state["final_answer"])

print("\nExecution Timeline")
print("-" * 40)

for item in state["execution_history"]:
    print(f"{item['agent']} : {item['duration']} sec")