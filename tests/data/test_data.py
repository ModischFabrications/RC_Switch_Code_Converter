from app.data.DecimalCode import DecimalCode
from app.data.DipCode import DipCode


def test_decimal_code_init():
    decimal = DecimalCode(42)

    assert decimal is not None
    assert str(decimal) == "42"


def test_dip_code_init():
    dip = DipCode("10101", 1, True)

    assert dip is not None
    assert str(dip) == "10101, 1, 1"
