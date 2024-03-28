from typing import Any, Optional

class Token:
    def __init__(self, type: str, value: Optional[Any] = None) -> None:
        self.type: str = type
        self.value: Optional[Any] = value

    def __repr__(self) -> str:
        if self.value is not None:
            return f"{self.type}:{self.value}"
        return str(self.type)
