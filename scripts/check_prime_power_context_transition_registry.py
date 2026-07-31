#!/usr/bin/env python3
"""Check exact typed transitions for the square/asymmetric T02 context engine."""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any, Iterable

from check_prime_power_required_prefix_parent_generation import (
    Edge, exact_edge, exact_prescription, exact_required,
    generate_exact_triple_universe,
)
from check_prime_power_asymmetric_context_generation import (
    asymmetric_host_edges, contract_forced_set, exact_asymmetric_context,
    exact_asymmetric_manifest, generate_asymmetric_family,
)
from check_prime_power_asymmetric_target_dispatch import (
    exact_asymmetric_state, exact_first_missing_asymmetric_manifest,
)

EXPECTED_CONTRACT_SHA256 = "ace68b33d5c7111a5d623cb5a1db128ccc86bb193601404a5ede4713571b241d"


class ContextTransitionRegistryError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ContextTransitionRegistryError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode()).hexdigest()


def exact_labels(raw: Any) -> dict[str, str]:
    keys = ("operation_slot", "owner", "routing", "factor", "envelope")
    require(isinstance(raw, dict) and set(raw) == set(keys),
            "construction labels: exact key set required")
    require(all(isinstance(raw[key], str) and raw[key] for key in keys),
            "construction labels: nonempty strings required")
    return {key: raw[key] for key in keys}


def context_identity(n: int, rows: Any, columns: Any,
                     deleted: Any, required: Any) -> dict[str, Any]:
    domains, deleted_exact, required_exact = exact_asymmetric_context(
        n, rows, columns, deleted, required
    )
    row_domains = tuple(domain[0] for domain in domains)
    column_domains = tuple(domain[1] for domain in domains)
    manifest = exact_asymmetric_manifest(
        n, row_domains, column_domains, deleted_exact, required_exact
    )
    result: dict[str, Any] = {
        "ambient_side": n,
        "row_domains": [list(value) for value in row_domains],
        "column_domains": [list(value) for value in column_domains],
        "deleted_edges": [list(edge) for edge in deleted_exact],
        "required_edges": [list(edge) for edge in required_exact],
        "feasible_states": manifest["claims"]["feasible_states"],
        "realizable_collinear_triples": manifest["claims"][
            "realizable_collinear_triples"
        ],
        "feasible_family_sha256": digest(manifest["feasible_family"]),
        "triple_universe_sha256": digest(manifest["exact_triple_universe"]),
    }
    result["context_sha256"] = digest(result)
    return result


def contradiction_identity(n: int, rows: Any, columns: Any,
                           deleted: Any, required: Any) -> dict[str, Any]:
    deleted_exact = tuple(tuple(edge) for edge in deleted)
    required_exact = tuple(tuple(edge) for edge in required)
    require(set(deleted_exact) & set(required_exact),
            "contradiction terminal requires overlap")
    result: dict[str, Any] = {
        "ambient_side": n,
        "row_domains": [list(value) for value in rows],
        "column_domains": [list(value) for value in columns],
        "deleted_edges": [list(edge) for edge in deleted_exact],
        "required_edges": [list(edge) for edge in required_exact],
        "context_status": "required-deleted-contradiction-terminal",
        "feasible_states": 0,
        "realizable_collinear_triples": 0,
        "feasible_family_sha256": digest([]),
        "triple_universe_sha256": digest([]),
    }
    result["context_sha256"] = digest(result)
    return result


def record(kind: str, theorems: tuple[str, ...], labels: Any,
           parent: dict[str, Any], child: dict[str, Any],
           payload: dict[str, Any], semantics: str) -> dict[str, Any]:
    require(theorems and len(theorems) == len(set(theorems)),
            "source theorems must be nonempty and unique")
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-context-transition-record-v1",
        "operation_kind": kind,
        "source_theorems": list(theorems),
        "construction_labels": exact_labels(labels),
        "parent_context": parent,
        "child_context": child,
        "operation_payload": payload,
        "family_semantics": semantics,
        "claims": {
            "literal_parent_context_bound": 1,
            "literal_child_context_generated": 1,
            "child_family_semantics_exact": 1,
            "construction_labels_bound": 1,
            "actual_construction_ancestry_proved": 0,
            "global_transition_kind_bank_exhaustive": 0,
            "global_termination_proved": 0,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["transition_sha256"] = digest(result)
    return result


def deletion_transition(n: int, rows: Any, columns: Any, deleted: Any,
                        required: Any, edge_raw: Iterable[int],
                        labels: Any) -> dict[str, Any]:
    domains, deleted_exact, required_exact = exact_asymmetric_context(
        n, rows, columns, deleted, required
    )
    row_domains = tuple(domain[0] for domain in domains)
    column_domains = tuple(domain[1] for domain in domains)
    edge = exact_edge(edge_raw, n, "deleted_edge")
    require(edge in asymmetric_host_edges(domains), "deleted edge outside host")
    require(edge not in set(deleted_exact) | set(required_exact),
            "deleted edge already classified")
    parent_family = generate_asymmetric_family(
        n, row_domains, column_domains, deleted_exact, required_exact
    )
    child_deleted = tuple(sorted(deleted_exact + (edge,)))
    child_family = generate_asymmetric_family(
        n, row_domains, column_domains, child_deleted, required_exact
    )
    require(child_family == tuple(
        state for state in parent_family if edge not in set(state)
    ), "deletion transition family mismatch")
    require(set(generate_exact_triple_universe(child_family)) <=
            set(generate_exact_triple_universe(parent_family)),
            "deletion transition created a triple")
    return record(
        "single-edge-deletion", ("CMR830", "CMR2843", "CMR2868"), labels,
        context_identity(n, row_domains, column_domains,
                         deleted_exact, required_exact),
        context_identity(n, row_domains, column_domains,
                         child_deleted, required_exact),
        {"deleted_edge": list(edge), "parent_states": len(parent_family),
         "child_states": len(child_family)},
        "child family equals parent states omitting the deleted edge",
    )


def required_transition(n: int, rows: Any, columns: Any, deleted: Any,
                        required: Any, edge_raw: Iterable[int],
                        labels: Any) -> dict[str, Any]:
    domains, deleted_exact, required_exact = exact_asymmetric_context(
        n, rows, columns, deleted, required
    )
    row_domains = tuple(domain[0] for domain in domains)
    column_domains = tuple(domain[1] for domain in domains)
    edge = exact_edge(edge_raw, n, "required_edge")
    require(edge in asymmetric_host_edges(domains), "required edge outside host")
    require(edge not in set(deleted_exact) | set(required_exact),
            "required edge already classified")
    child_required = tuple(sorted(required_exact + (edge,)))
    exact_required(n, child_required)
    parent_family = generate_asymmetric_family(
        n, row_domains, column_domains, deleted_exact, required_exact
    )
    child_family = generate_asymmetric_family(
        n, row_domains, column_domains, deleted_exact, child_required
    )
    require(child_family == tuple(
        state for state in parent_family if edge in set(state)
    ), "required transition family mismatch")
    require(set(generate_exact_triple_universe(child_family)) <=
            set(generate_exact_triple_universe(parent_family)),
            "required transition created a triple")
    return record(
        "required-edge-conditioning", ("CMR862", "CMR2844", "CMR2869"),
        labels,
        context_identity(n, row_domains, column_domains,
                         deleted_exact, required_exact),
        context_identity(n, row_domains, column_domains,
                         deleted_exact, child_required),
        {"required_edge": list(edge), "parent_states": len(parent_family),
         "child_states": len(child_family)},
        "child family equals parent states containing the required edge",
    )


def contraction_transition(n: int, rows: Any, columns: Any, deleted: Any,
                           required: Any, forced_raw: Any,
                           labels: Any) -> dict[str, Any]:
    domains, deleted_exact, required_exact = exact_asymmetric_context(
        n, rows, columns, deleted, required
    )
    row_domains = tuple(domain[0] for domain in domains)
    column_domains = tuple(domain[1] for domain in domains)
    forced = exact_required(n, forced_raw)
    require(forced and set(forced) <= set(required_exact),
            "forced set must be nonempty and required")
    contraction = contract_forced_set(
        n, row_domains, column_domains, deleted_exact, required_exact, forced
    )
    child = context_identity(
        n, contraction["child_row_domains"],
        contraction["child_column_domains"],
        contraction["child_deleted_edges"],
        contraction["child_required_edges"],
    )
    require(child["feasible_family_sha256"] == digest(contraction["child_family"]),
            "contraction child-family seal mismatch")
    require(child["triple_universe_sha256"] ==
            digest(contraction["child_triple_universe"]),
            "contraction triple-universe seal mismatch")
    return record(
        "forced-set-contraction",
        ("CMR864", "CMR2849", "CMR2870", "CMR2871", "CMR2872"), labels,
        context_identity(n, row_domains, column_domains,
                         deleted_exact, required_exact), child,
        {"forced_edges": [list(edge) for edge in forced],
         "opposite_layer_blockers": contraction["opposite_layer_blockers"],
         "parent_states": contraction["claims"]["parent_feasible_states"],
         "child_states": contraction["claims"]["child_feasible_states"]},
        "child family is the exact forced-set restriction of the parent family",
    )


def cmr830_trace(n: int, rows: Any, columns: Any, deleted: Any,
                 required: Any, rejected_raw: Any, edge_raw: Any,
                 labels: Any) -> dict[str, Any]:
    domains, deleted_exact, required_exact = exact_asymmetric_context(
        n, rows, columns, deleted, required
    )
    row_domains = tuple(domain[0] for domain in domains)
    column_domains = tuple(domain[1] for domain in domains)
    rejected = exact_asymmetric_state(n, domains, rejected_raw, "rejected")
    edge = exact_edge(edge_raw, n, "selected_edge")
    family = generate_asymmetric_family(
        n, row_domains, column_domains, deleted_exact, required_exact
    )
    require(rejected in family and edge in set(rejected),
            "CMR830 trace requires a feasible rejected state and one of its edges")
    transition = deletion_transition(
        n, row_domains, column_domains, deleted_exact, required_exact, edge, labels
    )
    child_family = generate_asymmetric_family(
        n, row_domains, column_domains,
        tuple(sorted(deleted_exact + (edge,))), required_exact
    )
    require(rejected not in child_family, "CMR830 trace did not remove rejected state")
    result = {
        "version": 1, "rule_kind": "cmr830-context-transition-trace-v1",
        "rejected_state": [list(item) for item in rejected],
        "selected_edge": list(edge), "transition": transition,
        "claims": {"rejected_state_removed": 1,
                   "every_parent_state_omitting_edge_preserved": 1,
                   "cmr830_single_edge_trace_exact": 1,
                   "actual_construction_ancestry_proved": 0,
                   "actual_global_parent_rule_complete": 0,
                   "all_n_proved_by_checker": 0},
    }
    result["trace_sha256"] = digest(result)
    return result


def cmr862_trace(n: int, rows: Any, columns: Any, deleted: Any,
                 required: Any, rejected_raw: Any, prescription_raw: Any,
                 labels_raw: Any) -> dict[str, Any]:
    domains, deleted_exact, required_exact = exact_asymmetric_context(
        n, rows, columns, deleted, required
    )
    row_domains = tuple(domain[0] for domain in domains)
    column_domains = tuple(domain[1] for domain in domains)
    rejected = exact_asymmetric_state(n, domains, rejected_raw, "rejected")
    prescription = exact_prescription(n, prescription_raw)
    split = exact_first_missing_asymmetric_manifest(
        n, row_domains, column_domains, deleted_exact, required_exact,
        prescription, rejected
    )
    parent = context_identity(
        n, row_domains, column_domains, deleted_exact, required_exact
    )
    base_labels = exact_labels(labels_raw)
    transitions = []
    for branch in split["branches"]:
        index = branch["branch_index"]
        branch_labels = dict(base_labels)
        branch_labels["operation_slot"] += f":branch-{index}"
        if index < 3:
            if branch["context_status"] == "required-deleted-contradiction-terminal":
                child = contradiction_identity(
                    n, row_domains, column_domains,
                    branch["deleted_edges"], branch["required_edges"]
                )
            else:
                child = context_identity(
                    n, row_domains, column_domains,
                    branch["deleted_edges"], branch["required_edges"]
                )
            kind = "first-missing-deletion"
            payload = {"branch_index": index,
                       "omitted_edge": branch["omitted_edge"],
                       "context_status": branch["context_status"],
                       "branch_states": len(branch["members"])}
            semantics = "exact first-missing branch family or contradiction terminal"
        else:
            contraction = branch["conditioned_contraction"]
            child = context_identity(
                n, contraction["child_row_domains"],
                contraction["child_column_domains"],
                contraction["child_deleted_edges"],
                contraction["child_required_edges"]
            )
            kind = "first-missing-conditioned-contraction"
            payload = {"branch_index": 3,
                       "forced_edges": split["prescription"],
                       "conditioned_states": len(branch["members"]),
                       "child_states": contraction["claims"]["child_feasible_states"]}
            semantics = "exact contraction of the full-prescription branch"
        transitions.append(record(
            kind, ("CMR862", "CMR2794", "CMR2847", "CMR2882", "CMR2883"),
            branch_labels, parent, child, payload, semantics
        ))
    result = {
        "version": 1,
        "rule_kind": "cmr862-first-missing-context-transition-bundle-v1",
        "parent_context": parent,
        "rejected_state": [list(edge) for edge in rejected],
        "prescription": [list(edge) for edge in prescription],
        "branch_transitions": transitions,
        "claims": {"branch_transitions": 4, "branch_union_exact": 1,
                   "branch_partition_pairwise_disjoint": 1,
                   "rejected_state_only_in_conditioned_branch": 1,
                   "cmr862_first_missing_trace_exact": 1,
                   "actual_construction_ancestry_proved": 0,
                   "actual_global_parent_rule_complete": 0,
                   "all_n_proved_by_checker": 0},
    }
    result["bundle_sha256"] = digest(result)
    return result


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-context-transition-registry-v1",
        "source_theorems": [
            "CMR830", "CMR862", "CMR864", "CMR2794", "CMR2843",
            "CMR2844", "CMR2847", "CMR2849", "CMR2868", "CMR2869",
            "CMR2870", "CMR2871", "CMR2872", "CMR2882", "CMR2883",
        ],
        "transition_kinds": [
            "single-edge-deletion", "required-edge-conditioning",
            "forced-set-contraction", "first-missing-deletion",
            "first-missing-conditioned-contraction",
        ],
        "claims": {
            "canonical_context_identity_sealed": 1,
            "single_edge_deletion_transition_exact": 1,
            "required_edge_conditioning_transition_exact": 1,
            "forced_set_contraction_transition_exact": 1,
            "cmr830_single_edge_trace_exact": 1,
            "cmr862_first_missing_trace_exact": 1,
            "transition_child_context_generated": 1,
            "transition_family_semantics_exact": 1,
            "construction_labels_bound": 1,
            "actual_construction_ancestry_proved": 0,
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


def labels(slot: str) -> dict[str, str]:
    return {"operation_slot": slot, "owner": "unverified-owner",
            "routing": "unverified-routing", "factor": "unverified-factor",
            "envelope": "unverified-envelope"}


def finite_regression() -> dict[str, int]:
    n = 3
    rows = (tuple(range(n)), tuple(range(n)))
    columns = rows
    family = generate_asymmetric_family(n, rows, columns, (), ())
    require(len(family) == 12, "side-three base-family census drift")
    domains, _, _ = exact_asymmetric_context(n, rows, columns, (), ())
    host = asymmetric_host_edges(domains)
    for edge in host:
        deletion_transition(n, rows, columns, (), (), edge, labels(f"d:{edge}"))
        required_transition(n, rows, columns, (), (), edge, labels(f"r:{edge}"))
    traces = 0
    for rejected in family:
        for edge in rejected:
            cmr830_trace(n, rows, columns, (), (), rejected, edge,
                         labels(f"830:{rejected}:{edge}"))
            traces += 1
    contractions = bundles = 0
    for prescription in generate_exact_triple_universe(family):
        containing = [state for state in family if set(prescription) <= set(state)]
        contraction_transition(n, rows, columns, (), prescription, prescription,
                               labels(f"c:{prescription}"))
        contractions += 1
        for rejected in containing:
            cmr862_trace(n, rows, columns, (), (), rejected, prescription,
                         labels(f"862:{prescription}:{rejected}"))
            bundles += 1
    require((len(host), traces) == (18, 72), "transition census drift")
    require(contractions > 0 and bundles > 0, "missing contraction coverage")
    return {"side_three_parent_states": 12,
            "single_edge_deletion_transitions": 18,
            "required_edge_conditioning_transitions": 18,
            "cmr830_traces": traces,
            "forced_set_contraction_transitions": contractions,
            "cmr862_first_missing_bundles": bundles,
            "cmr862_branch_transitions": 4 * bundles}


def mutation_tests() -> int:
    n = 3
    rows = (tuple(range(n)), tuple(range(n)))
    columns = rows
    family = generate_asymmetric_family(n, rows, columns, (), ())
    prescription = generate_exact_triple_universe(family)[0]
    rejected = next(state for state in family if set(prescription) <= set(state))
    good = cmr830_trace(n, rows, columns, (), (), rejected, rejected[0], labels("good"))
    bad_calls = [
        lambda: deletion_transition(n, rows, columns, (), (), (0, 3, 0), labels("x")),
        lambda: required_transition(n, rows, columns, ((0, 0, 0),), (),
                                    (0, 0, 0), labels("x")),
        lambda: contraction_transition(n, rows, columns, (), (), prescription, labels("x")),
        lambda: cmr830_trace(n, rows, columns, (), (), rejected,
                             next(edge for edge in asymmetric_host_edges(
                                 exact_asymmetric_context(n, rows, columns, (), ())[0]
                             ) if edge not in set(rejected)), labels("x")),
        lambda: cmr862_trace(n, rows, columns, (), (),
                             next(state for state in family
                                  if not set(prescription) <= set(state)),
                             prescription, labels("x")),
        lambda: deletion_transition(n, rows, columns, (), (), (0, 0, 0),
                                    {"owner": "missing"}),
    ]
    rejected_total = 0
    for call in bad_calls:
        try:
            call()
        except (ValueError, StopIteration):
            rejected_total += 1
        else:
            raise ContextTransitionRegistryError("malformed transition accepted")
    for mutation in ("honesty", "seal"):
        bad = copy.deepcopy(good)
        if mutation == "honesty":
            bad["transition"]["claims"]["actual_construction_ancestry_proved"] = 1
        else:
            bad["trace_sha256"] = "0" * 64
        try:
            require(bad == good, "corrupted transition trace mismatch")
        except ContextTransitionRegistryError:
            rejected_total += 1
        else:
            raise ContextTransitionRegistryError("corrupted trace accepted")
    require(rejected_total == 8, "mutation rejection census drift")
    return rejected_total


def self_test() -> dict[str, Any]:
    return {**validate_contract(), **finite_regression(),
            "rejected_mutations": mutation_tests(),
            "contract_sha256": contract_manifest()["contract_sha256"]}


def main() -> None:
    print(json.dumps(self_test(), sort_keys=True))


if __name__ == "__main__":
    main()
