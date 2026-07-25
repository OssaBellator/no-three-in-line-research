#!/usr/bin/env python3
"""Finite checks for CMR378--CMR384.

The checks cover exact host churn under an old-cell-clean rematching, the flat
p-adic fine-token return profile of a coarse block, one-pass aggregate bounds,
reset-multiplicity thresholds, and the primitive-line witness trichotomy used in
CMR384.
"""

from __future__ import annotations

from math import gcd


def valuation(value: int, prime: int) -> int:
    """Return v_p(value) for a nonzero integer."""

    assert value != 0
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def verify_exact_host_churn() -> None:
    """Check H' minus H = M for cyclic disjoint matchings."""

    for side in range(5, 18):
        old = {(column, column) for column in range(side)}
        opposite = {
            (column, (column + 1) % side) for column in range(side)
        }
        replacement = {
            (column, (column + 2) % side) for column in range(side)
        }

        assert old.isdisjoint(opposite)
        assert old.isdisjoint(replacement)
        assert opposite.isdisjoint(replacement)

        complete = {
            (column, row)
            for column in range(side)
            for row in range(side)
        }
        before = complete - old - opposite
        after = complete - replacement - opposite

        assert after - before == old
        assert before - after == replacement

        # A persistent deletion mask can only suppress returned old edges.
        deleted = {edge for edge in old if edge[0] % 2 == 0}
        residual_before = before - deleted
        residual_after = after - deleted
        assert residual_after - residual_before == old - deleted


def affine_prefix_permutation(prime: int, depth: int, shift: int) -> tuple[int, ...]:
    """Return a deterministic affine permutation of residues modulo p^depth."""

    modulus = prime**depth
    if modulus == 1:
        return (0,)
    multiplier = prime + 1
    assert gcd(multiplier, modulus) == 1
    return tuple(
        (multiplier * residue + shift) % modulus
        for residue in range(modulus)
    )


def verify_flat_token_profile() -> None:
    """Check the exact t/p^b return count and unique compatible block."""

    for prime in (3, 5, 7):
        for height in range(2, 5):
            side = prime**height
            for coarse_depth in range(height - 1):
                coarse_modulus = prime**coarse_depth
                row_prefixes = affine_prefix_permutation(
                    prime, coarse_depth, coarse_depth + 1
                )
                assert sorted(row_prefixes) == list(range(coarse_modulus))

                for fine_depth in range(coarse_depth + 1, height):
                    fine_modulus = prime**fine_depth
                    expected = side // fine_modulus

                    for token_residue in range(fine_modulus):
                        compatible_blocks = [
                            block_residue
                            for block_residue, row_residue in enumerate(row_prefixes)
                            if token_residue % coarse_modulus == row_residue
                        ]
                        assert len(compatible_blocks) == 1

                        block_residue = compatible_blocks[0]
                        row_residue = row_prefixes[block_residue]
                        row_fibre = [
                            row
                            for row in range(side)
                            if row % coarse_modulus == row_residue
                        ]
                        returned = [
                            row
                            for row in row_fibre
                            if row % fine_modulus == token_residue
                        ]
                        assert len(returned) == expected

                        for other_block, other_row_residue in enumerate(row_prefixes):
                            if other_block == block_residue:
                                continue
                            other_fibre = [
                                row
                                for row in range(side)
                                if row % coarse_modulus == other_row_residue
                            ]
                            assert not any(
                                row % fine_modulus == token_residue
                                for row in other_fibre
                            )


def verify_one_pass_sums() -> None:
    """Check CMR381--CMR382 exactly at the displayed arithmetic level."""

    for prime in (3, 5, 7, 11):
        directions = prime + 1
        for height in range(1, 8):
            side = prime**height
            aggregate = 0

            for depth in range(1, height):
                token_count = directions * prime**depth
                per_token = 2 * depth * side // prime**depth
                aggregate += token_count * per_token

                initial_stock = side * side // prime**depth
                executable_bound = initial_stock + per_token
                assert executable_bound == (
                    side * side + 2 * depth * side
                ) // prime**depth

            assert aggregate == directions * side * height * (height - 1)


def verify_reset_multiplicity_threshold() -> None:
    """Check the ancestor-slot pigeonhole threshold from CMR383."""

    for depth in range(1, 12):
        slots = 2 * depth
        for cap in range(6):
            bounded_counts = [cap] * slots
            assert sum(bounded_counts) <= slots * cap

            if slots:
                violating_counts = bounded_counts.copy()
                violating_counts[0] += 1
                assert sum(violating_counts) > slots * cap
                assert max(violating_counts) > cap

        for prime in (3, 5, 7):
            side = prime ** (depth + 1)
            unit_return = side // prime**depth
            for cap in range(5):
                maximum_return = slots * cap * unit_return
                assert maximum_return == 2 * depth * cap * side // prime**depth


def verify_witness_trichotomy() -> None:
    """Enumerate the valuation alternatives underlying CMR384."""

    for prime in (3, 5, 7):
        modulus = prime**4
        for gap in range(1, modulus):
            b = valuation(gap, prime)
            for parameter in range(1, modulus):
                if parameter == gap:
                    continue
                c = valuation(parameter, prime)
                e = valuation(parameter - gap, prime)

                two_smallest = sorted((b, c, e))[:2]
                assert two_smallest[0] == two_smallest[1]

                if c < b:
                    assert e == c
                elif c > b:
                    assert e == b
                    assert c > b
                else:
                    assert e >= b
                    if e > b:
                        assert e > c


def main() -> None:
    verify_exact_host_churn()
    verify_flat_token_profile()
    verify_one_pass_sums()
    verify_reset_multiplicity_threshold()
    verify_witness_trichotomy()
    print(
        "verified coarse reset profile: exact host churn, flat p-adic token "
        "returns, one-pass O_p(t log^2 t) sum, reset multiplicity, and witness "
        "routing"
    )


if __name__ == "__main__":
    main()
