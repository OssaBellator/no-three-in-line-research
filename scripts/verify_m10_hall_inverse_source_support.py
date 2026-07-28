#!/usr/bin/env python3
"""Verify the inverse-compatible-source envelope for the complete m=10 Hall audit."""
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
    low = load(exp / "m10-weighted-hall-low-source-bands-audit.json")
    mid = load(exp / "m10-weighted-hall-mid-source-400-575-audit.json")
    hi1 = load(exp / "m10-weighted-hall-source-576-649-audit.json")
    hi2 = load(exp / "m10-weighted-hall-source-650-719-audit.json")
    full = load(exp / "m10-full-source-weighted-hall-tranche-audit.json")
    complete = load(exp / "m10-weighted-hall-complete-audit.json")

    rows: list[tuple[int, int, Fraction, int]] = []
    # A band maximum at upper endpoint h proves gamma(F) < 4/s(F) throughout
    # the band whenever h * gamma_band < 4, since s(F) <= h.
    for band in low["bands"]:
        lo, hi = band["source_cycle_band"]
        rows.append((lo, hi, Fraction(band["source_band_worst_charge"]),
                     band["source_band_signed_flaws"]))
    for band in mid["partitions"]:
        lo, hi = band["source_cycle_band"]
        rows.append((lo, hi, Fraction(band["worst_charge"]),
                     band["signed_flaws"]))
    for ledger in (hi1, hi2):
        columns = ledger["columns"]
        for packed in ledger["parts"]:
            part = dict(zip(columns, packed))
            if part["flaws"]:
                source_count = int(part["count"])
                rows.append((source_count, source_count, Fraction(part["charge"]),
                             int(part["flaws"])))
    rows.append((720, 720, Fraction(full["full_source_tranche_worst_charge"]),
                 int(full["full_source_tranche_signed_flaws"])))

    assert sum(row[3] for row in rows) == 47_512
    assert complete["exact_mincuts_completed"] == 47_512
    assert complete["all_47512_weighted_hall_mincuts_completed"] is True

    witnesses = []
    for lo, hi, charge, flaws in rows:
        product = hi * charge
        assert product < 4
        witnesses.append((product, lo, hi, charge, flaws))

    product, lo, hi, charge, flaws = max(witnesses)
    assert lo == hi == 600
    assert charge == Fraction(5254, 791819)
    assert product == Fraction(3152400, 791819)
    assert Fraction(4) - product == Fraction(14876, 791819)

    print("complete m=10 inverse-source Hall envelope verified")
    print(f"rows={len(rows)} flaws={sum(row[3] for row in rows)}")
    print(f"max_s_gamma={product} source_count={hi}")
    print(f"margin_below_4={Fraction(4)-product}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
