from random import Random


def main() -> None:
    rng = Random(20260731)
    epochs = 11_000
    transfers = adverse = deposits_total = cycles_returned = 0

    for _ in range(epochs):
        rank_count = rng.randint(1, 7)
        mass = [0] * (rank_count + 1)
        mass[0] = rng.randint(0, 35)
        deposits = rng.randint(0, 35)
        mass[0] += deposits
        deposits_total += deposits
        external = mass[0]
        created = 0

        for rank in range(rank_count):
            moved = rng.randint(0, mass[rank])
            mass[rank] -= moved
            mass[rank + 1] += moved
            created += moved
            transfers += moved

            target_recreation = rng.randint(0, moved)
            donor_destruction = moved - target_recreation
            adverse += target_recreation + donor_destruction

        assert created <= rank_count * external
        assert sum(mass) == external

        if rng.random() < 0.08:
            cycles_returned += 1

    print(f"{epochs:,} ranked adverse-source epochs")
    print(f"{transfers:,} precursor transfers")
    print(f"{adverse:,} target-recreation/donor-destruction units")
    print(f"{deposits_total:,} exogenous adverse-source units")
    print(f"{cycles_returned:,} explicit dependency-cycle returns")


if __name__ == "__main__":
    main()
