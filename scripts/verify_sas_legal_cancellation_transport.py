from functools import lru_cache
from random import Random

def max_matching(adj, right_n):
    left_n = len(adj)

    @lru_cache(None)
    def dp(i, used):
        if i == left_n:
            return 0
        best = dp(i + 1, used)
        for j in adj[i]:
            if not (used >> j) & 1:
                best = max(best, 1 + dp(i + 1, used | (1 << j)))
        return best

    return dp(0, 0)

def hall_deficiency_smaller(adj, right_n):
    left_n = len(adj)
    best = 0
    best_mask = 0
    for mask in range(1 << left_n):
        size = mask.bit_count()
        neigh = set()
        for i in range(left_n):
            if mask >> i & 1:
                neigh.update(adj[i])
        val = size - len(neigh)
        if val > best:
            best = val
            best_mask = mask
    return best, best_mask

def main() -> None:
    rng = Random(2026072816)
    systems = 10000
    coordinates = 0
    positive_units = 0
    negative_units = 0
    legal_pairs = 0
    full_cancellation_coords = 0
    deficient_cuts = 0
    incompatibility_units = 0

    for _ in range(systems):
        d = rng.randint(1, 5)
        coordinates += d
        for _coord in range(d):
            p = rng.randint(0, 7)
            n = rng.randint(0, 7)
            positive_units += p
            negative_units += n

            if p <= n:
                left, right = p, n
            else:
                left, right = n, p
            adj = [set(j for j in range(right) if rng.random() < 0.58) for _ in range(left)]
            mu = max_matching(adj, right)
            deficiency, mask = hall_deficiency_smaller(adj, right)
            assert mu == left - deficiency

            legal_pairs += mu
            incompatibility_units += deficiency
            if deficiency == 0:
                full_cancellation_coords += 1
                assert mu == min(p, n)
            else:
                deficient_cuts += 1
                assert mask != 0
                assert mu < min(p, n)

            residual = p + n - 2 * mu
            assert residual == abs(p - n) + 2 * deficiency

    print("SAS legal cancellation transport audit")
    print(f"  systems: {systems}")
    print(f"  boundary coordinates: {coordinates}")
    print(f"  positive units: {positive_units}")
    print(f"  negative units: {negative_units}")
    print(f"  maximum legal cancellation pairs: {legal_pairs}")
    print(f"  full-cancellation coordinates: {full_cancellation_coords}")
    print(f"  deficient sign-pair cuts: {deficient_cuts}")
    print(f"  compatibility-deficiency units: {incompatibility_units}")

if __name__ == "__main__":
    main()
