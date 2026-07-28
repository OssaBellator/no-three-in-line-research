#!/usr/bin/env python3
"""Synchronize local block weights through explicit cross-block state identifications.

If two local states represent one global state, their scaled weights must agree. The checker
derives the exact rational scale ratios forced between blocks, rejects inconsistent cycles,
clears all denominators componentwise, and publishes minimal positive integer block
multipliers together with globally identified state weights and scaled block rows.

Disconnected block components remain independently normalized. A later interface layer may
choose one positive multiplier for each disconnected component.
"""
from __future__ import annotations

import json
import math
import sys
from collections import defaultdict, deque
from fractions import Fraction
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_cross_block_state_identification as identity


class WeightSynchronizationError(ValueError):
    """Raised when cross-block weight ratios are inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise WeightSynchronizationError(message)


def lcm(left: int, right: int) -> int:
    return abs(left * right) // math.gcd(left, right)


def local_weights(block_certificate: dict[str, Any]) -> dict[str, int]:
    policy = block_certificate["candidate_policy_certificate"]
    common = policy["recurrent_population_certificate"]["common_weight_certificate"]
    return {record["state_id"]: record["weight"] for record in common["state_weights"]}


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    identification = certificate.get("state_identification_certificate")
    require(isinstance(identification, dict), "state_identification_certificate: expected object")
    identity.validate_certificate(identification)
    identification_exact = identity.exact_certificate(identification)

    block_certificates = {
        record["block_id"]: record["certificate"] for record in identification_exact["integer_blocks"]
    }
    weights_by_block = {block_id: local_weights(cert) for block_id, cert in block_certificates.items()}
    link_by_local = {
        (record["block_id"], record["local_state_id"]): record["global_state_id"]
        for record in identification_exact["state_links"]
    }

    constraints: dict[str, list[tuple[str, Fraction, str]]] = defaultdict(list)
    global_members: dict[str, list[tuple[str, str]]] = {}
    for global_record in identification_exact["global_state_records"]:
        members = [(item["block_id"], item["local_state_id"]) for item in global_record["members"]]
        global_members[global_record["global_state_id"]] = members
        if not members:
            continue
        base_block, base_state = members[0]
        base_weight = weights_by_block[base_block][base_state]
        for other_block, other_state in members[1:]:
            other_weight = weights_by_block[other_block][other_state]
            ratio = Fraction(base_weight, other_weight)
            constraints[base_block].append((other_block, ratio, global_record["global_state_id"]))
            constraints[other_block].append((base_block, Fraction(1, 1) / ratio, global_record["global_state_id"]))

    unvisited = set(block_certificates)
    component_records = []
    block_multiplier: dict[str, int] = {}
    block_component: dict[str, str] = {}

    while unvisited:
        root = min(unvisited)
        scales: dict[str, Fraction] = {root: Fraction(1, 1)}
        queue = deque([root])
        component_blocks = []
        while queue:
            block_id = queue.popleft()
            component_blocks.append(block_id)
            for neighbor, ratio, global_state_id in constraints.get(block_id, []):
                proposed = scales[block_id] * ratio
                if neighbor in scales:
                    require(scales[neighbor] == proposed,
                            f"weight ratio conflict through global state {global_state_id}")
                else:
                    scales[neighbor] = proposed
                    queue.append(neighbor)
        component_blocks = sorted(set(component_blocks))
        unvisited -= set(component_blocks)

        denominator = 1
        for scale in scales.values():
            denominator = lcm(denominator, scale.denominator)
        raw_multipliers = {block_id: int(scales[block_id] * denominator) for block_id in component_blocks}
        common_gcd = math.gcd(*raw_multipliers.values())
        multipliers = {block_id: raw_multipliers[block_id] // common_gcd for block_id in component_blocks}
        component_states = sorted(
            global_state_id
            for global_state_id, members in global_members.items()
            if any(block_id in component_blocks for block_id, _ in members)
        )
        component_core = {"block_ids": component_blocks, "global_state_ids": component_states}
        component_id = f"scale-{catalogue.canonical_digest(component_core)[:24]}"
        for block_id in component_blocks:
            block_multiplier[block_id] = multipliers[block_id]
            block_component[block_id] = component_id
        multiplier_records = [
            {"block_id": block_id, "multiplier": multipliers[block_id]}
            for block_id in component_blocks
        ]
        for record in multiplier_records:
            record["multiplier_record_sha256"] = catalogue.canonical_digest(record)
        component = {
            "component_id": component_id,
            "block_ids": component_blocks,
            "global_state_ids": component_states,
            "block_multipliers": multiplier_records,
            "multiplier_gcd": math.gcd(*(record["multiplier"] for record in multiplier_records)),
        }
        component["scale_component_sha256"] = catalogue.canonical_digest(component)
        component_records.append(component)

    component_records.sort(key=lambda item: item["component_id"])

    global_record_by_id = {
        record["global_state_id"]: record for record in identification_exact["global_state_records"]
    }
    global_weight_records = []
    for global_state_id in sorted(global_members):
        values = []
        for block_id, local_state_id in global_members[global_state_id]:
            values.append(block_multiplier[block_id] * weights_by_block[block_id][local_state_id])
        require(len(set(values)) == 1, f"global state {global_state_id}: synchronized weights differ")
        component_ids = {block_component[block_id] for block_id, _ in global_members[global_state_id]}
        require(len(component_ids) == 1, f"global state {global_state_id}: spans disconnected scale components")
        source = global_record_by_id[global_state_id]
        record = {
            "global_state_id": global_state_id,
            "component_id": next(iter(component_ids)),
            "role": source["role"],
            "stratum": source["stratum"],
            "owner": source["owner"],
            "component_weight": values[0],
            "member_count": source["member_count"],
        }
        record["global_weight_record_sha256"] = catalogue.canonical_digest(record)
        global_weight_records.append(record)

    global_weights = {record["global_state_id"]: record["component_weight"] for record in global_weight_records}
    scaled_rows = []
    for block_record in identification_exact["integer_blocks"]:
        block_id = block_record["block_id"]
        block_certificate = block_record["certificate"]
        multiplier = block_multiplier[block_id]
        component_id = block_component[block_id]
        local_columns = block_certificate["integer_block"]["column_state_ids"]
        for row in block_certificate["quotient_row_records"]:
            parent_global = link_by_local[(block_id, row["parent_state_id"])]
            target_counts: dict[str, int] = defaultdict(int)
            for local_state_id, coefficient in zip(local_columns, row["target_vector"]):
                if coefficient:
                    target_counts[link_by_local[(block_id, local_state_id)]] += coefficient
            targets = [[state_id, target_counts[state_id]] for state_id in sorted(target_counts)]
            scaled_parent_weight = multiplier * row["parent_weight"]
            scaled_fixed = multiplier * row["net_fixed_offset"]
            scaled_margin = multiplier * row["margin"]
            require(scaled_parent_weight == global_weights[parent_global],
                    f"block {block_id}: parent global weight mismatch")
            target_weight = sum(value * global_weights[state_id] for state_id, value in targets)
            require(scaled_parent_weight - scaled_fixed - target_weight == scaled_margin,
                    f"block {block_id}: scaled row identity failed")
            output = {
                "block_id": block_id,
                "component_id": component_id,
                "local_parent_state_id": row["parent_state_id"],
                "global_parent_state_id": parent_global,
                "selected_slot_id": row["selected_slot_id"],
                "selected_fibre_id": row["selected_fibre_id"],
                "selected_response": row["selected_response"],
                "block_multiplier": multiplier,
                "scaled_parent_weight": scaled_parent_weight,
                "scaled_fixed_offset": scaled_fixed,
                "global_target_multiplicities": targets,
                "scaled_target_weight": target_weight,
                "scaled_margin": scaled_margin,
            }
            output["scaled_block_row_sha256"] = catalogue.canonical_digest(output)
            scaled_rows.append(output)
    scaled_rows.sort(key=lambda item: (item["component_id"], item["block_id"], item["global_parent_state_id"]))

    claims = {
        "blocks": len(block_certificates),
        "scale_components": len(component_records),
        "global_states": len(global_weight_records),
        "scaled_rows": len(scaled_rows),
        "shared_global_states": sum(record["member_count"] > 1 for record in global_weight_records),
        "maximum_block_multiplier": max(block_multiplier.values()),
        "minimum_scaled_margin": min(record["scaled_margin"] for record in scaled_rows),
        "exact_ratio_consistency": 1,
        "state_identification_sha256": identification["certificate_sha256"],
        "scale_components_sha256": catalogue.canonical_digest(component_records),
        "global_weights_sha256": catalogue.canonical_digest(global_weight_records),
        "scaled_rows_sha256": catalogue.canonical_digest(scaled_rows),
    }
    return {
        "scale_components": component_records,
        "global_weight_records": global_weight_records,
        "scaled_block_rows": scaled_rows,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("scale_components", "global_weight_records", "scaled_block_rows", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "blocks": claims["blocks"],
        "components": claims["scale_components"],
        "states": claims["global_states"],
        "rows": claims["scaled_rows"],
        "exact": claims["exact_ratio_consistency"],
    }


def build_certificate(state_identification_certificate: dict[str, Any]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "state_identification_certificate": state_identification_certificate,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_cross_block_weight_synchronization.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
