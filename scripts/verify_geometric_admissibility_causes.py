#!/usr/bin/env python3
"""Finite checks for GC3g--GC3i."""

from __future__ import annotations

from collections import Counter
from itertools import product


def verify_single_type_fibres(counts: Counter[str]) -> None:
    for cause_count in range(1, 6):
        causes = tuple(range(cause_count))
        for edge_count in range(0, 8):
            for cause_word in product(causes, repeat=edge_count):
                loads = [cause_word.count(cause) for cause in causes]
                maximum = max(loads, default=0)
                assert edge_count <= maximum * cause_count
                counts["single-type cause maps"] += 1


def verify_typed_fibres(counts: Counter[str]) -> None:
    # Each cause has one of three geometric types.  Canonical edge causes are
    # arbitrary changed atoms; summing the typewise maximum load times the type
    # size must cover every edge.
    for cause_count in range(1, 6):
        causes = tuple(range(cause_count))
        for types in product(range(3), repeat=cause_count):
            type_classes = {
                kind: [cause for cause, value in zip(causes, types, strict=True) if value == kind]
                for kind in range(3)
            }
            for edge_count in range(0, 7):
                for cause_word in product(causes, repeat=edge_count):
                    bound = 0
                    for kind, members in type_classes.items():
                        del kind
                        if not members:
                            continue
                        maximum = max(cause_word.count(cause) for cause in members)
                        bound += maximum * len(members)
                    assert edge_count <= bound
                    counts["typed cause maps"] += 1


def verify_shadow_substitution(counts: Counter[str]) -> None:
    for residual in range(0, 8):
        for cause_count in range(0, 9):
            for cause_load in range(0, 9):
                assignments = cause_count * cause_load
                shadow = 3 * residual * assignments
                assert shadow == 3 * residual * cause_load * cause_count
                counts["shadow substitutions"] += 1


def verify_ticket_histories(counts: Counter[str]) -> None:
    for ticket_stock in range(0, 10):
        for cause_load in range(0, 8):
            used = 0
            assignments = 0
            while used < ticket_stock:
                used += 1
                assignments += cause_load
                assert assignments <= cause_load * ticket_stock
                counts["ticket steps"] += 1
            assert assignments <= cause_load * ticket_stock
            counts["ticket histories"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_single_type_fibres(counts)
    verify_typed_fibres(counts)
    verify_shadow_substitution(counts)
    verify_ticket_histories(counts)

    print("GC3g--GC3i admissibility cause audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
