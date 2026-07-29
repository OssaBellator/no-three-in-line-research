#!/usr/bin/env python3
"""Finite checks for AC5fu--AC5fy."""

import random

TRACKS = ("AC", "RI", "BDA", "GC", "OP", "SRR", "SAS")


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


def transition(rng, prefix):
    nr = rng.randint(1, 7); nt = rng.randint(nr, nr + 4)
    old_r = [f"{prefix}r{i}" for i in range(nr)]
    old_t = [f"{prefix}t{i}" for i in range(nt)]
    old_edges = {(old_r[i], old_t[i]) for i in range(nr)}
    old_edges |= {(r, t) for r in old_r for t in old_t if rng.random() < 0.32}
    old_assignment = maximum_matching(old_r, old_t, old_edges)
    assert len(old_assignment) == nr

    removed_r = set(rng.sample(old_r, rng.randint(0, min(2, nr))))
    removed_t = set(rng.sample(old_t, rng.randint(0, min(2, nt))))
    stable_r = [r for r in old_r if r not in removed_r]
    stable_t = [t for t in old_t if t not in removed_t]
    new_r = [f"{prefix}nr{rng.randrange(10**8)}_{i}" for i in range(rng.randint(0, 2))]
    new_t = [f"{prefix}nt{rng.randrange(10**8)}_{i}" for i in range(rng.randint(0, 2))]
    next_r, next_t = stable_r + new_r, stable_t + new_t

    unchanged = {(r, t) for r, t in old_edges if r in stable_r and t in stable_t}
    boundary = {(r, t) for r in new_r for t in next_t} | {(r, t) for r in stable_r for t in new_t}
    assert len(boundary) == len(new_r) * len(next_t) + len(stable_r) * len(new_t)
    next_edges = unchanged | {pair for pair in boundary if rng.random() < 0.32}
    for r in new_r:
        if next_t and not any(x == r for x, _ in next_edges):
            next_edges.add((r, rng.choice(next_t)))
    assert next_edges == unchanged | {pair for pair in boundary if pair in next_edges}

    carried = {r: t for r, t in old_assignment.items() if r in stable_r and t in stable_t}
    disturbed = sum(1 for r in stable_r if r in old_assignment and old_assignment[r] not in stable_t)
    churn = len(new_r) + disturbed
    deficit = len(next_r) - len(maximum_matching(next_r, next_t, next_edges))
    assert deficit <= churn
    return len(boundary), churn, deficit


def main():
    rng = random.Random(777)
    macro_epochs = boundary_pairs = total_churn = total_deficit = deficient_epochs = 0
    maximum_macro_deficit = 0

    for epoch in range(1500):
        rows = [transition(rng, f"{track}{epoch}_") for track in TRACKS]
        boundary = sum(row[0] for row in rows)
        churn = sum(row[1] for row in rows)
        deficit = sum(row[2] for row in rows)
        assert deficit <= churn
        if deficit:
            deficient_epochs += 1
            assert max(row[2] for row in rows) * len(TRACKS) >= deficit
        maximum_macro_deficit = max(maximum_macro_deficit, deficit)
        boundary_pairs += boundary
        total_churn += churn
        total_deficit += deficit
        macro_epochs += 1

    print(
        f"verified {macro_epochs} synchronized epochs, {boundary_pairs} boundary pairs, "
        f"churn {total_churn}, deficit {total_deficit}, {deficient_epochs} deficient epochs, "
        f"maximum macro deficit {maximum_macro_deficit}"
    )


if __name__ == "__main__":
    main()
