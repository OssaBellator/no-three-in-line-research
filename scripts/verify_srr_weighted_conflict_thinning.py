from itertools import combinations
from random import Random


def max_independent_weight(weights: list[int], adjacency: list[int]) -> int:
    n = len(weights)
    best = 0
    for mask in range(1 << n):
        total = 0
        valid = True
        for vertex in range(n):
            if mask >> vertex & 1:
                total += weights[vertex]
                if adjacency[vertex] & mask:
                    valid = False
                    break
        if valid and total > best:
            best = total
    return best


def main() -> None:
    rng = Random(20260802)
    graphs = 3_500
    vertices = edges = 0

    for _ in range(graphs):
        n = rng.randint(3, 13)
        weights = [rng.randint(1, 9) for _ in range(n)]
        adjacency = [0] * n
        density = rng.uniform(0.08, 0.45)

        for left, right in combinations(range(n), 2):
            if rng.random() < density:
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left
                edges += 1

        lower_bound = sum(
            weights[vertex] / (adjacency[vertex].bit_count() + 1)
            for vertex in range(n)
        )
        optimum = max_independent_weight(weights, adjacency)
        assert optimum + 1e-12 >= lower_bound
        vertices += n

    print(f"{graphs:,} conflict graphs")
    print(f"{vertices:,} weighted switching candidates")
    print(f"{edges:,} exact conflict edges")
    print(f"{graphs:,} weighted local-minimum bounds verified")


if __name__ == "__main__":
    main()
