from random import Random


def main() -> None:
    rng = Random(20260730)
    epochs = 12_000
    payments = overloads = deposits_total = 0

    for _ in range(epochs):
        owners = rng.randint(1, 10)
        initial = [rng.randint(0, 25) for _ in range(owners)]
        deposits = [rng.randint(0, 20) for _ in range(owners)]
        balance = [initial[i] + deposits[i] for i in range(owners)]
        used = [0] * owners
        deposits_total += sum(deposits)

        for _ in range(rng.randint(5, 40)):
            owner = rng.randrange(owners)
            symmetric_cost = rng.randint(1, 7)
            if balance[owner] >= symmetric_cost:
                balance[owner] -= symmetric_cost
                used[owner] += symmetric_cost
                payments += 1
            else:
                overloads += 1

        for owner in range(owners):
            assert used[owner] <= initial[owner] + deposits[owner]

    print(f"{epochs:,} owner-collateral epochs")
    print(f"{payments:,} symmetric fibre payments")
    print(f"{overloads:,} exact owner-collateral overloads")
    print(f"{deposits_total:,} collateral deposit units")


if __name__ == "__main__":
    main()
