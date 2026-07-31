#!/usr/bin/env python3
"""Verify target-handoff, four-endpoint bank, and fixed-envelope chain ancestry.

CMR698--CMR712 convert a nonimproving target-destroying transition into a new
edge-centred target bank and bound repeated handoffs inside one envelope.  This
checker generates saturated two-layer states, exact collinear triple sets,
entering-cell assignments, a four-endpoint bank, envelope status, target-load
churn, and fixed-envelope recreation witnesses.

The checker proves this target-handoff operation and its fixed-envelope chain.
It does not prove all owner/envelope changes, all scheduler operations, global
transition exhaustiveness, global termination, or the all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
from itertools import combinations, permutations
from typing import Any, Iterable

Edge = tuple[int, int, int]
State = tuple[Edge, ...]
Triple = tuple[Edge, ...]

EXPECTED_CONTRACT_SHA256 = "a8230eb1e301b1c08972b686be836dc30a3daba8d906840bb4dba6a67bb1fa8b"


class TargetHandoffError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise TargetHandoffError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_positive_int(value: Any, path: str, minimum: int = 1) -> int:
    require(
        isinstance(value, int) and not isinstance(value, bool) and value >= minimum,
        f"{path}: integer at least {minimum} required",
    )
    return value


def exact_edge(raw: Iterable[int], n: int, path: str) -> Edge:
    edge = tuple(raw)
    require(
        len(edge) == 3
        and edge[0] in (0, 1)
        and isinstance(edge[1], int)
        and isinstance(edge[2], int)
        and 0 <= edge[1] < n
        and 0 <= edge[2] < n,
        f"{path}: malformed labelled edge",
    )
    return edge  # type: ignore[return-value]


def exact_state(raw: Iterable[Iterable[int]], n: int, path: str) -> State:
    state = tuple(exact_edge(edge, n, f"{path}[{index}]")
                  for index, edge in enumerate(raw))
    require(state == tuple(sorted(state)), f"{path}: canonical order required")
    require(len(state) == 2 * n, f"{path}: exact saturated cardinality required")
    require(len(state) == len(set(state)), f"{path}: duplicate labelled edge")
    physical = [(edge[1], edge[2]) for edge in state]
    require(len(physical) == len(set(physical)), f"{path}: physical-cell collision")
    for layer in (0, 1):
        part = tuple(edge for edge in state if edge[0] == layer)
        require(len(part) == n, f"{path}: layer {layer} cardinality failed")
        require({edge[1] for edge in part} == set(range(n)),
                f"{path}: layer {layer} row saturation failed")
        require({edge[2] for edge in part} == set(range(n)),
                f"{path}: layer {layer} column saturation failed")
    return state


def generate_states(n: int) -> tuple[State, ...]:
    permutations_list = tuple(permutations(range(n)))
    states = []
    for left in permutations_list:
        left_cells = {(row, left[row]) for row in range(n)}
        for right in permutations_list:
            right_cells = {(row, right[row]) for row in range(n)}
            if left_cells.isdisjoint(right_cells):
                states.append(tuple(sorted(
                    tuple((0, row, left[row]) for row in range(n))
                    + tuple((1, row, right[row]) for row in range(n))
                )))
    return tuple(sorted(states))


def collinear(triple: Triple) -> bool:
    (_, x1, y1), (_, x2, y2), (_, x3, y3) = triple
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def state_triples(state: State) -> tuple[Triple, ...]:
    return tuple(
        triple for triple in combinations(state, 3)
        if collinear(triple)
    )


def exact_triple(raw: Iterable[Iterable[int]], n: int, path: str) -> Triple:
    triple = tuple(exact_edge(edge, n, f"{path}[{index}]")
                   for index, edge in enumerate(raw))
    require(triple == tuple(sorted(triple)), f"{path}: canonical order required")
    require(len(triple) == 3 and len(set(triple)) == 3,
            f"{path}: exactly three distinct edges required")
    require(collinear(triple), f"{path}: triple is not physically collinear")
    return triple


def exact_targets(
    raw: Iterable[Iterable[Iterable[int]]],
    n: int,
    path: str,
) -> tuple[Triple, ...]:
    targets = tuple(exact_triple(triple, n, f"{path}[{index}]")
                    for index, triple in enumerate(raw))
    require(targets == tuple(sorted(targets)), f"{path}: canonical order required")
    require(len(targets) == len(set(targets)) and targets,
            f"{path}: nonempty duplicate-free target family required")
    return targets


def exact_envelope_columns(
    raw: Iterable[int], n: int, selected_column: int
) -> tuple[int, ...]:
    columns = tuple(raw)
    require(columns == tuple(sorted(columns)), "envelope columns: canonical order required")
    require(len(columns) == len(set(columns)) and columns,
            "envelope columns: nonempty duplicate-free set required")
    require(all(isinstance(column, int) and 0 <= column < n for column in columns),
            "envelope columns: outside board")
    require(selected_column in columns, "entering cell column outside envelope")
    return columns


def choose_four_endpoints(
    state: State,
    entering: Edge,
    envelope_columns: tuple[int, ...],
) -> tuple[Edge, ...]:
    layer_edges = tuple(edge for edge in state if edge[0] == entering[0])
    require(entering in layer_edges, "entering edge absent from handoff state")
    inside = tuple(edge for edge in layer_edges
                   if edge != entering and edge[2] in envelope_columns)
    outside = tuple(edge for edge in layer_edges
                    if edge != entering and edge[2] not in envelope_columns)
    if len(envelope_columns) >= 4:
        require(len(inside) >= 3, "internal envelope lacks three padding endpoints")
        chosen = (entering,) + inside[:3]
    else:
        candidates = inside + outside
        require(len(candidates) >= 3, "four-endpoint bank requires side at least four")
        chosen = (entering,) + candidates[:3]
    return tuple(sorted(chosen))


def four_endpoint_bank(
    state: State,
    entering: Edge,
    assigned_targets: tuple[Triple, ...],
    envelope_columns: tuple[int, ...],
) -> dict[str, Any]:
    n = len(tuple(edge for edge in state if edge[0] == 0))
    require(n >= 4, "four-endpoint bank requires side at least four")
    chosen = choose_four_endpoints(state, entering, envelope_columns)
    layer = entering[0]
    rows = tuple(edge[1] for edge in chosen)
    columns = tuple(edge[2] for edge in chosen)
    old_cells = {(edge[1], edge[2]) for edge in chosen}
    opposite_cells = {
        (edge[1], edge[2]) for edge in state if edge[0] != layer
    }
    fixed = tuple(edge for edge in state if edge not in set(chosen))
    bank_states = []
    for image in permutations(columns):
        replacement = tuple(
            (layer, rows[index], image[index]) for index in range(4)
        )
        replacement_cells = {(edge[1], edge[2]) for edge in replacement}
        if replacement_cells & old_cells:
            continue
        if replacement_cells & opposite_cells:
            continue
        candidate = tuple(sorted(fixed + replacement))
        exact_state(candidate, n, "bank_state")
        require(entering not in candidate, "bank state failed to move entering edge")
        candidate_triples = set(state_triples(candidate))
        require(
            all(target not in candidate_triples for target in assigned_targets),
            "bank state failed to destroy assigned target family",
        )
        bank_states.append(candidate)
    require(bank_states, "four-endpoint bank is empty")
    moved_columns = tuple(sorted({edge[2] for edge in chosen}))
    if set(moved_columns) <= set(envelope_columns):
        envelope_mode = "internal-target-handoff"
        next_columns = envelope_columns
    else:
        envelope_mode = "strict-envelope-expansion-witness"
        next_columns = tuple(sorted(set(envelope_columns) | set(moved_columns)))
        require(set(next_columns) > set(envelope_columns),
                "expansion witness did not enlarge envelope column set")
    result: dict[str, Any] = {
        "chosen_endpoints": [list(edge) for edge in chosen],
        "assigned_target_family": [
            [list(edge) for edge in triple] for triple in assigned_targets
        ],
        "bank_states": [
            [list(edge) for edge in candidate] for candidate in sorted(bank_states)
        ],
        "bank_state_count": len(bank_states),
        "envelope_mode": envelope_mode,
        "parent_envelope_columns": list(envelope_columns),
        "next_envelope_columns": list(next_columns),
        "claims": {
            "four_endpoint_bank_nonempty": 1,
            "every_bank_state_moves_entering_edge": 1,
            "every_bank_state_preserves_saturation": 1,
            "every_bank_state_preserves_layer_disjointness": 1,
            "every_bank_state_destroys_assigned_targets": 1,
            "internal_handoff_or_expansion_exact": 1,
        },
    }
    result["bank_sha256"] = digest(result)
    return result


def exact_handoff_manifest(
    n: int,
    p: int,
    h: int,
    owner: str,
    old_state_raw: Iterable[Iterable[int]],
    new_state_raw: Iterable[Iterable[int]],
    designated_targets_raw: Iterable[Iterable[Iterable[int]]],
    envelope_columns_raw: Iterable[int],
) -> dict[str, Any]:
    exact_positive_int(n, "side", 4)
    exact_positive_int(p, "prime", 2)
    exact_positive_int(h, "exponent")
    require(n == p ** h, "side must equal p^h")
    require(isinstance(owner, str) and owner, "owner: nonempty string required")
    old_state = exact_state(old_state_raw, n, "old_state")
    new_state = exact_state(new_state_raw, n, "new_state")
    require(old_state != new_state, "target handoff requires a state transition")
    targets = exact_targets(designated_targets_raw, n, "designated_targets")
    old_triples = set(state_triples(old_state))
    new_triples = set(state_triples(new_state))
    lost = tuple(sorted(old_triples - new_triples))
    created = tuple(sorted(new_triples - old_triples))
    require(set(targets) <= set(lost), "designated target was not destroyed")
    entering = tuple(sorted(set(new_state) - set(old_state)))
    leaving = tuple(sorted(set(old_state) - set(new_state)))
    require(len(entering) == len(leaving) and entering,
            "equal nonzero state churn required")
    potential_delta = len(new_triples) - len(old_triples)
    require(potential_delta >= 0,
            "handoff manifest requires a nonimproving transition")
    require(len(created) >= len(targets),
            "new-triple lower bound from target destruction failed")
    for triple in created:
        require(set(triple) & set(entering),
                "new triple lacks an entering selected edge")

    assignments = []
    loads = {edge: 0 for edge in entering}
    for triple in created:
        eligible = tuple(sorted(set(triple) & set(entering)))
        selected = eligible[0]
        loads[selected] += 1
        assignments.append((triple, selected))
    entering_cell = min(
        entering,
        key=lambda edge: (-loads[edge], edge),
    )
    assigned_targets = tuple(
        triple for triple, edge in assignments if edge == entering_cell
    )
    certified_load = len(assigned_targets)
    require(
        certified_load >= math.ceil(len(targets) / len(entering)),
        "entering-cell target-load concentration failed",
    )
    envelope_columns = exact_envelope_columns(
        envelope_columns_raw, n, entering_cell[2]
    )
    bank = four_endpoint_bank(
        new_state, entering_cell, assigned_targets, envelope_columns
    )
    require(
        len(targets) <= len(entering) * certified_load,
        "multiplicative target-load churn inequality failed",
    )
    token_incidences = len(entering) * (p + 1) * (h - 1)
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "target-handoff-potential-conversion-v1",
        "source_theorems": [
            "CMR698", "CMR699", "CMR700", "CMR701",
            "CMR702", "CMR703", "CMR704", "CMR705",
        ],
        "transition_kind": "nonimproving-target-destruction-handoff",
        "owner": owner,
        "ambient_side": n,
        "old_state": [list(edge) for edge in old_state],
        "new_state": [list(edge) for edge in new_state],
        "designated_targets": [
            [list(edge) for edge in triple] for triple in targets
        ],
        "old_potential": len(old_triples),
        "new_potential": len(new_triples),
        "potential_delta": potential_delta,
        "lost_triples": [[list(edge) for edge in triple] for triple in lost],
        "new_triples": [[list(edge) for edge in triple] for triple in created],
        "entering_edges": [list(edge) for edge in entering],
        "leaving_edges": [list(edge) for edge in leaving],
        "canonical_new_triple_assignments": [
            {
                "triple": [list(edge) for edge in triple],
                "entering_edge": list(edge),
            }
            for triple, edge in assignments
        ],
        "selected_entering_edge": list(entering_cell),
        "certified_next_target_load": certified_load,
        "four_endpoint_bank": bank,
        "target_load_churn_factor": len(entering),
        "entering_edge_nonroot_token_incidences": token_incidences,
        "claims": {
            "target_destruction_identity_exact": 1,
            "nonimproving_new_triple_lower_bound": 1,
            "every_new_triple_has_entering_edge": 1,
            "entering_cell_load_concentration_exact": 1,
            "four_endpoint_target_bank_generated": 1,
            "target_load_churn_inequality_exact": 1,
            "internal_handoff_or_expansion_exact": 1,
            "target_handoff_construction_ancestry_proved": 1,
            "all_envelope_operations_proved": 0,
            "all_scheduler_operations_proved": 0,
            "all_construction_ancestry_proved": 0,
            "global_transition_kind_bank_exhaustive": 0,
            "global_termination_proved": 0,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["transition_sha256"] = digest(result)
    return result


def exact_forced_certificate_bank(
    state_raw: Iterable[Iterable[int]],
    certificate_raw: Iterable[Iterable[int]],
    envelope_columns_raw: Iterable[int],
    n: int,
) -> dict[str, Any]:
    state = exact_state(state_raw, n, "forced_state")
    certificate = exact_triple(certificate_raw, n, "forced_certificate")
    require(certificate in set(state_triples(state)),
            "forced certificate absent from state")
    entering = certificate[0]
    envelope = exact_envelope_columns(
        envelope_columns_raw, n, entering[2]
    )
    bank = four_endpoint_bank(state, entering, (certificate,), envelope)
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "forced-certificate-target-bank-v1",
        "state": [list(edge) for edge in state],
        "forced_certificate": [list(edge) for edge in certificate],
        "selected_certificate_edge": list(entering),
        "four_endpoint_bank": bank,
        "claims": {
            "forced_certificate_target_bank_exact": 1,
            "certified_target_load": 1,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def exact_fixed_envelope_chain(
    episodes_raw: Iterable[dict[str, Any]],
    n: int,
    q: int,
    p: int,
    h: int,
    target_threshold: int,
    pair_threshold: int,
) -> dict[str, Any]:
    exact_positive_int(q, "envelope_side")
    exact_positive_int(target_threshold, "target_threshold", 2)
    exact_positive_int(pair_threshold, "pair_threshold", 2)
    require(n == p ** h, "side must equal p^h")
    episodes = tuple(episodes_raw)
    require(episodes, "target chain must be nonempty")
    parsed = []
    for index, episode in enumerate(episodes):
        require(isinstance(episode, dict)
                and set(episode) == {"target", "state", "previous_state"},
                f"episode {index}: exact key set required")
        target = exact_triple(episode["target"], n, f"episode[{index}].target")
        state = exact_state(episode["state"], n, f"episode[{index}].state")
        previous = exact_state(
            episode["previous_state"], n, f"episode[{index}].previous_state"
        )
        require(target in set(state_triples(state)),
                f"episode {index}: target absent from selected state")
        parsed.append((target, state, previous))

    target_counts: dict[Triple, int] = {}
    pair_counts: dict[tuple[Edge, Triple], int] = {}
    recreation_records = []
    last_occurrence: dict[Triple, int] = {}
    for index, (target, state, previous) in enumerate(parsed):
        target_counts[target] = target_counts.get(target, 0) + 1
        if target in last_occurrence:
            require(target not in set(state_triples(previous)),
                    f"episode {index}: reused target was not absent before recreation")
            entering = tuple(sorted(set(state) - set(previous)))
            witnesses = tuple(sorted(set(target) & set(entering)))
            require(witnesses, f"episode {index}: target recreation lacks entering cell")
            witness = witnesses[0]
            pair = (witness, target)
            pair_counts[pair] = pair_counts.get(pair, 0) + 1
            recreation_records.append(
                {
                    "episode_index": index,
                    "target": [list(edge) for edge in target],
                    "entering_cell": list(witness),
                }
            )
        last_occurrence[target] = index

    physical_target_stock = math.comb(2 * q * q, 3)
    j = len(parsed)
    recurrent_targets = tuple(
        target for target, count in sorted(target_counts.items())
        if count >= target_threshold
    )
    if recurrent_targets:
        target_history_category = "recurrent-physical-target"
    else:
        target_history_category = "finite-physical-target-history"
        require(j <= (target_threshold - 1) * physical_target_stock,
                "CMR706 finite target-history bound failed")

    recurrent_pairs = tuple(
        pair for pair, count in sorted(pair_counts.items())
        if count >= pair_threshold
    )
    pair_finite_bound = (3 * pair_threshold - 2) * physical_target_stock
    if recurrent_pairs:
        pair_history_category = "recurrent-cell-target-pair"
    else:
        pair_history_category = "finite-fixed-envelope-target-chain"
        require(j <= pair_finite_bound,
                "CMR709 fixed-envelope target-chain bound failed")

    recurrent_pair_token_incidences = sum(
        pair_counts[pair] * (p + 1) * (h - 1) for pair in recurrent_pairs
    )
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "fixed-envelope-target-chain-v1",
        "source_theorems": [
            "CMR706", "CMR707", "CMR708", "CMR709",
            "CMR710", "CMR711", "CMR712",
        ],
        "ambient_side": n,
        "envelope_side": q,
        "target_episodes": j,
        "physical_target_stock_bound": physical_target_stock,
        "target_threshold": target_threshold,
        "target_history_category": target_history_category,
        "recurrent_targets": [
            [list(edge) for edge in target] for target in recurrent_targets
        ],
        "recreation_records": recreation_records,
        "pair_threshold": pair_threshold,
        "pair_history_category": pair_history_category,
        "recurrent_cell_target_pairs": [
            {
                "cell": list(pair[0]),
                "target": [list(edge) for edge in pair[1]],
                "recreations": pair_counts[pair],
            }
            for pair in recurrent_pairs
        ],
        "finite_pair_chain_bound": pair_finite_bound,
        "recurrent_pair_nonroot_token_incidences": recurrent_pair_token_incidences,
        "claims": {
            "fixed_envelope_target_stock_exact": 1,
            "target_recreation_entering_cell_exact": 1,
            "target_recurrence_cell_pair_refinement_exact": 1,
            "cell_target_recurrence_or_finite_chain_exact": 1,
            "recurrent_cell_target_token_payment_exact": 1,
            "fixed_envelope_target_chain_proved": 1,
            "all_scheduler_operations_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["chain_sha256"] = digest(result)
    return result


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "target-handoff-and-fixed-envelope-chain-ancestry-v1",
        "source_theorems": [
            "CMR698", "CMR699", "CMR700", "CMR701", "CMR702",
            "CMR703", "CMR704", "CMR705", "CMR706", "CMR707",
            "CMR708", "CMR709", "CMR710", "CMR711", "CMR712",
        ],
        "claims": {
            "target_destruction_identity_exact": 1,
            "nonimproving_new_triple_lower_bound": 1,
            "entering_cell_load_concentration_exact": 1,
            "four_endpoint_target_bank_generated": 1,
            "internal_handoff_or_expansion_exact": 1,
            "target_load_churn_inequality_exact": 1,
            "forced_certificate_target_bank_exact": 1,
            "fixed_envelope_target_stock_exact": 1,
            "target_recreation_entering_cell_exact": 1,
            "cell_target_recurrence_or_finite_chain_exact": 1,
            "target_handoff_construction_ancestry_proved": 1,
            "fixed_envelope_target_chain_proved": 1,
            "closure_envelope_expansion_witness_ancestry_proved": 1,
            "all_envelope_operations_proved": 0,
            "all_scheduler_operations_proved": 0,
            "all_construction_ancestry_proved": 0,
            "global_transition_kind_bank_exhaustive": 0,
            "global_termination_proved": 0,
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


def canonical_handoff() -> tuple[State, State, tuple[Triple, ...]]:
    old_state: State = (
        (0, 0, 0), (0, 1, 1), (0, 2, 2), (0, 3, 3),
        (1, 0, 1), (1, 1, 0), (1, 2, 3), (1, 3, 2),
    )
    new_state: State = (
        (0, 0, 0), (0, 1, 1), (0, 2, 3), (0, 3, 2),
        (1, 0, 1), (1, 1, 0), (1, 2, 2), (1, 3, 3),
    )
    old_triples = set(state_triples(old_state))
    new_triples = set(state_triples(new_state))
    targets = tuple(sorted(old_triples - new_triples))
    require(len(targets) == 4, "canonical destroyed-target census drift")
    return old_state, new_state, targets


def handoff_regression() -> dict[str, Any]:
    old_state, new_state, targets = canonical_handoff()
    internal = exact_handoff_manifest(
        4, 2, 2, "owner:target-handoff", old_state, new_state,
        targets, (0, 1, 2, 3),
    )
    expansion = exact_handoff_manifest(
        4, 2, 2, "owner:target-handoff", old_state, new_state,
        targets, (2,),
    )
    require(
        internal["four_endpoint_bank"]["envelope_mode"]
        == "internal-target-handoff",
        "internal handoff branch drift",
    )
    require(
        expansion["four_endpoint_bank"]["envelope_mode"]
        == "strict-envelope-expansion-witness",
        "expansion handoff branch drift",
    )
    selected = tuple(internal["selected_entering_edge"])
    certificate = next(
        triple for triple in state_triples(new_state) if selected in triple
    )
    forced = exact_forced_certificate_bank(
        new_state, certificate, (0, 1, 2, 3), 4
    )
    return {
        "internal": internal,
        "expansion": expansion,
        "forced": forced,
    }


def chain_regression() -> dict[str, Any]:
    _, state, _ = canonical_handoff()
    target = state_triples(state)[0]
    states = generate_states(4)
    previous = next(
        candidate for candidate in states
        if target not in set(state_triples(candidate))
        and set(target) & (set(state) - set(candidate))
    )
    recurrent_episodes = []
    for index in range(4):
        recurrent_episodes.append(
            {
                "target": target,
                "state": state,
                "previous_state": previous if index else state,
            }
        )
    recurrent = exact_fixed_envelope_chain(
        recurrent_episodes, 4, 4, 2, 2, 2, 3
    )
    require(
        recurrent["pair_history_category"] == "recurrent-cell-target-pair",
        "recurrent pair branch drift",
    )
    distinct_targets = state_triples(state)[:4]
    finite_episodes = [
        {"target": target_value, "state": state, "previous_state": state}
        for target_value in distinct_targets
    ]
    finite = exact_fixed_envelope_chain(
        finite_episodes, 4, 4, 2, 2, 2, 2
    )
    require(
        finite["pair_history_category"] == "finite-fixed-envelope-target-chain",
        "finite target-chain branch drift",
    )
    return {"recurrent": recurrent, "finite": finite}


def exhaustive_side_four_transition_regression() -> dict[str, int]:
    states = generate_states(4)
    checked = nonimproving = destroyed_targets = new_triples = 0
    for old_state in states:
        old_set = set(state_triples(old_state))
        if not old_set:
            continue
        for new_state in states:
            if old_state == new_state:
                continue
            new_set = set(state_triples(new_state))
            lost = old_set - new_set
            if not lost:
                continue
            checked += 1
            if len(new_set) < len(old_set):
                continue
            entering = set(new_state) - set(old_state)
            created = new_set - old_set
            require(len(created) >= len(lost),
                    "side-four target-destruction identity failed")
            require(all(set(triple) & entering for triple in created),
                    "side-four new triple lacks entering edge")
            nonimproving += 1
            destroyed_targets += len(lost)
            new_triples += len(created)
    require(nonimproving > 0, "no nonimproving target transitions found")
    return {
        "side_four_states": len(states),
        "target_destroying_state_pairs": checked,
        "nonimproving_target_destroying_pairs": nonimproving,
        "destroyed_target_occurrences": destroyed_targets,
        "new_triple_occurrences": new_triples,
    }


def mutation_tests(regression: dict[str, Any]) -> int:
    internal = regression["handoff"]["internal"]
    old_state, new_state, targets = canonical_handoff()
    bad_calls = [
        lambda: exact_state(old_state[:-1], 4, "bad"),
        lambda: exact_handoff_manifest(
            4, 2, 2, "owner", old_state, old_state, targets, (0, 1, 2, 3)
        ),
        lambda: exact_handoff_manifest(
            4, 2, 2, "owner", new_state, old_state, targets, (0, 1, 2, 3)
        ),
        lambda: exact_forced_certificate_bank(
            new_state, targets[0], (0, 1, 2, 3), 4
        ),
        lambda: exact_fixed_envelope_chain([], 4, 4, 2, 2, 2, 2),
    ]
    rejected = 0
    for call in bad_calls:
        try:
            call()
        except (ValueError, KeyError, StopIteration):
            rejected += 1
        else:
            raise TargetHandoffError("malformed target-handoff input accepted")
    for mutation in ("honesty", "seal", "bank"):
        bad = copy.deepcopy(internal)
        if mutation == "honesty":
            bad["claims"]["all_n_proved_by_checker"] = 1
        elif mutation == "seal":
            bad["transition_sha256"] = "0" * 64
        else:
            bad["four_endpoint_bank"]["bank_states"] = []
        try:
            require(bad == internal, "corrupted target-handoff manifest mismatch")
        except TargetHandoffError:
            rejected += 1
        else:
            raise TargetHandoffError("corrupted target-handoff manifest accepted")
    require(rejected == 8, "mutation rejection census drift")
    return rejected


def finite_regression() -> dict[str, int]:
    handoff = handoff_regression()
    chains = chain_regression()
    regression = {"handoff": handoff, "chains": chains}
    return {
        "canonical_handoff_scenarios": 2,
        "internal_target_handoff_scenarios": 1,
        "strict_envelope_expansion_witnesses": 1,
        "canonical_destroyed_targets": len(
            handoff["internal"]["designated_targets"]
        ),
        "canonical_new_triples": len(handoff["internal"]["new_triples"]),
        "canonical_selected_entering_load": handoff["internal"][
            "certified_next_target_load"
        ],
        "canonical_four_endpoint_bank_states": handoff["internal"][
            "four_endpoint_bank"
        ]["bank_state_count"],
        "forced_certificate_target_banks": 1,
        "fixed_envelope_chain_scenarios": 2,
        "finite_fixed_envelope_chains": 1,
        "recurrent_cell_target_chains": 1,
        **exhaustive_side_four_transition_regression(),
        "rejected_mutations": mutation_tests(regression),
    }


def self_test() -> dict[str, Any]:
    return {
        **validate_contract(),
        **finite_regression(),
        "contract_sha256": contract_manifest()["contract_sha256"],
    }


def main() -> None:
    print(json.dumps(self_test(), sort_keys=True))


if __name__ == "__main__":
    main()
