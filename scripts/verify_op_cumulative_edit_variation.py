from random import Random

def max_deficit(demand, capacity, adj):
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
    rng = Random(2026072814)
    epochs = 5000
    steps_total = 0
    deletion_charge = 0
    positive_variation = 0
    negative_variation = 0
    unit_edits = 0
    jump_checks = 0
    closed_epochs = 0

    for _ in range(epochs):
        n = rng.randint(1, 6)
        m = rng.randint(1, 7)
        demand = [rng.randint(0, 4) for _ in range(n)]
        capacity = [rng.randint(0, 5) for _ in range(m)]
        adj = [set(j for j in range(m) if rng.random() < 0.55) for _ in range(n)]
        start_adj = [set(s) for s in adj]
        deficit = max_deficit(demand, capacity, adj)
        epoch_charge = 0
        epoch_pos = 0

        for _ in range(rng.randint(1, 10)):
            steps_total += 1
            old = deficit
            i = rng.randrange(n)
            j = rng.randrange(m)
            step_charge = 0
            if j in adj[i]:
                adj[i].remove(j)
                step_charge = capacity[j]
                epoch_charge += step_charge
                deletion_charge += step_charge
            else:
                adj[i].add(j)

            if rng.random() < 0.18:
                unit_edits += 1

            deficit = max_deficit(demand, capacity, adj)
            delta = deficit - old
            if delta > 0:
                positive_variation += delta
                epoch_pos += delta
                assert delta <= step_charge
                for _J in range(1, delta + 1):
                    jump_checks += 1
            elif delta < 0:
                negative_variation += -delta

        assert epoch_pos <= epoch_charge
        if all(adj[i] == start_adj[i] for i in range(n)):
            closed_epochs += 1
            assert deficit == max_deficit(demand, capacity, start_adj)

    print("OP cumulative edit-variation audit")
    print(f"  epochs: {epochs}")
    print(f"  edit steps: {steps_total}")
    print(f"  deletion-capacity charge: {deletion_charge}")
    print(f"  positive deficit variation: {positive_variation}")
    print(f"  negative deficit variation: {negative_variation}")
    print(f"  unit-field edits: {unit_edits}")
    print(f"  threshold jump checks: {jump_checks}")
    print(f"  exact closed signature epochs: {closed_epochs}")

if __name__ == "__main__":
    main()
