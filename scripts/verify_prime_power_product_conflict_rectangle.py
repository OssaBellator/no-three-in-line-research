#!/usr/bin/env python3
"""Verify CMR629--CMR635 product-conflict rectangle identities.

The exhaustive range uses every canonical forbidden permutation through side
four.  A few side-five forbidden permutations are also sampled.  Geometry is
always evaluated in the original board coordinates, not in the matching
relabel used to make the forbidden matching diagonal.
"""

from itertools import combinations, permutations, product
from math import comb


Edge = tuple[int, int]
Cell = tuple[int, int]


def collinear(a: Cell, b: Cell, c: Cell) -> bool:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        == (b[1] - a[1]) * (c[0] - a[0])
    )


def original_cell(edge: Edge, forbidden: tuple[int, ...]) -> Cell:
    """Pull a relabelled matching edge back to original board coordinates."""
    source, relabelled_target = edge
    return source, forbidden[relabelled_target]


def has_conflict(edges: tuple[Edge, ...], forbidden: tuple[int, ...]) -> bool:
    for triple in combinations(edges, 3):
        cells = tuple(original_cell(edge, forbidden) for edge in triple)
        if collinear(*cells):
            return True
    return False


def mixed_atom_universe(
    edge_i: set[Edge],
    edge_j: set[Edge],
    skeleton: set[Edge],
    forbidden: tuple[int, ...],
) -> set[tuple[Edge, Edge, Edge]]:
    universe = edge_i | edge_j | skeleton
    atoms: set[tuple[Edge, Edge, Edge]] = set()
    for triple in combinations(sorted(universe), 3):
        if len({x for x, _ in triple}) < 3:
            continue
        if len({y for _, y in triple}) < 3:
            continue
        cells = tuple(original_cell(edge, forbidden) for edge in triple)
        if not collinear(*cells):
            continue
        triple_set = set(triple)
        if triple_set <= edge_i or triple_set <= edge_j:
            continue
        atoms.add(triple)
    return atoms


def check_skeleton_class(
    n: int,
    protected_size: int,
    forbidden: tuple[int, ...],
    skeleton_tuple: tuple[Edge, ...],
    records: list[tuple[tuple[Edge, ...], tuple[Edge, ...]]],
) -> None:
    protected = set(range(protected_size))
    free = set(range(protected_size, n))
    skeleton = set(skeleton_tuple)

    protected_matchings = sorted({p for p, _ in records})
    free_matchings = sorted({q for _, q in records})

    # CMR618 product property, used by the rectangle theorem.
    assert set(records) == set(product(protected_matchings, free_matchings))

    i_sources = {x for x, y in skeleton if x in protected}
    i_targets = {y for x, y in skeleton if y in protected}
    j_sources = {x for x, y in skeleton if x in free}
    j_targets = {y for x, y in skeleton if y in free}

    edge_i = {
        (x, y)
        for x in protected - i_sources
        for y in protected - i_targets
        if x != y
    }
    edge_j = {
        (x, y)
        for x in free - j_sources
        for y in free - j_targets
        if x != y
    }

    atoms = mixed_atom_universe(edge_i, edge_j, skeleton, forbidden)
    carrier = edge_j | skeleton
    complete_universe = edge_i | edge_j | skeleton

    if carrier:
        assert len(atoms) <= len(carrier) * comb(len(complete_universe) - 1, 2)
    else:
        assert not atoms

    free_size = len(free)
    assert len(carrier) <= free_size**2 + 2 * free_size

    pure_clean_i = [
        p for p in protected_matchings if not has_conflict(p, forbidden)
    ]
    pure_clean_j = [q for q in free_matchings if not has_conflict(q, forbidden)]

    # CMR629 exact pure/mixed decomposition and CMR631 rectangle occurrence.
    for p, q in product(protected_matchings, free_matchings):
        state = tuple(sorted(skeleton | set(p) | set(q)))
        conflicts = []
        for triple in combinations(state, 3):
            cells = tuple(original_cell(edge, forbidden) for edge in triple)
            if collinear(*cells):
                conflicts.append(triple)

        pure_i = [triple for triple in conflicts if set(triple) <= set(p)]
        pure_j = [triple for triple in conflicts if set(triple) <= set(q)]
        mixed = [
            triple
            for triple in conflicts
            if triple not in pure_i and triple not in pure_j
        ]
        assert len(conflicts) == len(pure_i) + len(pure_j) + len(mixed)
        assert set(mixed) <= atoms

    for atom in atoms:
        atom_set = set(atom)
        prescription_i = atom_set & edge_i
        prescription_j = atom_set & edge_j
        prescription_s = atom_set & skeleton

        assert len(prescription_i) <= 2
        if not prescription_i:
            assert prescription_s

        p_support = {
            p for p in protected_matchings if prescription_i <= set(p)
        }
        q_support = {q for q in free_matchings if prescription_j <= set(q)}

        actual = {
            (p, q)
            for p, q in product(protected_matchings, free_matchings)
            if atom_set <= skeleton | set(p) | set(q)
        }
        assert actual == set(product(p_support, q_support))

    # CMR632 averaging whenever every pure-clean pair is globally dirty.
    if pure_clean_i and pure_clean_j:
        all_dirty = all(
            has_conflict(
                tuple(sorted(skeleton | set(p) | set(q))),
                forbidden,
            )
            for p, q in product(pure_clean_i, pure_clean_j)
        )
        if all_dirty:
            assert atoms
            best_rectangle = 0
            for atom in atoms:
                atom_set = set(atom)
                prescription_i = atom_set & edge_i
                prescription_j = atom_set & edge_j
                p_count = sum(
                    prescription_i <= set(p) for p in pure_clean_i
                )
                q_count = sum(
                    prescription_j <= set(q) for q in pure_clean_j
                )
                best_rectangle = max(best_rectangle, p_count * q_count)

            assert (
                best_rectangle * len(atoms)
                >= len(pure_clean_i) * len(pure_clean_j)
            )


def check_forbidden_permutation(
    n: int,
    forbidden: tuple[int, ...],
) -> int:
    classes = 0
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
            groups.setdefault(skeleton, []).append((matching_i, matching_j))

        for skeleton, records in groups.items():
            check_skeleton_class(
                n,
                protected_size,
                forbidden,
                skeleton,
                records,
            )
            classes += 1

    return classes


def main() -> None:
    classes = 0

    # Exhaust every canonical forbidden matching through side four.
    for n in range(3, 5):
        for forbidden in permutations(range(n)):
            classes += check_forbidden_permutation(n, forbidden)

    # Sample distinct geometric relabellings at side five.
    n = 5
    samples = [
        tuple(range(n)),
        tuple(reversed(range(n))),
        (1, 3, 0, 4, 2),
    ]
    for forbidden in samples:
        classes += check_forbidden_permutation(n, forbidden)

    print(
        "verified product-conflict rectangles for "
        f"{classes} skeleton classes through the configured ranges"
    )


if __name__ == "__main__":
    main()
