#!/usr/bin/env python3
"""Finite audit for RI5gw--RI5gz."""

from __future__ import annotations

import random
from collections import Counter

SEED = 1
CASES = 2000


def compat(r: tuple[int, int, int, int], t: tuple[int, int, int, int]) -> bool:
    return r[1] == t[1] and (3 * r[2] + 2 * t[2] + r[3] + t[3]) % 7 not in (0, 1)


def maximum_matching(rs, ts):
    adj = {r[0]: [t[0] for t in ts if compat(r, t)] for r in rs}
    match_t: dict[int, int] = {}

    def visit(rid: int, seen: set[int]) -> bool:
        for tid in adj[rid]:
            if tid in seen:
                continue
            seen.add(tid)
            if tid not in match_t or visit(match_t[tid], seen):
                match_t[tid] = rid
                return True
        return False

    for r in rs:
        visit(r[0], set())
    return len(match_t), {rid: tid for tid, rid in match_t.items()}


def keyed(xs, key_count):
    return {k: [x for x in xs if x[1] == k] for k in range(key_count)}


def main() -> None:
    rng = random.Random(SEED)
    stats: Counter[str] = Counter()
    accepted = 0
    trial = 0
    while accepted < CASES:
        trial += 1
        nr = rng.randint(2, 8)
        key_count = rng.randint(1, 4)
        rs = [(i, rng.randrange(key_count), rng.randrange(9), rng.randrange(3)) for i in range(nr)]
        ts = [(100 + i, rng.randrange(key_count), rng.randrange(9), rng.randrange(3)) for i in range(nr + rng.randint(1, 4))]
        size, old_assignment = maximum_matching(rs, ts)
        if size < nr:
            continue

        r0 = [r for r in rs if rng.random() < 0.65]
        t0 = [t for t in ts if rng.random() < 0.65]
        a, c = rng.randint(0, 3), rng.randint(0, 3)
        dr = [(1000 + 10 * trial + i, rng.randrange(key_count), rng.randrange(9), rng.randrange(3)) for i in range(a)]
        dt = [(100000 + 10 * trial + i, rng.randrange(key_count), rng.randrange(9), rng.randrange(3)) for i in range(c)]
        rp, tp = r0 + dr, t0 + dt

        old_edges = {(r[0], t[0]) for r in rs for t in ts if compat(r, t)}
        full_edges = {(r[0], t[0]) for r in rp for t in tp if compat(r, t)}
        unchanged_edges = {(r[0], t[0]) for r in r0 for t in t0 if (r[0], t[0]) in old_edges}
        boundary = [(r, t) for r in dr for t in tp if r[1] == t[1]]
        boundary += [(r, t) for r in r0 for t in dt if r[1] == t[1]]
        reconstructed = unchanged_edges | {(r[0], t[0]) for r, t in boundary if compat(r, t)}
        assert reconstructed == full_edges

        drk, tpk, r0k, dtk = (keyed(x, key_count) for x in (dr, tp, r0, dt))
        exact = sum(len(drk[k]) * len(tpk[k]) + len(r0k[k]) * len(dtk[k]) for k in range(key_count))
        assert exact == len(boundary)
        lt = max(len(tpk[k]) for k in range(key_count))
        lr = max(len(r0k[k]) for k in range(key_count))
        assert len(boundary) <= a * lt + c * lr

        unchanged_token_ids = {t[0] for t in t0}
        b = sum(1 for r in r0 if old_assignment.get(r[0]) not in unchanged_token_ids)
        e = len(ts) - len(t0)
        assert b <= e
        new_size, _ = maximum_matching(rp, tp)
        deficit = len(rp) - new_size
        assert deficit <= a + b <= a + e

        stats.update(boundary=len(boundary), full_pairs=len(rp) * len(tp), deficient=deficit > 0,
                     deficit=deficit, churn=a + b)
        accepted += 1

    print(f"RI keyed epochs: {accepted}")
    print(f"key-local boundary pairs: {stats['boundary']}")
    print(f"full next-epoch pairs: {stats['full_pairs']}")
    print(f"deficient updates: {stats['deficient']}")
    print(f"total deficit/churn: {stats['deficit']}/{stats['churn']}")


if __name__ == "__main__":
    main()
