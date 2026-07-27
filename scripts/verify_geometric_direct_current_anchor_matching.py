#!/usr/bin/env python3
"""Finite audit for GC2ff--GC2fj."""

from collections import defaultdict
from fractions import Fraction
import random

SEED = 20260727


def disjoint_permutations(n, rng):
    first = list(range(n))
    rng.shuffle(first)
    while True:
        second = list(range(n))
        rng.shuffle(second)
        if all(first[c] != second[c] for c in range(n)):
            return first, second


def perfect_matching(allowed):
    """Return source->target matching in a bipartite graph, or None."""
    n = len(allowed)
    target_owner = [-1] * n

    def augment(source, seen):
        for target in allowed[source]:
            if target in seen:
                continue
            seen.add(target)
            if target_owner[target] == -1 or augment(target_owner[target], seen):
                target_owner[target] = source
                return True
        return False

    for source in range(n):
        if not augment(source, set()):
            return None

    result = [-1] * n
    for target, source in enumerate(target_owner):
        result[source] = target
    return result


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(50000):
        n = rng.randint(7, 22)
        q_ch = rng.randint(1, 5)
        layers = disjoint_permutations(n, rng)

        endpoints = [(layer, col, layers[layer][col]) for layer in range(2) for col in range(n)]
        rng.shuffle(endpoints)
        pair_count = rng.randint(1, n)
        chosen = endpoints[: 2 * pair_count]

        pairs = []
        a_star = 0
        for i in range(pair_count):
            left = chosen[2 * i]
            right = chosen[2 * i + 1]
            weight = rng.randint(1, 20)
            channels = (rng.randrange(q_ch), rng.randrange(q_ch))
            pairs.append((left, right, channels, weight))
            a_star += weight

        incidence = defaultdict(int)
        for left, right, channels, weight in pairs:
            incidence[(left[0], channels[0])] += weight
            incidence[(right[0], channels[1])] += weight

        best_type, best_incidence = max(incidence.items(), key=lambda item: item[1])
        assert best_incidence * q_ch >= a_star

        selected = []
        a_type = 0
        for pair_index, (left, right, channels, weight) in enumerate(pairs):
            candidates = []
            if (left[0], channels[0]) == best_type:
                candidates.append(left)
            if (right[0], channels[1]) == best_type:
                candidates.append(right)
            if candidates:
                endpoint = min(candidates)
                selected.append((pair_index, endpoint, weight))
                a_type += weight

        assert 2 * q_ch * a_type >= a_star
        selected_cells = [(endpoint[1], endpoint[2]) for _, endpoint, _ in selected]
        assert len({col for col, _ in selected_cells}) == len(selected_cells)
        assert len({row for _, row in selected_cells}) == len(selected_cells)

        t = len(selected)
        l_cert = rng.randint(1, 7)
        delta_cap = l_cert * (n * n - 2)
        xden = 2 * delta_cap - 1
        w_birth = Fraction(a_star * n * n * xden, 2)
        assert Fraction(a_star, 1) > Fraction(3 * w_birth, 2 * n * n * xden)

        if t <= 6:
            heavy = max(weight for _, _, weight in selected)
            assert heavy * t >= a_type
            assert Fraction(heavy, 1) >= Fraction(a_type, 6)
            global_bound = Fraction(w_birth, 8 * q_ch * n * n * xden)
            assert Fraction(heavy, 1) > global_bound
            counts["small_heavy_atom_branches"] += 1
            counts["heavy_atom_weight"] += heavy
        else:
            layer = best_type[0]
            other = 1 - layer
            columns = [endpoint[1] for _, endpoint, _ in selected]
            rows = [endpoint[2] for _, endpoint, _ in selected]
            row_index = {row: i for i, row in enumerate(rows)}

            forbidden = [set() for _ in range(t)]
            for i in range(t):
                forbidden[i].add(i)  # original diagonal
                other_row = layers[other][columns[i]]
                if other_row in row_index:
                    forbidden[i].add(row_index[other_row])

            row_degree = [len(values) for values in forbidden]
            col_degree = [0] * t
            for values in forbidden:
                for target in values:
                    col_degree[target] += 1
            assert max(row_degree) <= 2
            assert max(col_degree) <= 2

            allowed = [
                [target for target in range(t) if target not in forbidden[source]]
                for source in range(t)
            ]
            matching = perfect_matching(allowed)
            assert matching is not None
            assert all(matching[i] != i for i in range(t))
            assert all(rows[matching[i]] != layers[other][columns[i]] for i in range(t))

            # Every selected exact source lineage loses its chosen endpoint.
            for i, (_, endpoint, _) in enumerate(selected):
                assert rows[matching[i]] != endpoint[2]

            a = Fraction(a_type, 1)
            assert a >= Fraction(a_star, 2 * q_ch)
            epsilon = Fraction(rng.randint(1, 9), 10)

            descent = epsilon * a
            global_descent = Fraction(3 * epsilon * w_birth, 4 * q_ch * n * n * xden)
            assert descent > global_descent

            k_tri = n * n * (n * n - 1) // 2
            local_certificate = (1 - epsilon) * a / (384 * k_tri)
            global_certificate = Fraction(
                (1 - epsilon) * w_birth,
                512 * q_ch * n * n * xden * k_tri,
            )
            assert local_certificate > global_certificate

            counts["large_direct_an_branches"] += 1
            counts["selected_matching_cells"] += t
            counts["forbidden_positions"] += sum(row_degree)

        counts["systems"] += 1
        counts["lineages"] += pair_count
        counts["selected_type_lineages"] += t

    print("GC direct current-anchor matching audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
