#!/usr/bin/env python3
from __future__ import annotations

import math
import random
from collections import Counter, defaultdict

TRACKS = ("AC", "RI", "BDA", "GC", "OP", "SRR", "SAS")
CASES = 1500
SEED = 52057


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


def run_track(rng, track):
    h = rng.randint(1, 4)
    support = tuple(range(h))
    key_count = rng.randint(1, 4)
    stable = rng.randint(1, 7)
    changed_r = rng.randint(0, 6)
    changed_t = rng.randint(0, 6)
    lost_old_t = rng.randint(0, 5)

    r_stable = [f"{track}s{i}" for i in range(stable)]
    r_changed = [f"{track}c{i}" for i in range(changed_r)]
    r_disturbed = [f"{track}d{i}" for i in range(lost_old_t)]
    R = r_stable + r_changed + r_disturbed
    t_stable = [f"{track}u{i}" for i in range(stable)]
    t_new = [f"{track}n{i}" for i in range(changed_t)]
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
    labels = [
        (track, cause_r[r] if r in cause_r else cause_lost[r])
        for r in unmatched
    ]
    return h, boundary, len(R) * len(T), disturbance, deficit, labels


def main():
    rng = random.Random(SEED)
    totals = Counter()
    for _ in range(CASES):
        active_support = 0
        macro_deficit = 0
        labels = []
        for track in TRACKS:
            h, boundary, full, disturbance, deficit, roots = run_track(rng, track)
            active_support += h
            macro_deficit += deficit
            labels.extend(roots)
            totals["boundary"] += boundary
            totals["full"] += full
            totals["disturbance"] += disturbance
        totals["deficit"] += macro_deficit
        if macro_deficit:
            assert max(Counter(labels).values()) >= math.ceil(
                macro_deficit / active_support
            )

    print(
        f"verified {CASES} synchronized support-local macro epochs; "
        f"{totals['boundary']} key-local pairs / {totals['full']} full pairs; "
        f"{totals['disturbance']} disturbed roots; {totals['deficit']} residual deficits"
    )


if __name__ == "__main__":
    main()
