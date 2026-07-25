#!/usr/bin/env python3
"""Finite checks for AC3fa--AC3fd.

The Markdown proof carries the general argument.  This script exhausts small
set systems and integer ledgers, verifies the finite decoder role alphabets,
and checks every composed constant used by the created-cell rank router.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import comb


def verify_new_cell_ranks() -> int:
    checks = 0
    for size in range(3, 8):
        universe = range(size)
        triples = list(combinations(universe, 3))
        for mask in range(1 << size):
            initial = {i for i in universe if (mask >> i) & 1}
            for triple in triples:
                if set(triple).issubset(initial):
                    continue
                rank = sum(cell not in initial for cell in triple)
                assert 1 <= rank <= 3
                checks += 1
    return checks


def verify_failed_ledgers() -> int:
    checks = 0
    for destroyed in range(1, 31):
        for rank_weights in product(range(11), repeat=3):
            if sum(rank_weights) < destroyed:
                continue
            assert 3 * max(rank_weights) >= destroyed
            checks += 1
    return checks


def verify_role_multisets() -> tuple[int, dict[int, tuple[int, int, int]]]:
    checks = 0
    table: dict[int, tuple[int, int, int]] = {}
    for alphabet_size in (8, 10, 16, 34):
        counts = []
        for rank in (1, 2, 3):
            expected = comb(alphabet_size + rank - 1, rank)
            if alphabet_size <= 16:
                observed = sum(
                    1
                    for _ in combinations_with_replacement(
                        range(alphabet_size), rank
                    )
                )
                assert observed == expected
            counts.append(expected)
            checks += 1
        table[alphabet_size] = tuple(counts)  # type: ignore[assignment]
    return checks, table


def verify_role_alphabets() -> dict[str, int]:
    clean = {
        "C_u",
        "D_u",
        "C_v",
        "D_v",
        "A_u:blocker",
        "B_u:blocker",
        "A_v:blocker",
        "B_v:blocker",
        "blocked_u->blocked_v",
        "blocked_v->blocked_u",
    }
    assert len(clean) == 10

    active_completion = {"U", "V", "Q_u", "Q_v"}
    selected_replacements = {
        f"{source}->{target}"
        for source in range(4)
        for target in range(4)
        if source != target
    }
    auxiliary_replacements = {
        *(f"{role}->*" for role in range(4)),
        *(f"*->{role}" for role in range(4)),
    }
    blocker_completion = selected_replacements | auxiliary_replacements
    assert len(active_completion) == 4
    assert len(blocker_completion) == 20

    missing = (
        {f"A:{role}" for role in active_completion}
        | {f"B:{role}" for role in blocker_completion}
        | {f"D:{role}" for role in clean}
    )
    assert len(missing) == 34

    direct = {
        "R:C",
        "R:D",
        "B:C->D",
        "B:D->C",
        "B:C->*",
        "B:*->C",
        "B:D->*",
        "B:*->D",
    }
    assert len(direct) == 8

    absent = {"A:Z", "A:Q", "R:C", "R:D"}
    first_repair = ("Z->Q", "Q->Z", "Z->*", "*->Z", "Q->*", "*->Q")
    second_repair = ("C->D", "D->C", "C->*", "*->C", "D->*", "*->D")
    absent |= {f"B1:{role}" for role in first_repair}
    absent |= {f"B2:{role}" for role in second_repair}
    assert len(absent) == 16

    return {
        "clean": len(clean),
        "missing": len(missing),
        "direct": len(direct),
        "absent": len(absent),
    }


def verify_constants() -> int:
    checks = 0
    identities = (
        (Fraction(1, 32) / 3, Fraction(1, 96)),
        (Fraction(1, 64) / 3, Fraction(1, 192)),
        (Fraction(1, 31) / 3, Fraction(1, 93)),
        (Fraction(1, 93) / 3, Fraction(1, 279)),
        (Fraction(1, 51) / 3, Fraction(1, 153)),
        (Fraction(1, 62) / 3, Fraction(1, 186)),
    )
    for left, right in identities:
        assert left == right
        checks += 1
    return checks


def main() -> None:
    rank_checks = verify_new_cell_ranks()
    ledger_checks = verify_failed_ledgers()
    multiset_checks, table = verify_role_multisets()
    alphabets = verify_role_alphabets()
    constant_checks = verify_constants()

    print("AC created-cell rank router verification passed")
    print(f"  created-triple rank checks: {rank_checks}")
    print(f"  failed-bank ledger checks: {ledger_checks}")
    print(f"  role-multiset formula checks: {multiset_checks}")
    print(f"  role alphabets: {alphabets}")
    print(f"  multiset table: {table}")
    print(f"  composed constant checks: {constant_checks}")


if __name__ == "__main__":
    main()
