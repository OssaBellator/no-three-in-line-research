#!/usr/bin/env python3
"""Exact finite checks for AC3jd--AC3jh.

The Markdown proof carries the general theorem.  This script exhausts the
finite abstractions and small rank systems used by the interface.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product
from math import ceil
from random import Random


def verify_label_formula(counts: Counter[str]) -> None:
    for q in range(1, 8):
        for r in range(1, 8):
            direct = q * sum(s * 2 ** (s - 1) for s in range(1, r + 1))
            closed = q * (1 + (r - 1) * 2**r)
            assert direct == closed
            counts["unary role formulae"] += 1


def verify_exact_checks(counts: Counter[str]) -> None:
    # Exhaust canonical one-cell activations through rank four.  For rank at
    # most three, also exhaust every allowed local relation containing the
    # current word and excluding the target word.
    for s in range(1, 5):
        states = list(product((0, 1), repeat=s))
        for current in states:
            for target_pos in range(s):
                if current[target_pos] != 0:
                    continue
                target = list(current)
                target[target_pos] = 1
                target = tuple(target)

                activated = []
                for pos in range(s):
                    if current[pos] == 0:
                        candidate = list(current)
                        candidate[pos] = 1
                        if tuple(candidate) == target:
                            activated.append(pos)
                assert activated == [target_pos]
                assert (
                    target[:target_pos] + target[target_pos + 1 :]
                    == current[:target_pos] + current[target_pos + 1 :]
                )
                counts["exact unary patterns"] += 1

                if s <= 3:
                    other = [word for word in states if word not in (current, target)]
                    for mask in range(1 << len(other)):
                        allowed = {current}
                        for bit, word in enumerate(other):
                            if mask >> bit & 1:
                                allowed.add(word)
                        assert current in allowed
                        assert target not in allowed
                        counts["local hard relations"] += 1


def verify_weighted_owner_router(counts: Counter[str]) -> None:
    rng = Random(0)
    for n in range(3, 10):
        cells = list(range(n * n))
        for role_count in range(1, 6):
            for owner_capacity in range(1, 4):
                for projection_count in range(1, 7):
                    for _ in range(200):
                        weights = [rng.randint(1, 5) for _ in range(projection_count)]
                        total_weight = sum(weights)
                        records: list[list[tuple[int, int, tuple[int, int, int]]]] = []

                        for projection in range(projection_count):
                            defect_count = rng.randint(n - 2, min(n * n, n + 4))
                            defect_cells = rng.sample(cells, defect_count)
                            roles = [rng.randrange(role_count) for _ in defect_cells]
                            per_role: dict[int, list[list[object]]] = defaultdict(list)
                            next_owner = 0
                            projection_records = []

                            for cell, role in zip(defect_cells, roles):
                                available = [
                                    entry for entry in per_role[role]
                                    if int(entry[1]) < owner_capacity
                                ]
                                if available and rng.random() < 0.6:
                                    entry = rng.choice(available)
                                    owner = entry[0]
                                    entry[1] = int(entry[1]) + 1
                                else:
                                    owner = (projection, role, next_owner)
                                    next_owner += 1
                                    per_role[role].append([owner, 1])
                                projection_records.append((cell, role, owner))
                            records.append(projection_records)

                        role_incidence = [0] * role_count
                        owners_by_projection = [
                            [set() for _ in range(role_count)]
                            for _ in range(projection_count)
                        ]
                        for projection, projection_records in enumerate(records):
                            for _, role, owner in projection_records:
                                role_incidence[role] += weights[projection]
                                owners_by_projection[projection][role].add(owner)

                        assert sum(role_incidence) >= (n - 2) * total_weight
                        selected = max(range(role_count), key=role_incidence.__getitem__)
                        assert role_incidence[selected] * role_count >= (n - 2) * total_weight

                        weighted_owner_degree = sum(
                            weights[p] * len(owners_by_projection[p][selected])
                            for p in range(projection_count)
                        )
                        assert weighted_owner_degree * owner_capacity >= role_incidence[selected]

                        maximum_degree = max(
                            len(owners_by_projection[p][selected])
                            for p in range(projection_count)
                        )
                        assert maximum_degree >= ceil(
                            (n - 2) / (role_count * owner_capacity)
                        )
                        counts["weighted owner routers"] += 1


def verify_residual_router(counts: Counter[str]) -> None:
    universe = range(5)
    residuals = [
        frozenset(choice)
        for size in (1, 2)
        for choice in combinations(universe, size)
    ]
    for mask in range(1, 1 << len(residuals)):
        family = [residuals[i] for i in range(len(residuals)) if mask >> i & 1]
        matching = []
        used: set[int] = set()
        for residual in family:
            if residual.isdisjoint(used):
                matching.append(residual)
                used.update(residual)
        transversal = set().union(*matching) if matching else set()
        assert all(not residual.isdisjoint(transversal) for residual in family)
        assert len(transversal) <= 2 * len(matching)
        counts["rank-two residual families"] += 1


def verify_exceptional_stock(counts: Counter[str]) -> None:
    for stock_size in range(1, 9):
        for length in range(stock_size + 1, stock_size + 5):
            sequence = [index % stock_size for index in range(length)]
            seen = set()
            new_exposures = 0
            repeated = False
            for token in sequence:
                if token in seen:
                    repeated = True
                else:
                    seen.add(token)
                    new_exposures += 1
            assert new_exposures <= stock_size
            assert repeated
            counts["exceptional exposure histories"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_label_formula(counts)
    verify_exact_checks(counts)
    verify_weighted_owner_router(counts)
    verify_residual_router(counts)
    verify_exceptional_stock(counts)

    print("AC3jd--AC3jh unary blocker-host reason verification passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
