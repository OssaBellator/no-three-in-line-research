#!/usr/bin/env python3
"""Verify required-prefix contexts for the canonical masked-host parent rule.

A context is determined by a side length, a deleted labelled-edge mask and a
compatible required labelled-edge set.  The checker reconstructs exactly the
saturated two-layer states avoiding the mask and containing the required set,
then realizes each first-missing prescription branch as another generated
context.

This is a finite conditional T02 theorem.  It does not prove that the actual
prime-power recurrence generates every context, that conditioned residuals are
standard smaller masked hosts, termination, or the all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations, product
from typing import Any, Iterable

from check_prime_power_masked_host_parent_generation import (
    Edge,
    State,
    Triple,
    all_host_edges,
    exact_edge,
    exact_mask,
    generate_exact_triple_universe,
    generate_feasible_family,
)

EXPECTED_CONTRACT_SHA256 = "030398f03aae9f26e71ad867a49ad163752410fb3f6eb437cc2538fdba82e0e1"


class RequiredPrefixGenerationError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RequiredPrefixGenerationError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_required(n: int, raw: Iterable[Iterable[int]]) -> tuple[Edge, ...]:
    required = tuple(exact_edge(edge, n, f"required[{i}]") for i, edge in enumerate(raw))
    require(required == tuple(sorted(required)), "required: canonical order required")
    require(len(required) == len(set(required)), "required: duplicate edge")
    for layer in (0, 1):
        part = tuple(edge for edge in required if edge[0] == layer)
        require(len({edge[1] for edge in part}) == len(part),
                "required: repeated layer row")
        require(len({edge[2] for edge in part}) == len(part),
                "required: repeated layer column")
    physical = tuple((edge[1], edge[2]) for edge in required)
    require(len(physical) == len(set(physical)),
            "required: physical-cell collision")
    return required


def exact_context(
    n: int,
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
) -> tuple[tuple[Edge, ...], tuple[Edge, ...]]:
    deleted = exact_mask(n, deleted_raw)
    required = exact_required(n, required_raw)
    require(set(deleted).isdisjoint(required),
            "deleted and required edges must be disjoint")
    return deleted, required


def context_family(
    n: int,
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
) -> tuple[State, ...]:
    deleted, required = exact_context(n, deleted_raw, required_raw)
    required_set = set(required)
    return tuple(
        state
        for state in generate_feasible_family(n, deleted)
        if required_set <= set(state)
    )


def exact_context_manifest(
    n: int,
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    deleted, required = exact_context(n, deleted_raw, required_raw)
    family = context_family(n, deleted, required)
    universe = generate_exact_triple_universe(family)
    unrestricted = generate_feasible_family(n, deleted)
    require(
        family == tuple(state for state in unrestricted if set(required) <= set(state)),
        "required-prefix restriction identity failed",
    )
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-required-prefix-parent-generation-v1",
        "side": n,
        "deleted_edges": [list(edge) for edge in deleted],
        "required_edges": [list(edge) for edge in required],
        "feasible_family": [[list(edge) for edge in state] for state in family],
        "exact_triple_universe": [
            [list(edge) for edge in triple] for triple in universe
        ],
        "canonical_anchor": None if not family else [list(edge) for edge in family[0]],
        "claims": {
            "host_edges": 2 * n * n,
            "deleted_edges": len(deleted),
            "required_edges": len(required),
            "feasible_states": len(family),
            "realizable_collinear_triples": len(universe),
            "required_prefix_family_generated": 1,
            "required_prefix_restriction_exact": 1,
            "context_triple_universe_generated_from_family": 1,
            "canonical_context_anchor_generated": int(bool(family)),
            "infeasible_context_terminal": int(not family),
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def exact_prescription(n: int, raw: Iterable[Iterable[int]]) -> Triple:
    prescription = tuple(
        exact_edge(edge, n, f"prescription[{i}]") for i, edge in enumerate(raw)
    )
    require(len(prescription) == 3, "prescription: exact size three required")
    require(prescription == tuple(sorted(prescription)),
            "prescription: canonical order required")
    require(len(set(prescription)) == 3, "prescription: duplicate edge")
    return prescription  # type: ignore[return-value]


def exact_state(n: int, raw: Iterable[Iterable[int]], path: str) -> State:
    state = tuple(exact_edge(edge, n, f"{path}[{i}]") for i, edge in enumerate(raw))
    require(state == tuple(sorted(state)), f"{path}: canonical order required")
    require(len(state) == 2 * n and len(state) == len(set(state)),
            f"{path}: saturated state size required")
    return state


def first_missing_index(state: State, prescription: Triple) -> int:
    state_set = set(state)
    return next((i for i, edge in enumerate(prescription) if edge not in state_set), 3)


def exact_first_missing_manifest(
    n: int,
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
    prescription_raw: Iterable[Iterable[int]],
    rejected_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    deleted, required = exact_context(n, deleted_raw, required_raw)
    prescription = exact_prescription(n, prescription_raw)
    rejected = exact_state(n, rejected_raw, "rejected")
    family = context_family(n, deleted, required)
    require(rejected in family, "rejected: absent from contextual family")
    require(set(prescription) <= set(rejected),
            "prescription: absent from rejected state")

    parent_universe = set(generate_exact_triple_universe(family))
    occurrences = {state: 0 for state in family}
    branches: list[dict[str, Any]] = []
    for index in range(4):
        prefix = tuple(sorted(set(required) | set(prescription[:index])))
        exact_required(n, prefix)
        contradiction = False
        if index < 3:
            omitted = prescription[index]
            child_deleted = tuple(sorted(set(deleted) | {omitted}))
            child_required = prefix
            contradiction = omitted in set(required)
        else:
            omitted = None
            child_deleted = deleted
            child_required = tuple(sorted(set(required) | set(prescription)))

        direct = tuple(
            state for state in family
            if first_missing_index(state, prescription) == index
        )
        if contradiction:
            members: tuple[State, ...] = ()
            require(not direct, "required/deleted contradiction branch is not empty")
        else:
            members = context_family(n, child_deleted, child_required)
            require(members == direct,
                    f"branch {index}: generated context differs from direct partition")
        for state in members:
            occurrences[state] += 1

        child_universe = set(generate_exact_triple_universe(members))
        require(child_universe <= parent_universe,
                f"branch {index}: child triple universe is not monotone")
        residuals = (
            [[list(edge) for edge in state] for state in members]
            if index < 3
            else [
                [list(edge) for edge in state if edge not in set(prescription)]
                for state in members
            ]
        )
        if index == 3:
            require(
                len(residuals) == len({
                    tuple(tuple(edge) for edge in residual) for residual in residuals
                }),
                "conditioned prescription contraction is not injective",
            )
        branch: dict[str, Any] = {
            "branch_index": index,
            "deleted_edges": [list(edge) for edge in child_deleted],
            "required_edges": [list(edge) for edge in child_required],
            "omitted_edge": None if omitted is None else list(omitted),
            "context_status": (
                "required-deleted-contradiction-terminal"
                if contradiction else "generated-context"
            ),
            "members": [[list(edge) for edge in state] for state in members],
            "residuals": residuals,
            "context_family_generated": 1,
            "context_restriction_exact": 1,
            "triple_universe_monotone": 1,
            "cardinality_drop": 0 if index < 3 else 3,
        }
        branch["branch_sha256"] = digest(branch)
        branches.append(branch)

    require(set(occurrences.values()) == {1},
            "first-missing contexts do not form a disjoint partition")
    require(
        [branch["branch_index"] for branch in branches
         if [list(edge) for edge in rejected] in branch["members"]] == [3],
        "rejected state is not isolated in the conditioned branch",
    )
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-required-prefix-first-missing-v1",
        "side": n,
        "parent_deleted_edges": [list(edge) for edge in deleted],
        "parent_required_edges": [list(edge) for edge in required],
        "prescription": [list(edge) for edge in prescription],
        "rejected": [list(edge) for edge in rejected],
        "branches": branches,
        "claims": {
            "parent_feasible_states": len(family),
            "first_missing_branch_count": 4,
            "required_prefix_contexts_generated": 1,
            "deletion_extension_exact": 1,
            "required_edge_extension_exact": 1,
            "first_missing_partition_exact": 1,
            "first_missing_partition_pairwise_disjoint": 1,
            "child_triple_universes_monotone": 1,
            "conditioned_branch_set_contraction_exact": 1,
            "conditioned_residual_standard_host_representability_proved": 0,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def validate_context_manifest(
    manifest: Any,
    n: int,
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
) -> dict[str, int]:
    expected = exact_context_manifest(n, deleted_raw, required_raw)
    require(isinstance(manifest, dict) and manifest == expected,
            "context manifest mismatch")
    return copy.deepcopy(expected["claims"])


def validate_first_missing_manifest(
    manifest: Any,
    n: int,
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
    prescription_raw: Iterable[Iterable[int]],
    rejected_raw: Iterable[Iterable[int]],
) -> dict[str, int]:
    expected = exact_first_missing_manifest(
        n, deleted_raw, required_raw, prescription_raw, rejected_raw
    )
    require(isinstance(manifest, dict) and manifest == expected,
            "first-missing manifest mismatch")
    return copy.deepcopy(expected["claims"])


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-required-prefix-parent-generation-v1",
        "source_theorems": [
            "CMR830", "CMR831", "CMR862", "CMR863", "CMR864",
            "CMR2794", "CMR2795", "CMR2796", "CMR2802", "CMR2830",
            "CMR2832", "CMR2833", "CMR2834",
        ],
        "context_semantics": {
            "host": "two labelled permutation layers",
            "deleted_context": "edges forbidden in every state",
            "required_context": "compatible edges present in every state",
            "first_missing_child": "required prefix plus one omitted edge",
        },
        "claims": {
            "required_prefix_family_generated": 1,
            "required_prefix_restriction_exact": 1,
            "context_triple_universe_generated_from_family": 1,
            "deletion_extension_exact": 1,
            "required_edge_extension_exact": 1,
            "first_missing_contexts_generated": 1,
            "first_missing_partition_exact": 1,
            "first_missing_partition_pairwise_disjoint": 1,
            "child_triple_universes_monotone": 1,
            "conditioned_branch_set_contraction_exact": 1,
            "conditioned_residual_standard_host_representability_proved": 0,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["contract_sha256"] = digest(result)
    return result


def validate_contract() -> dict[str, int]:
    contract = contract_manifest()
    require(contract["contract_sha256"] == EXPECTED_CONTRACT_SHA256,
            "built-in contract digest drift")
    return copy.deepcopy(contract["claims"])


def exhaustive_regression() -> dict[str, int]:
    host2 = all_host_edges(2)
    contexts2 = feasible2 = infeasible2 = occurrences2 = 0
    for assignment in product(range(3), repeat=len(host2)):
        deleted = tuple(host2[i] for i, value in enumerate(assignment) if value == 1)
        required = tuple(host2[i] for i, value in enumerate(assignment) if value == 2)
        try:
            manifest = exact_context_manifest(2, deleted, required)
        except RequiredPrefixGenerationError:
            continue
        contexts2 += 1
        claims = manifest["claims"]
        feasible2 += int(claims["feasible_states"] > 0)
        infeasible2 += claims["infeasible_context_terminal"]
        occurrences2 += claims["feasible_states"]

    host3 = all_host_edges(3)
    scenarios3 = branch_records3 = nonempty3 = 0
    for deleted_size in range(2):
        for deleted in combinations(host3, deleted_size):
            family = context_family(3, deleted, ())
            universe = generate_exact_triple_universe(family)
            for rejected in family:
                prescriptions = tuple(
                    triple for triple in universe if set(triple) <= set(rejected)
                )
                for prescription in prescriptions:
                    for required_size in range(2):
                        for required in combinations(rejected, required_size):
                            manifest = exact_first_missing_manifest(
                                3, deleted, required, prescription, rejected
                            )
                            scenarios3 += 1
                            branch_records3 += len(manifest["branches"])
                            nonempty3 += sum(
                                int(bool(branch["members"]))
                                for branch in manifest["branches"]
                            )

    require(feasible2 + infeasible2 == contexts2,
            "side-two context census drift")
    require(branch_records3 == 4 * scenarios3,
            "side-three branch census drift")
    require(
        (contexts2, feasible2, infeasible2, occurrences2) == (2592, 511, 2081, 512),
        "side-two exact census drift",
    )
    require(
        (scenarios3, branch_records3, nonempty3) == (728, 2912, 1624),
        "side-three exact census drift",
    )
    return {
        "side_two_valid_contexts": contexts2,
        "side_two_feasible_contexts": feasible2,
        "side_two_infeasible_contexts": infeasible2,
        "side_two_state_occurrences": occurrences2,
        "side_three_first_missing_scenarios": scenarios3,
        "side_three_branch_records": branch_records3,
        "side_three_nonempty_branch_records": nonempty3,
    }


def mutation_tests() -> int:
    n = 3
    family = context_family(n, (), ())
    rejected = next(state for state in family if generate_exact_triple_universe((state,)))
    prescription = generate_exact_triple_universe((rejected,))[0]
    context_manifest = exact_context_manifest(n, (), ())
    split_manifest = exact_first_missing_manifest(n, (), (), prescription, rejected)
    rejected_total = 0

    bad_calls = [
        lambda: exact_context_manifest(n, ((1, 0, 0), (0, 0, 0)), ()),
        lambda: exact_context_manifest(n, ((0, 0, 0),), ((0, 0, 0),)),
        lambda: exact_context_manifest(n, (), ((0, 0, 0), (0, 0, 1))),
        lambda: exact_context_manifest(n, (), ((0, 0, 0), (1, 0, 0))),
        lambda: exact_first_missing_manifest(
            n, (), (), prescription,
            next(state for state in family if not set(prescription) <= set(state)),
        ),
    ]
    for call in bad_calls:
        try:
            call()
        except (ValueError, StopIteration):
            rejected_total += 1
        else:
            raise RequiredPrefixGenerationError("malformed input accepted")

    bad_context = copy.deepcopy(context_manifest)
    bad_context["feasible_family"].pop()
    bad_split = copy.deepcopy(split_manifest)
    bad_split["branches"][0]["members"].append(bad_split["rejected"])
    bad_honesty = copy.deepcopy(split_manifest)
    bad_honesty["claims"]["all_n_proved_by_checker"] = 1
    bad_seal = copy.deepcopy(split_manifest)
    bad_seal["manifest_sha256"] = "0" * 64
    checks = [
        lambda: validate_context_manifest(bad_context, n, (), ()),
        lambda: validate_first_missing_manifest(
            bad_split, n, (), (), prescription, rejected
        ),
        lambda: validate_first_missing_manifest(
            bad_honesty, n, (), (), prescription, rejected
        ),
        lambda: validate_first_missing_manifest(
            bad_seal, n, (), (), prescription, rejected
        ),
    ]
    for check in checks:
        try:
            check()
        except RequiredPrefixGenerationError:
            rejected_total += 1
        else:
            raise RequiredPrefixGenerationError("corrupted manifest accepted")
    require(rejected_total == 9, "mutation rejection census drift")
    return rejected_total


def self_test() -> dict[str, Any]:
    return {
        **validate_contract(),
        **exhaustive_regression(),
        "rejected_mutations": mutation_tests(),
        "contract_sha256": contract_manifest()["contract_sha256"],
    }


def main() -> None:
    print(json.dumps(self_test(), sort_keys=True))


if __name__ == "__main__":
    main()
