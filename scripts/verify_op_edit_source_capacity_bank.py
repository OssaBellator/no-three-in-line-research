#!/usr/bin/env python3
import random


def main() -> None:
    rng = random.Random(1105)
    epochs = 8_500
    edit_steps = 0
    deletion_charge_units = 0
    positive_variation_units = 0
    paid_epochs = 0
    overload_epochs = 0
    source_class_checks = 0

    for _ in range(epochs):
        class_count = rng.randint(1, 6)
        balances = [rng.randint(0, 20) + rng.randint(0, 8) for _ in range(class_count)]
        used = [0 for _ in range(class_count)]
        epoch_variation = 0

        for _ in range(rng.randint(1, 12)):
            charge = rng.randint(0, 6)
            edit_class = rng.randrange(class_count)
            used[edit_class] += charge
            deletion_charge_units += charge
            increase = rng.randint(0, charge)
            positive_variation_units += increase
            epoch_variation += increase
            edit_steps += 1

        source_class_checks += class_count
        assert epoch_variation <= sum(used)
        if all(used[i] <= balances[i] for i in range(class_count)):
            paid_epochs += 1
        else:
            overload_epochs += 1
            assert any(used[i] > balances[i] for i in range(class_count))

    print(f"epochs={epochs}")
    print(f"edit_steps={edit_steps}")
    print(f"deletion_charge_units={deletion_charge_units}")
    print(f"positive_variation_units={positive_variation_units}")
    print(f"paid_epochs={paid_epochs}")
    print(f"overload_epochs={overload_epochs}")
    print(f"source_class_checks={source_class_checks}")


if __name__ == "__main__":
    main()
