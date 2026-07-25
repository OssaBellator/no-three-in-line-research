#!/usr/bin/env python3
"""Exhaust the weighted same-token labelled-fan lemma on small graphs."""

from itertools import combinations, product


def maximum_independent_weight(vertices, edges, weights):
    edge_set = {tuple(sorted(edge)) for edge in edges}
    best = 0
    for mask in range(1 << len(vertices)):
        chosen = [vertices[i] for i in range(len(vertices)) if mask & (1 << i)]
        if all(tuple(sorted((u, v))) not in edge_set for u, v in combinations(chosen, 2)):
            best = max(best, sum(weights[v] for v in chosen))
    return best


def verify(maximum_vertices=4, maximum_labels=3, maximum_weight=3):
    for vertex_count in range(1, maximum_vertices + 1):
        vertices = tuple(range(vertex_count))
        possible_edges = tuple(combinations(vertices, 2))
        for label_count in range(1, maximum_labels + 1):
            for labels in product(range(label_count), repeat=vertex_count):
                for weight_tuple in product(range(1, maximum_weight + 1), repeat=vertex_count):
                    weights = dict(enumerate(weight_tuple))
                    total_weight = sum(weight_tuple)
                    class_weights = [
                        sum(weights[v] for v in vertices if labels[v] == label)
                        for label in range(label_count)
                    ]
                    selected_label = max(range(label_count), key=class_weights.__getitem__)
                    fibre = tuple(v for v in vertices if labels[v] == selected_label)
                    fibre_weight = class_weights[selected_label]
                    assert fibre_weight * label_count >= total_weight

                    for edge_mask in range(1 << len(possible_edges)):
                        edges = tuple(
                            edge
                            for index, edge in enumerate(possible_edges)
                            if edge_mask & (1 << index)
                        )
                        fibre_edges = tuple(
                            edge for edge in edges if edge[0] in fibre and edge[1] in fibre
                        )
                        degrees = {
                            v: sum(v in edge for edge in fibre_edges)
                            for v in fibre
                        }
                        optimum = maximum_independent_weight(fibre, fibre_edges, weights)
                        for gamma in range(vertex_count):
                            if any(degree > gamma for degree in degrees.values()):
                                continue
                            assert optimum * (gamma + 1) >= fibre_weight
                            assert optimum * label_count * (gamma + 1) >= total_weight


def main():
    verify()
    print("weighted labelled-fan dichotomy: verified through four vertices")


if __name__ == "__main__":
    main()
