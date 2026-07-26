#!/usr/bin/env python3
"""Finite checks for AC3qk--AC3qo."""

from __future__ import annotations

from collections import Counter
from itertools import product
from random import Random


def positive_change(old: tuple[int, ...], new: tuple[int, ...]) -> int:
    return sum(max(y - x, 0) for x, y in zip(old, new))


def negative_change(old: tuple[int, ...], new: tuple[int, ...]) -> int:
    return sum(max(x - y, 0) for x, y in zip(old, new))


def exhaustive_capacity_steps(counts: Counter[str]) -> None:
    for width in range(1, 4):
        vectors = list(product(range(3), repeat=width))
        for old in vectors:
            for new in vectors:
                g = positive_change(old, new)
                d = negative_change(old, new)
                assert sum(new) == sum(old) + g - d
                counts["exhaustive capacity steps"] += 1
                counts["gross created capacity"] += g
                counts["gross destroyed capacity"] += d

                # A one-source realization exists exactly when rho*debit covers creation.
                for rho in range(1, 4):
                    for debit in range(4):
                        source_faithful = g <= rho * debit
                        if g > 0 and source_faithful:
                            assert debit > 0
                        counts["source-step tests"] += 1


def random_histories(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(30000):
        width = rng.randint(1, 6)
        source_count = rng.randint(1, 4)
        rates = [rng.randint(1, 4) for _ in range(source_count)]
        sources0 = [rng.randint(0, 12) for _ in range(source_count)]
        sources = sources0[:]

        capacities = [rng.randint(0, 5) for _ in range(width)]
        occupancy = [rng.randint(0, cap) for cap in capacities]
        b0 = sum(capacities)
        s0 = sum(occupancy)

        total_g = 0
        total_d = 0
        amp = 0
        loss = 0
        transitions = 0
        activations = 0

        for _step in range(60):
            debits = [rng.randint(0, value) for value in sources]
            budget = sum(rate * debit for rate, debit in zip(rates, debits))
            for i, debit in enumerate(debits):
                sources[i] -= debit

            # Destroy arbitrary capacity only where final occupancy can still fit.
            reduced = []
            for cap, occ in zip(capacities, occupancy):
                reduced.append(rng.randint(occ, cap))

            increments = [0] * width
            remaining = rng.randint(0, budget) if budget else 0
            for i in range(width):
                add = rng.randint(0, remaining)
                increments[i] = add
                remaining -= add
            new_capacities = [x + y for x, y in zip(reduced, increments)]

            g = positive_change(tuple(capacities), tuple(new_capacities))
            d = negative_change(tuple(capacities), tuple(new_capacities))
            assert g <= budget
            if g > 0:
                assert sum(debits) > 0
            assert sum(new_capacities) == sum(capacities) + g - d
            activations += sum(1 for x, y in zip(capacities, new_capacities) if x == 0 < y)

            capacities = new_capacities
            total_g += g
            total_d += d

            # One alpha-pure source-unit transition, kept physically feasible.
            if sum(occupancy) > 0:
                occupied_atoms = [i for i, value in enumerate(occupancy) if value > 0]
                debit_atom = rng.choice(occupied_atoms)
                occupancy[debit_atom] -= 1
                free_slots = [i for i, (occ, cap) in enumerate(zip(occupancy, capacities)) if occ < cap]
                max_h = min(3, sum(cap - occ for occ, cap in zip(occupancy, capacities)))
                h = rng.randint(0, max_h)
                for _unit in range(h):
                    free_slots = [i for i, (occ, cap) in enumerate(zip(occupancy, capacities)) if occ < cap]
                    atom = rng.choice(free_slots)
                    occupancy[atom] += 1
                amp += max(h - 1, 0)
                loss += max(1 - h, 0)
                transitions += 1

            assert all(occ <= cap for occ, cap in zip(occupancy, capacities))

        assert sum(capacities) == b0 + total_g - total_d
        assert amp - loss == sum(occupancy) - s0
        assert total_g <= sum(rate * value for rate, value in zip(rates, sources0))
        assert amp + total_d <= loss + (b0 - s0) + total_g
        assert amp + total_d <= loss + (b0 - s0) + sum(
            rate * value for rate, value in zip(rates, sources0)
        )

        counts["random histories"] += 1
        counts["random transitions"] += transitions
        counts["random created capacity"] += total_g
        counts["random destroyed capacity"] += total_d
        counts["random amplification units"] += amp
        counts["random loss units"] += loss
        counts["atom activations"] += activations


def address_localization(counts: Counter[str]) -> None:
    rng = Random(20260727)
    for _ in range(30000):
        k = rng.randint(1, 20)
        weights = [rng.randint(0, 30) for _ in range(k)]
        total = sum(weights)
        assert max(weights, default=0) * k >= total
        counts["address systems"] += 1
        counts["addressed created units"] += total


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_capacity_steps(counts)
    random_histories(counts)
    address_localization(counts)
    print("AC3qk--AC3qo source-capacity recreation audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
