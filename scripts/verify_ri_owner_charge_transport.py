#!/usr/bin/env python3
import random


def maximum_hall_deficit(demands, capacities, neighbourhoods):
    owner_count = len(demands)
    best_deficit = 0
    best_mask = 0
    for mask in range(1, 1 << owner_count):
        demand = sum(demands[i] for i in range(owner_count) if (mask >> i) & 1)
        sources = set()
        for i in range(owner_count):
            if (mask >> i) & 1:
                sources.update(neighbourhoods[i])
        capacity = sum(capacities[j] for j in sources)
        deficit = demand - capacity
        if deficit > best_deficit:
            best_deficit = deficit
            best_mask = mask
    return best_deficit, best_mask


def main() -> None:
    rng = random.Random(1103)
    systems = 8_000
    owner_source_arcs = 0
    charge_units = 0
    paid_systems = 0
    deficient_systems = 0
    unpaid_units = 0
    hall_checks = 0

    for _ in range(systems):
        owner_count = rng.randint(1, 6)
        source_count = rng.randint(1, 6)
        demands = [rng.randint(0, 7) for _ in range(owner_count)]
        capacities = [rng.randint(0, 8) for _ in range(source_count)]
        neighbourhoods = []
        for _ in range(owner_count):
            neighbourhoods.append({j for j in range(source_count) if rng.random() < 0.45})

        deficit, mask = maximum_hall_deficit(demands, capacities, neighbourhoods)
        hall_checks += (1 << owner_count) - 1
        owner_source_arcs += sum(len(neighbourhood) for neighbourhood in neighbourhoods)
        charge_units += sum(demands)

        if deficit == 0:
            paid_systems += 1
        else:
            deficient_systems += 1
            unpaid_units += deficit
            demand = sum(demands[i] for i in range(owner_count) if (mask >> i) & 1)
            sources = set()
            for i in range(owner_count):
                if (mask >> i) & 1:
                    sources.update(neighbourhoods[i])
            assert demand - sum(capacities[j] for j in sources) == deficit

    print(f"systems={systems}")
    print(f"owner_source_arcs={owner_source_arcs}")
    print(f"charge_units={charge_units}")
    print(f"paid_systems={paid_systems}")
    print(f"deficient_systems={deficient_systems}")
    print(f"unpaid_units={unpaid_units}")
    print(f"hall_checks={hall_checks}")


if __name__ == "__main__":
    main()
