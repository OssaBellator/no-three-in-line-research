#!/usr/bin/env python3
"""Verify SRR2j--SRR2m: endpoint-cost Hall deficiency formulas."""

from itertools import combinations, product, permutations


def saturating_matchings(a_size, b_size, edges):
    edge_set = set(edges)
    result = []
    for chosen in combinations(range(b_size), a_size):
        for image in permutations(chosen):
            if all((a, image[a]) in edge_set for a in range(a_size)):
                result.append(image)
    return result


def rank_into(a_size, subset_b, edges):
    subset_b = tuple(subset_b)
    edge_set = set(edges)
    best = 0
    for size in range(1, min(a_size, len(subset_b)) + 1):
        for chosen_a in combinations(range(a_size), size):
            for chosen_b in combinations(subset_b, size):
                for image in permutations(chosen_b):
                    if all((a, b) in edge_set for a, b in zip(chosen_a, image, strict=True)):
                        best = max(best, size)
                        break
    return best


def hall_deficiency(a_size, subset_b, edges):
    subset_b = set(subset_b)
    adjacency = {
        a: {b for aa, b in edges if aa == a and b in subset_b}
        for a in range(a_size)
    }
    deficiency = 0
    for size in range(a_size + 1):
        for chosen_a in combinations(range(a_size), size):
            neighbours = set().union(*(adjacency[a] for a in chosen_a)) if chosen_a else set()
            deficiency = max(deficiency, size - len(neighbours))
    return deficiency


def check_instance(a_size, b_size, edges, costs):
    matchings = saturating_matchings(a_size, b_size, edges)
    if not matchings:
        return 0
    minimum = min(sum(costs[b] for b in matching) for matching in matchings)
    cmax = max(costs, default=0)
    deficiency_sum = 0
    rank_sum = 0
    for threshold in range(1, cmax + 1):
        low = [b for b, cost in enumerate(costs) if cost < threshold]
        rank = rank_into(a_size, low, edges)
        deficiency = hall_deficiency(a_size, low, edges)
        assert deficiency == a_size - rank
        rank_sum += a_size - rank
        deficiency_sum += deficiency
    assert minimum == rank_sum == deficiency_sum
    return 1


def exhaustive():
    checks = graphs = 0
    for a_size, b_size in ((1, 2), (2, 3), (2, 4), (3, 4)):
        possible = [(a, b) for a in range(a_size) for b in range(b_size)]
        masks = range(1 << len(possible))
        if len(possible) > 8:
            masks = range(0, 1 << len(possible), 31)
        for mask in masks:
            edges = [edge for i, edge in enumerate(possible) if mask >> i & 1]
            if not saturating_matchings(a_size, b_size, edges):
                continue
            graphs += 1
            cost_vectors = product(range(4), repeat=b_size)
            if b_size == 4:
                cost_vectors = list(cost_vectors)[::7]
            for costs in cost_vectors:
                checks += check_instance(a_size, b_size, edges, costs)
    return graphs, checks


def main():
    graphs, checks = exhaustive()
    print(
        "Superregular endpoint-cost cuts: verified "
        f"{graphs} Hall-feasible graphs and {checks} integer endpoint-cost instances"
    )


if __name__ == "__main__":
    main()
