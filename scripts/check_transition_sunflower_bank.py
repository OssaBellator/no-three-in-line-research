#!/usr/bin/env python3
"""Check the finite free-or-one-pool extraction from a transition sunflower."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{label}: expected a nonempty string")
    return value


def require_int(value: Any, label: str, *, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected an integer >= {minimum}")
    return value


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")

        pool_count = require_int(
            payload.get("controller_pool_count"),
            "controller_pool_count",
            minimum=1,
        )
        raw_records = payload.get("records")
        if not isinstance(raw_records, list) or not raw_records:
            raise ValueError("records must be a nonempty list")

        records: list[dict[str, Any]] = []
        seen_ids: set[str] = set()
        seen_anchors: set[str] = set()
        resource_owner: dict[str, str] = {}

        for index, raw in enumerate(raw_records):
            label = f"records[{index}]"
            if not isinstance(raw, dict):
                raise ValueError(f"{label}: expected an object")
            record_id = require_string(raw.get("id"), f"{label}.id")
            anchor = require_string(raw.get("anchor"), f"{label}.anchor")
            layer = require_string(raw.get("anchor_layer"), f"{label}.anchor_layer")
            pool = raw.get("anchor_pool")
            if pool is not None:
                pool = require_int(pool, f"{label}.anchor_pool")
                if pool >= pool_count:
                    raise ValueError(
                        f"{label}.anchor_pool: outside [0, controller_pool_count)"
                    )

            raw_resources = raw.get("resources")
            if not isinstance(raw_resources, list) or not raw_resources:
                raise ValueError(f"{label}.resources: expected a nonempty list")
            resources = [
                require_string(value, f"{label}.resources[{resource_index}]")
                for resource_index, value in enumerate(raw_resources)
            ]
            if len(set(resources)) != len(resources):
                raise ValueError(f"{label}.resources: duplicate resource inside one petal")
            if record_id in seen_ids:
                raise ValueError(f"duplicate record id {record_id!r}")
            if anchor in seen_anchors:
                raise ValueError(f"duplicate witness anchor {anchor!r}")
            seen_ids.add(record_id)
            seen_anchors.add(anchor)

            for resource in resources:
                previous = resource_owner.get(resource)
                if previous is not None:
                    raise ValueError(
                        f"resource {resource!r} occurs in both {previous!r} "
                        f"and {record_id!r}"
                    )
                resource_owner[resource] = record_id

            records.append(
                {
                    "id": record_id,
                    "anchor": anchor,
                    "anchor_layer": layer,
                    "anchor_pool": pool,
                    "resources": resources,
                }
            )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    layer_counts = Counter(record["anchor_layer"] for record in records)
    maximum_layer_size = max(layer_counts.values())
    selected_layer = min(
        layer for layer, count in layer_counts.items() if count == maximum_layer_size
    )
    layer_records = [
        record for record in records if record["anchor_layer"] == selected_layer
    ]

    free_records = [
        record for record in layer_records if record["anchor_pool"] is None
    ]
    pool_records: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for record in layer_records:
        pool = record["anchor_pool"]
        if pool is not None:
            pool_records[pool].append(record)

    candidates: list[tuple[int, str, list[dict[str, Any]]]] = [
        (len(free_records), "free", free_records)
    ]
    candidates.extend(
        (len(group), f"pool:{pool}", group)
        for pool, group in sorted(pool_records.items())
    )
    best_size = max(size for size, _, _ in candidates)
    _, selected_class, selected_records = min(
        candidate for candidate in candidates if candidate[0] == best_size
    )

    layer_size = len(layer_records)
    exact_bound = (layer_size + pool_count) // (pool_count + 1)
    if best_size < exact_bound:
        raise SystemExit(
            "check failed: extracted class violates ceil(L/(M+1)) pigeonhole bound"
        )

    result = {
        "petal_count": len(records),
        "pairwise_noncentral_resource_disjoint": True,
        "layer_counts": dict(sorted(layer_counts.items())),
        "selected_layer": selected_layer,
        "selected_layer_size": layer_size,
        "controller_pool_count": pool_count,
        "pigeonhole_lower_bound": exact_bound,
        "selected_class": selected_class,
        "selected_bank_size": best_size,
        "selected_record_ids": [record["id"] for record in selected_records],
        "selected_anchors": [record["anchor"] for record in selected_records],
        "certificate_removal_credit": best_size,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
