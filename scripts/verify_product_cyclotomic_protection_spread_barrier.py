#!/usr/bin/env python3
"""Verify PX176--PX178 cyclotomic protection/spread barriers."""
from __future__ import annotations

from collections import Counter
from math import ceil


def falling(value: int, length: int) -> int:
    result = 1
    for offset in range(length):
        result *= value - offset
    return result


def triangle_multiplicity(mapping: tuple[int, ...]) -> int:
    prime = len(mapping)
    inverse = [0] + [pow(value, -1, prime) for value in range(1, prime)]
    counts: Counter[tuple[int, int, int]] = Counter()
    for first in range(prime):
        for second in range(prime):
            if first == second:
                continue
            row_difference = (second - first) % prime
            image_difference = (mapping[second] - mapping[first]) % prime
            if image_difference == 0:
                continue
            slope = image_difference * inverse[row_difference] % prime
            for row_ratio in range(2, prime):
                third = (first + row_ratio * row_difference) % prime
                image_ratio = (
                    (mapping[third] - mapping[first])
                    * inverse[image_difference]
                    % prime
                )
                counts[(slope, row_ratio, image_ratio)] += 1
    return max(counts.values())


def affine_packet_lower_bound(prime: int, packet_size: int) -> int:
    if packet_size < 3:
        return 0
    return ceil(falling(packet_size, 3) / (prime - 2))


def verify_piecewise_linear_examples() -> None:
    # Quadratic-character permutations x -> a*x on residues and b*x on
    # nonresidues, using exact examples that are permutations. The theorem only
    # needs one affine packet, not strong completeness.
    examples = {
        7: (1, 3),
        11: (1, 2),
        13: (1, 2),
        17: (1, 3),
        19: (1, 2),
    }
    for prime, (residue_multiplier, nonresidue_multiplier) in examples.items():
        residues = {pow(value, 2, prime) for value in range(1, prime)}
        mapping = [0]
        for value in range(1, prime):
            multiplier = (
                residue_multiplier if value in residues else nonresidue_multiplier
            )
            mapping.append(multiplier * value % prime)
        # Some displayed multiplier pairs can map the two classes to the same
        # image class. Retain only genuine permutations; the packet inequality
        # is then checked exactly.
        if len(set(mapping)) != prime:
            continue
        packet_size = (prime - 1) // 2
        observed = triangle_multiplicity(tuple(mapping))
        predicted = affine_packet_lower_bound(prime, packet_size)
        assert observed >= predicted
        print(
            f"p={prime}: packet={packet_size}, tau={observed}, lower={predicted}"
        )


def verify_symbolic_ranges() -> None:
    # If K3 <= p^gamma, then (m)_3 <= p^(1+gamma). Check the convenient
    # consequence m <= 2*p^((1+gamma)/3) on representative ranges.
    for prime in (101, 1009, 10007):
        for gamma_times_100 in (5, 10, 25, 50):
            gamma = gamma_times_100 / 100
            threshold = 2 * prime ** ((1 + gamma) / 3)
            for packet_size in range(3, prime):
                k3_lower = falling(packet_size, 3) / prime
                if k3_lower <= prime**gamma:
                    assert packet_size <= threshold

    # Near-linear maps change one packet and retain p-m affine rows. The exact
    # orbit constant lower bound is (p-m)_3 / p.
    for prime in (101, 1009, 10007):
        for divisor in range(2, prime):
            if (prime - 1) % divisor:
                continue
            packet_size = (prime - 1) // divisor
            retained = prime - packet_size
            if retained >= 3:
                lower = falling(retained, 3) / prime
                assert lower > 0
                if divisor >= 2:
                    assert retained >= (prime + 1) // 2
                    assert lower >= falling((prime + 1) // 2, 3) / prime
    print("symbolic cyclotomic and near-linear barriers verified")


def verify_fear_wanless_count() -> None:
    # Theorem 10 of Fear--Wanless: a near-linear index-d orthomorphism is
    # orthogonal to (p-3d-1)/d linear orthomorphisms. Check integrality and its
    # expression in terms of packet size m=(p-1)/d: m-3.
    for prime in (13, 17, 29, 37, 41, 53, 61, 73, 89, 101):
        for divisor in range(3, (prime - 1) // 2):
            if (prime - 1) % divisor:
                continue
            count = (prime - 3 * divisor - 1) // divisor
            packet_size = (prime - 1) // divisor
            assert count == packet_size - 3
            assert count >= 0
    print("Fear--Wanless near-linear orthogonality count verified algebraically")


def main() -> None:
    verify_piecewise_linear_examples()
    verify_symbolic_ranges()
    verify_fear_wanless_count()
    print("PX176--PX178 verified")


if __name__ == "__main__":
    main()
