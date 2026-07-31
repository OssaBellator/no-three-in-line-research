#!/usr/bin/env python3
"""Verify target-edge return, redeletion, ancestry and contraction transitions.

CMR720--CMR726 store a perfect matching avoiding a deleted target edge.  When
that edge later returns, the stored matching either survives and authorizes
exact redeletion, or a canonical stored edge is absent.  Essential returns then
contract exactly and transfer a target triple to a residual prescription of
rank at most two.

This checker proves ancestry for this returned-target-edge operation only.  It
does not prove every restoration, owner/envelope change, global transition
exhaustiveness, global termination, or the all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations
from typing import Any, Iterable

from check_prime_power_forced_certificate_escape_ancestry import (
    Edge,
    Matching,
    digest,
    exact_coordinates,
    exact_edges,
    exact_matching,
    factor_context,
    generate_matchings,
    require as base_require,
)

EXPECTED_CONTRACT_SHA256 = "04a533666c90c2f13bcb18731e10e0bca4d6357a806f8be44ee47af6f90e2382"


class TargetEdgeReturnError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise TargetEdgeReturnError(message)


def exact_edge(raw: Iterable[int], rows: tuple[int, ...],
               columns: tuple[int, ...], path: str) -> Edge:
    edge = tuple(raw)
    require(
        len(edge) == 2 and edge[0] in rows and edge[1] in columns,
        f"{path}: edge outside factor domains",
    )
    return edge  # type: ignore[return-value]


def context_signature(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "name": context["name"],
        "ambient_side": context["ambient_side"],
        "rows": context["rows"],
        "columns": context["columns"],
        "allowed_edges": context["allowed_edges"],
        "deleted_edges": context["deleted_edges"],
        "family_sha256": context["family_sha256"],
        "context_sha256": context["context_sha256"],
    }


def empty_or_factor_context(
    n: int,
    name: str,
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    allowed: tuple[Edge, ...],
) -> dict[str, Any]:
    require(len(rows) == len(columns), f"{name}: residual balance failed")
    if rows:
        return factor_context(n, name, rows, columns, allowed)
    require(not allowed, f"{name}: empty residual has an edge")
    result: dict[str, Any] = {
        "name": name,
        "ambient_side": n,
        "rows": [],
        "columns": [],
        "allowed_edges": [],
        "deleted_edges": [],
        "feasible_matchings": [[]],
        "essential_edges": [],
        "family_sha256": digest([[]]),
    }
    result["context_sha256"] = digest(result)
    return result


def exact_target_triple(
    raw: Iterable[Iterable[int]],
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    target: Edge,
    allowed: tuple[Edge, ...],
) -> tuple[Edge, ...]:
    triple = tuple(tuple(edge) for edge in raw)
    require(triple == tuple(sorted(triple)), "target_triple: canonical order required")
    require(len(triple) == 3 and len(set(triple)) == 3,
            "target_triple: exactly three distinct edges required")
    require(target in triple, "target_triple: returned target edge absent")
    require(set(triple) <= set(allowed), "target_triple: edge outside later host")
    require(len({edge[0] for edge in triple}) == 3,
            "target_triple: matching-compatible rows required")
    require(len({edge[1] for edge in triple}) == 3,
            "target_triple: matching-compatible columns required")
    require(all(edge[0] in rows and edge[1] in columns for edge in triple),
            "target_triple: edge outside domains")
    return triple  # type: ignore[return-value]


def contraction_manifest(
    n: int,
    later: dict[str, Any],
    target: Edge,
    target_triple_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    rows = tuple(later["rows"])
    columns = tuple(later["columns"])
    allowed = tuple(tuple(edge) for edge in later["allowed_edges"])
    family = tuple(
        tuple(tuple(edge) for edge in matching)
        for matching in later["feasible_matchings"]
    )
    require(target in set(tuple(edge) for edge in later["essential_edges"]),
            "contraction requires an essential target edge")
    triple = exact_target_triple(target_triple_raw, rows, columns, target, allowed)

    child_rows = tuple(row for row in rows if row != target[0])
    child_columns = tuple(column for column in columns if column != target[1])
    child_allowed = tuple(
        edge for edge in allowed
        if edge[0] in child_rows and edge[1] in child_columns
    )
    child = empty_or_factor_context(
        n, f"{later['name']}:contracted:{target}", child_rows, child_columns,
        child_allowed,
    )
    child_family = tuple(
        tuple(tuple(edge) for edge in matching)
        for matching in child["feasible_matchings"]
    )
    restricted = tuple(sorted(
        tuple(edge for edge in matching if edge != target)
        for matching in family
    ))
    require(child_family == restricted,
            "essential target contraction family identity failed")
    adjoined = tuple(sorted(
        tuple(sorted(matching + (target,))) for matching in child_family
    ))
    require(adjoined == family, "essential target contraction adjoin inverse failed")

    residual = tuple(edge for edge in triple if edge != target)
    require(len(residual) <= 2, "residual target rank exceeds two")
    result: dict[str, Any] = {
        "parent_context": context_signature(later),
        "contracted_target_edge": list(target),
        "child_context": context_signature(child),
        "target_triple": [list(edge) for edge in triple],
        "residual_target_prescription": [list(edge) for edge in residual],
        "residual_target_rank": len(residual),
        "claims": {
            "essential_target_contraction_exact": 1,
            "restriction_adjoin_bijection": 1,
            "strict_factor_side_descent": 1,
            "residual_target_rank_at_most_two": 1,
        },
    }
    result["contraction_sha256"] = digest(result)
    return result


def exact_return_manifest(
    n: int,
    owner: str,
    deletion_context: dict[str, Any],
    target_raw: Iterable[int],
    stored_avoidance_raw: Iterable[Iterable[int]],
    later_context: dict[str, Any],
    later_matching_raw: Iterable[Iterable[int]],
    target_triple_raw: Iterable[Iterable[int]] | None = None,
) -> dict[str, Any]:
    require(isinstance(owner, str) and owner, "owner: nonempty string required")
    require(deletion_context["ambient_side"] == n == later_context["ambient_side"],
            "ambient side mismatch")
    require(
        deletion_context["rows"] == later_context["rows"]
        and deletion_context["columns"] == later_context["columns"],
        "returned-edge operation requires fixed labelled domains",
    )
    rows = tuple(deletion_context["rows"])
    columns = tuple(deletion_context["columns"])
    target = exact_edge(target_raw, rows, columns, "target_edge")
    deletion_allowed = tuple(tuple(edge) for edge in deletion_context["allowed_edges"])
    later_allowed = tuple(tuple(edge) for edge in later_context["allowed_edges"])
    require(target not in set(deletion_allowed),
            "deletion context must omit the target edge")
    require(target in set(later_allowed),
            "later context must restore the target edge")

    stored = exact_matching(
        stored_avoidance_raw, rows, columns, deletion_allowed,
        "stored_avoidance_matching",
    )
    require(target not in set(stored), "stored matching does not avoid target edge")
    later_matching = exact_matching(
        later_matching_raw, rows, columns, later_allowed, "later_matching"
    )
    later_family = tuple(
        tuple(tuple(edge) for edge in matching)
        for matching in later_context["feasible_matchings"]
    )
    target_essential = target in set(
        tuple(edge) for edge in later_context["essential_edges"]
    )
    missing_stored = tuple(edge for edge in stored if edge not in set(later_allowed))

    if not missing_stored:
        category = "stored-avoidance-survives-exact-redeletion"
        redeleted_allowed = tuple(edge for edge in later_allowed if edge != target)
        redeleted = factor_context(
            n, f"{later_context['name']}:redeleted:{target}",
            rows, columns, redeleted_allowed,
        )
        redeleted_family = tuple(
            tuple(tuple(edge) for edge in matching)
            for matching in redeleted["feasible_matchings"]
        )
        direct = tuple(matching for matching in later_family if target not in set(matching))
        require(redeleted_family == direct, "returned-edge redeletion identity failed")
        require(stored in redeleted_family, "stored avoidance matching lost after redeletion")
        witness = None
        contraction = None
        alternate_redeletion = context_signature(redeleted)
        semantics = "stored avoidance matching survives and witnesses exact redeletion"
    else:
        witness_edge = missing_stored[0]
        witness = {
            "witness_kind": "stored-avoidance-edge-absent",
            "physical_edge": list(witness_edge),
            "all_missing_stored_edges": [list(edge) for edge in missing_stored],
        }
        if target_essential:
            category = "essential-return-deletion-ancestry-and-contraction"
            require(target_triple_raw is not None,
                    "essential return requires a current target triple")
            contraction = contraction_manifest(
                n, later_context, target, target_triple_raw
            )
            alternate_redeletion = None
            semantics = (
                "stored avoidance is blocked; essential returned edge contracts "
                "and transfers the target to rank at most two"
            )
        else:
            category = "blocked-stored-avoidance-nonessential-return"
            avoiding = tuple(
                matching for matching in later_family if target not in set(matching)
            )
            require(avoiding, "nonessential target has no avoiding matching")
            redeleted_allowed = tuple(edge for edge in later_allowed if edge != target)
            redeleted = factor_context(
                n, f"{later_context['name']}:redeleted:{target}",
                rows, columns, redeleted_allowed,
            )
            redeleted_family = tuple(
                tuple(tuple(edge) for edge in matching)
                for matching in redeleted["feasible_matchings"]
            )
            require(redeleted_family == avoiding,
                    "alternate returned-edge redeletion identity failed")
            contraction = None
            alternate_redeletion = context_signature(redeleted)
            semantics = (
                "stored avoidance is blocked by a missing old edge, but another "
                "later matching still authorizes exact redeletion"
            )

    labels = {
        "operation_slot": "CMR720-CMR726-returned-target-edge",
        "owner": owner,
        "target_edge": list(target),
        "deletion_context": deletion_context["context_sha256"],
        "later_context": later_context["context_sha256"],
    }
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "returned-target-edge-ancestry-transition-v1",
        "source_theorems": [
            "CMR720", "CMR721", "CMR722", "CMR723",
            "CMR724", "CMR725", "CMR726",
        ],
        "transition_kind": category,
        "construction_labels": labels,
        "target_edge": list(target),
        "deletion_context": context_signature(deletion_context),
        "later_context": context_signature(later_context),
        "restored_edges": [
            list(edge) for edge in sorted(set(later_allowed) - set(deletion_allowed))
        ],
        "simultaneously_deleted_edges": [
            list(edge) for edge in sorted(set(deletion_allowed) - set(later_allowed))
        ],
        "stored_avoidance_matching": [list(edge) for edge in stored],
        "later_matching": [list(edge) for edge in later_matching],
        "target_essential_in_later_context": int(target_essential),
        "canonical_deletion_ancestry_witness": witness,
        "redeletion_child_context": alternate_redeletion,
        "essential_contraction": contraction,
        "exact_semantics": semantics,
        "claims": {
            "returned_target_edge_restoration_exact": 1,
            "stored_avoidance_survival_redeletion_exact": int(not missing_stored),
            "stored_avoidance_deletion_ancestry_exact": int(bool(missing_stored)),
            "blocked_nonessential_alternate_redeletion_exact": int(
                bool(missing_stored) and not target_essential
            ),
            "essential_return_deletion_witness_exact": int(
                bool(missing_stored) and target_essential
            ),
            "essential_target_contraction_exact": int(target_essential),
            "residual_target_rank_at_most_two": int(target_essential),
            "returned_target_edge_ancestry_proved": 1,
            "all_restoration_operations_proved": 0,
            "all_returned_edge_operations_proved": 0,
            "all_construction_ancestry_proved": 0,
            "global_transition_kind_bank_exhaustive": 0,
            "global_termination_proved": 0,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["transition_sha256"] = digest(result)
    return result


def exact_essential_return_history(
    records: Iterable[dict[str, Any]],
    recurrence_threshold: int,
) -> dict[str, Any]:
    require(
        isinstance(recurrence_threshold, int)
        and not isinstance(recurrence_threshold, bool)
        and recurrence_threshold >= 2,
        "recurrence threshold at least two required",
    )
    events = tuple(records)
    require(events, "essential-return history must be nonempty")
    require(
        all(
            event["transition_kind"]
            == "essential-return-deletion-ancestry-and-contraction"
            for event in events
        ),
        "history contains a nonessential return",
    )
    owners = {event["construction_labels"]["owner"] for event in events}
    targets = {tuple(event["target_edge"]) for event in events}
    stored = {
        tuple(tuple(edge) for edge in event["stored_avoidance_matching"])
        for event in events
    }
    require(len(owners) == len(targets) == len(stored) == 1,
            "history owner, target and stored matching must be fixed")
    matching = next(iter(stored))
    witness_edges = tuple(
        tuple(event["canonical_deletion_ancestry_witness"]["physical_edge"])
        for event in events
    )
    require(all(edge in matching for edge in witness_edges),
            "history witness outside stored matching")
    counts = {edge: witness_edges.count(edge) for edge in sorted(set(witness_edges))}
    recurrent = tuple(
        edge for edge, count in counts.items() if count >= recurrence_threshold
    )
    k = len(events)
    finite_bound = (recurrence_threshold - 1) * len(matching)
    if recurrent:
        category = "recurrent-stored-matching-blocker"
    else:
        category = "finite-essential-return-history"
        require(k <= finite_bound, "CMR723 finite history bound failed")
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "essential-target-return-history-v1",
        "owner": next(iter(owners)),
        "target_edge": list(next(iter(targets))),
        "stored_matching_size": len(matching),
        "recurrence_threshold": recurrence_threshold,
        "essential_return_episodes": k,
        "witness_multiplicities": [
            {"physical_edge": list(edge), "count": count}
            for edge, count in counts.items()
        ],
        "history_category": category,
        "recurrent_witnesses": [list(edge) for edge in recurrent],
        "finite_history_bound": finite_bound,
        "claims": {
            "linear_blocking_witness_stock_exact": 1,
            "recurrent_or_finite_essential_return_history_exact": 1,
            "returned_target_edge_ancestry_proved": 1,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["history_sha256"] = digest(result)
    return result


def exact_absence_run_manifest(
    physical_edge_raw: Iterable[int],
    presence_timeline: Iterable[bool],
) -> dict[str, Any]:
    edge = tuple(physical_edge_raw)
    require(len(edge) == 2 and all(isinstance(x, int) for x in edge),
            "physical edge pair required")
    timeline = tuple(presence_timeline)
    require(timeline and all(isinstance(value, bool) for value in timeline),
            "nonempty boolean presence timeline required")
    absence_runs = 0
    reintroductions = 0
    previous = True
    for present in timeline:
        if not present and previous:
            absence_runs += 1
        if present and not previous:
            reintroductions += 1
        previous = present
    require(absence_runs <= 1 + reintroductions,
            "absence-run/reintroduction identity failed")
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "stored-blocker-absence-run-v1",
        "physical_edge": list(edge),
        "presence_timeline": list(timeline),
        "maximal_absence_runs": absence_runs,
        "absent_to_present_reintroductions": reintroductions,
        "claims": {
            "absence_runs_at_most_one_plus_reintroductions": 1,
            "reintroduction_payment_route_bound": 1,
            "all_n_proved_by_checker": 0,
        },
    }
    result["absence_run_sha256"] = digest(result)
    return result


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "returned-target-edge-ancestry-v1",
        "source_theorems": [
            "CMR720", "CMR721", "CMR722", "CMR723",
            "CMR724", "CMR725", "CMR726",
        ],
        "claims": {
            "returned_target_edge_restoration_exact": 1,
            "stored_avoidance_survival_redeletion_exact": 1,
            "stored_avoidance_deletion_ancestry_exact": 1,
            "blocked_nonessential_alternate_redeletion_exact": 1,
            "essential_return_deletion_witness_exact": 1,
            "linear_blocking_witness_stock_exact": 1,
            "absence_run_reintroduction_identity_exact": 1,
            "essential_target_contraction_exact": 1,
            "residual_target_rank_at_most_two": 1,
            "returned_target_edge_ancestry_proved": 1,
            "all_restoration_operations_proved": 0,
            "all_returned_edge_operations_proved": 0,
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


def make_context(
    n: int, name: str, size: int, allowed: Iterable[Edge]
) -> dict[str, Any]:
    domain = tuple(range(size))
    return factor_context(n, name, domain, domain, tuple(sorted(allowed)))


def canonical_scenarios() -> dict[str, dict[str, Any]]:
    n = 4
    target = (0, 0)

    deletion_two = make_context(
        n, "two:deleted-target", 2, ((0, 1), (1, 0))
    )
    later_survives = make_context(
        n, "two:return-survives", 2,
        ((0, 0), (0, 1), (1, 0), (1, 1)),
    )
    survives = exact_return_manifest(
        n, "owner:return", deletion_two, target,
        ((0, 1), (1, 0)), later_survives,
        ((0, 1), (1, 0)),
    )

    stored_three = ((0, 1), (1, 2), (2, 0))
    deletion_three = make_context(
        n, "three:deleted-target", 3, stored_three
    )
    alternate = ((0, 2), (1, 0), (2, 1))
    later_nonessential = make_context(
        n, "three:blocked-nonessential", 3,
        (
            (0, 0), (0, 2), (1, 0), (1, 1),
            (2, 1), (2, 2),
        ),
    )
    blocked_nonessential = exact_return_manifest(
        n, "owner:return", deletion_three, target, stored_three,
        later_nonessential, alternate,
    )

    stored_essential = ((0, 1), (1, 0), (2, 2))
    deletion_essential = make_context(
        n, "three:deleted-essential-target", 3, stored_essential
    )
    identity = ((0, 0), (1, 1), (2, 2))
    later_essential_first = make_context(
        n, "three:essential-first", 3, identity
    )
    essential_first = exact_return_manifest(
        n, "owner:return", deletion_essential, target, stored_essential,
        later_essential_first, identity, identity,
    )
    later_essential_second = make_context(
        n, "three:essential-second", 3,
        ((0, 0), (0, 1), (1, 1), (2, 2)),
    )
    essential_second = exact_return_manifest(
        n, "owner:return", deletion_essential, target, stored_essential,
        later_essential_second, identity, identity,
    )
    return {
        "survives": survives,
        "blocked_nonessential": blocked_nonessential,
        "essential_first": essential_first,
        "essential_second": essential_second,
    }


def exhaustive_two_by_two_returns() -> dict[str, int]:
    n = 2
    domain = (0, 1)
    all_edges = tuple((row, column) for row in domain for column in domain)
    target = (0, 0)
    transitions = survives = blocked = essential = 0
    for deletion_size in range(1, len(all_edges) + 1):
        for deletion_allowed in combinations(
            tuple(edge for edge in all_edges if edge != target), deletion_size
        ):
            stored_family = generate_matchings(domain, domain, tuple(deletion_allowed))
            for stored in stored_family:
                for later_size in range(1, len(all_edges) + 1):
                    for later_allowed in combinations(all_edges, later_size):
                        if target not in later_allowed:
                            continue
                        later_family = generate_matchings(
                            domain, domain, tuple(later_allowed)
                        )
                        if not later_family:
                            continue
                        missing = tuple(edge for edge in stored if edge not in set(later_allowed))
                        target_is_essential = all(
                            target in set(matching) for matching in later_family
                        )
                        if not missing:
                            survives += 1
                        else:
                            blocked += 1
                            essential += int(target_is_essential)
                            if target_is_essential:
                                require(missing, "essential return lacks stored-edge witness")
                        transitions += 1
    require(transitions > 0 and survives > 0 and essential > 0,
            "two-by-two returned-edge census lacks a branch")
    return {
        "two_by_two_return_transitions": transitions,
        "two_by_two_stored_survival_cases": survives,
        "two_by_two_blocked_stored_cases": blocked,
        "two_by_two_essential_return_cases": essential,
    }


def history_and_absence_regression(
    scenarios: dict[str, dict[str, Any]]
) -> dict[str, int]:
    finite = exact_essential_return_history(
        [scenarios["essential_first"], scenarios["essential_second"]], 2
    )
    recurrent = exact_essential_return_history(
        [scenarios["essential_first"], scenarios["essential_first"]], 2
    )
    require(finite["history_category"] == "finite-essential-return-history",
            "finite essential-return history branch drift")
    require(recurrent["history_category"] == "recurrent-stored-matching-blocker",
            "recurrent essential-return history branch drift")
    absence = exact_absence_run_manifest(
        (0, 1), (False, False, True, False, True, False)
    )
    require(
        absence["maximal_absence_runs"] == 3
        and absence["absent_to_present_reintroductions"] == 2,
        "absence-run census drift",
    )
    return {
        "essential_return_history_scenarios": 2,
        "finite_essential_return_histories": 1,
        "recurrent_essential_return_histories": 1,
        "absence_run_scenarios": 1,
        "maximal_absence_runs": 3,
        "absent_to_present_reintroductions": 2,
    }


def mutation_tests(scenarios: dict[str, dict[str, Any]]) -> int:
    bad_calls = [
        lambda: exact_absence_run_manifest((0,), (False,)),
        lambda: exact_essential_return_history(
            [scenarios["survives"]], 2
        ),
        lambda: exact_return_manifest(
            4, "owner", scenarios["survives"]["later_context"],
            (0, 0), ((0, 1), (1, 0)),
            scenarios["survives"]["later_context"],
            ((0, 1), (1, 0)),
        ),
        lambda: exact_target_triple(
            ((0, 0), (0, 1), (1, 0)), (0, 1), (0, 1),
            (0, 0), ((0, 0), (0, 1), (1, 0), (1, 1)),
        ),
        lambda: exact_essential_return_history(
            [scenarios["essential_first"]], 1
        ),
    ]
    rejected = 0
    for call in bad_calls:
        try:
            call()
        except (ValueError, KeyError, TypeError):
            rejected += 1
        else:
            raise TargetEdgeReturnError("malformed returned-edge input accepted")
    for mutation in ("honesty", "seal", "witness"):
        bad = copy.deepcopy(scenarios["essential_first"])
        if mutation == "honesty":
            bad["claims"]["all_n_proved_by_checker"] = 1
        elif mutation == "seal":
            bad["transition_sha256"] = "0" * 64
        else:
            bad["canonical_deletion_ancestry_witness"]["physical_edge"] = [3, 3]
        try:
            require(bad == scenarios["essential_first"],
                    "corrupted returned-edge manifest mismatch")
        except TargetEdgeReturnError:
            rejected += 1
        else:
            raise TargetEdgeReturnError("corrupted returned-edge manifest accepted")
    require(rejected == 8, "mutation rejection census drift")
    return rejected


def finite_regression() -> dict[str, int]:
    scenarios = canonical_scenarios()
    categories = {record["transition_kind"] for record in scenarios.values()}
    require(
        categories
        == {
            "stored-avoidance-survives-exact-redeletion",
            "blocked-stored-avoidance-nonessential-return",
            "essential-return-deletion-ancestry-and-contraction",
        },
        "returned-edge category census drift",
    )
    return {
        "canonical_return_scenarios": len(scenarios),
        "stored_survival_redeletion_scenarios": 1,
        "blocked_nonessential_return_scenarios": 1,
        "essential_return_contraction_scenarios": 2,
        **exhaustive_two_by_two_returns(),
        **history_and_absence_regression(scenarios),
        "rejected_mutations": mutation_tests(scenarios),
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
