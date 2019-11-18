from dataclasses import dataclass


@dataclass(frozen=True)
class DecimalCode:
    # could be a str instead
    code: int

    def __str__(self) -> str:
        return f"{self.code}"
