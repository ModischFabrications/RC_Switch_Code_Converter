import argparse
import sys
from typing import Tuple

from app import converter
from app.data.DecimalCode import DecimalCode
from app.data.DipCode import DipCode


def parse_args() -> Tuple[int, str]:
    parser = argparse.ArgumentParser(description="Convert between common code formats for 433 MHz socket libraries")
    parser.add_argument("-d", "--decimal", type=int,
                        help="Input Decimals, will be converted to switches, e.g.: 4457809")
    parser.add_argument("-s", "--switches", type=str,
                        help="DIP codes, will be converted to decimals. "
                             "Expects 'SYSTEM|DEVICE[|STATE]', e.g.: 01011|1 or 01011|1|1")

    args = parser.parse_args()

    return args.decimal, args.switches


def main():
    decimals, switches = parse_args()

    if decimals is not None and switches is not None:
        raise ValueError("Can't pass both decimals and switches")

    if decimals is None and switches is None:
        raise ValueError("Need at least decimals or switches")

    if decimals:
        decimal_code = DecimalCode(decimals)
        print(converter.to_dip(decimal_code))

    if switches:
        # INPUT: 10101|000100 or 10101|000100|1
        n_params = switches.count("|")

        if n_params == 1:
            system, device = switches.split("|")
            on = DipCode(system, int(device), True)
            on_decimals = converter.to_decimal(on)
            off = DipCode(system, int(device), False)
            off_decimals = converter.to_decimal(off)
            print(f"ON: {on_decimals},\nOFF: {off_decimals}")
        elif n_params == 2:
            system, device, state = switches.split("|")
            print(converter.to_decimal(DipCode(system, int(device), bool(state))))
        else:
            raise ValueError("Invalid number of parts for switches")

    return 0


if __name__ == '__main__':
    sys.exit(main())
