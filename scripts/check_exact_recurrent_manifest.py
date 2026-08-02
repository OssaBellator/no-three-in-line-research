#!/usr/bin/env python3
"""Validate exact recurrent-state Lyapunov manifests.

This checker verifies a finite declared offspring matrix and an exact positive
rational strict supersolution. It deliberately does not infer that the declared
state set or coefficients are complete for no-three-in-line repair dynamics.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


class ManifestError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ManifestError(message)


def parse_fraction(value: Any, context: str) -> Fraction:
    require(isinstance(value, str), f"{context}: expected rational string")
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ManifestError(f"{context}: invalid rational {value!r}") from exc
    return result


def validate_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    require(manifest.get("schema") == "exact-recurrent-lyapunov/v1", "schema mismatch")
    states = manifest.get("states")
    require(isinstance(states, list) and states, "states must be a nonempty list")

    state_ids: list[str] = []
    weights: dict[str, Fraction] = {}
    for index, state in enumerate(states):
        require(isinstance(state, dict), f"states[{index}]: expected object")
        state_id = state.get("id")
        require(isinstance(state_id, str) and state_id, f"states[{index}].id invalid")
        require(state_id not in weights, f"duplicate state id {state_id}")
        weight = parse_fraction(state.get("weight"), f"state {state_id} weight")
        require(weight > 0, f"state {state_id}: weight must be positive")
        state_ids.append(state_id)
        weights[state_id] = weight

    declared_complete = manifest.get("declared_state_set_complete")
    require(isinstance(declared_complete, bool), "declared_state_set_complete must be boolean")
    coefficient_provenance_complete = manifest.get("coefficient_provenance_complete")
    require(
        isinstance(coefficient_provenance_complete, bool),
        "coefficient_provenance_complete must be boolean",
    )

    rows = manifest.get("rows")
    require(isinstance(rows, list), "rows must be a list")
    require(len(rows) == len(states), "exactly one row is required per state")

    seen_rows: set[str] = set()
    minimum_slack: Fraction | None = None
    total_nonzero = 0
    normalized_rows: dict[str, dict[str, str]] = {}

    for index, row in enumerate(rows):
        require(isinstance(row, dict), f"rows[{index}]: expected object")
        parent = row.get("parent")
        require(parent in weights, f"rows[{index}]: unknown parent {parent!r}")
        require(parent not in seen_rows, f"duplicate row for parent {parent}")
        seen_rows.add(parent)

        coefficients = row.get("offspring")
        require(isinstance(coefficients, dict), f"row {parent}: offspring must be object")
        unknown = sorted(set(coefficients) - set(weights))
        require(not unknown, f"row {parent}: unknown children {unknown}")

        lhs = Fraction(0)
        normalized: dict[str, str] = {}
        for child in state_ids:
            coefficient = parse_fraction(
                coefficients.get(child, "0"),
                f"row {parent} child {child}",
            )
            require(
                coefficient >= 0,
                f"row {parent} child {child}: coefficient must be nonnegative",
            )
            if coefficient:
                total_nonzero += 1
                normalized[child] = str(coefficient)
            lhs += coefficient * weights[child]

        explicit_slack = parse_fraction(row.get("slack"), f"row {parent} slack")
        require(explicit_slack > 0, f"row {parent}: slack must be positive")
        actual_slack = weights[parent] - lhs
        require(
            actual_slack == explicit_slack,
            f"row {parent}: declared slack {explicit_slack} != exact slack {actual_slack}",
        )
        require(actual_slack > 0, f"row {parent}: row is not strictly subcritical")

        minimum_slack = (
            actual_slack if minimum_slack is None else min(minimum_slack, actual_slack)
        )
        normalized_rows[parent] = normalized

    missing_rows = sorted(set(weights) - seen_rows)
    require(not missing_rows, f"missing rows for {missing_rows}")

    proof_eligible = declared_complete and coefficient_provenance_complete
    return {
        "state_count": len(states),
        "row_count": len(rows),
        "nonzero_coefficient_count": total_nonzero,
        "minimum_exact_slack": str(minimum_slack),
        "strict_lyapunov_certificate_valid": 1,
        "declared_state_set_complete": int(declared_complete),
        "coefficient_provenance_complete": int(coefficient_provenance_complete),
        "proof_eligible_under_manifest_declarations": int(proof_eligible),
        "all_n_proved_by_checker": 0,
        "normalized_rows": normalized_rows,
    }


def built_in_manifest() -> dict[str, Any]:
    return {
        "schema": "exact-recurrent-lyapunov/v1",
        "research_status": "toy certificate only",
        "declared_state_set_complete": False,
        "coefficient_provenance_complete": False,
        "states": [
            {"id": "diffuse", "weight": "5"},
            {"id": "concentrated", "weight": "8"},
        ],
        "rows": [
            {
                "parent": "diffuse",
                "offspring": {"diffuse": "1/5", "concentrated": "1/4"},
                "slack": "2",
            },
            {
                "parent": "concentrated",
                "offspring": {"diffuse": "1/2", "concentrated": "1/2"},
                "slack": "3/2",
            },
        ],
    }


def mutation_audit() -> int:
    base = built_in_manifest()
    mutations = [
        lambda value: value.update(schema="wrong"),
        lambda value: value["states"].append(copy.deepcopy(value["states"][0])),
        lambda value: value["rows"].pop(),
        lambda value: value["rows"][0]["offspring"].update(unknown="1"),
        lambda value: value["rows"][0]["offspring"].update(diffuse="-1"),
        lambda value: value["rows"][0].update(slack="1"),
        lambda value: value["states"][0].update(weight="0"),
        lambda value: value["rows"][1]["offspring"].update(concentrated="1"),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(base)
        mutate(candidate)
        try:
            validate_manifest(candidate)
        except ManifestError:
            rejected += 1
    require(rejected == len(mutations), "mutation audit accepted an invalid manifest")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", nargs="?", help="JSON manifest path")
    args = parser.parse_args()

    try:
        if args.manifest:
            path = Path(args.manifest)
            require(path.is_file(), f"manifest not found: {path}")
            manifest = json.loads(path.read_text(encoding="utf-8"))
            require(isinstance(manifest, dict), "manifest root must be an object")
        else:
            manifest = built_in_manifest()
        report = validate_manifest(manifest)
        report["rejected_corruptions"] = mutation_audit()
        print(json.dumps(report, sort_keys=True))
    except (ManifestError, json.JSONDecodeError) as exc:
        print(f"invalid exact recurrent manifest: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
