#!/usr/bin/env python3
"""Finite audit for SRR2x--SRR2ab."""

from itertools import product
from math import floor


def hall_deficiency(n_left: int, n_right: int, edges: set[tuple[int, int]]) -> int:
    deficiency = 0
    for mask in range(1 << n_left):
        left_set = [left for left in range(n_left) if (mask >> left) & 1]
        neighbours = {
            right
            for left in left_set
            for right in range(n_right)
            if (left, right) in edges
        }
        deficiency = max(deficiency, len(left_set) - len(neighbours))
    return max(0, deficiency)


def main() -> None:
    graphs = thresholds = conditioned = 0

    for n_left in range(1, 5):
        for n_right in range(1, 5):
            possible_edges = [(left, right) for left in range(n_left) for right in range(n_right)]
            if len(possible_edges) <= 9:
                masks = range(1 << len(possible_edges))
            else:
                stride = max(1, (1 << len(possible_edges)) // 1500)
                masks = range(0, 1 << len(possible_edges), stride)

            for mask in masks:
                edges = {
                    edge for bit, edge in enumerate(possible_edges) if (mask >> bit) & 1
                }
                endpoint_cost = [right % 3 for right in range(n_right)]
                graphs += 1

                for threshold in range(1, 4):
                    low_edges = {
                        edge for edge in edges if endpoint_cost[edge[1]] < threshold
                    }
                    low_right = [
                        right for right in range(n_right) if endpoint_cost[right] < threshold
                    ]
                    minimum_left_degree = min(
                        sum((left, right) in low_edges for right in range(n_right))
                        for left in range(n_left)
                    )
                    maximum_right_load = max(
                        (
                            sum((left, right) in low_edges for left in range(n_left))
                            for right in low_right
                        ),
                        default=0,
                    )
                    exact = hall_deficiency(n_left, n_right, low_edges)

                    if minimum_left_degree == 0 or maximum_right_load == 0:
                        assert exact <= n_left
                    else:
                        relative_bound = max(
                            0,
                            floor(
                                n_left
                                * (maximum_right_load - minimum_left_degree)
                                / maximum_right_load
                            ),
                        )
                        assert exact <= relative_bound

                        conditioned_edges = set(low_edges)
                        for left in range(n_left):
                            incident = sorted(
                                edge for edge in conditioned_edges if edge[0] == left
                            )
                            if incident:
                                conditioned_edges.remove(incident[0])

                        conditioned_exact = hall_deficiency(
                            n_left, n_right, conditioned_edges
                        )
                        deletion_bound = 1
                        surviving_degree = max(
                            0, minimum_left_degree - deletion_bound
                        )
                        if surviving_degree == 0:
                            assert conditioned_exact <= n_left
                        else:
                            conditioned_bound = max(
                                0,
                                floor(
                                    n_left
                                    * (maximum_right_load - surviving_degree)
                                    / maximum_right_load
                                ),
                            )
                            assert conditioned_exact <= conditioned_bound
                        conditioned += 1

                    thresholds += 1

    assert graphs == 6847
    assert thresholds == 20541
    assert conditioned == 8968
    print(
        "relative threshold-slack audit passed:",
        f"{graphs} graphs, {thresholds} thresholds, {conditioned} conditioned cases",
    )


if __name__ == "__main__":
    main()
