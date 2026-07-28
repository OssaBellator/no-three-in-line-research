#!/usr/bin/env python3
"""Eliminate an acyclic hierarchy of auxiliary child coordinates.

A one-step auxiliary expansion may still target another auxiliary. This checker accepts a
finite directed acyclic expansion graph, recursively expands every positively used
auxiliary to nonauxiliary targets, forbids credit on every eliminated coordinate, and
checks responsewise common-weight load monotonicity after complete substitution.
"""
from __future__ import annotations

import json
import sys
from collections import Counter, deque
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_common_recurrent_block_weights as common
import check_prime_power_labelled_recurrent_row_margin as row_margin


class AcyclicAuxiliaryError(ValueError):
    """Raised when an auxiliary expansion graph or full substitution is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AcyclicAuxiliaryError(message)


def exact_target(record: dict[str, Any], path: str) -> dict[str, Any]:
    state_id = record.get("state_id")
    multiplicity = record.get("multiplicity")
    require(isinstance(state_id, str) and state_id, f"{path}.state_id: required")
    require(type(multiplicity) is int and multiplicity > 0,
            f"{path}.multiplicity: positive integer required")
    output = {"state_id": state_id, "multiplicity": multiplicity}
    output["target_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_expansion(record: dict[str, Any], path: str) -> dict[str, Any]:
    auxiliary = record.get("auxiliary_state_id")
    fixed_load = record.get("fixed_load")
    raw_targets = record.get("target_multiplicities")
    evidence = record.get("evidence")
    require(isinstance(auxiliary, str) and auxiliary, f"{path}.auxiliary_state_id: required")
    require(type(fixed_load) is int and fixed_load >= 0,
            f"{path}.fixed_load: nonnegative integer required")
    require(isinstance(raw_targets, list), f"{path}.target_multiplicities: expected list")
    require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
    targets = [exact_target(raw, f"{path}.target_multiplicities[{index}]")
               for index, raw in enumerate(raw_targets)]
    require(raw_targets == targets, f"{path}.target_multiplicities: canonical records required")
    require(targets == sorted(targets, key=lambda item: item["state_id"]),
            f"{path}.target_multiplicities: canonical order required")
    require(len({target["state_id"] for target in targets}) == len(targets),
            f"{path}.target_multiplicities: duplicate target")
    require(fixed_load > 0 or targets, f"{path}: zero expansion forbidden")
    output = {
        "auxiliary_state_id": auxiliary,
        "fixed_load": fixed_load,
        "target_multiplicities": targets,
        "evidence": evidence,
    }
    output["expansion_record_sha256"] = catalogue.canonical_digest(output)
    return output


def state_registry(block: dict[str, Any]) -> dict[str, dict[str, Any]]:
    states: dict[str, dict[str, Any]] = {}
    for routed in block["routed_row_certificates"]:
        source = routed["row_margin_certificate"]["linked_operation_certificate"]["linkage_certificate"]["source_manifest"]
        for raw in source["states"]:
            core = {key: raw[key] for key in ("id", "role", "stratum", "owner")}
            if core["id"] in states:
                require(states[core["id"]] == core, f"state {core['id']}: definition drift")
            else:
                states[core["id"]] = core
    return states


def response_key(response: list[list[int]]) -> tuple[tuple[int, int], ...]:
    return row_margin.response_key(response)


def topological_order(nodes: set[str], edges: dict[str, set[str]]) -> list[str]:
    indegree = {node: 0 for node in nodes}
    reverse: dict[str, set[str]] = {node: set() for node in nodes}
    for source in nodes:
        for target in edges.get(source, set()):
            indegree[target] += 1
            reverse[source].add(target)
    queue = deque(sorted(node for node, degree in indegree.items() if degree == 0))
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for target in sorted(reverse[node]):
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    require(len(order) == len(nodes), "auxiliary expansion graph contains a directed cycle")
    return order


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    block = certificate.get("common_weight_certificate")
    raw_expansions = certificate.get("auxiliary_expansions")
    require(isinstance(block, dict), "common_weight_certificate: expected object")
    require(isinstance(raw_expansions, list), "auxiliary_expansions: expected list")
    common.validate_certificate(block)
    block_exact = common.exact_certificate(block)
    states = state_registry(block)
    weights = {record["state_id"]: record["weight"] for record in block["state_weights"]}

    expansions = [exact_expansion(record, f"auxiliary_expansions[{index}]")
                  for index, record in enumerate(raw_expansions)]
    require(raw_expansions == expansions, "auxiliary_expansions: canonical records or digests required")
    require(expansions == sorted(expansions, key=lambda record: record["auxiliary_state_id"]),
            "auxiliary_expansions: canonical order required")
    require(len({record["auxiliary_state_id"] for record in expansions}) == len(expansions),
            "auxiliary_expansions: duplicate auxiliary")
    expansion_map = {record["auxiliary_state_id"]: record for record in expansions}

    root_auxiliaries: set[str] = set()
    for routed in block["routed_row_certificates"]:
        row_certificate = routed["row_margin_certificate"]
        children = row_certificate["weight_exposure_certificate"]["children"]
        for position, child in enumerate(children):
            if states[child]["role"] == "auxiliary" and any(
                response["child_vector"][position] > 0
                for response in row_certificate["weight_exposure_certificate"]["response_vectors"]
            ):
                root_auxiliaries.add(child)

    closure = set(root_auxiliaries)
    pending = list(root_auxiliaries)
    while pending:
        auxiliary = pending.pop()
        require(auxiliary in expansion_map, f"{auxiliary}: missing expansion")
        for target in expansion_map[auxiliary]["target_multiplicities"]:
            state_id = target["state_id"]
            require(state_id in states, f"{auxiliary}: unknown target {state_id}")
            if states[state_id]["role"] == "auxiliary" and state_id not in closure:
                closure.add(state_id)
                pending.append(state_id)
    require(set(expansion_map) == closure,
            "auxiliary_expansions: must cover exactly the recursive closure of used auxiliaries")

    edges: dict[str, set[str]] = {auxiliary: set() for auxiliary in closure}
    local_records = []
    for auxiliary in sorted(closure):
        require(auxiliary in states and states[auxiliary]["role"] == "auxiliary",
                f"{auxiliary}: expansion source is not auxiliary")
        record = expansion_map[auxiliary]
        local_load = record["fixed_load"]
        for target in record["target_multiplicities"]:
            state_id = target["state_id"]
            require(state_id != auxiliary, f"{auxiliary}: self-target forbidden")
            local_load += target["multiplicity"] * weights[state_id]
            if states[state_id]["role"] == "auxiliary":
                edges[auxiliary].add(state_id)
        require(local_load <= weights[auxiliary],
                f"{auxiliary}: local expansion exceeds global weight")
        local = {
            "auxiliary_state_id": auxiliary,
            "auxiliary_weight": weights[auxiliary],
            "local_weighted_load": local_load,
            "local_weight_slack": weights[auxiliary] - local_load,
            "auxiliary_targets": sorted(edges[auxiliary]),
            "expansion_record_sha256": record["expansion_record_sha256"],
        }
        local["local_record_sha256"] = catalogue.canonical_digest(local)
        local_records.append(local)

    order = topological_order(closure, edges)
    effective: dict[str, tuple[int, Counter[str]]] = {}
    effective_records = []
    for auxiliary in reversed(order):
        record = expansion_map[auxiliary]
        fixed = record["fixed_load"]
        targets: Counter[str] = Counter()
        for target in record["target_multiplicities"]:
            state_id = target["state_id"]
            multiplicity = target["multiplicity"]
            if states[state_id]["role"] == "auxiliary":
                child_fixed, child_targets = effective[state_id]
                fixed += multiplicity * child_fixed
                for final_state, final_multiplicity in child_targets.items():
                    targets[final_state] += multiplicity * final_multiplicity
            else:
                targets[state_id] += multiplicity
        effective_load = fixed + sum(weights[state_id] * multiplicity
                                     for state_id, multiplicity in targets.items())
        require(effective_load <= weights[auxiliary],
                f"{auxiliary}: fully expanded load exceeds global weight")
        effective[auxiliary] = (fixed, targets)
        output = {
            "auxiliary_state_id": auxiliary,
            "topological_index": order.index(auxiliary),
            "effective_fixed_load": fixed,
            "effective_target_multiplicities": [
                {"state_id": state_id, "multiplicity": targets[state_id]}
                for state_id in sorted(targets)
            ],
            "effective_weighted_load": effective_load,
            "effective_weight_slack": weights[auxiliary] - effective_load,
        }
        output["effective_record_sha256"] = catalogue.canonical_digest(output)
        effective_records.append(output)
    effective_records.sort(key=lambda record: record["auxiliary_state_id"])

    row_records = []
    total_original = total_eliminated = 0
    minimum_gain: int | None = None
    for routed in block["routed_row_certificates"]:
        row_certificate = routed["row_margin_certificate"]
        children = row_certificate["weight_exposure_certificate"]["children"]
        for credit in row_certificate["response_credit_records"]:
            for auxiliary in closure & set(children):
                require(credit["credit_routes"][auxiliary] == 0,
                        f"row {row_certificate['claims']['fibre_id']}: credit routed to eliminated auxiliary")
        original_rows = {response_key(record["response"]): record
                         for record in row_certificate["row_records"]}
        transformed_responses = []
        for response in row_certificate["weight_exposure_certificate"]["response_vectors"]:
            key = response_key(response["response"])
            original = original_rows[key]
            transformed: Counter[str] = Counter()
            fixed_increment = 0
            for child, coefficient in zip(children, response["child_vector"]):
                if coefficient == 0:
                    continue
                if child in closure:
                    child_fixed, child_targets = effective[child]
                    fixed_increment += coefficient * child_fixed
                    for state_id, multiplicity in child_targets.items():
                        transformed[state_id] += coefficient * multiplicity
                else:
                    transformed[child] += coefficient
            transformed_vector = [[state_id, transformed[state_id]] for state_id in sorted(transformed)]
            transformed_child_load = sum(weights[state_id] * multiplicity
                                         for state_id, multiplicity in transformed.items())
            net_fixed_offset = row_certificate["fixed_load"] + fixed_increment - original["weighted_credit"]
            eliminated_load = net_fixed_offset + transformed_child_load
            eliminated_margin = row_certificate["parent_budget"] - eliminated_load
            require(eliminated_load <= original["row_load"], "full auxiliary elimination increased row load")
            require(eliminated_margin >= original["margin"], "full auxiliary elimination decreased margin")
            gain = eliminated_margin - original["margin"]
            minimum_gain = gain if minimum_gain is None else min(minimum_gain, gain)
            total_original += original["row_load"]
            total_eliminated += eliminated_load
            transformed_responses.append({
                "response": response["response"],
                "original_child_vector": response["child_vector"],
                "eliminated_fixed_increment": fixed_increment,
                "eliminated_child_vector": transformed_vector,
                "weighted_credit": original["weighted_credit"],
                "net_fixed_offset": net_fixed_offset,
                "original_row_load": original["row_load"],
                "eliminated_row_load": eliminated_load,
                "original_margin": original["margin"],
                "eliminated_margin": eliminated_margin,
                "margin_gain": gain,
            })
        transformed_responses.sort(key=lambda record: record["response"])
        selected = min(transformed_responses,
                       key=lambda record: (record["eliminated_row_load"], record["response"]))
        minimum_load = selected["eliminated_row_load"]
        minimizers = [record for record in transformed_responses
                      if record["eliminated_row_load"] == minimum_load]
        row = {
            "parent_state_id": row_certificate["linked_operation_certificate"]["linkage_certificate"]["source_manifest"]["parent"],
            "fibre_id": row_certificate["claims"]["fibre_id"],
            "responses": len(transformed_responses),
            "selected_response": selected["response"],
            "selected_net_fixed_offset": selected["net_fixed_offset"],
            "selected_child_vector": selected["eliminated_child_vector"],
            "selected_row_load": selected["eliminated_row_load"],
            "selected_margin": selected["eliminated_margin"],
            "minimizer_count": len(minimizers),
            "original_maximum_margin": row_certificate["claims"]["maximum_margin"],
            "eliminated_maximum_margin": row_certificate["parent_budget"] - minimum_load,
            "strict_after_elimination": int(row_certificate["parent_budget"] - minimum_load > 0),
            "transformed_responses": transformed_responses,
            "transformed_responses_sha256": catalogue.canonical_digest(transformed_responses),
        }
        row["row_elimination_sha256"] = catalogue.canonical_digest(row)
        row_records.append(row)
    row_records.sort(key=lambda record: (record["parent_state_id"], record["fibre_id"]))

    claims = {
        "states": len(states),
        "rows": len(row_records),
        "root_auxiliary_states": len(root_auxiliaries),
        "eliminated_auxiliary_states": len(closure),
        "auxiliary_edges": sum(len(values) for values in edges.values()),
        "topological_depth_order": order,
        "effective_nonauxiliary_targets": sum(len(record["effective_target_multiplicities"])
                                               for record in effective_records),
        "responses": sum(record["responses"] for record in row_records),
        "total_original_row_load": total_original,
        "total_eliminated_row_load": total_eliminated,
        "total_load_reduction": total_original - total_eliminated,
        "minimum_response_margin_gain": 0 if minimum_gain is None else minimum_gain,
        "strict_rows_after_elimination": sum(record["strict_after_elimination"] for record in row_records),
        "all_rows_strict_after_elimination": int(all(record["strict_after_elimination"] for record in row_records)),
        "source_complete_strict_scc": block_exact["claims"]["complete_strict_scc"],
        "strict_scc_preserved_after_elimination": int(
            block_exact["claims"]["complete_strict_scc"]
            and all(record["strict_after_elimination"] for record in row_records)
        ),
        "common_weight_sha256": block["certificate_sha256"],
        "expansions_sha256": catalogue.canonical_digest(expansions),
        "local_records_sha256": catalogue.canonical_digest(local_records),
        "effective_records_sha256": catalogue.canonical_digest(effective_records),
        "rows_sha256": catalogue.canonical_digest(row_records),
    }
    return {
        "auxiliary_expansions": expansions,
        "local_expansion_records": local_records,
        "effective_expansion_records": effective_records,
        "eliminated_row_records": row_records,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("auxiliary_expansions", "local_expansion_records", "effective_expansion_records",
                "eliminated_row_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "rows": claims["rows"],
        "roots": claims["root_auxiliary_states"],
        "auxiliaries": claims["eliminated_auxiliary_states"],
        "edges": claims["auxiliary_edges"],
        "responses": claims["responses"],
        "reduction": claims["total_load_reduction"],
        "preserved": claims["strict_scc_preserved_after_elimination"],
    }


def build_certificate(block: dict[str, Any], expansions: list[dict[str, Any]]) -> dict[str, Any]:
    canonical = [exact_expansion(record, "auxiliary_expansion") for record in expansions]
    canonical.sort(key=lambda record: record["auxiliary_state_id"])
    certificate: dict[str, Any] = {
        "version": 1,
        "common_weight_certificate": block,
        "auxiliary_expansions": canonical,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_acyclic_auxiliary_elimination.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
