#!/usr/bin/env python3
"""Validate and merge a complete minimum-seven attempt-shard census."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("shards", nargs="+", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    payloads = [json.loads(path.read_text()) for path in args.shards]
    shard_counts = {payload["shard_count"] for payload in payloads}
    if len(shard_counts) != 1:
        raise AssertionError("inconsistent shard counts")
    shard_count = shard_counts.pop()
    by_index = {payload["shard_index"]: payload for payload in payloads}
    if len(by_index) != len(payloads):
        raise AssertionError("duplicate shard index")
    if set(by_index) != set(range(shard_count)):
        raise AssertionError({
            "missing": sorted(set(range(shard_count)) - set(by_index)),
            "extra": sorted(set(by_index) - set(range(shard_count))),
        })

    records = []
    seen_attempts = []
    for shard_index in range(shard_count):
        payload = by_index[shard_index]
        assert payload["frontier"] == "twenty-second raw minimum-seven layer"
        assert payload["budget"] == 7
        assert payload["total_attempts"] == 205
        assert payload["status"] == "passed"
        expected = list(range(shard_index, 205, shard_count))
        assert payload["attempt_indices"] == expected
        assert payload["core_records"] == len(payload["records"])
        assert payload["repairs"] == sum(
            record["repair_found"] for record in payload["records"]
        )
        seen_attempts.extend(expected)
        records.extend(payload["records"])

    assert sorted(seen_attempts) == list(range(205))
    keys = [(record["attempt_index"], record["core_index"]) for record in records]
    assert len(keys) == len(set(keys))
    records.sort(key=lambda record: (record["attempt_index"], record["core_index"]))

    output = {
        "frontier": "twenty-second raw minimum-seven layer",
        "budget": 7,
        "attempts": 205,
        "minimum_cores": len(records),
        "exact_cover_subsets_tested_until_stop": sum(
            record["exact_cover_subsets_tested_until_stop"] for record in records
        ),
        "exact_cover_nodes_tested_until_stop": sum(
            record["exact_cover_nodes_tested_until_stop"] for record in records
        ),
        "repairs": sum(record["repair_found"] for record in records),
        "records": records,
        "status": "passed",
        "warning": (
            "This merge proves complete shard coverage only. Repair witnesses still "
            "require independent coordinate audit and exact next-spectrum comparison."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "attempts": output["attempts"],
        "minimum_cores": output["minimum_cores"],
        "repairs": output["repairs"],
        "status": output["status"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
