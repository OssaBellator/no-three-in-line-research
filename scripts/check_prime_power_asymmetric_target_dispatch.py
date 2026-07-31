#!/usr/bin/env python3
"""Verify the complete local target response on asymmetric contexts.

The checker starts from a canonical asymmetric context, generates its feasible
family, exact triple universe and least anchor, then applies the same exact
target-response trichotomy used on square hosts. Target-preserving families
contract through the asymmetric forced-set theorem; strict improvements are
retained; nonimproving target destruction chooses the least new triple and
generates a disjoint first-missing asymmetric context partition.

This is a complete local response relative to a supplied asymmetric context. It
does not generate the global owner/routing/factor/envelope context sequence,
prove termination, or establish the all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any, Iterable

from check_prime_power_required_prefix_parent_generation import (
    Edge,
    State,
    Triple,
    exact_edge,
    exact_prescription,
    exact_required,
    generate_exact_triple_universe,
)
from check_prime_power_asymmetric_context_generation import (
    all_coordinate_subsets,
    contract_forced_set,
    exact_asymmetric_context,
    exact_asymmetric_manifest,
    generate_asymmetric_family,
    state_triples,
)

EXPECTED_CONTRACT_SHA256 = "5e982b03f24ce4cd1230ede70563b49e3ac67976b0a84e038ae27b463e39fa83"


class AsymmetricTargetDispatchError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AsymmetricTargetDispatchError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_asymmetric_state(
    n: int,
    domains: tuple[tuple[tuple[int, ...], tuple[int, ...]], ...],
    raw: Iterable[Iterable[int]],
    path: str,
) -> State:
    state = tuple(
        exact_edge(edge, n, f"{path}[{index}]")
        for index, edge in enumerate(raw)
    )
    require(state == tuple(sorted(state)), f"{path}: canonical order required")
    require(len(state) == len(set(state)), f"{path}: duplicate edge")
    expected_size = sum(len(domains[layer][0]) for layer in (0, 1))
    require(len(state) == expected_size,
            f"{path}: exact asymmetric state cardinality required")
    for edge in state:
        layer, row, column = edge
        rows, columns = domains[layer]
        require(row in rows and column in columns,
                f"{path}: edge outside layer domain")
    return state


def first_missing_index(state: State, prescription: Triple) -> int:
    state_set = set(state)
    return next(
        (index for index, edge in enumerate(prescription)
         if edge not in state_set),
        3,
    )


def exact_first_missing_asymmetric_manifest(
    n: int,
    row_domains_raw: Iterable[Iterable[int]],
    column_domains_raw: Iterable[Iterable[int]],
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
    prescription_raw: Iterable[Iterable[int]],
    rejected_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    domains, deleted, required = exact_asymmetric_context(
        n, row_domains_raw, column_domains_raw, deleted_raw, required_raw
    )
    rows = tuple(domain[0] for domain in domains)
    columns = tuple(domain[1] for domain in domains)
    prescription = exact_prescription(n, prescription_raw)
    rejected = exact_asymmetric_state(n, domains, rejected_raw, "rejected")
    family = generate_asymmetric_family(
        n, rows, columns, deleted, required
    )
    require(rejected in family, "rejected state absent from asymmetric family")
    require(set(prescription) <= set(rejected),
            "prescription absent from rejected state")

    parent_universe = set(generate_exact_triple_universe(family))
    occurrences = {state: 0 for state in family}
    branches: list[dict[str, Any]] = []
    for index in range(4):
        prefix_required = tuple(sorted(
            set(required) | set(prescription[:index])
        ))
        exact_required(n, prefix_required)
        contradiction = False
        if index < 3:
            omitted = prescription[index]
            child_deleted = tuple(sorted(set(deleted) | {omitted}))
            child_required = prefix_required
            contradiction = omitted in set(required)
        else:
            omitted = None
            child_deleted = deleted
            child_required = tuple(sorted(
                set(required) | set(prescription)
            ))

        direct = tuple(
            state for state in family
            if first_missing_index(state, prescription) == index
        )
        if contradiction:
            members: tuple[State, ...] = ()
            require(not direct,
                    "required/deleted asymmetric branch is not empty")
        else:
            members = generate_asymmetric_family(
                n, rows, columns, child_deleted, child_required
            )
            require(members == direct,
                    f"branch {index}: generated asymmetric context mismatch")
        for state in members:
            occurrences[state] += 1

        child_universe = generate_exact_triple_universe(members)
        require(set(child_universe) <= parent_universe,
                f"branch {index}: triple universe is not monotone")

        contraction = None
        if index == 3:
            require(members, "conditioned asymmetric branch unexpectedly empty")
            contraction = contract_forced_set(
                n, rows, columns, child_deleted, child_required, prescription
            )
        branch: dict[str, Any] = {
            "branch_index": index,
            "deleted_edges": [list(edge) for edge in child_deleted],
            "required_edges": [list(edge) for edge in child_required],
            "omitted_edge": None if omitted is None else list(omitted),
            "context_status": (
                "required-deleted-contradiction-terminal"
                if contradiction else "generated-asymmetric-context"
            ),
            "members": [
                [list(edge) for edge in state] for state in members
            ],
            "exact_triple_universe": [
                [list(edge) for edge in triple] for triple in child_universe
            ],
            "conditioned_contraction": contraction,
            "context_restriction_exact": 1,
            "triple_universe_monotone": 1,
        }
        branch["branch_sha256"] = digest(branch)
        branches.append(branch)

    require(set(occurrences.values()) == {1},
            "asymmetric first-missing branches are not a partition")
    require(
        [branch["branch_index"] for branch in branches
         if [list(edge) for edge in rejected] in branch["members"]]
        == [3],
        "rejected state not isolated in asymmetric conditioned branch",
    )
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-asymmetric-first-missing-response-v1",
        "ambient_side": n,
        "row_domains": [list(rows[layer]) for layer in (0, 1)],
        "column_domains": [
            list(columns[layer]) for layer in (0, 1)
        ],
        "parent_deleted_edges": [list(edge) for edge in deleted],
        "parent_required_edges": [list(edge) for edge in required],
        "prescription": [list(edge) for edge in prescription],
        "rejected": [list(edge) for edge in rejected],
        "branches": branches,
        "claims": {
            "parent_feasible_states": len(family),
            "first_missing_branch_count": 4,
            "asymmetric_first_missing_contexts_generated": 1,
            "asymmetric_first_missing_partition_exact": 1,
            "asymmetric_first_missing_partition_pairwise_disjoint": 1,
            "asymmetric_conditioned_contraction_exact": 1,
            "child_triple_universes_monotone": 1,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def candidate_record(
    n: int,
    rows: tuple[tuple[int, ...], tuple[int, ...]],
    columns: tuple[tuple[int, ...], tuple[int, ...]],
    deleted: tuple[Edge, ...],
    required: tuple[Edge, ...],
    family: tuple[State, ...],
    universe: tuple[Triple, ...],
    anchor: State,
    candidate: State,
    target: Triple,
) -> dict[str, Any]:
    anchor_triples = state_triples(anchor, universe)
    candidate_triples = state_triples(candidate, universe)
    target_preserved = int(set(target) <= set(candidate))
    potential_delta = len(candidate_triples) - len(anchor_triples)
    new_triples = tuple(sorted(
        set(candidate_triples) - set(anchor_triples)
    ))

    if target_preserved:
        category = "asymmetric-target-preserving-contraction"
        canonical_new_triple = None
        response = None
    elif potential_delta < 0:
        category = "asymmetric-target-destroying-strict-improvement"
        canonical_new_triple = None
        response = None
    else:
        require(new_triples,
                "nonimproving asymmetric target destruction has no new triple")
        category = "asymmetric-target-destroying-new-triple"
        canonical_new_triple = new_triples[0]
        response = exact_first_missing_asymmetric_manifest(
            n, rows, columns, deleted, required,
            canonical_new_triple, candidate
        )

    result: dict[str, Any] = {
        "candidate": [list(edge) for edge in candidate],
        "anchor_potential": len(anchor_triples),
        "candidate_potential": len(candidate_triples),
        "potential_delta": potential_delta,
        "canonical_target_preserved": target_preserved,
        "new_triples": [
            [list(edge) for edge in triple] for triple in new_triples
        ],
        "trigger_category": category,
        "canonical_new_triple": (
            None if canonical_new_triple is None
            else [list(edge) for edge in canonical_new_triple]
        ),
        "new_triple_response": response,
    }
    result["candidate_record_sha256"] = digest(result)
    return result


def exact_asymmetric_dispatch_manifest(
    n: int,
    row_domains_raw: Iterable[Iterable[int]],
    column_domains_raw: Iterable[Iterable[int]],
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    domains, deleted, required = exact_asymmetric_context(
        n, row_domains_raw, column_domains_raw, deleted_raw, required_raw
    )
    rows = tuple(domain[0] for domain in domains)
    columns = tuple(domain[1] for domain in domains)
    context = exact_asymmetric_manifest(
        n, rows, columns, deleted, required
    )
    family = generate_asymmetric_family(
        n, rows, columns, deleted, required
    )
    universe = generate_exact_triple_universe(family)

    target_contraction = None
    records: list[dict[str, Any]] = []
    category_counts = {
        "asymmetric-target-preserving-contraction": 0,
        "asymmetric-target-destroying-strict-improvement": 0,
        "asymmetric-target-destroying-new-triple": 0,
    }
    if family:
        anchor = family[0]
        anchor_triples = state_triples(anchor, universe)
    else:
        anchor = None
        anchor_triples = ()

    if anchor_triples:
        target = anchor_triples[0]
        target_required = tuple(sorted(set(required) | set(target)))
        exact_required(n, target_required)
        target_members = generate_asymmetric_family(
            n, rows, columns, deleted, target_required
        )
        require(
            target_members == tuple(
                state for state in family if set(target) <= set(state)
            ),
            "asymmetric target-preserving family generation failed",
        )
        target_contraction = contract_forced_set(
            n, rows, columns, deleted, target_required, target
        )
        records = [
            candidate_record(
                n, rows, columns, deleted, required,
                family, universe, anchor, candidate, target
            )
            for candidate in family if candidate != anchor
        ]
        for record in records:
            category_counts[record["trigger_category"]] += 1
        require(sum(category_counts.values()) == len(family) - 1,
                "asymmetric candidate classification incomplete")
    else:
        target = None

    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-asymmetric-target-dispatch-v1",
        "context": context,
        "canonical_target": (
            None if target is None else [list(edge) for edge in target]
        ),
        "target_preserving_contraction": target_contraction,
        "candidate_records": records,
        "claims": {
            "feasible_states": len(family),
            "alternative_candidates": max(0, len(family) - 1),
            "dirty_anchor_dispatch": int(bool(anchor_triples)),
            "asymmetric_target_preserving_candidates": category_counts[
                "asymmetric-target-preserving-contraction"
            ],
            "asymmetric_strict_improvement_candidates": category_counts[
                "asymmetric-target-destroying-strict-improvement"
            ],
            "asymmetric_nonimproving_new_triple_candidates": category_counts[
                "asymmetric-target-destroying-new-triple"
            ],
            "asymmetric_target_preserving_contraction_exact": 1,
            "asymmetric_strict_improvement_action_exact": 1,
            "asymmetric_nonimproving_new_triple_response_exact": 1,
            "asymmetric_first_missing_contexts_generated": 1,
            "local_asymmetric_candidate_response_complete": 1,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def validate_dispatch_manifest(
    manifest: Any,
    n: int,
    row_domains_raw: Iterable[Iterable[int]],
    column_domains_raw: Iterable[Iterable[int]],
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
) -> dict[str, int]:
    expected = exact_asymmetric_dispatch_manifest(
        n, row_domains_raw, column_domains_raw, deleted_raw, required_raw
    )
    require(isinstance(manifest, dict) and manifest == expected,
            "asymmetric target dispatch manifest mismatch")
    return copy.deepcopy(expected["claims"])


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-asymmetric-target-dispatch-v1",
        "source_theorems": [
            "CMR698", "CMR866", "CMR2794", "CMR2818",
            "CMR2864", "CMR2865", "CMR2866", "CMR2867",
            "CMR2868", "CMR2869", "CMR2870", "CMR2872",
            "CMR2875",
        ],
        "claims": {
            "asymmetric_target_preserving_contraction_exact": 1,
            "asymmetric_strict_improvement_action_exact": 1,
            "asymmetric_nonimproving_new_triple_response_exact": 1,
            "asymmetric_first_missing_contexts_generated": 1,
            "asymmetric_first_missing_partition_exact": 1,
            "asymmetric_conditioned_contraction_exact": 1,
            "local_asymmetric_candidate_response_complete": 1,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["contract_sha256"] = digest(result)
    return result


def validate_contract() -> dict[str, int]:
    contract = contract_manifest()
    require(
        contract["contract_sha256"] == EXPECTED_CONTRACT_SHA256,
        "built-in contract digest drift",
    )
    return copy.deepcopy(contract["claims"])


def exhaustive_side_three_regression() -> dict[str, int]:
    n = 3
    subsets = all_coordinate_subsets(n)
    hosts = dirty = candidate_records = 0
    preserving = improving = nonimproving = 0
    first_missing_scenarios = branch_records = nonempty_branches = 0

    for rows0 in subsets:
        for columns0 in subsets:
            if len(rows0) != len(columns0):
                continue
            for rows1 in subsets:
                for columns1 in subsets:
                    if len(rows1) != len(columns1):
                        continue
                    rows = (rows0, rows1)
                    columns = (columns0, columns1)
                    manifest = exact_asymmetric_dispatch_manifest(
                        n, rows, columns, (), ()
                    )
                    hosts += 1
                    claims = manifest["claims"]
                    dirty += claims["dirty_anchor_dispatch"]
                    candidate_records += len(manifest["candidate_records"])
                    preserving += claims[
                        "asymmetric_target_preserving_candidates"
                    ]
                    improving += claims[
                        "asymmetric_strict_improvement_candidates"
                    ]
                    nonimproving += claims[
                        "asymmetric_nonimproving_new_triple_candidates"
                    ]
                    for record in manifest["candidate_records"]:
                        response = record["new_triple_response"]
                        if response is None:
                            continue
                        first_missing_scenarios += 1
                        branch_records += len(response["branches"])
                        nonempty_branches += sum(
                            int(bool(branch["members"]))
                            for branch in response["branches"]
                        )

    require(
        (
            hosts, dirty, candidate_records, preserving,
            improving, nonimproving, first_missing_scenarios,
            branch_records, nonempty_branches,
        )
        == (400, 44, 148, 1, 108, 39, 39, 156, 111),
        "side-three asymmetric target census drift",
    )
    return {
        "side_three_asymmetric_hosts": hosts,
        "side_three_dirty_dispatches": dirty,
        "side_three_candidate_records": candidate_records,
        "side_three_preserving_candidates": preserving,
        "side_three_improving_candidates": improving,
        "side_three_nonimproving_candidates": nonimproving,
        "side_three_first_missing_scenarios": first_missing_scenarios,
        "side_three_branch_records": branch_records,
        "side_three_nonempty_branches": nonempty_branches,
    }


def side_four_regression() -> dict[str, int]:
    n = 4
    rows = (tuple(range(n)), tuple(range(n)))
    columns = rows
    manifest = exact_asymmetric_dispatch_manifest(
        n, rows, columns, (), ()
    )
    claims = manifest["claims"]
    first_missing = [
        record["new_triple_response"]
        for record in manifest["candidate_records"]
        if record["new_triple_response"] is not None
    ]
    result = {
        "side_four_feasible_states": claims["feasible_states"],
        "side_four_candidate_records": len(manifest["candidate_records"]),
        "side_four_preserving_candidates": claims[
            "asymmetric_target_preserving_candidates"
        ],
        "side_four_improving_candidates": claims[
            "asymmetric_strict_improvement_candidates"
        ],
        "side_four_nonimproving_candidates": claims[
            "asymmetric_nonimproving_new_triple_candidates"
        ],
        "side_four_first_missing_scenarios": len(first_missing),
        "side_four_branch_records": sum(
            len(response["branches"]) for response in first_missing
        ),
        "side_four_nonempty_branches": sum(
            int(bool(branch["members"]))
            for response in first_missing
            for branch in response["branches"]
        ),
    }
    require(
        result == {
            "side_four_feasible_states": 216,
            "side_four_candidate_records": 215,
            "side_four_preserving_candidates": 8,
            "side_four_improving_candidates": 172,
            "side_four_nonimproving_candidates": 35,
            "side_four_first_missing_scenarios": 35,
            "side_four_branch_records": 140,
            "side_four_nonempty_branches": 140,
        },
        "side-four asymmetric target census drift",
    )
    return result


def mutation_tests() -> int:
    n = 4
    rows = (tuple(range(n)), tuple(range(n)))
    columns = rows
    manifest = exact_asymmetric_dispatch_manifest(
        n, rows, columns, (), ()
    )
    rejected = 0

    malformed = [
        lambda: exact_asymmetric_dispatch_manifest(
            n, ((1, 0, 2, 3), rows[1]), columns, (), ()
        ),
        lambda: exact_asymmetric_dispatch_manifest(
            n, rows, ((0, 1, 2), columns[1]), (), ()
        ),
        lambda: exact_first_missing_asymmetric_manifest(
            n, rows, columns, (), (),
            manifest["canonical_target"],
            next(
                record["candidate"]
                for record in manifest["candidate_records"]
                if not record["canonical_target_preserved"]
            ),
        ),
        lambda: exact_first_missing_asymmetric_manifest(
            n, rows, columns, (), (),
            tuple(reversed(manifest["canonical_target"])),
            manifest["candidate_records"][0]["candidate"],
        ),
    ]
    for call in malformed:
        try:
            call()
        except (ValueError, TypeError):
            rejected += 1
        else:
            raise AsymmetricTargetDispatchError("malformed dispatch input accepted")

    def corrupt(mutator: Any) -> None:
        nonlocal rejected
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        try:
            validate_dispatch_manifest(
                candidate, n, rows, columns, (), ()
            )
        except AsymmetricTargetDispatchError:
            rejected += 1
        else:
            raise AsymmetricTargetDispatchError(
                "corrupted asymmetric dispatch accepted"
            )

    corrupt(lambda data: data["candidate_records"].pop())
    corrupt(lambda data: data["target_preserving_contraction"].update(
        child_family=[]
    ))
    corrupt(lambda data: data["candidate_records"][0].update(
        trigger_category="wrong"
    ))
    corrupt(lambda data: data["claims"].update(
        local_asymmetric_candidate_response_complete=0
    ))
    corrupt(lambda data: data["claims"].update(all_n_proved_by_checker=1))
    corrupt(lambda data: data.update(manifest_sha256="0" * 64))

    require(rejected == 10, "mutation rejection census drift")
    return rejected


def self_test() -> dict[str, Any]:
    return {
        **validate_contract(),
        **exhaustive_side_three_regression(),
        **side_four_regression(),
        "rejected_mutations": mutation_tests(),
        "contract_sha256": contract_manifest()["contract_sha256"],
    }


def main() -> None:
    print(json.dumps(self_test(), sort_keys=True))


if __name__ == "__main__":
    main()
