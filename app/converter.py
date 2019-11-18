from app.data.DecimalCode import DecimalCode
from app.data.DipCode import DipCode

state_to_code = {True: "01", False: "10"}
code_to_state = {v: k for k, v in state_to_code.items()}


def to_decimal(dip_code: DipCode) -> DecimalCode:
    inverted_system = _invert(dip_code.system)

    # could be doing all at once but this shows the algorithm better
    device_bits = "1" + ((dip_code.device - 1) * "0")
    lpad_device_bits = device_bits.zfill(5)
    mirrored_lpad_device_bits = lpad_device_bits[::-1]
    inverted_device = _invert(mirrored_lpad_device_bits)

    state = state_to_code[dip_code.state]

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
    cleaned_binary = binary.lstrip("0b").zfill(24)
    stripped_binary = _strip_zeros(cleaned_binary)

    system = _invert(stripped_binary[0:5])

    device_bits = _invert(stripped_binary[5:10])
    device = device_bits.index("1") + 1

    status_bits = stripped_binary[10:12]
    status = code_to_state[status_bits]

    return DipCode(system, device, status)
