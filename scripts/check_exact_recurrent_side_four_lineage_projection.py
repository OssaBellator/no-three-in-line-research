#!/usr/bin/env python3
"""Audit the exact join from the local side-four residual kernel to upstream lineage IDs.

This is a provenance-gap certificate, not a global repair or no-three-in-line proof.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any


class LineageAuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise LineageAuditError(message)


def edge_key(values: Any, context: str) -> tuple[str, ...]:
    require(isinstance(values, list) and values, f"{context}: nonempty edge list required")
    require(
        all(
            isinstance(value, str)
            and len(value) == 2
            and value.isdigit()
            for value in values
        ),
        f"{context}: invalid edge code",
    )
    require(len(values) == len(set(values)), f"{context}: duplicate edge")
    return tuple(sorted(values))


def response_key(values: Any, context: str) -> tuple[str, ...]:
    require(isinstance(values, list) and values, f"{context}: nonempty response list required")
    parsed: list[str] = []
    for value in values:
        require(isinstance(value, str) and ":" in value, f"{context}: malformed response")
        permutation, count = value.split(":", 1)
        require(len(permutation) == 4 and permutation.isdigit(), f"{context}: bad permutation")
        require(count.isdigit(), f"{context}: bad triple count")
        parsed.append(f"{permutation}:{int(count)}")
    require(len(parsed) == len(set(parsed)), f"{context}: duplicate response")
    return tuple(sorted(parsed))


def validate(kernel: dict[str, Any], projection: dict[str, Any]) -> dict[str, Any]:
    require(
        kernel.get("schema") == "exact-recurrent-side-four-host-kernel/v1",
        "kernel schema mismatch",
    )
    require(
        projection.get("schema")
        == "exact-recurrent-side-four-lineage-projection/v1",
        "projection schema mismatch",
    )

    source = projection.get("source")
    require(isinstance(source, dict), "source object required")
    require(
        source.get("source_schema")
        == "prime-power-side-four-raw-fibre-lineage-manifest/v1",
        "source schema mismatch",
    )
    source_honesty = source.get("source_honesty")
    require(isinstance(source_honesty, dict), "source honesty required")
    expected_source_honesty = {
        "coordinate_host_response": 1,
        "global_owner_fate_collision_interface_crt": 0,
        "all_recurrent_states_populated": 0,
        "compulsory_weighted_rows_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    require(source_honesty == expected_source_honesty, "source honesty changed")

    blockers = projection.get("blockers")
    require(isinstance(blockers, list) and len(blockers) == 3, "three blockers required")
    blocker_by_edges: dict[tuple[str, ...], str] = {}
    blocker_ids: set[str] = set()
    for index, blocker in enumerate(blockers):
        require(isinstance(blocker, dict), f"blocker[{index}] object required")
        upstream_id = blocker.get("upstream_id")
        require(
            isinstance(upstream_id, str) and upstream_id.startswith("b4-"),
            f"blocker[{index}] id",
        )
        require(upstream_id not in blocker_ids, f"duplicate blocker id {upstream_id}")
        edges = edge_key(blocker.get("edges"), f"blocker[{index}]")
        require(edges not in blocker_by_edges, f"duplicate blocker edges {edges}")
        blocker_ids.add(upstream_id)
        blocker_by_edges[edges] = upstream_id

    kernel_blockers = {
        edge_key(item.get("edges"), f"kernel blocker[{index}]")
        for index, item in enumerate(
            kernel.get("minimal_good_response_blockers", [])
        )
    }
    require(kernel_blockers == set(blocker_by_edges), "blocker basis join mismatch")

    local_hosts = kernel.get("residual_hosts")
    projected_hosts = projection.get("residual_hosts")
    require(
        isinstance(local_hosts, list) and len(local_hosts) == 11,
        "kernel must contain eleven residual hosts",
    )
    require(
        isinstance(projected_hosts, list) and len(projected_hosts) == 11,
        "projection must contain eleven residual hosts",
    )

    local_by_deletions: dict[tuple[str, ...], dict[str, Any]] = {}
    for index, host in enumerate(local_hosts):
        require(isinstance(host, dict), f"kernel host[{index}] object required")
        deletions = edge_key(host.get("deletions"), f"kernel host[{index}]")
        require(
            deletions not in local_by_deletions,
            f"duplicate kernel host {deletions}",
        )
        local_by_deletions[deletions] = host

    required_slots = (
        "background",
        "deletion_causes",
        "owner",
        "fate",
        "collision",
        "line",
        "interface",
        "crt",
        "legal_operations",
        "child_rows",
    )
    projected_keys: set[tuple[str, ...]] = set()
    upstream_ids: set[str] = set()
    deletion_cause_slots = 0

    for index, host in enumerate(projected_hosts):
        require(isinstance(host, dict), f"projection host[{index}] object required")
        upstream_id = host.get("upstream_id")
        require(
            isinstance(upstream_id, str) and upstream_id.startswith("s4-"),
            f"projection host[{index}] id",
        )
        require(
            upstream_id not in upstream_ids,
            f"duplicate upstream host id {upstream_id}",
        )
        upstream_ids.add(upstream_id)

        deletions = edge_key(host.get("deletions"), f"projection host[{index}]")
        require(deletions not in projected_keys, f"duplicate projected host {deletions}")
        projected_keys.add(deletions)
        require(
            deletions in local_by_deletions,
            f"projected host absent locally: {deletions}",
        )
        local = local_by_deletions[deletions]

        expected_responses = tuple(
            sorted(
                f"{item['permutation']}:{item['intrinsic_triples']}"
                for item in local.get("surviving_bad_responses", [])
            )
        )
        require(
            response_key(
                host.get("response_spectrum"),
                f"projection host[{index}]",
            )
            == expected_responses,
            f"response join mismatch for {deletions}",
        )
        require(
            host.get("dispatch") == "blocker-alternative",
            f"dispatch mismatch for {deletions}",
        )

        expected_blockers = tuple(
            sorted(
                blocker_by_edges[
                    edge_key(edges, f"local active blocker {deletions}")
                ]
                for edges in local.get("active_minimal_blockers", [])
            )
        )
        contained = host.get("contained_blockers")
        require(
            isinstance(contained, list)
            and all(value in blocker_ids for value in contained),
            f"contained blockers invalid for {deletions}",
        )
        require(
            tuple(sorted(contained)) == expected_blockers,
            f"blocker join mismatch for {deletions}",
        )

        slots = host.get("provenance_slots")
        require(
            isinstance(slots, dict) and set(slots) == set(required_slots),
            f"provenance slot schema mismatch for {deletions}",
        )
        require(
            all(slots[name] is None for name in required_slots),
            f"unsupported provenance populated for {deletions}",
        )
        deletion_cause_slots += len(deletions)

    require(
        projected_keys == set(local_by_deletions),
        "lineage projection is not bijective",
    )

    honesty = projection.get("honesty")
    expected_honesty = {
        "coordinate_lineage_projection_complete": 1,
        "backgrounds_populated": 0,
        "deletion_causes_populated": 0,
        "owner_fate_collision_line_interface_crt_populated": 0,
        "legal_operations_populated": 0,
        "recurrent_offspring_rows_populated": 0,
        "strict_lyapunov_certificate_proved": 0,
        "all_n_proved_by_checker": 0,
    }
    require(honesty == expected_honesty, "projection honesty changed")

    return {
        "joined_residual_hosts": len(projected_hosts),
        "joined_blocker_classes": len(blockers),
        "missing_deletion_cause_assignments": deletion_cause_slots,
        "missing_background_records": len(projected_hosts),
        "missing_owner_fate_collision_line_interface_crt_fields": 6
        * len(projected_hosts),
        "missing_legal_operation_families": len(projected_hosts),
        "missing_recurrent_child_rows": len(projected_hosts),
        "coordinate_lineage_projection_complete": 1,
        "provenance_complete": 0,
        "strict_lyapunov_certificate_proved": 0,
        "all_n_proved_by_checker": 0,
    }


def mutation_audit(kernel: dict[str, Any], projection: dict[str, Any]) -> int:
    mutations = [
        lambda item: item.update(schema="wrong"),
        lambda item: item["residual_hosts"].pop(),
        lambda item: item["residual_hosts"][1].update(
            upstream_id=item["residual_hosts"][0]["upstream_id"]
        ),
        lambda item: item["residual_hosts"][0].update(
            deletions=["02", "31"]
        ),
        lambda item: item["residual_hosts"][0].update(
            response_spectrum=["3012:2"]
        ),
        lambda item: item["residual_hosts"][0].update(
            contained_blockers=[]
        ),
        lambda item: item["residual_hosts"][0]["provenance_slots"].update(
            owner="invented"
        ),
        lambda item: item["source"]["source_honesty"].update(
            global_owner_fate_collision_interface_crt=1
        ),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(projection)
        mutate(candidate)
        try:
            validate(kernel, candidate)
        except (LineageAuditError, KeyError, TypeError, ValueError):
            rejected += 1
    require(
        rejected == len(mutations),
        "mutation audit accepted a corrupted projection",
    )
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kernel", type=Path, required=True)
    parser.add_argument("--projection", type=Path, required=True)
    args = parser.parse_args()
    kernel = json.loads(args.kernel.read_text(encoding="utf-8"))
    projection = json.loads(args.projection.read_text(encoding="utf-8"))
    result = validate(kernel, projection)
    result["mutation_corruptions_rejected"] = mutation_audit(
        kernel,
        projection,
    )
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
