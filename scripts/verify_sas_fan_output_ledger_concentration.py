from random import Random


def main() -> None:
    rng = Random(20260803)
    epochs = 10_000
    candidates = paid = overloads = total_output = 0

    for _ in range(epochs):
        ledgers = rng.randint(1, 8)
        capacities = [rng.randint(20, 120) for _ in range(ledgers)]
        aggregate = [0] * ledgers
        total_weight = 0
        certified_output = 0

        for _ in range(rng.randint(4, 30)):
            weight = rng.randint(1, 8)
            output = [rng.randint(0, 4) * weight for _ in range(ledgers)]
            if sum(output) < weight:
                output[rng.randrange(ledgers)] += weight

            total_weight += weight
            certified_output += sum(output)
            candidates += 1
            for ledger in range(ledgers):
                aggregate[ledger] += output[ledger]

        assert max(aggregate) * ledgers >= certified_output
        assert certified_output >= total_weight

        if any(aggregate[j] > capacities[j] for j in range(ledgers)):
            overloads += 1
        else:
            paid += 1
        total_output += certified_output

    print(f"{epochs:,} compatible fan epochs")
    print(f"{candidates:,} fan candidates")
    print(f"{total_output:,} aggregate barrier/neutral output units")
    print(f"{paid:,} fully capacity-paid fans")
    print(f"{overloads:,} exact output-ledger overloads")


if __name__ == "__main__":
    main()
