#!/usr/bin/env python3
"""Verify AC5ag--AC5aj: sublevel Hall cuts for min-cost safe drift."""

from itertools import combinations, permutations, product


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
    for size in range(min(a_size, len(subset_b)) + 1):
        for chosen_a in combinations(range(a_size), size):
            for chosen_b in combinations(subset_b, size):
                if any(
                    all((a, b) in edge_set for a, b in zip(chosen_a, image, strict=True))
                    for image in permutations(chosen_b)
                ):
                    best = max(best, size)
    return best


def optimal_cost(a_size, b_size, edges, costs):
    matchings = saturating_matchings(a_size, b_size, edges)
    if not matchings:
        return None
    return min(sum(costs[b] for b in matching) for matching in matchings)


def deficiency_profile(a_size, edges, costs):
    return [
        a_size - rank_into(
            a_size,
            [b for b, cost in enumerate(costs) if cost < threshold],
            edges,
        )
        for threshold in range(1, max(costs, default=0) + 1)
    ]


def check_instance(a_size, b_size, edges, current, high, batch):
    costs = [current[b] + batch * high[b] for b in range(b_size)]
    optimum = optimal_cost(a_size, b_size, edges, costs)
    if optimum is None:
        return 0
    profile = deficiency_profile(a_size, edges, costs)
    assert optimum == sum(profile)

    safe = optimum < batch * a_size
    if not safe and profile:
        assert max(profile) >= (batch * a_size + len(profile) - 1) // len(profile)

    for matching in saturating_matchings(a_size, b_size, edges):
        cost = sum(costs[b] for b in matching)
        if cost < batch * a_size:
            total_high = sum(high[b] for b in matching)
            total_current = sum(current[b] for b in matching)
            assert total_current + batch * total_high < batch * a_size
    return 1


def exhaustive():
    checks = 0
    for a_size, b_size in ((1, 2), (2, 3), (2, 4)):
        possible = [(a, b) for a in range(a_size) for b in range(b_size)]
        for mask in range(1 << len(possible)):
            edges = [edge for i, edge in enumerate(possible) if mask >> i & 1]
            if not saturating_matchings(a_size, b_size, edges):
                continue
            inventories = product(range(3), repeat=2 * b_size)
            if b_size == 4:
                inventories = list(inventories)[::23]
            for values in inventories:
                current = values[:b_size]
                high = values[b_size:]
                for batch in (1, 2, 3):
                    checks += check_instance(
                        a_size, b_size, edges, current, high, batch
                    )
    return checks


def main():
    checks = exhaustive()
    print(f"AC5 sublevel Hall cuts: verified {checks} flow/inventory/batch instances")


if __name__ == "__main__":
    main()
