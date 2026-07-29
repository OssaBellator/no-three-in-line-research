from math import log2
from random import Random


def primes_below_100() -> list[int]:
    out: list[int] = []
    for n in range(2, 100):
        if all(n % d for d in range(2, int(n**0.5) + 1)):
            out.append(n)
    return out


def main() -> None:
    rng = Random(20260801)
    primes = primes_below_100()
    epochs = 14_000
    accepted = rejected = deposits = novel_primes = 0

    for _ in range(epochs):
        height = rng.randint(2, 10_000)
        support_product = 1
        seen: set[int] = set()

        for _ in range(rng.randint(4, 30)):
            if rng.random() < 0.22:
                height *= rng.randint(2, 9)
                deposits += 1

            picks = rng.sample(primes, rng.randint(1, 3))
            novel = [prime for prime in picks if prime not in seen]
            novel_part = 1
            for prime in novel:
                novel_part *= prime

            if novel_part == 1:
                continue

            if support_product * novel_part <= height:
                support_product *= novel_part
                seen.update(novel)
                accepted += 1
                novel_primes += len(novel)
                assert support_product <= height
                assert len(seen) <= int(log2(height))
            else:
                rejected += 1

    print(f"{epochs:,} multiplicative height epochs")
    print(f"{accepted:,} accepted novel-factor witnesses")
    print(f"{novel_primes:,} newly charged primes")
    print(f"{deposits:,} multiplicative height deposits")
    print(f"{rejected:,} exact unpaid factor-creation returns")


if __name__ == "__main__":
    main()
