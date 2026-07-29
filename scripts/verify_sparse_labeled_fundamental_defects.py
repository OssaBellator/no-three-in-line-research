#!/usr/bin/env python3
"""Finite checks for SAS5ig--SAS5ij."""


def main() -> None:
    checks = 0
    for beta in range(1, 25):
        for K in range(1, 8):
            for seed in range(1200):
                defects = [((seed + 5 * i + i * i) % 21) - 10 for i in range(beta)]
                labels = [((seed + 3 * i + i * i) % K) for i in range(beta)]
                masses = [0] * K
                pos = [0] * K
                neg = [0] * K
                counts = [0] * K
                pos_counts = [0] * K
                neg_counts = [0] * K
                for d, label in zip(defects, labels):
                    masses[label] += abs(d)
                    counts[label] += 1
                    if d > 0:
                        pos[label] += d
                        pos_counts[label] += 1
                    elif d < 0:
                        neg[label] += -d
                        neg_counts[label] += 1
                total = sum(abs(d) for d in defects)
                assert sum(masses) == total
                heavy_label = max(range(K), key=lambda j: masses[j])
                assert masses[heavy_label] * K >= total
                assert max(pos[heavy_label], neg[heavy_label]) * 2 >= masses[heavy_label]

                if masses[heavy_label] > 0:
                    edge_max = max(abs(d) for d, lab in zip(defects, labels) if lab == heavy_label)
                    assert edge_max * counts[heavy_label] >= masses[heavy_label]

                if pos[heavy_label] >= neg[heavy_label] and pos_counts[heavy_label]:
                    edge_pos = max(d for d, lab in zip(defects, labels) if lab == heavy_label)
                    assert edge_pos * pos_counts[heavy_label] >= pos[heavy_label]
                elif neg_counts[heavy_label]:
                    edge_neg = max(-d for d, lab in zip(defects, labels) if lab == heavy_label)
                    assert edge_neg * neg_counts[heavy_label] >= neg[heavy_label]
                checks += 1
    print(f"verified {checks} labeled fundamental-defect systems")


if __name__ == "__main__":
    main()
