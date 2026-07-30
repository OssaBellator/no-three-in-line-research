#!/usr/bin/env python3
"""Check the complete local target-trigger response rule.

For a fixed anchor and nonempty target bank, every alternative is exactly one of:
(1) target-preserving, hence conditioned on the full target core;
(2) target-destroying with lower triple potential; or
(3) target-destroying without lower potential, hence carrying a canonical new
triple and a duplicate-free first-missing partition.

This is a finite conditional T02 theorem. It does not generate the global parent
family or prove recurrence exhaustiveness, and always reports
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
EXPECTED_CONTRACT_SHA256 = "c7239521fb73e0347783e76ebfde83d96e968712376745542b5a93888312c0ef"


class TriggerPartitionError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise TriggerPartitionError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode()).hexdigest()


def exact_set(raw: Iterable[int], path: str, size: int | None = None) -> State:
    require(not isinstance(raw, (str, bytes)), f"{path}: iterable required")
    values = tuple(raw)
    require(values and values == tuple(sorted(values)), f"{path}: nonempty sorted values required")
    require(len(values) == len(set(values)), f"{path}: duplicate value")
    require(all(isinstance(x, int) and not isinstance(x, bool) for x in values), f"{path}: integer values required")
    if size is not None:
        require(len(values) == size, f"{path}: size {size} required")
    return values


def exact_inputs(family_raw: Iterable[Iterable[int]], anchor_raw: Iterable[int],
                 triples_raw: Iterable[Iterable[int]], targets_raw: Iterable[Iterable[int]]) -> tuple[tuple[State, ...], State, tuple[Triple, ...], tuple[Triple, ...]]:
    family = tuple(exact_set(x, f"family[{i}]") for i, x in enumerate(family_raw))
    require(family and family == tuple(sorted(family)), "family: canonical order required")
    require(len(family) == len(set(family)), "family: duplicate state")
    require(len({len(x) for x in family}) == 1, "family: equal cardinality required")
    anchor = exact_set(anchor_raw, "anchor")
    require(anchor in family, "anchor: absent from family")
    triples = tuple(exact_set(x, f"triples[{i}]", 3) for i, x in enumerate(triples_raw))
    require(triples == tuple(sorted(triples)) and len(triples) == len(set(triples)), "triples: canonical unique order required")
    targets = tuple(exact_set(x, f"targets[{i}]", 3) for i, x in enumerate(targets_raw))
    require(targets and targets == tuple(sorted(targets)) and len(targets) == len(set(targets)), "targets: nonempty canonical unique order required")
    triple_set, anchor_set = set(triples), set(anchor)
    require(all(t in triple_set for t in targets), "targets: target absent from triple universe")
    require(all(set(t) <= anchor_set for t in targets), "targets: target absent from anchor")
    return family, anchor, triples, targets  # type: ignore[return-value]


def state_triples(state: State, triples: tuple[Triple, ...]) -> tuple[Triple, ...]:
    cells = set(state)
    return tuple(t for t in triples if set(t) <= cells)


def first_missing(state: State, prescription: Triple) -> int:
    cells = set(state)
    return next((i for i, x in enumerate(prescription) if x not in cells), 3)


def prescription_partition(family: tuple[State, ...], rejected: State,
                           prescription: Triple) -> dict[str, Any]:
    require(set(prescription) <= set(rejected), "prescription absent from rejected candidate")
    occurrences = {state: 0 for state in family}
    branches = []
    pset = set(prescription)
    for i in range(4):
        members = tuple(state for state in family if first_missing(state, prescription) == i)
        for state in members:
            occurrences[state] += 1
        residuals = ([list(state) for state in members] if i < 3 else
                     [[x for x in state if x not in pset] for state in members])
        if i == 3:
            require(len(residuals) == len({tuple(x) for x in residuals}), "conditioned contraction not injective")
        branch = {
            "branch_index": i,
            "operation_kind": "new-triple-first-missing-deletion" if i < 3 else "new-triple-conditioned-contraction",
            "required_prefix": list(prescription[:i]),
            "omitted_cell": prescription[i] if i < 3 else None,
            "members": [list(state) for state in members],
            "residuals": residuals,
            "cardinality_drop": 0 if i < 3 else 3,
        }
        branch["branch_sha256"] = digest(branch)
        branches.append(branch)
    require(set(occurrences.values()) == {1}, "prescription branches not an exact partition")
    require([b["branch_index"] for b in branches if list(rejected) in b["members"]] == [3], "rejected candidate not isolated")
    result = {"prescription": list(prescription), "branches": branches,
              "exact_union": 1, "pairwise_disjoint": 1,
              "conditioned_cardinality_drop": 3}
    result["partition_sha256"] = digest(result)
    return result


def candidate_record(family: tuple[State, ...], anchor: State, candidate: State,
                     triples: tuple[Triple, ...], targets: tuple[Triple, ...]) -> dict[str, Any]:
    anchor_triples = state_triples(anchor, triples)
    candidate_triples = state_triples(candidate, triples)
    lost = tuple(t for t in targets if t not in set(candidate_triples))
    new = tuple(sorted(set(candidate_triples) - set(anchor_triples)))
    delta = len(candidate_triples) - len(anchor_triples)
    if not lost:
        category, witness, split = "target-preserving-core-contraction", None, None
    elif delta < 0:
        category, witness, split = "target-destroying-strict-improvement", None, None
    else:
        require(len(new) >= len(lost) and new, "CMR698 new-triple inequality failed")
        category, witness = "target-destroying-nonimproving-new-triple", new[0]
        split = prescription_partition(family, candidate, witness)
    record = {
        "candidate": list(candidate), "anchor_potential": len(anchor_triples),
        "candidate_potential": len(candidate_triples), "potential_delta": delta,
        "lost_targets": [list(t) for t in lost], "new_triples": [list(t) for t in new],
        "trigger_category": category,
        "canonical_new_triple": None if witness is None else list(witness),
        "new_triple_partition": split,
    }
    record["candidate_record_sha256"] = digest(record)
    return record


def exact_manifest(family_raw: Iterable[Iterable[int]], anchor_raw: Iterable[int],
                   triples_raw: Iterable[Iterable[int]], targets_raw: Iterable[Iterable[int]]) -> dict[str, Any]:
    family, anchor, triples, targets = exact_inputs(family_raw, anchor_raw, triples_raw, targets_raw)
    core = tuple(sorted({x for target in targets for x in target}))
    core_set = set(core)
    preserving = tuple(state for state in family if all(set(t) <= set(state) for t in targets))
    require(preserving == tuple(state for state in family if core_set <= set(state)), "target preservation differs from core containment")
    residuals = [[x for x in state if x not in core_set] for state in preserving]
    require(len(residuals) == len({tuple(x) for x in residuals}), "target-core contraction not injective")
    alternatives = tuple(state for state in family if state != anchor)
    records = [candidate_record(family, anchor, state, triples, targets) for state in alternatives]
    categories = {name: 0 for name in (
        "target-preserving-core-contraction",
        "target-destroying-strict-improvement",
        "target-destroying-nonimproving-new-triple",
    )}
    for record in records:
        categories[record["trigger_category"]] += 1
    require(sum(categories.values()) == len(alternatives), "candidate classification not exhaustive")
    result: dict[str, Any] = {
        "version": 1, "rule_kind": "local-target-trigger-response-v1",
        "family": [list(x) for x in family], "anchor": list(anchor),
        "triple_universe": [list(x) for x in triples],
        "designated_targets": [list(x) for x in targets], "target_core": list(core),
        "target_preserving_branch": {
            "operation_kind": "target-preserving-core-contraction",
            "members": [list(x) for x in preserving], "residuals": residuals,
            "cardinality_drop": len(core),
        },
        "candidate_records": records,
        "claims": {
            "family_states": len(family), "alternative_candidates": len(alternatives),
            "target_preserving_alternatives": categories["target-preserving-core-contraction"],
            "target_destroying_strict_improvements": categories["target-destroying-strict-improvement"],
            "target_destroying_nonimproving_candidates": categories["target-destroying-nonimproving-new-triple"],
            "exact_candidate_trigger_partition": 1,
            "target_preserving_equals_core_conditioned": 1,
            "target_core_contraction_injective": 1,
            "nonimproving_target_destruction_new_triple": 1,
            "local_target_response_rule_ready": 1,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def validate_manifest(manifest: Any, *inputs: Any) -> dict[str, int]:
    require(isinstance(manifest, dict) and manifest == exact_manifest(*inputs), "canonical manifest mismatch")
    return copy.deepcopy(manifest["claims"])


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1, "rule_kind": "local-target-trigger-response-v1",
        "source_theorems": ["CMR698", "CMR866", "CMR867", "CMR869", "CMR2794", "CMR2795", "CMR2799", "CMR2800"],
        "trigger_categories": [
            "target-preserving-core-contraction",
            "target-destroying-strict-improvement",
            "target-destroying-nonimproving-new-triple",
        ],
        "claims": {
            "exact_candidate_trigger_partition": 1,
            "target_preserving_core_contraction": 1,
            "strict_improvement_action": 1,
            "nonimproving_new_triple_action": 1,
            "local_target_response_rule_ready": 1,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["contract_sha256"] = digest(result)
    return result


def exhaustive_hypergraphs() -> dict[str, int]:
    states, triples = tuple(combinations(range(5), 4)), tuple(combinations(range(5), 3))
    scenarios = candidates = preserving = improving = nonimproving = 0
    for mask in range(1 << len(triples)):
        hypergraph = tuple(t for i, t in enumerate(triples) if mask & (1 << i))
        if not hypergraph:
            continue
        hset = set(hypergraph)
        for anchor in states:
            available = tuple(t for t in combinations(anchor, 3) if t in hset)
            for tmask in range(1, 1 << len(available)):
                targets = tuple(t for i, t in enumerate(available) if tmask & (1 << i))
                claims = exact_manifest(states, anchor, hypergraph, targets)["claims"]
                scenarios += 1
                candidates += claims["alternative_candidates"]
                preserving += claims["target_preserving_alternatives"]
                improving += claims["target_destroying_strict_improvements"]
                nonimproving += claims["target_destroying_nonimproving_candidates"]
    require((scenarios, candidates) == (20800, 83200), "hypergraph census drift")
    return {"exhaustive_hypergraph_scenarios": scenarios,
            "exhaustive_candidate_records": candidates,
            "preserving_candidate_records": preserving,
            "improving_candidate_records": improving,
            "nonimproving_candidate_records": nonimproving}


def exhaustive_subfamilies() -> dict[str, int]:
    states, triples = tuple(combinations(range(5), 4)), tuple(combinations(range(5), 3))
    scenarios = candidates = 0
    for anchor in states:
        others = tuple(x for x in states if x != anchor)
        target_options = tuple(combinations(anchor, 3))
        for tmask in range(1, 1 << 4):
            targets = tuple(t for i, t in enumerate(target_options) if tmask & (1 << i))
            for fmask in range(1 << 4):
                family = tuple(sorted((anchor,) + tuple(x for i, x in enumerate(others) if fmask & (1 << i))))
                claims = exact_manifest(family, anchor, triples, targets)["claims"]
                scenarios += 1
                candidates += claims["alternative_candidates"]
    require((scenarios, candidates) == (1200, 2400), "subfamily census drift")
    return {"exhaustive_subfamily_scenarios": scenarios,
            "exhaustive_subfamily_candidate_records": candidates}


def fixture() -> tuple[Any, ...]:
    return (
        tuple(combinations(range(5), 4)),
        (0, 1, 2, 3),
        tuple(sorted({(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3),
                      (1, 2, 4), (1, 3, 4), (2, 3, 4)})),
        ((0, 1, 2),),
    )


def mutation_tests() -> int:
    family, anchor, triples, targets = fixture()
    manifest = exact_manifest(family, anchor, triples, targets)
    require((manifest["claims"]["target_preserving_alternatives"],
             manifest["claims"]["target_destroying_strict_improvements"],
             manifest["claims"]["target_destroying_nonimproving_candidates"]) == (1, 2, 1), "fixture category drift")
    mutations: list[tuple[str, Any]] = [
        ("input", (family + (family[0],), anchor, triples, targets)),
        ("input", (tuple(sorted(family + ((0, 1, 2),))), anchor, triples, targets)),
        ("input", (family[1:], anchor, triples, targets)),
        ("input", (family, anchor, triples + (triples[0],), targets)),
        ("input", (family, anchor, triples, ((0, 2, 4),))),
        ("input", (family, anchor, triples + ((0, 2, 4),), ((0, 2, 4),))),
    ]
    for change in (
        lambda x: x.update(target_core=[99]),
        lambda x: x["candidate_records"][0].update(trigger_category="bad"),
        lambda x: x["candidate_records"][-1].update(canonical_new_triple=[0, 1, 2]),
        lambda x: x["candidate_records"].pop(),
        lambda x: x["claims"].update(all_n_proved_by_checker=1),
        lambda x: x.update(manifest_sha256="0" * 64),
    ):
        bad = copy.deepcopy(manifest)
        change(bad)
        mutations.append(("manifest", bad))
    rejected = 0
    for kind, value in mutations:
        try:
            exact_manifest(*value) if kind == "input" else validate_manifest(value, family, anchor, triples, targets)
        except TriggerPartitionError:
            rejected += 1
        else:
            raise TriggerPartitionError("mutation accepted")
    require(rejected == 12, "mutation census drift")
    return rejected


def self_test() -> dict[str, Any]:
    contract = contract_manifest()
    if EXPECTED_CONTRACT_SHA256 != "TO_BE_FILLED":
        require(contract["contract_sha256"] == EXPECTED_CONTRACT_SHA256, "contract digest drift")
    return {**contract["claims"], **exhaustive_hypergraphs(), **exhaustive_subfamilies(),
            "rejected_mutations": mutation_tests(),
            "contract_sha256": contract["contract_sha256"]}


def main() -> None:
    print(json.dumps(self_test(), sort_keys=True))


if __name__ == "__main__":
    main()
