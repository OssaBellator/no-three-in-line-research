#!/usr/bin/env python3
"""Validate and synchronize the exact T12 auxiliary-semantics proof bank.

T07 supplies the exact state and transition claim banks, while T11 supplies the exact selected
recurrent blocks, common-weight rows and strict margins. This checker reuses the older acyclic
auxiliary-elimination checker for finite weighted substitution, but requires every elimination
certificate to use the exact T11 common-weight certificate and gives every expansion edge explicit
support from the selected slots' T07 state and transition claims.

For a proved block, complete elimination must preserve the T11 selected response, may not increase its
row load, and may not decrease its strict margin. The checker validates documentary identity,
coverage, support and arithmetic only; it does not prove the semantic statements true and permanently
reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_acyclic_auxiliary_elimination as acyclic
import check_prime_power_all_n_implication_closure as closure
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as target_artifacts
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_fate_transition_state_frontier as t07_frontier
import check_prime_power_obligation_artifact_registry as obligation_artifacts
import check_prime_power_recurrent_block_closure_frontier as t11_frontier


class AuxiliarySemanticsFrontierError(ValueError):
    """Raised when the exact T12 auxiliary-semantics bank is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AuxiliarySemanticsFrontierError(message)


BLOCK_ARTIFACT_KIND = "recurrent-block-auxiliary-elimination-proof"
OBLIGATION_LOCATOR = "auxiliary-semantics-frontier://AUXILIARY_EXPANSIONS_SEMANTIC"
T12_TARGET_LOCATOR = "auxiliary-semantics-frontier://T12_AUXILIARY_SEMANTICS"


def exact_status_record(
    raw: dict[str, Any],
    *,
    block_record: dict[str, Any],
    common_record: dict[str, Any] | None,
    path: str,
) -> dict[str, Any]:
    block_id = block_record["block_id"]
    require(raw.get("block_id") == block_id, f"{path}.block_id: mismatch")
    require(
        raw.get("t11_block_closure_record_sha256")
        == block_record["block_closure_record_sha256"],
        f"{path}.t11_block_closure_record_sha256: mismatch",
    )
    common_sha = None if common_record is None else common_record[
        "recurrent_block_common_weight_record_sha256"
    ]
    require(
        raw.get("t11_common_weight_record_sha256") == common_sha,
        f"{path}.t11_common_weight_record_sha256: mismatch",
    )
    status = raw.get("status")
    locator = raw.get("verification_locator")
    digest = raw.get("verification_digest")
    note = raw.get("note")
    require(status in {"open", "proved"}, f"{path}.status: expected open/proved")
    require(isinstance(note, str) and note, f"{path}.note: required")
    if status == "open":
        require(locator is None, f"{path}.verification_locator: open requires null")
        require(digest is None, f"{path}.verification_digest: open requires null")
    else:
        require(
            block_record["status"] == "proved" and common_record is not None,
            f"{path}: proved T12 block requires proved T11 block",
        )
        require(
            locator == f"auxiliary-semantics-registry://{block_id}",
            f"{path}.verification_locator: canonical block URI required",
        )
        require(isinstance(digest, str) and digest, f"{path}.verification_digest: required")
    core = {
        "block_id": block_id,
        "t11_block_closure_record_sha256": block_record["block_closure_record_sha256"],
        "t11_common_weight_record_sha256": common_sha,
        "status": status,
        "verification_locator": locator,
        "note": note,
    }
    output = {
        **core,
        "verification_digest": digest,
        "auxiliary_semantics_record_core_sha256": catalogue.canonical_digest(core),
    }
    output["auxiliary_semantics_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_claim_id_list(
    raw: Any,
    *,
    allowed: set[str],
    nonempty: bool,
    path: str,
) -> list[str]:
    require(isinstance(raw, list), f"{path}: expected list")
    require(all(isinstance(value, str) and value for value in raw), f"{path}: bad claim ID")
    require(raw == sorted(raw), f"{path}: sorted order required")
    require(len(raw) == len(set(raw)), f"{path}: duplicates")
    require(set(raw) <= allowed, f"{path}: claim outside exact block T07 bank")
    if nonempty:
        require(bool(raw), f"{path}: nonempty support required")
    return list(raw)


def exact_edge_semantics(
    raw: dict[str, Any],
    *,
    target: dict[str, Any],
    state_claim_ids: set[str],
    transition_claim_ids: set[str],
    path: str,
) -> dict[str, Any]:
    require(
        raw.get("target_state_id") == target["state_id"],
        f"{path}.target_state_id: mismatch",
    )
    require(
        raw.get("multiplicity") == target["multiplicity"],
        f"{path}.multiplicity: mismatch",
    )
    require(
        raw.get("target_record_sha256") == target["target_record_sha256"],
        f"{path}.target_record_sha256: mismatch",
    )
    state_support = exact_claim_id_list(
        raw.get("target_state_claim_ids"),
        allowed=state_claim_ids,
        nonempty=True,
        path=f"{path}.target_state_claim_ids",
    )
    transition_support = exact_claim_id_list(
        raw.get("transition_claim_ids"),
        allowed=transition_claim_ids,
        nonempty=True,
        path=f"{path}.transition_claim_ids",
    )
    statement = raw.get("edge_statement")
    evidence = raw.get("evidence")
    require(isinstance(statement, str) and statement, f"{path}.edge_statement: required")
    require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
    output = {
        "target_state_id": target["state_id"],
        "multiplicity": target["multiplicity"],
        "target_record_sha256": target["target_record_sha256"],
        "target_state_claim_ids": state_support,
        "transition_claim_ids": transition_support,
        "edge_statement": statement,
        "evidence": evidence,
    }
    output["auxiliary_edge_semantics_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_expansion_semantics(
    raw: dict[str, Any],
    *,
    block_id: str,
    expansion: dict[str, Any],
    state_claim_ids: set[str],
    transition_claim_ids: set[str],
    path: str,
) -> dict[str, Any]:
    auxiliary = expansion["auxiliary_state_id"]
    require(raw.get("block_id") == block_id, f"{path}.block_id: mismatch")
    require(
        raw.get("auxiliary_state_id") == auxiliary,
        f"{path}.auxiliary_state_id: mismatch",
    )
    require(
        raw.get("expansion_record_sha256") == expansion["expansion_record_sha256"],
        f"{path}.expansion_record_sha256: mismatch",
    )
    source_support = exact_claim_id_list(
        raw.get("source_state_claim_ids"),
        allowed=state_claim_ids,
        nonempty=True,
        path=f"{path}.source_state_claim_ids",
    )
    fixed_support = exact_claim_id_list(
        raw.get("fixed_load_transition_claim_ids"),
        allowed=transition_claim_ids,
        nonempty=expansion["fixed_load"] > 0,
        path=f"{path}.fixed_load_transition_claim_ids",
    )
    raw_edges = raw.get("target_edge_semantics")
    require(isinstance(raw_edges, list), f"{path}.target_edge_semantics: expected list")
    require(
        len(raw_edges) == len(expansion["target_multiplicities"]),
        f"{path}.target_edge_semantics: exact target coverage required",
    )
    edges = [
        exact_edge_semantics(
            edge,
            target=target,
            state_claim_ids=state_claim_ids,
            transition_claim_ids=transition_claim_ids,
            path=f"{path}.target_edge_semantics[{index}]",
        )
        for index, (edge, target) in enumerate(
            zip(raw_edges, expansion["target_multiplicities"])
        )
    ]
    require(raw_edges == edges, f"{path}.target_edge_semantics: canonical records required")
    statement = raw.get("expansion_statement")
    evidence = raw.get("evidence")
    no_credit_statement = raw.get("no_auxiliary_credit_statement")
    no_credit_evidence = raw.get("no_auxiliary_credit_evidence")
    for name, value in (
        ("expansion_statement", statement),
        ("evidence", evidence),
        ("no_auxiliary_credit_statement", no_credit_statement),
        ("no_auxiliary_credit_evidence", no_credit_evidence),
    ):
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    output = {
        "block_id": block_id,
        "auxiliary_state_id": auxiliary,
        "expansion_record_sha256": expansion["expansion_record_sha256"],
        "fixed_load": expansion["fixed_load"],
        "source_state_claim_ids": source_support,
        "fixed_load_transition_claim_ids": fixed_support,
        "target_edge_semantics": edges,
        "expansion_statement": statement,
        "evidence": evidence,
        "no_auxiliary_credit_statement": no_credit_statement,
        "no_auxiliary_credit_evidence": no_credit_evidence,
    }
    output["auxiliary_expansion_semantics_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_elimination_wrapper(
    raw: dict[str, Any],
    *,
    block_record: dict[str, Any],
    common_record: dict[str, Any],
    state_claim_ids: set[str],
    transition_claim_ids: set[str],
    path: str,
) -> dict[str, Any]:
    block_id = block_record["block_id"]
    require(raw.get("block_id") == block_id, f"{path}.block_id: mismatch")
    require(
        raw.get("t11_common_weight_record_sha256")
        == common_record["recurrent_block_common_weight_record_sha256"],
        f"{path}.t11_common_weight_record_sha256: mismatch",
    )
    certificate = raw.get("acyclic_auxiliary_elimination_certificate")
    require(
        isinstance(certificate, dict),
        f"{path}.acyclic_auxiliary_elimination_certificate: required",
    )
    acyclic.validate_certificate(certificate)
    exact = acyclic.exact_certificate(certificate)
    require(
        certificate["common_weight_certificate"] == common_record["common_weight_certificate"],
        f"{path}: elimination certificate uses a parallel common-weight population",
    )
    require(
        exact["claims"]["strict_scc_preserved_after_elimination"] == 1,
        f"{path}: strict recurrent block not preserved after elimination",
    )

    raw_semantics = raw.get("expansion_semantic_records")
    require(
        isinstance(raw_semantics, list),
        f"{path}.expansion_semantic_records: expected list",
    )
    expansions = exact["auxiliary_expansions"]
    require(
        len(raw_semantics) == len(expansions),
        f"{path}.expansion_semantic_records: exact expansion coverage required",
    )
    semantics = [
        exact_expansion_semantics(
            semantic,
            block_id=block_id,
            expansion=expansion,
            state_claim_ids=state_claim_ids,
            transition_claim_ids=transition_claim_ids,
            path=f"{path}.expansion_semantic_records[{index}]",
        )
        for index, (semantic, expansion) in enumerate(zip(raw_semantics, expansions))
    ]
    require(
        raw_semantics == semantics,
        f"{path}.expansion_semantic_records: canonical records required",
    )

    bridge_by_key = {
        (bridge["local_parent_state_id"], bridge["fibre_id"]): bridge
        for bridge in common_record["row_bridge_records"]
    }
    eliminated_rows = exact["eliminated_row_records"]
    require(
        {(row["parent_state_id"], row["fibre_id"]) for row in eliminated_rows}
        == set(bridge_by_key),
        f"{path}: eliminated-row bank differs from exact T11 row bank",
    )
    selected_stability_records = []
    for row in eliminated_rows:
        key = (row["parent_state_id"], row["fibre_id"])
        bridge = bridge_by_key[key]
        require(
            row["selected_response"] == bridge["selected_response"],
            f"{path}: auxiliary elimination changed selected response for {key}",
        )
        require(
            row["selected_row_load"] <= bridge["minimum_row_load"],
            f"{path}: auxiliary elimination increased selected row load for {key}",
        )
        require(
            row["selected_margin"] >= bridge["strict_margin"],
            f"{path}: auxiliary elimination decreased selected margin for {key}",
        )
        stability = {
            "parent_state_id": row["parent_state_id"],
            "fibre_id": row["fibre_id"],
            "selected_response": copy.deepcopy(row["selected_response"]),
            "selected_response_sha256": catalogue.canonical_digest(row["selected_response"]),
            "original_selected_row_load": bridge["minimum_row_load"],
            "eliminated_selected_row_load": row["selected_row_load"],
            "original_strict_margin": bridge["strict_margin"],
            "eliminated_selected_margin": row["selected_margin"],
            "row_elimination_sha256": row["row_elimination_sha256"],
            "common_weight_row_bridge_sha256": bridge["common_weight_row_bridge_sha256"],
        }
        stability["selected_response_stability_sha256"] = catalogue.canonical_digest(stability)
        selected_stability_records.append(stability)
    selected_stability_records.sort(
        key=lambda item: (item["parent_state_id"], item["fibre_id"])
    )

    output = {
        "block_id": block_id,
        "t11_common_weight_record_sha256": common_record[
            "recurrent_block_common_weight_record_sha256"
        ],
        "acyclic_auxiliary_elimination_certificate": certificate,
        "acyclic_auxiliary_elimination_certificate_sha256": certificate["certificate_sha256"],
        "expansion_semantic_records": semantics,
        "expansion_semantic_records_sha256": catalogue.canonical_digest(semantics),
        "selected_response_stability_records": selected_stability_records,
        "selected_response_stability_records_sha256": catalogue.canonical_digest(
            selected_stability_records
        ),
        "topological_order": list(exact["claims"]["topological_depth_order"]),
        "root_auxiliary_states": exact["claims"]["root_auxiliary_states"],
        "eliminated_auxiliary_states": exact["claims"]["eliminated_auxiliary_states"],
        "minimum_response_margin_gain": exact["claims"]["minimum_response_margin_gain"],
        "strict_scc_preserved_after_elimination": exact["claims"][
            "strict_scc_preserved_after_elimination"
        ],
    }
    output["block_auxiliary_elimination_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_block_artifact(
    raw: dict[str, Any],
    *,
    block_id: str,
    elimination_sha256: str,
    expected_t11_common_support: list[str],
    expected_t11_closure_support: list[str],
    expected_t07_support: list[str],
    path: str,
) -> dict[str, Any]:
    values = {
        key: raw.get(key)
        for key in (
            "artifact_id",
            "artifact_kind",
            "proof_locator",
            "proof_digest",
            "proof_statement",
            "evidence",
        )
    }
    for name, value in values.items():
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    require(raw.get("block_id") == block_id, f"{path}.block_id: mismatch")
    require(
        values["artifact_kind"] == BLOCK_ARTIFACT_KIND,
        f"{path}.artifact_kind: wrong kind",
    )
    require(
        raw.get("block_auxiliary_elimination_sha256") == elimination_sha256,
        f"{path}.block_auxiliary_elimination_sha256: mismatch",
    )
    support_specs = {
        "support_t11_common_weight_artifact_ids": expected_t11_common_support,
        "support_t11_block_closure_artifact_ids": expected_t11_closure_support,
        "support_t07_semantic_artifact_ids": expected_t07_support,
    }
    output = {
        "block_id": block_id,
        "artifact_id": values["artifact_id"],
        "artifact_kind": values["artifact_kind"],
        "block_auxiliary_elimination_sha256": elimination_sha256,
        "proof_locator": values["proof_locator"],
        "proof_digest": values["proof_digest"],
        "proof_statement": values["proof_statement"],
    }
    for name, expected in support_specs.items():
        support = raw.get(name)
        require(support == expected, f"{path}.{name}: exact support required")
        require(isinstance(support, list), f"{path}.{name}: list required")
        require(support == sorted(support), f"{path}.{name}: sorted")
        require(len(support) == len(set(support)), f"{path}.{name}: duplicates")
        require(values["artifact_id"] not in support, f"{path}: self support")
        output[name] = list(support)
    output["evidence"] = values["evidence"]
    output["auxiliary_elimination_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    t11_certificate = certificate.get("recurrent_block_closure_frontier_certificate")
    raw_records = certificate.get("auxiliary_semantics_records")
    raw_eliminations = certificate.get("block_auxiliary_eliminations")
    raw_artifacts = certificate.get("auxiliary_semantics_artifacts")
    require(
        isinstance(t11_certificate, dict),
        "recurrent_block_closure_frontier_certificate: expected object",
    )
    for name, value in (
        ("auxiliary_semantics_records", raw_records),
        ("block_auxiliary_eliminations", raw_eliminations),
        ("auxiliary_semantics_artifacts", raw_artifacts),
    ):
        require(isinstance(value, list), f"{name}: expected list")

    t11_frontier.validate_certificate(t11_certificate)
    t11_exact = t11_frontier.exact_certificate(t11_certificate)
    t10_certificate = t11_certificate["transition_resource_frontier_certificate"]
    t06_certificate = t10_certificate["candidate_policy_frontier_certificate"]
    t07_certificate = t06_certificate["fate_transition_state_frontier_certificate"]
    t07_frontier.validate_certificate(t07_certificate)
    t07_exact = t07_frontier.exact_certificate(t07_certificate)

    t04_certificate = t06_certificate["geometry_selector_frontier_certificate"][
        "block_interface_population_frontier_certificate"
    ]
    target_registry = t04_certificate["atomic_target_artifact_registry_certificate"]
    target_artifacts.validate_certificate(target_registry)
    target_exact = target_artifacts.exact_certificate(target_registry)
    current = target_registry["current_frontier_execution_certificate"]
    atomic_certificate = current["atomic_frontier_execution_certificate"]
    atomic.validate_certificate(atomic_certificate)
    atomic_exact = atomic.exact_certificate(atomic_certificate)

    rule_certificate = t04_certificate["slot_candidate_population_frontier_certificate"][
        "rule_exhaustiveness_frontier_certificate"
    ]
    source_registry = rule_certificate["source_truth_frontier_execution_certificate"][
        "source_statement_truth_registry_certificate"
    ]
    obligation_certificate = source_registry["obligation_artifact_registry_certificate"]
    obligation_artifacts.validate_certificate(obligation_certificate)
    obligation_exact = obligation_artifacts.exact_certificate(obligation_certificate)
    closure_certificate = obligation_certificate["all_n_implication_closure_certificate"]
    closure_exact = closure.exact_certificate(closure_certificate)

    block_records = t11_exact["recurrent_block_closure_records"]
    common_by_block = {
        record["block_id"]: record
        for record in t11_exact["recurrent_block_common_weight_records"]
    }
    common_artifact_by_block = {
        artifact["block_id"]: artifact["artifact_id"]
        for artifact in t11_exact["recurrent_block_common_weight_artifacts"]
    }
    closure_artifact_by_block = {
        artifact["block_id"]: artifact["artifact_id"]
        for artifact in t11_exact["recurrent_block_closure_artifacts"]
    }
    semantic_by_slot = {
        item["slot_id"]: item
        for item in t07_exact["slot_fate_transition_state_semantic_certificates"]
    }
    semantic_artifact_by_slot = {
        artifact["slot_id"]: artifact["artifact_id"]
        for artifact in t07_exact["slot_fate_transition_state_artifacts"]
    }

    require(
        len(raw_records) == len(block_records),
        "auxiliary_semantics_records: exact T11 block cardinality required",
    )
    require(
        [record.get("block_id") for record in raw_records]
        == [record["block_id"] for record in block_records],
        "auxiliary_semantics_records: canonical block order required",
    )
    records = [
        exact_status_record(
            raw,
            block_record=block_record,
            common_record=common_by_block.get(block_record["block_id"]),
            path=f"auxiliary_semantics_records[{index}]",
        )
        for index, (raw, block_record) in enumerate(zip(raw_records, block_records))
    ]
    require(
        raw_records == records,
        "auxiliary_semantics_records: canonical records/digests required",
    )

    elimination_groups = {record["block_id"]: [] for record in records}
    for raw in raw_eliminations:
        require(isinstance(raw, dict), "block_auxiliary_eliminations: expected objects")
        block_id = raw.get("block_id")
        require(
            block_id in elimination_groups,
            f"block_auxiliary_eliminations: unknown block {block_id}",
        )
        elimination_groups[block_id].append(raw)

    eliminations: list[dict[str, Any]] = []
    elimination_by_block: dict[str, dict[str, Any]] = {}
    slots_by_block: dict[str, list[str]] = {}
    for record in records:
        block_id = record["block_id"]
        group = elimination_groups[block_id]
        if record["status"] == "open":
            require(not group, f"block {block_id}: open T12 record cannot contain elimination")
            continue
        require(len(group) == 1, f"block {block_id}: exactly one elimination required")
        common_record = common_by_block[block_id]
        selected_slots = sorted(
            {bridge["selected_slot_id"] for bridge in common_record["row_bridge_records"]}
        )
        slots_by_block[block_id] = selected_slots
        require(
            all(slot in semantic_by_slot for slot in selected_slots),
            f"block {block_id}: selected slot lacks T07 semantics",
        )
        state_ids = {
            claim["claim_id"]
            for slot in selected_slots
            for claim in semantic_by_slot[slot]["state_claims"]
        }
        transition_ids = {
            claim["claim_id"]
            for slot in selected_slots
            for claim in semantic_by_slot[slot]["transition_claims"]
        }
        elimination = exact_elimination_wrapper(
            group[0],
            block_record=record,
            common_record=common_record,
            state_claim_ids=state_ids,
            transition_claim_ids=transition_ids,
            path=f"block_auxiliary_elimination[{block_id}]",
        )
        eliminations.append(elimination)
        elimination_by_block[block_id] = elimination
    require(
        raw_eliminations == eliminations,
        "block_auxiliary_eliminations: canonical order/content required",
    )

    artifact_groups = {record["block_id"]: [] for record in records}
    for raw in raw_artifacts:
        require(isinstance(raw, dict), "auxiliary_semantics_artifacts: expected objects")
        block_id = raw.get("block_id")
        require(
            block_id in artifact_groups,
            f"auxiliary semantics artifact: unknown block {block_id}",
        )
        artifact_groups[block_id].append(raw)

    artifacts: list[dict[str, Any]] = []
    proof_bundles: list[dict[str, Any]] = []
    for record in records:
        block_id = record["block_id"]
        group = artifact_groups[block_id]
        if record["status"] == "open":
            require(not group, f"block {block_id}: open T12 record cannot contain artifact")
            continue
        require(len(group) == 1, f"block {block_id}: exactly one T12 artifact required")
        require(
            block_id in common_artifact_by_block and block_id in closure_artifact_by_block,
            f"block {block_id}: T11 internal artifacts missing",
        )
        selected_slots = slots_by_block[block_id]
        require(
            all(slot in semantic_artifact_by_slot for slot in selected_slots),
            f"block {block_id}: selected T07 artifact missing",
        )
        artifact = exact_block_artifact(
            group[0],
            block_id=block_id,
            elimination_sha256=elimination_by_block[block_id][
                "block_auxiliary_elimination_sha256"
            ],
            expected_t11_common_support=[common_artifact_by_block[block_id]],
            expected_t11_closure_support=[closure_artifact_by_block[block_id]],
            expected_t07_support=sorted(
                semantic_artifact_by_slot[slot] for slot in selected_slots
            ),
            path=f"auxiliary_semantics_artifact[{block_id}]",
        )
        artifacts.append(artifact)
        proof_bundle = {
            "block_id": block_id,
            "auxiliary_semantics_record_core_sha256": record[
                "auxiliary_semantics_record_core_sha256"
            ],
            "block_auxiliary_elimination_sha256": elimination_by_block[block_id][
                "block_auxiliary_elimination_sha256"
            ],
            "auxiliary_elimination_artifact_sha256": artifact[
                "auxiliary_elimination_artifact_sha256"
            ],
            "support_t11_common_weight_artifact_ids": artifact[
                "support_t11_common_weight_artifact_ids"
            ],
            "support_t11_block_closure_artifact_ids": artifact[
                "support_t11_block_closure_artifact_ids"
            ],
            "support_t07_semantic_artifact_ids": artifact[
                "support_t07_semantic_artifact_ids"
            ],
        }
        proof_bundle["auxiliary_semantics_proof_bundle_sha256"] = (
            catalogue.canonical_digest(proof_bundle)
        )
        require(
            record["verification_digest"]
            == proof_bundle["auxiliary_semantics_proof_bundle_sha256"],
            f"block {block_id}: verification digest does not bind exact T12 bundle",
        )
        proof_bundles.append(proof_bundle)
    require(
        raw_artifacts == artifacts,
        "auxiliary_semantics_artifacts: canonical order/content required",
    )
    artifact_ids = [artifact["artifact_id"] for artifact in artifacts]
    require(
        len(artifact_ids) == len(set(artifact_ids)),
        "auxiliary_semantics_artifacts: duplicate artifact_id",
    )

    counts = Counter(record["status"] for record in records)
    t07_ready = int(t07_exact["claims"]["fate_transition_state_semantics_ready"])
    t11_ready = int(t11_exact["claims"]["t11_recurrent_block_closure_ready"])
    t12_ready = int(
        t07_ready
        and t11_ready
        and counts["proved"] == len(records)
        and len(eliminations) == len(records)
        and len(artifacts) == len(records)
    )
    proof_bank = {
        "t07_state_semantics_proof_bank_sha256": t07_exact["claims"][
            "state_semantics_proof_bank_sha256"
        ],
        "t07_transition_proof_bank_sha256": t07_exact["claims"][
            "transition_proof_bank_sha256"
        ],
        "t11_recurrent_block_closure_proof_bank_sha256": t11_exact["claims"][
            "t11_recurrent_block_closure_proof_bank_sha256"
        ],
        "auxiliary_semantics_records_sha256": catalogue.canonical_digest(records),
        "block_auxiliary_eliminations_sha256": catalogue.canonical_digest(eliminations),
        "auxiliary_semantics_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "auxiliary_semantics_proof_bundles_sha256": catalogue.canonical_digest(
            proof_bundles
        ),
    }
    proof_bank["auxiliary_semantics_proof_bank_sha256"] = catalogue.canonical_digest(
        proof_bank
    )

    closure_by_id = {
        item["obligation_id"]: item
        for item in closure_exact["obligation_closure_records"]
    }
    require(
        int(closure_by_id["AUXILIARY_EXPANSIONS_SEMANTIC"]["closed"])
        == t12_ready,
        "AUXILIARY_EXPANSIONS_SEMANTIC closure disagrees with exact T12 bank",
    )
    obligation_records = [
        artifact
        for artifact in obligation_exact["proof_artifacts"]
        if artifact["obligation_id"] == "AUXILIARY_EXPANSIONS_SEMANTIC"
    ]
    require(
        len(obligation_records) == (1 if t12_ready else 0),
        "AUXILIARY_EXPANSIONS_SEMANTIC artifact presence disagrees with readiness",
    )
    if t12_ready:
        artifact = obligation_records[0]
        require(
            artifact["artifact_kind"] == "auxiliary-expansion-proof",
            "AUXILIARY_EXPANSIONS_SEMANTIC: wrong artifact kind",
        )
        require(
            artifact["locator"] == OBLIGATION_LOCATOR,
            "AUXILIARY_EXPANSIONS_SEMANTIC: locator mismatch",
        )
        require(
            artifact["digest"] == proof_bank["auxiliary_semantics_proof_bank_sha256"],
            "AUXILIARY_EXPANSIONS_SEMANTIC: digest mismatch",
        )
        expected_support = sorted(
            item["artifact_id"]
            for item in obligation_exact["proof_artifacts"]
            if item["obligation_id"] == "FATE_TRANSITION_STATE_SEMANTICS"
        )
        require(
            artifact["support_artifact_ids"] == expected_support,
            "AUXILIARY_EXPANSIONS_SEMANTIC: exact T07 obligation support required",
        )

    target_results = {
        item["target_id"]: item for item in atomic_exact["target_result_records"]
    }
    require(
        int(target_results["T12_AUXILIARY_SEMANTICS"]["effective_target_complete"])
        == t12_ready,
        "T12_AUXILIARY_SEMANTICS completion disagrees with exact T12 bank",
    )
    target_artifact_by_id = {
        artifact["target_id"]: artifact
        for artifact in target_exact["atomic_target_artifacts"]
    }
    target_artifact = target_artifact_by_id.get("T12_AUXILIARY_SEMANTICS")
    if t12_ready:
        require(target_artifact is not None, "completed T12 target missing artifact")
        require(
            target_artifact["artifact_kind"] == "auxiliary-semantics-proof",
            "T12 target requires auxiliary-semantics-proof",
        )
        require(
            target_artifact["proof_locator"] == T12_TARGET_LOCATOR,
            "T12 target proof locator mismatch",
        )
        require(
            target_artifact["proof_digest"]
            == proof_bank["auxiliary_semantics_proof_bank_sha256"],
            "T12 target proof digest mismatch",
        )
    else:
        require(target_artifact is None, "open T12 target cannot contain target artifact")

    claims = {
        "expected_recurrent_blocks": len(records),
        "open_auxiliary_semantics_blocks": counts["open"],
        "proved_auxiliary_semantics_blocks": counts["proved"],
        "elimination_certificates": len(eliminations),
        "auxiliary_expansion_semantic_records": sum(
            len(item["expansion_semantic_records"]) for item in eliminations
        ),
        "eliminated_auxiliary_states": sum(
            item["eliminated_auxiliary_states"] for item in eliminations
        ),
        "selected_response_stability_records": sum(
            len(item["selected_response_stability_records"]) for item in eliminations
        ),
        "minimum_response_margin_gain": (
            min(item["minimum_response_margin_gain"] for item in eliminations)
            if eliminations
            else None
        ),
        "t07_fate_transition_state_ready": t07_ready,
        "t11_recurrent_block_closure_ready": t11_ready,
        "t12_auxiliary_semantics_ready": t12_ready,
        "exact_t11_common_weight_identity": 1,
        "exact_recursive_auxiliary_closure": 1,
        "exact_t07_edgewise_semantic_support": 1,
        "exact_selected_response_stability": 1,
        "exact_responsewise_load_monotonicity": 1,
        "noncircular_t12_bank_binding": 1,
        "all_n_proved_by_checker": 0,
        "open_block_ids": [
            record["block_id"] for record in records if record["status"] == "open"
        ],
        "auxiliary_semantics_records_sha256": catalogue.canonical_digest(records),
        "block_auxiliary_eliminations_sha256": catalogue.canonical_digest(eliminations),
        "auxiliary_semantics_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "auxiliary_semantics_proof_bank_sha256": proof_bank[
            "auxiliary_semantics_proof_bank_sha256"
        ],
        "obligation_artifact_registry_sha256": obligation_certificate["certificate_sha256"],
        "atomic_target_artifact_registry_sha256": target_registry["certificate_sha256"],
    }
    return {
        "auxiliary_semantics_records": records,
        "block_auxiliary_eliminations": eliminations,
        "auxiliary_semantics_artifacts": artifacts,
        "auxiliary_semantics_proof_bundles": proof_bundles,
        "auxiliary_semantics_proof_bank": proof_bank,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int | None]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "auxiliary_semantics_records",
        "block_auxiliary_eliminations",
        "auxiliary_semantics_artifacts",
        "auxiliary_semantics_proof_bundles",
        "auxiliary_semantics_proof_bank",
        "claims",
    ):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {
        key: value for key, value in certificate.items() if key != "certificate_sha256"
    }
    require(
        certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
        "certificate_sha256: incorrect",
    )
    claims = exact["claims"]
    return {
        "blocks": claims["expected_recurrent_blocks"],
        "proved": claims["proved_auxiliary_semantics_blocks"],
        "auxiliaries": claims["eliminated_auxiliary_states"],
        "stability_rows": claims["selected_response_stability_records"],
        "minimum_gain": claims["minimum_response_margin_gain"],
        "ready": claims["t12_auxiliary_semantics_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    t11_certificate: dict[str, Any],
    records: list[dict[str, Any]],
    eliminations: list[dict[str, Any]],
    artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "recurrent_block_closure_frontier_certificate": t11_certificate,
        "auxiliary_semantics_records": records,
        "block_auxiliary_eliminations": eliminations,
        "auxiliary_semantics_artifacts": artifacts,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_auxiliary_semantics_frontier.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
