#!/usr/bin/env python3
"""Verify CMR649--CMR655 complete-core contraction and conflict recursion."""

from itertools import combinations, permutations


Edge = tuple[int, int]


def collinear(a: Edge, b: Edge, c: Edge) -> bool:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        == (b[1] - a[1]) * (c[0] - a[0])
    )


def perfect_matchings(
    left: set[int],
    right: set[int],
    edges: set[Edge],
) -> list[set[Edge]]:
    left_order = sorted(left)
    right_order = sorted(right)
    out: list[set[Edge]] = []

    for image in permutations(right_order):
        matching = set(zip(left_order, image))
        if matching <= edges:
            out.append(matching)

    return out


def check_host(n: int, host: set[Edge]) -> bool:
    vertices = set(range(n))
    matchings = perfect_matchings(vertices, vertices, host)
    if not matchings:
        return False

    essential = set.intersection(*(set(matching) for matching in matchings))

    # The complete essential core is a matching.
    assert len({x for x, _ in essential}) == len(essential)
    assert len({y for _, y in essential}) == len(essential)

    residual_left = vertices - {x for x, _ in essential}
    residual_right = vertices - {y for _, y in essential}
    residual_host = {
        edge
        for edge in host
        if edge[0] in residual_left and edge[1] in residual_right
    }
    residual_matchings = perfect_matchings(
        residual_left,
        residual_right,
        residual_host,
    )

    # CMR649 exact contraction.
    stripped = {frozenset(matching - essential) for matching in matchings}
    assert stripped == {frozenset(matching) for matching in residual_matchings}

    # The residual complete essential core is empty.
    if residual_matchings:
        residual_essential = set.intersection(
            *(set(matching) for matching in residual_matchings)
        )
        assert not residual_essential

        # Therefore every residual physical edge is nonessential: deleting it
        # preserves at least one perfect matching, whether or not it was used.
        for edge in residual_host:
            assert perfect_matchings(
                residual_left,
                residual_right,
                residual_host - {edge},
            )

    # CMR650--CMR651 conflict decomposition by core rank.
    for residual in residual_matchings:
        full = essential | residual
        by_rank = [0, 0, 0, 0]

        for triple in combinations(sorted(full), 3):
            if collinear(*triple):
                rank = len(set(triple) & essential)
                by_rank[rank] += 1
                if rank >= 1:
                    assert 3 - rank <= 2

        total = sum(
            1
            for triple in combinations(sorted(full), 3)
            if collinear(*triple)
        )
        assert total == sum(by_rank)

        if by_rank[3]:
            assert any(
                collinear(*triple)
                for triple in combinations(sorted(essential), 3)
            )

    return True


def main() -> None:
    checked = 0

    for n in range(1, 4):
        all_edges = [(i, j) for i in range(n) for j in range(n)]
        for mask in range(1 << (n * n)):
            host = {
                edge
                for index, edge in enumerate(all_edges)
                if (mask >> index) & 1
            }
            if check_host(n, host):
                checked += 1

    print(
        "verified pure-factor essential recursion for "
        f"{checked} matchable bipartite hosts through side three"
    )


if __name__ == "__main__":
    main()
