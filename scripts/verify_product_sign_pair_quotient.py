#!/usr/bin/env python3
"""Verify PX148--PX151: sign-pair quotient matching and odd seeds."""
from collections import Counter
from itertools import combinations

ODD_SEEDS = {
    43: (0,9,25,33,28,30,42,40,12,20,7,26,29,8,5,16,2,39,24,21,32,37,6,11,22,19,4,41,27,38,35,14,17,36,23,31,3,1,13,15,10,18,34),
    47: (0,37,39,9,24,28,7,41,36,12,32,25,20,18,43,3,33,13,2,21,5,30,1,16,31,46,17,42,26,45,34,14,44,4,29,27,22,15,35,11,6,40,19,23,38,8,10),
    53: (0,7,16,35,24,22,44,12,15,40,34,1,4,50,17,6,20,30,48,45,32,39,11,25,43,26,51,2,27,10,28,42,14,21,8,5,23,33,47,36,3,49,52,19,13,38,41,9,31,29,18,37,46),
    59: (0,13,17,20,1,6,27,36,49,40,3,30,25,38,57,41,8,11,9,15,43,31,54,37,26,14,4,47,52,24,35,7,12,55,45,33,22,5,28,16,44,50,48,51,18,2,21,34,29,56,19,10,23,32,53,58,39,42,46),
    61: (0,44,29,24,58,18,35,4,14,1,11,41,53,46,39,34,38,2,6,36,9,7,13,33,19,21,49,51,30,45,56,5,16,31,10,12,40,42,28,48,54,52,25,55,59,23,27,22,15,8,20,50,60,47,57,26,43,3,37,32,17),
    67: (0,33,62,48,3,23,50,13,28,60,52,38,36,41,16,53,42,9,66,4,32,11,18,2,57,20,12,30,45,59,61,40,43,46,21,24,27,6,8,22,37,55,47,10,65,49,56,35,63,1,58,25,14,51,26,31,29,15,7,39,54,17,44,64,19,5,34),
}
EXPECTED = {
    43: (72, 10),
    47: (84, 12),
    53: (76, 10),
    59: (94, 10),
    61: (90, 12),
    67: (96, 12),
}


def sign_class(value: int, prime: int) -> int | None:
    value %= prime
    if value == 0:
        return None
    return min(value, prime - value)


def strong_odd(mapping: tuple[int, ...]) -> bool:
    prime = len(mapping)
    target = list(range(prime))
    return (
        mapping[0] == 0
        and all(mapping[prime - x] == (-mapping[x]) % prime for x in range(1, prime))
        and sorted(mapping) == target
        and sorted((x - mapping[x]) % prime for x in range(prime)) == target
        and sorted((x + mapping[x]) % prime for x in range(prime)) == target
    )


def multiplicities(mapping: tuple[int, ...]) -> tuple[int, int]:
    prime = len(mapping)
    inverse = [0] + [pow(x, -1, prime) for x in range(1, prime)]
    secants: Counter[int] = Counter()
    triangles: Counter[tuple[int, int, int]] = Counter()
    for u in range(prime):
        for v in range(prime):
            if u == v:
                continue
            difference = (v - u) % prime
            image_difference = (mapping[v] - mapping[u]) % prime
            slope = image_difference * inverse[difference] % prime
            secants[slope] += 1
            for row_ratio in range(2, prime):
                w = (u + row_ratio * difference) % prime
                image_ratio = (
                    (mapping[w] - mapping[u]) * inverse[image_difference] % prime
                )
                triangles[(slope, row_ratio, image_ratio)] += 1
    return max(secants.values()), max(triangles.values())


def quotient_edges(prime: int) -> list[tuple[int, int, int, int]]:
    seen: set[tuple[int, int, int, int]] = set()
    for x in range(1, prime):
        for y in range(1, prime):
            if y in (x, (-x) % prime):
                continue
            edge = (
                sign_class(x, prime),
                sign_class(y, prime),
                sign_class(x - y, prime),
                sign_class(x + y, prime),
            )
            assert all(value is not None for value in edge)
            seen.add(edge)
    return sorted(seen)


def verify_hypergraph(prime: int) -> None:
    edges = quotient_edges(prime)
    part_size = (prime - 1) // 2
    degree = prime - 3
    assert len(edges) == part_size * degree

    for part in range(4):
        degrees = Counter(edge[part] for edge in edges)
        assert len(degrees) == part_size
        assert set(degrees.values()) == {degree}

    maximum_pair_codegree = 0
    maximum_triple_codegree = 0
    for first, second in combinations(range(4), 2):
        counts = Counter((edge[first], edge[second]) for edge in edges)
        maximum_pair_codegree = max(maximum_pair_codegree, max(counts.values()))
    for first, second, third in combinations(range(4), 3):
        counts = Counter(
            (edge[first], edge[second], edge[third]) for edge in edges
        )
        maximum_triple_codegree = max(
            maximum_triple_codegree, max(counts.values())
        )

    assert maximum_pair_codegree == 2
    assert maximum_triple_codegree == 1
    print(
        f"p={prime}: edges={len(edges)}, degree={degree}, "
        "Delta2=2, Delta3=1"
    )


def main() -> None:
    for prime in (7, 11, 13, 17, 19):
        verify_hypergraph(prime)

    for prime, mapping in ODD_SEEDS.items():
        assert strong_odd(mapping)
        assert multiplicities(mapping) == EXPECTED[prime]
        mu, tau = EXPECTED[prime]
        print(f"p={prime}: odd seed mu={mu}, tau={tau}")

    print("PX148--PX151 verified")


if __name__ == "__main__":
    main()
