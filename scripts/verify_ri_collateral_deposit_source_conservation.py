import random


def main():
    rng = random.Random(1503)
    systems = 6500
    totals = {
        "physical_sources": 0,
        "collateral_classes": 0,
        "transfers": 0,
        "initial_mass": 0,
        "exogenous_deposits": 0,
        "collateral_issued": 0,
        "collateral_paid": 0,
        "terminal_mass": 0,
        "amplification_witnesses": 0,
    }

    for _ in range(systems):
        np = rng.randint(2, 6)
        nc = rng.randint(2, 6)
        live = [rng.randint(0, 8) for _ in range(np)]
        collateral = [0] * nc
        initial = sum(live)
        exogenous = 0
        issued = 0
        paid = 0
        terminal = 0
        witness = False

        for _step in range(rng.randint(8, 20)):
            operation = rng.randrange(5)
            if operation == 0:
                u = rng.randrange(np)
                v = rng.randrange(np)
                amount = rng.randint(0, live[u] if live[u] else 0)
                loss = rng.randint(0, amount)
                live[u] -= amount
                live[v] += amount - loss
                terminal += loss
                totals["transfers"] += 1
            elif operation == 1:
                u = rng.randrange(np)
                amount = rng.randint(0, 5)
                live[u] += amount
                exogenous += amount
            elif operation == 2:
                u = rng.randrange(np)
                c = rng.randrange(nc)
                amount = rng.randint(0, live[u] if live[u] else 0)
                live[u] -= amount
                collateral[c] += amount
                issued += amount
            elif operation == 3:
                c = rng.randrange(nc)
                amount = rng.randint(0, collateral[c] if collateral[c] else 0)
                collateral[c] -= amount
                paid += amount
                terminal += amount
            elif rng.random() < 0.22:
                c = rng.randrange(nc)
                amount = rng.randint(1, 3)
                collateral[c] += amount
                issued += amount
                witness = True

            if sum(live) + sum(collateral) + terminal > initial + exogenous:
                witness = True
                break

        totals["physical_sources"] += np
        totals["collateral_classes"] += nc
        totals["initial_mass"] += initial
        totals["exogenous_deposits"] += exogenous
        totals["collateral_issued"] += issued
        totals["collateral_paid"] += paid
        totals["terminal_mass"] += terminal
        if witness:
            totals["amplification_witnesses"] += 1

    print(f"systems={systems}")
    for key, value in totals.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
