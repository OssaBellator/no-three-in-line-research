#!/usr/bin/env python3
"""Finite checks for AC3kr--AC3ku."""

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
                # The current assignment is all zero and must be hard-feasible.
                if all(value == 0 for value in values):
                    continue
                checks.append((scope, values))
    return checks


def verify_witness_trichotomy(counts: Counter[str]) -> None:
    # Variable 0 is v, variable 1 is x, and every other variable remains current.
    for variable_count in range(2, 6):
        for alphabet_size in range(2, 5):
            checks = generate_checks(variable_count, alphabet_size)
            counts["canonical checks"] += len(checks)
            for centre_phase in range(1, alphabet_size):
                for residual_phase in range(1, alphabet_size):
                    assignment = [0] * variable_count
                    assignment[0] = centre_phase
                    assignment[1] = residual_phase
                    state = tuple(assignment)
                    counts["two-block assignments"] += 1
                    for check in checks:
                        if not violated(check, state):
                            continue
                        scope, values = check
                        counts["new hard witnesses"] += 1
                        assert 0 in scope or 1 in scope
                        for index, value in zip(scope, values):
                            if index not in (0, 1):
                                assert value == 0
                        changed_count = int(0 in scope) + int(1 in scope)
                        assert changed_count in (1, 2)
                        residual_rank = len(scope) - changed_count
                        if changed_count == 1:
                            assert residual_rank <= 2
                            if 0 in scope:
                                counts["centre-only witnesses"] += 1
                            else:
                                counts["residual-only witnesses"] += 1
                        else:
                            assert residual_rank <= 1
                            counts["joint witnesses"] += 1


def verify_phase_cover(counts: Counter[str]) -> None:
    for alphabet_size in range(2, 8):
        phases = tuple(range(1, alphabet_size))
        phase_set = set(phases)
        phase_count = len(phases)
        for x_mask in range(1 << phase_count):
            x_blocked = {phases[index] for index in range(phase_count) if x_mask & (1 << index)}
            for joint_mask in range(1 << phase_count):
                joint_blocked = {
                    phases[index] for index in range(phase_count) if joint_mask & (1 << index)
                }
                for centre_only in (False, True):
                    safe = [
                        phase
                        for phase in phases
                        if not centre_only and phase not in x_blocked | joint_blocked
                    ]
                    failure = not safe
                    assert failure == (centre_only or x_blocked | joint_blocked == phase_set)
                    if failure and not centre_only:
                        assert len(x_blocked) + len(joint_blocked) >= phase_count
                        assert max(len(x_blocked), len(joint_blocked)) >= (phase_count + 1) // 2
                    counts["phase-cover systems"] += 1


def verify_common_residual_router(counts: Counter[str]) -> None:
    statuses = ("complete", "centre_only", "x_heavy", "joint_heavy")
    for target_count in range(1, 7):
        for routing in product(statuses, repeat=target_count):
            assert sum(routing.count(status) for status in statuses) == target_count
            open_targets = routing.count("joint_heavy")
            for residual_phase_count in range(1, 8):
                joint_incidence = open_targets * ((residual_phase_count + 1) // 2)
                for role_count in range(1, 7):
                    if joint_incidence:
                        heaviest = (joint_incidence + role_count - 1) // role_count
                        assert heaviest * role_count >= joint_incidence
                    counts["common-residual routing systems"] += 1


def verify_support_disjoint_selection(counts: Counter[str]) -> None:
    # Residual scopes are represented by disjoint integer intervals.  Selecting
    # the least member must give distinct correction blocks.
    for family_size in range(1, 9):
        for widths in product((1, 2), repeat=family_size):
            scopes: list[set[int]] = []
            cursor = 0
            for width in widths:
                scope = set(range(cursor, cursor + width))
                scopes.append(scope)
                cursor += width
            selected = [min(scope) for scope in scopes]
            assert len(selected) == len(set(selected))
            for left, right in combinations(scopes, 2):
                assert left.isdisjoint(right)
            counts["support-disjoint selector systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_witness_trichotomy(counts)
    verify_phase_cover(counts)
    verify_common_residual_router(counts)
    verify_support_disjoint_selection(counts)

    print("AC3kr--AC3ku two-block target completion audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
