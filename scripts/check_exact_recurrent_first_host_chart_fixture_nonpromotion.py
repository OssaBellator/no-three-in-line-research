#!/usr/bin/env python3
"""Prove installed grid fixtures do not establish a physical chart invariant."""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any

HOST_ID = "s4-75b04c45c1c8eac2"
DOC_ORBIT = "docs/325-prime-power-geometric-orbit-fibre-correction.md"
DOC_HOST = "docs/328-prime-power-geometric-fibre-host-census-and-line-caps.md"
HOST_VERIFIER = "scripts/verify_prime_power_geometric_fibre_host_census.py"
CAPACITY_VERIFIER = "scripts/verify_prime_power_line_occupancy_capacity.py"
ANCESTRY_CHECKER = "scripts/check_prime_power_geometric_fibre_outer_assignment_ancestry.py"
STATUS_PATH = "STATUS.md"


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise AuditError("unable to locate repository root")


def read(root: Path, relative: str) -> str:
    path = root / relative
    require(path.is_file(), f"missing source: {relative}")
    return path.read_text(encoding="utf-8")


def expected_manifest() -> dict[str, Any]:
    return {
        "schema": "exact-recurrent-first-host-chart-fixture-nonpromotion/v1",
        "scope": {
            "host_id": HOST_ID,
            "question": "whether installed standard-grid background fixtures prove physical chart confinement or response disjointness",
        },
        "source_bindings": [
            {
                "path": DOC_ORBIT,
                "fact": "standard-grid coordinates define the response-host geometric fibre and its line-incidence signature",
            },
            {
                "path": DOC_HOST,
                "fact": "background B is an independent fixed set and actual background/provenance attachment remains open",
            },
            {
                "path": HOST_VERIFIER,
                "fact": "test backgrounds are random samples from grid minus the current response",
            },
            {
                "path": CAPACITY_VERIFIER,
                "fact": "test backgrounds are again random samples from grid minus the current response",
            },
            {
                "path": ANCESTRY_CHECKER,
                "fact": "geometric fibre rows complete for all provenance remains zero",
            },
            {
                "path": STATUS_PATH,
                "fact": "raw fibre backgrounds covering all provenance remains zero",
            },
        ],
        "distinctions": {
            "coordinate_labelled_response_hosts_on_standard_grid": 1,
            "synthetic_grid_minus_response_background_fixtures_present": 1,
            "background_is_independent_input_in_source_theorem": 1,
            "source_chapter_explicitly_leaves_actual_background_attachment_open": 1,
            "physical_chart_confinement_invariant_installed": 0,
            "physical_response_disjointness_invariant_installed": 0,
        },
        "aggregate": {
            "source_files_audited": 6,
            "synthetic_fixture_verifiers": 2,
            "physical_occurrence_background_manifests": 0,
            "physical_chart_invariant_theorems": 0,
            "physical_response_disjointness_theorems": 0,
        },
        "conclusion": {
            "grid_fixture_may_validate_conditional_energy_identity": 1,
            "grid_fixture_may_promote_to_physical_chart_proof": 0,
            "grid_fixture_may_promote_to_physical_response_disjointness_proof": 0,
            "chart_confinement_transfer_remains_conditional": 1,
        },
        "honesty": {
            "physical_source_proves_chart_confinement": 0,
            "physical_source_proves_response_disjointness": 0,
            "physical_background_coverage_proved": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def audit_sources(root: Path) -> None:
    orbit = read(root, DOC_ORBIT)
    host = read(root, DOC_HOST)
    host_verifier = read(root, HOST_VERIFIER)
    capacity_verifier = read(root, CAPACITY_VERIFIER)
    ancestry = read(root, ANCESTRY_CHECKER)
    status = read(root, STATUS_PATH)

    require("Omega_d=\\{0,\\ldots,d-1\\}^2" in orbit, "standard-grid host domain")
    require("complete collinearity or line-incidence structure" in orbit, "geometric signature")
    require("For fixed background set `B`" in host, "independent background input")
    require("The remaining work\nis to attach the actual background and recurrent provenance data" in host, "actual background remains open")

    fixture_snippet = "remaining = sorted(grid - set(response))"
    sample_snippet = "background = set(\n                    random.sample("
    require(fixture_snippet in host_verifier and sample_snippet in host_verifier, "host verifier grid fixture")
    require(fixture_snippet in capacity_verifier and sample_snippet in capacity_verifier, "capacity verifier grid fixture")
    require("random = Random(" in host_verifier and "random = Random(" in capacity_verifier, "random fixture seeds")

    require('"geometric_fibre_rows_complete_all_provenance":0' in ancestry, "ancestry provenance honesty")
    require("raw_fibre_backgrounds_cover_all_provenance = 0" in status, "status background honesty")
    require(HOST_ID not in host_verifier, "fixture unexpectedly attached to first-host occurrence")
    require(HOST_ID not in capacity_verifier, "capacity fixture unexpectedly attached to first-host occurrence")


def compile_manifest(root: Path) -> dict[str, Any]:
    audit_sources(root)
    return expected_manifest()


def validate(manifest: dict[str, Any], root: Path) -> None:
    require(manifest == compile_manifest(root), "manifest differs from exact source audit")
    distinctions = manifest.get("distinctions", {})
    require(distinctions.get("physical_chart_confinement_invariant_installed") == 0, "chart honesty")
    require(distinctions.get("physical_response_disjointness_invariant_installed") == 0, "disjointness honesty")
    require(manifest.get("honesty", {}).get("all_n_proved_by_checker") == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, Any], root: Path) -> int:
    mutations = [
        lambda item: item["aggregate"].update(source_files_audited=5),
        lambda item: item["aggregate"].update(synthetic_fixture_verifiers=1),
        lambda item: item["aggregate"].update(physical_occurrence_background_manifests=1),
        lambda item: item["distinctions"].update(background_is_independent_input_in_source_theorem=0),
        lambda item: item["distinctions"].update(source_chapter_explicitly_leaves_actual_background_attachment_open=0),
        lambda item: item["distinctions"].update(physical_chart_confinement_invariant_installed=1),
        lambda item: item["distinctions"].update(physical_response_disjointness_invariant_installed=1),
        lambda item: item["source_bindings"].pop(),
        lambda item: item["conclusion"].update(grid_fixture_may_promote_to_physical_chart_proof=1),
        lambda item: item["conclusion"].update(chart_confinement_transfer_remains_conditional=0),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate, root)
        except (AuditError, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "mutation audit")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    arguments = parser.parse_args()
    root = repository_root()
    manifest = compile_manifest(root)
    if arguments.write:
        arguments.write.parent.mkdir(parents=True, exist_ok=True)
        arguments.write.write_text(json.dumps(manifest, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    if arguments.check:
        observed = json.loads(arguments.check.read_text(encoding="utf-8"))
        validate(observed, root)
    print(json.dumps({"checker": "exact-recurrent-first-host-chart-fixture-nonpromotion", **manifest["aggregate"], "mutation_corruptions_rejected": mutation_audit(manifest, root), **manifest["honesty"]}, sort_keys=True))


if __name__ == "__main__":
    main()
