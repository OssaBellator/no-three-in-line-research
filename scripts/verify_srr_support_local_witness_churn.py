#!/usr/bin/env python3
from __future__ import annotations

import math
import random
from collections import Counter, defaultdict

CASES = 2500
SEED = 52055


def augment_to_max(R, edges, carried):
    match_r = dict(carried)
    match_t = {t: r for r, t in carried.items()}
    initial_unmatched = set(R) - set(match_r)

    def dfs(r, seen_r, seen_t):
        if r in seen_r:
            return False
        seen_r.add(r)
        for t in edges[r]:
            if t in seen_t:
                continue
            seen_t.add(t)
            mate = match_t.get(t)
            if mate is None or dfs(mate, seen_r, seen_t):
                old = match_r.get(r)
                if old is not None:
                    match_t.pop(old, None)
                match_r[r] = t
                match_t[t] = r
                return True
        return False

    changed = True
    while changed:
        changed = False
        for r in R:
            if r not in match_r and dfs(r, set(), set()):
                changed = True
    return match_r, initial_unmatched


def run_case(rng):
    h = rng.randint(1, 5)
    support = tuple(range(h))
    key_count = rng.randint(1, 4)
    stable = rng.randint(1, 8)
    changed_r = rng.randint(0, 7)
    changed_t = rng.randint(0, 7)
    lost_old_t = rng.randint(0, 6)

    r_stable = [f"s{i}" for i in range(stable)]
    r_changed = [f"c{i}" for i in range(changed_r)]
    r_disturbed = [f"d{i}" for i in range(lost_old_t)]
    R = r_stable + r_changed + r_disturbed
    t_stable = [f"u{i}" for i in range(stable)]
    t_new = [f"n{i}" for i in range(changed_t)]
    T = t_stable + t_new

    key_r, key_t = {}, {}
    for i, r in enumerate(r_stable):
        key = rng.randrange(key_count)
        key_r[r] = key
        key_t[t_stable[i]] = key
    for r in r_changed + r_disturbed:
        key_r[r] = rng.randrange(key_count)
    for t in t_new:
        key_t[t] = rng.randrange(key_count)

    cause_r = {r: rng.choice(support) for r in r_changed}
    cause_lost = {r: rng.choice(support) for r in r_disturbed}
    cause_t = {t: rng.choice(support) for t in t_new}
    alpha_r = max((sum(x == c for c in cause_r.values()) for x in support), default=0)
    alpha_plus = max((sum(x == c for c in cause_t.values()) for x in support), default=0)
    alpha_minus = max((sum(x == c for c in cause_lost.values()) for x in support), default=0)
    assert changed_r <= h * alpha_r if changed_r else alpha_r == 0
    assert changed_t <= h * alpha_plus if changed_t else alpha_plus == 0
    assert lost_old_t <= h * alpha_minus if lost_old_t else alpha_minus == 0

    dr = Counter(key_r[r] for r in r_changed)
    dt = Counter(key_t[t] for t in t_new)
    sr = Counter(key_r[r] for r in r_stable)
    nt = Counter(key_t[t] for t in T)
    boundary = sum(dr[k] * nt[k] + sr[k] * dt[k] for k in range(key_count))
    lt = max(nt.values(), default=0)
    lr = max(sr.values(), default=0)
    assert boundary <= changed_r * lt + changed_t * lr
    assert boundary <= h * (alpha_r * lt + alpha_plus * lr)

    carried = {r_stable[i]: t_stable[i] for i in range(stable)}
    edges = defaultdict(list)
    for i, r in enumerate(r_stable):
        edges[r].append(t_stable[i])
    for r in R:
        for t in T:
            if key_r[r] == key_t[t] and rng.random() < 0.35 and t not in edges[r]:
                edges[r].append(t)

    matching, initial_unmatched = augment_to_max(R, edges, carried)
    expected = set(r_changed + r_disturbed)
    assert initial_unmatched == expected
    unmatched = set(R) - set(matching)
    assert unmatched <= expected
    deficit = len(unmatched)
    disturbance = changed_r + lost_old_t
    assert deficit <= disturbance <= h * (alpha_r + alpha_minus)
    if deficit:
        causes = [cause_r[r] if r in cause_r else cause_lost[r] for r in unmatched]
        assert max(Counter(causes).values()) >= math.ceil(deficit / h)
    return boundary, len(R) * len(T), disturbance, deficit


def main():
    rng = random.Random(SEED)
    totals = Counter()
    for _ in range(CASES):
        boundary, full, disturbance, deficit = run_case(rng)
        totals["boundary"] += boundary
        totals["full"] += full
        totals["disturbance"] += disturbance
        totals["deficit"] += deficit
    print(
        f"verified {CASES} SRR support-local systems; "
        f"{totals['boundary']} key-local pairs / {totals['full']} full pairs; "
        f"{totals['disturbance']} disturbed roots; {totals['deficit']} residual deficits"
    )


if __name__ == "__main__":
    main()
