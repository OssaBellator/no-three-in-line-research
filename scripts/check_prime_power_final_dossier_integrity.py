#!/usr/bin/env python3
"""Compose the final implication contract with noncircular artifact-support integrity.

The final implication-premise contract checks semantic closure, typed artifact coverage,
blocker closure, termination mode, and ten ordinary proof premises. This checker adds the
missing requirement that the typed proof artifacts form an acyclic, dependency-aligned support
graph whose proved bundles reach all immediate prerequisite artifacts.

A ready integrity dossier is still documentary. This checker never verifies ordinary
mathematical proofs and never declares the no-three-in-line conjecture proved.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_final_implication_premise_contract as final_contract
import check_prime_power_obligation_artifact_support_dag as support_dag


class FinalDossierIntegrityError(ValueError):
    """Raised when the final contract and artifact-support dossier do not compose."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise FinalDossierIntegrityError(message)


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    contract_certificate = certificate.get("final_implication_premise_contract_certificate")
    support_certificate = certificate.get("obligation_artifact_support_dag_certificate")
    require(isinstance(contract_certificate, dict),
            "final_implication_premise_contract_certificate: expected object")
    require(isinstance(support_certificate, dict),
            "obligation_artifact_support_dag_certificate: expected object")
    final_contract.validate_certificate(contract_certificate)
    support_dag.validate_certificate(support_certificate)
    contract_exact = final_contract.exact_certificate(contract_certificate)
    support_exact = support_dag.exact_certificate(support_certificate)

    contract_registry = contract_certificate["obligation_artifact_registry_certificate"]
    support_registry = support_certificate["obligation_artifact_registry_certificate"]
    require(contract_registry["certificate_sha256"] == support_registry["certificate_sha256"],
            "final contract and artifact-support DAG use different artifact registries")

    support_claims = support_exact["claims"]
    support_ready = int(
        support_claims["artifact_support_acyclic"]
        and support_claims["artifact_support_dependency_aligned"]
        and support_claims["exact_dependency_artifact_support_coverage"]
    )
    contract_ready = int(contract_exact["claims"]["final_implication_contract_ready"])
    integrity_ready = int(contract_ready and support_ready)
    incomplete_support_obligations = [
        record["obligation_id"]
        for record in support_exact["obligation_support_records"]
        if record["declared_status"] == "proved" and not record["dependency_support_complete"]
    ]
    gate_record = {
        "final_implication_contract_ready": contract_ready,
        "artifact_support_integrity_ready": support_ready,
        "final_dossier_integrity_ready": integrity_ready,
        "open_premise_ids": contract_exact["claims"]["open_premise_ids"],
        "incomplete_artifact_support_obligation_ids": incomplete_support_obligations,
    }
    gate_record["final_dossier_gate_sha256"] = catalogue.canonical_digest(gate_record)

    claims = {
        "final_implication_contract_ready": contract_ready,
        "artifact_support_integrity_ready": support_ready,
        "final_dossier_integrity_ready": integrity_ready,
        "all_n_proved_by_checker": 0,
        "open_premises": len(contract_exact["claims"]["open_premise_ids"]),
        "incomplete_artifact_support_obligations": len(incomplete_support_obligations),
        "maximum_artifact_support_depth": support_claims["maximum_artifact_support_depth"],
        "final_contract_sha256": contract_certificate["certificate_sha256"],
        "artifact_support_dag_sha256": support_certificate["certificate_sha256"],
        "artifact_registry_sha256": contract_registry["certificate_sha256"],
        "final_dossier_gate_sha256": gate_record["final_dossier_gate_sha256"],
    }
    return {"final_dossier_gate": gate_record, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("final_dossier_gate", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "contract_ready": claims["final_implication_contract_ready"],
        "support_ready": claims["artifact_support_integrity_ready"],
        "ready": claims["final_dossier_integrity_ready"],
        "proved": claims["all_n_proved_by_checker"],
    }


def build_certificate(contract_certificate: dict[str, Any],
                      support_certificate: dict[str, Any]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "final_implication_premise_contract_certificate": contract_certificate,
        "obligation_artifact_support_dag_certificate": support_certificate,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_final_dossier_integrity.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
