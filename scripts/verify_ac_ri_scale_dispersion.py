#!/usr/bin/env python3
"""Verify AC3dg--AC3di on finite cyclic quotient groups."""

from itertools import product


def quotient_differences(values, modulus):
    return {
        (left - right) % modulus
        for left in values
        for right in values
    }


def greedy_coloring(vertices, adjacency):
    colors = {}
    for vertex in vertices:
        forbidden = {colors[neighbor] for neighbor in adjacency[vertex] if neighbor in colors}
        color = 0
        while color in forbidden:
            color += 1
        colors[vertex] = color
    return colors


def verify_support_alphabets(maximum_order=40):
    label_checks = 0
    ratio_checks = 0
    graph_checks = 0
    coloring_checks = 0
    maximum_degree_seen = 0

    for order in range(2, maximum_order + 1):
        vertices = tuple(range(order))
        for anchor_a, image, ratio in product(range(order), repeat=3):
            anchor_b = (ratio + image - anchor_a) % order

            columns = {0, image, anchor_a, anchor_b}
            rows = {
                0,
                (-image) % order,
                (anchor_b - image) % order,
                (anchor_a - image) % order,
            }
            assert len(columns) <= 4
            assert len(rows) <= 4
            label_checks += 1

            conflict_ratios = (
                quotient_differences(columns, order)
                | quotient_differences(rows, order)
            )
            nontrivial = conflict_ratios - {0}
            assert len(conflict_ratios) <= 31
            assert len(nontrivial) <= 30
            ratio_checks += 1

            adjacency = {scale: set() for scale in vertices}
            for scale in vertices:
                for difference in nontrivial:
                    other = (scale + difference) % order
                    if other != scale:
                        adjacency[scale].add(other)
                        adjacency[other].add(scale)
            maximum_degree = max(len(adjacency[scale]) for scale in vertices)
            maximum_degree_seen = max(maximum_degree_seen, maximum_degree)
            assert maximum_degree <= 30
            graph_checks += 1

            colors = greedy_coloring(vertices, adjacency)
            color_count = max(colors.values()) + 1
            assert color_count <= maximum_degree + 1 <= 31

            patterns = [
                {scale: 1 for scale in vertices},
                {scale: scale % 5 for scale in vertices},
                {scale: (scale * scale + 3) % 11 for scale in vertices},
            ]
            for weights in patterns:
                total = sum(weights.values())
                class_weights = [0] * color_count
                class_sizes = [0] * color_count
                for scale, color in colors.items():
                    class_weights[color] += weights[scale]
                    class_sizes[color] += 1
                assert max(class_weights) * color_count >= total
                assert max(class_weights) * 31 >= total
                assert max(class_sizes) * color_count >= order
                assert max(class_sizes) * 31 >= order
                coloring_checks += 1

    return (
        label_checks,
        ratio_checks,
        graph_checks,
        coloring_checks,
        maximum_degree_seen,
    )


def verify_load_router(maximum_weight=60):
    load_checks = 0
    count_checks = 0

    for total in range(1, maximum_weight + 1):
        for threshold in range(1, maximum_weight + 1):
            minimum_count = (total + threshold - 1) // threshold
            assert minimum_count * threshold >= total
            count_checks += 1

            for scale_count in range(1, min(total, 20) + 1):
                # Distribute integer weight as evenly as possible. This is the
                # extremal test for the heavy-scale or many-scale calculation.
                quotient, remainder = divmod(total, scale_count)
                weights = [
                    quotient + (1 if index < remainder else 0)
                    for index in range(scale_count)
                ]
                assert sum(weights) == total
                if max(weights) <= threshold:
                    assert scale_count * threshold >= total
                load_checks += 1

    return load_checks, count_checks


def main():
    support = verify_support_alphabets()
    loads = verify_load_router()
    print(
        "AC RI scale dispersion: verified "
        f"{support[0]} quotient-label systems, {support[1]} ratio alphabets, "
        f"{support[2]} conflict graphs, {support[3]} weighted colourings, "
        f"maximum degree {support[4]}, {loads[0]} load systems, "
        f"and {loads[1]} heavy-or-many counts"
    )


if __name__ == "__main__":
    main()
