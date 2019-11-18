from app.data.DecimalCode import DecimalCode
from app.data.DipCode import DipCode

d_state = {True: "01", False: "10"}


def to_decimal(dip_code: DipCode) -> DecimalCode:
    inverted_system = _invert(dip_code.system)

    # could be doing all at once but this shows the algorithm better
    device_bits = "1" + ((dip_code.device - 1) * "0")
    lpad_device_bits = device_bits.zfill(5)
    mirrored_lpad_device_bits = lpad_device_bits[::-1]
    inverted_device = _invert(mirrored_lpad_device_bits)

    state = d_state[dip_code.state]

    concat = inverted_system + inverted_device + state
    binary = _pad_with_zeros(concat)

    # must be 24 bits
    assert len(binary) == 24

    code = DecimalCode(int(binary, 2))

    return code


def _pad_with_zeros(pre_pad: str) -> str:
    out = ""
    for c in pre_pad:
        out += "0" + c

    return out


def _strip_zeros(padded: str) -> str:
    if not all(bit == "0" for bit in padded[::2]):
        raise ValueError("non-zero value stripped!")

    # skip every second 0
    return padded[1::2]


def _invert(bits: str) -> str:
    out = ""
    for b in bits:
        if b != "1" and b != "0":
            raise ValueError(f"invalid bit: {b}")
        out += str(int(not bool(int(b))))

    return out


def to_dip(decimal_code: DecimalCode) -> DipCode:
    binary = bin(decimal_code.code)

    return DipCode("10101", 1, True)
