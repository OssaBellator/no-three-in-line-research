from random import Random

def max_deficit(demand, capacity, adj):
    n = len(demand)
    best = 0
    best_mask = 0
    for mask in range(1 << n):
        dem = sum(demand[i] for i in range(n) if mask >> i & 1)
        neigh = set()
        for i in range(n):
            if mask >> i & 1:
                neigh.update(adj[i])
        cap = sum(capacity[j] for j in neigh)
        val = dem - cap
        if val > best:
            best = val
            best_mask = mask
    return best, best_mask

def main() -> None:
    rng = Random(2026072812)
    systems = 9000
    deleted_arcs = 0
    added_arcs = 0
    worsened = 0
    local_witnesses = 0
    subset_checks = 0
    total_charge = 0

    for _ in range(systems):
        n = rng.randint(1, 7)
        m = rng.randint(1, 7)
        demand = [rng.randint(0, 5) for _ in range(n)]
        capacity = [rng.randint(0, 6) for _ in range(m)]
        ref = [set(j for j in range(m) if rng.random() < 0.55) for _ in range(n)]
        act = [set(s) for s in ref]
        deleted_by_owner = [set() for _ in range(n)]

        for i in range(n):
            for j in list(act[i]):
                if rng.random() < 0.18:
                    act[i].remove(j)
                    deleted_by_owner[i].add(j)
                    deleted_arcs += 1
            for j in range(m):
                if j not in act[i] and j not in ref[i] and rng.random() < 0.10:
                    act[i].add(j)
                    added_arcs += 1

        charge = [sum(capacity[j] for j in deleted_by_owner[i]) for i in range(n)]
        total_charge += sum(charge)

        for mask in range(1 << n):
            dem = sum(demand[i] for i in range(n) if mask >> i & 1)
            nr = set()
            na = set()
            q = 0
            for i in range(n):
                if mask >> i & 1:
                    nr.update(ref[i])
                    na.update(act[i])
                    q += charge[i]
            dr = dem - sum(capacity[j] for j in nr)
            da = dem - sum(capacity[j] for j in na)
            assert da - dr <= q
            subset_checks += 1

        ref_def, _ = max_deficit(demand, capacity, ref)
        act_def, act_mask = max_deficit(demand, capacity, act)
        assert act_def <= ref_def + sum(charge)
        if act_def > ref_def:
            worsened += 1
            X = [i for i in range(n) if act_mask >> i & 1]
            assert X
            inc = act_def - ref_def
            assert max(charge[i] for i in X) * len(X) >= inc
            local_witnesses += 1

    print("RI owner-local deletion-charge audit")
    print(f"  systems: {systems}")
    print(f"  deleted compatibility arcs: {deleted_arcs}")
    print(f"  added compatibility arcs: {added_arcs}")
    print(f"  owner-subset checks: {subset_checks}")
    print(f"  total local deletion charge: {total_charge}")
    print(f"  worsened systems: {worsened}")
    print(f"  canonical local owner witnesses: {local_witnesses}")

if __name__ == "__main__":
    main()
