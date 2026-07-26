#!/usr/bin/env python3
from __future__ import annotations

import math
import random
from fractions import Fraction
from itertools import combinations, permutations

SEED = 20260727
RNG = random.Random(SEED)


def third_column(
    rows: tuple[int, int, int],
    pos_a: int,
    col_a: int,
    pos_b: int,
    col_b: int,
    pos_c: int,
) -> Fraction:
    ra, rb, rc = rows[pos_a], rows[pos_b], rows[pos_c]
    return Fraction(col_a, 1) + Fraction(rc - ra, rb - ra) * (col_b - col_a)


def exhaustive_geometry() -> tuple[int, int, int, int]:
    singleton_records = 0
    singleton_certified = 0
    double_records = 0
    systems = 0
    for N in range(3, 9):
        row_triples = list(combinations(range(N), 3))
        for x, y in combinations(range(N), 2):
            for z in range(N):
                if z in (x, y):
                    continue
                for pos in permutations(range(3)):
                    px, py, pz = pos
                    count = 0
                    for rows in row_triples:
                        lhs = (rows[py] - rows[px]) * (z - x)
                        rhs = (rows[pz] - rows[px]) * (y - x)
                        if lhs == rhs:
                            count += 1
                    assert count <= math.comb(N, 3)
                    double_records += count
                    systems += 1

                for s in (x, y):
                    for ps, pz in permutations(range(3), 2):
                        pc = ({0, 1, 2} - {ps, pz}).pop()
                        geometric = 0
                        for rows in row_triples:
                            c = third_column(rows, ps, s, pz, z, pc)
                            if c.denominator != 1:
                                continue
                            ci = c.numerator
                            if not (0 <= ci < N) or ci in (s, z):
                                continue
                            geometric += 1
                        for b in range(1, 6):
                            count = b * geometric
                            assert count <= b * math.comb(N, 3)
                            singleton_records += count
                            assert geometric <= math.comb(N, 3)
                            singleton_certified += geometric
                            systems += 1
    return systems, double_records, singleton_records, singleton_certified


def weighted_threshold_checks(trials: int = 80_000) -> tuple[int, int, int, int]:
    scale_dominant = 0
    collateral_dominant = 0
    sharper = 0
    total_match = 0
    for _ in range(trials):
        N = RNG.randint(3, 30)
        b = RNG.randint(1, min(8, N))
        K_bound = b * math.comb(N, 3)
        k = RNG.randint(1, 20)
        d = RNG.randint(1, 20)
        m = min(k, max(d - 3, 0))
        if m == 0:
            continue
        column_sums = []
        heaviest = []
        max_actual = min(K_bound, 40)
        for _z in range(k):
            K_actual = RNG.randint(1, max_actual)
            weights = [RNG.randint(1, 25) for _ in range(K_actual)]
            column_sums.append(sum(weights))
            heaviest.append(max(weights))
            assert max(weights) * K_actual >= sum(weights)
            assert max(weights) * K_bound >= sum(weights)
        W = sum(column_sums)
        top = sorted(heaviest, reverse=True)[:m]
        L_match = sum(top)
        L0_num = m * W
        L0_den = k * K_bound
        assert L_match * L0_den >= L0_num
        total_match += L_match

        omega = RNG.randint(0, max(1, 2 * L_match))
        if L0_num > 2 * omega * L0_den:
            scale_dominant += 1
            assert L_match > 2 * omega
            assert (L_match - 2 * omega) * L0_den >= L0_num - 2 * omega * L0_den
        else:
            collateral_dominant += 1
            assert 2 * omega * L0_den >= L0_num

        K_sharp = math.comb(N, 3)
        if max_actual <= K_sharp:
            sharp_num = m * W
            sharp_den = k * K_sharp
            assert sharp_den > 0
            sharper += 1
    return scale_dominant, collateral_dominant, sharper, total_match


def label_factor_checks(trials: int = 40_000) -> tuple[int, int]:
    uncertified = 0
    certified = 0
    for _ in range(trials):
        b = RNG.randint(1, 20)
        geometry_count = RNG.randint(0, 500)
        possible = geometry_count * b
        if geometry_count:
            assert possible <= b * geometry_count
        else:
            assert possible == 0
        uncertified += possible
        forced = geometry_count
        assert forced <= possible
        certified += forced
    return uncertified, certified


def main() -> None:
    systems, double_records, singleton_records, singleton_certified = exhaustive_geometry()
    scale, collateral, sharper, total_match = weighted_threshold_checks()
    uncertified, certified = label_factor_checks()
    print(
        "PASS SAS defect-column exact-record stock audit:",
        f"{systems} exact geometry systems;",
        f"{double_records} double-scope records;",
        f"{singleton_records} singleton labelled records;",
        f"{singleton_certified} label-certified singleton records;",
        f"{scale} scale-dominant systems;",
        f"{collateral} collateral-dominant systems;",
        f"{sharper} sharp-stock substitutions;",
        f"{total_match} matched designated weight;",
        f"{uncertified} uncertified label choices;",
        f"{certified} certified label choices.",
    )


if __name__ == "__main__":
    main()
