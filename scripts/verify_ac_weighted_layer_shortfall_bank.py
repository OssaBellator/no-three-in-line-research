#!/usr/bin/env python3
from fractions import Fraction
import random


def main() -> None:
    rng = random.Random(1101)
    systems = 10_000
    layers = 0
    shortfall_layers = 0
    aggregate_shortfall = Fraction(0)
    local_shortfall = Fraction(0)
    paid = 0
    overloads = 0
    class_checks = 0

    for _ in range(systems):
        layer_count = rng.randint(1, 7)
        theta = Fraction(rng.randint(1, 5), rng.randint(2, 6))
        class_count = rng.randint(1, 5)
        balances = [Fraction(rng.randint(0, 20) + rng.randint(0, 8)) for _ in range(class_count)]
        reverse_loads = []
        degrees = []
        class_shortfall = [Fraction(0) for _ in range(class_count)]

        for _ in range(layer_count):
            reverse_load = rng.randint(1, 12)
            degree = rng.randint(0, 12)
            obstruction_class = rng.randrange(class_count)
            shortfall = max(Fraction(0), theta * reverse_load - degree)
            reverse_loads.append(reverse_load)
            degrees.append(degree)
            class_shortfall[obstruction_class] += shortfall
            layers += 1
            if shortfall > 0:
                shortfall_layers += 1

        aggregate = max(Fraction(0), theta * sum(reverse_loads) - sum(degrees))
        local = sum(class_shortfall)
        assert aggregate <= local
        aggregate_shortfall += aggregate
        local_shortfall += local
        class_checks += class_count

        if all(class_shortfall[j] <= balances[j] for j in range(class_count)):
            paid += 1
        else:
            overloads += 1
            assert any(class_shortfall[j] > balances[j] for j in range(class_count))

    print(f"systems={systems}")
    print(f"layers={layers}")
    print(f"shortfall_layers={shortfall_layers}")
    print(f"aggregate_shortfall={float(aggregate_shortfall):.6f}")
    print(f"local_shortfall={float(local_shortfall):.6f}")
    print(f"paid_systems={paid}")
    print(f"overload_systems={overloads}")
    print(f"class_checks={class_checks}")


if __name__ == "__main__":
    main()
