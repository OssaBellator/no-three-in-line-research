#!/usr/bin/env python3
"""Validate the terminal routing table for the completed local prime-patching frontier."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any

EXPECTED_RAW = {"independent", "dense_current", "dense_source"}
FORBIDDEN_RAW = {
    "hall_failure", "alternating_failure", "non_superregular_failure",
    "role_host_failure", "coordinate_shortage", "distinguished_endpoint_failure",
    "locally_impossible", "raw_source_host",
}
TERMINALS = {"paid_progress", "patch_completion", "source_valid_joint_completion"}
ALLOWED = {
    "fixed_attempt_failure": {"source_valid_first_package", "paid_progress", "patch_completion"},
    "source_valid_first_package": {"second_host"},
    "second_host": EXPECTED_RAW,
    "independent": {"paid_progress"},
    "dense_current": {"paid_progress", "patch_completion", "dense_source"},
    "dense_source": TERMINALS,
}

def analyse(data: dict[str, Any]) -> dict[str, Any]:
    W = int(data["W"])
    marked = int(data["marked_scale"])
    helpers = int(data["helper_reservoir"])
    role_loss = int(data["role_loss"])
    support_rank = int(data["support_rank"])
    routes = {str(k): set(map(str, v)) for k, v in data["routes"].items()}

    hypotheses = {
        "marked_scale_ok": 1 <= marked <= W,
        "quadratic_helpers_ok": helpers >= marked * marked,
        "linear_role_loss_ok": role_loss <= marked,
        "rank_three_support_ok": support_rank <= 3,
    }
    raw = routes.get("second_host", set())
    raw_exact = raw == EXPECTED_RAW
    forbidden_present = sorted(set().union(*routes.values()) & FORBIDDEN_RAW) if routes else []

    route_mismatches = {}
    for node, expected in ALLOWED.items():
        actual = routes.get(node, set())
        if actual != expected:
            route_mismatches[node] = {"expected": sorted(expected), "actual": sorted(actual)}

    def reaches_terminal(start: str) -> bool:
        stack=[start]; seen=set()
        while stack:
            node=stack.pop()
            if node in TERMINALS:
                return True
            if node in seen:
                continue
            seen.add(node)
            stack.extend(routes.get(node, ()))
        return False

    nonterminal_nodes=sorted(ALLOWED)
    reachability={node: reaches_terminal(node) for node in nonterminal_nodes}
    all_terminal=all(reachability.values())
    ok = all(hypotheses.values()) and raw_exact and not forbidden_present and not route_mismatches and all_terminal
    return {
        **hypotheses,
        "raw_second_host_outcomes": sorted(raw),
        "raw_trichotomy_exact": raw_exact,
        "forbidden_raw_leaves_present": forbidden_present,
        "route_mismatches": route_mismatches,
        "terminal_reachability": reachability,
        "all_local_routes_terminal": all_terminal,
        "outcome": "local_frontier_terminal" if ok else "routing_or_hypothesis_failure",
    }

def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args=parser.parse_args()
    data=json.loads(args.input.read_text(encoding="utf-8"))
    print(json.dumps(analyse(data), indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
