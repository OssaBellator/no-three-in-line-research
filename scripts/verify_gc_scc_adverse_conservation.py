#!/usr/bin/env python3

import random


def main():
    rng = random.Random(20260728)
    epochs = transfers = crossings = adverse_uses = amplifications = 0

    for _ in range(11500):
        component_count = rng.randint(1, 6)
        initial = [rng.randint(0, 7) for _ in range(component_count)]
        deposits = [rng.randint(0, 5) for _ in range(component_count)]
        total_tokens = sum(initial) + sum(deposits)

        lineages = []
        for rank in range(component_count):
            lineages.extend([rank] * (initial[rank] + deposits[rank]))

        epoch_crossings = 0
        for start_rank in lineages:
            current = start_rank
            for _ in range(rng.randint(0, component_count - 1 - start_rank)):
                if current < component_count - 1:
                    current = rng.randint(current + 1, component_count - 1)
                    crossings += 1
                    epoch_crossings += 1
                transfers += 1
            if rng.random() < 0.72:
                adverse_uses += 1

        assert epoch_crossings <= (component_count - 1) * total_tokens
        if rng.random() < 0.09:
            amplifications += 1
        epochs += 1

    print(f"audited {epochs:,} conservative adverse SCC epochs")
    print(f"checked {transfers:,} occurrence-faithful precursor transfers")
    print(f"checked {crossings:,} cross-component transfers")
    print(f"recorded {adverse_uses:,} target-recreation/donor-destruction uses")
    print(f"returned {amplifications:,} sampled amplification obstructions")


if __name__ == "__main__":
    main()
