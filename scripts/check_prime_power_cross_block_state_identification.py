#!/usr/bin/env python3
"""Identify local states across denominator-cleared recurrent quotient blocks.

Each integer recurrent block has a complete local state registry inherited from its common
weight certificate. This checker requires one explicit local-to-global link for every local
state, rejects missing or duplicate coverage, and verifies that all local members of one
global state have identical role, stratum and owner data.

Passing this checker proves exact cross-block state identification relative to the supplied
links. It does not prove that the links have their intended external mathematical meaning.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_integer_recurrent_quotient_block as integer_block


class CrossBlockStateError(ValueError):
    """Raised when local-to-global state identification is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CrossBlockStateError(message)


def state_core(record: dict[str, Any]) -> dict[str, Any]:
    state_id = record.get("id")
    role = record.get("role")
    stratum = record.get("stratum")
    owner = record.get("owner")
    require(isinstance(state_id, str) and state_id, "state.id: nonempty string required")
    require(role in {"recurrent", "offdiagonal", "auxiliary", "sink"}, f"state {state_id}: bad role")
    require(type(stratum) is int and stratum >= 0, f"state {state_id}: bad stratum")
    require(owner is None or (isinstance(owner, list) and len(owner) == 2), f"state {state_id}: bad owner")
    return {"id": state_id, "role": role, "stratum": stratum, "owner": copy.deepcopy(owner)}


def local_state_registry(block_certificate: dict[str, Any]) -> dict[str, dict[str, Any]]:
    policy = block_certificate["candidate_policy_certificate"]
    population = policy["recurrent_population_certificate"]
    common = population["common_weight_certificate"]
    states: dict[str, dict[str, Any]] = {}
    for routed in common["routed_row_certificates"]:
        source = routed["row_margin_certificate"]["linked_operation_certificate"]["linkage_certificate"]["source_manifest"]
        for raw in source["states"]:
            core = state_core(raw)
            if core["id"] in states:
                require(states[core["id"]] == core, f"state {core['id']}: definition drift inside block")
            else:
                states[core["id"]] = core
    return states


def exact_block_record(record: dict[str, Any], path: str) -> dict[str, Any]:
    block_id = record.get("block_id")
    certificate = record.get("certificate")
    require(isinstance(block_id, str) and block_id, f"{path}.block_id: required")
    require(isinstance(certificate, dict), f"{path}.certificate: expected object")
    integer_block.validate_certificate(certificate)
    states = local_state_registry(certificate)
    output = {
        "block_id": block_id,
        "certificate": certificate,
        "certificate_sha256": certificate["certificate_sha256"],
        "local_states": len(states),
        "local_state_ids_sha256": catalogue.canonical_digest(sorted(states)),
    }
    output["block_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_link_record(record: dict[str, Any], path: str) -> dict[str, Any]:
    block_id = record.get("block_id")
    local_state_id = record.get("local_state_id")
    global_state_id = record.get("global_state_id")
    evidence = record.get("evidence")
    require(isinstance(block_id, str) and block_id, f"{path}.block_id: required")
    require(isinstance(local_state_id, str) and local_state_id, f"{path}.local_state_id: required")
    require(isinstance(global_state_id, str) and global_state_id, f"{path}.global_state_id: required")
    require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
    output = {
        "block_id": block_id,
        "local_state_id": local_state_id,
        "global_state_id": global_state_id,
        "evidence": evidence,
    }
    output["state_link_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    raw_blocks = certificate.get("integer_blocks")
    raw_links = certificate.get("state_links")
    require(isinstance(raw_blocks, list) and raw_blocks, "integer_blocks: nonempty list required")
    require(isinstance(raw_links, list) and raw_links, "state_links: nonempty list required")

    blocks = [exact_block_record(record, f"integer_blocks[{index}]") for index, record in enumerate(raw_blocks)]
    require(raw_blocks == blocks, "integer_blocks: canonical records or digests required")
    require(blocks == sorted(blocks, key=lambda item: item["block_id"]), "integer_blocks: canonical block order required")
    block_ids = [record["block_id"] for record in blocks]
    require(len(block_ids) == len(set(block_ids)), "integer_blocks: duplicate block_id")

    states_by_block = {record["block_id"]: local_state_registry(record["certificate"]) for record in blocks}
    expected_local_refs = {
        (block_id, state_id)
        for block_id, states in states_by_block.items()
        for state_id in states
    }

    links = [exact_link_record(record, f"state_links[{index}]") for index, record in enumerate(raw_links)]
    require(raw_links == links, "state_links: canonical records or digests required")
    require(
        links == sorted(links, key=lambda item: (item["global_state_id"], item["block_id"], item["local_state_id"])),
        "state_links: canonical global/block/local order required",
    )
    local_refs = [(record["block_id"], record["local_state_id"]) for record in links]
    require(len(local_refs) == len(set(local_refs)), "state_links: local state linked more than once")
    require(set(local_refs) == expected_local_refs, "state_links: must cover every local state exactly")
    for record in links:
        require(record["block_id"] in states_by_block, f"state link: unknown block {record['block_id']}")
        require(
            record["local_state_id"] in states_by_block[record["block_id"]],
            f"state link: unknown local state {record['block_id']}:{record['local_state_id']}",
        )

    by_global: dict[str, list[dict[str, Any]]] = {}
    for link in links:
        local = states_by_block[link["block_id"]][link["local_state_id"]]
        member = {
            "block_id": link["block_id"],
            "local_state_id": link["local_state_id"],
            "role": local["role"],
            "stratum": local["stratum"],
            "owner": local["owner"],
            "evidence": link["evidence"],
            "state_link_sha256": link["state_link_sha256"],
        }
        by_global.setdefault(link["global_state_id"], []).append(member)

    global_records = []
    role_counts: Counter[str] = Counter()
    shared_classes = 0
    block_overlap_edges: set[tuple[str, str]] = set()
    for global_state_id in sorted(by_global):
        members = sorted(by_global[global_state_id], key=lambda item: (item["block_id"], item["local_state_id"]))
        semantic_cores = {(item["role"], item["stratum"], json.dumps(item["owner"], sort_keys=True)) for item in members}
        require(len(semantic_cores) == 1, f"global state {global_state_id}: semantic definition drift")
        role = members[0]["role"]
        stratum = members[0]["stratum"]
        owner = members[0]["owner"]
        role_counts[role] += 1
        shared_classes += int(len(members) > 1)
        member_blocks = sorted({item["block_id"] for item in members})
        for left_index, left in enumerate(member_blocks):
            for right in member_blocks[left_index + 1:]:
                block_overlap_edges.add((left, right))
        record = {
            "global_state_id": global_state_id,
            "role": role,
            "stratum": stratum,
            "owner": owner,
            "members": members,
            "member_count": len(members),
            "member_blocks": member_blocks,
        }
        record["global_state_record_sha256"] = catalogue.canonical_digest(record)
        global_records.append(record)

    claims = {
        "blocks": len(blocks),
        "local_states": len(links),
        "global_states": len(global_records),
        "shared_global_states": shared_classes,
        "maximum_class_size": max(record["member_count"] for record in global_records),
        "block_overlap_edges": len(block_overlap_edges),
        "role_distribution": [[role, role_counts[role]] for role in sorted(role_counts)],
        "complete_local_state_coverage": 1,
        "integer_blocks_sha256": catalogue.canonical_digest(blocks),
        "state_links_sha256": catalogue.canonical_digest(links),
        "global_states_sha256": catalogue.canonical_digest(global_records),
        "block_overlap_edges_sha256": catalogue.canonical_digest([list(edge) for edge in sorted(block_overlap_edges)]),
    }
    return {"integer_blocks": blocks, "state_links": links, "global_state_records": global_records, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("integer_blocks", "state_links", "global_state_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "blocks": claims["blocks"],
        "local_states": claims["local_states"],
        "global_states": claims["global_states"],
        "shared": claims["shared_global_states"],
        "complete": claims["complete_local_state_coverage"],
    }


def build_certificate(integer_blocks: list[dict[str, Any]], state_links: list[dict[str, Any]]) -> dict[str, Any]:
    blocks = [exact_block_record(record, "integer_block") for record in integer_blocks]
    blocks.sort(key=lambda item: item["block_id"])
    links = [exact_link_record(record, "state_link") for record in state_links]
    links.sort(key=lambda item: (item["global_state_id"], item["block_id"], item["local_state_id"]))
    certificate: dict[str, Any] = {"version": 1, "integer_blocks": blocks, "state_links": links}
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_cross_block_state_identification.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
