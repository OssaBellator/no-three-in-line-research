#!/usr/bin/env python3
"""Finite audit for OP4cl--OP4cp unit-edit capacity banks."""

from __future__ import annotations

import collections
import random


def main() -> None:
    rng = random.Random(1205)
    totals = collections.Counter()

    for _ in range(8500):
        n_units = rng.randint(2, 6)
        n_classes = rng.randint(1, 5)
        initial = [rng.randint(0, 12) for _ in range(n_classes)]
        deposits = [
            rng.randint(0, 6) if rng.random() < 0.65 else 0
            for _ in range(n_classes)
        ]
        balances = [initial[i] + deposits[i] for i in range(n_classes)]
        class_cost: collections.Counter[int] = collections.Counter()

        previous = rng.randrange(n_units)
        for _step in range(rng.randint(1, 10)):
            current = rng.randrange(n_units)
            source_class = rng.randrange(n_classes)
            cost = 0 if current == previous else rng.randint(1, 4)
            class_cost[source_class] += cost
            totals["edit_steps"] += 1
            totals["edit_cost_units"] += cost
            if current != previous:
                totals["unit_changes"] += 1
            previous = current

        overloaded = False
        for source_class, cost in sorted(class_cost.items()):
            totals["class_checks"] += 1
            if cost > balances[source_class]:
                totals["overload_units"] += cost - balances[source_class]
                overloaded = True
                break
            balances[source_class] -= cost

        totals["epochs"] += 1
        totals["initial_units"] += sum(initial)
        totals["deposit_units"] += sum(deposits)
        if overloaded:
            totals["overloaded_epochs"] += 1
        else:
            totals["paid_epochs"] += 1

    print("OP unit-edit capacity-bank audit")
    for key in (
        "epochs", "edit_steps", "unit_changes", "edit_cost_units",
        "initial_units", "deposit_units", "class_checks", "paid_epochs",
        "overloaded_epochs", "overload_units",
    ):
        print(f"{key}: {totals[key]}")


if __name__ == "__main__":
    main()
