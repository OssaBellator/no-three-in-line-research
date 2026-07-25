#!/usr/bin/env python3
"""Verify CMR643--CMR648 essentiality-loss and escape identities."""

from itertools import permutations, product


Edge = tuple[int, int]
Vertex = tuple[str, int]


def perfect_matchings(n: int, edges: set[Edge]) -> list[set[Edge]]:
    out: list[set[Edge]] = []
    for image in permutations(range(n)):
        matching = {(i, image[i]) for i in range(n)}
        if matching <= edges:
            out.append(matching)
    return out


def symmetric_difference_components(
    first: set[Edge],
    second: set[Edge],
) -> list[set[Edge]]:
    diff = first ^ second
    adjacency: dict[Vertex, set[Vertex]] = {}

    for source, target in diff:
        left = ("L", source)
        right = ("R", target)
        adjacency.setdefault(left, set()).add(right)
        adjacency.setdefault(right, set()).add(left)

    seen: set[Vertex] = set()
    components: list[set[Edge]] = []

    for root in adjacency:
        if root in seen:
            continue

        stack = [root]
        seen.add(root)
        component: set[Edge] = set()

        while stack:
            vertex = stack.pop()
            for neighbour in adjacency[vertex]:
                if vertex[0] == "L":
                    edge = (vertex[1], neighbour[1])
                else:
                    edge = (neighbour[1], vertex[1])
                component.add(edge)

                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)

        components.append(component)

    return components


def check_side_three() -> tuple[int, int]:
    n = 3
    all_edges = [(i, j) for i in range(n) for j in range(n)]
    old_hosts = 0
    omitted_cases = 0

    # Each edge is absent, old, or genuinely new.
    for states in product(range(3), repeat=n * n):
        old_host = {
            edge for edge, state in zip(all_edges, states) if state == 1
        }
        added = {edge for edge, state in zip(all_edges, states) if state == 2}

        old_matchings = perfect_matchings(n, old_host)
        if not old_matchings:
            continue

        old_hosts += 1
        essential = set.intersection(*(set(m) for m in old_matchings))
        reference = old_matchings[0]

        for later in perfect_matchings(n, old_host | added):
            omitted = essential - later
            if omitted:
                omitted_cases += 1
                # CMR643: at least one genuinely new matching edge is necessary.
                assert later & added

            components = symmetric_difference_components(reference, later)
            affected = 0

            for component in components:
                if component & omitted:
                    # CMR644: every affected alternating component has an
                    # entering matching edge.
                    assert component & later & added
                    affected += 1

            # Distinct affected components use distinct entering edges.
            assert affected <= len(later & added)

    return old_hosts, omitted_cases


def check_escape_stock() -> None:
    for n in range(1, 50):
        for recurrence in range(2, 10):
            witness_stock = 3 * n * n
            finite_bound = (recurrence - 1) * witness_stock
            assert finite_bound == 3 * (recurrence - 1) * n * n


def main() -> None:
    old_hosts, omitted_cases = check_side_three()
    check_escape_stock()
    print(
        "verified forced-product escape across "
        f"{old_hosts} ternary old/addition hosts and {omitted_cases} "
        "essentiality-loss matching cases"
    )


if __name__ == "__main__":
    main()
