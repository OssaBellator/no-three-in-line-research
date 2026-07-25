#!/usr/bin/env python3
"""Check random thinning of credited-line self-recapture traces."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path


def falling(n: int, k: int) -> int:
    out = 1
    for t in range(k):
        out *= n - t
    return out


def derangements(items: tuple[int, ...]):
    for perm in itertools.permutations(items):
        if all(perm[i] != items[i] for i in range(len(items))):
            yield dict(zip(items, perm))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("instance", type=Path)
    args = parser.parse_args()
    data = json.loads(args.instance.read_text(encoding="utf-8"))

    Q = int(data["bank_size"])
    q = int(data["subbank_size"])
    traces_raw = data["traces"]
    if not 3 <= q <= Q:
        raise ValueError("require 3 <= subbank_size <= bank_size")
    if len(traces_raw) != Q:
        raise ValueError("one trace is required for every credit line")

    traces: list[set[tuple[int, int]]] = []
    offdiag_count = 0
    for i, raw in enumerate(traces_raw):
        trace = {tuple(map(int, cell)) for cell in raw}
        if (i, i) not in trace:
            raise AssertionError(f"trace {i} misses its current diagonal")
        rows = [a for a, _ in trace]
        cols = [b for _, b in trace]
        if len(rows) != len(set(rows)) or len(cols) != len(set(cols)):
            raise AssertionError(f"trace {i} is not a matching")
        for k, l in trace:
            if not (0 <= k < Q and 0 <= l < Q):
                raise ValueError("trace index out of range")
            if (k, l) != (i, i):
                if k == l or k == i or l == i:
                    raise AssertionError(
                        f"trace {i} violates unique-current/resource exclusion"
                    )
                offdiag_count += 1
        traces.append(trace)

    subsets = list(itertools.combinations(range(Q), q))
    self_counts: list[int] = []
    derangement_counts: list[float] = []
    zero_subbanks = 0

    for subset in subsets:
        I = set(subset)
        z = 0
        for i in subset:
            z += sum(
                1
                for k, l in traces[i]
                if (k, l) != (i, i) and k in I and l in I
            )
        self_counts.append(z)
        if z == 0:
            zero_subbanks += 1

        ds = list(derangements(subset))
        if not ds:
            raise AssertionError("no derangements")
        total_recreated = 0
        for sigma in ds:
            recreated = 0
            for i in subset:
                for k in subset:
                    if (k, sigma[k]) in traces[i]:
                        recreated += 1
            total_recreated += recreated
        derangement_counts.append(total_recreated / len(ds))

    exact_subset_average = sum(self_counts) / len(self_counts)
    expected_formula = offdiag_count * falling(q, 3) / falling(Q, 3)
    if not math.isclose(
        exact_subset_average,
        expected_formula,
        rel_tol=1e-12,
        abs_tol=1e-12,
    ):
        raise AssertionError("triple-selection expectation mismatch")

    exact_joint_average = sum(derangement_counts) / len(derangement_counts)
    expected_joint_formula = expected_formula / (q - 1)
    if not math.isclose(
        exact_joint_average,
        expected_joint_formula,
        rel_tol=1e-12,
        abs_tol=1e-12,
    ):
        raise AssertionError("joint derangement expectation mismatch")

    zero_verified = True
    for subset, z in zip(subsets, self_counts):
        if z != 0:
            continue
        I = tuple(subset)
        for sigma in derangements(I):
            for i in I:
                for k in I:
                    if (k, sigma[k]) in traces[i]:
                        zero_verified = False
    if not zero_verified:
        raise AssertionError("zero-self subbank recreated a selected credit")

    result = {
        "bank_size": Q,
        "subbank_size": q,
        "offdiagonal_trace_entries": offdiag_count,
        "subbank_count": len(subsets),
        "average_self_trace_entries": exact_subset_average,
        "triple_selection_formula": expected_formula,
        "average_recreated_credits": exact_joint_average,
        "joint_formula": expected_joint_formula,
        "zero_self_subbanks": zero_subbanks,
        "zero_self_derangement_verified": zero_verified,
        "asymptotic_bound_q_cubed_over_Q": q**3 / Q,
        "outcome": (
            "zero_self_recapture_subbank"
            if zero_subbanks
            else "finite_no_zero_subbank"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
