#!/usr/bin/env python3
"""Validate the exact documentary T18 final row-theorem frontier.

The final row census is the canonical union of T12-eliminated recurrent rows and T15 interface rows.
Every theorem binds exact T17 predicates, fixed offsets, multiplicities, weights, margins and T16 rank
edges where required.  No independently supplied global quotient is accepted.  The checker validates
finite identity and support only and permanently reports all_n_proved_by_checker = 0.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import check_prime_power_acyclic_auxiliary_elimination as acyclic
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as target_artifacts
import check_prime_power_auxiliary_semantics_frontier_v2 as t12_frontier
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_component_scale_frontier as t14_frontier
import check_prime_power_fate_transition_state_frontier as t07_frontier
import check_prime_power_geometry_selector_frontier_v2 as t05_frontier
import check_prime_power_global_rank_frontier as t16_frontier
import check_prime_power_interface_exhaustiveness_frontier as t15_frontier
import check_prime_power_recurrent_block_closure_frontier as t11_frontier
import check_prime_power_state_equivalence_frontier as t13_frontier
import check_prime_power_state_predicate_frontier as t17_frontier
import check_prime_power_transition_resource_frontier as t10_frontier


class RowTheoremFrontierError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RowTheoremFrontierError(message)


def text(value: Any, path: str) -> str:
    require(isinstance(value, str) and value, f"{path}: nonempty string required")
    return value


def exact_ids(value: Any, expected: list[str], path: str) -> list[str]:
    require(isinstance(value, list) and value == expected, f"{path}: exact list required")
    require(value == sorted(value) and len(value) == len(set(value)), f"{path}: canonical IDs required")
    return list(value)


def aggregate_targets(items: list[list[Any]], local_to_global: dict[str, str]) -> list[dict[str, Any]]:
    counts: Counter[str] = Counter()
    for local_state, multiplicity in items:
        require(local_state in local_to_global and type(multiplicity) is int and multiplicity > 0,
                "recurrent target: valid local state and positive multiplicity required")
        counts[local_to_global[local_state]] += multiplicity
    return [{"global_state_id": state, "multiplicity": counts[state]} for state in sorted(counts)]


def final_weight_maps(t14_exact: dict[str, Any], t15_exact: dict[str, Any]) -> tuple[dict[str, int], dict[str, str]]:
    multiplier = {item["component_id"]: item["interface_multiplier"]
                  for item in t15_exact["interface_component_multiplier_records"]}
    weights: dict[str, int] = {}
    components: dict[str, str] = {}
    for item in t14_exact["global_component_weight_records"]:
        component = item["component_id"]
        require(component in multiplier, f"component {component}: missing T15 multiplier")
        state = item["global_state_id"]
        weights[state] = multiplier[component] * item["component_weight"]
        components[state] = component
    return weights, components


def recurrent_subjects(*, t11_exact: dict[str, Any], t12_exact: dict[str, Any],
                       t13_exact: dict[str, Any], t14_exact: dict[str, Any],
                       t15_exact: dict[str, Any]) -> list[dict[str, Any]]:
    links = {(item["block_id"], item["local_state_id"]): item["global_state_id"]
             for item in t13_exact["local_to_global_state_links"]}
    final_weight, component_by_state = final_weight_maps(t14_exact, t15_exact)
    common_by_block = {item["block_id"]: item
                       for item in t11_exact["recurrent_block_common_weight_records"]}
    output = []
    for elimination in t12_exact["block_auxiliary_eliminations"]:
        block_id = elimination["block_id"]
        common = common_by_block[block_id]
        bridge_by_key = {(item["local_parent_state_id"], item["fibre_id"]): item
                         for item in common["row_bridge_records"]}
        local_weights = {item["state_id"]: item["weight"] for item in common["state_weights"]}
        exact = acyclic.exact_certificate(elimination["acyclic_auxiliary_elimination_certificate"])
        local_to_global = {local: global_id for (block, local), global_id in links.items()
                           if block == block_id}
        for row in exact["eliminated_row_records"]:
            key = (row["parent_state_id"], row["fibre_id"])
            require(key in bridge_by_key, f"block {block_id}: recurrent row bridge missing")
            bridge = bridge_by_key[key]
            parent_local = row["parent_state_id"]
            require(parent_local in local_to_global and parent_local in local_weights,
                    f"block {block_id}: recurrent parent identity missing")
            parent_global = local_to_global[parent_local]
            require(parent_global in final_weight, f"state {parent_global}: final weight missing")
            require(final_weight[parent_global] % local_weights[parent_local] == 0,
                    f"row {bridge['row_id']}: nonintegral final scaling")
            scale = final_weight[parent_global] // local_weights[parent_local]
            targets = aggregate_targets(row["selected_child_vector"], local_to_global)
            target_weight = sum(item["multiplicity"] * final_weight[item["global_state_id"]]
                                for item in targets)
            fixed = scale * row["selected_net_fixed_offset"]
            load = scale * row["selected_row_load"]
            margin = scale * row["selected_margin"]
            require(load == fixed + target_weight and margin == final_weight[parent_global] - load
                    and margin > 0, f"row {bridge['row_id']}: recurrent scaled arithmetic mismatch")
            core = {
                "source_kind": "recurrent",
                "row_id": bridge["row_id"],
                "block_id": block_id,
                "parent_global_state_id": parent_global,
                "selected_slot_id": bridge["selected_slot_id"],
                "fibre_id": bridge["fibre_id"],
                "t11_row_bridge_sha256": bridge["common_weight_row_bridge_sha256"],
                "t12_row_elimination_sha256": row["row_elimination_sha256"],
                "t12_block_elimination_sha256": elimination["block_auxiliary_elimination_sha256"],
                "selected_response_sha256": catalogue.canonical_digest(row["selected_response"]),
                "scale_multiplier": scale,
                "parent_final_global_weight": final_weight[parent_global],
                "parent_component_id": component_by_state[parent_global],
                "fixed_offset": fixed,
                "target_semantics": targets,
                "target_weight": target_weight,
                "row_load": load,
                "margin": margin,
                "classification": "strict",
            }
            item = {"final_row_id": f"final-row::recurrent::{bridge['row_id']}", **core}
            item["final_row_subject_sha256"] = catalogue.canonical_digest(item)
            output.append(item)
    return output


def interface_subjects(t15_exact: dict[str, Any]) -> list[dict[str, Any]]:
    output = []
    for row in t15_exact["interface_row_semantic_certificates"]:
        targets = [{"global_state_id": item["global_state_id"], "multiplicity": item["multiplicity"]}
                   for item in row["target_semantics"]]
        core = {
            "source_kind": "interface",
            "row_id": row["row_id"],
            "block_id": None,
            "parent_global_state_id": row["parent_global_state_id"],
            "selected_slot_id": row["operation_slot_id"],
            "fibre_id": None,
            "t15_interface_row_semantic_sha256": row["interface_row_semantic_certificate_sha256"],
            "parent_final_global_weight": row["parent_final_global_weight"],
            "parent_component_id": row["parent_component_id"],
            "fixed_offset": row["fixed_offset"],
            "target_semantics": targets,
            "target_weight": row["target_weight"],
            "row_load": row["row_load"],
            "margin": row["margin"],
            "classification": "strict" if row["classification"] == "strict" else "critical-descending",
        }
        item = {"final_row_id": f"final-row::interface::{row['row_id']}", **core}
        item["final_row_subject_sha256"] = catalogue.canonical_digest(item)
        output.append(item)
    return output


def exact_status(raw: dict[str, Any], subject: dict[str, Any]) -> dict[str, Any]:
    row_id = subject["final_row_id"]
    require(raw.get("final_row_id") == row_id
            and raw.get("final_row_subject_sha256") == subject["final_row_subject_sha256"],
            f"row {row_id}: subject mismatch")
    theorem_id = text(raw.get("theorem_id"), f"row {row_id} theorem_id")
    status = raw.get("status")
    require(status in {"open", "proved"}, f"row {row_id}: open/proved required")
    locator, digest = raw.get("verification_locator"), raw.get("verification_digest")
    if status == "open":
        require(locator is None and digest is None, f"row {row_id}: open requires null verification")
    else:
        require(locator == f"global-row-theorem-registry://{row_id}"
                and isinstance(digest, str) and digest,
                f"row {row_id}: canonical proved verification required")
    core = {"final_row_id": row_id,
            "final_row_subject_sha256": subject["final_row_subject_sha256"],
            "theorem_id": theorem_id, "status": status,
            "verification_locator": locator,
            "note": text(raw.get("note"), f"row {row_id} note")}
    output = {**core, "verification_digest": digest,
              "final_row_theorem_record_core_sha256": catalogue.canonical_digest(core)}
    output["final_row_theorem_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_semantic(raw: dict[str, Any], *, subject: dict[str, Any], record: dict[str, Any],
                   predicates: dict[str, dict[str, Any]], critical_edges: list[dict[str, Any]]) -> dict[str, Any]:
    row_id = subject["final_row_id"]
    require(raw.get("final_row_id") == row_id and raw.get("theorem_id") == record["theorem_id"],
            f"row {row_id}: semantic identity mismatch")
    parent = subject["parent_global_state_id"]
    require(parent in predicates, f"row {row_id}: parent predicate missing")
    target_predicates = []
    for target in subject["target_semantics"]:
        state = target["global_state_id"]
        require(state in predicates, f"row {row_id}: target predicate missing for {state}")
        target_predicates.append({
            "global_state_id": state,
            "predicate_id": predicates[state]["predicate_id"],
            "global_state_predicate_semantic_sha256": predicates[state][
                "global_state_predicate_semantic_sha256"],
            "multiplicity": target["multiplicity"],
        })
    require(raw.get("target_predicate_multiplicities") == target_predicates,
            f"row {row_id}: exact target predicate multiset required")
    expected_edges = sorted(item["critical_edge_id"] for item in critical_edges)
    exact_ids(raw.get("critical_edge_ids"), expected_edges, f"row {row_id} critical edges")
    if subject["classification"] == "critical-descending":
        require(expected_edges and len(expected_edges) == len(subject["target_semantics"]),
                f"row {row_id}: every critical target requires T16 descent")
    else:
        require(not expected_edges, f"row {row_id}: strict row must not use T16 critical edges")
    output = {
        "final_row_id": row_id,
        "final_row_subject_sha256": subject["final_row_subject_sha256"],
        "theorem_id": record["theorem_id"],
        "source_kind": subject["source_kind"],
        "parent_global_state_id": parent,
        "parent_predicate_id": predicates[parent]["predicate_id"],
        "parent_predicate_semantic_sha256": predicates[parent][
            "global_state_predicate_semantic_sha256"],
        "fixed_offset": subject["fixed_offset"],
        "target_predicate_multiplicities": target_predicates,
        "row_load": subject["row_load"],
        "margin": subject["margin"],
        "classification": subject["classification"],
        "critical_edge_ids": expected_edges,
        "row_theorem_statement": text(raw.get("row_theorem_statement"), f"row {row_id} theorem"),
        "fixed_offset_interpretation": text(raw.get("fixed_offset_interpretation"),
                                            f"row {row_id} fixed-offset interpretation"),
        "external_recurrence_statement": text(raw.get("external_recurrence_statement"),
                                              f"row {row_id} recurrence statement"),
        "evidence": text(raw.get("evidence"), f"row {row_id} evidence"),
    }
    output["global_row_theorem_semantic_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_artifact(raw: dict[str, Any], *, row_id: str, semantic: dict[str, Any], support: list[str]) -> dict[str, Any]:
    require(raw.get("final_row_id") == row_id
            and raw.get("artifact_kind") == "global-row-theorem-proof",
            f"row {row_id}: artifact identity/kind mismatch")
    exact_ids(raw.get("support_artifact_ids"), support, f"row {row_id} support")
    require(raw.get("global_row_theorem_semantic_sha256")
            == semantic["global_row_theorem_semantic_sha256"],
            f"row {row_id}: artifact semantic mismatch")
    output = {
        "final_row_id": row_id,
        "artifact_id": text(raw.get("artifact_id"), f"row {row_id} artifact ID"),
        "artifact_kind": "global-row-theorem-proof",
        "global_row_theorem_semantic_sha256": semantic["global_row_theorem_semantic_sha256"],
        "proof_locator": text(raw.get("proof_locator"), f"row {row_id} proof locator"),
        "proof_digest": text(raw.get("proof_digest"), f"row {row_id} proof digest"),
        "proof_statement": text(raw.get("proof_statement"), f"row {row_id} proof statement"),
        "support_artifact_ids": support,
        "evidence": text(raw.get("evidence"), f"row {row_id} artifact evidence"),
    }
    require(output["artifact_id"] not in support, f"row {row_id}: self support")
    output["global_row_theorem_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    t17_certificate = certificate.get("state_predicate_frontier_certificate")
    require(isinstance(t17_certificate, dict), "state_predicate_frontier_certificate: object required")
    for name in ("final_row_theorem_records", "global_row_theorem_semantic_certificates",
                 "global_row_theorem_artifacts", "global_row_theorem_proof_bundles"):
        require(isinstance(certificate.get(name), list), f"{name}: list required")
    t17_frontier.validate_certificate(t17_certificate)
    t17_exact = t17_frontier.exact_certificate(t17_certificate)
    t16_certificate = t17_certificate["global_rank_frontier_certificate"]
    t16_frontier.validate_certificate(t16_certificate)
    t16_exact = t16_frontier.exact_certificate(t16_certificate)
    t15_certificate = t16_certificate["interface_exhaustiveness_frontier_certificate"]
    t15_frontier.validate_certificate(t15_certificate)
    t15_exact = t15_frontier.exact_certificate(t15_certificate)
    t14_certificate = t15_certificate["component_scale_frontier_certificate"]
    t14_frontier.validate_certificate(t14_certificate)
    t14_exact = t14_frontier.exact_certificate(t14_certificate)
    t13_certificate = t14_certificate["state_equivalence_frontier_certificate"]
    t13_frontier.validate_certificate(t13_certificate)
    t13_exact = t13_frontier.exact_certificate(t13_certificate)
    t12_certificate = t15_certificate["auxiliary_semantics_frontier_certificate"]
    t12_frontier.validate_certificate(t12_certificate)
    t12_exact = t12_frontier.exact_certificate(t12_certificate)
    t11_certificate = t12_certificate["recurrent_block_closure_frontier_certificate"]
    t11_frontier.validate_certificate(t11_certificate)
    t11_exact = t11_frontier.exact_certificate(t11_certificate)
    t10_certificate = t11_certificate["transition_resource_frontier_certificate"]
    t10_frontier.validate_certificate(t10_certificate)
    t10_exact = t10_frontier.exact_certificate(t10_certificate)
    t06_certificate = t10_certificate["candidate_policy_frontier_certificate"]
    t05_certificate = t06_certificate["geometry_selector_frontier_certificate"]
    t07_certificate = t06_certificate["fate_transition_state_frontier_certificate"]
    t05_frontier.validate_certificate(t05_certificate)
    t05_exact = t05_frontier.exact_certificate(t05_certificate)
    t07_frontier.validate_certificate(t07_certificate)
    t07_exact = t07_frontier.exact_certificate(t07_certificate)

    subjects = recurrent_subjects(t11_exact=t11_exact, t12_exact=t12_exact, t13_exact=t13_exact,
                                  t14_exact=t14_exact, t15_exact=t15_exact)
    subjects.extend(interface_subjects(t15_exact))
    subjects.sort(key=lambda item: item["final_row_id"])
    require(len({item["final_row_id"] for item in subjects}) == len(subjects),
            "final row subjects: duplicate ID")

    raw_records = certificate["final_row_theorem_records"]
    require(len(raw_records) == len(subjects)
            and [item.get("final_row_id") for item in raw_records]
            == [item["final_row_id"] for item in subjects],
            "final_row_theorem_records: exact derived order required")
    records = [exact_status(raw, subject) for raw, subject in zip(raw_records, subjects)]
    require(raw_records == records, "final_row_theorem_records: noncanonical")
    theorem_ids = [item["theorem_id"] for item in records]
    require(len(theorem_ids) == len(set(theorem_ids)), "T18 theorem IDs duplicate")
    record_by_id = {item["final_row_id"]: item for item in records}

    predicate_by_state = {item["global_state_id"]: item
                          for item in t17_exact["global_state_predicate_semantic_certificates"]}
    predicate_artifact_by_state = {item["global_state_id"]: item["artifact_id"]
                                   for item in t17_exact["global_state_predicate_artifacts"]}
    edge_subject_by_id = {item["critical_edge_id"]: item for item in t16_exact["critical_edge_subjects"]}
    edge_record_by_id = {item["critical_edge_id"]: item for item in t16_exact["critical_edge_records"]}
    edge_artifact_by_id = {item["critical_edge_id"]: item["artifact_id"]
                           for item in t16_exact["critical_edge_artifacts"]}
    critical_by_row: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for edge_id, edge in edge_subject_by_id.items():
        require(edge_id in edge_record_by_id and edge_record_by_id[edge_id]["status"] == "proved"
                and edge_id in edge_artifact_by_id, f"T16 edge {edge_id}: proved data required")
        critical_by_row[edge["row_id"]].append(edge)

    semantic_groups = {item["final_row_id"]: [] for item in subjects}
    for raw in certificate["global_row_theorem_semantic_certificates"]:
        require(raw.get("final_row_id") in semantic_groups, "T18 semantic: unknown row")
        semantic_groups[raw["final_row_id"]].append(raw)
    semantics = []
    semantic_by_id = {}
    for subject in subjects:
        row_id = subject["final_row_id"]
        record = record_by_id[row_id]
        group = semantic_groups[row_id]
        if record["status"] == "open":
            require(not group, f"row {row_id}: open theorem has semantic")
            continue
        require(len(group) == 1, f"row {row_id}: exactly one theorem semantic required")
        critical = critical_by_row.get(subject["row_id"], []) if subject["source_kind"] == "interface" else []
        semantic = exact_semantic(group[0], subject=subject, record=record,
                                  predicates=predicate_by_state, critical_edges=critical)
        semantics.append(semantic)
        semantic_by_id[row_id] = semantic
    require(certificate["global_row_theorem_semantic_certificates"] == semantics,
            "global_row_theorem_semantic_certificates: noncanonical")

    t05_artifact_by_slot = {item["slot_id"]: item["artifact_id"]
                            for item in t05_exact["slot_geometry_selector_artifacts"]}
    t07_artifact_by_slot = {item["slot_id"]: item["artifact_id"]
                            for item in t07_exact["slot_fate_transition_state_artifacts"]}
    t10_artifact_by_row = {item["row_id"]: item["artifact_id"]
                           for item in t10_exact["routed_credit_semantic_artifacts"]}
    t11_common_by_block = {item["block_id"]: item["artifact_id"]
                           for item in t11_exact["recurrent_block_common_weight_artifacts"]}
    t11_closure_by_block = {item["block_id"]: item["artifact_id"]
                            for item in t11_exact["recurrent_block_closure_artifacts"]}
    t12_artifact_by_block = {item["block_id"]: item["artifact_id"]
                             for item in t12_exact["auxiliary_semantics_artifacts"]}
    t14_artifact_by_component = {item["component_id"]: item["artifact_id"]
                                 for item in t14_exact["component_scale_artifacts"]}
    t15_artifact_by_row = {item["row_id"]: item["artifact_id"]
                           for item in t15_exact["interface_row_artifacts"]}
    scale_artifact = t15_exact["interface_component_scale_artifact"]
    require(scale_artifact is not None, "T18 requires T15 interface scale artifact")

    artifact_groups = {item["final_row_id"]: [] for item in subjects}
    for raw in certificate["global_row_theorem_artifacts"]:
        require(raw.get("final_row_id") in artifact_groups, "T18 artifact: unknown row")
        artifact_groups[raw["final_row_id"]].append(raw)
    artifacts = []
    bundles = []
    for subject in subjects:
        row_id = subject["final_row_id"]
        record = record_by_id[row_id]
        group = artifact_groups[row_id]
        if record["status"] == "open":
            require(not group, f"row {row_id}: open theorem has artifact")
            continue
        support = {scale_artifact["artifact_id"],
                   predicate_artifact_by_state[subject["parent_global_state_id"]]}
        support.update(predicate_artifact_by_state[item["global_state_id"]]
                       for item in subject["target_semantics"])
        components = {subject["parent_component_id"]}
        components.update(next(item["component_id"] for item in t14_exact["global_component_weight_records"]
                               if item["global_state_id"] == target["global_state_id"])
                          for target in subject["target_semantics"])
        support.update(t14_artifact_by_component[item] for item in components)
        slot = subject["selected_slot_id"]
        support.add(t07_artifact_by_slot[slot])
        if subject["source_kind"] == "recurrent":
            block = subject["block_id"]
            support.update({t05_artifact_by_slot[slot], t10_artifact_by_row[subject["row_id"]],
                            t11_common_by_block[block], t11_closure_by_block[block],
                            t12_artifact_by_block[block]})
        else:
            support.add(t15_artifact_by_row[subject["row_id"]])
            for edge in critical_by_row.get(subject["row_id"], []):
                support.add(edge_artifact_by_id[edge["critical_edge_id"]])
        support_ids = sorted(support)
        require(len(group) == 1, f"row {row_id}: exactly one theorem artifact required")
        artifact = exact_artifact(group[0], row_id=row_id,
                                  semantic=semantic_by_id[row_id], support=support_ids)
        artifacts.append(artifact)
        bundle = {"final_row_id": row_id,
                  "final_row_theorem_record_core_sha256": record[
                      "final_row_theorem_record_core_sha256"],
                  "global_row_theorem_semantic_sha256": semantic_by_id[row_id][
                      "global_row_theorem_semantic_sha256"],
                  "global_row_theorem_artifact_sha256": artifact[
                      "global_row_theorem_artifact_sha256"],
                  "support_artifact_ids": support_ids}
        bundle["global_row_theorem_proof_bundle_sha256"] = catalogue.canonical_digest(bundle)
        require(record["verification_digest"] == bundle["global_row_theorem_proof_bundle_sha256"],
                f"row {row_id}: verification digest mismatch")
        bundles.append(bundle)
    require(certificate["global_row_theorem_artifacts"] == artifacts,
            "global_row_theorem_artifacts: noncanonical")
    require(certificate["global_row_theorem_proof_bundles"] == bundles,
            "global_row_theorem_proof_bundles: incorrect")
    artifact_ids = [item["artifact_id"] for item in artifacts]
    require(len(artifact_ids) == len(set(artifact_ids)), "T18 artifact IDs duplicate")

    counts = Counter(item["status"] for item in records)
    upstream_ready = all((t05_exact["claims"]["geometry_selector_correct_ready"],
                          t07_exact["claims"]["fate_transition_state_semantics_ready"],
                          t10_exact["claims"]["t10_routed_credit_semantics_ready"],
                          t11_exact["claims"]["t11_recurrent_block_closure_ready"],
                          t12_exact["claims"]["t12_auxiliary_semantics_ready"],
                          t14_exact["claims"]["t14_component_scales_ready"],
                          t15_exact["claims"]["t15_interface_exhaustiveness_ready"],
                          t16_exact["claims"]["t16_global_rank_ready"],
                          t17_exact["claims"]["t17_state_predicates_ready"]))
    ready = int(upstream_ready and counts["proved"] == len(records)
                and len(semantics) == len(records) and len(artifacts) == len(records))
    bank = {
        "t05_geometry_selector_proof_bank_sha256": t05_exact["claims"][
            "geometry_selector_frontier_proof_bank_sha256"],
        "t07_state_semantics_proof_bank_sha256": t07_exact["claims"]["state_semantics_proof_bank_sha256"],
        "t10_routed_credit_proof_bank_sha256": t10_exact["claims"][
            "routed_credit_semantics_proof_bank_sha256"],
        "t11_recurrent_block_proof_bank_sha256": t11_exact["claims"][
            "t11_recurrent_block_closure_proof_bank_sha256"],
        "t12_auxiliary_semantics_proof_bank_sha256": t12_exact["claims"][
            "auxiliary_semantics_proof_bank_sha256"],
        "t14_component_scale_proof_bank_sha256": t14_exact["claims"][
            "component_scale_frontier_proof_bank_sha256"],
        "t15_interface_proof_bank_sha256": t15_exact["claims"][
            "interface_exhaustiveness_frontier_proof_bank_sha256"],
        "t16_global_rank_proof_bank_sha256": t16_exact["claims"][
            "global_rank_frontier_proof_bank_sha256"],
        "t17_state_predicate_proof_bank_sha256": t17_exact["claims"][
            "state_predicate_frontier_proof_bank_sha256"],
        "final_row_subjects_sha256": catalogue.canonical_digest(subjects),
        "final_row_theorem_records_sha256": catalogue.canonical_digest(records),
        "global_row_theorem_semantic_certificates_sha256": catalogue.canonical_digest(semantics),
        "global_row_theorem_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "global_row_theorem_proof_bundles_sha256": catalogue.canonical_digest(bundles),
    }
    bank["row_theorem_frontier_proof_bank_sha256"] = catalogue.canonical_digest(bank)

    t13_t04 = t13_certificate["fate_transition_state_frontier_certificate"][
        "block_interface_population_frontier_certificate"]
    registry = t13_t04["atomic_target_artifact_registry_certificate"]
    target_artifacts.validate_certificate(registry)
    target_exact = target_artifacts.exact_certificate(registry)
    atomic_certificate = registry["current_frontier_execution_certificate"][
        "atomic_frontier_execution_certificate"]
    atomic.validate_certificate(atomic_certificate)
    atomic_exact = atomic.exact_certificate(atomic_certificate)
    results = {item["target_id"]: item for item in atomic_exact["target_result_records"]}
    require(int(results["T18_ROW_THEOREMS"]["effective_target_complete"]) == ready,
            "T18 atomic completion mismatch")
    target = {item["target_id"]: item for item in target_exact["atomic_target_artifacts"]}.get(
        "T18_ROW_THEOREMS")
    if ready:
        require(target is not None and target["artifact_kind"] == "global-row-theorem-proof"
                and target["proof_locator"] == "row-theorem-frontier://T18_ROW_THEOREMS"
                and target["proof_digest"] == bank["row_theorem_frontier_proof_bank_sha256"],
                "T18 target artifact mismatch")
    else:
        require(target is None, "open T18 target has artifact")

    claims = {
        "final_rows": len(subjects),
        "recurrent_final_rows": sum(item["source_kind"] == "recurrent" for item in subjects),
        "interface_final_rows": sum(item["source_kind"] == "interface" for item in subjects),
        "strict_final_rows": sum(item["classification"] == "strict" for item in subjects),
        "critical_descending_final_rows": sum(item["classification"] == "critical-descending"
                                               for item in subjects),
        "open_final_row_theorems": counts["open"],
        "proved_final_row_theorems": counts["proved"],
        "t18_row_theorems_ready": ready,
        "exact_t12_recurrent_row_census": 1,
        "exact_t15_interface_row_census": 1,
        "exact_t17_predicate_multisets": 1,
        "exact_t16_critical_edge_binding": 1,
        "legacy_parallel_global_quotient_excluded": 1,
        "noncircular_t18_bank_binding": 1,
        "all_n_proved_by_checker": 0,
        "open_final_row_ids": [item["final_row_id"] for item in records if item["status"] == "open"],
        "row_theorem_frontier_proof_bank_sha256": bank["row_theorem_frontier_proof_bank_sha256"],
    }
    return {"final_row_subjects": subjects,
            "final_row_theorem_records": records,
            "global_row_theorem_semantic_certificates": semantics,
            "global_row_theorem_artifacts": artifacts,
            "global_row_theorem_proof_bundles": bundles,
            "row_theorem_frontier_proof_bank": bank,
            "claims": claims}


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
    return {"rows": claims["final_rows"], "recurrent": claims["recurrent_final_rows"],
            "interface": claims["interface_final_rows"], "proved": claims["proved_final_row_theorems"],
            "ready": claims["t18_row_theorems_ready"], "all_n": 0}


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_row_theorem_frontier.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
