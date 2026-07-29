#!/usr/bin/env python3
from __future__ import annotations

import math
import random


def main() -> None:
    rng = random.Random(1414)
    vector_count = 0
    unit_period_sum = 0
    combined_period_sum = 0

    for _ in range(25000):
        moduli = [rng.randint(2, 12) for _ in range(rng.randint(1, 4))]
        step = [rng.randrange(modulus) for modulus in moduli]

        period = 1
        for modulus, value in zip(moduli, step):
            coordinate_period = modulus // math.gcd(modulus, value) if value else 1
            period = math.lcm(period, coordinate_period)

        assert all((period * value) % modulus == 0 for modulus, value in zip(moduli, step))
        for time in range(1, period):
            assert not all((time * value) % modulus == 0 for modulus, value in zip(moduli, step))

        holonomy_period = rng.randint(1, 20)
        combined_period = math.lcm(period, holonomy_period)
        assert combined_period % period == 0
        assert combined_period % holonomy_period == 0

        vector_count += 1
        unit_period_sum += period
        combined_period_sum += combined_period

    print(f"unit_vectors={vector_count}")
    print(f"total_unit_period={unit_period_sum}")
    print(f"total_combined_period={combined_period_sum}")


if __name__ == "__main__":
    main()
