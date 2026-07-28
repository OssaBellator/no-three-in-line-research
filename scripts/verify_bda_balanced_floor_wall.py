#!/usr/bin/env python3
"""Finite audit for BDA5bq--BDA5bu."""

from itertools import product


def main() -> None:
    cycles = restorations = 0

    for q in range(2, 6):
        for bound in range(1, 4):
            values = range(-4, 9)
            for length in range(2, 6):
                for increments in product(range(-bound, bound + 1), repeat=length):
                    if sum(increments) != 0 or all(step == 0 for step in increments):
                        continue

                    for start in values:
                        numerators = [start]
                        for step in increments:
                            numerators.append(numerators[-1] + step)
                        if any(value not in values for value in numerators):
                            continue

                        floors = [value // q for value in numerators[:-1]]
                        if len(set(floors)) == 1:
                            continue

                        cycles += 1
                        minimum = min(floors)
                        exits = [
                            t
                            for t in range(length)
                            if floors[t] == minimum and numerators[t + 1] // q != minimum
                        ]
                        assert exits
                        first_exit = exits[0]

                        restoration = None
                        for distance in range(1, length + 1):
                            t = (first_exit + distance) % length
                            if numerators[t] // q != minimum and numerators[t + 1] // q == minimum:
                                restoration = t
                                break
                        assert restoration is not None

                        before = numerators[restoration]
                        after = numerators[restoration + 1]
                        step = after - before
                        overshoot = before - (minimum + 1) * q

                        assert -bound <= step <= -1
                        assert 0 <= overshoot <= bound - 1
                        assert minimum * q <= after <= (minimum + 1) * q - 1
                        restorations += 1

                        # A nonconstant closed numerator word cannot be one-sided monotone.
                        assert not all(step >= 0 for step in increments)
                        assert not all(step <= 0 for step in increments)

    assert cycles == 69686
    assert restorations == cycles
    print(
        "balanced-floor wall audit passed:",
        f"{cycles} exact cycles and {restorations} bounded restoration crossings",
    )


if __name__ == "__main__":
    main()
