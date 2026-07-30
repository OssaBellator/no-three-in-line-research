#!/usr/bin/env python3
"""Verify canonical masked-host family, triple-universe and anchor generation.

For a side-n two-layer labelled permutation host and a monotone deleted-edge mask,
this checker reconstructs every feasible saturated state, the exact realizable
collinear-triple universe, and the lexicographically least feasible anchor.  The
anchor is then dispatched canonically: an empty family is infeasible, a
triple-free anchor is clean, and a dirty anchor selects its least triple and
uses the complete local response rule.

This is a finite conditional T02 theorem.  It does not prove that the actual
prime-power recurrence generates every required mask, that these masks exhaust
all parent/closure situations, termination, or the all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations, permutations
from typing import Any, Iterable

Edge = tuple[int, int, int]       # (layer,row,column)
State = tuple[Edge, ...]
Triple = tuple[Edge, Edge, Edge]
EXPECTED_CONTRACT_SHA256 = "8fe3f68df6b25cf3c86e8d822ef37bfb9c8778382d3a3b6a58ac5d21f5595f70"


class MaskedHostGenerationError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise MaskedHostGenerationError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_edge(raw: Iterable[int], n: int, path: str) -> Edge:
    values = tuple(raw)
    require(len(values) == 3, f"{path}: three coordinates required")
    require(all(isinstance(x, int) and not isinstance(x, bool) for x in values),
            f"{path}: integer coordinates required")
    layer, row, column = values
    require(layer in (0, 1), f"{path}: layer must be 0 or 1")
    require(0 <= row < n and 0 <= column < n, f"{path}: row/column outside host")
    return layer, row, column


def exact_mask(n: int, deleted_raw: Iterable[Iterable[int]]) -> tuple[Edge, ...]:
    require(isinstance(n, int) and not isinstance(n, bool) and n >= 1,
            "side length must be a positive integer")
    deleted = tuple(exact_edge(edge, n, f"deleted[{i}]")
                    for i, edge in enumerate(deleted_raw))
    require(deleted == tuple(sorted(deleted)), "deleted mask must be canonically sorted")
    require(len(deleted) == len(set(deleted)), "deleted mask contains duplicate edge")
    return deleted


def all_host_edges(n: int) -> tuple[Edge, ...]:
    return tuple((layer, row, column)
                 for layer in range(2)
                 for row in range(n)
                 for column in range(n))


def state_from_permutations(left: tuple[int, ...], right: tuple[int, ...]) -> State:
    n = len(left)
    return tuple(sorted(
        tuple((0, row, left[row]) for row in range(n))
        + tuple((1, row, right[row]) for row in range(n))
    ))


def generate_feasible_family(n: int, deleted_raw: Iterable[Iterable[int]]) -> tuple[State, ...]:
    deleted = set(exact_mask(n, deleted_raw))
    family: list[State] = []
    for left in permutations(range(n)):
        for right in permutations(range(n)):
            if any(left[row] == right[row] for row in range(n)):
                continue
            state = state_from_permutations(left, right)
            if deleted.isdisjoint(state):
                family.append(state)
    return tuple(sorted(family))


def validate_saturated_state(state: State, n: int, deleted: set[Edge]) -> None:
    require(len(state) == 2 * n and len(state) == len(set(state)),
            "state must contain exactly 2n distinct labelled edges")
    require(deleted.isdisjoint(state), "state contains deleted edge")
    for layer in (0, 1):
        part = tuple(edge for edge in state if edge[0] == layer)
        require(len(part) == n, "each layer must contain n edges")
        require({edge[1] for edge in part} == set(range(n)), "layer rows not saturated")
        require({edge[2] for edge in part} == set(range(n)), "layer columns not saturated")
    physical = [(edge[1], edge[2]) for edge in state]
    require(len(physical) == len(set(physical)), "layers collide in a physical cell")


def is_collinear(triple: Triple) -> bool:
    points = tuple((edge[1], edge[2]) for edge in triple)
    if len(set(points)) != 3:
        return False
    (x1, y1), (x2, y2), (x3, y3) = points
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def generate_exact_triple_universe(family: tuple[State, ...]) -> tuple[Triple, ...]:
    triples: set[Triple] = set()
    for state in family:
        for raw in combinations(state, 3):
            triple = tuple(raw)
            if is_collinear(triple):
                triples.add(triple)  # type: ignore[arg-type]
    return tuple(sorted(triples))


def state_triples(state: State, universe: tuple[Triple, ...]) -> tuple[Triple, ...]:
    edge_set = set(state)
    return tuple(triple for triple in universe if set(triple) <= edge_set)


def first_missing(state: State, prescription: Triple) -> int:
    edge_set = set(state)
    return next((i for i, edge in enumerate(prescription) if edge not in edge_set), 3)


def prescription_partition(family: tuple[State, ...], rejected: State,
                           prescription: Triple) -> dict[str, Any]:
    require(set(prescription) <= set(rejected), "new triple absent from rejected state")
    occurrences = {state: 0 for state in family}
    branches: list[dict[str, Any]] = []
    pset = set(prescription)
    for index in range(4):
        members = tuple(state for state in family if first_missing(state, prescription) == index)
        for state in members:
            occurrences[state] += 1
        residuals = ([list(map(list, state)) for state in members] if index < 3 else
                     [[list(edge) for edge in state if edge not in pset] for state in members])
        if index == 3:
            require(len(residuals) == len({tuple(tuple(edge) for edge in row) for row in residuals}),
                    "conditioned triple contraction not injective")
        branch: dict[str, Any] = {
            "branch_index": index,
            "operation_kind": (
                "new-triple-first-missing-deletion"
                if index < 3 else "new-triple-conditioned-contraction"
            ),
            "required_prefix": [list(edge) for edge in prescription[:index]],
            "omitted_edge": list(prescription[index]) if index < 3 else None,
            "members": [[list(edge) for edge in state] for state in members],
            "residuals": residuals,
            "cardinality_drop": 0 if index < 3 else 3,
        }
        branch["branch_sha256"] = digest(branch)
        branches.append(branch)
    require(set(occurrences.values()) == {1}, "new-triple branches are not a partition")
    require([b["branch_index"] for b in branches
             if [list(edge) for edge in rejected] in b["members"]] == [3],
            "rejected candidate not isolated in conditioned branch")
    result = {
        "prescription": [list(edge) for edge in prescription],
        "branches": branches,
        "exact_union": 1,
        "pairwise_disjoint": 1,
        "conditioned_cardinality_drop": 3,
    }
    result["partition_sha256"] = digest(result)
    return result


def dirty_candidate_record(family: tuple[State, ...], anchor: State, candidate: State,
                           universe: tuple[Triple, ...], target: Triple) -> dict[str, Any]:
    anchor_triples = state_triples(anchor, universe)
    candidate_triples = state_triples(candidate, universe)
    target_preserved = int(set(target) <= set(candidate))
    new = tuple(sorted(set(candidate_triples) - set(anchor_triples)))
    delta = len(candidate_triples) - len(anchor_triples)
    if target_preserved:
        category, witness, partition = "canonical-target-preserving-contraction", None, None
    elif delta < 0:
        category, witness, partition = "canonical-target-destroying-strict-improvement", None, None
    else:
        require(new, "nonimproving target destruction has no new triple")
        witness = new[0]
        category = "canonical-target-destroying-new-triple"
        partition = prescription_partition(family, candidate, witness)
    record = {
        "candidate": [list(edge) for edge in candidate],
        "target_preserved": target_preserved,
        "anchor_potential": len(anchor_triples),
        "candidate_potential": len(candidate_triples),
        "potential_delta": delta,
        "new_triples": [[[int(x) for x in edge] for edge in triple] for triple in new],
        "trigger_category": category,
        "canonical_new_triple": (
            None if witness is None else [list(edge) for edge in witness]
        ),
        "new_triple_partition": partition,
    }
    record["candidate_record_sha256"] = digest(record)
    return record


def exact_manifest(n: int, deleted_raw: Iterable[Iterable[int]]) -> dict[str, Any]:
    deleted = exact_mask(n, deleted_raw)
    deleted_set = set(deleted)
    family = generate_feasible_family(n, deleted)
    for state in family:
        validate_saturated_state(state, n, deleted_set)
    require(len(family) == len(set(family)), "family generation produced duplicates")
    universe = generate_exact_triple_universe(family)
    require(all(is_collinear(triple) for triple in universe),
            "triple universe contains noncollinear triple")
    require(all(any(set(triple) <= set(state) for state in family) for triple in universe),
            "triple universe contains unrealizable triple")

    mode: str
    anchor: State | None
    target: Triple | None
    target_branch: dict[str, Any] | None
    records: list[dict[str, Any]]
    if not family:
        mode, anchor, target, target_branch, records = (
            "infeasible-mask-terminal", None, None, None, []
        )
    else:
        anchor = family[0]
        anchor_triples = state_triples(anchor, universe)
        if not anchor_triples:
            mode, target, target_branch, records = (
                "clean-anchor-terminal", None, None, []
            )
        else:
            mode, target = "dirty-anchor-canonical-target-dispatch", anchor_triples[0]
            preserving = tuple(state for state in family if set(target) <= set(state))
            residuals = [[list(edge) for edge in state if edge not in set(target)]
                         for state in preserving]
            require(len(residuals) == len({tuple(tuple(edge) for edge in row)
                                           for row in residuals}),
                    "canonical target contraction not injective")
            target_branch = {
                "operation_kind": "canonical-singleton-target-contraction",
                "members": [[list(edge) for edge in state] for state in preserving],
                "residuals": residuals,
                "cardinality_drop": 3,
            }
            records = [
                dirty_candidate_record(family, anchor, state, universe, target)
                for state in family if state != anchor
            ]

    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-masked-host-parent-generation-v1",
        "side": n,
        "deleted_edges": [list(edge) for edge in deleted],
        "feasible_family": [[list(edge) for edge in state] for state in family],
        "exact_triple_universe": [
            [list(edge) for edge in triple] for triple in universe
        ],
        "anchor": None if anchor is None else [list(edge) for edge in anchor],
        "dispatch_mode": mode,
        "canonical_target": None if target is None else [list(edge) for edge in target],
        "target_preserving_branch": target_branch,
        "candidate_records": records,
        "claims": {
            "host_edges": 2 * n * n,
            "deleted_edges": len(deleted),
            "feasible_states": len(family),
            "realizable_collinear_triples": len(universe),
            "masked_host_family_generated": 1,
            "family_generation_duplicate_free": 1,
            "triple_universe_generated_from_family": 1,
            "canonical_anchor_generated": int(bool(family)),
            "infeasible_mask_terminal": int(not family),
            "clean_anchor_terminal": int(mode == "clean-anchor-terminal"),
            "dirty_anchor_dispatch": int(mode == "dirty-anchor-canonical-target-dispatch"),
            "canonical_target_bank_external_choice_required": 0,
            "local_masked_parent_dispatch_complete": 1,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def validate_manifest(manifest: Any, n: int,
                      deleted_raw: Iterable[Iterable[int]]) -> dict[str, int]:
    require(isinstance(manifest, dict) and manifest == exact_manifest(n, deleted_raw),
            "canonical masked-host manifest mismatch")
    return copy.deepcopy(manifest["claims"])


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-masked-host-parent-generation-v1",
        "source_theorems": [
            "CMR830", "CMR831", "CMR838", "CMR839", "CMR840",
            "CMR841", "CMR845", "CMR2818", "CMR2820", "CMR2822",
        ],
        "host_semantics": {
            "layers": 2,
            "each_layer": "permutation matching",
            "cross_layer_constraint": "physical-cell disjointness",
            "parent_context": "monotone labelled-edge deletion mask",
        },
        "claims": {
            "masked_host_family_generated": 1,
            "family_generation_duplicate_free": 1,
            "triple_universe_generated_from_family": 1,
            "canonical_anchor_and_target_generated": 1,
            "empty_clean_dirty_dispatch_exhaustive": 1,
            "local_masked_parent_dispatch_complete": 1,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["contract_sha256"] = digest(result)
    return result


def validate_contract() -> dict[str, int]:
    contract = contract_manifest()
    if EXPECTED_CONTRACT_SHA256 != "TO_BE_FILLED":
        require(contract["contract_sha256"] == EXPECTED_CONTRACT_SHA256,
                "built-in contract digest drift")
    return copy.deepcopy(contract["claims"])


def exhaustive_regression() -> dict[str, int]:
    # Every mask on the complete side-two labelled host.
    host2 = all_host_edges(2)
    masks2 = feasible2 = infeasible2 = clean2 = dirty2 = 0
    state_occurrences2 = 0
    for mask_bits in range(1 << len(host2)):
        deleted = tuple(edge for i, edge in enumerate(host2)
                        if mask_bits & (1 << i))
        manifest = exact_manifest(2, deleted)
        claims = manifest["claims"]
        masks2 += 1
        feasible2 += int(claims["feasible_states"] > 0)
        infeasible2 += claims["infeasible_mask_terminal"]
        clean2 += claims["clean_anchor_terminal"]
        dirty2 += claims["dirty_anchor_dispatch"]
        state_occurrences2 += claims["feasible_states"]

    # Every side-three mask of size at most two.
    host3 = all_host_edges(3)
    masks3 = feasible3 = clean3 = dirty3 = candidates3 = 0
    for size in range(3):
        for deleted in combinations(host3, size):
            manifest = exact_manifest(3, deleted)
            claims = manifest["claims"]
            masks3 += 1
            feasible3 += int(claims["feasible_states"] > 0)
            clean3 += claims["clean_anchor_terminal"]
            dirty3 += claims["dirty_anchor_dispatch"]
            candidates3 += len(manifest["candidate_records"])

    require(masks2 == 256 and feasible2 + infeasible2 == masks2,
            "side-two mask census drift")
    require(clean2 + dirty2 == feasible2, "side-two dispatch census drift")
    require(masks3 == 172 and clean3 + dirty3 == feasible3,
            "side-three mask census drift")
    return {
        "side_two_masks": masks2,
        "side_two_feasible_masks": feasible2,
        "side_two_infeasible_masks": infeasible2,
        "side_two_clean_anchors": clean2,
        "side_two_dirty_anchors": dirty2,
        "side_two_state_occurrences": state_occurrences2,
        "side_three_masks_size_at_most_two": masks3,
        "side_three_feasible_masks": feasible3,
        "side_three_clean_anchors": clean3,
        "side_three_dirty_anchors": dirty3,
        "side_three_candidate_records": candidates3,
    }


def mutation_tests() -> int:
    n, deleted = 3, ()
    manifest = exact_manifest(n, deleted)
    mutations: list[tuple[str, Any]] = []

    for name, bad_deleted in (
        ("unsorted-mask", ((1, 0, 0), (0, 0, 0))),
        ("duplicate-mask-edge", ((0, 0, 0), (0, 0, 0))),
        ("bad-layer", ((2, 0, 0),)),
        ("out-of-range-edge", ((0, 3, 0),)),
    ):
        mutations.append((name, ("input", bad_deleted)))

    def add_manifest_mutation(name: str, mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append((name, ("manifest", candidate)))

    add_manifest_mutation("family-state-removal",
                          lambda data: data["feasible_family"].pop())
    add_manifest_mutation("triple-universe-corruption",
                          lambda data: data["exact_triple_universe"].append(
                              [[[0, 0, 0], [0, 0, 1], [0, 1, 0]]]))
    add_manifest_mutation("anchor-corruption",
                          lambda data: data.update(anchor=data["feasible_family"][-1]))
    add_manifest_mutation("dispatch-corruption",
                          lambda data: data.update(dispatch_mode="clean-anchor-terminal"))
    add_manifest_mutation("target-corruption",
                          lambda data: data.update(canonical_target=None))
    add_manifest_mutation("candidate-category-corruption",
                          lambda data: data["candidate_records"][0].update(
                              trigger_category="wrong"))
    add_manifest_mutation("honesty-corruption",
                          lambda data: data["claims"].update(all_n_proved_by_checker=1))
    add_manifest_mutation("seal-corruption",
                          lambda data: data.update(manifest_sha256="0" * 64))

    rejected = 0
    for name, mutation in mutations:
        try:
            if mutation[0] == "input":
                exact_manifest(n, mutation[1])
            else:
                validate_manifest(mutation[1], n, deleted)
        except MaskedHostGenerationError:
            rejected += 1
        else:
            raise MaskedHostGenerationError(f"mutation accepted: {name}")
    require(rejected == len(mutations), "mutation rejection census drift")
    return rejected


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
