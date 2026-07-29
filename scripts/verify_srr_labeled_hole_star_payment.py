#!/usr/bin/env python3
"""Finite checks for SRR2as--SRR2av."""

from itertools import product


def main() -> None:
    checks = 0
    for na in range(1, 6):
        for nb in range(1, 7):
            for K in range(1, 5):
                for seed in range(1200):
                    buckets = [[0 for _ in range(K)] for _ in range(na)]
                    total = 0
                    for a in range(na):
                        for b in range(nb):
                            hole = ((seed + 3 * a + 5 * b + a * b) % 5) < 2
                            if not hole:
                                continue
                            weight = (seed + 7 * a + 11 * b) % 9
                            cause = (seed + 2 * a + 3 * b + a * b) % K
                            buckets[a][cause] += weight
                            total += weight
                    assert sum(sum(row) for row in buckets) == total
                    assert max(max(row) for row in buckets) * na * K >= total

                    tau = seed % (na + 1)
                    Lambda = (seed * 3 + 4) % 17
                    exceptional_weight = 0
                    weighted_mass = 0
                    for b in range(nb):
                        multiplicity = sum(
                            ((seed + 3 * a + 5 * b + a * b) % 5) < 2
                            for a in range(na)
                        )
                        weight = (seed + 11 * b) % 9
                        weighted_mass += multiplicity * weight
                        if multiplicity > tau:
                            exceptional_weight += weight
                    assert exceptional_weight * (tau + 1) <= weighted_mass
                    if exceptional_weight > Lambda:
                        # Rebuild source-cause buckets with endpoint-only weights.
                        bc = [[0 for _ in range(K)] for _ in range(na)]
                        for a in range(na):
                            for b in range(nb):
                                if ((seed + 3 * a + 5 * b + a * b) % 5) >= 2:
                                    continue
                                weight = (seed + 11 * b) % 9
                                cause = (seed + 2 * a + 3 * b + a * b) % K
                                bc[a][cause] += weight
                        assert max(max(row) for row in bc) * na * K > (tau + 1) * Lambda
                    checks += 1
    print(f"verified {checks} labeled source-hole systems")


if __name__ == "__main__":
    main()
