#!/usr/bin/env python3
"""Synchronize the exact source-statement truth bank with the all-frontier execution stack.

This wrapper requires the current-frontier execution certificate and the exact source-statement
truth registry to share the same typed obligation-artifact registry. It then requires the source
truth census, SOURCE_STATEMENTS_TRUE closure, and T01_SOURCE_STATEMENTS completion to agree.

The checker is a documentary source-root gate. It does not verify proof truth and permanently
reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_current_frontier_execution as current_frontier
import check_prime_power_source_statement_truth_registry as source_truth


class SourceTruthFrontierError(ValueError):
    """Raised when the source truth bank and all-frontier stack disagree."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SourceTruthFrontierError(message)


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    current_certificate = certificate.get("current_frontier_execution_certificate")
    source_certificate = certificate.get("source_statement_truth_registry_certificate")
    require(isinstance(current_certificate, dict),
            "current_frontier_execution_certificate: expected object")
    require(isinstance(source_certificate, dict),
            "source_statement_truth_registry_certificate: expected object")

    current_frontier.validate_certificate(current_certificate)
    source_truth.validate_certificate(source_certificate)
    current_exact = current_frontier.exact_certificate(current_certificate)
    source_exact = source_truth.exact_certificate(source_certificate)

    atomic_certificate = current_certificate["atomic_frontier_execution_certificate"]
    atomic_exact = atomic.exact_certificate(atomic_certificate)
    dossier = atomic_certificate["final_dossier_integrity_certificate"]
    handoff = dossier["final_induction_handoff_certificate"]
    premise_registry = handoff["premise_artifact_registry_certificate"]
    contract = premise_registry["final_implication_premise_contract_certificate"]
    nested_obligation_registry = contract["obligation_artifact_registry_certificate"]
    source_obligation_registry = source_certificate["obligation_artifact_registry_certificate"]
    require(
        nested_obligation_registry["certificate_sha256"]
        == source_obligation_registry["certificate_sha256"],
        "source truth registry and current frontier use different obligation registries",
    )

    target_by_id = {
        record["target_id"]: record for record in atomic_exact["target_result_records"]
    }
    t01_complete = int(target_by_id["T01_SOURCE_STATEMENTS"]["effective_target_complete"])
    source_ready = int(source_exact["claims"]["source_statement_truth_ready"])
    require(t01_complete == source_ready,
            "T01_SOURCE_STATEMENTS completion disagrees with exact source truth registry")

    current_ready = int(current_exact["claims"]["current_frontier_execution_ready"])
    source_root_ready = int(current_ready and source_ready and t01_complete)
    gate = {
        "current_frontier_execution_ready": current_ready,
        "source_statement_truth_ready": source_ready,
        "t01_source_statements_complete": t01_complete,
        "source_root_execution_ready": source_root_ready,
    }
    gate["source_root_gate_sha256"] = catalogue.canonical_digest(gate)

    source_claims = source_exact["claims"]
    blocker = {
        "proved_source_statements": source_claims["proved_source_statements"],
        "open_source_statements": source_claims["open_source_statements"],
        "open_source_ids_by_downstream_use": source_claims[
            "open_source_ids_by_downstream_use"
        ],
        "current_atomic_source_target_id": (
            "T02_RULE_EXHAUSTIVENESS" if source_ready else "T01_SOURCE_STATEMENTS"
        ),
    }
    blocker["source_root_blockers_sha256"] = catalogue.canonical_digest(blocker)

    claims = {
        "sources": source_claims["sources"],
        "proved_source_statements": source_claims["proved_source_statements"],
        "open_source_statements": source_claims["open_source_statements"],
        "source_root_execution_ready": source_root_ready,
        "exact_source_target_synchronization": 1,
        "shared_obligation_registry_identity": 1,
        "all_n_proved_by_checker": 0,
        "current_frontier_execution_sha256": current_certificate["certificate_sha256"],
        "source_statement_truth_registry_sha256": source_certificate["certificate_sha256"],
        "obligation_artifact_registry_sha256": nested_obligation_registry[
            "certificate_sha256"
        ],
        "source_root_gate_sha256": gate["source_root_gate_sha256"],
        "source_root_blockers_sha256": blocker["source_root_blockers_sha256"],
    }
    return {
        "source_root_gate": gate,
        "source_root_blockers": blocker,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("source_root_gate", "source_root_blockers", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "sources": claims["sources"],
        "proved": claims["proved_source_statements"],
        "open": claims["open_source_statements"],
        "ready": claims["source_root_execution_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    current_certificate: dict[str, Any],
    source_certificate: dict[str, Any],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "current_frontier_execution_certificate": current_certificate,
        "source_statement_truth_registry_certificate": source_certificate,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_source_truth_frontier_execution.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
