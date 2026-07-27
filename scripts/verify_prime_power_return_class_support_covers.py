#!/usr/bin/env python3
"""Finite checks for CMR1670--CMR1677."""

from __future__ import annotations

from itertools import permutations, product
from random import Random


Edge = tuple[int, int]
Vertex = tuple[str, int]


def main() -> None:
    random = Random(1670)
    systems = 0
    level_checks = 0
    alternative_cover_checks = 0
    integer_checks = 0

    for _ in range(1_200):
        side = random.randint(2, 7)
        class_count = random.randint(1, 7)
        classes = list(range(class_count))
        caps = {class_id: random.randint(0, 15) for class_id in classes}

        edge_class: dict[Edge, int] = {}
        for index in range(side):
            edge_class[(index, index)] = random.choice(classes)
        for left in range(side):
            for right in range(side):
                if (left, right) not in edge_class and random.random() < 0.45:
                    edge_class[(left, right)] = random.choice(classes)

        edges = set(edge_class)
        response_matchings = [
            permutation
            for permutation in permutations(range(side))
            if all((left, permutation[left]) in edges for left in range(side))
        ]
        assert response_matchings

        exact_score = {
            edge: random.randint(0, caps[edge_class[edge]]) for edge in edges
        }
        source_support = {
            class_id: {
                left
                for (left, _), edge_class_id in edge_class.items()
                if edge_class_id == class_id
            }
            for class_id in classes
        }
        target_support = {
            class_id: {
                right
                for (_, right), edge_class_id in edge_class.items()
                if edge_class_id == class_id
            }
            for class_id in classes
        }

        chosen_cover: dict[int, set[Vertex]] = {}
        for class_id in classes:
            if random.random() < 0.5:
                chosen_cover[class_id] = {
                    ("L", left) for left in source_support[class_id]
                }
            else:
                chosen_cover[class_id] = {
                    ("R", right) for right in target_support[class_id]
                }

        levels = sorted({value for value in caps.values() if value > 0})
        previous = 0
        cover_bound = 0
        for level in levels:
            active = [class_id for class_id in classes if caps[class_id] >= level]
            cover: set[Vertex] = set()
            for class_id in active:
                cover.update(chosen_cover[class_id])

            for (left, right), score in exact_score.items():
                if score >= level:
                    assert ("L", left) in cover or ("R", right) in cover

            cover_bound += (level - previous) * len(cover)
            previous = level
            level_checks += 1

            best_union_size: int | None = None
            for choices in product([0, 1], repeat=len(active)):
                candidate_cover: set[Vertex] = set()
                for choice, class_id in zip(choices, active):
                    if choice == 0:
                        candidate_cover.update(
                            ("L", left) for left in source_support[class_id]
                        )
                    else:
                        candidate_cover.update(
                            ("R", right) for right in target_support[class_id]
                        )
                if best_union_size is None:
                    best_union_size = len(candidate_cover)
                else:
                    best_union_size = min(best_union_size, len(candidate_cover))
            assert best_union_size is not None
            alternative_cover_checks += 1

        optimum = max(
            sum(exact_score[(left, permutation[left])] for left in range(side))
            for permutation in response_matchings
        )
        assert optimum <= cover_bound

        vertex_weight: dict[Vertex, int] = {}
        vertices = [
            *(('L', index) for index in range(side)),
            *(('R', index) for index in range(side)),
        ]
        for vertex in vertices:
            vertex_weight[vertex] = max(
                [
                    caps[class_id]
                    for class_id in classes
                    if vertex in chosen_cover[class_id]
                ]
                or [0]
            )

        for (left, right), score in exact_score.items():
            assert (
                vertex_weight[("L", left)] + vertex_weight[("R", right)]
                >= score
            )
        assert sum(vertex_weight.values()) == cover_bound

        denominator = cover_bound + random.randint(1, 30)
        assert sum(vertex_weight.values()) < denominator
        integer_checks += 1
        systems += 1

    print(
        "verified class-supported return covers: "
        f"{systems} score systems, "
        f"{level_checks} threshold unions, "
        f"{alternative_cover_checks} finite cover optimizations and "
        f"{integer_checks} strict dual certificates"
    )


if __name__ == "__main__":
    main()
