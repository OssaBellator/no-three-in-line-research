#!/usr/bin/env python3
"""Exhaust BDA5u--BDA5v on small scalar-lift profiles."""

from itertools import combinations, product
from math import ceil, gcd


def primitive_vectors(bound):
    return [
        (x, y)
        for x in range(1, bound + 1)
        for y in range(-bound, bound + 1)
        if y != 0 and gcd(x, abs(y)) == 1
    ]


def same_projective_class(left, right, modulus):
    if modulus == 1:
        return True
    x, y = left
    u, v = right
    return any(
        gcd(scale, modulus) == 1
        and (u - scale * x) % modulus == 0
        and (v - scale * y) % modulus == 0
        for scale in range(modulus)
    )


def maximum_disjoint_adjacent(occupied, step):
    count = 0
    index = 0
    while index + 1 < len(occupied):
        if occupied[index + 1] - occupied[index] == step:
            count += 1
            index += 2
        else:
            index += 1
    return count


def verify(bound=6, maximum_q=10, maximum_height=24):
    vectors = primitive_vectors(bound)
    congruence_checks = 0
    projective_checks = 0
    chain_checks = 0

    for q in range(2, maximum_q + 1):
        for d, e in product(vectors, repeat=2):
            a, b = d
            r, s = e
            determinant = a * s - b * r
            if determinant == 0:
                continue

            common = gcd(abs(determinant), q)
            step = q // common

            for residue in range(q):
                solutions = [
                    h
                    for h in range(0, 3 * q + 1)
                    if (h * determinant - residue) % q == 0
                ]
                if residue % common:
                    assert not solutions
                else:
                    assert len({h % step for h in solutions}) == 1
                congruence_checks += 1

            assert same_projective_class(d, e, common)
            projective_checks += 1

            norm_d = max(abs(a), abs(b))
            norm_e = max(abs(r), abs(s))
            slope_gap = abs(b / a - s / r)
            assert slope_gap + 1e-12 >= common / (norm_d * norm_e)

            for height in range(1, maximum_height + 1):
                for residue in range(step):
                    slots = [
                        h
                        for h in range(1, height + 1)
                        if h % step == residue
                    ]
                    slot_count = len(slots)
                    if slot_count:
                        assert height >= 1 + step * (slot_count - 1)
                        assert slot_count <= ceil(height * common / q)

                    if slot_count > 8:
                        continue
                    for size in range(1, slot_count + 1):
                        for occupied in combinations(slots, size):
                            adjacent = sum(
                                occupied[index + 1] - occupied[index] == step
                                for index in range(size - 1)
                            )
                            lower = max(0, 2 * size - slot_count - 1)
                            assert adjacent >= lower
                            assert maximum_disjoint_adjacent(occupied, step) >= ceil(lower / 2)
                            for index in range(size - 1):
                                if occupied[index + 1] - occupied[index] == step:
                                    increment = step * determinant
                                    assert increment == q * (determinant // common)
                            chain_checks += 1

    return congruence_checks, projective_checks, chain_checks


def main():
    congruences, projective, chains = verify()
    print(
        "BDA scalar-lift spacing: verified "
        f"{congruences} congruences, {projective} projective pairs, "
        f"and {chains} occupied chains"
    )


if __name__ == "__main__":
    main()
