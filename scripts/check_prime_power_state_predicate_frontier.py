#!/usr/bin/env python3
"""Validate the exact documentary T17 global-state predicate frontier.

The state census is derived from the exact T13 global classes.  T16 contributes rank records only
for rank-sensitive classes.  Every proved predicate has representative-by-representative agreement,
exact T13/T16 artifact support, typed sealing, and synchronization with T17_STATE_PREDICATES.
The checker validates identity and support only and permanently reports all_n_proved_by_checker = 0.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as target_artifacts
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_global_rank_frontier as t16_frontier
import check_prime_power_state_equivalence_frontier as t13_frontier


class StatePredicateFrontierError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise StatePredicateFrontierError(message)


def text(value: Any, path: str) -> str:
    require(isinstance(value, str) and value, f"{path}: nonempty string required")
    return value


def exact_ids(value: Any, expected: list[str], path: str) -> list[str]:
    require(isinstance(value, list), f"{path}: list required")
    require(value == expected, f"{path}: exact support required")
    require(value == sorted(value) and len(value) == len(set(value)), f"{path}: canonical IDs required")
    return list(value)


def exact_status_record(raw: dict[str, Any], state: dict[str, Any], class_artifact_id: str) -> dict[str, Any]:
    state_id = state["global_state_id"]
    require(raw.get("global_state_id") == state_id, f"state {state_id}: ID mismatch")
    require(raw.get("global_state_record_sha256") == state["global_state_record_sha256"],
            f"state {state_id}: T13 record mismatch")
    require(raw.get("t13_class_artifact_id") == class_artifact_id,
            f"state {state_id}: T13 artifact mismatch")
    predicate_id = text(raw.get("predicate_id"), f"state {state_id} predicate_id")
    status = raw.get("status")
    require(status in {"open", "proved"}, f"state {state_id}: open/proved required")
    locator, digest = raw.get("verification_locator"), raw.get("verification_digest")
    if status == "open":
        require(locator is None and digest is None, f"state {state_id}: open requires null verification")
    else:
        require(locator == f"global-state-predicate-registry://{state_id}"
                and isinstance(digest, str) and digest,
                f"state {state_id}: canonical proved verification required")
    core = {
        "global_state_id": state_id,
        "global_state_record_sha256": state["global_state_record_sha256"],
        "t13_class_artifact_id": class_artifact_id,
        "predicate_id": predicate_id,
        "status": status,
        "verification_locator": locator,
        "note": text(raw.get("note"), f"state {state_id} note"),
    }
    output = {**core, "verification_digest": digest,
              "state_predicate_record_core_sha256": catalogue.canonical_digest(core)}
    output["state_predicate_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_semantic(raw: dict[str, Any], *, state: dict[str, Any], record: dict[str, Any],
                   rank_record: dict[str, Any] | None, rank_artifact_id: str | None) -> dict[str, Any]:
    state_id = state["global_state_id"]
    require(raw.get("global_state_id") == state_id and raw.get("predicate_id") == record["predicate_id"],
            f"state {state_id}: semantic identity mismatch")
    require(raw.get("global_state_record_sha256") == state["global_state_record_sha256"],
            f"state {state_id}: semantic T13 binding mismatch")
    members = state["members"]
    raw_agreements = raw.get("representative_agreement_records")
    require(isinstance(raw_agreements, list) and len(raw_agreements) == len(members),
            f"state {state_id}: exact representative agreement count required")
    agreements = []
    for index, (item, member) in enumerate(zip(raw_agreements, members)):
        prefix = f"state {state_id} representative {index}"
        expected_support = sorted(member["support_state_claim_ids"])
        agreement = {
            "block_id": member["block_id"],
            "unit_id": member["unit_id"],
            "local_state_id": member["local_state_id"],
            "local_state_subject_sha256": member["local_state_subject_sha256"],
            "local_to_global_state_link_sha256": member["local_to_global_state_link_sha256"],
            "support_state_claim_ids": exact_ids(item.get("support_state_claim_ids"), expected_support,
                                                   f"{prefix} support"),
            "agreement_statement": text(item.get("agreement_statement"), f"{prefix} statement"),
            "evidence": text(item.get("evidence"), f"{prefix} evidence"),
        }
        require(all(item.get(key) == value for key, value in agreement.items()),
                f"{prefix}: exact identity required")
        agreement["representative_predicate_agreement_sha256"] = catalogue.canonical_digest(agreement)
        agreements.append(agreement)
    require(raw_agreements == agreements, f"state {state_id}: canonical representative bank required")

    rank_sensitive = int(rank_record is not None)
    if rank_sensitive:
        require(rank_artifact_id is not None and rank_record["status"] == "proved",
                f"state {state_id}: rank-sensitive predicate requires proved T16 rank")
        require(raw.get("t16_rank_record_sha256") == rank_record["global_state_rank_record_sha256"]
                and raw.get("t16_rank_artifact_id") == rank_artifact_id,
                f"state {state_id}: exact T16 rank binding required")
        rank_value = copy.deepcopy(rank_record["rank_value"])
    else:
        require(raw.get("t16_rank_record_sha256") is None
                and raw.get("t16_rank_artifact_id") is None,
                f"state {state_id}: non-rank predicate must not cite T16 rank")
        rank_value = None
    output = {
        "global_state_id": state_id,
        "global_state_record_sha256": state["global_state_record_sha256"],
        "predicate_id": record["predicate_id"],
        "role": state["role"],
        "stratum": state["stratum"],
        "owner": copy.deepcopy(state["owner"]),
        "rank_sensitive": rank_sensitive,
        "t16_rank_record_sha256": None if rank_record is None else rank_record["global_state_rank_record_sha256"],
        "t16_rank_artifact_id": rank_artifact_id,
        "rank_value": rank_value,
        "predicate_statement": text(raw.get("predicate_statement"), f"state {state_id} predicate statement"),
        "representative_agreement_records": agreements,
        "representative_agreements_sha256": catalogue.canonical_digest(agreements),
        "external_meaning_statement": text(raw.get("external_meaning_statement"),
                                           f"state {state_id} external meaning"),
        "evidence": text(raw.get("evidence"), f"state {state_id} semantic evidence"),
    }
    output["global_state_predicate_semantic_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_artifact(raw: dict[str, Any], *, state_id: str, semantic: dict[str, Any],
                   support_ids: list[str]) -> dict[str, Any]:
    require(raw.get("global_state_id") == state_id, f"state {state_id}: artifact identity mismatch")
    require(raw.get("artifact_kind") == "global-state-predicate-proof",
            f"state {state_id}: wrong artifact kind")
    exact_ids(raw.get("support_artifact_ids"), support_ids, f"state {state_id} artifact support")
    output = {
        "global_state_id": state_id,
        "artifact_id": text(raw.get("artifact_id"), f"state {state_id} artifact ID"),
        "artifact_kind": "global-state-predicate-proof",
        "global_state_predicate_semantic_sha256": semantic["global_state_predicate_semantic_sha256"],
        "proof_locator": text(raw.get("proof_locator"), f"state {state_id} proof locator"),
        "proof_digest": text(raw.get("proof_digest"), f"state {state_id} proof digest"),
        "proof_statement": text(raw.get("proof_statement"), f"state {state_id} proof statement"),
        "support_artifact_ids": support_ids,
        "evidence": text(raw.get("evidence"), f"state {state_id} artifact evidence"),
    }
    require(raw.get("global_state_predicate_semantic_sha256")
            == semantic["global_state_predicate_semantic_sha256"],
            f"state {state_id}: artifact semantic binding mismatch")
    require(output["artifact_id"] not in support_ids, f"state {state_id}: artifact self support")
    output["global_state_predicate_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    t16_certificate = certificate.get("global_rank_frontier_certificate")
    require(isinstance(t16_certificate, dict), "global_rank_frontier_certificate: object required")
    for name in ("global_state_predicate_records", "global_state_predicate_semantic_certificates",
                 "global_state_predicate_artifacts", "global_state_predicate_proof_bundles"):
        require(isinstance(certificate.get(name), list), f"{name}: list required")
    t16_frontier.validate_certificate(t16_certificate)
    t16_exact = t16_frontier.exact_certificate(t16_certificate)
    t15_certificate = t16_certificate["interface_exhaustiveness_frontier_certificate"]
    t14_certificate = t15_certificate["component_scale_frontier_certificate"]
    t13_certificate = t14_certificate["state_equivalence_frontier_certificate"]
    t13_frontier.validate_certificate(t13_certificate)
    t13_exact = t13_frontier.exact_certificate(t13_certificate)

    states = t13_exact["global_state_records"]
    class_artifact_by_state = {item["global_state_id"]: item["artifact_id"]
                               for item in t13_exact["state_equivalence_class_artifacts"]}
    rank_record_by_state = {item["global_state_id"]: item
                            for item in t16_exact["global_state_rank_records"]}
    rank_artifact_by_state = {item["global_state_id"]: item["artifact_id"]
                              for item in t16_exact["global_state_rank_artifacts"]}
    require(all(state["global_state_id"] in class_artifact_by_state for state in states),
            "T17 requires every T13 class artifact")

    raw_records = certificate["global_state_predicate_records"]
    require(len(raw_records) == len(states)
            and [item.get("global_state_id") for item in raw_records]
            == [item["global_state_id"] for item in states],
            "global_state_predicate_records: exact T13 order required")
    records = [exact_status_record(raw, state, class_artifact_by_state[state["global_state_id"]])
               for raw, state in zip(raw_records, states)]
    require(raw_records == records, "global_state_predicate_records: noncanonical")
    predicate_ids = [item["predicate_id"] for item in records]
    require(len(predicate_ids) == len(set(predicate_ids)), "T17 predicate IDs must be unique")
    record_by_state = {item["global_state_id"]: item for item in records}

    semantic_groups = {state["global_state_id"]: [] for state in states}
    for raw in certificate["global_state_predicate_semantic_certificates"]:
        require(raw.get("global_state_id") in semantic_groups, "T17 semantic: unknown state")
        semantic_groups[raw["global_state_id"]].append(raw)
    semantics = []
    semantic_by_state = {}
    for state in states:
        state_id = state["global_state_id"]
        record = record_by_state[state_id]
        group = semantic_groups[state_id]
        if record["status"] == "open":
            require(not group, f"state {state_id}: open predicate has semantics")
            continue
        require(len(group) == 1, f"state {state_id}: exactly one predicate semantic required")
        semantic = exact_semantic(group[0], state=state, record=record,
                                  rank_record=rank_record_by_state.get(state_id),
                                  rank_artifact_id=rank_artifact_by_state.get(state_id))
        semantics.append(semantic)
        semantic_by_state[state_id] = semantic
    require(certificate["global_state_predicate_semantic_certificates"] == semantics,
            "global_state_predicate_semantic_certificates: noncanonical")

    artifact_groups = {state["global_state_id"]: [] for state in states}
    for raw in certificate["global_state_predicate_artifacts"]:
        require(raw.get("global_state_id") in artifact_groups, "T17 artifact: unknown state")
        artifact_groups[raw["global_state_id"]].append(raw)
    artifacts = []
    bundles = []
    for state in states:
        state_id = state["global_state_id"]
        record = record_by_state[state_id]
        group = artifact_groups[state_id]
        if record["status"] == "open":
            require(not group, f"state {state_id}: open predicate has artifact")
            continue
        require(len(group) == 1, f"state {state_id}: exactly one predicate artifact required")
        support = [class_artifact_by_state[state_id]]
        if state_id in rank_artifact_by_state:
            support.append(rank_artifact_by_state[state_id])
        support.sort()
        artifact = exact_artifact(group[0], state_id=state_id,
                                  semantic=semantic_by_state[state_id], support_ids=support)
        artifacts.append(artifact)
        bundle = {
            "global_state_id": state_id,
            "state_predicate_record_core_sha256": record["state_predicate_record_core_sha256"],
            "global_state_predicate_semantic_sha256": semantic_by_state[state_id][
                "global_state_predicate_semantic_sha256"],
            "global_state_predicate_artifact_sha256": artifact[
                "global_state_predicate_artifact_sha256"],
            "support_artifact_ids": support,
        }
        bundle["global_state_predicate_proof_bundle_sha256"] = catalogue.canonical_digest(bundle)
        require(record["verification_digest"] == bundle["global_state_predicate_proof_bundle_sha256"],
                f"state {state_id}: verification digest mismatch")
        bundles.append(bundle)
    require(certificate["global_state_predicate_artifacts"] == artifacts,
            "global_state_predicate_artifacts: noncanonical")
    require(certificate["global_state_predicate_proof_bundles"] == bundles,
            "global_state_predicate_proof_bundles: incorrect")
    artifact_ids = [item["artifact_id"] for item in artifacts]
    require(len(artifact_ids) == len(set(artifact_ids)), "T17 artifact IDs duplicate")

    counts = Counter(item["status"] for item in records)
    ready = int(t13_exact["claims"]["t13_state_equivalence_ready"]
                and t16_exact["claims"]["t16_global_rank_ready"]
                and counts["proved"] == len(records)
                and len(semantics) == len(records)
                and len(artifacts) == len(records))
    bank = {
        "t13_state_equivalence_proof_bank_sha256": t13_exact["claims"][
            "state_equivalence_frontier_proof_bank_sha256"],
        "t16_global_rank_proof_bank_sha256": t16_exact["claims"][
            "global_rank_frontier_proof_bank_sha256"],
        "global_state_predicate_records_sha256": catalogue.canonical_digest(records),
        "global_state_predicate_semantic_certificates_sha256": catalogue.canonical_digest(semantics),
        "global_state_predicate_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "global_state_predicate_proof_bundles_sha256": catalogue.canonical_digest(bundles),
    }
    bank["state_predicate_frontier_proof_bank_sha256"] = catalogue.canonical_digest(bank)

    t04_certificate = t13_certificate["fate_transition_state_frontier_certificate"][
        "block_interface_population_frontier_certificate"]
    registry = t04_certificate["atomic_target_artifact_registry_certificate"]
    target_artifacts.validate_certificate(registry)
    target_exact = target_artifacts.exact_certificate(registry)
    atomic_certificate = registry["current_frontier_execution_certificate"][
        "atomic_frontier_execution_certificate"]
    atomic.validate_certificate(atomic_certificate)
    atomic_exact = atomic.exact_certificate(atomic_certificate)
    results = {item["target_id"]: item for item in atomic_exact["target_result_records"]}
    require(int(results["T17_STATE_PREDICATES"]["effective_target_complete"]) == ready,
            "T17 atomic completion mismatch")
    target = {item["target_id"]: item for item in target_exact["atomic_target_artifacts"]}.get(
        "T17_STATE_PREDICATES")
    if ready:
        require(target is not None
                and target["artifact_kind"] == "global-state-predicate-proof"
                and target["proof_locator"] == "state-predicate-frontier://T17_STATE_PREDICATES"
                and target["proof_digest"] == bank["state_predicate_frontier_proof_bank_sha256"],
                "T17 target artifact mismatch")
    else:
        require(target is None, "open T17 target has artifact")

    claims = {
        "global_state_predicates": len(records),
        "open_global_state_predicates": counts["open"],
        "proved_global_state_predicates": counts["proved"],
        "rank_sensitive_predicates": len(rank_record_by_state),
        "representative_agreement_records": sum(len(item["representative_agreement_records"])
                                                  for item in semantics),
        "t17_state_predicates_ready": ready,
        "exact_t13_global_state_census": 1,
        "exact_representative_agreement_coverage": 1,
        "exact_t16_rank_sensitive_binding": 1,
        "legacy_parallel_refinement_excluded": 1,
        "noncircular_t17_bank_binding": 1,
        "all_n_proved_by_checker": 0,
        "open_global_state_ids": [item["global_state_id"] for item in records
                                  if item["status"] == "open"],
        "state_predicate_frontier_proof_bank_sha256": bank[
            "state_predicate_frontier_proof_bank_sha256"],
    }
    return {
        "global_state_predicate_records": records,
        "global_state_predicate_semantic_certificates": semantics,
        "global_state_predicate_artifacts": artifacts,
        "global_state_predicate_proof_bundles": bundles,
        "state_predicate_frontier_proof_bank": bank,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, Any]:
    require(isinstance(certificate, dict) and certificate.get("version") == 1,
            "version 1 certificate required")
    exact = exact_certificate(certificate)
    for key, value in exact.items():
        require(certificate.get(key) == value, f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"states": claims["global_state_predicates"],
            "proved": claims["proved_global_state_predicates"],
            "rank_sensitive": claims["rank_sensitive_predicates"],
            "ready": claims["t17_state_predicates_ready"], "all_n": 0}


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_state_predicate_frontier.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
