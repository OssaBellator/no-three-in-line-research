from functools import lru_cache
from random import Random

def min_cost_transport(demand, capacity, adj, cost):
    units = []
    for i, d in enumerate(demand):
        units.extend([i] * d)

    @lru_cache(None)
    def dp(k, caps):
        if k == len(units):
            return 0
        i = units[k]
        best = None
        caps = list(caps)
        for j in adj[i]:
            if caps[j] > 0:
                caps[j] -= 1
                sub = dp(k + 1, tuple(caps))
                caps[j] += 1
                if sub is not None:
                    val = cost[j] + sub
                    if best is None or val < best:
                        best = val
        return best

    return dp(0, tuple(capacity))

def hall_deficit(demand, capacity, adj):
    n = len(demand)
    best = 0
    for mask in range(1 << n):
        dem = sum(demand[i] for i in range(n) if mask >> i & 1)
        neigh = set()
        for i in range(n):
            if mask >> i & 1:
                neigh.update(adj[i])
        best = max(best, dem - sum(capacity[j] for j in neigh))
    return best

def main() -> None:
    rng = Random(2026072813)
    epochs = 7000
    feasible_epochs = 0
    infeasible_cuts = 0
    paid_epochs = 0
    overload_epochs = 0
    zero_loss_epochs = 0
    total_min_loss = 0
    total_deposits = 0
    threshold_checks = 0

    reserve = 30
    for _ in range(epochs):
        n = rng.randint(1, 4)
        m = rng.randint(1, 5)
        demand = [rng.randint(0, 2) for _ in range(n)]
        capacity = [rng.randint(0, 3) for _ in range(m)]
        cost = [rng.randint(0, 5) for _ in range(m)]
        adj = [set(j for j in range(m) if rng.random() < 0.65) for _ in range(n)]
        deposit = rng.randint(0, 3)
        reserve += deposit
        total_deposits += deposit

        loss = min_cost_transport(demand, capacity, adj, cost)
        if loss is None:
            assert hall_deficit(demand, capacity, adj) > 0
            infeasible_cuts += 1
            continue

        feasible_epochs += 1
        total_min_loss += loss
        if loss == 0:
            zero_loss_epochs += 1

        for J in range(1, 6):
            if loss >= J:
                threshold_checks += 1

        if loss <= reserve:
            reserve -= loss
            paid_epochs += 1
        else:
            overload_epochs += 1
            assert loss > reserve
            reserve = 0

    assert paid_epochs + overload_epochs == feasible_epochs
    print("GC clean-height bank audit")
    print(f"  epochs: {epochs}")
    print(f"  feasible epochs: {feasible_epochs}")
    print(f"  infeasible Hall cuts: {infeasible_cuts}")
    print(f"  zero-loss preservation epochs: {zero_loss_epochs}")
    print(f"  paid epochs: {paid_epochs}")
    print(f"  clean-height overload epochs: {overload_epochs}")
    print(f"  minimum-loss units: {total_min_loss}")
    print(f"  exact deposits: {total_deposits}")
    print(f"  threshold loss checks: {threshold_checks}")

if __name__ == "__main__":
    main()
