#!/usr/bin/env python3
"""Verify fixed-routing child-product and strict child-handoff ancestry.

CMR656--CMR663 split a factor by its canonical prefix envelope and prove exact
factorisation after fixing the vertex-routing skeleton. CMR682--CMR683 show that
a mixed-clean dirty product hands its obstruction to a strict child factor. This
checker reconstructs both operations as typed context transitions.

It does not implement the preceding mixed-atom deletion procedure, prove all
construction operations exhaustive, prove global termination, or prove the
all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations, product
from typing import Any, Iterable

import check_prime_power_routing_change_context_ancestry as routing

Matching = routing.Matching
EXPECTED_CONTRACT_SHA256 = "bd725106632e65cac38f2b33fb1787f3d5ef93d0825c4ccfc0d2afd2c6492dae"


class FactorChildProductAncestryError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise FactorChildProductAncestryError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def is_collinear(triple: tuple[tuple[int, int], ...]) -> bool:
    if len(set(triple)) != 3:
        return False
    (x1, y1), (x2, y2), (x3, y3) = triple
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def matching_triples(matching: Matching) -> tuple[tuple[tuple[int, int], ...], ...]:
    return tuple(triple for triple in combinations(matching, 3) if is_collinear(triple))


def child_data(
    p: int,
    beta: int,
    x: tuple[int, ...],
    y: tuple[int, ...],
    deleted: tuple[tuple[int, int], ...],
    skeleton: dict[str, Any],
) -> tuple[dict[str, Any], ...]:
    children = []
    for cell in skeleton["routing_cells"]:
        xs = tuple(cell["sources"])
        ys = tuple(cell["targets"])
        child_deleted = tuple(edge for edge in deleted if edge[0] in xs and edge[1] in ys)
        family = routing.generate_factor_family(xs, ys, child_deleted)
        record: dict[str, Any] = {
            "source_child": cell["source_child"],
            "target_child": cell["target_child"],
            "sources": list(xs),
            "targets": list(ys),
            "matching_size": len(xs),
            "deleted_edges": [list(edge) for edge in child_deleted],
            "feasible_family": [[list(edge) for edge in matching] for matching in family],
            "feasible_states": len(family),
            "prefix_depth": beta + 1,
        }
        record["child_sha256"] = digest(record)
        children.append(record)
    return tuple(sorted(children, key=lambda row: (row["source_child"], row["target_child"])))


def product_family(children: tuple[dict[str, Any], ...]) -> tuple[Matching, ...]:
    child_families = [
        tuple(tuple(tuple(edge) for edge in matching) for matching in child["feasible_family"])
        for child in children
    ]
    states = []
    for choices in product(*child_families):
        states.append(tuple(sorted(edge for matching in choices for edge in matching)))
    return tuple(sorted(states))


def exact_factor_product_manifest(
    p: int,
    h: int,
    x_raw: Iterable[int],
    y_raw: Iterable[int],
    deleted_raw: Iterable[Iterable[int]],
    routing_matching_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    t = p ** h
    x = routing.exact_coordinates(x_raw, t, "sources")
    y = routing.exact_coordinates(y_raw, t, "targets")
    require(len(x) == len(y) and len(x) >= 2, "nontrivial balanced factor required")
    deleted = routing.exact_deleted(deleted_raw, x, y)
    selected = routing.exact_matching(
        routing_matching_raw, x, y, deleted, "routing_matching"
    )
    beta = min(routing.delta(x, p, h), routing.delta(y, p, h))
    require(beta < h, "strict factor split required")
    skeleton = routing.routing_skeleton(selected, x, y, p, beta)
    children = child_data(p, beta, x, y, deleted, skeleton)
    require(len(children) >= 2, "routing product must have at least two positive children")
    require(all(1 <= child["matching_size"] <= len(x) - 1 for child in children),
            "child matching size is not strict")

    parent_family = routing.generate_factor_family(x, y, deleted)
    selected_digest = skeleton["routing_sha256"]
    fixed_routing_family = tuple(
        matching for matching in parent_family
        if routing.routing_skeleton(matching, x, y, p, beta)["routing_sha256"]
        == selected_digest
    )
    generated_product = product_family(children)
    require(generated_product == fixed_routing_family,
            "fixed-routing family differs from generated child product")

    parent_context = routing.context_identity(t, x, y, deleted)
    factor_label = digest({"ambient_side": t, "sources": x, "targets": y,
                           "deleted": deleted})
    child_contexts = []
    for child in children:
        xs, ys = tuple(child["sources"]), tuple(child["targets"])
        child_deleted = tuple(tuple(edge) for edge in child["deleted_edges"])
        context = routing.context_identity(t, xs, ys, child_deleted)
        context.update({
            "source_child": child["source_child"],
            "target_child": child["target_child"],
            "prefix_depth": beta + 1,
            "matching_size": child["matching_size"],
        })
        context["child_context_sha256"] = digest(context)
        child_contexts.append(context)

    envelope = {
        "prime": p,
        "height": h,
        "parent_depth": beta,
        "child_depth": beta + 1,
        "parent_envelope_side": t // (p ** beta),
        "child_envelope_side": t // (p ** (beta + 1)),
    }
    envelope["envelope_sha256"] = digest(envelope)
    result: dict[str, Any] = {
        "version": 1,
        "transition_kind": "fixed-routing-child-product-split",
        "source_theorems": [
            "CMR656", "CMR657", "CMR658", "CMR659", "CMR660",
            "CMR661", "CMR662", "CMR663", "CMR2900", "CMR2901", "CMR2902",
        ],
        "construction_labels": {
            "operation_slot": "CMR659-CMR663-fixed-routing-child-product",
            "owner": f"factor-owner:{factor_label}",
            "routing": f"routing:{selected_digest}",
            "factor": f"factor:{factor_label}",
            "envelope": f"prefix-envelope:{envelope['envelope_sha256']}",
        },
        "parent_context": parent_context,
        "routing_skeleton": skeleton,
        "factor_envelope": envelope,
        "child_product": child_contexts,
        "fixed_routing_family": [[list(edge) for edge in state]
                                 for state in fixed_routing_family],
        "generated_product_family": [[list(edge) for edge in state]
                                     for state in generated_product],
        "claims": {
            "factor_context_embedded": 1,
            "canonical_first_split_exact": 1,
            "routing_skeleton_fixed": 1,
            "child_contexts_generated": 1,
            "fixed_routing_product_bijection_exact": 1,
            "positive_child_count_at_least_two": 1,
            "strict_child_matching_size_descent": 1,
            "strict_prefix_envelope_descent": 1,
            "factor_product_construction_ancestry_proved": 1,
            "all_construction_ancestry_proved": 0,
            "global_transition_kind_bank_exhaustive": 0,
            "global_termination_proved": 0,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def edge_child_index(edge: tuple[int, int], children: tuple[dict[str, Any], ...]) -> int:
    candidates = [index for index, child in enumerate(children)
                  if edge[0] in child["sources"] and edge[1] in child["targets"]]
    require(len(candidates) == 1, "product edge has no unique child")
    return candidates[0]


def exact_mixed_clean_child_handoff_manifest(
    p: int,
    h: int,
    x_raw: Iterable[int],
    y_raw: Iterable[int],
    deleted_raw: Iterable[Iterable[int]],
    routing_matching_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    product_manifest = exact_factor_product_manifest(
        p, h, x_raw, y_raw, deleted_raw, routing_matching_raw
    )
    x = tuple(x_raw)
    y = tuple(y_raw)
    deleted = tuple(tuple(edge) for edge in deleted_raw)
    beta = product_manifest["factor_envelope"]["parent_depth"]
    skeleton = product_manifest["routing_skeleton"]
    children = child_data(p, beta, x, y, deleted, skeleton)
    states = tuple(tuple(tuple(edge) for edge in state)
                   for state in product_manifest["generated_product_family"])

    mixed_triples = set()
    clean_states = []
    for state in states:
        triples = matching_triples(state)
        if not triples:
            clean_states.append(state)
        for triple in triples:
            indices = {edge_child_index(edge, children) for edge in triple}
            if len(indices) > 1:
                mixed_triples.add(triple)
    require(not mixed_triples, "product is not mixed-clean")
    require(not clean_states, "mixed-clean product already has a globally clean state")

    dirty_children = []
    for index, child in enumerate(children):
        family = tuple(tuple(tuple(edge) for edge in matching)
                       for matching in child["feasible_family"])
        if family and all(matching_triples(matching) for matching in family):
            dirty_children.append(index)
    require(dirty_children, "no pure-dirty child exists")
    selected_index = dirty_children[0]
    selected_child = product_manifest["child_product"][selected_index]
    require(selected_child["matching_size"] < len(x),
            "selected child does not decrease factor side")
    require(selected_child["prefix_depth"] == beta + 1,
            "selected child does not increase envelope depth")

    result: dict[str, Any] = {
        "version": 1,
        "transition_kind": "mixed-clean-strict-child-handoff",
        "source_theorems": ["CMR659", "CMR682", "CMR683", "CMR2920"],
        "parent_product_manifest_sha256": product_manifest["manifest_sha256"],
        "parent_factor": product_manifest["construction_labels"]["factor"],
        "parent_envelope": product_manifest["construction_labels"]["envelope"],
        "mixed_triples": [],
        "globally_clean_product_states": [],
        "pure_dirty_child_indices": dirty_children,
        "selected_child_index": selected_index,
        "selected_child_context": selected_child,
        "claims": {
            "mixed_clean_product_exact": 1,
            "global_clean_state_absent": 1,
            "pure_dirty_child_exists": 1,
            "canonical_dirty_child_selected": 1,
            "strict_child_factor_side_descent": 1,
            "strict_child_envelope_descent": 1,
            "mixed_clean_child_handoff_ancestry_proved": 1,
            "mixed_atom_deletion_ancestry_proved": 0,
            "all_construction_ancestry_proved": 0,
            "global_transition_kind_bank_exhaustive": 0,
            "global_termination_proved": 0,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def validate_manifest(manifest: Any, function: Any, *args: Any) -> dict[str, int]:
    expected = function(*args)
    require(isinstance(manifest, dict) and manifest == expected,
            "factor child-product manifest mismatch")
    return copy.deepcopy(expected["claims"])


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "prime-power-factor-child-product-ancestry-v1",
        "source_theorems": [
            "CMR656", "CMR657", "CMR658", "CMR659", "CMR660", "CMR661",
            "CMR662", "CMR663", "CMR682", "CMR683", "CMR2900", "CMR2901",
            "CMR2902",
        ],
        "claims": {
            "fixed_routing_product_bijection_exact": 1,
            "child_contexts_generated": 1,
            "strict_child_matching_size_descent": 1,
            "strict_prefix_envelope_descent": 1,
            "factor_product_construction_ancestry_proved": 1,
            "mixed_clean_child_handoff_ancestry_proved": 1,
            "mixed_atom_deletion_ancestry_proved": 0,
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
    result = contract_manifest()
    require(result["contract_sha256"] == EXPECTED_CONTRACT_SHA256,
            "built-in contract digest drift")
    return copy.deepcopy(result["claims"])


def finite_regression() -> dict[str, int]:
    splits = child_contexts = fixed_states = 0
    for p, h, coordinates in (
        (2, 2, (0, 1, 2, 3)),
        (3, 1, (0, 1, 2)),
    ):
        for d in range(2, min(len(coordinates), 3) + 1):
            for x in combinations(coordinates, d):
                for y in combinations(coordinates, d):
                    family = routing.generate_factor_family(x, y, ())
                    seen = set()
                    for matching in family:
                        beta = min(routing.delta(x, p, h), routing.delta(y, p, h))
                        if beta >= h:
                            continue
                        skeleton = routing.routing_skeleton(matching, x, y, p, beta)
                        key = skeleton["routing_sha256"]
                        if key in seen or len(skeleton["routing_cells"]) < 2:
                            continue
                        seen.add(key)
                        manifest = exact_factor_product_manifest(p, h, x, y, (), matching)
                        splits += 1
                        child_contexts += len(manifest["child_product"])
                        fixed_states += len(manifest["fixed_routing_family"])

    witness_x = (0, 1, 2, 4)
    witness_y = (0, 2, 3, 4)
    even_x = (0, 2, 4)
    even_y = (0, 2, 4)
    allowed_even = {(0, 0), (2, 2), (4, 4)}
    deleted = tuple(sorted(
        (source, target) for source in even_x for target in even_y
        if (source, target) not in allowed_even
    ))
    witness_matching = ((0, 0), (1, 3), (2, 2), (4, 4))
    handoff = exact_mixed_clean_child_handoff_manifest(
        2, 3, witness_x, witness_y, deleted, witness_matching
    )
    require(handoff["selected_child_context"]["matching_size"] == 3,
            "strict-child handoff witness drift")
    require(splits > 0 and child_contexts >= 2 * splits,
            "factor product regression produced no strict products")
    return {
        "fixed_routing_product_splits": splits,
        "generated_child_contexts": child_contexts,
        "fixed_routing_states": fixed_states,
        "mixed_clean_handoff_witnesses": 1,
        "handoff_child_matching_size": 3,
    }


def mutation_tests() -> int:
    p, h = 2, 2
    x = y = (0, 1, 2, 3)
    matching = ((0, 0), (1, 1), (2, 2), (3, 3))
    good = exact_factor_product_manifest(p, h, x, y, (), matching)
    bad_calls = [
        lambda: exact_factor_product_manifest(p, h, (0,), (0,), (), ((0, 0),)),
        lambda: exact_factor_product_manifest(p, h, x, y, ((0, 0),), matching),
        lambda: exact_factor_product_manifest(p, h, x, (0, 1, 2), (), matching),
    ]
    rejected = 0
    for call in bad_calls:
        try:
            call()
        except (ValueError, routing.RoutingChangeContextAncestryError):
            rejected += 1
        else:
            raise FactorChildProductAncestryError("malformed factor product accepted")
    for field, value in (
        ("all_construction_ancestry_proved", 1),
        ("global_termination_proved", 1),
        ("fixed_routing_product_bijection_exact", 0),
    ):
        bad = copy.deepcopy(good)
        bad["claims"][field] = value
        try:
            validate_manifest(bad, exact_factor_product_manifest,
                              p, h, x, y, (), matching)
        except FactorChildProductAncestryError:
            rejected += 1
        else:
            raise FactorChildProductAncestryError("corrupted factor product accepted")
    bad = copy.deepcopy(good)
    bad["manifest_sha256"] = "0" * 64
    try:
        validate_manifest(bad, exact_factor_product_manifest,
                          p, h, x, y, (), matching)
    except FactorChildProductAncestryError:
        rejected += 1
    else:
        raise FactorChildProductAncestryError("bad factor-product seal accepted")
    require(rejected == 7, "mutation rejection census drift")
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
