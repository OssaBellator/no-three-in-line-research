#!/usr/bin/env python3
"""Verify AC3dj--AC3dm on finite reflected scalar systems."""

from itertools import product
from math import gcd


def verify_profile_counts(maximum_q=16, maximum_bound=10):
    checks = 0
    for denominator_bound in range(2, maximum_q + 1):
        for coefficient_bound in range(maximum_bound + 1):
            profiles = {
                (q, coefficient, residue)
                for q in range(2, denominator_bound + 1)
                for coefficient in range(-coefficient_bound, coefficient_bound + 1)
                for residue in range(q)
            }
            predicted = (2 * coefficient_bound + 1) * sum(
                range(2, denominator_bound + 1)
            )
            assert len(profiles) == predicted
            checks += 1
    return checks


def verify_slots(maximum_q=80, coefficient_bound=24):
    congruence_checks = 0
    gap_checks = 0

    for q in range(2, maximum_q + 1):
        for coefficient in range(-coefficient_bound, coefficient_bound + 1):
            divisor = gcd(abs(2 * coefficient), q)
            modulus = q // divisor
            for residue in range(q):
                scales = [
                    h
                    for h in range(0, 3 * q + 1)
                    if coefficient * (2 * h + q) % q == residue
                ]
                if not scales:
                    continue
                base = scales[0] % modulus
                assert all(scale % modulus == base for scale in scales)
                congruence_checks += 1

                represented = set(scales)
                for scale in scales:
                    if scale + q in represented:
                        left_index = (scale - scales[0]) // modulus
                        right_index = (scale + q - scales[0]) // modulus
                        assert right_index - left_index == divisor
                        gap_checks += 1

    return congruence_checks, gap_checks


def path_parity(edge_start, step):
    residue = edge_start % step
    path_index = (edge_start - residue) // step
    return path_index % 2


def verify_weighted_overlap(maximum_length=7, maximum_cap=3):
    inequality_checks = 0
    parity_checks = 0
    multi_anchor_checks = 0

    for length in range(1, maximum_length + 1):
        for step in range(1, length + 1):
            for cap in range(1, maximum_cap + 1):
                for weights in product(range(cap + 1), repeat=length):
                    total = sum(weights)
                    overlap = sum(
                        min(weights[index], weights[index + step])
                        for index in range(length - step)
                    )
                    lower = max(0, 2 * total - cap * (length + step))
                    assert overlap >= lower
                    inequality_checks += 1

                    parity_totals = [0, 0]
                    parity_edges = [[], []]
                    for index in range(length - step):
                        parity = path_parity(index, step)
                        value = min(weights[index], weights[index + step])
                        parity_totals[parity] += value
                        parity_edges[parity].append((index, index + step))
                    assert max(parity_totals) * 2 >= overlap
                    for edges in parity_edges:
                        used = set()
                        for left, right in edges:
                            assert left not in used
                            assert right not in used
                            used.add(left)
                            used.add(right)
                    parity_checks += 1

    # Additive check over two anchors with possibly different weight vectors.
    for length in range(1, 6):
        for step in range(1, length + 1):
            cap = 2
            vectors = list(product(range(cap + 1), repeat=length))
            for first in vectors[: min(40, len(vectors))]:
                for second in vectors[: min(40, len(vectors))]:
                    total = sum(first) + sum(second)
                    overlap = sum(
                        min(first[index], first[index + step])
                        + min(second[index], second[index + step])
                        for index in range(length - step)
                    )
                    lower = max(0, 2 * total - 2 * cap * (length + step))
                    assert overlap >= lower
                    multi_anchor_checks += 1

    return inequality_checks, parity_checks, multi_anchor_checks


def verify_composition(maximum_weight=60):
    checks = 0
    for total in range(1, maximum_weight + 1):
        for profile_count in range(1, 30):
            quotient, remainder = divmod(total, profile_count)
            largest = quotient + (1 if remainder else 0)
            assert largest * profile_count >= total
            checks += 1
    return checks


def main():
    profiles = verify_profile_counts()
    slots, gaps = verify_slots()
    inequalities, parities, anchors = verify_weighted_overlap()
    compositions = verify_composition()
    print(
        "AC BDA reflected role: verified "
        f"{profiles} profile counts, {slots} reflected congruence classes, "
        f"{gaps} q-step slot gaps, {inequalities} overlap inequalities, "
        f"{parities} parity matchings, {anchors} multi-anchor sums, "
        f"and {compositions} composition bounds"
    )


if __name__ == "__main__":
    main()
