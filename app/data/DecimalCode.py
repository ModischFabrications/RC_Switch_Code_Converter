from dataclasses import dataclass


@dataclass
class DecimalCode:
    # could be a str instead
    code: int

    def __repr__(self) -> str:
        return f"{self.code}"
