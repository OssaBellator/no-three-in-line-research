#!/usr/bin/env python3
"""Check the rank-three middle-path paid choice-grid reduction."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


Pair = tuple[int, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def require_fraction(value: Any, label: str) -> Fraction:
    if isinstance(value, int) and not isinstance(value, bool):
        return Fraction(value, 1)
    if not isinstance(value, str):
        raise ValueError(f"{label}: expected integer or rational string")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"{label}: invalid rational") from exc


def parse_vertex_list(raw: Any, label: str) -> list[int]:
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected list")
    result: list[int] = []
    seen: set[int] = set()
    for pos, value in enumerate(raw):
        value = require_int(value, f"{label}[{pos}]")
        if value in seen:
            raise ValueError(f"{label}: duplicate value {value}")
        seen.add(value)
        result.append(value)
    if not result:
        raise ValueError(f"{label}: must be nonempty")
    return result


def parse_pairs(raw: Any, label: str, p_set: set[int], s_set: set[int]) -> set[Pair]:
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected list")
    result: set[Pair] = set()
    for pos, item in enumerate(raw):
        if not isinstance(item, list) or len(item) != 2:
            raise ValueError(f"{label}[{pos}]: expected [p,s]")
        p = require_int(item[0], f"{label}[{pos}][0]")
        s = require_int(item[1], f"{label}[{pos}][1]")
        if p not in p_set or s not in s_set:
            raise ValueError(f"{label}[{pos}]: pair outside P x S")
        pair = (p, s)
        if pair in result:
            raise ValueError(f"{label}: duplicate pair {pair}")
        result.add(pair)
    return result


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        p_values = parse_vertex_list(payload.get("P"), "P")
        s_values = parse_vertex_list(payload.get("S"), "S")
        p_set, s_set = set(p_values), set(s_values)
        invalid = parse_pairs(
            payload.get("middle_source_invalid", []),
            "middle_source_invalid",
            p_set,
            s_set,
        )
        omega = require_int(payload.get("omega"), "omega", minimum=1)
        removal_credit = require_fraction(payload.get("removal_credit"), "removal_credit")
        residual_source_average = require_fraction(
            payload.get("residual_source_average", 0),
            "residual_source_average",
        )
        residual_paid_average = require_fraction(
            payload.get("residual_paid_average", 0),
            "residual_paid_average",
        )

        raw_weights = payload.get("weights")
        if not isinstance(raw_weights, list):
            raise ValueError("weights: expected list")
        weights: dict[Pair, int] = {}
        for pos, item in enumerate(raw_weights):
            if not isinstance(item, list) or len(item) != 3:
                raise ValueError(f"weights[{pos}]: expected [p,s,weight]")
            p = require_int(item[0], f"weights[{pos}][0]")
            s = require_int(item[1], f"weights[{pos}][1]")
            weight = require_int(item[2], f"weights[{pos}][2]", minimum=1)
            if p not in p_set or s not in s_set:
                raise ValueError(f"weights[{pos}]: pair outside P x S")
            pair = (p, s)
            if pair in weights:
                raise ValueError(f"weights: duplicate pair {pair}")
            weights[pair] = weight

        raw_candidates = payload.get("candidate_states", {})
        if not isinstance(raw_candidates, dict):
            raise ValueError("candidate_states: expected object")
        candidate_states: dict[str, set[Pair]] = {}
        for candidate, raw_pairs in raw_candidates.items():
            if not isinstance(candidate, str) or not candidate:
                raise ValueError("candidate_states: candidate keys must be nonempty strings")
            candidate_states[candidate] = parse_pairs(
                raw_pairs, f"candidate_states[{candidate!r}]", p_set, s_set
            )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    product = len(p_values) * len(s_values)
    diagonal = {(p, s) for p in p_set for s in s_set if p == s}
    deleted = invalid | diagonal
    valid = {
        (p, s)
        for p in p_set
        for s in s_set
        if (p, s) not in deleted
    }
    d_c = len(invalid) + min(len(p_values), len(s_values))
    small_product = product <= omega * d_c if d_c else False

    result: dict[str, Any] = {
        "P_size": len(p_values),
        "S_size": len(s_values),
        "product": product,
        "omega": omega,
        "D_c_upper_bound": d_c,
        "valid_state_count": len(valid),
        "valid_fraction": str(Fraction(len(valid), product)),
    }

    if small_product:
        result.update({
            "outcome": "small_outer_core",
            "smaller_side": min(len(p_values), len(s_values)),
        })
        print(json.dumps(result, indent=2, sort_keys=True))
        return

    missing_weights = sorted(valid - weights.keys())
    extra_weights = sorted(weights.keys() - valid)
    if missing_weights or extra_weights:
        raise SystemExit(
            "check failed: weights must be specified exactly on valid states; "
            f"missing={missing_weights}, extra={extra_weights}"
        )

    total_weight = sum(weights.values())
    average_weight = Fraction(total_weight, len(valid))
    normalized_objective = (
        residual_source_average
        + (average_weight + residual_paid_average) / removal_credit
    )
    result.update({
        "total_middle_weight": total_weight,
        "average_middle_weight": str(average_weight),
        "removal_credit": str(removal_credit),
        "residual_source_average": str(residual_source_average),
        "residual_paid_average": str(residual_paid_average),
        "normalized_paid_objective": str(normalized_objective),
    })

    if normalized_objective < 1:
        result["outcome"] = "paid_average_completion"
        print(json.dumps(result, indent=2, sort_keys=True))
        return

    covered_occurrences: dict[Pair, int] = {pair: 0 for pair in valid}
    for candidate, pairs in candidate_states.items():
        left_seen: set[int] = set()
        right_seen: set[int] = set()
        for p, s in pairs:
            if (p, s) not in valid:
                raise SystemExit(
                    f"check failed: candidate {candidate!r} uses invalid state {(p, s)}"
                )
            if p in left_seen or s in right_seen:
                raise SystemExit(
                    f"check failed: candidate {candidate!r} does not colour a matching"
                )
            left_seen.add(p)
            right_seen.add(s)
            covered_occurrences[(p, s)] += 1

    if candidate_states:
        for pair, weight in weights.items():
            if covered_occurrences[pair] != weight:
                raise SystemExit(
                    "check failed: candidate incidence count does not equal weight "
                    f"at {pair}: {covered_occurrences[pair]} != {weight}"
                )
        lower_bound = Fraction(total_weight, min(len(p_values), len(s_values)))
        if len(candidate_states) < lower_bound:
            raise SystemExit("check failed: candidate-cover lower bound violated")
        result["candidate_count"] = len(candidate_states)
        result["candidate_cover_lower_bound"] = str(lower_bound)

    result["outcome"] = "weighted_grid_or_projective_cover"
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
