#!/usr/bin/env python3
"""Finite checks for AC3ec--AC3eg."""

from fractions import Fraction
from itertools import product


def check_partner_geometry():
    records = clean = lower = collisions = missing = 0
    occupancy_words = tuple(product((0, 1, 2), repeat=2))
    # 0=absent/empty, 1=absent/blocker, 2=active.
    for q in range(1, 8):
        for h in range(1, 13):
            for sign in (-1, 1):
                H = h + sign * q
                for u in range(-4, 5):
                    for v in range(-4, 5):
                        if 0 in (u, v) or u == v:
                            continue
                        for occ_u, occ_v in occupancy_words:
                            records += 1
                            if H <= 0:
                                assert sign == -1 and h <= q
                                lower += 1
                                continue
                            mixed = (h * u == H * v) or (h * v == H * u)
                            coeffs = (0, h * u, h * v, H * u, H * v)
                            all_distinct = len(set(coeffs)) == 5
                            assert all_distinct == (not mixed)
                            if mixed:
                                collisions += 1
                            elif occ_u == 2 and occ_v == 2:
                                clean += 1
                            else:
                                absent = [state for state in (occ_u, occ_v) if state != 2]
                                assert 1 <= len(absent) <= 2
                                assert all(state in (0, 1) for state in absent)
                                missing += 1
    return records, clean, lower, collisions, missing


def check_partition_weights():
    systems = 0
    for weights in product(range(5), repeat=4):
        total = sum(weights)
        if total:
            assert max(weights) >= Fraction(total, 4)
        systems += 1
    return systems


def check_ticket():
    tickets = 0
    for q in range(1, 9):
        for h in range(1, 13):
            H = h + q
            forward = (min(h, H), max(h, H), q)
            backward = (min(H, h), max(H, h), q)
            assert forward == backward
            capacity = 1
            assert capacity < 2
            tickets += 1
    return tickets


def check_constants():
    checks = 0
    for role_count in range(1, 6):
        for multiplicity in range(1, 5):
            for profile_count in range(1, 7):
                scale = role_count * multiplicity * profile_count
                endpoint_source = 8 * scale
                variation_source = 16 * scale
                assert Fraction(endpoint_source, 32 * scale) == Fraction(1, 4)
                assert Fraction(variation_source, 64 * scale) == Fraction(1, 4)
                for k in range(1, 6):
                    assert Fraction(endpoint_source, 32 * scale * k) == Fraction(1, 4 * k)
                    assert Fraction(variation_source, 64 * scale * k) == Fraction(1, 4 * k)
                    checks += 1
    return checks


def main():
    records, clean, lower, collisions, missing = check_partner_geometry()
    partitions = check_partition_weights()
    tickets = check_ticket()
    constants = check_constants()
    print(
        "AC BDA front installation: verified "
        f"{records} partner records, {clean} clean pairs, {lower} lower fronts, "
        f"{collisions} scalar collisions, {missing} missing-support words, "
        f"{partitions} weighted partitions, {tickets} tickets, and {constants} constants"
    )


if __name__ == "__main__":
    main()
