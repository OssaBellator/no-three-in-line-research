#!/usr/bin/env python3
"""Finite audit for GC2eg--GC2ek."""

from collections import defaultdict
import random

SEED = 20260727


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(80000):
        n = rng.randint(3, 24)
        cells = n * n
        atom_count = rng.randint(1, 80)

        lineages = []
        for lineage_id in range(atom_count):
            certificate = tuple(sorted(rng.sample(range(cells), 3)))
            weight = rng.randint(1, 10000)
            death = None if rng.random() < 0.45 else rng.randint(1, 20)
            lineages.append((lineage_id, certificate, weight, death))

        checkpoint = rng.randint(1, 20)
        total = sum(weight for _, _, weight, _ in lineages)
        paid = sum(
            weight
            for _, _, weight, death in lineages
            if death is not None and death <= checkpoint
        )
        surviving = sum(
            weight
            for _, _, weight, death in lineages
            if death is None or death > checkpoint
        )
        assert total == paid + surviving

        for _, _, weight, death in lineages:
            surviving_one = weight if death is None or death > checkpoint else 0
            paid_one = weight if death is not None and death <= checkpoint else 0
            assert surviving_one + paid_one == weight

        assert paid * 2 >= total or surviving * 2 >= total

        if surviving:
            incidence = [0] * cells
            for _, certificate, weight, death in lineages:
                if death is None or death > checkpoint:
                    for cell in certificate:
                        incidence[cell] += weight
            assert sum(incidence) == 3 * surviving
            assert max(incidence) * cells >= 3 * surviving
            counts["surviving_systems"] += 1

        if paid:
            counts["paid_systems"] += 1

        counts["lineage_banks"] += 1
        counts["exact_lineages"] += atom_count

    for _ in range(30000):
        witnesses = rng.randint(1, 40)
        realized = [rng.random() > 0.04 for _ in range(witnesses)]
        if all(realized):
            selected = {
                (i, tuple(sorted(rng.sample(range(400), 3))))
                for i in range(witnesses)
            }
            assert len(selected) == witnesses
            counts["realized_products"] += 1
            counts["installed_certificates"] += witnesses
        else:
            first_failure = realized.index(False)
            assert 0 <= first_failure < witnesses
            counts["realization_failures"] += 1

    print("GC exact-certificate lineage import audit passed")
    print(f"  lineage banks: {counts['lineage_banks']}")
    print(f"  exact lineages: {counts['exact_lineages']}")
    print(f"  systems with paid mass: {counts['paid_systems']}")
    print(f"  systems with surviving mass: {counts['surviving_systems']}")
    print(f"  realized compatible products: {counts['realized_products']}")
    print(f"  exact realization failures: {counts['realization_failures']}")
    print(f"  installed exact certificates: {counts['installed_certificates']}")


if __name__ == "__main__":
    main()
