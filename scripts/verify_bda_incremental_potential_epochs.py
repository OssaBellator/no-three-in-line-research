#!/usr/bin/env python3
"""Finite checks for BDA5ha--BDA5he."""

import random


def maximum_matching(left, right, edges):
    adjacency = {x: [y for y in right if (x, y) in edges] for x in left}
    owner = {}
    def visit(x, seen):
        for y in adjacency[x]:
            if y in seen:
                continue
            seen.add(y)
            if y not in owner or visit(owner[y], seen):
                owner[y] = x
                return True
        return False
    for x in left:
        visit(x, set())
    return {x: y for y, x in owner.items()}


def main():
    rng = random.Random(222)
    systems = boundary_checks = corrupted = complete = deficient = 0
    for _ in range(2000):
        nr = rng.randint(1, 8)
        nt = rng.randint(nr, nr + 5)
        old_r = [f"r{i}" for i in range(nr)]
        old_t = [f"t{i}" for i in range(nt)]
        old_edges = {(r, old_t[i]) for i, r in enumerate(old_r)}
        for r in old_r:
            for t in old_t:
                if rng.random() < 0.35:
                    old_edges.add((r, t))
        old_assignment = maximum_matching(old_r, old_t, old_edges)
        assert len(old_assignment) == len(old_r)

        removed_r = set(rng.sample(old_r, rng.randint(0, min(3, nr))))
        removed_t = set(rng.sample(old_t, rng.randint(0, min(3, nt))))
        stable_r = [r for r in old_r if r not in removed_r]
        stable_t = [t for t in old_t if t not in removed_t]
        new_r = [f"nr{rng.randrange(10**9)}_{i}" for i in range(rng.randint(0, 3))]
        new_t = [f"nt{rng.randrange(10**9)}_{i}" for i in range(rng.randint(0, 3))]
        next_r = stable_r + new_r
        next_t = stable_t + new_t

        unchanged = {(r, t) for r, t in old_edges if r in stable_r and t in stable_t}
        boundary = {(r, t) for r in new_r for t in next_t} | {(r, t) for r in stable_r for t in new_t}
        assert len(boundary) == len(new_r) * len(next_t) + len(stable_r) * len(new_t)
        next_edges = set(unchanged)
        for pair in boundary:
            if rng.random() < 0.35:
                next_edges.add(pair)
        for r in new_r:
            if next_t and not any(x == r for x, _ in next_edges):
                next_edges.add((r, rng.choice(next_t)))

        rebuilt = unchanged | {pair for pair in boundary if pair in next_edges}
        assert rebuilt == next_edges
        if boundary:
            pair = next(iter(boundary))
            bad = set(rebuilt)
            bad.symmetric_difference_update({pair})
            assert bad != next_edges
            corrupted += 1

        carried = {r: t for r, t in old_assignment.items() if r in stable_r and t in stable_t}
        assert len(set(carried.values())) == len(carried)
        assert all((r, t) in next_edges for r, t in carried.items())
        disturbed = sum(1 for r in stable_r if r in old_assignment and old_assignment[r] not in stable_t)
        churn = len(new_r) + disturbed
        assert len(next_r) - len(carried) <= churn
        new_assignment = maximum_matching(next_r, next_t, next_edges)
        deficit = len(next_r) - len(new_assignment)
        assert deficit <= churn
        if deficit:
            deficient += 1
        else:
            complete += 1
        boundary_checks += len(boundary)
        systems += 1

    print(f"verified {systems} BDA epochs, {boundary_checks} boundary pairs, {corrupted} corruptions, {complete} complete and {deficient} deficient updates")


if __name__ == "__main__":
    main()
