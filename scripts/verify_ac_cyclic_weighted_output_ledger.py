#!/usr/bin/env python3
"""Finite audit for AC3qu--AC3qy.

Checks exact cyclic-component output changes, downstream yield drops, finite weighted
ceilings, surplus/loss accounting, unit-cycle leakage and internal branching.
"""

from __future__ import annotations

import random
from itertools import product

SEED = 20260727
RNG = random.Random(SEED)


def exhaustive_component_steps() -> int:
    checked = 0
    for s, u, capacity in product(range(4), repeat=3):
        for yield_weight in range(1, 4):
            potential = s + yield_weight * u + capacity
            for debit in range(s + 1):
                for internal_create in range(4):
                    for downstream_create in range(3):
                        for terminal_create in range(3):
                            s2 = s - debit + internal_create
                            u2 = u + downstream_create
                            capacity2 = capacity + terminal_create
                            surplus = (
                                internal_create
                                + yield_weight * downstream_create
                                + terminal_create
                                - debit
                            )
                            assert (
                                s2 + yield_weight * u2 + capacity2 - potential
                                == surplus
                            )
                            checked += 1
    return checked


def exhaustive_downstream_steps() -> int:
    checked = 0
    for u, capacity, weight, debit, created, destroyed in product(
        range(4), range(4), range(1, 4), range(4), range(4), range(4)
    ):
        if debit > u or created > weight * debit or destroyed > capacity + created:
            continue
        potential = weight * u + capacity
        u2 = u - debit
        capacity2 = capacity + created - destroyed
        delta = weight * u2 + capacity2 - potential
        assert delta <= -destroyed
        checked += 1
    return checked


def random_histories(histories: int = 12_000) -> tuple[int, int, int, int]:
    total_steps = 0
    positive_steps = 0
    unit_cycle_leaks = 0
    internal_branches = 0

    for _ in range(histories):
        n_component = RNG.randint(1, 4)
        n_downstream = RNG.randint(0, 3)
        component_caps = [RNG.randint(1, 8) for _ in range(n_component)]
        downstream_caps = [RNG.randint(0, 8) for _ in range(n_downstream)]
        yield_weights = [RNG.randint(1, 5) for _ in range(n_downstream)]
        terminal_cap = RNG.randint(2, 15)

        component = [RNG.randint(0, cap) for cap in component_caps]
        downstream = [RNG.randint(0, cap) for cap in downstream_caps]
        terminal = RNG.randint(0, terminal_cap)

        ceiling = (
            sum(component_caps)
            + sum(w * cap for w, cap in zip(yield_weights, downstream_caps))
            + terminal_cap
        )

        def potential() -> int:
            return (
                sum(component)
                + sum(w * value for w, value in zip(yield_weights, downstream))
                + terminal
            )

        initial = potential()
        positive = 0
        negative = 0
        downstream_drop = 0

        for _step in range(100):
            if RNG.random() < 0.7 and any(component):
                debits = [0] * n_component
                source = RNG.choice([i for i, value in enumerate(component) if value > 0])
                debits[source] = RNG.randint(1, component[source])

                internal_create = [0] * n_component
                for i in range(n_component):
                    available = component_caps[i] - (component[i] - debits[i])
                    internal_create[i] = RNG.randint(0, available)

                downstream_create = [
                    RNG.randint(0, downstream_caps[i] - downstream[i])
                    for i in range(n_downstream)
                ]
                terminal_create = RNG.randint(0, terminal_cap - terminal)

                old = potential()
                for i in range(n_component):
                    component[i] = component[i] - debits[i] + internal_create[i]
                for i in range(n_downstream):
                    downstream[i] += downstream_create[i]
                terminal += terminal_create

                weighted_exit = (
                    sum(
                        w * value
                        for w, value in zip(yield_weights, downstream_create)
                    )
                    + terminal_create
                )
                surplus = sum(internal_create) + weighted_exit - sum(debits)
                assert potential() - old == surplus

                if surplus > 0:
                    positive += surplus
                    positive_steps += 1
                else:
                    negative += -surplus

                if sum(internal_create) == sum(debits) and weighted_exit > 0:
                    unit_cycle_leaks += 1
                    assert surplus == weighted_exit
                if sum(downstream_create) + terminal_create == 0 and sum(
                    internal_create
                ) > sum(debits):
                    internal_branches += 1
                    assert surplus == sum(internal_create) - sum(debits)
            else:
                available = [i for i, value in enumerate(downstream) if value > 0]
                if not available:
                    continue
                source = RNG.choice(available)
                debit = RNG.randint(1, downstream[source])
                created = RNG.randint(
                    0, min(yield_weights[source] * debit, terminal_cap - terminal)
                )
                destroyed = RNG.randint(0, terminal + created)

                old = potential()
                downstream[source] -= debit
                terminal = terminal + created - destroyed
                delta = potential() - old
                assert delta <= -destroyed
                downstream_drop += -delta

            assert 0 <= potential() <= ceiling
            total_steps += 1

        assert potential() == initial + positive - negative - downstream_drop
        assert positive <= negative + downstream_drop + ceiling - initial

    return total_steps, positive_steps, unit_cycle_leaks, internal_branches


def main() -> None:
    component_steps = exhaustive_component_steps()
    downstream_steps = exhaustive_downstream_steps()
    total_steps, positive_steps, leaks, branches = random_histories()
    print(
        "PASS AC cyclic weighted-output audit:",
        f"{component_steps} exhaustive component steps;",
        f"{downstream_steps} exhaustive downstream steps;",
        f"{total_steps} mixed history steps;",
        f"{positive_steps} positive-surplus steps;",
        f"{leaks} unit-cycle leaks;",
        f"{branches} internal branches.",
    )


if __name__ == "__main__":
    main()
