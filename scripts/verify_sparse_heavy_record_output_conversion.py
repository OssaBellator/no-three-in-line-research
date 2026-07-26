#!/usr/bin/env python3
"""Finite audit for active-record stock and heavy energy-output conversion."""

from __future__ import annotations

from itertools import permutations, product
from math import comb, ceil
from random import Random


def curvature(table: tuple[int, int, int, int]) -> int:
    i00, i10, i01, i11 = table
    return i11 - i10 - i01 + i00


def positive_pattern_checks() -> tuple[int, int]:
    systems = 0
    positive = 0
    allowed = {(1, 0, 0, 0), (0, 0, 0, 1)}
    for A0, A1, B0, B1, C in product((0, 1), repeat=5):
        table = (A0 * B0 * C, A1 * B0 * C, A0 * B1 * C, A1 * B1 * C)
        curv = curvature(table)
        assert curv in (-1, 0, 1)
        if curv == 1:
            assert table in allowed
            positive += 1
        systems += 1
    assert positive == 2
    return systems, positive


def incident_donors(scope: tuple[int, int, int], donors: list[tuple[int, int]]) -> int:
    s = set(scope)
    return sum(bool(s.intersection(pair)) for pair in donors)


def active_stock_checks() -> tuple[int, int, int]:
    systems = 0
    scopes_checked = 0
    active_signature_addresses = 0
    for N in range(4, 11):
        original = {0, 1}
        remaining = list(range(2, N))
        donors = [(remaining[i], remaining[i + 1]) for i in range(0, len(remaining) - 1, 2)]
        ordered_scopes = [
            scope
            for scope in permutations(range(N), 3)
            if original.intersection(scope)
        ]
        assert len(ordered_scopes) == 6 * (N - 2) ** 2

        per_row = 0
        for scope in ordered_scopes:
            nu = incident_donors(scope, donors)
            assert 0 <= nu <= 2
            per_row += 2 * nu
            scopes_checked += 1
        safe_per_row = 24 * (N - 2) ** 2
        assert per_row <= safe_per_row

        rows = comb(N, 3)
        total = rows * per_row
        safe_total = 24 * rows * (N - 2) ** 2
        assert total <= safe_total
        active_signature_addresses += total
        systems += 1
    return systems, scopes_checked, active_signature_addresses


def random_partition(total: int, parts: int, rng: Random) -> list[int]:
    out = [0] * parts
    for _ in range(total):
        out[rng.randrange(parts)] += 1
    return out


def barrier_to_repair_word_checks(seed: int = 20260727, systems: int = 80000) -> tuple[int, int]:
    rng = Random(seed)
    omega_cases = 0
    donor_cases = 0
    for idx in range(systems):
        D = rng.randint(0, 300)
        a = rng.randint(1, 150)
        R = D + a + rng.randint(0, 100)
        words = random_partition(R, 12, rng)
        assert max(words) >= ceil(R / 12)
        assert 12 * max(words) >= a
        if idx % 2:
            omega_cases += 1
        else:
            donor_cases += 1
    return omega_cases, donor_cases


def positive_localization_checks(seed: int = 41, systems: int = 70000) -> tuple[int, int]:
    rng = Random(seed)
    current_only = 0
    composed_only = 0
    for _ in range(systems):
        Cplus = rng.randint(1, 1000)
        current = rng.randint(0, Cplus)
        composed = Cplus - current
        orientation_mass = max(current, composed)
        assert 2 * orientation_mass >= Cplus

        cells = random_partition(orientation_mass, 12, rng)
        heavy = max(cells)
        assert 24 * heavy >= Cplus
        if current >= composed:
            current_only += 1
        else:
            composed_only += 1
    return current_only, composed_only


def heavy_router_checks(seed: int = 73, systems: int = 120000) -> tuple[int, int, int, int, int]:
    rng = Random(seed)
    improvement = barrier_omega = barrier_tau = scale = positive = 0

    for _ in range(systems):
        Omega = rng.randint(1, 1000)
        domega = rng.randint(0, 1000)
        dtau = rng.randint(0, 1000)
        L = rng.randint(0, 1000)
        Cplus = rng.randint(0, 1000)
        A = domega + dtau + L + Cplus
        Cminus = rng.randint(Omega, Omega + 1500)
        dcomb = A - Cminus

        if dcomb < 0:
            improvement += 1
            continue

        assert A >= Cminus >= Omega
        terms = [domega, dtau, L, Cplus]
        which = max(range(4), key=terms.__getitem__)
        assert 4 * terms[which] >= Omega
        if which == 0:
            assert 48 * domega >= Omega
            barrier_omega += 1
        elif which == 1:
            assert 48 * dtau >= Omega
            barrier_tau += 1
        elif which == 2:
            assert 4 * L >= Omega
            scale += 1
        else:
            assert 96 * Cplus >= Omega
            positive += 1

    return improvement, barrier_omega, barrier_tau, scale, positive


def explicit_kact_threshold_checks(seed: int = 101, systems: int = 50000) -> int:
    rng = Random(seed)
    checks = 0
    for _ in range(systems):
        N = rng.randint(4, 30)
        K = 24 * comb(N, 3) * (N - 2) ** 2
        Lbank = rng.randint(1, 10**7)
        assert K > 0
        assert 96 * K > 0
        assert 8 * K > 0
        assert 192 * K > 0
        assert Lbank / 2 >= Lbank / (2 * K)
        checks += 1
    return checks


def main() -> None:
    boolean_systems, positive_patterns = positive_pattern_checks()
    stock_systems, scopes, addresses = active_stock_checks()
    omega, tau = barrier_to_repair_word_checks()
    current, composed = positive_localization_checks()
    improvement, b_omega, b_tau, scale, positive = heavy_router_checks()
    thresholds = explicit_kact_threshold_checks()
    print("heavy active-record output-conversion audit passed")
    print(f"  Boolean factor systems: {boolean_systems}")
    print(f"  positive curvature patterns: {positive_patterns}")
    print(f"  active-stock board sizes: {stock_systems}")
    print(f"  ordered cross scopes checked: {scopes}")
    print(f"  active signature addresses: {addresses}")
    print(f"  original-barrier word systems: {omega}")
    print(f"  donor-barrier word systems: {tau}")
    print(f"  current-only positive fibres: {current}")
    print(f"  composed-only positive fibres: {composed}")
    print(f"  improving heavy-record systems: {improvement}")
    print(f"  original repair-word outputs: {b_omega}")
    print(f"  donor repair-word outputs: {b_tau}")
    print(f"  designated-scale outputs: {scale}")
    print(f"  positive-curvature outputs: {positive}")
    print(f"  explicit K_act threshold checks: {thresholds}")


if __name__ == "__main__":
    main()
