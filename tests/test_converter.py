from app import converter
from app.data.DecimalCode import DecimalCode
from app.data.DipCode import DipCode


def test_to_decimal():
    target_code = DecimalCode(4474193)
    source_code = DipCode("01010", "1", True)

    converted_code = converter.to_decimal(source_code)

    assert converted_code == target_code


def test_to_dips():
    target_code = DipCode("01010", "1", True)
    source_code = DecimalCode(4474193)

    converted_code = converter.to_dip(source_code)

    assert converted_code == target_code


def test_roundtrip():
    dip = DipCode("01010", "1", True)

    decimal = converter.to_decimal(dip)
    new_dip = converter.to_dip(decimal)

    assert new_dip == dip
