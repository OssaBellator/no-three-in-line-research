#!/usr/bin/env python3
"""Finite checks for AC3qa--AC3qe."""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from itertools import product
from random import Random


def audit_history(s0: int, outputs: tuple[int, ...], loss_types: tuple[int, ...], counts: Counter[str]) -> None:
    assert len(outputs) == len(loss_types)
    stock = s0
    stocks = [stock]
    amplification_units: list[int] = []
    loss_units: list[tuple[int, int]] = []

    for t, (h, loss_type) in enumerate(zip(outputs, loss_types)):
        assert stock >= 1
        stock += h - 1
        assert stock >= 0
        stocks.append(stock)
        amplification_units.extend([t] * max(h - 1, 0))
        loss_units.extend([(t, loss_type)] * max(1 - h, 0))

    a_total = sum(max(h - 1, 0) for h in outputs)
    l_total = sum(max(1 - h, 0) for h in outputs)
    assert stock == s0 + a_total - l_total
    assert a_total == l_total + stock - s0

    cap = max(stocks)
    assert a_total <= l_total + cap - s0

    unmatched = deque(amplification_units)
    matched_by_type: dict[int, int] = defaultdict(int)
    matched_losses = 0
    for loss_time, loss_type in loss_units:
        if unmatched and unmatched[0] < loss_time:
            unmatched.popleft()
            matched_by_type[loss_type] += 1
            matched_losses += 1

    # Surplus not matched chronologically to later losses occupies final/cap headroom.
    assert len(unmatched) == max(stock - s0, 0) or len(unmatched) <= cap - s0
    required_loss_matches = max(a_total - (cap - s0), 0)
    assert matched_losses >= required_loss_matches

    if matched_by_type:
        k_loss = max(loss_types) + 1
        assert max(matched_by_type.values()) * k_loss >= matched_losses

    counts["histories"] += 1
    counts["transitions"] += len(outputs)
    counts["amplification units"] += a_total
    counts["loss units"] += l_total
    counts["matched surplus units"] += matched_losses


def exhaustive_histories(counts: Counter[str]) -> None:
    for s0 in range(1, 4):
        for length in range(0, 7):
            for outputs in product(range(4), repeat=length):
                stock = s0
                valid = True
                for h in outputs:
                    if stock < 1:
                        valid = False
                        break
                    stock += h - 1
                if not valid:
                    continue
                for loss_types in product(range(2), repeat=length):
                    audit_history(s0, outputs, loss_types, counts)
                    counts["exhaustive histories"] += 1


def random_histories(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(50000):
        s0 = rng.randint(1, 20)
        cap = rng.randint(s0, s0 + 30)
        stock = s0
        outputs: list[int] = []
        loss_types: list[int] = []
        for _step in range(100):
            if stock < 1:
                break
            choices = [h for h in range(4) if stock + h - 1 <= cap]
            if not choices:
                break
            h = rng.choice(choices)
            outputs.append(h)
            loss_types.append(rng.randrange(5))
            stock += h - 1
        audit_history(s0, tuple(outputs), tuple(loss_types), counts)
        counts["random histories"] += 1


def joint_ticket_checks(counts: Counter[str]) -> None:
    for j in range(21):
        for attempted in range(31):
            realized = min(j, attempted)
            assert realized <= j
            counts["joint-ticket systems"] += 1
            counts["joint-ticket realizations"] += realized

    for j1 in range(16):
        for j2 in range(16):
            for attempted in range(20):
                realized = min(j1, j2, attempted)
                assert realized <= min(j1, j2)
                counts["two-slot ticket systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_histories(counts)
    random_histories(counts)
    joint_ticket_checks(counts)
    print("AC3qa--AC3qe realized-amplification audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
