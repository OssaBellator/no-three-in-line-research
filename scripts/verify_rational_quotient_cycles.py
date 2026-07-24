#!/usr/bin/env python3
"""Verify RI2k--RI4a product-coloured quotient dynamics."""

from __future__ import annotations

from itertools import product
from math import gcd


Edge = tuple[int, int]
ColouredEdge = tuple[int, int, int]


def walk(
    start: int,
    root_colour: int,
    colours: tuple[int, ...],
    order: int,
) -> tuple[int, ...]:
    vertices = [start]
    for colour in colours:
        vertices.append(
            (root_colour + colour - vertices[-1]) % order
        )
    return tuple(vertices)


def generated_ratio_subgroup(
    colours: set[int],
    order: int,
) -> set[int]:
    if not colours:
        return {0}
    base = min(colours)
    step = order
    for colour in colours:
        step = gcd(step, (colour - base) % order)
    return {
        multiple * step % order
        for multiple in range(order // step)
    }


def generated_subgroup(values: set[int], order: int) -> set[int]:
    step = order
    for value in values:
        step = gcd(step, value % order)
    return {
        multiple * step % order
        for multiple in range(order // step)
    }


def connected_components(
    edges: set[Edge],
) -> tuple[set[int], ...]:
    incident = {vertex for edge in edges for vertex in edge}
    components: list[set[int]] = []
    unseen = set(incident)
    while unseen:
        root = min(unseen)
        component = {root}
        frontier = [root]
        unseen.remove(root)
        while frontier:
            vertex = frontier.pop()
            neighbours = {
                right if left == vertex else left
                for left, right in edges
                if left == vertex or right == vertex
            }
            for neighbour in neighbours & unseen:
                unseen.remove(neighbour)
                component.add(neighbour)
                frontier.append(neighbour)
        components.append(component)
    return tuple(components)


def bipartition(
    component: set[int],
    edges: set[Edge],
) -> tuple[set[int], set[int]] | None:
    side = {min(component): 0}
    frontier = [min(component)]
    while frontier:
        vertex = frontier.pop()
        for left, right in edges:
            if left != vertex and right != vertex:
                continue
            neighbour = right if left == vertex else left
            if neighbour == vertex:
                return None
            expected = 1 - side[vertex]
            if neighbour in side:
                if side[neighbour] != expected:
                    return None
            else:
                side[neighbour] = expected
                frontier.append(neighbour)
    return (
        {vertex for vertex in component if side[vertex] == 0},
        {vertex for vertex in component if side[vertex] == 1},
    )


def all_ratios(vertices: set[int], order: int) -> set[int]:
    return {
        (left - right) % order
        for left in vertices
        for right in vertices
    }


def verify_walk_formula(maximum_order: int = 8, maximum_length: int = 4) -> None:
    """Exhaustively check every colour word in the advertised small range."""
    for order in range(1, maximum_order + 1):
        for root_colour in range(order):
            for start in range(order):
                for length in range(1, maximum_length + 1):
                    for colours in product(range(order), repeat=length):
                        vertices = walk(
                            start,
                            root_colour,
                            colours,
                            order,
                        )
                        for index, vertex in enumerate(vertices):
                            if index % 2 == 0:
                                half = index // 2
                                closed = start
                                for offset in range(half):
                                    closed += (
                                        colours[2 * offset + 1]
                                        - colours[2 * offset]
                                    )
                            else:
                                half = (index - 1) // 2
                                closed = root_colour - start
                                closed += sum(
                                    colours[2 * offset]
                                    for offset in range(half + 1)
                                )
                                closed -= sum(
                                    colours[2 * offset + 1]
                                    for offset in range(half)
                                )
                            assert vertex == closed % order

                        if vertices[-1] == start:
                            if length % 2 == 0:
                                assert sum(colours[1::2]) % order == (
                                    sum(colours[0::2]) % order
                                )
                            else:
                                assert 2 * start % order == (
                                    root_colour
                                    + sum(colours[0::2])
                                    - sum(colours[1::2])
                                ) % order

                        colour_set = set(colours)
                        subgroup = generated_ratio_subgroup(
                            colour_set,
                            order,
                        )
                        base = min(colour_set)
                        even_coset = {
                            (start + element) % order
                            for element in subgroup
                        }
                        odd_coset = {
                            (
                                root_colour
                                - start
                                + base
                                + element
                            ) % order
                            for element in subgroup
                        }
                        assert set(vertices[0::2]) <= even_coset
                        assert set(vertices[1::2]) <= odd_coset
                        assert colour_set <= {
                            (base + element) % order
                            for element in subgroup
                        }
                        assert len(set(vertices)) <= 2 * len(subgroup)


def verify_component_parity(maximum_order: int = 5) -> None:
    for order in range(1, maximum_order + 1):
        edge_slots = tuple(
            (left, right)
            for left in range(order)
            for right in range(left, order)
        )
        for mask in range(1, 1 << len(edge_slots)):
            edges = {
                edge
                for index, edge in enumerate(edge_slots)
                if mask & (1 << index)
            }
            for component in connected_components(edges):
                component_edges = {
                    edge
                    for edge in edges
                    if edge[0] in component and edge[1] in component
                }
                for root_colour in range(order):
                    colours = {
                        (left + right - root_colour) % order
                        for left, right in component_edges
                    }
                    ratio_subgroup = generated_ratio_subgroup(
                        colours,
                        order,
                    )
                    parts = bipartition(component, component_edges)
                    if parts is not None:
                        left_part, right_part = parts
                        side_subgroup = generated_subgroup(
                            all_ratios(left_part, order)
                            | all_ratios(right_part, order),
                            order,
                        )
                        assert ratio_subgroup == side_subgroup
                        left_root = min(left_part)
                        right_root = min(right_part)
                        assert left_part <= {
                            (left_root + value) % order
                            for value in ratio_subgroup
                        }
                        assert right_part <= {
                            (right_root + value) % order
                            for value in ratio_subgroup
                        }
                        assert colours <= {
                            (
                                left_root
                                + right_root
                                - root_colour
                                + value
                            ) % order
                            for value in ratio_subgroup
                        }
                    else:
                        source_subgroup = generated_subgroup(
                            all_ratios(component, order),
                            order,
                        )
                        assert ratio_subgroup == source_subgroup
                        source_root = min(component)
                        assert component <= {
                            (source_root + value) % order
                            for value in ratio_subgroup
                        }
                        assert colours <= {
                            (
                                2 * source_root
                                - root_colour
                                + value
                            ) % order
                            for value in ratio_subgroup
                        }


def verify_order_two_templates(maximum_order: int = 20) -> None:
    checked_weight_patterns: set[tuple[int, ...]] = set()
    for order in range(2, maximum_order + 1, 2):
        involution = order // 2
        subgroup = {0, involution}
        for root_colour in range(order):
            for base_colour in range(order):
                colours = {
                    base_colour,
                    (base_colour + involution) % order,
                }
                assert generated_ratio_subgroup(colours, order) == subgroup
                for source in range(order):
                    partner = (
                        root_colour + base_colour - source
                    ) % order
                    source_coset = {
                        source,
                        (source + involution) % order,
                    }
                    partner_coset = {
                        partner,
                        (partner + involution) % order,
                    }
                    vertices = source_coset | partner_coset
                    edges: set[ColouredEdge] = set()
                    for vertex in vertices:
                        for colour in colours:
                            neighbour = (
                                root_colour + colour - vertex
                            ) % order
                            assert neighbour in vertices
                            left, right = sorted((vertex, neighbour))
                            edges.add((left, right, colour))

                    if source_coset.isdisjoint(partner_coset):
                        assert len(vertices) == 4
                        assert len(edges) == 4
                        assert all(left != right for left, right, _ in edges)
                        assert all(
                            sum(colour == selected for _, _, colour in edges)
                            == 2
                            for selected in colours
                        )
                        uncoloured = {
                            (left, right) for left, right, _ in edges
                        }
                        assert len(connected_components(uncoloured)) == 1
                        assert all(
                            sum(vertex in edge for edge in uncoloured) == 2
                            for vertex in vertices
                        )
                    else:
                        assert source_coset == partner_coset
                        assert len(vertices) == 2
                        assert len(edges) == 3
                        loops = {
                            edge for edge in edges if edge[0] == edge[1]
                        }
                        links = edges - loops
                        assert len(loops) == 2
                        assert len(links) == 1
                        assert len({colour for _, _, colour in loops}) == 1
                        loop_colour = next(iter(loops))[2]
                        assert next(iter(links))[2] != loop_colour

                    colour_counts = tuple(sorted(
                        sum(
                            edge_colour == colour
                            for _, _, edge_colour in edges
                        )
                        for colour in colours
                    ))
                    if colour_counts in checked_weight_patterns:
                        continue
                    checked_weight_patterns.add(colour_counts)
                    edge_list = tuple(edges)
                    for weights in product(
                        range(4),
                        repeat=len(edge_list),
                    ):
                        total = sum(weights)
                        if total == 0:
                            continue
                        assert len(edge_list) * max(weights) >= total
                        weight_by_colour = {
                            colour: sum(
                                weight
                                for edge, weight in zip(
                                    edge_list,
                                    weights,
                                )
                                if edge[2] == colour
                            )
                            for colour in colours
                        }
                        assert 2 * max(weight_by_colour.values()) >= total


def verify_cycle_multiplicity(maximum_order: int = 30) -> None:
    for order in range(1, maximum_order + 1):
        for target in range(order):
            roots = [
                value
                for value in range(order)
                if 2 * value % order == target
            ]
            assert len(roots) in (0, gcd(2, order))
            if len(roots) == 2:
                assert (roots[1] - roots[0]) % order == order // 2

        for root_colour in range(order):
            for colour in range(order):
                neighbour = lambda value: (
                    root_colour + colour - value
                ) % order
                assert all(
                    neighbour(neighbour(value)) == value
                    for value in range(order)
                )


def main() -> None:
    verify_walk_formula()
    verify_component_parity()
    verify_order_two_templates()
    verify_cycle_multiplicity()
    print("rational quotient cycle dynamics: verified")


if __name__ == "__main__":
    main()
