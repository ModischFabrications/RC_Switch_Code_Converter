from app.data.DecimalCode import DecimalCode
from app.data.DipCode import DipCode


def to_decimal(dip_code: DipCode) -> DecimalCode:
    return DecimalCode(42)


def to_dip(decimal_code: DecimalCode) -> DipCode:
    return DipCode("10101", "1", True)
