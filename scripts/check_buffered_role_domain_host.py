#!/usr/bin/env python3
"""Check the buffered role-domain square-root helper theorem."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def maximum_role_matching(domains: list[list[int]]) -> tuple[int, list[int | None]]:
    helper_to_role: dict[int, int] = {}

    def augment(role: int, seen: set[int]) -> bool:
        for helper in domains[role]:
            if helper in seen:
                continue
            seen.add(helper)
            old_role = helper_to_role.get(helper)
            if old_role is None or augment(old_role, seen):
                helper_to_role[helper] = role
                return True
        return False

    matched = 0
    for role in range(len(domains)):
        matched += int(augment(role, set()))

    assignment: list[int | None] = [None] * len(domains)
    for helper, role in helper_to_role.items():
        assignment[role] = helper
    return matched, assignment


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())

    s = int(data["marked_size"])
    n = int(data["helper_reservoir"])
    kappa = int(data["domain_loss_constant"])
    step = int(data["cyclic_exclusion_step"])
    buffer_size = (kappa + 1) * s

    if buffer_size > n:
        raise AssertionError("buffer does not fit in the helper reservoir")

    buffer = set(range(buffer_size))
    domains: list[list[int]] = []
    excluded_per_role = kappa * s
    for role in range(s):
        excluded = {(step * role + offset) % n for offset in range(excluded_per_role)}
        domains.append(sorted(buffer - excluded))

    minimum_allowed = min(map(len, domains))
    matched, assignment = maximum_role_matching(domains)
    if minimum_allowed < s:
        raise AssertionError("buffered Hall lower bound failed")
    if matched != s or any(value is None for value in assignment):
        raise AssertionError("role-domain matching did not cover every role")
    if len(set(assignment)) != s:
        raise AssertionError("assigned helpers are not distinct")

    n2_threshold = n * (n - 1) / (2 * buffer_size * (buffer_size - 1))
    n3_threshold = (
        n * (n - 1) * (n - 2)
        / (2 * buffer_size * (buffer_size - 1) * (buffer_size - 2))
    )
    complete_graph_edges = n * (n - 1) // 2
    complete_graph_matching = n // 2
    complete_triples = n * (n - 1) * (n - 2) // 6

    print("marked roles", s)
    print("helper reservoir", n)
    print("domain loss constant", kappa)
    print("excluded per role", excluded_per_role)
    print("buffer size", buffer_size)
    print("allowed counts in buffer", [len(domain) for domain in domains])
    print("minimum allowed", minimum_allowed)
    print("role matching size", matched)
    print("role assignment", assignment)
    print("rank-two failure threshold", n2_threshold)
    print("complete rank-two support", complete_graph_edges)
    print("rank-two matching size", complete_graph_matching)
    print("rank-three failure threshold", n3_threshold)
    print("complete rank-three support", complete_triples)
    print("outcome", "buffered_role_domain_square_root_host")


if __name__ == "__main__":
    main()
