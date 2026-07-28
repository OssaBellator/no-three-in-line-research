#!/usr/bin/env python3
"""Validate return and interface rows under one globally cleared integer weight registry.

Cross-block state sharing determines relative scales only inside connected block components.
This checker accepts one positive integer multiplier per disconnected component, normalizes
those multipliers globally, and validates exact return/interface/offdiagonal rows.

Each interface row must have positive margin, or zero margin together with strict descent in
a supplied nonnegative state rank on every positive target. Negative-margin rows and
non-descending zero-margin rows are rejected.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_cross_block_weight_synchronization as synchronization


class InterfaceRowError(ValueError):
    """Raised when global component scales or interface rows are inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise InterfaceRowError(message)


def exact_multiplier(record: dict[str, Any], path: str) -> dict[str, Any]:
    component_id = record.get("component_id")
    multiplier = record.get("multiplier")
    require(isinstance(component_id, str) and component_id, f"{path}.component_id: required")
    require(type(multiplier) is int and multiplier > 0, f"{path}.multiplier: positive integer required")
    output = {"component_id": component_id, "multiplier": multiplier}
    output["component_multiplier_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_rank(record: dict[str, Any], path: str) -> dict[str, Any]:
    state_id = record.get("global_state_id")
    rank = record.get("rank")
    require(isinstance(state_id, str) and state_id, f"{path}.global_state_id: required")
    require(type(rank) is int and rank >= 0, f"{path}.rank: nonnegative integer required")
    output = {"global_state_id": state_id, "rank": rank}
    output["state_rank_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_target(record: dict[str, Any], path: str) -> dict[str, Any]:
    state_id = record.get("global_state_id")
    multiplicity = record.get("multiplicity")
    require(isinstance(state_id, str) and state_id, f"{path}.global_state_id: required")
    require(type(multiplicity) is int and multiplicity > 0, f"{path}.multiplicity: positive integer required")
    output = {"global_state_id": state_id, "multiplicity": multiplicity}
    output["target_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    synchronization_certificate = certificate.get("weight_synchronization_certificate")
    raw_multipliers = certificate.get("component_multipliers")
    raw_ranks = certificate.get("state_ranks")
    raw_rows = certificate.get("interface_rows")
    require(isinstance(synchronization_certificate, dict),
            "weight_synchronization_certificate: expected object")
    require(isinstance(raw_multipliers, list) and raw_multipliers,
            "component_multipliers: nonempty list required")
    require(isinstance(raw_ranks, list) and raw_ranks, "state_ranks: nonempty list required")
    require(isinstance(raw_rows, list), "interface_rows: expected list")
    synchronization.validate_certificate(synchronization_certificate)
    sync_exact = synchronization.exact_certificate(synchronization_certificate)

    multipliers = [exact_multiplier(record, f"component_multipliers[{index}]")
                   for index, record in enumerate(raw_multipliers)]
    require(raw_multipliers == multipliers, "component_multipliers: canonical records or digests required")
    require(multipliers == sorted(multipliers, key=lambda item: item["component_id"]),
            "component_multipliers: canonical component order required")
    component_ids = [record["component_id"] for record in sync_exact["scale_components"]]
    require([record["component_id"] for record in multipliers] == sorted(component_ids),
            "component_multipliers: must cover every scale component exactly")
    require(math.gcd(*(record["multiplier"] for record in multipliers)) == 1,
            "component_multipliers: common gcd must be one")
    multiplier_by_component = {record["component_id"]: record["multiplier"] for record in multipliers}

    state_records = {
        record["global_state_id"]: record
        for record in synchronization_certificate["state_identification_certificate"]["global_state_records"]
    }
    ranks = [exact_rank(record, f"state_ranks[{index}]") for index, record in enumerate(raw_ranks)]
    require(raw_ranks == ranks, "state_ranks: canonical records or digests required")
    require(ranks == sorted(ranks, key=lambda item: item["global_state_id"]),
            "state_ranks: canonical state order required")
    require([record["global_state_id"] for record in ranks] == sorted(state_records),
            "state_ranks: must cover every global state exactly")
    rank_by_state = {record["global_state_id"]: record["rank"] for record in ranks}

    final_weight_records = []
    final_weights: dict[str, int] = {}
    for record in sync_exact["global_weight_records"]:
        multiplier = multiplier_by_component[record["component_id"]]
        final_weight = multiplier * record["component_weight"]
        output = {
            "global_state_id": record["global_state_id"],
            "component_id": record["component_id"],
            "component_multiplier": multiplier,
            "component_weight": record["component_weight"],
            "global_weight": final_weight,
            "role": record["role"],
            "stratum": record["stratum"],
            "rank": rank_by_state[record["global_state_id"]],
        }
        output["final_weight_record_sha256"] = catalogue.canonical_digest(output)
        final_weight_records.append(output)
        final_weights[record["global_state_id"]] = final_weight
    final_weight_records.sort(key=lambda item: item["global_state_id"])

    interface_records = []
    strict_rows = descending_rows = 0
    for index, raw in enumerate(raw_rows):
        path = f"interface_rows[{index}]"
        row_id = raw.get("row_id")
        kind = raw.get("kind")
        parent = raw.get("parent_global_state_id")
        fixed_offset = raw.get("fixed_offset")
        raw_targets = raw.get("target_multiplicities")
        evidence = raw.get("evidence")
        require(isinstance(row_id, str) and row_id, f"{path}.row_id: required")
        require(kind in {"return", "interface", "offdiagonal"}, f"{path}.kind: bad kind")
        require(isinstance(parent, str) and parent in final_weights, f"{path}.parent: unknown state")
        require(state_records[parent]["role"] not in {"auxiliary", "sink"}, f"{path}.parent: invalid role")
        require(type(fixed_offset) is int, f"{path}.fixed_offset: integer required")
        require(isinstance(raw_targets, list), f"{path}.target_multiplicities: expected list")
        require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
        targets = [exact_target(record, f"{path}.target_multiplicities[{j}]")
                   for j, record in enumerate(raw_targets)]
        require(targets == sorted(targets, key=lambda item: item["global_state_id"]),
                f"{path}.target_multiplicities: canonical state order required")
        target_ids = [record["global_state_id"] for record in targets]
        require(len(target_ids) == len(set(target_ids)), f"{path}: duplicate target state")
        for target in targets:
            state_id = target["global_state_id"]
            require(state_id in final_weights, f"{path}: unknown target {state_id}")
            require(state_records[state_id]["role"] != "auxiliary", f"{path}: auxiliary target forbidden")
        parent_weight = final_weights[parent]
        target_weight = sum(record["multiplicity"] * final_weights[record["global_state_id"]]
                            for record in targets)
        row_load = fixed_offset + target_weight
        margin = parent_weight - row_load
        require(margin >= 0, f"{path}: negative global margin")
        if margin > 0:
            classification = "strict"
            strict_rows += 1
        else:
            require(targets, f"{path}: zero-margin row requires a descending target")
            parent_rank = rank_by_state[parent]
            require(all(rank_by_state[record["global_state_id"]] < parent_rank for record in targets),
                    f"{path}: zero-margin row fails strict rank descent")
            classification = "critical-descending"
            descending_rows += 1
        output = {
            "row_id": row_id,
            "kind": kind,
            "parent_global_state_id": parent,
            "parent_weight": parent_weight,
            "parent_rank": rank_by_state[parent],
            "fixed_offset": fixed_offset,
            "target_multiplicities": targets,
            "target_weight": target_weight,
            "row_load": row_load,
            "margin": margin,
            "classification": classification,
            "evidence": evidence,
        }
        output["interface_row_sha256"] = catalogue.canonical_digest(output)
        interface_records.append(output)
    require(interface_records == sorted(interface_records, key=lambda item: item["row_id"]),
            "interface_rows: canonical row_id order required")
    row_ids = [record["row_id"] for record in interface_records]
    require(len(row_ids) == len(set(row_ids)), "interface_rows: duplicate row_id")

    claims = {
        "scale_components": len(multipliers),
        "global_states": len(final_weight_records),
        "interface_rows": len(interface_records),
        "strict_interface_rows": strict_rows,
        "critical_descending_rows": descending_rows,
        "all_interface_rows_accepted": 1,
        "maximum_global_weight": max(final_weights.values()),
        "minimum_interface_margin": min([record["margin"] for record in interface_records], default=0),
        "weight_synchronization_sha256": synchronization_certificate["certificate_sha256"],
        "component_multipliers_sha256": catalogue.canonical_digest(multipliers),
        "state_ranks_sha256": catalogue.canonical_digest(ranks),
        "final_weights_sha256": catalogue.canonical_digest(final_weight_records),
        "interface_rows_sha256": catalogue.canonical_digest(interface_records),
    }
    return {
        "component_multipliers": multipliers,
        "state_ranks": ranks,
        "final_global_weight_records": final_weight_records,
        "interface_rows": interface_records,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("component_multipliers", "state_ranks", "final_global_weight_records", "interface_rows", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "components": claims["scale_components"],
        "states": claims["global_states"],
        "rows": claims["interface_rows"],
        "strict": claims["strict_interface_rows"],
        "descending": claims["critical_descending_rows"],
    }


def build_certificate(weight_synchronization_certificate: dict[str, Any],
                      component_multipliers: list[dict[str, Any]],
                      state_ranks: list[dict[str, Any]],
                      interface_rows: list[dict[str, Any]]) -> dict[str, Any]:
    multipliers = [exact_multiplier(record, "component_multiplier") for record in component_multipliers]
    multipliers.sort(key=lambda item: item["component_id"])
    ranks = [exact_rank(record, "state_rank") for record in state_ranks]
    ranks.sort(key=lambda item: item["global_state_id"])
    ordered_rows = sorted(interface_rows, key=lambda record: record["row_id"])
    certificate: dict[str, Any] = {
        "version": 1,
        "weight_synchronization_certificate": weight_synchronization_certificate,
        "component_multipliers": multipliers,
        "state_ranks": ranks,
        "interface_rows": ordered_rows,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_interface_return_rows.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
