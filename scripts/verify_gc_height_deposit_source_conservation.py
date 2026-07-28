#!/usr/bin/env python3
import random


def main() -> None:
    rng = random.Random(1104)
    epochs = 9_000
    transitions = 0
    deposit_units = 0
    paid_loss_epochs = 0
    overload_epochs = 0
    sampled_amplification_resets = 0

    for _ in range(epochs):
        source_types = rng.randint(1, 6)
        live = [rng.randint(0, 12) for _ in range(source_types)]
        reserve = rng.randint(0, 15)
        initial_total = sum(live) + reserve

        for _ in range(rng.randint(1, 20)):
            if rng.random() < 0.08:
                sampled_amplification_resets += 1
                continue
            nonempty = [i for i, value in enumerate(live) if value > 0]
            if not nonempty:
                break
            source = rng.choice(nonempty)
            live[source] -= 1
            if rng.random() < 0.35:
                reserve += 1
                deposit_units += 1
            else:
                target = rng.randrange(source_types)
                live[target] += 1
            transitions += 1
            assert sum(live) + reserve == initial_total

        loss = rng.randint(0, 20)
        if loss <= reserve:
            reserve -= loss
            paid_loss_epochs += 1
        else:
            overload_epochs += 1
        assert sum(live) + reserve <= initial_total

    print(f"epochs={epochs}")
    print(f"source_transitions={transitions}")
    print(f"height_deposit_units={deposit_units}")
    print(f"paid_loss_epochs={paid_loss_epochs}")
    print(f"overload_epochs={overload_epochs}")
    print(f"sampled_amplification_resets={sampled_amplification_resets}")


if __name__ == "__main__":
    main()
