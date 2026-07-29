#!/usr/bin/env python3
"""Finite checks for RI5hm--RI5hp."""
from collections import Counter, defaultdict, deque
import random


def run(seed=83, cases=2500):
    rng = random.Random(seed)
    stats = Counter()
    for _ in range(cases):
        m, b, c, surplus = rng.randint(1, 8), rng.randint(0, 8), rng.randint(0, 6), rng.randint(0, 4)
        U = [f"u{i}" for i in range(m)]
        A = U + [f"a{i}" for i in range(b)]
        B = [f"b{i}" for i in range(b)]
        CR, CT = [f"c{i}" for i in range(c)], [f"d{i}" for i in range(c)]
        Z = [f"z{i}" for i in range(m + surplus)]
        R, T = A + CR, B + CT + Z
        M = {(f"a{i}", f"b{i}") for i in range(b)} | {(f"c{i}", f"d{i}") for i in range(c)}
        E = set(M)
        for r in A:
            for t in B:
                if rng.random() < 0.45:
                    E.add((r, t))
        mt = {t: r for r, t in M}
        sr, st, qd = set(U), set(), deque(U)
        while qd:
            x = qd.popleft()
            if x in R:
                for r, t in E:
                    if r == x and (r, t) not in M and t not in st:
                        st.add(t); qd.append(t)
            elif x in mt and mt[x] not in sr:
                sr.add(mt[x]); qd.append(mt[x])
        assert {t for r, t in E if r in sr} == st
        assert len(sr) - len(st) == m
        free = [t for t in T if t not in {y for x, y in M}]
        assert set(free).isdisjoint(st) and len(free) >= m
        assert all((r, t) not in E for r in U for t in free)
        q = rng.randint(1, 6)
        labelled = [(r, t, rng.randrange(max(1, m * len(free) // 3)), rng.randrange(q)) for r in U for t in free]
        pc = Counter(p for r, t, w, p in labelled)
        p = max(pc, key=pc.get)
        F = [e for e in labelled if e[3] == p]
        assert len(F) * q >= m * len(free)
        r, t, w, p = F[0]
        assert len(M | {(r, t)}) == len(M) + 1
        rng.shuffle(F)
        used_r, used_t, N = set(), set(), []
        for e in F:
            r, t, w, p = e
            if r not in used_r and t not in used_t:
                used_r.add(r); used_t.add(t); N.append(e)
        by = defaultdict(list)
        for e in N: by[e[2]].append(e)
        mu = rng.randint(1, 4)
        if by and max(map(len, by.values())) >= mu + 1:
            Q = max(by.values(), key=len); stats['overload_batches'] += 1
        else:
            Q = [v[0] for v in by.values()]; stats['independent_stocks'] += 1
            assert len({e[2] for e in Q}) == len(Q)
        add = {(r, t) for r, t, w, p in Q}
        assert len({r for r, t in add}) == len(add) == len({t for r, t in add})
        assert len(M | add) == len(M) + len(add)
        stats['systems'] += 1
        stats['free_rectangle_pairs'] += m * len(free)
        stats['predicate_pairs'] += len(F)
        stats['repair_gain'] += len(add)
    print(dict(stats))


if __name__ == '__main__':
    run()
