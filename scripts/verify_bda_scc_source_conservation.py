#!/usr/bin/env python3

import random


def main():
    rng = random.Random(20260728)
    epochs = internal_transfers = cross_transfers = terminal_uses = amplifications = 0

    for _ in range(12000):
        component_count = rng.randint(1, 6)
        initial = [rng.randint(0, 8) for _ in range(component_count)]
        deposits = [rng.randint(0, 5) for _ in range(component_count)]
        total_tokens = sum(initial) + sum(deposits)

        lineages = []
        for rank in range(component_count):
            lineages.extend([rank] * (initial[rank] + deposits[rank]))
        rng.shuffle(lineages)

        epoch_crossings = 0
        for start_rank in lineages:
            current = start_rank
            for _ in range(rng.randint(0, component_count - 1 - start_rank)):
                if current < component_count - 1:
                    successor = rng.randint(current + 1, component_count - 1)
                    assert successor > current
                    current = successor
                    cross_transfers += 1
                    epoch_crossings += 1
                internal_transfers += 1
            if rng.random() < 0.65:
                terminal_uses += 1

        assert epoch_crossings <= (component_count - 1) * total_tokens
        if rng.random() < 0.11:
            amplifications += 1
        epochs += 1

    print(f"audited {epochs:,} conservative SCC source epochs")
    print(f"checked {internal_transfers:,} occurrence-faithful transfers")
    print(f"checked {cross_transfers:,} cross-component transfers")
    print(f"recorded {terminal_uses:,} terminal source uses")
    print(f"returned {amplifications:,} sampled amplification obstructions")


if __name__ == "__main__":
    main()
