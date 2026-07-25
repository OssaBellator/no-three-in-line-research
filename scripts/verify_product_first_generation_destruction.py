#!/usr/bin/env python3
"""Checks for PX240--PX244."""

from __future__ import annotations

import math


def check_loaded_line_formula(max_ell: int = 200) -> None:
    for ell in range(3, max_ell + 1):
        points = set(range(ell))
        triples = {frozenset(triple) for triple in __import__("itertools").combinations(points, 3)}
        for s in range(1, ell + 1):
            moved = set(range(s))
            surviving = {triple for triple in triples if triple.isdisjoint(moved)}
            destroyed = len(triples) - len(surviving)
            exact = math.comb(ell, 3) - math.comb(ell - s, 3)
            assert destroyed == exact
            assert exact >= s * math.comb(ell - s, 2)


def check_layer_channel_envelope(max_ell: int = 300, max_q: int = 30) -> None:
    for ell in range(8, max_ell + 1):
        for q in range(1, max_q + 1):
            s = math.ceil(ell / (2 * q))
            destroyed = math.comb(ell, 3) - math.comb(ell - s, 3)
            assert math.comb(ell - s, 2) >= ell * ell / 32
            assert destroyed >= s * ell * ell / 32
            assert destroyed >= ell**3 / (64 * q)


def check_star_and_radial_injections() -> None:
    for order in range(1, 100):
        star_certificates = {("z", f"p{j}", f"q{j}") for j in range(order)}
        moved_star = {f"q{j}" for j in range(order)}
        assert sum(bool(set(certificate) & moved_star) for certificate in star_certificates) == order

        radial_certificates = {(f"a{j}", f"u{j}", f"v{j}") for j in range(order)}
        moved_radial = {f"a{j}" for j in range(order)}
        assert sum(bool(set(certificate) & moved_radial) for certificate in radial_certificates) == order


def check_linear_sign_threshold() -> None:
    for ell in range(8, 200):
        for q in range(1, 20):
            s = math.ceil(ell / (2 * q))
            destroyed = math.comb(ell, 3) - math.comb(ell - s, 3)
            # The PX244 sufficient condition uses any b with ell^2/32 > b.
            b = ell * ell / 32 - 1e-9
            assert destroyed > b * s


def main() -> None:
    check_loaded_line_formula()
    check_layer_channel_envelope()
    check_star_and_radial_injections()
    check_linear_sign_threshold()
    print("PX240--PX244 first-generation destruction checks passed")


if __name__ == "__main__":
    main()
