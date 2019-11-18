from dataclasses import dataclass


@dataclass(frozen=True)
class DecimalCode:
    # could be a str instead
    code: int

    def __post_init__(self):
        self.assert_valid()

    def assert_valid(self):
        # TODO: extend with proper tests (how?)
        if not (type(self.code) == int and self.code > 4):
            raise SyntaxError(f"Code [{self.code}] is invalid, int expected")

    def __str__(self) -> str:
        return f"{self.code}"
