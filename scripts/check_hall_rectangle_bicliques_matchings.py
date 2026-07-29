#!/usr/bin/env python3
from itertools import combinations, product
from math import comb, ceil


def max_matching(rows, t):
    match_t = [-1] * t

    def aug(x, seen):
        for y in rows[x]:
            if seen[y]:
                continue
            seen[y] = True
            if match_t[y] < 0 or aug(match_t[y], seen):
                match_t[y] = x
                return True
        return False

    ans = 0
    for x in range(len(rows)):
        ans += aug(x, [False] * t)
    return ans


def main():
    s, t, d = 4, 5, 2
    neighbourhoods = list(combinations(range(t), d))
    checked = 0
    for rows in product(neighbourhoods, repeat=s):
        checked += 1
        for q in (1, 2):
            best = 0
            for core in combinations(range(t), q):
                carriers = sum(set(core).issubset(row) for row in rows)
                best = max(best, carriers)
            bound = ceil(s * comb(d, q) / comb(t, q))
            assert best >= bound

        target_deg = [sum(y in row for row in rows) for y in range(t)]
        D = d
        Delta = max(target_deg)
        E = s * d
        bound_m = ceil(E / (D + Delta - 1))
        assert max_matching(rows, t) >= bound_m

    print({
        "all_checks_passed": True,
        "rectangles_checked": checked,
        "sources": s,
        "targets": t,
        "source_degree": d,
    })


if __name__ == "__main__":
    main()
