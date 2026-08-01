#!/usr/bin/env python3
"""Verify CMR172--CMR175 and CMR193--CMR195 envelope transitions.

A closure branch carries the union of every moved column.  Its canonical owner
is the least lower-digit prime-power prefix block containing that history,
together with the two inherited layer row sets over the block.  A row-preserving
rematch whose columns stay inside the current block is an internal transition.
A move using any outside column is a strict expansion to an ancestor block and
decreases prefix depth.

The checker also generates a crossing-target four-endpoint witness: an outside
point of the target is moved, the target is destroyed, and the next envelope is
strictly larger.  This proves the complete internal-versus-expansion partition
for closure-branch rematches.  It does not prove every envelope use elsewhere in
the construction, the complete owner or scheduler bank, global termination, or
the all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations, permutations
from typing import Any, Iterable

Point = tuple[int, int, int]  # layer, column, row
Triple = tuple[Point, Point, Point]
State = tuple[tuple[int, ...], tuple[int, ...]]

EXPECTED_CONTRACT_SHA256 = "50b7720e03295dbde2557ab1d3a11dfc99a8f6d4a9528391555bc4e3adbf91c1"


class EnvelopeTransitionError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise EnvelopeTransitionError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_int(value: Any, path: str, minimum: int = 0) -> int:
    require(isinstance(value, int) and not isinstance(value, bool) and value >= minimum,
            f"{path}: integer at least {minimum} required")
    return value


def validate_prime_power(p: int, h: int, n: int) -> None:
    exact_int(p, "p", 2)
    exact_int(h, "h", 1)
    exact_int(n, "ambient_side", 2)
    require(n == p ** h, "ambient_side: exact p^h required")
    for q in range(2, int(p ** 0.5) + 1):
        require(p % q != 0, "p: prime required")


def canonical_state(raw: Iterable[Iterable[int]], n: int, path: str) -> State:
    layers = tuple(tuple(layer) for layer in raw)
    require(len(layers) == 2, f"{path}: two layers required")
    for i, layer in enumerate(layers):
        require(len(layer) == n, f"{path}[{i}]: full column domain required")
        require(all(isinstance(y, int) and not isinstance(y, bool) and 0 <= y < n
                    for y in layer), f"{path}[{i}]: row outside domain")
        require(set(layer) == set(range(n)), f"{path}[{i}]: permutation layer required")
    require(all(layers[0][x] != layers[1][x] for x in range(n)),
            f"{path}: layer collision")
    return layers  # type: ignore[return-value]


def canonical_columns(raw: Iterable[int], n: int, path: str, nonempty: bool = True) -> tuple[int, ...]:
    cols = tuple(raw)
    require(cols == tuple(sorted(cols)), f"{path}: canonical order required")
    require(len(cols) == len(set(cols)), f"{path}: duplicate column")
    if nonempty:
        require(cols, f"{path}: nonempty columns required")
    require(all(isinstance(x, int) and not isinstance(x, bool) and 0 <= x < n
                for x in cols), f"{path}: column outside ambient side")
    return cols


def envelope(p: int, h: int, history: tuple[int, ...]) -> dict[str, Any]:
    n = p ** h
    canonical_columns(history, n, "history")
    first = history[0]
    depth = 0
    for s in range(h + 1):
        modulus = p ** s
        if all(x % modulus == first % modulus for x in history):
            depth = s
        else:
            break
    modulus = p ** depth
    residue = first % modulus if modulus > 1 else 0
    block = tuple(x for x in range(n) if x % modulus == residue)
    payload = {
        "p": p,
        "h": h,
        "ambient_side": n,
        "depth": depth,
        "residue": residue,
        "columns": list(block),
        "block_side": len(block),
    }
    payload["envelope_sha256"] = digest(payload)
    return payload


def validate_envelope(raw: dict[str, Any], p: int, h: int,
                      history: tuple[int, ...], path: str) -> dict[str, Any]:
    expected = envelope(p, h, history)
    require(raw == expected, f"{path}: canonical envelope mismatch")
    return expected


def row_sets(state: State, columns: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return (
        tuple(sorted(state[0][x] for x in columns)),
        tuple(sorted(state[1][x] for x in columns)),
    )


def state_points(state: State) -> tuple[Point, ...]:
    n = len(state[0])
    return tuple((layer, x, state[layer][x]) for layer in (0, 1) for x in range(n))


def collinear_points(triple: Triple) -> bool:
    (_, x1, y1), (_, x2, y2), (_, x3, y3) = triple
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def canonical_target(raw: Iterable[Iterable[int]], state: State, path: str) -> Triple:
    points = tuple(tuple(point) for point in raw)
    require(len(points) == 3, f"{path}: three points required")
    require(points == tuple(sorted(points)), f"{path}: canonical order required")
    require(len(set(points)) == 3, f"{path}: distinct points required")
    n = len(state[0])
    for i, point in enumerate(points):
        require(len(point) == 3, f"{path}[{i}]: layer-column-row required")
        layer, column, row = point
        require(layer in (0, 1), f"{path}[{i}]: layer zero or one required")
        require(isinstance(column, int) and not isinstance(column, bool) and 0 <= column < n,
                f"{path}[{i}]: column outside state")
        require(isinstance(row, int) and not isinstance(row, bool) and 0 <= row < n,
                f"{path}[{i}]: row outside state")
        require(state[layer][column] == row, f"{path}[{i}]: point not selected")
    require(collinear_points(points), f"{path}: physical collinearity required")
    return points  # type: ignore[return-value]


def apply_move(state: State, layer: int, selected: tuple[int, ...],
               new_rows: tuple[int, ...]) -> State:
    require(layer in (0, 1), "move.layer: zero or one required")
    require(len(selected) == len(new_rows), "move: column/row length mismatch")
    old_rows = tuple(state[layer][x] for x in selected)
    require(tuple(sorted(new_rows)) == tuple(sorted(old_rows)),
            "move: selected row multiset not preserved")
    child = [list(state[0]), list(state[1])]
    for column, row in zip(selected, new_rows):
        child[layer][column] = row
    return canonical_state(child, len(state[0]), "child_state")


def move_record(p: int, h: int, initial: State, parent: State,
                parent_history: tuple[int, ...], layer: int,
                selected: tuple[int, ...], new_rows: tuple[int, ...],
                target: Triple | None = None, distinguished: Point | None = None) -> dict[str, Any]:
    parent_env = envelope(p, h, parent_history)
    child_history = tuple(sorted(set(parent_history).union(selected)))
    child_env = envelope(p, h, child_history)
    child = apply_move(parent, layer, selected, new_rows)
    internal = set(selected).issubset(parent_env["columns"])
    kind = "closure-envelope-internal-rematch" if internal else "closure-envelope-strict-expansion"
    parent_columns = tuple(parent_env["columns"])
    child_columns = tuple(child_env["columns"])
    parent_rows = row_sets(parent, parent_columns)
    child_rows = row_sets(child, child_columns)
    initial_parent_rows = row_sets(initial, parent_columns)
    initial_child_rows = row_sets(initial, child_columns)
    owner_parent = digest({
        "operation_owner": "closure-envelope-epoch",
        "envelope_sha256": parent_env["envelope_sha256"],
        "inherited_row_sets": parent_rows,
    })
    owner_child = digest({
        "operation_owner": "closure-envelope-epoch",
        "envelope_sha256": child_env["envelope_sha256"],
        "inherited_row_sets": child_rows,
    })
    record: dict[str, Any] = {
        "transition_kind": kind,
        "source_theorems": ["CMR172", "CMR173", "CMR174", "CMR175", "CMR193", "CMR194", "CMR195"],
        "p": p,
        "h": h,
        "initial_state": [list(initial[0]), list(initial[1])],
        "parent_state": [list(parent[0]), list(parent[1])],
        "child_state": [list(child[0]), list(child[1])],
        "parent_history": list(parent_history),
        "child_history": list(child_history),
        "move": {
            "layer": layer,
            "selected_columns": list(selected),
            "new_rows": list(new_rows),
        },
        "parent_envelope": parent_env,
        "child_envelope": child_env,
        "parent_owner": owner_parent,
        "child_owner": owner_child,
        "row_sets": {
            "parent_current": [list(parent_rows[0]), list(parent_rows[1])],
            "parent_initial": [list(initial_parent_rows[0]), list(initial_parent_rows[1])],
            "child_current": [list(child_rows[0]), list(child_rows[1])],
            "child_initial": [list(initial_child_rows[0]), list(initial_child_rows[1])],
        },
        "crossing_target": None,
    }
    if target is not None or distinguished is not None:
        require(target is not None and distinguished is not None,
                "crossing target and distinguished point must be supplied together")
        record["crossing_target"] = {
            "target": [list(point) for point in target],
            "distinguished_outside_point": list(distinguished),
        }
    record["seal_sha256"] = digest(record)
    return record


def validate_transition(raw: dict[str, Any]) -> dict[str, Any]:
    require(isinstance(raw, dict), "transition: object required")
    seal = raw.get("seal_sha256")
    require(isinstance(seal, str) and len(seal) == 64, "seal_sha256: digest required")
    unsealed = dict(raw)
    unsealed.pop("seal_sha256")
    require(digest(unsealed) == seal, "transition: seal mismatch")

    p = exact_int(raw.get("p"), "p", 2)
    h = exact_int(raw.get("h"), "h", 1)
    n = p ** h
    validate_prime_power(p, h, n)
    initial = canonical_state(raw.get("initial_state", []), n, "initial_state")
    parent = canonical_state(raw.get("parent_state", []), n, "parent_state")
    supplied_child = canonical_state(raw.get("child_state", []), n, "child_state")
    parent_history = canonical_columns(raw.get("parent_history", []), n, "parent_history")
    child_history = canonical_columns(raw.get("child_history", []), n, "child_history")
    parent_env = validate_envelope(raw.get("parent_envelope"), p, h, parent_history,
                                   "parent_envelope")
    move = raw.get("move")
    require(isinstance(move, dict), "move: object required")
    layer = exact_int(move.get("layer"), "move.layer", 0)
    require(layer in (0, 1), "move.layer: zero or one required")
    selected = canonical_columns(move.get("selected_columns", []), n,
                                 "move.selected_columns")
    new_rows = tuple(move.get("new_rows", []))
    require(all(isinstance(y, int) and not isinstance(y, bool) and 0 <= y < n
                for y in new_rows), "move.new_rows: rows outside domain")
    expected_child = apply_move(parent, layer, selected, new_rows)
    require(supplied_child == expected_child, "child_state: exact rematch mismatch")
    expected_history = tuple(sorted(set(parent_history).union(selected)))
    require(child_history == expected_history, "child_history: exact moved-column union required")
    child_env = validate_envelope(raw.get("child_envelope"), p, h, child_history,
                                  "child_envelope")

    parent_columns = tuple(parent_env["columns"])
    child_columns = tuple(child_env["columns"])
    parent_current_rows = row_sets(parent, parent_columns)
    parent_initial_rows = row_sets(initial, parent_columns)
    child_current_rows = row_sets(supplied_child, child_columns)
    child_initial_rows = row_sets(initial, child_columns)
    require(parent_current_rows == parent_initial_rows,
            "parent_state: inherited envelope row sets not preserved")
    require(child_current_rows == child_initial_rows,
            "child_state: inherited envelope row sets not preserved")
    expected_rows = {
        "parent_current": [list(parent_current_rows[0]), list(parent_current_rows[1])],
        "parent_initial": [list(parent_initial_rows[0]), list(parent_initial_rows[1])],
        "child_current": [list(child_current_rows[0]), list(child_current_rows[1])],
        "child_initial": [list(child_initial_rows[0]), list(child_initial_rows[1])],
    }
    require(raw.get("row_sets") == expected_rows, "row_sets: exact inheritance mismatch")

    internal = set(selected).issubset(parent_columns)
    expected_kind = ("closure-envelope-internal-rematch" if internal
                     else "closure-envelope-strict-expansion")
    require(raw.get("transition_kind") == expected_kind,
            "transition_kind: internal/expansion classification mismatch")
    if internal:
        require(child_env == parent_env, "internal move changed the envelope")
    else:
        require(child_env["depth"] < parent_env["depth"],
                "outside-column move did not strictly decrease depth")
        require(set(parent_columns).issubset(child_columns),
                "strict expansion did not move to an ancestor block")

    parent_owner = digest({
        "operation_owner": "closure-envelope-epoch",
        "envelope_sha256": parent_env["envelope_sha256"],
        "inherited_row_sets": parent_current_rows,
    })
    child_owner = digest({
        "operation_owner": "closure-envelope-epoch",
        "envelope_sha256": child_env["envelope_sha256"],
        "inherited_row_sets": child_current_rows,
    })
    require(raw.get("parent_owner") == parent_owner, "parent_owner: theorem-derived mismatch")
    require(raw.get("child_owner") == child_owner, "child_owner: theorem-derived mismatch")
    if internal:
        require(parent_owner == child_owner, "internal move changed envelope owner")
    else:
        require(parent_owner != child_owner, "strict expansion did not change envelope owner")

    require(raw.get("source_theorems") ==
            ["CMR172", "CMR173", "CMR174", "CMR175", "CMR193", "CMR194", "CMR195"],
            "source_theorems: ancestry mismatch")

    crossing = raw.get("crossing_target")
    if crossing is not None:
        require(not internal, "crossing target attached to internal transition")
        require(isinstance(crossing, dict), "crossing_target: object required")
        target = canonical_target(crossing.get("target", []), parent, "crossing_target.target")
        point_raw = tuple(crossing.get("distinguished_outside_point", []))
        require(len(point_raw) == 3, "distinguished_outside_point: point required")
        point = point_raw  # type: ignore[assignment]
        require(point in target, "distinguished_outside_point: not in target")
        point_layer, point_column, point_row = point
        require(point_column not in parent_columns,
                "distinguished_outside_point: column is not outside envelope")
        require(point_layer == layer and point_column in selected,
                "distinguished_outside_point: not moved by selected layer move")
        require(parent[layer][point_column] == point_row,
                "distinguished_outside_point: not selected in parent")
        require(supplied_child[layer][point_column] != point_row,
                "crossing target: outside point old cell was not removed")
        child_points = set(state_points(supplied_child))
        require(not set(target).issubset(child_points),
                "crossing target: target was not destroyed")

    return {
        "kind": expected_kind,
        "parent_depth": parent_env["depth"],
        "child_depth": child_env["depth"],
        "selected_columns": len(selected),
        "crossing_target": int(crossing is not None),
    }


def legal_rematches(state: State, layer: int, selected: tuple[int, ...],
                    move_all: bool = True) -> tuple[tuple[int, ...], ...]:
    old_rows = tuple(state[layer][x] for x in selected)
    opposite = state[1 - layer]
    result = []
    for new_rows in permutations(old_rows):
        if move_all and any(new_rows[i] == old_rows[i] for i in range(len(selected))):
            continue
        if any(new_rows[i] == opposite[selected[i]] for i in range(len(selected))):
            continue
        result.append(tuple(new_rows))
    return tuple(result)


def all_targets(state: State) -> tuple[Triple, ...]:
    points = state_points(state)
    return tuple(
        sorted(
            tuple(sorted(triple))  # type: ignore[arg-type]
            for triple in combinations(points, 3)
            if collinear_points(tuple(sorted(triple)))  # type: ignore[arg-type]
        )
    )


def find_depth_step(p: int, h: int, initial: State, parent: State,
                    history: tuple[int, ...]) -> dict[str, Any]:
    parent_env = envelope(p, h, history)
    n = p ** h
    target_depth = parent_env["depth"] - 1
    require(target_depth >= 0, "find_depth_step: parent already root")
    for layer in (0, 1):
        for selected in combinations(range(n), 2):
            if set(selected).issubset(parent_env["columns"]):
                continue
            child_history = tuple(sorted(set(history).union(selected)))
            if envelope(p, h, child_history)["depth"] != target_depth:
                continue
            for new_rows in legal_rematches(parent, layer, tuple(selected), move_all=True):
                record = move_record(p, h, initial, parent, history, layer,
                                     tuple(selected), new_rows)
                validate_transition(record)
                return record
    raise EnvelopeTransitionError("no exact one-depth expansion step found")


def crossing_target_record(p: int, h: int, initial: State, parent: State,
                           history: tuple[int, ...], target: Triple) -> dict[str, Any]:
    parent_env = envelope(p, h, history)
    outside = [point for point in target if point[1] not in parent_env["columns"]]
    require(outside, "target is not crossing")
    for distinguished in sorted(outside):
        layer, column, _ = distinguished
        others = [x for x in range(p ** h) if x != column]
        for padding in combinations(others, 3):
            selected = tuple(sorted((column, *padding)))
            for new_rows in legal_rematches(parent, layer, selected, move_all=True):
                record = move_record(p, h, initial, parent, history, layer,
                                     selected, new_rows, target, distinguished)
                validate_transition(record)
                return record
    raise EnvelopeTransitionError("crossing target has no four-endpoint witness")


def expect_rejection(record: dict[str, Any], mutator: Any) -> None:
    bad = copy.deepcopy(record)
    mutator(bad)
    try:
        validate_transition(bad)
    except EnvelopeTransitionError:
        return
    raise AssertionError("corrupted envelope transition was accepted")


def finite_regression() -> dict[str, int]:
    p, h, n = 2, 3, 8
    initial: State = (
        tuple(range(n)),
        tuple((x + 1) % n for x in range(n)),
    )
    canonical_state(initial, n, "initial")
    parent_history = (0, 2)
    parent_env = envelope(p, h, parent_history)
    require(parent_env["depth"] == 1 and parent_env["columns"] == [0, 2, 4, 6],
            "canonical even envelope mismatch")

    internal_count = 0
    expansion_count = 0
    selected_column_incidence = 0
    canonical_internal: dict[str, Any] | None = None
    canonical_expansion: dict[str, Any] | None = None
    for layer in (0, 1):
        for selected_raw in combinations(range(n), 4):
            selected = tuple(selected_raw)
            for new_rows in legal_rematches(initial, layer, selected, move_all=True):
                record = move_record(p, h, initial, initial, parent_history,
                                     layer, selected, new_rows)
                result = validate_transition(record)
                selected_column_incidence += result["selected_columns"]
                if result["kind"] == "closure-envelope-internal-rematch":
                    internal_count += 1
                    canonical_internal = canonical_internal or record
                else:
                    expansion_count += 1
                    canonical_expansion = canonical_expansion or record

    require(internal_count > 0 and expansion_count > 0,
            "finite regression: both envelope branches required")
    require(canonical_internal is not None and canonical_expansion is not None,
            "finite regression: canonical branch records missing")

    history = (0,)
    state = initial
    depths = [envelope(p, h, history)["depth"]]
    owner_chain = []
    for _ in range(h):
        record = find_depth_step(p, h, initial, state, history)
        result = validate_transition(record)
        owner_chain.append((record["parent_owner"], record["child_owner"]))
        state = canonical_state(record["child_state"], n, "chain.child_state")
        history = canonical_columns(record["child_history"], n, "chain.child_history")
        depths.append(result["child_depth"])
    require(depths == [3, 2, 1, 0], "finite regression: exact depth chain mismatch")
    require(all(a != b for a, b in owner_chain),
            "finite regression: expansion owner failed to change")

    targets = all_targets(initial)
    crossing_targets = tuple(
        target for target in targets
        if any(point[1] not in parent_env["columns"] for point in target)
    )
    crossing_witnesses = 0
    crossing_bank_state_incidence = 0
    canonical_crossing: dict[str, Any] | None = None
    for target in crossing_targets:
        record = crossing_target_record(p, h, initial, initial, parent_history, target)
        validate_transition(record)
        crossing_witnesses += 1
        crossing_bank_state_incidence += 1
        canonical_crossing = canonical_crossing or record
    require(crossing_targets and crossing_witnesses == len(crossing_targets),
            "finite regression: crossing-target witness census mismatch")
    require(canonical_crossing is not None, "finite regression: crossing record missing")

    rejection_count = 0
    mutations = [
        lambda r: r.__setitem__("transition_kind", "closure-envelope-internal-rematch"),
        lambda r: r["child_envelope"].__setitem__("depth", r["parent_envelope"]["depth"]),
        lambda r: r.__setitem__("child_history", r["parent_history"]),
        lambda r: r["move"].__setitem__("new_rows", r["move"]["new_rows"][::-1]),
        lambda r: r["row_sets"].__setitem__("child_current", [[], []]),
        lambda r: r.__setitem__("child_owner", r["parent_owner"]),
        lambda r: r["crossing_target"].__setitem__(
            "distinguished_outside_point", r["crossing_target"]["target"][0]),
        lambda r: r["parent_envelope"].__setitem__("envelope_sha256", "0" * 64),
        lambda r: r.__setitem__("source_theorems", ["CMR172"]),
        lambda r: r.__setitem__("seal_sha256", "0" * 64),
    ]
    for mutation in mutations:
        expect_rejection(canonical_crossing, mutation)
        rejection_count += 1

    return {
        "side_eight_internal_rematches": internal_count,
        "side_eight_strict_expansions": expansion_count,
        "selected_column_incidences": selected_column_incidence,
        "exact_depth_chain_transitions": h,
        "envelope_epoch_count": h + 1,
        "crossing_targets": len(crossing_targets),
        "crossing_target_expansion_witnesses": crossing_witnesses,
        "crossing_bank_state_incidences": crossing_bank_state_incidence,
        "rejected_corruptions": rejection_count,
    }


def main() -> None:
    contract = {
        "transition_kinds": [
            "closure-envelope-internal-rematch",
            "closure-envelope-strict-expansion",
        ],
        "sources": ["CMR172", "CMR173", "CMR174", "CMR175", "CMR193", "CMR194", "CMR195"],
        "fields": [
            "initial_state", "parent_state", "child_state", "parent_history",
            "child_history", "move", "parent_envelope", "child_envelope",
            "parent_owner", "child_owner", "row_sets", "crossing_target", "seal"
        ],
        "honesty": {
            "closure_branch_envelope_transition_bank_exhaustive": 1,
            "all_envelope_operations_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    require(digest(contract) == EXPECTED_CONTRACT_SHA256,
            "contract digest mismatch")
    census = finite_regression()
    report = {
        "checker": "prime-power-closure-envelope-transition-ancestry",
        "contract_sha256": EXPECTED_CONTRACT_SHA256,
        **census,
        "canonical_closure_envelope_identity_exact": 1,
        "envelope_row_set_invariance_exact": 1,
        "internal_envelope_transition_exact": 1,
        "strict_envelope_expansion_transition_exact": 1,
        "crossing_target_expansion_ancestry_proved": 1,
        "closure_envelope_depth_bound_exact": 1,
        "envelope_epoch_parent_assignment_exact": 1,
        "closure_branch_envelope_transition_bank_exhaustive": 1,
        "all_envelope_operations_proved": 0,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
