#!/usr/bin/env python3
"""Exhaust RI5o--RI5p on small auxiliary-transposition banks."""

from itertools import combinations, permutations, product
from math import ceil


def matching_cells(perm):
    return {(column, row) for column, row in enumerate(perm)}


def matching_triples(n):
    triples = []
    for columns in combinations(range(n), 3):
        for rows in combinations(range(n), 3):
            for assignment in permutations(rows):
                triples.append(frozenset(zip(columns, assignment, strict=True)))
    return triples


def verify_geometry(maximum_size=5):
    triple_count = 0
    paired_count = 0

    for n in range(3, maximum_size + 1):
        triples = matching_triples(n)

        for blocker in permutations(range(n)):
            old_cells = matching_cells(blocker)

            for c0 in range(n):
                r0 = blocker[c0]

                for c in range(n):
                    if c == c0:
                        continue
                    r_c = blocker[c]
                    vertical = (c0, r_c)
                    horizontal = (c, r0)

                    new_blocker = list(blocker)
                    new_blocker[c0] = r_c
                    new_blocker[c] = r0
                    new_cells = matching_cells(new_blocker)
                    created = {vertical, horizontal}
                    assert new_cells - old_cells == created

                    for triple in triples:
                        if not triple <= new_cells or triple <= old_cells:
                            continue
                        local = triple & created
                        assert local

                        if local == {vertical}:
                            channel = "V"
                        elif local == {horizontal}:
                            channel = "H"
                        else:
                            assert local == created
                            channel = "VH"

                        if channel == "V":
                            assert vertical in triple
                            assert horizontal not in triple
                        elif channel == "H":
                            assert horizontal in triple
                            assert vertical not in triple
                        else:
                            third = next(iter(triple - created))
                            s, t = third
                            assert (
                                (c - c0) * (t - r_c)
                                - (r0 - r_c) * (s - c0)
                                == 0
                            )
                            paired_count += 1

                        triple_count += 1

    return triple_count, paired_count


def verify_pigeonholes(maximum_weight=3, profile_count=3):
    checks = 0
    class_count = 3 * profile_count

    for weights in product(range(maximum_weight + 1), repeat=class_count):
        total = sum(weights)
        if total == 0:
            continue
        assert max(weights) * class_count >= total
        checks += 1

    # RI5p with integer weights and integer beta. This is enough to check the
    # exact ceiling form; the real-weight proof is the same averaging argument.
    for auxiliary_count in range(1, 6):
        for weights in product(range(maximum_weight + 1), repeat=auxiliary_count):
            total = sum(weights)
            if total == 0:
                continue
            for beta in range(1, maximum_weight + 1):
                if max(weights) > beta:
                    continue
                positive = sum(weight > 0 for weight in weights)
                assert positive >= ceil(total / beta)
                checks += 1

    return checks


def main():
    triples, paired = verify_geometry()
    pigeonholes = verify_pigeonholes()
    print(
        "RI crossed-channel localization: verified "
        f"{triples} variable triples, {paired} paired diagonals, "
        f"and {pigeonholes} weighted routers"
    )


if __name__ == "__main__":
    main()
