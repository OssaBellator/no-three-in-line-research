#!/usr/bin/env python3
"""Verify the exact Hall-subset scale profile of transition-window count maxima."""
from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

WINDOW = range(209, 288)
EXPECTED_VIOLATING = {
    209: (29, "45980/45691", 3520, 731056),
    215: (3, "3440/3321", 384, 79704),
    227: (27, "41768/39613", 2944, 633808),
    234: (2, "234/193", 256, 49408),
    248: (2, "1984/1563", 256, 50016),
    272: (3, "3264/2893", 384, 92576),
    276: (85, "14076/11845", 9792, 2274240),
    278: (124, "51152/38383", 13248, 2763576),
    280: (2, "4480/3781", 256, 60496),
    281: (6, "6744/6383", 384, 102128),
    282: (3, "564/445", 384, 85440),
    284: (1, "4544/4315", 128, 34520),
    286: (4, "2288/1957", 512, 125248),
}
EXPECTED_HIST = {
    1: (11, 1), 2: (7, 3), 3: (5, 3), 4: (3, 1), 5: (1, 0),
    6: (2, 1), 7: (1, 0), 8: (1, 0), 11: (1, 0), 13: (2, 0),
    14: (1, 0), 17: (1, 0), 27: (2, 1), 29: (1, 1), 40: (1, 0),
    49: (1, 0), 85: (1, 1), 124: (1, 1),
}


def load_rows(root: Path) -> list[dict]:
    source = json.loads(
        (root / "experiments/m10-hall-support-count-profile-106-399-audit.json").read_text()
    )
    columns = source["columns"]
    rows = [dict(zip(columns, row)) for row in source["parts"]]
    selected = [row for row in rows if row["source_cycles"] in WINDOW]
    assert len(selected) == 43
    return selected


def verify(root: Path) -> None:
    rows = load_rows(root)
    summary = json.loads(
        (root / "experiments/m10-hall-transition-count-maximizer-subset-scale-audit.json").read_text()
    )

    violations = [
        row for row in rows if Fraction(row["max_support_normalized_charge"]) > 1
    ]
    assert len(violations) == 13
    observed = {
        row["source_cycles"]: (
            row["worst_subset_size"],
            row["max_support_normalized_charge"],
            row["worst_supply"],
            row["worst_capacity"],
        )
        for row in violations
    }
    assert observed == EXPECTED_VIOLATING

    total = Counter(row["worst_subset_size"] for row in rows)
    bad = Counter(row["worst_subset_size"] for row in violations)
    assert {k: (total[k], bad[k]) for k in sorted(total)} == EXPECTED_HIST

    assert sum(row["worst_subset_size"] <= 3 for row in violations) == 7
    assert sum(row["worst_subset_size"] <= 6 for row in violations) == 9
    assert max(
        (Fraction(row["worst_subset_size"], row["source_cycles"]), row["source_cycles"])
        for row in violations
    ) == (Fraction(62, 139), 278)
    assert not any(7 <= row["worst_subset_size"] <= 26 for row in violations)
    assert not any(30 <= row["worst_subset_size"] <= 84 for row in violations)

    hist = {
        row["hall_subset_size"]: (
            row["count_maxima"], row["constant_one_violations"]
        )
        for row in summary["exact_subset_size_histogram"]
    }
    assert hist == EXPECTED_HIST
    assert summary["violating_count_maxima_with_subset_size_at_most_3"] == 7
    assert summary["violating_count_maxima_with_subset_size_at_most_6"] == 9
    assert Fraction(
        summary["largest_subset_fraction_among_violating_count_maxima"]["value"]
    ) == Fraction(62, 139)
    assert summary["violating_subset_sizes"] == [1, 2, 3, 4, 6, 27, 29, 85, 124]
    assert not summary["subset_size_alone_characterizes_violation"]
    assert not summary["asymptotic_subset_scale_theorem_proved"]
    assert summary["all_exact_regressions_verified"]


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()
    verify(args.root.resolve())
    print("m10 Hall transition count-maximizer subset scale verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
