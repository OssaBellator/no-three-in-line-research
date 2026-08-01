#!/usr/bin/env python3
"""Check complete state exclusion, essential cores and distinguishing rank."""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
from typing import Any

from target_anchor_common import (
    Edge, Matching,
    essential_core as matching_essential_core,
    perfect_matchings, permutation_states,
)


class BranchRankError(RuntimeError):
    pass


def need(ok: bool, message: str) -> None:
    if not ok:
        raise BranchRankError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def family_core(family: tuple[frozenset[Any], ...]) -> frozenset[Any]:
    need(bool(family), "family required")
    core = set(family[0])
    for state in family[1:]:
        core &= set(state)
    return frozenset(core)


def child_family(family: tuple[frozenset[Any], ...], edge: Any) -> tuple[frozenset[Any], ...]:
    return tuple(state for state in family if edge not in state)


def distinguishing_rank(family: tuple[frozenset[Any], ...], rejected: frozenset[Any]) -> int:
    alternatives = [state for state in family if state != rejected]
    if not alternatives:
        return 0
    items = sorted(rejected)
    for size in range(len(items) + 1):
        for subset in itertools.combinations(items, size):
            chosen = set(subset)
            if all(not chosen.issubset(state) for state in alternatives):
                return size
    raise AssertionError("rejected state itself always distinguishes")


def complete_branch_audit() -> dict[str, int]:
    states = tuple(frozenset(state) for state in permutation_states(3))
    need(len(states) == 12 and all(len(state) == 6 for state in states),
         "side-three equal-cardinality family")
    families = nodes = union_checks = viability_checks = contraction_checks = 0
    zero_child = one_child = genuine_branch = compressed_covers = 0
    total_core_rank = total_viable_children = 0
    for mask in range(1, 1 << len(states)):
        family = tuple(states[i] for i in range(len(states)) if mask >> i & 1)
        families += 1
        core = family_core(family)
        residual = tuple(frozenset(state - core) for state in family)
        if residual:
            need(not family_core(residual), "CMR841 residual core nonempty")
        contraction_checks += 1
        for rejected in family:
            nodes += 1
            alternatives = set(family) - {rejected}
            union = set()
            viable = []
            for edge in rejected:
                child = child_family(family, edge)
                if child:
                    viable.append(edge)
                    union.update(child)
                need(bool(child) == (edge not in core), "CMR839 viability mismatch")
                viability_checks += 1
            need(union == alternatives, "CMR830/831 exclusion union")
            union_checks += 1
            need(len(viable) == len(rejected) - len(core), "viable count")
            need(len(core) + len(viable) == len(rejected), "CMR842 conservation")
            total_core_rank += len(core)
            total_viable_children += len(viable)
            if len(viable) == 0:
                need(len(family) == 1, "CMR843 zero child not singleton")
                zero_child += 1
            elif len(viable) == 1:
                need(set(child_family(family, viable[0])) == alternatives,
                     "CMR843 deterministic child")
                one_child += 1
            else:
                genuine_branch += 1
            delta = distinguishing_rank(family, rejected)
            need(delta <= len(viable), "distinguishing rank exceeds branch width")
            found = False
            for subset in itertools.combinations(sorted(rejected), delta):
                cover = set()
                for edge in subset:
                    cover.update(child_family(family, edge))
                if cover == alternatives:
                    found = True
                    break
            need(found, "CMR847 compressed cover missing")
            compressed_covers += 1
    return {
        "equal_cardinality_state_families": families,
        "state_exclusion_nodes": nodes,
        "exact_exclusion_union_checks": union_checks,
        "viable_child_core_checks": viability_checks,
        "complete_core_contraction_checks": contraction_checks,
        "zero_child_nodes": zero_child,
        "one_child_nodes": one_child,
        "genuine_branch_nodes": genuine_branch,
        "compressed_branch_cover_checks": compressed_covers,
        "total_core_rank_incidences": total_core_rank,
        "total_viable_child_incidences": total_viable_children,
    }


def product_additivity_audit() -> dict[str, int]:
    families = [
        (frozenset({("a", 0)}), frozenset({("a", 1)})),
        (frozenset({("b", 0), ("b", 1)}),
         frozenset({("b", 0), ("b", 2)}),
         frozenset({("b", 1), ("b", 2)})),
        (frozenset({("c", 0), ("c", 2)}), frozenset({("c", 1), ("c", 2)})),
    ]
    checks = 0
    for count in (2, 3):
        selected = families[:count]
        product = tuple(frozenset().union(*choice) for choice in itertools.product(*selected))
        for choice in itertools.product(*selected):
            rejected = frozenset().union(*choice)
            need(distinguishing_rank(product, rejected)
                 == sum(distinguishing_rank(selected[i], choice[i]) for i in range(count)),
                 "CMR849 product additivity")
            checks += 1
    return {"distinguishing_product_additivity_checks": checks}


def exchange_graph(host: set[Edge], matching: Matching) -> dict[int, set[int]]:
    target = {row: column for row, column in matching}
    vertices = sorted(target)
    return {
        i: {j for j in vertices if i != j and (i, target[j]) in host}
        for i in vertices
    }


def has_directed_cycle(graph: dict[int, set[int]], removed: set[int] | None = None) -> bool:
    removed = removed or set()
    colour = {vertex: 0 for vertex in graph if vertex not in removed}

    def visit(vertex: int) -> bool:
        colour[vertex] = 1
        for other in graph[vertex]:
            if other in removed:
                continue
            if colour[other] == 1 or (colour[other] == 0 and visit(other)):
                return True
        colour[vertex] = 2
        return False

    return any(colour[vertex] == 0 and visit(vertex) for vertex in list(colour))


def feedback_vertex_number(graph: dict[int, set[int]]) -> int:
    vertices = sorted(graph)
    for size in range(len(vertices) + 1):
        for subset in itertools.combinations(vertices, size):
            if not has_directed_cycle(graph, set(subset)):
                return size
    raise AssertionError("removing all vertices is acyclic")


def has_directed_cycle_through(graph: dict[int, set[int]], start: int) -> bool:
    def reach(vertex: int, visited: set[int]) -> bool:
        for other in graph[vertex]:
            if other == start:
                return True
            if other not in visited and reach(other, visited | {other}):
                return True
        return False
    return reach(start, {start})


def exchange_digraph_audit() -> dict[str, int]:
    n = 3
    universe = [(row, column) for row in range(n) for column in range(n)]
    hosts = matching_nodes = fvs_checks = essential_cycle_checks = 0
    alternative_cycle_checks = 0
    for mask in range(1 << len(universe)):
        host = {universe[i] for i in range(len(universe)) if mask >> i & 1}
        family = perfect_matchings(host, range(n), range(n))
        if not family:
            continue
        hosts += 1
        core = matching_essential_core(family)
        family_sets = tuple(frozenset(matching) for matching in family)
        for rejected in family:
            matching_nodes += 1
            graph = exchange_graph(host, rejected)
            need(distinguishing_rank(family_sets, frozenset(rejected))
                 == feedback_vertex_number(graph), "CMR851 FVS equality")
            fvs_checks += 1
            inverse = {column: row for row, column in rejected}
            for alternative in family:
                if alternative == rejected:
                    continue
                moved = {row for row, column in rejected if (row, column) not in alternative}
                need(moved, "alternative matching has no moved vertices")
                sigma = {row: inverse[column] for row, column in alternative}
                need(all(sigma[row] in graph[row] for row in moved),
                     "CMR850 missing exchange arc")
                alternative_cycle_checks += 1
            for edge in rejected:
                row = edge[0]
                need((edge not in core) == has_directed_cycle_through(graph, row),
                     "CMR852 essential-cycle equivalence")
                essential_cycle_checks += 1
    return {
        "side_three_matchable_hosts": hosts,
        "matching_exchange_nodes": matching_nodes,
        "exchange_fvs_equality_checks": fvs_checks,
        "alternative_exchange_cycle_checks": alternative_cycle_checks,
        "essential_cycle_coverage_checks": essential_cycle_checks,
    }


CONTRACT = {
    "schema": "prime-power-complete-branch-distinguishing-rank/v1",
    "source_theorems": [f"CMR{i}" for i in range(830, 854)],
    "fixture_scales": {
        "joint_state_side": 3,
        "joint_state_count": 12,
        "matching_host_side": 3,
    },
    "required_flags": [
        "complete_state_exclusion_branching_exact",
        "viable_branch_essential_core_exact",
        "distinguishing_rank_exchange_digraph_exact",
        "complete_branch_distinguishing_rank_proved",
    ],
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_DIGEST = "d59d5eb82d388c12ba4551c377054d8bdce91b7d10098ebc32c78c56025727cc"


def validate_contract(contract: dict[str, Any]) -> None:
    need(contract.get("schema") == "prime-power-complete-branch-distinguishing-rank/v1",
         "schema")
    need(contract.get("source_theorems") == [f"CMR{i}" for i in range(830, 854)],
         "CMR830--853 ancestry")
    need(contract.get("fixture_scales") == {
        "joint_state_side": 3, "joint_state_count": 12, "matching_host_side": 3
    }, "scales")
    flags = contract.get("required_flags")
    need(isinstance(flags, list) and len(flags) == 4 and len(set(flags)) == 4, "flags")
    honesty = contract.get("honesty_flags")
    need(isinstance(honesty, dict) and honesty and all(value == 0 for value in honesty.values()),
         "honesty")


def mutation_audit() -> int:
    mutations = [
        lambda contract: contract.update(schema="anonymous"),
        lambda contract: contract["source_theorems"].pop(),
        lambda contract: contract["source_theorems"].append("CMR853"),
        lambda contract: contract["fixture_scales"].update(joint_state_side=2),
        lambda contract: contract["required_flags"].pop(),
        lambda contract: contract["required_flags"].append(contract["required_flags"][0]),
        lambda contract: contract["honesty_flags"].update(global_termination_proved=1),
        lambda contract: contract.pop("fixture_scales"),
        lambda contract: contract.pop("honesty_flags"),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(CONTRACT)
        mutate(bad)
        try:
            validate_contract(bad)
        except (BranchRankError, AttributeError, KeyError, TypeError):
            rejected += 1
    need(rejected == len(mutations), "contract corruption accepted")
    return rejected


def main() -> None:
    validate_contract(copy.deepcopy(CONTRACT))
    contract_digest = digest(CONTRACT)
    need(contract_digest == EXPECTED_CONTRACT_DIGEST, "contract digest")
    report = {
        "contract_digest": contract_digest,
        "complete_branch": complete_branch_audit(),
        "product_additivity": product_additivity_audit(),
        "exchange_digraph": exchange_digraph_audit(),
        "rejected_corruptions": mutation_audit(),
        "complete_state_exclusion_branching_exact": 1,
        "viable_branch_essential_core_exact": 1,
        "distinguishing_rank_exchange_digraph_exact": 1,
        "complete_branch_distinguishing_rank_proved": 1,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_restoration_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
