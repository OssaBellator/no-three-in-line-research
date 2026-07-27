#!/usr/bin/env python3
"""Verify GC4q--GC4t: union payment versus weighted Hall deficiency."""

from fractions import Fraction
from itertools import product


def check_instance(demands, capacities, incidence, reuse, kappa, eta):
    operation_count = len(demands)
    factor_count = len(capacities)
    p = [
        sum(capacities[f] for f in range(factor_count) if incidence[y][f])
        for y in range(operation_count)
    ]
    total_demand = sum(demands)
    incidence_mass = sum(p)
    union_capacity = sum(
        capacities[f]
        for f in range(factor_count)
        if any(incidence[y][f] for y in range(operation_count))
    )

    if reuse:
        assert incidence_mass <= reuse * union_capacity

    threshold = eta * total_demand / kappa
    if incidence_mass >= threshold:
        assert union_capacity >= eta * total_demand / (reuse * kappa)
        return "payment"

    scaled_demand = total_demand / kappa
    deficiency = scaled_demand - union_capacity
    assert deficiency > (1 - eta) * total_demand / kappa
    return "deficiency"


def exhaustive():
    payment = deficiency = checks = 0
    kappa = Fraction(2)
    eta = Fraction(1, 2)
    for operation_count in (1, 2, 3):
        for factor_count in (1, 2, 3):
            for capacities in product((Fraction(1), Fraction(2)), repeat=factor_count):
                for demands in product((Fraction(1), Fraction(2), Fraction(3)), repeat=operation_count):
                    for bits in product((0, 1), repeat=operation_count * factor_count):
                        incidence = [
                            list(bits[y * factor_count:(y + 1) * factor_count])
                            for y in range(operation_count)
                        ]
                        multiplicities = [
                            sum(incidence[y][f] for y in range(operation_count))
                            for f in range(factor_count)
                        ]
                        reuse = max(multiplicities, default=1)
                        if reuse == 0:
                            reuse = 1
                        result = check_instance(
                            demands, capacities, incidence, reuse, kappa, eta
                        )
                        payment += result == "payment"
                        deficiency += result == "deficiency"
                        checks += 1
    return checks, payment, deficiency


def main():
    checks, payment, deficiency = exhaustive()
    print(
        "Geometric same-token Hall router: verified "
        f"{checks} weighted incidence systems "
        f"({payment} payment, {deficiency} deficiency)"
    )


if __name__ == "__main__":
    main()
