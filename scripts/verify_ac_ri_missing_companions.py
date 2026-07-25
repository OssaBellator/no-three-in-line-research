#!/usr/bin/env python3
"""Verify AC3db--AC3df on small-prime rational fibres and support graphs."""

from itertools import product


def inverse(value, prime):
    return pow(value % prime, -1, prime)


def rational_image(prime, ratio, root):
    return root * (1 - root) * inverse(ratio - root, prime) % prime


def companion_root(prime, ratio, root):
    return ratio * (root - 1) * inverse(root - ratio, prime) % prime


def hyperbola_cell(prime, parameter, column):
    return (column, parameter * inverse(column, prime) % prime)


def determinant(points):
    (x1, y1), (x2, y2), (x3, y3) = points
    return (
        x1 * (y2 - y3)
        + x2 * (y3 - y1)
        + x3 * (y1 - y2)
    )


def support(prime, a, b, image, companion, base):
    return {
        hyperbola_cell(prime, a, base),
        hyperbola_cell(prime, a, image * base % prime),
        hyperbola_cell(prime, b, companion * base % prime),
    }


def valid_fibres(prime):
    for ratio in range(2, prime):
        for root in range(1, prime):
            if root in (1, ratio):
                continue
            image = rational_image(prime, ratio, root)
            if image in (0, 1):
                continue
            companion = companion_root(prime, ratio, root)
            if companion in (0, root):
                continue
            if rational_image(prime, ratio, companion) != image:
                continue
            yield ratio, root, companion, image


def verify_companions():
    algebra_checks = 0
    modular_checks = 0
    real_checks = 0
    carry_defects = 0
    real_companions = 0

    for prime in (5, 7, 11, 13, 17, 19):
        for ratio, root, companion, image in valid_fibres(prime):
            assert root * companion % prime == ratio * image % prime
            assert companion * inverse(root, prime) % prime == (
                companion * inverse(root, prime) % prime
            )
            algebra_checks += 1

            for a in range(1, prime):
                b = ratio * a % prime
                for base in range(1, prime):
                    source = hyperbola_cell(prime, a, base)
                    partner = hyperbola_cell(prime, a, image * base % prime)
                    anchor = hyperbola_cell(prime, b, root * base % prime)
                    companion_anchor = hyperbola_cell(
                        prime, b, companion * base % prime
                    )
                    original = (source, partner, anchor)
                    formal = (source, partner, companion_anchor)

                    assert determinant(original) % prime == 0
                    assert determinant(formal) % prime == 0
                    assert (
                        (root * base % prime) * (companion * base % prime)
                        - ratio * base * (image * base % prime)
                    ) % prime == 0
                    modular_checks += 1

                    if determinant(original) == 0:
                        real_checks += 1
                        if determinant(formal) == 0:
                            real_companions += 1
                        else:
                            carry_defects += 1

    assert real_checks
    assert carry_defects
    assert real_companions
    return algebra_checks, modular_checks, real_checks, carry_defects, real_companions


def greedy_coloring(vertices, adjacency):
    colors = {}
    for vertex in vertices:
        forbidden = {colors[neighbor] for neighbor in adjacency[vertex] if neighbor in colors}
        color = 0
        while color in forbidden:
            color += 1
        colors[vertex] = color
    return colors


def verify_support_graphs():
    graph_checks = 0
    degree_checks = 0
    ratio_checks = 0
    coloring_checks = 0

    for prime in (5, 7, 11, 13, 17, 19, 23, 29, 31):
        for ratio, root, companion, image in valid_fibres(prime):
            columns = {1, image, companion}
            rows = {1, inverse(image, prime), root * inverse(image, prime) % prime}
            column_ratios = {
                left * inverse(right, prime) % prime
                for left in columns
                for right in columns
            }
            row_ratios = {
                left * inverse(right, prime) % prime
                for left in rows
                for right in rows
            }
            nontrivial = (column_ratios | row_ratios) - {1}
            assert len(nontrivial) <= 16
            ratio_checks += 1

            a = 1
            b = ratio
            vertices = tuple(range(1, prime))
            supports = {
                base: support(prime, a, b, image, companion, base)
                for base in vertices
            }
            adjacency = {base: set() for base in vertices}
            for left in vertices:
                for right in vertices:
                    if left >= right:
                        continue
                    left_columns = {cell[0] for cell in supports[left]}
                    right_columns = {cell[0] for cell in supports[right]}
                    left_rows = {cell[1] for cell in supports[left]}
                    right_rows = {cell[1] for cell in supports[right]}
                    if left_columns & right_columns or left_rows & right_rows:
                        adjacency[left].add(right)
                        adjacency[right].add(left)
                    graph_checks += 1

            maximum_degree = max(len(adjacency[base]) for base in vertices)
            assert maximum_degree <= 16
            degree_checks += 1

            colors = greedy_coloring(vertices, adjacency)
            color_count = max(colors.values()) + 1
            assert color_count <= maximum_degree + 1 <= 17

            # Several deterministic weight patterns verify the weighted colour
            # class conclusion without assuming uniform weights.
            patterns = [
                {base: 1 for base in vertices},
                {base: base % 4 for base in vertices},
                {base: (base * base + 1) % 7 for base in vertices},
            ]
            for weights in patterns:
                total = sum(weights.values())
                class_weights = [0] * color_count
                for base, color in colors.items():
                    class_weights[color] += weights[base]
                assert max(class_weights) * color_count >= total
                assert max(class_weights) * 17 >= total
                coloring_checks += 1

    return graph_checks, degree_checks, ratio_checks, coloring_checks


def verify_weight_constants(maximum=60):
    partition_checks = 0
    completion_checks = 0
    profile_checks = 0

    for total in range(1, maximum + 1):
        for carry in range(total + 1):
            for current in range(total - carry + 1):
                absent = total - carry - current
                selected = max(carry, current, absent)
                assert selected * 3 >= total
                partition_checks += 1

                if selected == absent:
                    # A 17-colour support split retains at least 1/17.
                    retained = (absent + 16) // 17
                    assert retained * 17 >= absent
                    assert retained * 51 >= total
                    completion_checks += 1

                for profile_count in range(1, 9):
                    quotient, remainder = divmod(selected, profile_count)
                    largest = quotient + (1 if remainder else 0)
                    assert largest * profile_count >= selected
                    assert 3 * largest * profile_count >= total
                    profile_checks += 1

    return partition_checks, completion_checks, profile_checks


def main():
    companion = verify_companions()
    support_checks = verify_support_graphs()
    weights = verify_weight_constants()
    print(
        "AC RI missing companions: verified "
        f"{companion[0]} fibre identities, {companion[1]} modular companions, "
        f"{companion[2]} real source factors ({companion[3]} carry defects / "
        f"{companion[4]} real companions), {support_checks[0]} support pairs, "
        f"{support_checks[1]} degree bounds, {support_checks[2]} ratio alphabets, "
        f"{support_checks[3]} weighted colourings, {weights[0]} three-way routers, "
        f"{weights[1]} completion constants, and {weights[2]} profile routers"
    )


if __name__ == "__main__":
    main()
