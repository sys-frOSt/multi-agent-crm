"""Backend application entry point."""

from __future__ import annotations

from .api.chat import chat


def main() -> None:
    print(chat("hello"))


if __name__ == "__main__":
    main()
