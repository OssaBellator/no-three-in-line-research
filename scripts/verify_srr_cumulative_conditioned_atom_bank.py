import math
import random


def main():
    rng = random.Random(1506)
    systems = 6000
    totals = {
        "epochs": 0,
        "atoms": 0,
        "candidate_weight": 0,
        "reference_burden": 0,
        "removed_burden": 0,
        "added_burden": 0,
        "capacity_deposits": 0,
        "paid_burden": 0,
        "paid_epochs": 0,
        "overloaded_epochs": 0,
        "overload_units": 0,
        "guaranteed_weight_floor_sum": 0,
    }

    for _ in range(systems):
        atom_count = rng.randint(2, 6)
        balance = [rng.randint(4, 15) for _ in range(atom_count)]
        totals["atoms"] += atom_count

        for _epoch in range(rng.randint(1, 4)):
            totals["epochs"] += 1
            deposit = [rng.randint(0, 4) for _ in range(atom_count)]
            balance = [x + d for x, d in zip(balance, deposit)]
            totals["capacity_deposits"] += sum(deposit)

            reference = [rng.randint(0, 7) for _ in range(atom_count)]
            removed = [rng.randint(0, x) for x in reference]
            added = [rng.randint(0, 4) for _ in range(atom_count)]
            actual = [b - r + a for b, r, a in zip(reference, removed, added)]
            assert min(actual) >= 0
            weight = rng.randint(1, 30)

            totals["candidate_weight"] += weight
            totals["reference_burden"] += sum(reference)
            totals["removed_burden"] += sum(removed)
            totals["added_burden"] += sum(added)
            overload = sum(max(0, load - cap) for load, cap in zip(actual, balance))
            if overload:
                totals["overloaded_epochs"] += 1
                totals["overload_units"] += overload
                break

            totals["paid_epochs"] += 1
            totals["paid_burden"] += sum(actual)
            totals["guaranteed_weight_floor_sum"] += math.floor(
                weight * weight / (weight + sum(actual))
            )
            balance = [cap - load for cap, load in zip(balance, actual)]
            assert min(balance) >= 0

    print(f"systems={systems}")
    for key, value in totals.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
