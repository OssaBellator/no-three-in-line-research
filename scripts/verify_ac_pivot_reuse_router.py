#!/usr/bin/env python3
"""Finite checks for AC3gn--AC3gq."""

from __future__ import annotations

from itertools import permutations, product

Permutation = tuple[int, ...]
Signature = tuple[int, ...]


def derangements(n: int) -> tuple[Permutation, ...]:
    return tuple(
        perm for perm in permutations(range(n))
        if all(perm[c] != c for c in range(n))
    )


def is_permutation(perm: Permutation) -> bool:
    return sorted(perm) == list(range(len(perm)))


def disjoint(first: Permutation, second: Permutation) -> bool:
    return all(a != b for a, b in zip(first, second))


def canonical_signature_and_repair(
    pivot_layer: Permutation,
    opposite_layer: Permutation,
    pivot_column: int,
    partner_column: int,
    layer: int,
    role: int,
) -> tuple[Signature, Permutation, Permutation]:
    n = len(pivot_layer)
    c0, c1 = pivot_column, partner_column
    r0, r1 = pivot_layer[c0], pivot_layer[c1]
    b0, b1 = opposite_layer[c0], opposite_layer[c1]
    blocked0 = b0 == r1
    blocked1 = b1 == r0
    occupancy = int(blocked0) + int(blocked1)

    active_after = list(pivot_layer)
    active_after[c0], active_after[c1] = r1, r0
    blocker_after = list(opposite_layer)
    c2 = -1
    b2 = -1

    if occupancy == 0:
        case = 0
    elif blocked0 and not blocked1:
        case = 1
        blocker_after[c0], blocker_after[c1] = b1, b0
    elif blocked1 and not blocked0:
        case = 2
        c2 = next(c for c in range(n) if c not in (c0, c1))
        b2 = opposite_layer[c2]
        blocker_after[c1], blocker_after[c2] = b2, b1
    else:
        case = 3
        c2 = next(c for c in range(n) if c not in (c0, c1))
        b2 = opposite_layer[c2]
        blocker_after[c0] = b2
        blocker_after[c1] = r1
        blocker_after[c2] = r0

    first = tuple(active_after)
    second = tuple(blocker_after)
    assert is_permutation(first)
    assert is_permutation(second)
    assert disjoint(first, second)
    assert second[c0] != r0

    signature: Signature = (
        layer,
        role,
        c0,
        c1,
        r0,
        r1,
        b0,
        b1,
        case,
        c2,
        b2,
    )
    return signature, first, second


def verify_signatures() -> tuple[int, int, int]:
    checks = 0
    distinct_checks = 0
    actual_signatures: set[Signature] = set()
    role_count = 5
    for n in range(3, 7):
        active = tuple(range(n))
        for blocker in derangements(n):
            for layer, first, second in (
                (0, active, blocker),
                (1, blocker, active),
            ):
                for c0 in range(n):
                    for role in range(role_count):
                        current: list[Signature] = []
                        for c1 in range(n):
                            if c1 == c0:
                                continue
                            signature, repaired_first, repaired_second = (
                                canonical_signature_and_repair(
                                    first, second, c0, c1, layer, role
                                )
                            )
                            pivot = (c0, first[c0])
                            union_after = {
                                *enumerate(repaired_first),
                                *enumerate(repaired_second),
                            }
                            assert pivot not in union_after
                            current.append(signature)
                            actual_signatures.add(signature)
                            checks += 1
                        assert len(current) == n - 1
                        assert len(set(current)) == n - 1
                        distinct_checks += 1
        assert len(actual_signatures) <= 2 * role_count * n**8
    return checks, distinct_checks, len(actual_signatures)


def verify_exposure_dichotomy() -> int:
    checks = 0
    for partner_count in range(2, 7):
        signatures = tuple(range(partner_count))
        for mask in range(1 << partner_count):
            exposed = {
                signatures[index]
                for index in range(partner_count)
                if mask & (1 << index)
            }
            unused = set(signatures) - exposed
            if unused:
                chosen = min(unused)
                assert chosen not in exposed
            else:
                assert exposed == set(signatures)
            checks += 1
    return checks


def verify_weighted_roles() -> int:
    checks = 0
    for role_count in range(1, 7):
        for weights in product(range(4), repeat=role_count):
            total = sum(weights)
            if total == 0:
                continue
            assert role_count * max(weights) >= total
            checks += 1
    return checks


def verify_potential() -> int:
    checks = 0
    for universe_size in range(1, 10):
        for exposed in range(0, 15):
            for support_size in range(1, universe_size + 1):
                before = universe_size * exposed + universe_size - support_size
                for smaller in range(1, support_size):
                    after = universe_size * exposed + universe_size - smaller
                    assert after >= before + 1
                    checks += 1
                for reopened in range(1, universe_size + 1):
                    after = (
                        universe_size * (exposed + 1)
                        + universe_size
                        - reopened
                    )
                    assert after >= before + 1
                    checks += 1
    return checks


def verify_bound() -> int:
    checks = 0
    for n in range(3, 50):
        for roles in range(1, 20):
            bound = 2 * roles * n**8
            assert bound >= 2 * roles * n**7
            checks += 1
    return checks


def main() -> None:
    signature_checks, distinct_checks, actual_count = verify_signatures()
    exposure_checks = verify_exposure_dichotomy()
    role_checks = verify_weighted_roles()
    potential_checks = verify_potential()
    bound_checks = verify_bound()
    print("AC pivot reuse router verified")
    print(f"  canonical signature repairs: {signature_checks}")
    print(f"  partner-distinct signature sets: {distinct_checks}")
    print(f"  distinct sampled signatures: {actual_count}")
    print(f"  exposure/saturation subsets: {exposure_checks}")
    print(f"  weighted role ledgers: {role_checks}")
    print(f"  combined potential transitions: {potential_checks}")
    print(f"  polynomial bound checks: {bound_checks}")


if __name__ == "__main__":
    main()
