"""Groq client placeholder."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GroqClient:
    model: str = "llama-3.1-70b-versatile"

    def generate(self, prompt: str) -> str:
        return f"{self.model}: {prompt}"
