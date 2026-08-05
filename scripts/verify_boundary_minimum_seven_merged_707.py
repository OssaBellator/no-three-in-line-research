#!/usr/bin/env python3
"""Audit a complete merged minimum-seven census and compute next spectra.

This verifier consumes the JSON produced by
``merge_boundary_minimum_seven_attempt_shards_707.py``. It does not rerun the
expensive exact-cover census. Instead it reconstructs every raw attempt from the
certified twenty-one-block state, independently audits each emitted witness, and
computes the exact raw twenty-third spectrum for every repaired state.

The output is finite comparative evidence only. It neither selects a canonical
continuation nor proves recurrence or the all-n theorem.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import runpy
import tempfile

HERE = Path(__file__).resolve().parent


def cross(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def audit_repaired_state(
    all_points: list[tuple[int, int]],
    core: tuple[tuple[int, int], ...],
    deleted_raw: list[list[int]],
    added_raw: list[list[int]],
) -> list[tuple[int, int]]:
    deleted = {tuple(point) for point in deleted_raw}
    added = {tuple(point) for point in added_raw}
    base = set(all_points)

    assert len(core) == 7
    assert deleted == set(core)
    assert len(deleted) == len(added) == 7
    assert deleted <= base
    assert Counter(x for x, _ in deleted) == Counter(x for x, _ in added)
    assert Counter(y for _, y in deleted) == Counter(y for _, y in added)

    repaired = (base - deleted) | added
    assert len(repaired) == len(base) == 176
    assert repaired != base
    ordered = sorted(repaired)
    for a, b, c in combinations(ordered, 3):
        assert cross(a, b, c) != 0, (a, b, c)
    return ordered


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("merged", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    merged = json.loads(args.merged.read_text())
    assert merged["frontier"] == "twenty-second raw minimum-seven layer"
    assert merged["attempts"] == 205
    assert merged["budget"] == 7
    assert merged["status"] == "passed"

    records = merged["records"]
    keys = [(record["attempt_index"], record["core_index"]) for record in records]
    assert keys == sorted(keys)
    assert len(keys) == len(set(keys)) == merged["minimum_cores"]
    assert sum(bool(record["repair_found"]) for record in records) == merged["repairs"]

    context = runpy.run_path(str(HERE / "check_boundary_continuation_694.py"))
    state21 = context["state21"]
    block = context["block"]
    compile_kernel = context["compile"]
    spectrum = context["spectrum"]
    attempts = [attempt for attempt in context["s22"][2] if attempt[3] == 7]
    assert len(attempts) == 205

    witnesses = []
    for record in records:
        attempt_index = record["attempt_index"]
        core_index = record["core_index"]
        name, offset, _triples, minimum, cores = attempts[attempt_index]
        assert minimum == 7
        assert name == record["attempt_name"]
        assert offset == record["offset"]
        core = cores[core_index]
        all_points = sorted(state21 | block(name, 84, offset))

        if record["repair_found"]:
            assert record["deleted"] is not None
            assert record["added"] is not None
            repaired = audit_repaired_state(
                all_points,
                core,
                record["deleted"],
                record["added"],
            )
            witnesses.append({
                "attempt_index": attempt_index,
                "core_index": core_index,
                "attempt_name": name,
                "offset": offset,
                "deleted": record["deleted"],
                "added": record["added"],
                "repaired_state": repaired,
                "exact_cover_subsets_tested_until_stop": record[
                    "exact_cover_subsets_tested_until_stop"
                ],
                "exact_cover_nodes_tested_until_stop": record[
                    "exact_cover_nodes_tested_until_stop"
                ],
            })
        else:
            assert record["deleted"] is None
            assert record["added"] is None

    jobs = [
        (f"w{index}", witness["repaired_state"], 88, 6)
        for index, witness in enumerate(witnesses)
    ]
    with tempfile.TemporaryDirectory() as directory:
        binary = compile_kernel("boundary_spectrum_kernel.cpp", Path(directory))
        spectra = spectrum(binary, jobs) if jobs else {}

    for index, witness in enumerate(witnesses):
        histogram, minimum, next_attempts = spectra[f"w{index}"]
        assert minimum == min(histogram)
        assert sum(histogram.values()) == len(next_attempts)
        witness["raw_twenty_third_histogram"] = {
            str(key): histogram[key] for key in sorted(histogram)
        }
        witness["raw_twenty_third_minimum"] = minimum
        witness["raw_twenty_third_minimum_attempts"] = sum(
            attempt[3] == minimum for attempt in next_attempts
        )
        witness["raw_twenty_third_minimum_cores"] = sum(
            len(attempt[4]) for attempt in next_attempts if attempt[3] == minimum
        )

    output = {
        "frontier": merged["frontier"],
        "attempts": 205,
        "minimum_cores": merged["minimum_cores"],
        "budget": 7,
        "exact_cover_subsets_tested_until_stop": merged[
            "exact_cover_subsets_tested_until_stop"
        ],
        "exact_cover_nodes_tested_until_stop": merged[
            "exact_cover_nodes_tested_until_stop"
        ],
        "repairs": len(witnesses),
        "audited_witnesses": len(witnesses),
        "witnesses": witnesses,
        "evidence_level": "exact_finite_minimum_seven_budget_seven_verified_census",
        "status": "passed",
        "warning": (
            "This verifies complete finite census coverage and all positive "
            "witnesses. It does not select a canonical continuation or establish "
            "recurrence or the all-n theorem."
        ),
    }
    rendered = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
