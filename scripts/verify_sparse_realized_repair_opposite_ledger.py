#!/usr/bin/env python3
"""Finite audit for SAS5fc--SAS5fg."""

from collections import defaultdict
import random

SEED = 20260727
WORDS = tuple(range(12))


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(100000):
        n = rng.randint(4, 50)
        incidence_cap = rng.randint(1, 40)
        operation_count = rng.randint(1, 60)
        neutral_weight = rng.uniform(1.0, 1_000_000.0)
        retained_floor = neutral_weight / (
            (2 * n - 3) * (4 * incidence_cap + 1)
        )

        record_count = rng.randint(1, min(150, operation_count * 4))
        records = []
        raw = [rng.random() for _ in range(record_count)]
        scale = retained_floor * (1.0 + 4.0 * rng.random()) / sum(raw)
        for record_id, value in enumerate(raw):
            repaired = value * scale
            opposite = rng.random() * 2.0 * repaired
            word = rng.choice(WORDS)
            columns = tuple(sorted(rng.sample(range(n), 3)))
            records.append(
                (record_id, repaired, opposite, word, columns)
            )

        repaired_total = sum(record[1] for record in records)
        assert repaired_total >= retained_floor
        matched_total = sum(
            min(record[1], record[2]) for record in records
        )
        fresh_total = sum(
            max(0.0, record[1] - record[2]) for record in records
        )
        assert abs(repaired_total - (matched_total + fresh_total)) <= max(
            1e-7,
            1e-12 * repaired_total,
        )
        assert max(matched_total, fresh_total) + 1e-7 >= repaired_total / 2

        signed_before = sum(
            record[1] - record[2] for record in records
        )
        signed_after = sum(
            (record[1] - min(record[1], record[2]))
            - (record[2] - min(record[1], record[2]))
            for record in records
        )
        assert abs(signed_before - signed_after) <= max(
            1e-7,
            1e-12 * abs(signed_before),
        )

        if matched_total >= repaired_total / 2:
            assert matched_total + 1e-7 >= retained_floor / 2
            counts["matched_branches"] += 1
            counts["matched_records"] += sum(
                1
                for record in records
                if min(record[1], record[2]) > 0
            )
        else:
            assert fresh_total >= repaired_total / 2
            by_word = defaultdict(float)
            by_column = defaultdict(float)
            for _, repaired, opposite, word, _ in records:
                fresh = max(0.0, repaired - opposite)
                by_word[word] += fresh

            best_word = max(by_word, key=by_word.get)
            word_weight = by_word[best_word]
            assert word_weight * 12 + 1e-7 >= fresh_total

            for _, repaired, opposite, word, columns in records:
                if word != best_word:
                    continue
                fresh = max(0.0, repaired - opposite)
                for column in columns:
                    by_column[column] += fresh

            best_column_weight = max(by_column.values())
            assert best_column_weight * n + 1e-7 >= 3 * word_weight
            assert best_column_weight + 1e-7 >= fresh_total / (4 * n)
            assert word_weight + 1e-7 >= retained_floor / 24
            assert best_column_weight + 1e-7 >= retained_floor / (8 * n)

            counts["fresh_branches"] += 1
            counts["fresh_records"] += sum(
                1
                for record in records
                if record[1] > record[2]
            )

        counts["systems"] += 1
        counts["records"] += record_count

    print("SAS realized repair/opposite-ledger audit passed")
    keys = [
        "systems",
        "records",
        "matched_branches",
        "matched_records",
        "fresh_branches",
        "fresh_records",
    ]
    for key in keys:
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
