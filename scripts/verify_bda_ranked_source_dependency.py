from random import Random


def main() -> None:
    rng = Random(20260729)
    epochs = 10_000
    transfers = terminal = deposited_total = 0

    for _ in range(epochs):
        rank_count = rng.randint(1, 7)
        mass = [0] * (rank_count + 1)
        mass[0] = rng.randint(0, 40)
        deposits = rng.randint(0, 40)
        mass[0] += deposits
        deposited_total += deposits
        external = mass[0]
        created = 0

        for rank in range(rank_count):
            moved = rng.randint(0, mass[rank])
            mass[rank] -= moved
            mass[rank + 1] += moved
            created += moved
            transfers += moved

        terminal += mass[rank_count]
        assert created <= rank_count * external
        assert sum(mass) == external
        assert mass[rank_count] <= external

    print(f"{epochs:,} ranked source epochs")
    print(f"{transfers:,} source-token rank transfers")
    print(f"{terminal:,} terminal source units")
    print(f"{deposited_total:,} exogenous deposited units")


if __name__ == "__main__":
    main()
