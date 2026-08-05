#!/usr/bin/env python3
"""Compute exact raw twenty-third spectra for audited budget-seven repairs.

Input is the witness payload produced by
``check_boundary_twentysecond_budget_seven_witnesses_701.py``. Every repaired
state is re-audited, passed to the canonical spectrum kernel at the next block
origin, and ranked by explicit low-frontier statistics.

The output is comparative finite evidence only. It deliberately does not choose
or promote a canonical continuation state: ties and trade-offs are retained, and
a later theorem chapter must state and justify any selection rule.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import runpy
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent


def cross(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def audit_state(points: list[list[int]] | list[tuple[int, int]]) -> list[tuple[int, int]]:
    state = [tuple(point) for point in points]
    assert len(state) == 176
    assert len(set(state)) == 176
    ordered = sorted(state)
    for a, b, c in combinations(ordered, 3):
        assert cross(a, b, c) != 0, (a, b, c)
    return ordered


def low_vector(histogram: dict[int, int]) -> tuple[int, ...]:
    """A transparent comparison vector, not an automatic selection theorem.

    Prefer a larger raw minimum; then fewer attempts at each transversal size
    from that minimum upward. Negating the minimum lets ordinary ascending tuple
    order express that convention.
    """
    minimum = min(histogram)
    return (-minimum,) + tuple(histogram.get(k, 0) for k in range(minimum, 15))


def dominates(left: dict[int, int], right: dict[int, int]) -> bool:
    """Return whether left is no worse at every cumulative low threshold.

    Missing sizes count as zero. Thresholds six through fourteen are retained so
    that different minima can be compared without silently discarding mass.
    """
    left_cumulative = []
    right_cumulative = []
    lsum = rsum = 0
    for threshold in range(6, 15):
        lsum += left.get(threshold, 0)
        rsum += right.get(threshold, 0)
        left_cumulative.append(lsum)
        right_cumulative.append(rsum)
    return all(a <= b for a, b in zip(left_cumulative, right_cumulative)) and any(
        a < b for a, b in zip(left_cumulative, right_cumulative)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("witnesses", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = json.loads(args.witnesses.read_text())
    assert payload["frontier"] == "twenty-second"
    assert payload["budget"] == 7
    assert payload["status"] == "passed"
    assert payload["legacy_positive_jobs"] == payload["audited_witnesses"]
    witnesses = payload["witnesses"]
    assert len({w["global_index"] for w in witnesses}) == len(witnesses)

    context = runpy.run_path(str(HERE / "check_boundary_continuation_694.py"))
    compile_kernel = context["compile"]
    spectrum = context["spectrum"]

    jobs = []
    states = {}
    for witness in witnesses:
        state = audit_state(witness["repaired_state"])
        label = f"g{witness['global_index']}"
        jobs.append((label, state, 88, 6))
        states[label] = state

    with tempfile.TemporaryDirectory() as directory:
        binary = compile_kernel("boundary_spectrum_kernel.cpp", Path(directory))
        spectra = spectrum(binary, jobs) if jobs else {}

    records = []
    for witness in witnesses:
        label = f"g{witness['global_index']}"
        histogram, best, attempts = spectra[label]
        assert best == min(histogram)
        assert sum(histogram.values()) == len(attempts)
        minimum_attempts = [attempt for attempt in attempts if attempt[3] == best]
        minimum_cores = sum(len(attempt[4]) for attempt in minimum_attempts)
        histogram_json = {str(k): histogram[k] for k in sorted(histogram)}
        records.append({
            "global_index": witness["global_index"],
            "attempt_index": witness["attempt_index"],
            "core_index": witness["core_index"],
            "attempt_name": witness["attempt_name"],
            "offset": witness["offset"],
            "raw_twenty_third_histogram": histogram_json,
            "raw_minimum": best,
            "raw_minimum_attempts": len(minimum_attempts),
            "raw_minimum_cores": minimum_cores,
            "cumulative_at_most_6": sum(v for k, v in histogram.items() if k <= 6),
            "cumulative_at_most_7": sum(v for k, v in histogram.items() if k <= 7),
            "cumulative_at_most_8": sum(v for k, v in histogram.items() if k <= 8),
            "comparison_vector": list(low_vector(histogram)),
        })

    records.sort(key=lambda record: (tuple(record["comparison_vector"]), record["global_index"]))
    for rank, record in enumerate(records, start=1):
        record["lexicographic_low_frontier_rank"] = rank

    histograms = {
        record["global_index"]: {
            int(k): v for k, v in record["raw_twenty_third_histogram"].items()
        }
        for record in records
    }
    pareto = []
    for record in records:
        index = record["global_index"]
        if not any(
            other != index and dominates(histograms[other], histograms[index])
            for other in histograms
        ):
            pareto.append(index)

    summary = Counter(record["raw_minimum"] for record in records)
    output = {
        "source_frontier": "twenty-second",
        "source_budget": 7,
        "evaluated_repaired_states": len(records),
        "next_frontier": "twenty-third",
        "next_block_origin": 88,
        "spectrum_limit": 6,
        "raw_minimum_histogram": {str(k): summary[k] for k in sorted(summary)},
        "pareto_indices_by_cumulative_low_frontier": sorted(pareto),
        "records": records,
        "status": "passed",
        "warning": (
            "Ranks are descriptive finite comparisons, not a canonical-state "
            "selection theorem and not evidence of recurrence or an all-n proof."
        ),
    }
    rendered = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
