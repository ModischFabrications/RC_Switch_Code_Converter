import re
from dataclasses import dataclass

system_pattern = re.compile('[01]{5}')

@dataclass(frozen=True)
class DipCode:
    # couldn't be represented as ints because of leading 0
    system: str
    device: int
    state: bool

    def __post_init__(self):
        self.assert_valid()

    def assert_valid(self):
        if not system_pattern.match(self.system):
            raise SyntaxError(f"System code [{self.system}] is invalid, str expected")
        if not (type(self.device) == int and 0 < self.device <= 5):
            raise SyntaxError(f"device code [{self.device}] is invalid, int expected")
        if not type(self.state) == bool:
            raise SyntaxError(f"state [{self.state}] is invalid, bool expected")

    def __str__(self) -> str:
        return f"{self.system}, {self.device}, {int(self.state)}"
