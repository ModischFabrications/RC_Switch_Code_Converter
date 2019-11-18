from dataclasses import dataclass


@dataclass(frozen=True)
class DipCode:
    # couldn't be represented as ints because of leading 0
    system: str
    device: str
    state: bool

    def __str__(self) -> str:
        return f"{self.system}, {self.device}, {int(self.state)}"
