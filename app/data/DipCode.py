from dataclasses import dataclass


@dataclass
class DipCode:
    system: str
    device: str
    state: bool
