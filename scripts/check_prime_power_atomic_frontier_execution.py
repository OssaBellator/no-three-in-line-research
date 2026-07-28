#!/usr/bin/env python3
"""Validate exact execution coverage for every current all-n research frontier.

The checker fixes forty-three atomic proof targets, separates provisional research-start dependencies
from proof-closure dependencies, binds completed targets to obligations, premises, handoff assertions
and the final dossier gate, and permanently reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import heapq
import json
import sys
from collections import Counter, deque
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_final_dossier_integrity as dossier
import check_prime_power_final_implication_premise_contract as contract
import check_prime_power_final_induction_handoff as handoff


class AtomicFrontierExecutionError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AtomicFrontierExecutionError(message)


def ids(text: str) -> tuple[str, ...]:
    return tuple(text.split()) if text else ()


FRONTIERS: dict[str, str] = {
    "F01_SOURCE_RULE": "source truth and exhaustive recurrence skeleton",
    "F02_POPULATION": "complete genuine slot, candidate, block and interface population",
    "F03_GEOMETRY_POLICY": "geometry, selectors and candidate policy",
    "F04_TRANSITION_RESOURCE": "fate, transition, state, active-row, resource and credit semantics",
    "F05_RECURRENT_BLOCKS": "closed strongly connected recurrent blocks with strict common weights",
    "F06_AUXILIARIES": "semantic recursive auxiliary expansion and elimination",
    "F07_CROSS_BLOCK_SEMANTICS": "cross-block identity, scales, state predicates and row theorems",
    "F08_INTERFACE_RANK": "complete interface family and well-founded global rank",
    "F09_TYPED_SUPPORT": "genuine typed semantic and premise artifacts with noncircular support",
    "F10_GLOBAL_FAMILY": "skeleton-derived global-family exhaustiveness",
    "F11_EXCEPTIONAL_CORE": "zero-selector exceptional rows and the twenty-chamber hard core",
    "F12_FINAL_PREMISES_HANDOFF": "ten final premises, six handoff assertions and final audit",
    "F13_ROOT_IMPLICATION": "reviewed implication from the global quotient to D(n)=2n",
}

TARGET_ROWS = [
("T01_SOURCE_STATEMENTS","F01_SOURCE_RULE","prove every cited source statement","source-truth-proof","","","SOURCE_STATEMENTS_TRUE","","",0),
("T02_RULE_EXHAUSTIVENESS","F01_SOURCE_RULE","prove the genuine recurrence rule exhaustive","rule-exhaustiveness-proof","T01_SOURCE_STATEMENTS","T01_SOURCE_STATEMENTS","RULE_EXHAUSTIVE","","",0),
("T03_SLOT_CANDIDATE_POPULATION","F02_POPULATION","populate every genuine operation slot and candidate family","population-proof","T02_RULE_EXHAUSTIVENESS","","SLOT_AND_CANDIDATE_POPULATION","","",0),
("T04_BLOCK_INTERFACE_POPULATION","F02_POPULATION","populate every recurrent block and return/interface row","global-population-bank","T03_SLOT_CANDIDATE_POPULATION","T03_SLOT_CANDIDATE_POPULATION","","","",0),
("T05_GEOMETRY_SELECTORS","F03_GEOMETRY_POLICY","prove real geometry, thresholds and selectors","geometry-selector-proof","T03_SLOT_CANDIDATE_POPULATION T04_BLOCK_INTERFACE_POPULATION","","GEOMETRY_SELECTOR_CORRECT","","",0),
("T06_CANDIDATE_POLICY","F03_GEOMETRY_POLICY","prove the complete candidate minimization policy","candidate-policy-proof","T05_GEOMETRY_SELECTORS T07_FATE_TRANSITION_STATE","T05_GEOMETRY_SELECTORS","CANDIDATE_POLICY_CORRECT","","",0),
("T07_FATE_TRANSITION_STATE","F04_TRANSITION_RESOURCE","prove fate, transition and state semantics","transition-state-proof","T03_SLOT_CANDIDATE_POPULATION T04_BLOCK_INTERFACE_POPULATION","","FATE_TRANSITION_STATE_SEMANTICS","","",0),
("T08_ACTIVE_ROW_FAMILY","F04_TRANSITION_RESOURCE","prove the simultaneous active row family exhaustive","active-family-proof","T06_CANDIDATE_POLICY","T07_FATE_TRANSITION_STATE","ACTIVE_ROW_FAMILY_EXHAUSTIVE","","",0),
("T09_RESOURCE_MODEL","F04_TRANSITION_RESOURCE","prove the destroyed-resource model exhaustive","resource-model-proof","T05_GEOMETRY_SELECTORS T08_ACTIVE_ROW_FAMILY","T08_ACTIVE_ROW_FAMILY","DESTROYED_RESOURCE_MODEL_EXHAUSTIVE","","",0),
("T10_CREDIT_ROUTING","F04_TRANSITION_RESOURCE","prove routed-credit semantics","credit-routing-proof","T07_FATE_TRANSITION_STATE T09_RESOURCE_MODEL","T09_RESOURCE_MODEL","CREDIT_ROUTING_SEMANTIC","","",0),
("T11_RECURRENT_BLOCK_CLOSURE","F05_RECURRENT_BLOCKS","prove every recurrent block closed, strongly connected and strict","block-closure-proof","T04_BLOCK_INTERFACE_POPULATION T06_CANDIDATE_POLICY T10_CREDIT_ROUTING","","CLOSED_STRICT_RECURRENT_BLOCKS","","",0),
("T12_AUXILIARY_SEMANTICS","F06_AUXILIARIES","prove and eliminate every recursive auxiliary expansion","auxiliary-semantics-proof","T07_FATE_TRANSITION_STATE T11_RECURRENT_BLOCK_CLOSURE","T11_RECURRENT_BLOCK_CLOSURE","AUXILIARY_EXPANSIONS_SEMANTIC","","",0),
("T13_STATE_EQUIVALENCE","F07_CROSS_BLOCK_SEMANTICS","prove every cross-block state equivalence","state-equivalence-proof","T07_FATE_TRANSITION_STATE","","CROSS_BLOCK_STATE_IDENTITY_SEMANTIC","","",0),
("T14_COMPONENT_SCALES","F07_CROSS_BLOCK_SEMANTICS","prove every cross-block component scale","component-scale-proof","T11_RECURRENT_BLOCK_CLOSURE T13_STATE_EQUIVALENCE","T13_STATE_EQUIVALENCE","COMPONENT_SCALE_SEMANTIC","","",0),
("T15_INTERFACE_EXHAUSTIVENESS","F08_INTERFACE_RANK","prove every return and interface row present","interface-exhaustiveness-proof","T04_BLOCK_INTERFACE_POPULATION T07_FATE_TRANSITION_STATE T12_AUXILIARY_SEMANTICS T14_COMPONENT_SCALES","T12_AUXILIARY_SEMANTICS T14_COMPONENT_SCALES","INTERFACE_RETURN_ROWS_EXHAUSTIVE","","",0),
("T16_GLOBAL_RANK","F08_INTERFACE_RANK","prove the global rank genuinely well-founded","rank-well-foundedness-proof","T15_INTERFACE_EXHAUSTIVENESS","T15_INTERFACE_EXHAUSTIVENESS","GLOBAL_RANK_WELL_FOUNDED","","",0),
("T17_STATE_PREDICATES","F07_CROSS_BLOCK_SEMANTICS","prove every global-state predicate","global-state-predicate-proof","T13_STATE_EQUIVALENCE T16_GLOBAL_RANK","T13_STATE_EQUIVALENCE","","","",0),
("T18_ROW_THEOREMS","F07_CROSS_BLOCK_SEMANTICS","prove every final quotient row theorem and fixed-offset interpretation","global-row-theorem-proof","T05_GEOMETRY_SELECTORS T07_FATE_TRANSITION_STATE T10_CREDIT_ROUTING T11_RECURRENT_BLOCK_CLOSURE T12_AUXILIARY_SEMANTICS T14_COMPONENT_SCALES T15_INTERFACE_EXHAUSTIVENESS T16_GLOBAL_RANK T17_STATE_PREDICATES","T17_STATE_PREDICATES","","","",0),
("T19_GLOBAL_FAMILY","F10_GLOBAL_FAMILY","prove the skeleton-derived global family exhaustive","global-family-proof","T02_RULE_EXHAUSTIVENESS T11_RECURRENT_BLOCK_CLOSURE T15_INTERFACE_EXHAUSTIVENESS","","EXPECTED_GLOBAL_FAMILY_EXHAUSTIVE","","",0),
("T20_EXCEPTIONAL_ZERO_ROWS","F11_EXCEPTIONAL_CORE","close all zero-selector exceptional rows","exceptional-zero-proof","T05_GEOMETRY_SELECTORS T10_CREDIT_ROUTING T15_INTERFACE_EXHAUSTIVENESS","","EXCEPTIONAL_ZERO_ROWS_CLOSED","","",0),
("T21_HARD_CORE_ROWS","F11_EXCEPTIONAL_CORE","close the complete twenty-chamber hard core","hard-core-proof","T05_GEOMETRY_SELECTORS T10_CREDIT_ROUTING T15_INTERFACE_EXHAUSTIVENESS","","HARD_CORE_ROWS_CLOSED","","",0),
("T22_BASE_CASES_PREMISE","F12_FINAL_PREMISES_HANDOFF","prove the complete base-case premise","base-case-domain-proof","T01_SOURCE_STATEMENTS","","","BASE_CASES_COMPLETE","",0),
("T23_RECURRENCE_PREMISE","F12_FINAL_PREMISES_HANDOFF","prove the recurrence-exhaustiveness premise","recurrence-premise-proof","T02_RULE_EXHAUSTIVENESS T19_GLOBAL_FAMILY","","","RECURRENCE_EXHAUSTIVE","",0),
("T24_INVARIANT_PREMISE","F12_FINAL_PREMISES_HANDOFF","prove the state-invariant premise","invariant-premise-proof","T05_GEOMETRY_SELECTORS T07_FATE_TRANSITION_STATE","","","STATE_INVARIANTS_PRESERVED","",0),
("T25_SELECTION_PREMISE","F12_FINAL_PREMISES_HANDOFF","prove the operation-selection premise","selection-premise-proof","T03_SLOT_CANDIDATE_POPULATION T06_CANDIDATE_POLICY","","","OPERATION_SELECTION_SOUND","",0),
("T26_RESOURCE_PREMISE","F12_FINAL_PREMISES_HANDOFF","prove the resource-and-credit premise","resource-credit-premise-proof","T08_ACTIVE_ROW_FAMILY T09_RESOURCE_MODEL T10_CREDIT_ROUTING","","","RESOURCE_AND_CREDIT_SOUND","",0),
("T27_CONTRACTION_PREMISE","F12_FINAL_PREMISES_HANDOFF","prove the block-and-auxiliary contraction premise","contraction-premise-proof","T11_RECURRENT_BLOCK_CLOSURE T12_AUXILIARY_SEMANTICS","","","BLOCK_AND_AUXILIARY_CONTRACTION","",0),
("T28_CROSS_BLOCK_PREMISE","F12_FINAL_PREMISES_HANDOFF","prove the cross-block assembly premise","cross-block-premise-proof","T13_STATE_EQUIVALENCE T14_COMPONENT_SCALES T15_INTERFACE_EXHAUSTIVENESS T16_GLOBAL_RANK T17_STATE_PREDICATES T18_ROW_THEOREMS","","","CROSS_BLOCK_ASSEMBLY_SOUND","",0),
("T29_EXCEPTIONAL_PREMISE","F12_FINAL_PREMISES_HANDOFF","prove the exceptional-case premise","exceptional-premise-proof","T20_EXCEPTIONAL_ZERO_ROWS T21_HARD_CORE_ROWS","","","EXCEPTIONAL_CASES_CLOSED","",0),
("T30_TERMINATION_PREMISE","F12_FINAL_PREMISES_HANDOFF","prove the termination premise","termination-premise-proof","T11_RECURRENT_BLOCK_CLOSURE T16_GLOBAL_RANK T18_ROW_THEOREMS","","","TERMINATION_ARGUMENT","",0),
("T31_OBJECTIVE_TRANSLATION_PREMISE","F12_FINAL_PREMISES_HANDOFF","prove translation of the quotient conclusion to D(n)=2n","objective-translation-proof","T12_AUXILIARY_SEMANTICS T16_GLOBAL_RANK T18_ROW_THEOREMS T19_GLOBAL_FAMILY T20_EXCEPTIONAL_ZERO_ROWS T21_HARD_CORE_ROWS","","","OBJECTIVE_TRANSLATION_TO_D_EQ_2N","",0),
("T32_OBLIGATION_ARTIFACTS","F09_TYPED_SUPPORT","supply genuine typed artifacts for every semantic obligation","typed-obligation-artifact-bank","@OBLIGATION_TARGETS","","","","",0),
("T33_OBLIGATION_SUPPORT_DAG","F09_TYPED_SUPPORT","prove noncircular complete support among obligation artifacts","obligation-artifact-support-proof","T32_OBLIGATION_ARTIFACTS","T32_OBLIGATION_ARTIFACTS","","","",0),
("T34_PREMISE_ARTIFACTS","F09_TYPED_SUPPORT","supply and bind every genuine final-premise artifact","typed-premise-artifact-bank","T22_BASE_CASES_PREMISE T23_RECURRENCE_PREMISE T24_INVARIANT_PREMISE T25_SELECTION_PREMISE T26_RESOURCE_PREMISE T27_CONTRACTION_PREMISE T28_CROSS_BLOCK_PREMISE T29_EXCEPTIONAL_PREMISE T30_TERMINATION_PREMISE T31_OBJECTIVE_TRANSLATION_PREMISE T33_OBLIGATION_SUPPORT_DAG","T33_OBLIGATION_SUPPORT_DAG","","","",0),
("T35_BASE_HANDOFF","F12_FINAL_PREMISES_HANDOFF","close the base-domain handoff assertion","base-handoff-proof","T22_BASE_CASES_PREMISE T34_PREMISE_ARTIFACTS","","","","BASE_DOMAIN_ESTABLISHED",0),
("T36_RECURRENCE_HANDOFF","F12_FINAL_PREMISES_HANDOFF","close the exhaustive-recurrence handoff assertion","recurrence-handoff-proof","T23_RECURRENCE_PREMISE T25_SELECTION_PREMISE T34_PREMISE_ARTIFACTS","","","","NONBASE_RECURRENCE_COVERS_ALL_CASES",0),
("T37_INVARIANT_HANDOFF","F12_FINAL_PREMISES_HANDOFF","close the invariant-preservation handoff assertion","invariant-handoff-proof","T24_INVARIANT_PREMISE T26_RESOURCE_PREMISE T34_PREMISE_ARTIFACTS","","","","STATE_AND_RESOURCE_INVARIANTS_PRESERVED",0),
("T38_TERMINATION_HANDOFF","F12_FINAL_PREMISES_HANDOFF","close the branch-termination handoff assertion","termination-handoff-proof","T27_CONTRACTION_PREMISE T28_CROSS_BLOCK_PREMISE T30_TERMINATION_PREMISE T34_PREMISE_ARTIFACTS","","","","EVERY_RECURRENCE_BRANCH_TERMINATES",0),
("T39_EXCEPTIONAL_HANDOFF","F12_FINAL_PREMISES_HANDOFF","close the exceptional/hard-core handoff assertion","exceptional-handoff-proof","T29_EXCEPTIONAL_PREMISE T34_PREMISE_ARTIFACTS","","","","EXCEPTIONAL_AND_HARD_CORE_CASES_CLOSED",0),
("T40_TRANSLATION_HANDOFF","F12_FINAL_PREMISES_HANDOFF","close the objective-translation handoff assertion","translation-handoff-proof","T31_OBJECTIVE_TRANSLATION_PREMISE T34_PREMISE_ARTIFACTS","","","","QUOTIENT_CONCLUSION_TRANSLATES_TO_D_EQ_2N",0),
("T41_FINAL_HANDOFF_REVIEW","F12_FINAL_PREMISES_HANDOFF","complete the six-assertion induction handoff review","final-handoff-review","T35_BASE_HANDOFF T36_RECURRENCE_HANDOFF T37_INVARIANT_HANDOFF T38_TERMINATION_HANDOFF T39_EXCEPTIONAL_HANDOFF T40_TRANSLATION_HANDOFF","","","","",0),
("T42_FINAL_DOSSIER_AUDIT","F12_FINAL_PREMISES_HANDOFF","pass the seven-gate final dossier-integrity audit","final-dossier-audit","T41_FINAL_HANDOFF_REVIEW","T41_FINAL_HANDOFF_REVIEW","","","",1),
("T43_ROOT_IMPLICATION","F13_ROOT_IMPLICATION","prove the reviewed global quotient and handoff imply D(n)=2n","all-n-root-implication-proof","T42_FINAL_DOSSIER_AUDIT","","GLOBAL_QUOTIENT_IMPLIES_ALL_N","","",0),
]

TARGETS: dict[str, dict[str, Any]] = {}
for row in TARGET_ROWS:
    target_id, frontier_id, title, kind, proof, research, obligations, premises, assertions, gate = row
    TARGETS[target_id] = {
        "frontier_id": frontier_id,
        "title": title,
        "required_artifact_kind": kind,
        "proof_dependency_target_ids": ids(proof),
        "research_dependency_target_ids": ids(research),
        "obligation_ids": ids(obligations),
        "premise_ids": ids(premises),
        "handoff_assertion_ids": ids(assertions),
        "requires_final_dossier_gate": bool(gate),
    }
TARGETS["T32_OBLIGATION_ARTIFACTS"]["proof_dependency_target_ids"] = tuple(
    target_id for target_id, definition in TARGETS.items()
    if target_id < "T22" and definition["obligation_ids"]
)


def topological_order(key: str) -> list[str]:
    indegree = {target_id: 0 for target_id in TARGETS}
    dependents: dict[str, list[str]] = {target_id: [] for target_id in TARGETS}
    for target_id, definition in TARGETS.items():
        for dependency in definition[key]:
            require(dependency in TARGETS, f"target {target_id}: unknown dependency {dependency}")
            require(dependency != target_id, f"target {target_id}: self dependency")
            indegree[target_id] += 1
            dependents[dependency].append(target_id)
    queue = [target_id for target_id, degree in indegree.items() if degree == 0]
    heapq.heapify(queue)
    output: list[str] = []
    while queue:
        current = heapq.heappop(queue)
        output.append(current)
        for nxt in sorted(dependents[current]):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(queue, nxt)
    require(len(output) == len(TARGETS), f"{key}: target graph contains a cycle")
    return output


def validate_definitions() -> dict[str, int]:
    require(set(FRONTIERS) == {value["frontier_id"] for value in TARGETS.values()},
            "every frontier must contain targets")
    proof_order = topological_order("proof_dependency_target_ids")
    research_order = topological_order("research_dependency_target_ids")
    for field, expected, label in (
        ("obligation_ids", set(closure.OBLIGATION_DEPENDENCIES), "semantic obligation"),
        ("premise_ids", set(contract.PREMISE_DEPENDENCIES), "final premise"),
        ("handoff_assertion_ids", set(handoff.HANDOFF_DEPENDENCIES), "handoff assertion"),
    ):
        counts = Counter(item for definition in TARGETS.values() for item in definition[field])
        require(set(counts) == expected, f"{label} coverage mismatch")
        require(all(value == 1 for value in counts.values()), f"each {label} requires exactly one target")
    require(sum(value["requires_final_dossier_gate"] for value in TARGETS.values()) == 1,
            "exactly one final dossier gate target required")
    return {"frontiers": len(FRONTIERS), "targets": len(TARGETS),
            "proof_order": len(proof_order), "research_order": len(research_order)}


def target_definition_records() -> list[dict[str, Any]]:
    output = []
    for target_id, definition in TARGETS.items():
        record = {
            "target_id": target_id,
            "frontier_id": definition["frontier_id"],
            "title": definition["title"],
            "required_artifact_kind": definition["required_artifact_kind"],
            "proof_dependency_target_ids": list(definition["proof_dependency_target_ids"]),
            "research_dependency_target_ids": list(definition["research_dependency_target_ids"]),
            "obligation_ids": list(definition["obligation_ids"]),
            "premise_ids": list(definition["premise_ids"]),
            "handoff_assertion_ids": list(definition["handoff_assertion_ids"]),
            "requires_final_dossier_gate": int(definition["requires_final_dossier_gate"]),
        }
        record["target_definition_sha256"] = catalogue.canonical_digest(record)
        output.append(record)
    return output


def exact_completion(record: dict[str, Any], target_id: str) -> dict[str, Any]:
    require(record.get("target_id") == target_id, f"target {target_id}: ID mismatch")
    status, locator, digest, note = (
        record.get(key) for key in ("status", "artifact_locator", "artifact_digest", "note")
    )
    require(status in {"proved", "open"}, f"target {target_id}: bad status")
    require(isinstance(note, str) and note, f"target {target_id}: note required")
    if status == "proved":
        require(isinstance(locator, str) and locator, f"target {target_id}: locator required")
        require(isinstance(digest, str) and digest, f"target {target_id}: digest required")
    else:
        require(locator is None and digest is None,
                f"target {target_id}: open target requires null artifact fields")
    output = {"target_id": target_id, "status": status, "artifact_locator": locator,
              "artifact_digest": digest, "note": note}
    output["target_completion_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    validate_definitions()
    dossier_certificate = certificate.get("final_dossier_integrity_certificate")
    raw_completions = certificate.get("target_completion_records")
    require(isinstance(dossier_certificate, dict),
            "final_dossier_integrity_certificate: expected object")
    require(isinstance(raw_completions, list), "target_completion_records: expected list")
    dossier.validate_certificate(dossier_certificate)
    dossier_exact = dossier.exact_certificate(dossier_certificate)
    handoff_certificate = dossier_certificate["final_induction_handoff_certificate"]
    premise_registry = handoff_certificate["premise_artifact_registry_certificate"]
    contract_certificate = premise_registry["final_implication_premise_contract_certificate"]
    obligation_registry = contract_certificate["obligation_artifact_registry_certificate"]
    closure_exact = closure.exact_certificate(obligation_registry["all_n_implication_closure_certificate"])
    contract_exact = contract.exact_certificate(contract_certificate)
    handoff_exact = handoff.exact_certificate(handoff_certificate)

    target_ids = list(TARGETS)
    require([record.get("target_id") for record in raw_completions] == target_ids,
            "target_completion_records: exact canonical order required")
    completions = [exact_completion(record, target_id)
                   for record, target_id in zip(raw_completions, target_ids)]
    require(raw_completions == completions, "target_completion_records: noncanonical records")
    completion_by_id = {record["target_id"]: record for record in completions}
    obligation_closed = {record["obligation_id"]: bool(record["closed"])
                         for record in closure_exact["obligation_closure_records"]}
    premise_effective = {record["premise_id"]: bool(record["effective_premise_closed"])
                         for record in contract_exact["premise_result_records"]}
    assertion_effective = {record["assertion_id"]: bool(record["effective_assertion_closed"])
                           for record in handoff_exact["handoff_assertion_result_records"]}
    dossier_ready = bool(dossier_exact["claims"]["final_dossier_integrity_ready"])

    effective: dict[str, bool] = {}
    proof_wave: dict[str, int] = {}
    proof_chain: dict[str, list[str]] = {}
    results = []
    for target_id in topological_order("proof_dependency_target_ids"):
        definition = TARGETS[target_id]
        dependencies = definition["proof_dependency_target_ids"]
        dependencies_complete = all(effective[value] for value in dependencies)
        external = [obligation_closed[value] for value in definition["obligation_ids"]]
        external += [premise_effective[value] for value in definition["premise_ids"]]
        external += [assertion_effective[value] for value in definition["handoff_assertion_ids"]]
        if definition["requires_final_dossier_gate"]:
            external.append(dossier_ready)
        external_satisfied = all(external) if external else True
        declared = completion_by_id[target_id]["status"] == "proved"
        if external:
            require(declared == external_satisfied,
                    f"target {target_id}: status disagrees with linked gate")
        if declared:
            require(dependencies_complete, f"target {target_id}: proved before dependencies")
        completed = bool(declared and dependencies_complete and external_satisfied)
        effective[target_id] = completed
        open_dependencies = [value for value in dependencies if not effective[value]]
        if completed:
            proof_wave[target_id], proof_chain[target_id] = 0, []
        elif open_dependencies:
            predecessor = min(open_dependencies, key=lambda item: (-proof_wave[item], item))
            proof_wave[target_id] = proof_wave[predecessor] + 1
            proof_chain[target_id] = proof_chain[predecessor] + [target_id]
        else:
            proof_wave[target_id], proof_chain[target_id] = 1, [target_id]
        record = {
            "target_id": target_id,
            "frontier_id": definition["frontier_id"],
            "declared_proved": int(declared),
            "proof_dependencies_complete": int(dependencies_complete),
            "linked_external_gate_satisfied": int(external_satisfied),
            "effective_target_complete": int(completed),
            "open_proof_dependency_target_ids": open_dependencies,
            "earliest_proof_completion_wave": proof_wave[target_id],
            "longest_open_proof_chain": proof_chain[target_id],
            "target_completion_sha256": completion_by_id[target_id]["target_completion_sha256"],
        }
        record["target_result_sha256"] = catalogue.canonical_digest(record)
        results.append(record)

    research_wave: dict[str, int] = {}
    research_records = []
    for target_id in topological_order("research_dependency_target_ids"):
        dependencies = TARGETS[target_id]["research_dependency_target_ids"]
        open_dependencies = [value for value in dependencies if not effective[value]]
        actionable = int(not effective[target_id] and not open_dependencies)
        research_wave[target_id] = 0 if effective[target_id] else (
            1 + max((research_wave[value] for value in open_dependencies), default=0)
        )
        record = {"target_id": target_id, "research_actionable": actionable,
                  "open_research_dependency_target_ids": open_dependencies,
                  "earliest_research_start_wave": research_wave[target_id]}
        record["research_schedule_sha256"] = catalogue.canonical_digest(record)
        research_records.append(record)

    result_by_id = {record["target_id"]: record for record in results}
    research_by_id = {record["target_id"]: record for record in research_records}
    downstream: dict[str, list[str]] = {}
    for source in TARGETS:
        queue, seen = deque([source]), {source}
        while queue:
            current = queue.popleft()
            for target_id, definition in TARGETS.items():
                if current in definition["proof_dependency_target_ids"] and target_id not in seen:
                    seen.add(target_id)
                    queue.append(target_id)
        downstream[source] = [value for value in TARGETS
                              if value in seen and value != source and not effective[value]]

    frontier_records = []
    for frontier_id, title in FRONTIERS.items():
        frontier_targets = [target_id for target_id, definition in TARGETS.items()
                            if definition["frontier_id"] == frontier_id]
        record = {
            "frontier_id": frontier_id,
            "title": title,
            "target_ids": frontier_targets,
            "completed_target_ids": [value for value in frontier_targets if effective[value]],
            "research_actionable_target_ids": [value for value in frontier_targets
                                                if research_by_id[value]["research_actionable"]],
            "proof_actionable_target_ids": [value for value in frontier_targets
                                             if not effective[value]
                                             and result_by_id[value]["proof_dependencies_complete"]],
            "open_target_ids": [value for value in frontier_targets if not effective[value]],
            "maximum_downstream_unclosed_impact": max(
                (len(downstream[value]) for value in frontier_targets), default=0),
        }
        record["frontier_execution_sha256"] = catalogue.canonical_digest(record)
        frontier_records.append(record)

    proof_actionable = [value for value in TARGETS if not effective[value]
                        and result_by_id[value]["proof_dependencies_complete"]]
    research_actionable = [value for value in TARGETS
                           if research_by_id[value]["research_actionable"]]
    all_complete = int(all(effective.values()))
    definitions = target_definition_records()
    claims = {
        "frontier_groups": len(FRONTIERS),
        "atomic_targets": len(TARGETS),
        "completed_targets": sum(effective.values()),
        "open_targets": len(TARGETS) - sum(effective.values()),
        "research_actionable_targets": len(research_actionable),
        "proof_actionable_targets": len(proof_actionable),
        "minimum_parallel_proof_waves_to_root": proof_wave["T43_ROOT_IMPLICATION"],
        "all_frontier_targets_complete": all_complete,
        "root_implication_target_complete": int(effective["T43_ROOT_IMPLICATION"]),
        "final_frontier_execution_ready": int(all_complete and dossier_ready),
        "all_n_proved_by_checker": 0,
        "research_actionable_target_ids": research_actionable,
        "proof_actionable_target_ids": proof_actionable,
        "final_dossier_integrity_sha256": dossier_certificate["certificate_sha256"],
        "target_definitions_sha256": catalogue.canonical_digest(definitions),
        "target_completions_sha256": catalogue.canonical_digest(completions),
        "target_results_sha256": catalogue.canonical_digest(results),
        "research_schedule_sha256": catalogue.canonical_digest(research_records),
        "frontier_records_sha256": catalogue.canonical_digest(frontier_records),
    }
    return {"target_definition_records": definitions,
            "target_completion_records": completions,
            "target_result_records": results,
            "research_schedule_records": research_records,
            "frontier_execution_records": frontier_records,
            "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("target_definition_records", "target_completion_records", "target_result_records",
                "research_schedule_records", "frontier_execution_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"frontiers": claims["frontier_groups"], "targets": claims["atomic_targets"],
            "completed": claims["completed_targets"],
            "research_actionable": claims["research_actionable_targets"],
            "proof_actionable": claims["proof_actionable_targets"],
            "ready": claims["final_frontier_execution_ready"]}


def build_certificate(dossier_certificate: dict[str, Any],
                      records: list[dict[str, Any]]) -> dict[str, Any]:
    certificate: dict[str, Any] = {"version": 1,
                                  "final_dossier_integrity_certificate": dossier_certificate,
                                  "target_completion_records": records}
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        print(validate_definitions())
        return
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_atomic_frontier_execution.py certificate.json | --self-test")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
