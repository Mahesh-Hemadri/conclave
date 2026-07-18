from core.arena import Arena

from agents.architect import ArchitectAgent
from agents.backend import BackendAgent
from agents.security import SecurityAgent


arena = Arena()

arena.register_agent(ArchitectAgent())
arena.register_agent(BackendAgent())
arena.register_agent(SecurityAgent())

state = arena.solve(
    "Design a secure backend API architecture"
)

print()

print(state)