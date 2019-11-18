from dataclasses import dataclass


@dataclass
class DipCode:
    # could be represented as ints but why?
    system: str
    device: str
    state: bool

    def __repr__(self) -> str:
        return f"{self.system}, {self.device}, {int(self.state)}"
