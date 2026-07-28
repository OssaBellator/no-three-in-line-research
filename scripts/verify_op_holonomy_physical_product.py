#!/usr/bin/env python3
"""Finite audit for OP4an--OP4ar."""

from itertools import product
from math import gcd, lcm


def main() -> None:
    vectors = checked_returns = combined_states = 0

    for component_count in range(1, 4):
        for moduli in product(range(2, 8), repeat=component_count):
            for holonomy in product(*[range(modulus) for modulus in moduli]):
                component_orders = [
                    1 if value == 0 else modulus // gcd(modulus, value)
                    for modulus, value in zip(moduli, holonomy)
                ]
                simultaneous_order = 1
                for order in component_orders:
                    simultaneous_order = lcm(simultaneous_order, order)

                brute_return = None
                for repetition in range(1, simultaneous_order + 1):
                    if all(
                        repetition * value % modulus == 0
                        for modulus, value in zip(moduli, holonomy)
                    ):
                        brute_return = repetition
                        break
                assert brute_return == simultaneous_order

                for repetition in range(1, simultaneous_order):
                    assert any(
                        repetition * value % modulus != 0
                        for modulus, value in zip(moduli, holonomy)
                    )

                vectors += 1
                checked_returns += 1
                for physical_stock in range(1, 5):
                    combined_states += physical_stock * simultaneous_order

    assert vectors == 20439
    assert checked_returns == vectors
    assert combined_states == 5615980
    print(
        "holonomy physical-product audit passed:",
        f"{vectors} vectors and {combined_states} combined-state slots",
    )


if __name__ == "__main__":
    main()
