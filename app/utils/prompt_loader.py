from functools import lru_cache
from pathlib import Path


class PromptLoader:

    PROMPT_DIR = Path(__file__).resolve().parent.parent / "prompts"

    @classmethod
    @lru_cache(maxsize=None)
    def load(cls, filename: str) -> str:

        path = cls.PROMPT_DIR / filename

        return path.read_text(encoding="utf-8")