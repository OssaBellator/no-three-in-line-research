#!/usr/bin/env python3
"""Verify AC3cp--AC3ct on finite partial-permutation models."""

from itertools import combinations, permutations


def prescriptions(n, rank):
    for cols in combinations(range(n), rank):
        for rows in permutations(range(n), rank):
            if all(c != r for c, r in zip(cols, rows)):
                yield cols, rows


def graph_type(cols, rows):
    rank = len(cols)
    mapping = dict(zip(cols, rows))
    overlap = len(set(cols) & set(rows))
    cycles = 0
    for start in cols:
        path = []
        current = start
        while current in mapping and current not in path:
            path.append(current)
            current = mapping[current]
        if current in path and current == min(path[path.index(current):]):
            cycles += 1
    if rank == 1:
        return "arc"
    if rank == 2:
        return {0: "two_disjoint", 1: "path2", 2: "cycle2"}[overlap]
    if overlap == 0:
        return "three_disjoint"
    if overlap == 1:
        return "path2_plus_arc"
    if overlap == 2:
        return "cycle2_plus_arc" if cycles else "path3"
    return "cycle3"


EXPECTED = {
    "arc", "two_disjoint", "path2", "cycle2",
    "three_disjoint", "path2_plus_arc", "path3",
    "cycle2_plus_arc", "cycle3",
}


def components(cols, rows):
    mapping = dict(zip(cols, rows))
    vertices = set(cols) | set(rows)
    adjacency = {v: set() for v in vertices}
    for a, b in mapping.items():
        adjacency[a].add(b)
        adjacency[b].add(a)
    blocks = []
    unseen = set(vertices)
    while unseen:
        stack = [min(unseen)]
        block = set()
        while stack:
            v = stack.pop()
            if v in block:
                continue
            block.add(v)
            unseen.discard(v)
            stack.extend(adjacency[v] - block)
        edges = [(a, b) for a, b in mapping.items() if a in block]
        cycle = len(edges) == len(block)
        blocks.append((edges, cycle))
    return blocks


def verify_types_and_rectangles():
    type_checks = rectangle_checks = cycle_checks = 0
    observed = set()
    for n in range(2, 7):
        anchors = tuple((i + 1, 2 * i + 3) for i in range(n))
        for rank in range(1, min(3, n) + 1):
            for cols, rows in prescriptions(n, rank):
                observed.add(graph_type(cols, rows))
                type_checks += 1
                mapping = dict(zip(cols, rows))
                crossed = {}
                for i, j in mapping.items():
                    xi, yi = anchors[i]
                    xj, yj = anchors[j]
                    crossed[(i, j)] = (xi, yj)
                    assert (xj, yi) == (anchors[j][0], anchors[i][1])
                    rectangle_checks += 1
                for i, j in mapping.items():
                    if i < j and mapping.get(j) == i:
                        z1, z2 = crossed[(i, j)], crossed[(j, i)]
                        q1, q2 = anchors[i], anchors[j]
                        assert (z1[0] + z2[0], z1[1] + z2[1]) == (
                            q1[0] + q2[0], q1[1] + q2[1]
                        )
                        cycle_checks += 1
                vertices = set(cols) | set(rows)
                assert 2 ** len(vertices) <= 2 ** (2 * rank)
    assert observed == EXPECTED
    return type_checks, rectangle_checks, cycle_checks


def verify_products():
    arc_checks = path_checks = cycle_checks = 0
    for prime in (5, 7, 11, 13):
        n = min(5, prime - 1)
        xs = tuple(range(1, n + 1))
        ys = tuple((3 * x + 1) % prime or 1 for x in xs)
        if len(set(ys)) != n:
            ys = tuple(range(n, 0, -1))
        lambdas = tuple(x * y % prime for x, y in zip(xs, ys))
        for rank in range(1, min(3, n) + 1):
            for cols, rows in prescriptions(n, rank):
                mus = {}
                for i, j in zip(cols, rows):
                    mu = xs[i] * ys[j] % prime
                    assert mu == lambdas[j] * xs[i] * pow(xs[j], -1, prime) % prime
                    mus[(i, j)] = mu
                    arc_checks += 1
                for edges, is_cycle in components(cols, rows):
                    outgoing = dict(edges)
                    if is_cycle:
                        start = min(outgoing)
                        seq = [start]
                        while outgoing[seq[-1]] != start:
                            seq.append(outgoing[seq[-1]])
                        left = right = 1
                        for k, i in enumerate(seq):
                            j = seq[(k + 1) % len(seq)]
                            left = left * mus[(i, j)] % prime
                            right = right * lambdas[i] % prime
                        assert left == right
                        cycle_checks += 1
                    else:
                        incoming = set(outgoing.values())
                        start = next(i for i in outgoing if i not in incoming)
                        seq = [start]
                        while seq[-1] in outgoing:
                            seq.append(outgoing[seq[-1]])
                        left = right = 1
                        for i, j in zip(seq, seq[1:]):
                            left = left * mus[(i, j)] % prime
                            right = right * lambdas[j] % prime
                        right = right * xs[seq[0]] * pow(xs[seq[-1]], -1, prime) % prime
                        assert left == right
                        path_checks += 1
    return arc_checks, path_checks, cycle_checks


def main():
    types, rectangles, sums = verify_types_and_rectangles()
    arcs, paths, cycles = verify_products()
    print(
        "AC RI blocker rectangles: verified "
        f"{types} graph types, {rectangles} rectangles, {sums} cycle sums, "
        f"{arcs} arc products, {paths} path products, and {cycles} cycle products"
    )


if __name__ == "__main__":
    main()
