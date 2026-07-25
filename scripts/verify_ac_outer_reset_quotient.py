#!/usr/bin/env python3
"""Finite checks for AC3ka--AC3kd."""
from __future__ import annotations

from collections import Counter
from itertools import product


def verify_stock(counts: Counter[str]) -> None:
    for p in range(1, 9):
        for r in range(1, 7):
            edges = [
                (a, b, d)
                for a in range(p)
                for b in range(p)
                if a != b
                for d in range(r)
            ]
            assert len(edges) == r * p * (p - 1)
            counts["decorated edge stocks"] += 1

    for sizes in product(range(1, 6), repeat=4):
        profiles = 1
        for size in sizes:
            profiles *= size
        assert profiles == sizes[0] * sizes[1] * sizes[2] * sizes[3]
        counts["profile product bounds"] += 1


def verify_local_potential(counts: Counter[str]) -> None:
    for p in range(1, 9):
        for r in range(1, 6):
            edge_max = r * p * (p - 1)
            for epoch_max in range(0, 17):
                ceiling = (epoch_max + 1) * edge_max + epoch_max
                for seen in range(edge_max + 1):
                    for counter in range(epoch_max + 1):
                        old = (epoch_max + 1) * seen + counter
                        assert old <= ceiling
                        if counter < epoch_max:
                            assert (epoch_max + 1) * seen + counter + 1 > old
                            counts["internal potential steps"] += 1
                        if seen < edge_max:
                            assert (epoch_max + 1) * (seen + 1) > old
                            counts["first edge potential steps"] += 1


def classify_history(history: tuple[int, ...], edge_count: int) -> str:
    seen: set[int] = set()
    for edge in history:
        assert 0 <= edge < edge_count
        if edge in seen:
            return "repeat"
        seen.add(edge)
    return "simple"


def verify_histories(counts: Counter[str]) -> None:
    for edge_count in range(1, 7):
        for length in range(0, edge_count + 3):
            for history in product(range(edge_count), repeat=length):
                kind = classify_history(history, edge_count)
                if length > edge_count:
                    assert kind == "repeat"
                if kind == "simple":
                    assert len(set(history)) == length
                else:
                    assert len(set(history)) < length
                counts[f"{kind} macro histories"] += 1


def verify_weighted_concentration(counts: Counter[str]) -> None:
    for edge_count in range(1, 20):
        width = min(edge_count, 5)
        for weights in product(range(0, 6), repeat=width):
            expanded = [weights[i % width] for i in range(edge_count)]
            total = sum(expanded)
            max_weight = max(expanded, default=0)
            assert edge_count * max_weight >= total
            counts["weighted edge systems"] += 1


def verify_global_ticket_potential(counts: Counter[str]) -> None:
    for p in range(1, 7):
        for r in range(1, 5):
            edge_max = r * p * (p - 1)
            for ticket_max in range(0, 9):
                for epoch_max in range(0, 13):
                    ceiling = (
                        (epoch_max + 1) * (edge_max + ticket_max) + epoch_max
                    )
                    for seen in range(edge_max + 1):
                        for used in range(ticket_max + 1):
                            for counter in range(epoch_max + 1):
                                old = (
                                    (epoch_max + 1) * (seen + used) + counter
                                )
                                assert old <= ceiling
                                if counter < epoch_max:
                                    assert (
                                        (epoch_max + 1) * (seen + used)
                                        + counter
                                        + 1
                                        > old
                                    )
                                    counts["global internal steps"] += 1
                                if seen < edge_max:
                                    assert (
                                        (epoch_max + 1) * (seen + used + 1)
                                        > old
                                    )
                                    counts["global first edge steps"] += 1
                                if used < ticket_max:
                                    assert (
                                        (epoch_max + 1) * (seen + used + 1)
                                        > old
                                    )
                                    counts["global ticket steps"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_stock(counts)
    verify_local_potential(counts)
    verify_histories(counts)
    verify_weighted_concentration(counts)
    verify_global_ticket_potential(counts)

    print("AC3ka--AC3kd outer reset quotient audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
