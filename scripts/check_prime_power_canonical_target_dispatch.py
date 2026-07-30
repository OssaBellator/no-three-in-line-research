#!/usr/bin/env python3
"""Verify canonical target-bank dispatch for every supplied anchor family.

Given an equal-cardinality feasible family, anchor and exact triple universe, the
anchor is either triple-free (clean terminal) or has a canonical least triple.
The singleton bank containing that triple feeds the complete local target
response rule: preserving candidates contract the triple, improving candidates
strictly lower triple potential, and nonimproving destructive candidates receive
a canonical new-triple first-missing partition.

This is a finite conditional T02 theorem. It does not generate the global parent
family, prove the supplied triple universe geometrically exact, prove recurrence
termination, or establish the all-n conjecture. It permanently reports
``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations
from typing import Any, Iterable

State = tuple[int, ...]
Triple = tuple[int, int, int]
EXPECTED_CONTRACT_SHA256 = "634318242ece5cab549b9394ba33e116d7c1b01b4c74d5a02e276004fe1e8444"


class CanonicalTargetDispatchError(ValueError):
    """Raised when the canonical target dispatch is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CanonicalTargetDispatchError(message)


def canonical_digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_set(raw: Iterable[int], path: str, size: int | None = None) -> State:
    require(not isinstance(raw, (str, bytes)), f"{path}: iterable required")
    values = tuple(raw)
    require(values, f"{path}: nonempty set required")
    require(values == tuple(sorted(values)), f"{path}: canonical sorted order required")
    require(len(values) == len(set(values)), f"{path}: duplicate value")
    require(
        all(isinstance(value, int) and not isinstance(value, bool) for value in values),
        f"{path}: integer labels required",
    )
    if size is not None:
        require(len(values) == size, f"{path}: exact size {size} required")
    return values


def exact_inputs(
    family_raw: Iterable[Iterable[int]],
    anchor_raw: Iterable[int],
    triples_raw: Iterable[Iterable[int]],
) -> tuple[tuple[State, ...], State, tuple[Triple, ...]]:
    family = tuple(
        exact_set(state, f"family[{index}]")
        for index, state in enumerate(family_raw)
    )
    require(family, "family: nonempty")
    require(family == tuple(sorted(family)), "family: canonical state order required")
    require(len(family) == len(set(family)), "family: duplicate state")
    require(len({len(state) for state in family}) == 1, "family: equal cardinality required")

    anchor = exact_set(anchor_raw, "anchor")
    require(anchor in family, "anchor: absent from family")

    triples = tuple(
        exact_set(triple, f"triple_universe[{index}]", 3)
        for index, triple in enumerate(triples_raw)
    )
    require(
        triples == tuple(sorted(triples)),
        "triple_universe: canonical order required",
    )
    require(
        len(triples) == len(set(triples)),
        "triple_universe: duplicate triple",
    )
    return family, anchor, triples  # type: ignore[return-value]


def state_triples(state: State, triples: tuple[Triple, ...]) -> tuple[Triple, ...]:
    state_set = set(state)
    return tuple(triple for triple in triples if set(triple) <= state_set)


def first_missing_index(state: State, prescription: Triple) -> int:
    state_set = set(state)
    for index, cell in enumerate(prescription):
        if cell not in state_set:
            return index
    return 3


def exact_prescription_partition(
    family: tuple[State, ...],
    rejected: State,
    prescription: Triple,
) -> dict[str, Any]:
    require(
        set(prescription) <= set(rejected),
        "prescription: absent from rejected candidate",
    )
    occurrences = {state: 0 for state in family}
    prescription_set = set(prescription)
    branches: list[dict[str, Any]] = []
    for index in range(4):
        members = tuple(
            state
            for state in family
            if first_missing_index(state, prescription) == index
        )
        for state in members:
            occurrences[state] += 1
        if index < 3:
            operation_kind = "canonical-target-new-triple-first-missing-deletion"
            residuals = [list(state) for state in members]
            omitted_cell: int | None = prescription[index]
            cardinality_drop = 0
        else:
            operation_kind = "canonical-target-new-triple-conditioned-contraction"
            residuals = [
                [cell for cell in state if cell not in prescription_set]
                for state in members
            ]
            omitted_cell = None
            cardinality_drop = 3
            require(
                len(residuals) == len({tuple(residual) for residual in residuals}),
                "conditioned contraction: residual map not injective",
            )
        branch = {
            "branch_index": index,
            "operation_kind": operation_kind,
            "required_prefix": list(prescription[:index]),
            "omitted_cell": omitted_cell,
            "members": [list(state) for state in members],
            "residuals": residuals,
            "cardinality_drop": cardinality_drop,
        }
        branch["branch_sha256"] = canonical_digest(branch)
        branches.append(branch)

    require(
        set(occurrences.values()) == {1},
        "prescription partition: every state must occur exactly once",
    )
    require(
        [
            branch["branch_index"]
            for branch in branches
            if list(rejected) in branch["members"]
        ]
        == [3],
        "prescription partition: rejected candidate not isolated",
    )
    result = {
        "prescription": list(prescription),
        "branches": branches,
        "exact_union": 1,
        "pairwise_disjoint": 1,
        "conditioned_cardinality_drop": 3,
    }
    result["partition_sha256"] = canonical_digest(result)
    return result


def candidate_record(
    family: tuple[State, ...],
    anchor: State,
    candidate: State,
    triples: tuple[Triple, ...],
    target: Triple,
) -> dict[str, Any]:
    anchor_triples = state_triples(anchor, triples)
    candidate_triples = state_triples(candidate, triples)
    target_preserved = int(set(target) <= set(candidate))
    potential_delta = len(candidate_triples) - len(anchor_triples)
    new_triples = tuple(sorted(set(candidate_triples) - set(anchor_triples)))

    if target_preserved:
        trigger_category = "canonical-target-preserving-contraction"
        canonical_new_triple: Triple | None = None
        partition = None
    elif potential_delta < 0:
        trigger_category = "canonical-target-destroying-strict-improvement"
        canonical_new_triple = None
        partition = None
    else:
        require(
            new_triples,
            "nonimproving target destruction: new triple required",
        )
        trigger_category = "canonical-target-destroying-nonimproving-new-triple"
        canonical_new_triple = new_triples[0]
        partition = exact_prescription_partition(
            family,
            candidate,
            canonical_new_triple,
        )

    record = {
        "candidate": list(candidate),
        "anchor_potential": len(anchor_triples),
        "candidate_potential": len(candidate_triples),
        "potential_delta": potential_delta,
        "canonical_target_preserved": target_preserved,
        "new_triples": [list(triple) for triple in new_triples],
        "trigger_category": trigger_category,
        "canonical_new_triple": (
            None if canonical_new_triple is None else list(canonical_new_triple)
        ),
        "new_triple_partition": partition,
    }
    record["candidate_record_sha256"] = canonical_digest(record)
    return record


def exact_dispatch_manifest(
    family_raw: Iterable[Iterable[int]],
    anchor_raw: Iterable[int],
    triples_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    family, anchor, triples = exact_inputs(family_raw, anchor_raw, triples_raw)
    anchor_triples = state_triples(anchor, triples)
    alternatives = tuple(state for state in family if state != anchor)

    if not anchor_triples:
        dispatch_kind = "clean-anchor-terminal"
        canonical_target = None
        target_branch = None
        candidate_records: list[dict[str, Any]] = []
        category_counts = {
            "canonical-target-preserving-contraction": 0,
            "canonical-target-destroying-strict-improvement": 0,
            "canonical-target-destroying-nonimproving-new-triple": 0,
        }
    else:
        dispatch_kind = "canonical-singleton-target-response"
        canonical_target = anchor_triples[0]
        target_set = set(canonical_target)
        preserving = tuple(
            state for state in family if target_set <= set(state)
        )
        residuals = [
            [cell for cell in state if cell not in target_set]
            for state in preserving
        ]
        require(
            len(residuals) == len({tuple(residual) for residual in residuals}),
            "canonical target contraction: residual map not injective",
        )
        target_branch = {
            "operation_kind": "canonical-singleton-target-contraction",
            "members": [list(state) for state in preserving],
            "residuals": residuals,
            "cardinality_drop": 3,
        }
        target_branch["branch_sha256"] = canonical_digest(target_branch)

        candidate_records = [
            candidate_record(family, anchor, candidate, triples, canonical_target)
            for candidate in alternatives
        ]
        category_counts = {
            "canonical-target-preserving-contraction": 0,
            "canonical-target-destroying-strict-improvement": 0,
            "canonical-target-destroying-nonimproving-new-triple": 0,
        }
        for record in candidate_records:
            category_counts[record["trigger_category"]] += 1
        require(
            sum(category_counts.values()) == len(alternatives),
            "canonical target dispatch: candidate classification incomplete",
        )

    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-anchor-target-dispatch-v1",
        "family": [list(state) for state in family],
        "anchor": list(anchor),
        "triple_universe": [list(triple) for triple in triples],
        "anchor_triples": [list(triple) for triple in anchor_triples],
        "dispatch_kind": dispatch_kind,
        "canonical_target_bank": (
            [] if canonical_target is None else [list(canonical_target)]
        ),
        "target_preserving_branch": target_branch,
        "candidate_records": candidate_records,
        "claims": {
            "family_states": len(family),
            "alternative_candidates": len(alternatives),
            "anchor_triple_count": len(anchor_triples),
            "clean_anchor_terminal": int(not anchor_triples),
            "canonical_singleton_target_selected": int(bool(anchor_triples)),
            "canonical_target_preserving_candidates": category_counts[
                "canonical-target-preserving-contraction"
            ],
            "canonical_target_destroying_strict_improvements": category_counts[
                "canonical-target-destroying-strict-improvement"
            ],
            "canonical_target_destroying_nonimproving_candidates": category_counts[
                "canonical-target-destroying-nonimproving-new-triple"
            ],
            "canonical_target_bank_external_choice_required": 0,
            "local_anchor_dispatch_complete": 1,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = canonical_digest(result)
    return result


def validate_dispatch_manifest(
    manifest: Any,
    family_raw: Iterable[Iterable[int]],
    anchor_raw: Iterable[int],
    triples_raw: Iterable[Iterable[int]],
) -> dict[str, int]:
    require(isinstance(manifest, dict), "manifest: object required")
    expected = exact_dispatch_manifest(family_raw, anchor_raw, triples_raw)
    require(manifest == expected, "manifest: canonical target dispatch mismatch")
    return copy.deepcopy(expected["claims"])


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-anchor-target-dispatch-v1",
        "source_theorems": [
            "CMR698",
            "CMR866",
            "CMR2794",
            "CMR2807",
            "CMR2808",
            "CMR2809",
            "CMR2811",
            "CMR2813",
            "CMR2814",
        ],
        "dispatch_cases": [
            "clean-anchor-terminal",
            "canonical-singleton-target-response",
        ],
        "candidate_actions": [
            "canonical-target-preserving-contraction",
            "canonical-target-destroying-strict-improvement",
            "canonical-target-destroying-nonimproving-new-triple",
        ],
        "claims": {
            "clean_anchor_terminal": 1,
            "dirty_anchor_has_canonical_target": 1,
            "canonical_target_bank_external_choice_required": 0,
            "canonical_target_contraction_drop": 3,
            "local_anchor_dispatch_complete": 1,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["contract_sha256"] = canonical_digest(result)
    return result


def validate_contract() -> dict[str, int]:
    contract = contract_manifest()
    if EXPECTED_CONTRACT_SHA256 != "TO_BE_FILLED":
        require(
            contract["contract_sha256"] == EXPECTED_CONTRACT_SHA256,
            "built-in contract digest drift",
        )
    return copy.deepcopy(contract["claims"])


def exhaustive_hypergraph_regression() -> dict[str, int]:
    states = tuple(combinations(range(5), 4))
    triples = tuple(combinations(range(5), 3))
    scenarios = 0
    clean = 0
    dirty = 0
    candidate_records = 0
    preserving = 0
    improving = 0
    nonimproving = 0
    for mask in range(1 << len(triples)):
        hypergraph = tuple(
            triple
            for index, triple in enumerate(triples)
            if mask & (1 << index)
        )
        for anchor in states:
            claims = exact_dispatch_manifest(states, anchor, hypergraph)["claims"]
            scenarios += 1
            clean += claims["clean_anchor_terminal"]
            dirty += claims["canonical_singleton_target_selected"]
            candidate_records += (
                0
                if claims["clean_anchor_terminal"]
                else claims["alternative_candidates"]
            )
            preserving += claims["canonical_target_preserving_candidates"]
            improving += claims[
                "canonical_target_destroying_strict_improvements"
            ]
            nonimproving += claims[
                "canonical_target_destroying_nonimproving_candidates"
            ]
    require(scenarios == 5120, "hypergraph scenario census drift")
    require(clean + dirty == scenarios, "clean/dirty dispatch census drift")
    require(
        preserving + improving + nonimproving == candidate_records,
        "candidate category census drift",
    )
    return {
        "exhaustive_hypergraph_anchor_scenarios": scenarios,
        "clean_anchor_scenarios": clean,
        "dirty_anchor_scenarios": dirty,
        "classified_dirty_candidate_records": candidate_records,
        "preserving_candidate_records": preserving,
        "improving_candidate_records": improving,
        "nonimproving_candidate_records": nonimproving,
    }


def exhaustive_subfamily_regression() -> dict[str, int]:
    states = tuple(combinations(range(5), 4))
    triples = tuple(combinations(range(5), 3))
    scenarios = 0
    clean = 0
    dirty = 0
    for anchor in states:
        alternatives = tuple(state for state in states if state != anchor)
        for family_mask in range(1 << len(alternatives)):
            family = tuple(
                sorted(
                    (anchor,)
                    + tuple(
                        state
                        for index, state in enumerate(alternatives)
                        if family_mask & (1 << index)
                    )
                )
            )
            for triple_mask in range(1 << len(triples)):
                hypergraph = tuple(
                    triple
                    for index, triple in enumerate(triples)
                    if triple_mask & (1 << index)
                )
                claims = exact_dispatch_manifest(family, anchor, hypergraph)["claims"]
                scenarios += 1
                clean += claims["clean_anchor_terminal"]
                dirty += claims["canonical_singleton_target_selected"]
    require(scenarios == 81920, "subfamily scenario census drift")
    require(clean + dirty == scenarios, "subfamily dispatch census drift")
    return {
        "exhaustive_subfamily_scenarios": scenarios,
        "subfamily_clean_anchor_scenarios": clean,
        "subfamily_dirty_anchor_scenarios": dirty,
    }


def mutation_tests() -> int:
    family = tuple(combinations(range(5), 4))
    anchor = family[0]
    triples = tuple(combinations(range(5), 3))
    manifest = exact_dispatch_manifest(family, anchor, triples)
    clean_manifest = exact_dispatch_manifest(family, anchor, ())

    mutations: list[tuple[str, tuple[Any, ...]]] = []

    def add_input(name: str, family_value: Any, anchor_value: Any, triples_value: Any) -> None:
        mutations.append((name, ("input", family_value, anchor_value, triples_value)))

    add_input("missing-anchor", family[1:], anchor, triples)
    add_input("duplicate-family-state", tuple(sorted(family + (family[0],))), anchor, triples)
    add_input("unequal-cardinality", tuple(sorted(family + ((0, 1, 2),))), anchor, triples)
    add_input("duplicate-triple", family, anchor, tuple(sorted(triples + (triples[0],))))

    for name, base, mutator in (
        (
            "wrong-canonical-target",
            manifest,
            lambda data: data.update(canonical_target_bank=[[1, 2, 3]]),
        ),
        (
            "clean-terminal-corruption",
            clean_manifest,
            lambda data: data.update(dispatch_kind="canonical-singleton-target-response"),
        ),
        (
            "category-corruption",
            manifest,
            lambda data: data["candidate_records"][0].update(
                trigger_category="corrupted-category"
            ),
        ),
        (
            "new-triple-witness-corruption",
            manifest,
            lambda data: next(
                record
                for record in data["candidate_records"]
                if record["canonical_new_triple"] is not None
            ).update(canonical_new_triple=[99, 100, 101]),
        ),
        (
            "missing-candidate-record",
            manifest,
            lambda data: data["candidate_records"].pop(),
        ),
        (
            "target-contraction-corruption",
            manifest,
            lambda data: data["target_preserving_branch"]["residuals"].append([99]),
        ),
        (
            "honesty-corruption",
            manifest,
            lambda data: data["claims"].update(all_n_proved_by_checker=1),
        ),
        (
            "seal-corruption",
            manifest,
            lambda data: data.update(manifest_sha256="0" * 64),
        ),
    ):
        candidate = copy.deepcopy(base)
        mutator(candidate)
        mutations.append((name, ("manifest", candidate, family, anchor, triples if base is manifest else ())))

    rejected = 0
    for name, mutation in mutations:
        try:
            if mutation[0] == "input":
                _, family_value, anchor_value, triples_value = mutation
                exact_dispatch_manifest(family_value, anchor_value, triples_value)
            else:
                _, candidate, family_value, anchor_value, triples_value = mutation
                validate_dispatch_manifest(
                    candidate,
                    family_value,
                    anchor_value,
                    triples_value,
                )
        except CanonicalTargetDispatchError:
            rejected += 1
        else:
            raise CanonicalTargetDispatchError(f"mutation accepted: {name}")
    require(rejected == len(mutations), "mutation rejection census drift")
    return rejected


def self_test() -> dict[str, Any]:
    return {
        **validate_contract(),
        **exhaustive_hypergraph_regression(),
        **exhaustive_subfamily_regression(),
        "rejected_mutations": mutation_tests(),
        "contract_sha256": contract_manifest()["contract_sha256"],
    }


def main() -> None:
    print(json.dumps(self_test(), sort_keys=True))


if __name__ == "__main__":
    main()
