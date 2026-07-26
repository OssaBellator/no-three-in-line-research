#!/usr/bin/env python3
"""Finite checks for AC3pj--AC3pn."""

from __future__ import annotations

from collections import Counter
from itertools import product
from random import Random


def one_step_checks(counts: Counter[str]) -> None:
    # A small exhaustive grid is enough here; larger mixed histories are stressed below.
    for q in range(1, 3):
        for source_count in range(1, 3):
            for m in product(range(3), repeat=q):
                for s in product(range(2), repeat=source_count):
                    for rho in product(range(1, 4), repeat=source_count):
                        for m2 in product(range(3), repeat=q):
                            for s2 in product(*(range(value + 1) for value in s)):
                                created = sum(max(0, b - a) for a, b in zip(m, m2))
                                consumed = sum(max(0, a - b) for a, b in zip(m, m2))
                                debits = tuple(a - b for a, b in zip(s, s2))
                                budget = sum(rate * debit for rate, debit in zip(rho, debits))
                                if created > budget:
                                    continue
                                if created > 0:
                                    assert sum(debits) > 0
                                phi = sum(m) + sum(rate * value for rate, value in zip(rho, s))
                                phi2 = sum(m2) + sum(rate * value for rate, value in zip(rho, s2))
                                source_total = sum(s)
                                source_total2 = sum(s2)
                                assert phi2 <= phi - consumed
                                if consumed > 0:
                                    assert phi2 < phi
                                elif sum(debits) > 0:
                                    assert phi2 <= phi and source_total2 < source_total
                                counts["one-step ledgers"] += 1


def random_histories(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(50000):
        q = rng.randint(1, 5)
        source_count = rng.randint(1, 5)
        m = [rng.randint(0, 20) for _ in range(q)]
        s = [rng.randint(0, 12) for _ in range(source_count)]
        rho = [rng.randint(1, 6) for _ in range(source_count)]
        m0 = sum(m)
        s0 = tuple(s)
        total_created = 0
        total_consumed = 0
        total_debit = [0] * source_count
        replenishment_steps = 0
        source_only_steps = 0
        steps = 0

        for _step in range(100):
            can_consume = any(value > 0 for value in m)
            can_debit = any(value > 0 for value in s)
            if not can_consume and not can_debit:
                break

            old_m = tuple(m)
            old_s = tuple(s)
            source_only = can_debit and rng.randrange(10) == 0
            do_replenish = (
                not source_only
                and can_debit
                and (not can_consume or rng.randrange(3) != 0)
            )

            if source_only:
                available_sources = [a for a, value in enumerate(s) if value > 0]
                a = rng.choice(available_sources)
                debit = rng.randint(1, s[a])
                s[a] -= debit
                source_only_steps += 1
            elif do_replenish:
                available_sources = [a for a, value in enumerate(s) if value > 0]
                a = rng.choice(available_sources)
                debit = rng.randint(1, s[a])
                s[a] -= debit
                budget = rho[a] * debit
                created = rng.randint(1, budget)
                for _ in range(created):
                    m[rng.randrange(q)] += 1
                # Mixed moves may also consume some units.
                extra_consume = rng.randint(0, min(sum(m), 4))
                for _ in range(extra_consume):
                    positive = [i for i, value in enumerate(m) if value > 0]
                    if not positive:
                        break
                    m[rng.choice(positive)] -= 1
                replenishment_steps += 1
            else:
                positive = [i for i, value in enumerate(m) if value > 0]
                m[rng.choice(positive)] -= 1

            created = sum(max(0, b - a) for a, b in zip(old_m, m))
            consumed = sum(max(0, a - b) for a, b in zip(old_m, m))
            debits = [a - b for a, b in zip(old_s, s)]
            assert created <= sum(rate * debit for rate, debit in zip(rho, debits))
            assert consumed >= 1 or sum(debits) >= 1
            total_created += created
            total_consumed += consumed
            for a, debit in enumerate(debits):
                total_debit[a] += debit
            steps += 1

        source_budget = sum(rate * value for rate, value in zip(rho, s0))
        transition_bound = m0 + sum((rate + 1) * value for rate, value in zip(rho, s0))
        assert total_created <= source_budget
        assert replenishment_steps <= sum(s0)
        assert source_only_steps <= sum(s0)
        assert total_consumed <= m0 + total_created
        assert steps <= total_consumed + sum(total_debit)
        assert steps <= transition_bound
        counts["random histories"] += 1
        counts["accepted transitions"] += steps
        counts["source-only debits"] += source_only_steps


def capped_gate_checks(counts: Counter[str]) -> None:
    rng = Random(911)
    for _ in range(30000):
        base = rng.randint(1, 8)
        thresholds = [rng.randint(0, 5) for _ in range(rng.randint(1, 4))]
        kinds = rng.randint(1, 5)
        stock = base
        for threshold in thresholds:
            stock *= threshold + 1
        false_count = rng.randint(0, stock)
        true_count = stock - false_count
        gates = kinds * false_count * true_count
        assert gates <= kinds * (stock * stock // 4)
        counts["capped gate systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    one_step_checks(counts)
    random_histories(counts)
    capped_gate_checks(counts)
    print("AC3pj--AC3pn replenishment source-ledger audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
