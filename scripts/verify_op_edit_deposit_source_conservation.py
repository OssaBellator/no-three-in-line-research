import random


def main():
    rng = random.Random(1505)
    systems = 6500
    totals = {
        "physical_sources": 0,
        "edit_classes": 0,
        "transfers": 0,
        "initial_mass": 0,
        "exogenous_deposits": 0,
        "edit_issued": 0,
        "edit_paid": 0,
        "terminal_mass": 0,
        "amplification_witnesses": 0,
    }

    for _ in range(systems):
        np = rng.randint(2, 6)
        ne = rng.randint(2, 6)
        live = [rng.randint(0, 8) for _ in range(np)]
        edit = [0] * ne
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
                e = rng.randrange(ne)
                amount = rng.randint(0, live[u] if live[u] else 0)
                live[u] -= amount
                edit[e] += amount
                issued += amount
            elif operation == 3:
                e = rng.randrange(ne)
                amount = rng.randint(0, edit[e] if edit[e] else 0)
                edit[e] -= amount
                paid += amount
                terminal += amount
            elif rng.random() < 0.23:
                e = rng.randrange(ne)
                amount = rng.randint(1, 3)
                edit[e] += amount
                issued += amount
                witness = True

            if sum(live) + sum(edit) + terminal > initial + exogenous:
                witness = True
                break

        totals["physical_sources"] += np
        totals["edit_classes"] += ne
        totals["initial_mass"] += initial
        totals["exogenous_deposits"] += exogenous
        totals["edit_issued"] += issued
        totals["edit_paid"] += paid
        totals["terminal_mass"] += terminal
        if witness:
            totals["amplification_witnesses"] += 1

    print(f"systems={systems}")
    for key, value in totals.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
