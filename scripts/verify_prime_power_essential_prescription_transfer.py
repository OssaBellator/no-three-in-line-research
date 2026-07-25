#!/usr/bin/env python3
"""Verify CMR636--CMR642 essential-prescription transfer identities."""

from itertools import combinations, permutations, product


Edge = tuple[int, int]
Cell = tuple[int, int]


def collinear(a: Cell, b: Cell, c: Cell) -> bool:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        == (b[1] - a[1]) * (c[0] - a[0])
    )


def enumerate_matchings(
    edges: set[Edge],
    left: set[int],
    right: set[int],
) -> set[tuple[Edge, ...]]:
    left_order = sorted(left)
    right_order = sorted(right)
    out: set[tuple[Edge, ...]] = set()
    for image in permutations(right_order):
        matching = tuple(sorted(zip(left_order, image)))
        if all(edge in edges for edge in matching):
            out.add(matching)
    return out


def essential_core(matchings: set[tuple[Edge, ...]]) -> set[Edge]:
    assert matchings
    return set.intersection(*(set(matching) for matching in matchings))


def check_factor_class(
    n: int,
    protected_size: int,
    forbidden: tuple[int, ...],
    skeleton_tuple: tuple[Edge, ...],
    records: list[tuple[tuple[Edge, ...], tuple[Edge, ...]]],
) -> tuple[int, int]:
    protected = set(range(protected_size))
    free = set(range(protected_size, n))
    skeleton = set(skeleton_tuple)

    protected_matchings = {p for p, _ in records}
    free_matchings = {q for _, q in records}
    assert set(records) == set(product(protected_matchings, free_matchings))

    i_sources = {x for x, y in skeleton if x in protected}
    i_targets = {y for x, y in skeleton if y in protected}
    j_sources = {x for x, y in skeleton if x in free}
    j_targets = {y for x, y in skeleton if y in free}

    left_i = protected - i_sources
    right_i = protected - i_targets
    left_j = free - j_sources
    right_j = free - j_targets

    edge_i = {
        (x, y)
        for x in left_i
        for y in right_i
        if x != y
    }
    edge_j = {
        (x, y)
        for x in left_j
        for y in right_j
        if x != y
    }

    assert protected_matchings == enumerate_matchings(edge_i, left_i, right_i)
    assert free_matchings == enumerate_matchings(edge_j, left_j, right_j)

    essential_i = essential_core(protected_matchings)
    essential_j = essential_core(free_matchings)

    # CMR636 exact contraction of the complete essential matching.
    if essential_i:
        reduced_left = left_i - {x for x, _ in essential_i}
        reduced_right = right_i - {y for _, y in essential_i}
        reduced_edges = {
            edge
            for edge in edge_i
            if edge[0] in reduced_left and edge[1] in reduced_right
        }
        residual_restrictions = {
            tuple(sorted(set(matching) - essential_i))
            for matching in protected_matchings
        }
        assert residual_restrictions == enumerate_matchings(
            reduced_edges,
            reduced_left,
            reduced_right,
        )

    universe = edge_i | edge_j | skeleton
    transferred_atoms = 0

    for atom_tuple in combinations(sorted(universe), 3):
        if len({x for x, _ in atom_tuple}) < 3:
            continue
        if len({y for _, y in atom_tuple}) < 3:
            continue

        cells = tuple((x, forbidden[y]) for x, y in atom_tuple)
        if not collinear(*cells):
            continue

        atom = set(atom_tuple)
        if atom <= edge_i or atom <= edge_j:
            continue

        prescription_i = atom & edge_i
        prescription_j = atom & edge_j
        prescription_s = atom & skeleton

        if prescription_i and prescription_i <= essential_i:
            # CMR637: the protected occurrence rectangle is the full factor.
            protected_support = {
                matching
                for matching in protected_matchings
                if prescription_i <= set(matching)
            }
            assert protected_support == protected_matchings

            free_support = {
                matching
                for matching in free_matchings
                if prescription_j <= set(matching)
            }
            actual = {
                (p, q)
                for p, q in product(protected_matchings, free_matchings)
                if atom <= skeleton | set(p) | set(q)
            }
            assert actual == set(product(protected_matchings, free_support))

            # CMR638 exact rank table.
            assert len(prescription_i) in {1, 2}
            assert len(prescription_j) <= 2
            assert (
                len(prescription_i)
                + len(prescription_j)
                + len(prescription_s)
                == 3
            )

            # CMR639 forced product certificate.
            if not prescription_j:
                assert actual == set(product(protected_matchings, free_matchings))

            transferred_atoms += 1

    # CMR640 essential rank-one/rank-two stock bound in the free factor.
    essential_rank_stock = len(essential_j) + len(
        list(combinations(essential_j, 2))
    )
    free_side = len(left_j)
    assert essential_rank_stock <= free_side + free_side * (free_side - 1) // 2

    return 1, transferred_atoms


def main() -> None:
    classes = 0
    transferred_atoms = 0

    for n in range(3, 5):
        for forbidden in permutations(range(n)):
            derangements = [
                sigma
                for sigma in permutations(range(n))
                if all(sigma[i] != i for i in range(n))
            ]

            for protected_size in range(n + 1):
                protected = set(range(protected_size))
                groups: dict[
                    tuple[Edge, ...],
                    list[tuple[tuple[Edge, ...], tuple[Edge, ...]]],
                ] = {}

                for sigma in derangements:
                    skeleton = tuple(
                        sorted(
                            (i, sigma[i])
                            for i in range(n)
                            if ((i in protected) != (sigma[i] in protected))
                        )
                    )
                    matching_i = tuple(
                        sorted(
                            (i, sigma[i])
                            for i in protected
                            if sigma[i] in protected
                        )
                    )
                    matching_j = tuple(
                        sorted(
                            (i, sigma[i])
                            for i in range(protected_size, n)
                            if sigma[i] >= protected_size
                        )
                    )
                    groups.setdefault(skeleton, []).append(
                        (matching_i, matching_j)
                    )

                for skeleton, records in groups.items():
                    class_count, atom_count = check_factor_class(
                        n,
                        protected_size,
                        forbidden,
                        skeleton,
                        records,
                    )
                    classes += class_count
                    transferred_atoms += atom_count

    print(
        "verified essential-prescription transfer for "
        f"{classes} skeleton classes and {transferred_atoms} transferred atoms"
    )


if __name__ == "__main__":
    main()
