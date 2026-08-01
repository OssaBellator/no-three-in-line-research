#!/usr/bin/env python3
"""Verify CMR713--CMR719 recurrent-target entering-edge deletion ancestry.

The checker works with a literal one-layer balanced factor host.  A recurrent
target cell e is supplied by a transition from an avoiding perfect matching M
to a current perfect matching N, so e lies in N\\M.  The child host is exactly
the parent host with e deleted.  Complete family generation proves that M
survives, every active collinear target containing e disappears, and no
previously inactive target becomes active.

This installs the fixed-owner deletion response only.  It does not prove every
scheduler, owner, envelope, restoration or returned-edge operation, global
transition exhaustiveness, global termination, or the all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations, permutations
from math import comb, floor
from typing import Any, Iterable

Edge = tuple[int, int]
Matching = tuple[Edge, ...]
Triple = tuple[Edge, Edge, Edge]

EXPECTED_CONTRACT_SHA256 = "a7153947e5f44b8433e404050eb317fc17f5b380722c6c121b8a4d910140fad0"


class RecurrentTargetDeletionError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RecurrentTargetDeletionError(message)


def digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def exact_int(value: Any, path: str, minimum: int = 0) -> int:
    require(isinstance(value, int) and not isinstance(value, bool) and value >= minimum,
            f"{path}: integer at least {minimum} required")
    return value


def canonical_edge(raw: Iterable[int], n: int, path: str) -> Edge:
    edge = tuple(raw)
    require(len(edge) == 2, f"{path}: edge length two required")
    x, y = edge
    require(isinstance(x, int) and not isinstance(x, bool), f"{path}: integer column required")
    require(isinstance(y, int) and not isinstance(y, bool), f"{path}: integer row required")
    require(0 <= x < n and 0 <= y < n, f"{path}: edge outside host")
    return x, y


def canonical_deleted(raw: Iterable[Iterable[int]], n: int, path: str = "deleted_edges") -> tuple[Edge, ...]:
    edges = tuple(canonical_edge(edge, n, f"{path}[{i}]") for i, edge in enumerate(raw))
    require(edges == tuple(sorted(edges)), f"{path}: canonical order required")
    require(len(edges) == len(set(edges)), f"{path}: duplicate edge")
    return edges


def canonical_matching(raw: Iterable[Iterable[int]], n: int, deleted: tuple[Edge, ...],
                       path: str) -> Matching:
    matching = tuple(canonical_edge(edge, n, f"{path}[{i}]") for i, edge in enumerate(raw))
    require(matching == tuple(sorted(matching)), f"{path}: canonical order required")
    require(len(matching) == n, f"{path}: perfect matching size required")
    require({x for x, _ in matching} == set(range(n)), f"{path}: column saturation failed")
    require({y for _, y in matching} == set(range(n)), f"{path}: row saturation failed")
    require(set(matching).isdisjoint(deleted), f"{path}: deleted edge used")
    return matching


def collinear(triple: Triple) -> bool:
    (x1, y1), (x2, y2), (x3, y3) = triple
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def canonical_triple(raw: Iterable[Iterable[int]], n: int, path: str) -> Triple:
    triple = tuple(canonical_edge(edge, n, f"{path}[{i}]") for i, edge in enumerate(raw))
    require(len(triple) == 3, f"{path}: three edges required")
    require(triple == tuple(sorted(triple)), f"{path}: canonical order required")
    require(len(set(triple)) == 3, f"{path}: distinct edges required")
    require(collinear(triple), f"{path}: physical collinearity required")
    return triple  # type: ignore[return-value]


def matching_family(n: int, deleted: tuple[Edge, ...]) -> tuple[Matching, ...]:
    family: list[Matching] = []
    blocked = set(deleted)
    for perm in permutations(range(n)):
        matching = tuple((x, perm[x]) for x in range(n))
        if set(matching).isdisjoint(blocked):
            family.append(matching)
    return tuple(family)


def matching_triples(matching: Matching) -> tuple[Triple, ...]:
    return tuple(
        sorted(
            tuple(sorted(triple))  # type: ignore[arg-type]
            for triple in combinations(matching, 3)
            if collinear(tuple(sorted(triple)))  # type: ignore[arg-type]
        )
    )


def active_triples(family: tuple[Matching, ...]) -> tuple[Triple, ...]:
    triples: set[Triple] = set()
    for matching in family:
        triples.update(matching_triples(matching))
    return tuple(sorted(triples))


def context(n: int, deleted: tuple[Edge, ...]) -> dict[str, Any]:
    family = matching_family(n, deleted)
    triples = active_triples(family)
    payload = {
        "ambient_side": n,
        "row_domain": list(range(n)),
        "column_domain": list(range(n)),
        "deleted_edges": [list(edge) for edge in deleted],
        "feasible_state_count": len(family),
        "active_triple_count": len(triples),
        "family_sha256": digest(family),
        "active_triples_sha256": digest(triples),
    }
    payload["context_sha256"] = digest(payload)
    return payload


def validate_context(raw: dict[str, Any], path: str) -> tuple[int, tuple[Edge, ...], tuple[Matching, ...], tuple[Triple, ...]]:
    require(isinstance(raw, dict), f"{path}: object required")
    n = exact_int(raw.get("ambient_side"), f"{path}.ambient_side", 1)
    require(raw.get("row_domain") == list(range(n)), f"{path}.row_domain: full canonical domain required")
    require(raw.get("column_domain") == list(range(n)), f"{path}.column_domain: full canonical domain required")
    deleted = canonical_deleted(raw.get("deleted_edges", []), n, f"{path}.deleted_edges")
    family = matching_family(n, deleted)
    triples = active_triples(family)
    expected = context(n, deleted)
    require(raw == expected, f"{path}: generated context mismatch")
    return n, deleted, family, triples


def owner_label(ctx: dict[str, Any]) -> str:
    return digest({
        "operation_owner": "fixed-balanced-factor-host",
        "ambient_side": ctx["ambient_side"],
        "context_sha256": ctx["context_sha256"],
    })


def transition_record(n: int, deleted: tuple[Edge, ...], avoidance: Matching,
                      current: Matching, entering: Edge, target: Triple) -> dict[str, Any]:
    parent = context(n, deleted)
    child_deleted = tuple(sorted((*deleted, entering)))
    child = context(n, child_deleted)
    parent_family = matching_family(n, deleted)
    parent_active = active_triples(parent_family)
    star = tuple(triple for triple in parent_active if entering in triple)
    payload = {
        "source_theorems": ["CMR713", "CMR714", "CMR715", "CMR716", "CMR717", "CMR718", "CMR719"],
        "parent_family_sha256": parent["family_sha256"],
        "child_family_sha256": child["family_sha256"],
        "active_target_star_before": len(star),
        "active_target_star_after": 0,
        "deleted_edge_stock_before": n * n - len(deleted),
        "deleted_edge_stock_after": n * n - len(child_deleted),
    }
    record: dict[str, Any] = {
        "transition_kind": "recurrent-target-entering-edge-deletion",
        "owner": owner_label(parent),
        "parent_context": parent,
        "child_context": child,
        "avoidance_matching": [list(edge) for edge in avoidance],
        "current_matching": [list(edge) for edge in current],
        "entering_edge": list(entering),
        "target_triple": [list(edge) for edge in target],
        "target_star": [[list(edge) for edge in triple] for triple in star],
        "payload": payload,
    }
    record["seal_sha256"] = digest(record)
    return record


def validate_transition(raw: dict[str, Any]) -> dict[str, Any]:
    require(isinstance(raw, dict), "transition: object required")
    seal = raw.get("seal_sha256")
    require(isinstance(seal, str) and len(seal) == 64, "transition.seal_sha256: digest required")
    unsealed = dict(raw)
    unsealed.pop("seal_sha256")
    require(digest(unsealed) == seal, "transition: seal mismatch")
    require(raw.get("transition_kind") == "recurrent-target-entering-edge-deletion",
            "transition_kind: wrong operation")
    n, deleted, parent_family, parent_active = validate_context(raw.get("parent_context"), "parent_context")
    child_n, child_deleted, child_family, child_active = validate_context(raw.get("child_context"), "child_context")
    require(child_n == n, "child_context: ambient side changed")
    avoidance = canonical_matching(raw.get("avoidance_matching", []), n, deleted, "avoidance_matching")
    current = canonical_matching(raw.get("current_matching", []), n, deleted, "current_matching")
    entering = canonical_edge(raw.get("entering_edge", []), n, "entering_edge")
    target = canonical_triple(raw.get("target_triple", []), n, "target_triple")
    require(avoidance in parent_family, "avoidance_matching: not in parent family")
    require(current in parent_family, "current_matching: not in parent family")
    require(entering in current and entering not in avoidance,
            "entering_edge: must lie in current matching and be avoided by predecessor")
    require(set(target).issubset(current), "target_triple: not contained in current matching")
    require(entering in target, "target_triple: entering edge not distinguished")
    require(entering not in deleted, "entering_edge: already deleted")
    require(child_deleted == tuple(sorted((*deleted, entering))),
            "child_context: not the exact single-edge deletion")
    require(avoidance in child_family, "child_context: avoidance certificate did not survive")
    expected_child = tuple(matching for matching in parent_family if entering not in matching)
    require(child_family == expected_child, "child_context: exact family restriction failed")
    expected_star = tuple(triple for triple in parent_active if entering in triple)
    supplied_star = tuple(
        canonical_triple(triple, n, f"target_star[{i}]")
        for i, triple in enumerate(raw.get("target_star", []))
    )
    require(supplied_star == expected_star, "target_star: exact active star mismatch")
    require(all(entering not in triple for triple in child_active),
            "child_context: target star remains active")
    require(set(child_active).issubset(parent_active),
            "child_context: deletion activated a new target")
    require(target not in child_active, "child_context: selected target remains active")
    require(raw.get("owner") == owner_label(raw["parent_context"]),
            "owner: theorem-derived owner mismatch")
    payload = raw.get("payload")
    require(isinstance(payload, dict), "payload: object required")
    require(payload.get("source_theorems") ==
            ["CMR713", "CMR714", "CMR715", "CMR716", "CMR717", "CMR718", "CMR719"],
            "payload.source_theorems: ancestry mismatch")
    require(payload.get("parent_family_sha256") == raw["parent_context"]["family_sha256"],
            "payload.parent_family_sha256: mismatch")
    require(payload.get("child_family_sha256") == raw["child_context"]["family_sha256"],
            "payload.child_family_sha256: mismatch")
    require(payload.get("active_target_star_before") == len(expected_star),
            "payload.active_target_star_before: mismatch")
    require(payload.get("active_target_star_after") == 0,
            "payload.active_target_star_after: mismatch")
    require(payload.get("deleted_edge_stock_before") == n * n - len(deleted),
            "payload.deleted_edge_stock_before: mismatch")
    require(payload.get("deleted_edge_stock_after") == n * n - len(child_deleted),
            "payload.deleted_edge_stock_after: mismatch")
    require(payload["deleted_edge_stock_after"] + 1 == payload["deleted_edge_stock_before"],
            "payload: deletion stock did not fall by one")
    return {
        "ambient_side": n,
        "target_star_size": len(expected_star),
        "parent_states": len(parent_family),
        "child_states": len(child_family),
    }


def host_stage_count(m: int) -> int:
    return 2 * m * m + m + 1


def routing_change_bound(m: int, lam: int) -> int:
    return floor((lam - 1) * m * m / 2)


def owner_stage_stock(d: int, lam: int) -> int:
    exact_int(d, "d", 1)
    exact_int(lam, "lambda", 2)
    return sum(host_stage_count(m) * (1 + routing_change_bound(m, lam))
               for m in range(1, d + 1))


def owner_pair_stock(d: int, lam: int, ambient_side: int) -> int:
    exact_int(ambient_side, "ambient_side", 1)
    return 3 * owner_stage_stock(d, lam) * comb(ambient_side * ambient_side, 3)


def finite_or_recurrent_pair_history(episodes: list[str], stock: int, nu: int) -> dict[str, Any]:
    exact_int(stock, "stock", 1)
    exact_int(nu, "nu", 2)
    require(all(isinstance(label, str) and label for label in episodes),
            "episodes: nonempty string labels required")
    counts: dict[str, int] = {}
    for label in episodes:
        counts[label] = counts.get(label, 0) + 1
    recurrent = sorted(label for label, count in counts.items() if count >= nu)
    if recurrent:
        return {
            "endpoint": "recurrent-owner-cell-target-pair",
            "witness": recurrent[0],
            "multiplicity": counts[recurrent[0]],
        }
    bound = (nu - 1) * stock
    require(len(episodes) <= bound, "finite pair history exceeds stock bound")
    return {
        "endpoint": "finite-owner-cell-target-history",
        "episode_count": len(episodes),
        "bound": bound,
    }


def monotone_deletion_depth(n: int) -> int:
    deleted: tuple[Edge, ...] = ()
    steps = 0
    while True:
        family = matching_family(n, deleted)
        chosen: tuple[Matching, Matching, Edge] | None = None
        for current in family:
            for avoidance in family:
                for entering in current:
                    if entering not in avoidance:
                        chosen = current, avoidance, entering
                        break
                if chosen:
                    break
            if chosen:
                break
        if chosen is None:
            break
        _, avoidance, entering = chosen
        child_deleted = tuple(sorted((*deleted, entering)))
        require(avoidance in matching_family(n, child_deleted),
                "monotone deletion: avoidance matching lost")
        deleted = child_deleted
        steps += 1
        require(steps <= n * n, "monotone deletion exceeded physical edge stock")
    return steps


def expect_rejection(record: dict[str, Any], mutator: Any) -> None:
    bad = copy.deepcopy(record)
    mutator(bad)
    try:
        validate_transition(bad)
    except RecurrentTargetDeletionError:
        return
    raise AssertionError("corrupted transition was accepted")


def finite_regression() -> dict[str, int]:
    transition_count = 0
    target_star_incidence = 0
    parent_state_incidence = 0
    child_state_incidence = 0
    canonical_record: dict[str, Any] | None = None

    for n in (3, 4):
        deleted: tuple[Edge, ...] = ()
        family = matching_family(n, deleted)
        for current in family:
            for target in matching_triples(current):
                for avoidance in family:
                    for entering in target:
                        if entering in current and entering not in avoidance:
                            record = transition_record(n, deleted, avoidance, current, entering, target)
                            result = validate_transition(record)
                            transition_count += 1
                            target_star_incidence += result["target_star_size"]
                            parent_state_incidence += result["parent_states"]
                            child_state_incidence += result["child_states"]
                            canonical_record = canonical_record or record

    require(transition_count == 672, "finite regression: unexpected transition census")
    require(canonical_record is not None, "finite regression: no canonical record")

    deletion_depth_three = monotone_deletion_depth(3)
    deletion_depth_four = monotone_deletion_depth(4)
    require(0 < deletion_depth_three <= 9, "side-three deletion depth bound failed")
    require(0 < deletion_depth_four <= 16, "side-four deletion depth bound failed")

    stock = owner_pair_stock(3, 2, 4)
    finite_history = finite_or_recurrent_pair_history(
        [f"owner-pair-{i}" for i in range(12)], stock, 2
    )
    recurrent_history = finite_or_recurrent_pair_history(
        ["same-owner-pair", "same-owner-pair"], stock, 2
    )
    require(finite_history["endpoint"] == "finite-owner-cell-target-history",
            "finite owner-pair endpoint missing")
    require(recurrent_history["endpoint"] == "recurrent-owner-cell-target-pair",
            "recurrent owner-pair endpoint missing")

    rejection_count = 0
    mutations = [
        lambda r: r.__setitem__("entering_edge", r["avoidance_matching"][0]),
        lambda r: r.__setitem__("target_triple", [[0, 0], [1, 0], [2, 1]]),
        lambda r: r["child_context"].__setitem__("deleted_edges", []),
        lambda r: r.__setitem__("avoidance_matching", r["current_matching"]),
        lambda r: r["parent_context"].__setitem__("family_sha256", "0" * 64),
        lambda r: r.__setitem__("owner", "false-owner"),
        lambda r: r["payload"].__setitem__("active_target_star_after", 1),
        lambda r: r.__setitem__("seal_sha256", "0" * 64),
    ]
    for mutation in mutations:
        expect_rejection(canonical_record, mutation)
        rejection_count += 1

    return {
        "recurrent_target_deletion_transitions": transition_count,
        "target_star_incidences_destroyed": target_star_incidence,
        "parent_state_incidences": parent_state_incidence,
        "child_state_incidences": child_state_incidence,
        "side_three_monotone_deletions": deletion_depth_three,
        "side_four_monotone_deletions": deletion_depth_four,
        "owner_pair_stock_sample": stock,
        "finite_history_cases": 1,
        "recurrent_history_cases": 1,
        "rejected_corruptions": rejection_count,
    }


def main() -> None:
    contract = {
        "transition_kind": "recurrent-target-entering-edge-deletion",
        "sources": ["CMR713", "CMR714", "CMR715", "CMR716", "CMR717", "CMR718", "CMR719"],
        "fields": [
            "parent_context", "child_context", "avoidance_matching",
            "current_matching", "entering_edge", "target_triple",
            "target_star", "owner", "payload", "seal"
        ],
        "honesty": {
            "all_scheduler_operations_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    require(digest(contract) == EXPECTED_CONTRACT_SHA256,
            "contract digest mismatch")
    census = finite_regression()
    report = {
        "checker": "prime-power-recurrent-target-edge-deletion-ancestry",
        "contract_sha256": EXPECTED_CONTRACT_SHA256,
        **census,
        "entering_edge_nonessentiality_exact": 1,
        "recurrent_target_star_deactivation_exact": 1,
        "deletion_cannot_activate_target_exact": 1,
        "recurrent_target_edge_deletion_ancestry_proved": 1,
        "owner_labelled_cell_target_stock_exact": 1,
        "recurrent_target_deletion_depth_exact": 1,
        "recurrent_pair_return_requires_reintroduction_or_owner_change": 1,
        "all_scheduler_operations_proved": 0,
        "all_owner_operations_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
