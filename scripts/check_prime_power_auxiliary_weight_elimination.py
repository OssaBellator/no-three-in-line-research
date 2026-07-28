#!/usr/bin/env python3
"""Eliminate auxiliary child coordinates under one common state-weight vector.

For each auxiliary state that occurs with positive coefficient in a recurrent block, a
one-step expansion gives a fixed nonnegative load and nonauxiliary target multiplicities.
The expansion must have weighted load at most the auxiliary state's global weight. Direct
routed credit to an eliminated auxiliary coordinate is forbidden. Every response is then
rewritten exactly and its common-weight row margin can only improve.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_common_recurrent_block_weights as common
import check_prime_power_labelled_recurrent_row_margin as row_margin


class AuxiliaryEliminationError(ValueError):
    """Raised when an auxiliary expansion or transformed row is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AuxiliaryEliminationError(message)


def exact_expansion(record: dict[str, Any], path: str) -> dict[str, Any]:
    auxiliary = record.get("auxiliary_state_id")
    fixed_load = record.get("fixed_load")
    raw_targets = record.get("target_multiplicities")
    evidence = record.get("evidence")
    require(isinstance(auxiliary, str) and auxiliary, f"{path}.auxiliary_state_id: required")
    require(type(fixed_load) is int and fixed_load >= 0, f"{path}.fixed_load: nonnegative integer required")
    require(isinstance(raw_targets, list), f"{path}.target_multiplicities: expected list")
    require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
    targets = []
    for index, raw in enumerate(raw_targets):
        require(isinstance(raw, dict), f"{path}.target_multiplicities[{index}]: expected object")
        state_id = raw.get("state_id")
        multiplicity = raw.get("multiplicity")
        require(isinstance(state_id, str) and state_id, f"{path}.target[{index}].state_id: required")
        require(type(multiplicity) is int and multiplicity > 0,
                f"{path}.target[{index}].multiplicity: positive integer required")
        target = {"state_id": state_id, "multiplicity": multiplicity}
        target["target_record_sha256"] = catalogue.canonical_digest(target)
        targets.append(target)
    require(targets == sorted(targets, key=lambda item: item["state_id"]), f"{path}.targets: canonical order required")
    require(len({target["state_id"] for target in targets}) == len(targets), f"{path}.targets: duplicate state")
    require(fixed_load > 0 or targets, f"{path}: zero expansion is not allowed")
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


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    block = certificate.get("common_weight_certificate")
    raw_expansions = certificate.get("auxiliary_expansions")
    require(isinstance(block, dict), "common_weight_certificate: expected object")
    require(isinstance(raw_expansions, list), "auxiliary_expansions: expected list")
    common.validate_certificate(block)
    block_exact = common.exact_certificate(block)
    states = state_registry(block)
    weights = {record["state_id"]: record["weight"] for record in block["state_weights"]}

    expansions = [exact_expansion(record, f"auxiliary_expansions[{index}]") for index, record in enumerate(raw_expansions)]
    require(expansions == sorted(expansions, key=lambda record: record["auxiliary_state_id"]),
            "auxiliary_expansions: canonical order required")
    require(len({record["auxiliary_state_id"] for record in expansions}) == len(expansions),
            "auxiliary_expansions: duplicate auxiliary state")
    expansion_map = {record["auxiliary_state_id"]: record for record in expansions}

    used_auxiliaries: set[str] = set()
    for routed in block["routed_row_certificates"]:
        row_certificate = routed["row_margin_certificate"]
        children = row_certificate["weight_exposure_certificate"]["children"]
        for position, child in enumerate(children):
            if states[child]["role"] == "auxiliary" and any(
                response["child_vector"][position] > 0
                for response in row_certificate["weight_exposure_certificate"]["response_vectors"]
            ):
                used_auxiliaries.add(child)
    require(set(expansion_map) == used_auxiliaries,
            "auxiliary_expansions: must cover exactly the positively used auxiliary states")

    expansion_records = []
    for auxiliary in sorted(used_auxiliaries):
        record = expansion_map[auxiliary]
        require(auxiliary in states and states[auxiliary]["role"] == "auxiliary",
                f"{auxiliary}: expansion source is not auxiliary")
        load = record["fixed_load"]
        for target in record["target_multiplicities"]:
            state_id = target["state_id"]
            require(state_id in states, f"{auxiliary}: unknown target state")
            require(states[state_id]["role"] != "auxiliary", f"{auxiliary}: recursive auxiliary target forbidden")
            load += target["multiplicity"] * weights[state_id]
        require(load <= weights[auxiliary], f"{auxiliary}: expansion exceeds global auxiliary weight")
        enriched = dict(record)
        enriched["auxiliary_weight"] = weights[auxiliary]
        enriched["expansion_weighted_load"] = load
        enriched["weight_slack"] = weights[auxiliary] - load
        enriched["expansion_record_sha256"] = catalogue.canonical_digest(
            {key: value for key, value in enriched.items() if key != "expansion_record_sha256"}
        )
        expansion_records.append(enriched)

    row_records = []
    total_original = total_eliminated = 0
    minimum_margin_gain: int | None = None
    for routed in block["routed_row_certificates"]:
        row_certificate = routed["row_margin_certificate"]
        children = row_certificate["weight_exposure_certificate"]["children"]
        for credit in row_certificate["response_credit_records"]:
            for auxiliary in used_auxiliaries & set(children):
                require(credit["credit_routes"][auxiliary] == 0,
                        f"row {row_certificate['claims']['fibre_id']}: routed credit to eliminated auxiliary")
        original_rows = {response_key(record["response"]): record for record in row_certificate["row_records"]}
        transformed_responses = []
        for response in row_certificate["weight_exposure_certificate"]["response_vectors"]:
            key = response_key(response["response"])
            original = original_rows[key]
            transformed: Counter[str] = Counter()
            fixed_increment = 0
            for child, coefficient in zip(children, response["child_vector"]):
                if coefficient == 0:
                    continue
                if child in used_auxiliaries:
                    expansion = expansion_map[child]
                    fixed_increment += coefficient * expansion["fixed_load"]
                    for target in expansion["target_multiplicities"]:
                        transformed[target["state_id"]] += coefficient * target["multiplicity"]
                else:
                    transformed[child] += coefficient
            transformed_vector = [[state_id, transformed[state_id]] for state_id in sorted(transformed)]
            transformed_child_load = sum(weights[state_id] * value for state_id, value in transformed.items())
            eliminated_row_load = row_certificate["fixed_load"] + fixed_increment + transformed_child_load - original["weighted_credit"]
            eliminated_margin = row_certificate["parent_budget"] - eliminated_row_load
            require(eliminated_row_load <= original["row_load"], "auxiliary elimination increased row load")
            require(eliminated_margin >= original["margin"], "auxiliary elimination decreased margin")
            gain = eliminated_margin - original["margin"]
            minimum_margin_gain = gain if minimum_margin_gain is None else min(minimum_margin_gain, gain)
            total_original += original["row_load"]
            total_eliminated += eliminated_row_load
            transformed_responses.append({
                "response": response["response"],
                "original_child_vector": response["child_vector"],
                "eliminated_fixed_increment": fixed_increment,
                "eliminated_child_vector": transformed_vector,
                "original_row_load": original["row_load"],
                "eliminated_row_load": eliminated_row_load,
                "original_margin": original["margin"],
                "eliminated_margin": eliminated_margin,
                "margin_gain": gain,
            })
        transformed_responses.sort(key=lambda record: record["response"])
        minimum_load = min(record["eliminated_row_load"] for record in transformed_responses)
        maximum_margin = row_certificate["parent_budget"] - minimum_load
        row_records.append({
            "parent_state_id": row_certificate["linked_operation_certificate"]["linkage_certificate"]["source_manifest"]["parent"],
            "fibre_id": row_certificate["claims"]["fibre_id"],
            "responses": len(transformed_responses),
            "original_maximum_margin": row_certificate["claims"]["maximum_margin"],
            "eliminated_maximum_margin": maximum_margin,
            "strict_after_elimination": int(maximum_margin > 0),
            "transformed_responses": transformed_responses,
            "transformed_responses_sha256": catalogue.canonical_digest(transformed_responses),
        })
    row_records.sort(key=lambda record: (record["parent_state_id"], record["fibre_id"]))
    claims = {
        "states": len(states),
        "rows": len(row_records),
        "used_auxiliary_states": len(used_auxiliaries),
        "expansion_targets": sum(len(record["target_multiplicities"]) for record in expansion_records),
        "responses": sum(record["responses"] for record in row_records),
        "total_original_row_load": total_original,
        "total_eliminated_row_load": total_eliminated,
        "total_load_reduction": total_original - total_eliminated,
        "minimum_response_margin_gain": 0 if minimum_margin_gain is None else minimum_margin_gain,
        "strict_rows_after_elimination": sum(record["strict_after_elimination"] for record in row_records),
        "all_rows_strict_after_elimination": int(all(record["strict_after_elimination"] for record in row_records)),
        "source_complete_strict_scc": block_exact["claims"]["complete_strict_scc"],
        "strict_scc_preserved_after_elimination": int(
            block_exact["claims"]["complete_strict_scc"]
            and all(record["strict_after_elimination"] for record in row_records)
        ),
        "common_weight_sha256": block["certificate_sha256"],
        "expansions_sha256": catalogue.canonical_digest(expansion_records),
        "rows_sha256": catalogue.canonical_digest(row_records),
    }
    return {"auxiliary_expansions": expansion_records, "eliminated_row_records": row_records, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("auxiliary_expansions", "eliminated_row_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "rows": claims["rows"],
        "auxiliaries": claims["used_auxiliary_states"],
        "targets": claims["expansion_targets"],
        "responses": claims["responses"],
        "reduction": claims["total_load_reduction"],
        "strict": claims["strict_rows_after_elimination"],
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
        raise SystemExit("usage: check_prime_power_auxiliary_weight_elimination.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
