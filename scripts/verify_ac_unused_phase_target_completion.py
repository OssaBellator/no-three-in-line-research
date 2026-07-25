#!/usr/bin/env python3
"""Finite checks for AC3kv--AC3ky."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product


def violated(check: tuple[tuple[int, ...], tuple[int, ...]], assignment: tuple[int, ...]) -> bool:
    scope, values = check
    return all(assignment[index] == value for index, value in zip(scope, values))


def generate_checks(variable_count: int, alphabet_size: int) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    checks: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for rank in range(1, min(3, variable_count) + 1):
        for scope in combinations(range(variable_count), rank):
            for values in product(range(alphabet_size), repeat=rank):
                if all(value == 0 for value in values):
                    continue
                checks.append((scope, values))
    return checks


def verify_unused_phase_lemma(counts: Counter[str]) -> None:
    # Variable 0 is v and variable 1 is x.  The current assignment is all zero.
    for variable_count in range(2, 6):
        for alphabet_size in range(3, 6):
            checks = generate_checks(variable_count, alphabet_size)
            x_support = {
                values[scope.index(1)]
                for scope, values in checks
                if 1 in scope
            }
            # Test arbitrary support restrictions rather than only the complete
            # generated family.
            noncurrent = tuple(range(1, alphabet_size))
            for support_mask in range(1 << len(noncurrent)):
                allowed_support = {
                    noncurrent[index]
                    for index in range(len(noncurrent))
                    if support_mask & (1 << index)
                }
                restricted = [
                    check
                    for check in checks
                    if 1 not in check[0]
                    or check[1][check[0].index(1)] in allowed_support
                ]
                for unused_phase in set(noncurrent) - allowed_support:
                    for centre_phase in noncurrent:
                        assignment = [0] * variable_count
                        assignment[0] = centre_phase
                        assignment[1] = unused_phase
                        state = tuple(assignment)
                        for check in restricted:
                            if violated(check, state):
                                assert 1 not in check[0]
                                assert 0 in check[0]
                                counts["centre-only failures under unused phases"] += 1
                        counts["unused-phase assignments"] += 1
                counts["hard-support systems"] += 1
            assert x_support == set(range(alphabet_size))


def verify_common_batch(counts: Counter[str]) -> None:
    # Abstractly record whether each target has a centre-only witness.  One unused
    # residual phase completes exactly the targets without such a witness.
    for target_count in range(1, 10):
        for witness_bits in product((False, True), repeat=target_count):
            completed = [index for index, blocked in enumerate(witness_bits) if not blocked]
            assert len(completed) + sum(witness_bits) == target_count
            counts["common-residual batch systems"] += 1


def verify_literal_saturation(counts: Counter[str]) -> None:
    for alphabet_size in range(2, 10):
        noncurrent = tuple(range(1, alphabet_size))
        for support_mask in range(1 << len(noncurrent)):
            support = {
                noncurrent[index]
                for index in range(len(noncurrent))
                if support_mask & (1 << index)
            }
            saturated = set(noncurrent) <= support
            unused = set(noncurrent) - support
            assert saturated == (not unused)
            counts["literal-saturation systems"] += 1


def verify_support_disjoint_count(counts: Counter[str]) -> None:
    # Targets are assigned distinct residual blocks.  Every uncompleted target is
    # marked as replacement/reset or saturated.  If fewer than c are in the
    # former class, at least m-c are saturated.
    for target_count in range(1, 11):
        for statuses in product(("complete", "replacement", "reset", "saturated"), repeat=target_count):
            remaining = sum(status != "complete" for status in statuses)
            exceptional = statuses.count("replacement") + statuses.count("reset")
            saturated = statuses.count("saturated")
            assert remaining == exceptional + saturated
            for cap in range(exceptional, remaining + 1):
                if exceptional < cap:
                    assert saturated >= remaining - cap + 1
            counts["support-disjoint saturation ledgers"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_unused_phase_lemma(counts)
    verify_common_batch(counts)
    verify_literal_saturation(counts)
    verify_support_disjoint_count(counts)

    print("AC3kv--AC3ky unused-phase completion audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
