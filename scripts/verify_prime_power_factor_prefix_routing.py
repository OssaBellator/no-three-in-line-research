#!/usr/bin/env python3
"""Verify CMR656--CMR663 factor-prefix routing and child products."""

from itertools import combinations, permutations, product
from math import ceil


Edge = tuple[int, int]
RoutingKey = tuple[
    tuple[tuple[int, int], ...],
    tuple[tuple[int, int], ...],
]


def common_depth(values: set[int], p: int, h: int) -> int:
    assert values
    for depth in range(h, -1, -1):
        modulus = p**depth
        if len({value % modulus for value in values}) == 1:
            return depth
    raise AssertionError("root depth must contain every coordinate")


def perfect_matchings(
    left: set[int],
    right: set[int],
    edges: set[Edge],
) -> set[tuple[Edge, ...]]:
    left_order = sorted(left)
    right_order = sorted(right)
    out: set[tuple[Edge, ...]] = set()

    for image in permutations(right_order):
        matching = tuple(sorted(zip(left_order, image)))
        if all(edge in edges for edge in matching):
            out.add(matching)

    return out


def routing_key(
    matching: tuple[Edge, ...],
    p: int,
    beta: int,
) -> RoutingKey:
    scale = p**beta
    source_routes = tuple(
        sorted((x, (y // scale) % p) for x, y in matching)
    )
    target_routes = tuple(
        sorted((y, (x // scale) % p) for x, y in matching)
    )
    return source_routes, target_routes


def check_host(
    sources: set[int],
    targets: set[int],
    host: set[Edge],
    p: int,
    h: int,
) -> bool:
    matchings = perfect_matchings(sources, targets, host)
    if not matchings:
        return False

    side = len(sources)
    parent_side = p**h
    beta = min(
        common_depth(sources, p, h),
        common_depth(targets, p, h),
    )

    if side >= 2:
        assert beta < h
    if beta == h:
        return True

    scale = p**beta
    source_children = {
        r: {x for x in sources if (x // scale) % p == r}
        for r in range(p)
    }
    target_children = {
        s: {y for y in targets if (y // scale) % p == s}
        for s in range(p)
    }

    source_support = sum(bool(block) for block in source_children.values())
    target_support = sum(bool(block) for block in target_children.values())
    assert max(source_support, target_support) >= 2

    child_side = parent_side // (p ** (beta + 1))
    groups: dict[RoutingKey, set[tuple[Edge, ...]]] = {}

    for matching in matchings:
        transport = [[0 for _ in range(p)] for _ in range(p)]
        for x, y in matching:
            r = (x // scale) % p
            s = (y // scale) % p
            transport[r][s] += 1

        for r in range(p):
            assert sum(transport[r]) == len(source_children[r])
        for s in range(p):
            assert sum(transport[r][s] for r in range(p)) == len(
                target_children[s]
            )

        occupied = sum(
            transport[r][s] > 0
            for r in range(p)
            for s in range(p)
        )
        assert occupied >= max(source_support, target_support)
        assert occupied >= ceil(side / child_side)

        key = routing_key(matching, p, beta)
        groups.setdefault(key, set()).add(matching)

    assert len(groups) <= p ** (2 * side)

    # CMR659 exact Cartesian child factorisation.
    for key, realised in groups.items():
        source_routes = dict(key[0])
        target_routes = dict(key[1])
        child_families: list[set[tuple[Edge, ...]]] = []

        for r in range(p):
            for s in range(p):
                child_sources = {
                    x
                    for x in source_children[r]
                    if source_routes[x] == s
                }
                child_targets = {
                    y
                    for y in target_children[s]
                    if target_routes[y] == r
                }
                assert len(child_sources) == len(child_targets)

                child_host = {
                    edge
                    for edge in host
                    if edge[0] in child_sources and edge[1] in child_targets
                }
                child_families.append(
                    perfect_matchings(
                        child_sources,
                        child_targets,
                        child_host,
                    )
                )

        combined = {
            tuple(sorted(set().union(*(set(part) for part in choice))))
            for choice in product(*child_families)
        }
        assert combined == realised

    return True


def main() -> None:
    p = 2
    h = 2
    parent_side = p**h
    coordinates = range(parent_side)
    checked = 0

    for side in range(1, 4):
        for source_tuple in combinations(coordinates, side):
            for target_tuple in combinations(coordinates, side):
                sources = set(source_tuple)
                targets = set(target_tuple)
                universe = [
                    (x, y) for x in source_tuple for y in target_tuple
                ]

                for mask in range(1 << len(universe)):
                    host = {
                        edge
                        for index, edge in enumerate(universe)
                        if (mask >> index) & 1
                    }
                    if check_host(sources, targets, host, p, h):
                        checked += 1

    print(
        "verified factor-prefix routing for "
        f"{checked} matchable binary-parent factor hosts"
    )


if __name__ == "__main__":
    main()
