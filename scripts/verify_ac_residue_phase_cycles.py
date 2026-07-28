#!/usr/bin/env python3
"""Finite audit for AC3wa--AC3we.

This verifies only finite residue automata and displayed arithmetic identities.
The Markdown note contains the arbitrary-size proof.
"""

from itertools import product
import random


def orbit_and_cycle(trans, start):
    seen = {}
    seq = []
    phase = start
    while phase not in seen:
        seen[phase] = len(seq)
        seq.append(phase)
        phase = trans[phase][0]
    cut = seen[phase]
    return seq[:cut], seq[cut:], phase


def main():
    rng = random.Random(1729)
    cases = phase_slots = positive = negative = zero = 0

    for q in range(1, 4):
        for moduli in product(range(2, 5), repeat=q):
            phases = list(product(*[range(m) for m in moduli]))
            for _ in range(80):
                trans = {}
                for phase in phases:
                    increment = tuple(rng.randint(-2, 2) for _ in range(q))
                    next_phase = tuple(
                        (phase[i] + increment[i]) % moduli[i]
                        for i in range(q)
                    )
                    requirement = tuple(rng.randint(0, 4) for _ in range(q))
                    trans[phase] = (next_phase, increment, requirement)

                for start in rng.sample(phases, min(4, len(phases))):
                    preperiod, cycle, repeated = orbit_and_cycle(trans, start)
                    assert len(preperiod) + len(cycle) <= len(phases)
                    assert cycle and repeated == cycle[0]

                    drift = [0] * q
                    block_requirement = [0] * q
                    prefix = [0] * q
                    for phase in cycle:
                        _, increment, requirement = trans[phase]
                        for i in range(q):
                            block_requirement[i] = max(
                                block_requirement[i], requirement[i] - prefix[i]
                            )
                            prefix[i] += increment[i]
                            drift[i] += increment[i]

                    assert all(
                        drift[i] % moduli[i] == 0 for i in range(q)
                    )

                    if any(value < 0 for value in drift):
                        negative += 1
                        base = [
                            block_requirement[i] + rng.randint(0, 30)
                            for i in range(q)
                        ]
                        bounds = [
                            (base[i] - block_requirement[i]) // (-value) + 1
                            for i, value in enumerate(drift)
                            if value < 0
                        ]
                        first_failure = min(bounds)
                        assert all(
                            base[i] + (first_failure - 1) * drift[i]
                            >= block_requirement[i]
                            for i, value in enumerate(drift)
                            if value < 0
                        )
                        assert any(
                            base[i] + first_failure * drift[i]
                            < block_requirement[i]
                            for i, value in enumerate(drift)
                            if value < 0
                        )
                    elif any(value > 0 for value in drift):
                        positive += 1
                        assert all(value >= 0 for value in drift)
                    else:
                        zero += 1
                        assert prefix == [0] * q

                    cases += 1
                    phase_slots += len(cycle)

    print(f"{cases:,} residue systems checked")
    print(f"{phase_slots:,} eventual phase-cycle slots")
    print(f"{positive:,} monotone positive-drift blocks")
    print(f"{negative:,} finite negative-headroom blocks")
    print(f"{zero:,} exact zero-drift returns")


if __name__ == "__main__":
    main()
