from random import Random


def main() -> None:
    rng = Random(20260728)
    epochs = 12_000
    paid = overloads = deposited = 0
    threshold_checks = 0

    for _ in range(epochs):
        classes = rng.randint(1, 8)
        initial = [rng.randint(0, 30) for _ in range(classes)]
        deposits = [rng.randint(0, 25) for _ in range(classes)]
        threshold = [rng.randint(1, 8) for _ in range(classes)]
        balance = [initial[i] + deposits[i] for i in range(classes)]
        used = [0] * classes
        deposited += sum(deposits)

        for _ in range(rng.randint(5, 45)):
            cls = rng.randrange(classes)
            threshold_checks += 1
            if balance[cls] >= threshold[cls]:
                balance[cls] -= threshold[cls]
                used[cls] += threshold[cls]
                paid += 1
            else:
                overloads += 1

        for cls in range(classes):
            available = initial[cls] + deposits[cls]
            assert used[cls] <= available
            assert used[cls] // threshold[cls] <= available // threshold[cls]

    print(f"{epochs:,} obstruction-bank epochs")
    print(f"{paid:,} paid menu failures")
    print(f"{overloads:,} exact obstruction overloads")
    print(f"{deposited:,} deposited obstruction-capacity units")
    print(f"{threshold_checks:,} class-threshold checks")


if __name__ == "__main__":
    main()
