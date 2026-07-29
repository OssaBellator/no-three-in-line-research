#!/usr/bin/env python3
"""Build and validate the canonical all-open T01--T43 target-completion fixture.

The fixture exercises corrected target definitions and the open completion-record schema without supplying,
claiming or simulating any proof artifact. Its mutation self-test demonstrates that missing targets, premature
proved states, nonnull open artifact fields, root drift and digest corruption are rejected. It permanently
reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Callable

import check_prime_power_canonical_frontier_roots as canonical_roots
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_canonical_raw_host_catalogue as catalogue


class AllOpenTargetFixtureError(ValueError):
    """Raised when the fixed all-open target fixture is incomplete or inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AllOpenTargetFixtureError(message)


OPEN_NOTE = "Open mathematical target; documentary all-open fixture only."


def open_completion(target_id: str) -> dict[str, Any]:
    return atomic.exact_completion(
        {
            "target_id": target_id,
            "status": "open",
            "artifact_locator": None,
            "artifact_digest": None,
            "note": OPEN_NOTE,
        },
        target_id,
    )


def exact_payload() -> dict[str, Any]:
    root_audit = canonical_roots.exact_audit()
    definition_summary = atomic.validate_definitions()
    definitions = atomic.target_definition_records()
    target_ids = list(atomic.TARGETS)
    completions = [open_completion(target_id) for target_id in target_ids]

    require(definition_summary["frontiers"] == 13, "canonical fixture requires exactly thirteen frontiers")
    require(definition_summary["targets"] == 43, "canonical fixture requires exactly forty-three targets")
    require(len(definitions) == 43, "target definition bank must contain forty-three records")
    require(len(completions) == 43, "target completion bank must contain forty-three records")
    require(
        [record["target_id"] for record in definitions] == target_ids,
        "target definition order must equal canonical target order",
    )
    require(
        [record["target_id"] for record in completions] == target_ids,
        "target completion order must equal canonical target order",
    )
    require(
        all(record["status"] == "open" for record in completions),
        "all-open fixture contains a non-open target",
    )
    require(
        all(
            record["artifact_locator"] is None and record["artifact_digest"] is None
            for record in completions
        ),
        "all-open fixture contains an artifact pointer",
    )

    claims = {
        "frontier_groups": definition_summary["frontiers"],
        "atomic_targets": definition_summary["targets"],
        "open_targets": len(completions),
        "proved_targets": 0,
        "canonical_roots_installed": root_audit["claims"]["canonical_roots_installed"],
        "canonical_target_dag_acyclic": root_audit["claims"]["canonical_target_dag_acyclic"],
        "all_open_artifact_fields_null": 1,
        "fixture_contains_mathematical_proofs": 0,
        "all_n_proved_by_checker": 0,
        "target_definitions_sha256": catalogue.canonical_digest(definitions),
        "target_completions_sha256": catalogue.canonical_digest(completions),
        "canonical_root_records_sha256": root_audit["claims"]["canonical_root_records_sha256"],
    }
    return {
        "canonical_target_definition_records": definitions,
        "all_open_target_completion_records": completions,
        "claims": claims,
    }


def build_fixture() -> dict[str, Any]:
    fixture: dict[str, Any] = {"version": 1}
    fixture.update(exact_payload())
    fixture["certificate_sha256"] = catalogue.canonical_digest(fixture)
    return fixture


def validate_fixture(fixture: Any) -> dict[str, int]:
    require(isinstance(fixture, dict), "fixture: expected object")
    require(fixture.get("version") == 1, "version: expected 1")
    exact = exact_payload()
    for key, value in exact.items():
        require(fixture.get(key) == value, f"{key}: incorrect")
    payload = {key: value for key, value in fixture.items() if key != "certificate_sha256"}
    require(
        fixture.get("certificate_sha256") == catalogue.canonical_digest(payload),
        "certificate_sha256: incorrect",
    )
    claims = exact["claims"]
    return {
        "frontiers": claims["frontier_groups"],
        "targets": claims["atomic_targets"],
        "open": claims["open_targets"],
        "proved": claims["proved_targets"],
        "all_n": 0,
    }


def rejected_mutation(
    baseline: dict[str, Any],
    mutate: Callable[[dict[str, Any]], None],
    label: str,
) -> str:
    candidate = copy.deepcopy(baseline)
    mutate(candidate)
    try:
        validate_fixture(candidate)
    except (AllOpenTargetFixtureError, atomic.AtomicFrontierExecutionError):
        return label
    raise AllOpenTargetFixtureError(f"mutation was accepted: {label}")


def mutation_self_test() -> list[str]:
    baseline = build_fixture()
    validate_fixture(baseline)
    mutations: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
        (
            "missing-target-completion",
            lambda value: value["all_open_target_completion_records"].pop(),
        ),
        (
            "premature-proved-status",
            lambda value: value["all_open_target_completion_records"][0].__setitem__("status", "proved"),
        ),
        (
            "nonnull-open-artifact-locator",
            lambda value: value["all_open_target_completion_records"][0].__setitem__(
                "artifact_locator", "fixture://forbidden"
            ),
        ),
        (
            "missing-target-definition",
            lambda value: value["canonical_target_definition_records"].pop(),
        ),
        (
            "canonical-root-digest-drift",
            lambda value: value["claims"].__setitem__("canonical_root_records_sha256", "0" * 64),
        ),
        (
            "honesty-claim-flip",
            lambda value: value["claims"].__setitem__("all_n_proved_by_checker", 1),
        ),
        (
            "certificate-digest-corruption",
            lambda value: value.__setitem__("certificate_sha256", "f" * 64),
        ),
    )
    return [rejected_mutation(baseline, mutate, label) for label, mutate in mutations]


def main() -> None:
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        rejected = mutation_self_test()
        summary = validate_fixture(build_fixture())
        print({**summary, "rejected_mutations": len(rejected), "mutation_ids": rejected})
        return
    if len(sys.argv) == 3 and sys.argv[1] == "--write":
        path = Path(sys.argv[2])
        path.write_text(json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(path)
        return
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_all_open_target_fixture.py "
            "--self-test | --write fixture.json | fixture.json"
        )
    fixture = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_fixture(fixture))


if __name__ == "__main__":
    main()
