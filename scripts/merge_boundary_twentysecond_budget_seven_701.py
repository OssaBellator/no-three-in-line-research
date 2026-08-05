#!/usr/bin/env python3
"""Validate and merge a complete set of budget-seven shard records."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("shards", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payloads = [json.loads(path.read_text()) for path in args.shards]
    if not payloads:
        raise SystemExit("at least one shard is required")

    shard_counts = {payload["shard_count"] for payload in payloads}
    if len(shard_counts) != 1:
        raise AssertionError(f"inconsistent shard counts: {sorted(shard_counts)}")
    shard_count = shard_counts.pop()
    by_shard = {payload["shard_index"]: payload for payload in payloads}
    if len(by_shard) != len(payloads):
        raise AssertionError("duplicate shard index")
    if set(by_shard) != set(range(shard_count)):
        missing = sorted(set(range(shard_count)) - set(by_shard))
        extra = sorted(set(by_shard) - set(range(shard_count)))
        raise AssertionError({"missing_shards": missing, "extra_shards": extra})

    records = []
    for shard_index in range(shard_count):
        payload = by_shard[shard_index]
        assert payload["frontier"] == "twenty-second"
        assert payload["budget"] == 7
        assert payload["total_core_jobs"] == 178
        assert payload["status"] == "passed"
        assert payload["job_count"] == len(payload["records"])
        assert payload["global_indices"] == [
            record["global_index"] for record in payload["records"]
        ]
        for record in payload["records"]:
            assert record["global_index"] % shard_count == shard_index
        records.extend(payload["records"])

    records.sort(key=lambda record: record["global_index"])
    indices = [record["global_index"] for record in records]
    if indices != list(range(178)):
        raise AssertionError("shards do not form the exact 0..177 core partition")

    repairs = [record for record in records if record["repair_found"]]
    merged = {
        "frontier": "twenty-second",
        "budget": 7,
        "core_jobs": len(records),
        "complete_partition": True,
        "repairs_found": len(repairs),
        "repair_positive_core_indices": [
            record["global_index"] for record in repairs
        ],
        "replacement_permutations_tested_until_stop": sum(
            record["replacement_permutations_tested_until_stop"]
            for record in records
        ),
        "records": records,
        "status": "passed",
        "warning": (
            "This merge certifies the complete existence census only.  Any positive "
            "core still requires witness extraction, exact global no-three audit, "
            "and next-spectrum comparison before continuation selection."
        ),
    }
    rendered = json.dumps(merged, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
