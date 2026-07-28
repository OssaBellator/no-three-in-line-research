#!/usr/bin/env python3
"""Verify the exact m=10 Hall phase profile by compatible-source count."""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    exp = root / "experiments"
    rows: list[dict] = []

    for name in (
        "m10-hall-support-count-profile-106-399-audit.json",
        "m10-hall-support-count-profile-400-575-audit.json",
    ):
        ledger = load(exp / name)
        columns = ledger["columns"]
        rows.extend(dict(zip(columns, packed)) for packed in ledger["parts"])

    for name in (
        "m10-weighted-hall-source-576-649-audit.json",
        "m10-weighted-hall-source-650-719-audit.json",
    ):
        ledger = load(exp / name)
        columns = ledger["columns"]
        for packed in ledger["parts"]:
            part = dict(zip(columns, packed))
            if not part["flaws"]:
                continue
            source_count = int(part["count"])
            charge = Fraction(part["charge"])
            rows.append({
                "source_cycles": source_count,
                "signed_flaws": int(part["flaws"]),
                "proper_bottlenecks": int(part["proper"]),
                "worst_charge": str(charge),
                "max_support_normalized_charge": str(source_count * charge),
            })

    full = load(exp / "m10-full-source-weighted-hall-tranche-audit.json")
    full_charge = Fraction(full["full_source_tranche_worst_charge"])
    rows.append({
        "source_cycles": 720,
        "signed_flaws": int(full["full_source_tranche_signed_flaws"]),
        "proper_bottlenecks": int(full["full_source_tranche_proper_bottlenecks"]),
        "worst_charge": str(full_charge),
        "max_support_normalized_charge": str(720 * full_charge),
    })

    rows.sort(key=lambda row: int(row["source_cycles"]))
    counts = [int(row["source_cycles"]) for row in rows]
    assert len(counts) == len(set(counts)) == 479
    assert counts[0] == 106 and counts[-1] == 720
    assert sum(int(row["signed_flaws"]) for row in rows) == 47_512
    assert all(int(row["signed_flaws"]) == int(row["proper_bottlenecks"])
               for row in rows)

    for row in rows:
        source_count = int(row["source_cycles"])
        assert Fraction(row["max_support_normalized_charge"]) == \
            source_count * Fraction(row["worst_charge"])

    below = [row for row in rows
             if Fraction(row["max_support_normalized_charge"]) < 1]
    above = [row for row in rows
             if Fraction(row["max_support_normalized_charge"]) > 1]
    assert len(below) == 55 and len(above) == 424
    assert int(above[0]["source_cycles"]) == 209
    assert Fraction(above[0]["max_support_normalized_charge"]) == Fraction(45980, 45691)
    assert int(below[-1]["source_cycles"]) == 287
    assert Fraction(below[-1]["max_support_normalized_charge"]) == Fraction(861, 1133)

    closest_below = max(below,
                        key=lambda row: Fraction(row["max_support_normalized_charge"]))
    assert int(closest_below["source_cycles"]) == 279
    assert Fraction(closest_below["max_support_normalized_charge"]) == \
        Fraction(29574, 29677)

    permanent = [row for row in rows if int(row["source_cycles"]) >= 288]
    assert len(permanent) == 411
    assert sum(int(row["signed_flaws"]) for row in permanent) == 47_076
    assert all(Fraction(row["max_support_normalized_charge"]) > 1
               for row in permanent)
    permanent_min = min(
        permanent,
        key=lambda row: Fraction(row["max_support_normalized_charge"]),
    )
    assert int(permanent_min["source_cycles"]) == 305
    assert Fraction(permanent_min["max_support_normalized_charge"]) == \
        Fraction(685640, 632751)

    maximum = max(rows,
                  key=lambda row: Fraction(row["max_support_normalized_charge"]))
    assert int(maximum["source_cycles"]) == 600
    assert Fraction(maximum["max_support_normalized_charge"]) == \
        Fraction(3152400, 791819)

    summary = load(exp / "m10-hall-support-count-phase-summary-audit.json")
    assert summary["nonempty_source_counts"] == 479
    assert summary["constant_one_first_fails_at_source_count"] == 209
    assert summary["every_nonempty_source_count_at_least_288_has_A_s_above_one"] is True
    assert summary["global_maximum"]["value"] == "3152400/791819"

    print("complete m=10 Hall support-count phase profile verified")
    print("nonempty_counts=479 flaws=47512")
    print("first_above_one=209 last_later_below_one=287")
    print("all_nonempty_counts_288_through_720_above_one=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
