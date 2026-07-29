#!/usr/bin/env python3
"""Verify the canonical duplicate-free parent-rule partition for a labelled prescription.

The earlier exact prescription split covers a state family by one deletion child
per prescribed edge plus one conditioned child, but deletion children may overlap.
Ordering the prescription and assigning each state to its first missing prescribed
edge gives a disjoint complete partition.  For a labelled triple this yields at
most three deletion branches and one forced-triple contraction branch.

This is a genuine finite set-family theorem and a conditional T02 parent-rule
clause.  It does not supply the actual global parent rule or prove recurrence
exhaustiveness, and permanently reports all_n_proved_by_checker=0.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations
from typing import Any, Iterable

Edge = int
State = tuple[Edge, ...]

EXPECTED_CONTRACT_SHA256 = "dca487a954f03f5aaebf09394ab427ef5b338f0e107adf6581146d84863ce39c"


class CanonicalPrescriptionPartitionError(ValueError):
    """Raised when the canonical prescription partition is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CanonicalPrescriptionPartitionError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def canonical_digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def exact_state(raw: Iterable[int], path: str) -> State:
    require(not isinstance(raw, (str, bytes)), f"{path}: state iterable required")
    values = tuple(raw)
    require(values, f"{path}: nonempty state required")
    require(all(isinstance(value, int) and not isinstance(value, bool) for value in values),
            f"{path}: integer edge labels required")
    require(len(values) == len(set(values)), f"{path}: duplicate edge")
    require(values == tuple(sorted(values)), f"{path}: canonical sorted state required")
    return values


def exact_inputs(
    family_raw: Iterable[Iterable[int]],
    prescription_raw: Iterable[int],
    rejected_raw: Iterable[int],
) -> tuple[tuple[State, ...], tuple[Edge, ...], State]:
    family = tuple(exact_state(state, f"family[{index}]") for index, state in enumerate(family_raw))
    require(family, "family: nonempty")
    require(family == tuple(sorted(family)), "family: canonical state order required")
    require(len(family) == len(set(family)), "family: duplicate state")
    cardinalities = {len(state) for state in family}
    require(len(cardinalities) == 1, "family: equal-cardinality states required")

    prescription = tuple(prescription_raw)
    require(prescription, "prescription: nonempty")
    require(all(isinstance(edge, int) and not isinstance(edge, bool) for edge in prescription),
            "prescription: integer edge labels required")
    require(len(prescription) == len(set(prescription)), "prescription: duplicate edge")

    rejected = exact_state(rejected_raw, "rejected")
    require(rejected in family, "rejected: must belong to family")
    require(set(prescription) <= set(rejected), "prescription: must be contained in rejected state")
    return family, prescription, rejected


def first_missing_index(state: State, prescription: tuple[Edge, ...]) -> int:
    state_set = set(state)
    for index, edge in enumerate(prescription):
        if edge not in state_set:
            return index
    return len(prescription)


def branch_core(
    family: tuple[State, ...],
    prescription: tuple[Edge, ...],
    index: int,
) -> dict[str, Any]:
    require(0 <= index <= len(prescription), "branch index outside canonical range")
    members = tuple(state for state in family if first_missing_index(state, prescription) == index)
    if index < len(prescription):
        operation_kind = "prescription-first-missing-deletion"
        omitted_edge: int | None = prescription[index]
        required_prefix = list(prescription[:index])
        residual_states = [list(state) for state in members]
        cardinality_drop = 0
    else:
        operation_kind = "prescription-conditioned-contraction"
        omitted_edge = None
        required_prefix = list(prescription)
        prescription_set = set(prescription)
        residual_states = [
            [edge for edge in state if edge not in prescription_set]
            for state in members
        ]
        cardinality_drop = len(prescription)

    branch = {
        "branch_index": index,
        "branch_id": (
            f"first-missing::{index}::{prescription[index]}"
            if index < len(prescription)
            else "conditioned::all-prescribed"
        ),
        "operation_kind": operation_kind,
        "required_prescription_prefix": required_prefix,
        "omitted_prescription_edge": omitted_edge,
        "nonempty": int(bool(members)),
        "member_states": [list(state) for state in members],
        "residual_states": residual_states,
        "cardinality_drop": cardinality_drop,
    }
    branch["branch_sha256"] = canonical_digest(branch)
    return branch


def exact_partition_manifest(
    family_raw: Iterable[Iterable[int]],
    prescription_raw: Iterable[int],
    rejected_raw: Iterable[int],
) -> dict[str, Any]:
    family, prescription, rejected = exact_inputs(family_raw, prescription_raw, rejected_raw)
    branches = [
        branch_core(family, prescription, index)
        for index in range(len(prescription) + 1)
    ]

    member_occurrences: dict[State, int] = {state: 0 for state in family}
    for branch in branches:
        for state_raw in branch["member_states"]:
            state = tuple(state_raw)
            require(state in member_occurrences, "branch contains state outside family")
            member_occurrences[state] += 1
    require(set(member_occurrences.values()) == {1}, "branches must form an exact disjoint partition")

    rejected_branches = [
        branch["branch_index"]
        for branch in branches
        if list(rejected) in branch["member_states"]
    ]
    require(rejected_branches == [len(prescription)],
            "rejected state must occur only in conditioned branch")

    state_size = len(family[0])
    conditioned = branches[-1]
    require(
        all(len(residual) == state_size - len(prescription)
            for residual in conditioned["residual_states"]),
        "conditioned residual cardinality mismatch",
    )
    require(
        len(conditioned["residual_states"])
        == len({tuple(residual) for residual in conditioned["residual_states"]}),
        "conditioned contraction must be injective",
    )

    nonempty_branches = [branch for branch in branches if branch["nonempty"]]
    operation_slots = []
    for branch in nonempty_branches:
        slot = {
            "clause_id": "canonical-first-missing-prescription-v1",
            "branch_index": branch["branch_index"],
            "branch_id": branch["branch_id"],
            "operation_kind": branch["operation_kind"],
            "required_prescription_prefix": branch["required_prescription_prefix"],
            "omitted_prescription_edge": branch["omitted_prescription_edge"],
        }
        slot["operation_slot_key_sha256"] = canonical_digest(slot)
        operation_slots.append(slot)

    claims = {
        "family_states": len(family),
        "state_cardinality": state_size,
        "prescription_size": len(prescription),
        "canonical_branches": len(branches),
        "nonempty_branches": len(nonempty_branches),
        "deletion_branches": sum(
            branch["nonempty"] and branch["operation_kind"] == "prescription-first-missing-deletion"
            for branch in branches
        ),
        "conditioned_branches": int(conditioned["nonempty"]),
        "exact_union": 1,
        "pairwise_disjoint": 1,
        "each_state_occurs_once": 1,
        "rejected_state_only_in_conditioned_branch": 1,
        "conditioned_cardinality_drop": len(prescription),
        "conditional_parent_rule_clause_ready": 1,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    output: dict[str, Any] = {
        "version": 1,
        "clause_id": "canonical-first-missing-prescription-v1",
        "family": [list(state) for state in family],
        "prescription": list(prescription),
        "rejected_state": list(rejected),
        "branches": branches,
        "operation_slots": operation_slots,
        "claims": claims,
    }
    output["manifest_sha256"] = canonical_digest(output)
    return output


def validate_partition_manifest(
    manifest: Any,
    family_raw: Iterable[Iterable[int]],
    prescription_raw: Iterable[int],
    rejected_raw: Iterable[int],
) -> dict[str, int]:
    require(isinstance(manifest, dict), "manifest: object required")
    expected = exact_partition_manifest(family_raw, prescription_raw, rejected_raw)
    require(manifest == expected, "manifest: canonical prescription partition mismatch")
    return copy.deepcopy(expected["claims"])


def contract_manifest() -> dict[str, Any]:
    output: dict[str, Any] = {
        "version": 1,
        "clause_id": "canonical-first-missing-prescription-v1",
        "source_theorems": ["CMR862", "CMR863", "CMR864", "CMR866", "CMR867", "CMR868", "CMR869"],
        "prescription_semantics": "ordered labelled new triple",
        "branch_schema": [
            {
                "branch_index": 0,
                "predicate": "omit f0",
                "operation_kind": "prescription-first-missing-deletion",
            },
            {
                "branch_index": 1,
                "predicate": "contain f0 and omit f1",
                "operation_kind": "prescription-first-missing-deletion",
            },
            {
                "branch_index": 2,
                "predicate": "contain f0,f1 and omit f2",
                "operation_kind": "prescription-first-missing-deletion",
            },
            {
                "branch_index": 3,
                "predicate": "contain f0,f1,f2",
                "operation_kind": "prescription-conditioned-contraction",
            },
        ],
        "claims": {
            "prescription_size": 3,
            "maximum_nonempty_branches": 4,
            "exact_union": 1,
            "pairwise_disjoint": 1,
            "duplicate_free_child_assignment": 1,
            "rejected_candidate_only_in_conditioned_branch": 1,
            "conditioned_cardinality_drop": 3,
            "conditional_parent_rule_clause_ready": 1,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    output["contract_sha256"] = canonical_digest(output)
    return output


def validate_contract() -> dict[str, int]:
    contract = contract_manifest()
    if EXPECTED_CONTRACT_SHA256 != "TO_BE_FILLED":
        require(contract["contract_sha256"] == EXPECTED_CONTRACT_SHA256,
                "built-in contract digest drift")
    return copy.deepcopy(contract["claims"])


def exhaustive_triple_regression() -> dict[str, int]:
    universe = tuple(range(5))
    prescription = (0, 1, 2)
    rejected = (0, 1, 2)
    all_states = tuple(combinations(universe, 3))
    alternatives = tuple(state for state in all_states if state != rejected)

    families = 0
    state_occurrences = 0
    branch_occurrences = 0
    fully_populated_branch_families = 0
    for mask in range(1 << len(alternatives)):
        family = tuple(sorted(
            (rejected,)
            + tuple(state for index, state in enumerate(alternatives) if mask & (1 << index))
        ))
        manifest = exact_partition_manifest(family, prescription, rejected)
        claims = validate_partition_manifest(manifest, family, prescription, rejected)
        require(claims["canonical_branches"] == 4, "triple branch census drift")
        require(claims["conditioned_cardinality_drop"] == 3, "triple contraction drift")
        families += 1
        state_occurrences += len(family)
        branch_occurrences += claims["nonempty_branches"]
        fully_populated_branch_families += int(claims["nonempty_branches"] == 4)

    require(families == 512, "exhaustive family census drift")
    require(state_occurrences == 2816, "exhaustive state-occurrence census drift")
    return {
        "exhaustive_families": families,
        "exhaustive_state_occurrences": state_occurrences,
        "nonempty_branch_occurrences": branch_occurrences,
        "four_nonempty_branch_families": fully_populated_branch_families,
    }


def mutation_tests() -> int:
    family = tuple(combinations(range(5), 3))
    prescription = (0, 1, 2)
    rejected = (0, 1, 2)
    manifest = exact_partition_manifest(family, prescription, rejected)
    mutations: list[tuple[str, Any]] = []

    def input_mutation(name: str, family_value: Any, prescription_value: Any, rejected_value: Any) -> None:
        mutations.append((name, ("input", family_value, prescription_value, rejected_value)))

    input_mutation("duplicate-prescription-edge", family, (0, 1, 1), rejected)
    input_mutation("rejected-missing", family[1:], prescription, rejected)
    input_mutation("prescription-not-contained", family, (0, 1, 4), rejected)
    input_mutation("unequal-state-cardinality", tuple(sorted(family + ((0, 1),))), prescription, rejected)

    for name, mutator in (
        ("missing-branch-member", lambda data: data["branches"][0]["member_states"].pop()),
        ("duplicate-branch-member", lambda data: data["branches"][1]["member_states"].append(
            copy.deepcopy(data["branches"][0]["member_states"][0])
        )),
        ("operation-kind-corruption", lambda data: data["branches"][0].update(
            operation_kind="prescription-conditioned-contraction"
        )),
        ("prefix-corruption", lambda data: data["branches"][2].update(
            required_prescription_prefix=[]
        )),
        ("residual-corruption", lambda data: data["branches"][-1]["residual_states"].append([99])),
        ("honesty-corruption", lambda data: data["claims"].update(all_n_proved_by_checker=1)),
        ("seal-corruption", lambda data: data.update(manifest_sha256="0" * 64)),
    ):
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append((name, ("manifest", candidate)))

    rejected_count = 0
    for name, mutation in mutations:
        try:
            if mutation[0] == "input":
                _, f, p, q = mutation
                exact_partition_manifest(f, p, q)
            else:
                validate_partition_manifest(mutation[1], family, prescription, rejected)
        except CanonicalPrescriptionPartitionError:
            rejected_count += 1
        else:
            raise CanonicalPrescriptionPartitionError(f"mutation accepted: {name}")

    require(rejected_count == len(mutations), "mutation rejection census drift")
    return rejected_count


def self_test() -> dict[str, Any]:
    contract_claims = validate_contract()
    exhaustive = exhaustive_triple_regression()
    rejected = mutation_tests()
    return {
        **contract_claims,
        **exhaustive,
        "rejected_mutations": rejected,
        "contract_sha256": contract_manifest()["contract_sha256"],
    }


def main() -> None:
    result = self_test()
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
