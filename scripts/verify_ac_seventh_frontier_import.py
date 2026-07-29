#!/usr/bin/env python3
"""Finite checks for AC5ca--AC5cg."""

from itertools import product


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def sub(a, b, p):
    n = max(len(a), len(b))
    return trim([((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p for i in range(n)])


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def mixed_rank(x, radices):
    out = 0
    for i, value in enumerate(x):
        place = 1
        for k in radices[i + 1 :]:
            place *= k
        out += value * place
    return out


def main() -> None:
    checks = 0
    for seed in range(50000):
        # RI center-plus-label partition.
        K = seed % 5 + 1
        degree = seed % 9
        weights = [((seed + 5 * i + i * i) % 17) for i in range(degree + 1)]
        labels = [((seed + 3 * i + i * i) % K) for i in range(degree)]
        buckets = [weights[0]] + [0] * K
        for w, label in zip(weights[1:], labels):
            buckets[label + 1] += w
        assert sum(buckets) == sum(weights)
        assert max(buckets) * (K + 1) >= sum(weights)

        # Source-cause weighted hole partition.
        na = seed % 5 + 1
        causes = (seed // 5) % 5 + 1
        source_cause = [[0] * causes for _ in range(na)]
        for a in range(na):
            for b in range(7):
                if (seed + 2 * a + 3 * b + a * b) % 4:
                    continue
                source_cause[a][(seed + a + 2 * b) % causes] += (seed + 7 * a + b) % 11
        hole_mass = sum(sum(row) for row in source_cause)
        assert max(max(row) for row in source_cause) * na * causes >= hole_mass

        # BDA realization class partition.
        realization = (seed // 7) % 6 + 1
        pair_weights = [((2 * seed + 3 * i) % 13) for i in range(seed % 10 + 1)]
        rb = [0] * realization
        for i, w in enumerate(pair_weights):
            rb[(seed + i * i) % realization] += w
        assert sum(rb) == sum(pair_weights)
        assert max(rb) * realization >= sum(pair_weights)

        # Sparse label and sign concentration.
        defect_K = (seed // 11) % 6 + 1
        defects = [((seed + 5 * i) % 19) - 9 for i in range(seed % 12 + 1)]
        dm = [0] * defect_K
        dp = [0] * defect_K
        dn = [0] * defect_K
        for i, value in enumerate(defects):
            label = (seed + 3 * i + i * i) % defect_K
            dm[label] += abs(value)
            dp[label] += max(value, 0)
            dn[label] += max(-value, 0)
        total_defect = sum(abs(x) for x in defects)
        heavy = max(range(defect_K), key=lambda j: dm[j])
        assert dm[heavy] * defect_K >= total_defect
        assert max(dp[heavy], dn[heavy]) * 2 >= dm[heavy]

        # Mixed-radix injection/order on one sampled product.
        radices = (2 + seed % 3, 2 + (seed // 3) % 3, 2 + (seed // 9) % 3)
        states = list(product(*(range(k) for k in radices)))
        ranks = [mixed_rank(x, radices) for x in states]
        assert len(set(ranks)) == len(states)
        assert sorted(states) == sorted(states, key=lambda x: mixed_rank(x, radices))

        # Degenerate rational dependence B=lambda*A.
        p = (2, 3, 5, 7)[seed % 4]
        d = seed % 4 + 1
        a0 = trim([(seed + 3 * k) % p for k in range(d + 1)])
        a1 = trim([(seed + 5 * k + 1) % p for k in range(d + 1)])
        lam = trim([(seed + 7 * k + k * k) % p for k in range(d + 1)])
        b0, b1 = mul(lam, a0, p), mul(lam, a1, p)
        assert sub(mul(a0, b1, p), mul(a1, b0, p), p) == (0,)
        if a0 != (0,):
            assert mul(a0, b1, p) == mul(b0, a1, p)
        elif a1 != (0,):
            assert mul(a1, b0, p) == mul(b1, a0, p)
        checks += 1

    print(f"verified {checks} combined AC seventh-frontier instances")


if __name__ == "__main__":
    main()
