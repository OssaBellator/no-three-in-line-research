#!/usr/bin/env python3
"""Verify routing-change history payment and finite-stock alternatives.

This companion to check_prime_power_routing_change_context_ancestry.py applies
CMR674--CMR676 to theorem-derived routing-change transition records. It checks
exact entering/leaving support incidence, labelled nonroot full-token payment,
and the recurrent-edge versus finite-history bound at one fixed factor owner and
envelope.

It does not prove the complete construction transition bank, global termination,
or the all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
from collections import Counter
from typing import Any, Iterable

import check_prime_power_routing_change_context_ancestry as ancestry

EXPECTED_CONTRACT_SHA256 = "b7c4efe585e6fa70cf6556e4eb86969e685c542d8192326b3c29169c8f9b2259"


class RoutingChangeHistoryPaymentError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RoutingChangeHistoryPaymentError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_lambda(value: Any) -> int:
    require(isinstance(value, int) and not isinstance(value, bool) and value >= 2,
            "lambda: integer at least two required")
    return value


def exact_history_manifest(
    p: int,
    h: int,
    x: Iterable[int],
    y: Iterable[int],
    deleted: Iterable[Iterable[int]],
    matching_history: Iterable[Iterable[Iterable[int]]],
    lambda_raw: Any,
) -> dict[str, Any]:
    lam = exact_lambda(lambda_raw)
    history = tuple(tuple(tuple(edge) for edge in matching) for matching in matching_history)
    require(len(history) >= 2, "history: at least two matchings required")
    require(len(history) == len(set(history)), "history: simple distinct matching history required")

    transitions = []
    for index, (old, new) in enumerate(zip(history, history[1:])):
        try:
            transition = ancestry.exact_routing_change_manifest(
                p, h, x, y, deleted, old, new
            )
        except ancestry.RoutingChangeContextAncestryError as error:
            raise RoutingChangeHistoryPaymentError(
                f"history transition {index}: {error}"
            ) from error
        transitions.append(transition)

    factor_labels = {record["construction_labels"]["factor"] for record in transitions}
    envelope_labels = {record["construction_labels"]["envelope"] for record in transitions}
    owner_labels = {record["construction_labels"]["owner"] for record in transitions}
    require(len(factor_labels) == len(envelope_labels) == len(owner_labels) == 1,
            "history: factor, envelope and owner must remain fixed")

    entering_counter: Counter[tuple[int, int, int]] = Counter()
    leaving_counter: Counter[tuple[int, int, int]] = Counter()
    for record in transitions:
        entering_counter.update(tuple(edge) for edge in record["entering_routing_support"])
        leaving_counter.update(tuple(edge) for edge in record["leaving_routing_support"])

    transition_count = len(transitions)
    entering_incidences = sum(entering_counter.values())
    leaving_incidences = sum(leaving_counter.values())
    require(entering_incidences >= 2 * transition_count,
            "entering support lower bound failed")
    require(leaving_incidences >= 2 * transition_count,
            "leaving support lower bound failed")

    first = transitions[0]
    prime = first["factor_envelope"]["prime"]
    height = first["factor_envelope"]["height"]
    incidence_per_edge = (prime + 1) * (height - 1)
    host_edges = len(tuple(x)) * len(tuple(y)) - len(tuple(deleted))
    finite_bound = ((lam - 1) * host_edges) // 2
    recurrent_entering = tuple(sorted(
        edge for edge, count in entering_counter.items() if count >= lam
    ))
    recurrent_leaving = tuple(sorted(
        edge for edge, count in leaving_counter.items() if count >= lam
    ))
    if not recurrent_entering:
        require(transition_count <= finite_bound,
                "CMR674 entering finite-history bound failed")
    if not recurrent_leaving:
        require(transition_count <= finite_bound,
                "CMR674 leaving finite-history bound failed")

    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "prime-power-routing-change-history-payment-v1",
        "lambda": lam,
        "factor": next(iter(factor_labels)),
        "owner": next(iter(owner_labels)),
        "envelope": next(iter(envelope_labels)),
        "transition_sha256s": [record["transition_sha256"] for record in transitions],
        "transition_count": transition_count,
        "factor_host_edges": host_edges,
        "finite_history_bound": finite_bound,
        "entering_support_multiplicities": [
            [list(edge), entering_counter[edge]] for edge in sorted(entering_counter)
        ],
        "leaving_support_multiplicities": [
            [list(edge), leaving_counter[edge]] for edge in sorted(leaving_counter)
        ],
        "recurrent_entering_edges": [list(edge) for edge in recurrent_entering],
        "recurrent_leaving_edges": [list(edge) for edge in recurrent_leaving],
        "labelled_nonroot_full_token_incidence_per_edge": incidence_per_edge,
        "entering_full_token_incidences": incidence_per_edge * entering_incidences,
        "leaving_full_token_incidences": incidence_per_edge * leaving_incidences,
        "claims": {
            "fixed_factor_owner_envelope_history": 1,
            "routing_change_support_minimum_two": 1,
            "routing_change_full_token_payment_exact": 1,
            "entering_recurrent_edge_or_finite_history_exact": 1,
            "leaving_recurrent_edge_or_finite_history_exact": 1,
            "routing_change_history_endpoint_exact": 1,
            "routing_change_construction_ancestry_proved": 1,
            "all_construction_ancestry_proved": 0,
            "global_transition_kind_bank_exhaustive": 0,
            "global_termination_proved": 0,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def validate_manifest(manifest: Any, *args: Any) -> dict[str, int]:
    expected = exact_history_manifest(*args)
    require(isinstance(manifest, dict) and manifest == expected,
            "routing-change history manifest mismatch")
    return copy.deepcopy(expected["claims"])


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "prime-power-routing-change-history-payment-v1",
        "source_theorems": ["CMR413", "CMR674", "CMR675", "CMR676", "CMR2900"],
        "claims": {
            "fixed_factor_owner_envelope_history": 1,
            "routing_change_support_minimum_two": 1,
            "routing_change_full_token_payment_exact": 1,
            "entering_recurrent_edge_or_finite_history_exact": 1,
            "leaving_recurrent_edge_or_finite_history_exact": 1,
            "routing_change_history_endpoint_exact": 1,
            "routing_change_construction_ancestry_proved": 1,
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
    manifest = contract_manifest()
    require(manifest["contract_sha256"] == EXPECTED_CONTRACT_SHA256,
            "built-in contract digest drift")
    return copy.deepcopy(manifest["claims"])


def greedy_routing_history(p: int, h: int, x: tuple[int, ...],
                           y: tuple[int, ...]) -> tuple[ancestry.Matching, ...]:
    family = ancestry.generate_factor_family(x, y, ())
    beta = min(ancestry.delta(x, p, h), ancestry.delta(y, p, h))
    history = [family[0]]
    remaining = list(family[1:])
    while remaining:
        current = history[-1]
        current_routing = ancestry.routing_skeleton(current, x, y, p, beta)[
            "routing_sha256"
        ]
        index = next((index for index, candidate in enumerate(remaining)
                      if ancestry.routing_skeleton(candidate, x, y, p, beta)[
                          "routing_sha256"
                      ] != current_routing), None)
        if index is None:
            break
        history.append(remaining.pop(index))
    return tuple(history)


def finite_regression() -> dict[str, int]:
    histories = transitions = recurrent_cases = finite_cases = token_incidences = 0
    for p, h, x in (
        (2, 2, (0, 1, 2, 3)),
        (3, 1, (0, 1, 2)),
    ):
        history = greedy_routing_history(p, h, x, x)
        require(len(history) >= 3, "routing-history witness too short")
        for length in range(3, len(history) + 1):
            prefix = history[:length]
            for lam in (2, 3, 4):
                manifest = exact_history_manifest(p, h, x, x, (), prefix, lam)
                histories += 1
                transitions += manifest["transition_count"]
                token_incidences += manifest["entering_full_token_incidences"]
                recurrent_cases += int(bool(manifest["recurrent_entering_edges"]))
                finite_cases += int(not manifest["recurrent_entering_edges"])
    require(histories > 0 and recurrent_cases > 0 and finite_cases > 0,
            "history regression did not exercise both alternatives")
    return {
        "routing_histories_checked": histories,
        "routing_transitions_in_histories": transitions,
        "recurrent_entering_edge_cases": recurrent_cases,
        "finite_history_cases": finite_cases,
        "entering_full_token_incidences": token_incidences,
    }


def mutation_tests() -> int:
    p, h = 2, 2
    x = (0, 1, 2, 3)
    history = greedy_routing_history(p, h, x, x)[:4]
    good = exact_history_manifest(p, h, x, x, (), history, 3)
    bad_calls = [
        lambda: exact_history_manifest(p, h, x, x, (), history, 1),
        lambda: exact_history_manifest(p, h, x, x, (), history[:1], 2),
        lambda: exact_history_manifest(p, h, x, x, (), history + (history[0],), 2),
        lambda: exact_history_manifest(p, h, x, x, ((0, 0),), history, 2),
    ]
    rejected = 0
    for call in bad_calls:
        try:
            call()
        except (ValueError, ancestry.RoutingChangeContextAncestryError):
            rejected += 1
        else:
            raise RoutingChangeHistoryPaymentError("malformed history accepted")
    for field, value in (
        ("all_construction_ancestry_proved", 1),
        ("global_termination_proved", 1),
        ("routing_change_history_endpoint_exact", 0),
    ):
        bad = copy.deepcopy(good)
        bad["claims"][field] = value
        try:
            validate_manifest(bad, p, h, x, x, (), history, 3)
        except RoutingChangeHistoryPaymentError:
            rejected += 1
        else:
            raise RoutingChangeHistoryPaymentError("corrupted history accepted")
    bad = copy.deepcopy(good)
    bad["manifest_sha256"] = "0" * 64
    try:
        validate_manifest(bad, p, h, x, x, (), history, 3)
    except RoutingChangeHistoryPaymentError:
        rejected += 1
    else:
        raise RoutingChangeHistoryPaymentError("bad history seal accepted")
    require(rejected == 8, "mutation rejection census drift")
    return rejected


def self_test() -> dict[str, Any]:
    return {
        **validate_contract(),
        **finite_regression(),
        "rejected_mutations": mutation_tests(),
        "contract_sha256": contract_manifest()["contract_sha256"],
    }


def main() -> None:
    print(json.dumps(self_test(), sort_keys=True))


if __name__ == "__main__":
    main()
