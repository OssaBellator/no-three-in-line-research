#!/usr/bin/env python3
"""Verify mixed-child deletion and forced-certificate ancestry.

Starting from the generated fixed-routing child product of CMR2920--CMR2925,
this checker executes the canonical CMR677--CMR681 procedure. It reconstructs
active mixed triples, verifies their exact Cartesian occurrence boxes, deletes
the first nonessential atom edge while preserving the child product, and stops
at a mixed-clean product or a forced mixed certificate.

It does not prove the forced-certificate escape branches, all construction
operations exhaustive, global termination, or the all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations, product
from typing import Any, Iterable

import check_prime_power_factor_child_product_ancestry as factor
import check_prime_power_routing_change_context_ancestry as routing

Matching = routing.Matching
Triple = tuple[tuple[int, int], ...]
EXPECTED_CONTRACT_SHA256 = "b49c1313b765fc63676aed96bfbb91adf52f17293feb47089cfc8129b42b7429"


class MixedChildDeletionAncestryError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise MixedChildDeletionAncestryError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_children_from_manifest(product_manifest: dict[str, Any]) -> tuple[dict[str, Any], ...]:
    children = []
    for context in product_manifest["child_product"]:
        child = {
            "source_child": context["source_child"],
            "target_child": context["target_child"],
            "sources": tuple(context["row_domains"][0]),
            "targets": tuple(context["column_domains"][0]),
            "matching_size": context["matching_size"],
            "deleted_edges": tuple(
                (edge[1], edge[2]) for edge in context["deleted_edges"]
            ),
            "prefix_depth": context["prefix_depth"],
        }
        children.append(child)
    return tuple(children)


def child_families(children: tuple[dict[str, Any], ...]) -> tuple[tuple[Matching, ...], ...]:
    return tuple(
        routing.generate_factor_family(
            child["sources"], child["targets"], child["deleted_edges"]
        )
        for child in children
    )


def generated_product(families: tuple[tuple[Matching, ...], ...]) -> tuple[Matching, ...]:
    states = []
    for choices in product(*families):
        states.append(tuple(sorted(edge for matching in choices for edge in matching)))
    return tuple(sorted(states))


def edge_child_index(edge: tuple[int, int], children: tuple[dict[str, Any], ...]) -> int:
    indices = [index for index, child in enumerate(children)
               if edge[0] in child["sources"] and edge[1] in child["targets"]]
    require(len(indices) == 1, "edge lacks unique routing child")
    return indices[0]


def mixed_triples(states: tuple[Matching, ...],
                  children: tuple[dict[str, Any], ...]) -> tuple[Triple, ...]:
    triples = set()
    for state in states:
        for triple in factor.matching_triples(state):
            if len({edge_child_index(edge, children) for edge in triple}) > 1:
                triples.add(triple)
    return tuple(sorted(triples))


def occurrence_box(atom: Triple, children: tuple[dict[str, Any], ...],
                   families: tuple[tuple[Matching, ...], ...]) -> tuple[Matching, ...]:
    local_families = []
    for index, family in enumerate(families):
        local_atom = {edge for edge in atom if edge_child_index(edge, children) == index}
        local_families.append(tuple(
            matching for matching in family if local_atom <= set(matching)
        ))
    if any(not family for family in local_families):
        return ()
    return generated_product(tuple(local_families))


def essential_edges(atom: Triple, children: tuple[dict[str, Any], ...],
                    families: tuple[tuple[Matching, ...], ...]) -> tuple[tuple[int, int], ...]:
    essential = []
    for edge in atom:
        index = edge_child_index(edge, children)
        if all(edge in matching for matching in families[index]):
            essential.append(edge)
    return tuple(sorted(essential))


def context_record(ambient_side: int, child: dict[str, Any]) -> dict[str, Any]:
    context = routing.context_identity(
        ambient_side, child["sources"], child["targets"], child["deleted_edges"]
    )
    context.update({
        "source_child": child["source_child"],
        "target_child": child["target_child"],
        "prefix_depth": child["prefix_depth"],
        "matching_size": child["matching_size"],
    })
    context["child_context_sha256"] = digest(context)
    return context


def exact_mixed_deletion_manifest(
    p: int,
    h: int,
    x_raw: Iterable[int],
    y_raw: Iterable[int],
    deleted_raw: Iterable[Iterable[int]],
    routing_matching_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    product_manifest = factor.exact_factor_product_manifest(
        p, h, x_raw, y_raw, deleted_raw, routing_matching_raw
    )
    ambient_side = p ** h
    children = list(exact_children_from_manifest(product_manifest))
    initial_edge_stock = sum(
        child["matching_size"] ** 2 - len(child["deleted_edges"])
        for child in children
    )
    steps = []
    previous_active: set[Triple] | None = None
    terminal_kind = ""
    terminal_atom: Triple | None = None

    for step_index in range(initial_edge_stock + 1):
        child_tuple = tuple(children)
        families = child_families(child_tuple)
        require(all(families), "mixed-deletion product became infeasible")
        states = generated_product(families)
        active = mixed_triples(states, child_tuple)
        active_set = set(active)
        if previous_active is not None:
            require(active_set <= previous_active,
                    "edge deletion activated a new mixed atom")
        if not active:
            terminal_kind = "mixed-clean-product"
            break

        atom = active[0]
        box = occurrence_box(atom, child_tuple, families)
        direct_occurrences = tuple(state for state in states if set(atom) <= set(state))
        require(box == direct_occurrences and box,
                "active mixed-atom occurrence box mismatch")
        essential = essential_edges(atom, child_tuple, families)
        if set(essential) == set(atom):
            require(len(box) == len(states),
                    "essential mixed atom is not forced in every product state")
            terminal_kind = "forced-mixed-certificate"
            terminal_atom = atom
            break

        nonessential = tuple(sorted(set(atom) - set(essential)))
        edge = nonessential[0]
        child_index = edge_child_index(edge, child_tuple)
        before_child = context_record(ambient_side, child_tuple[child_index])
        before_states = states
        before_active = active

        child = copy.deepcopy(children[child_index])
        child["deleted_edges"] = tuple(sorted(set(child["deleted_edges"]) | {edge}))
        children[child_index] = child
        after_tuple = tuple(children)
        after_families = child_families(after_tuple)
        require(after_families[child_index],
                "nonessential deletion destroyed child matchability")
        after_states = generated_product(after_families)
        require(after_states, "nonessential deletion destroyed product matchability")
        require(not any(set(atom) <= set(state) for state in after_states),
                "selected mixed atom remains active after deleting its edge")
        after_active = mixed_triples(after_states, after_tuple)
        require(set(after_active) < set(before_active),
                "mixed deletion did not strictly decrease active atom set")
        after_child = context_record(ambient_side, after_tuple[child_index])

        step: dict[str, Any] = {
            "step_index": step_index,
            "transition_kind": "mixed-atom-nonessential-edge-deletion",
            "source_theorems": ["CMR677", "CMR678", "CMR679", "CMR680", "CMR2920"],
            "selected_atom": [list(edge) for edge in atom],
            "occurrence_states": len(box),
            "essential_atom_edges": [list(edge) for edge in essential],
            "deleted_nonessential_edge": list(edge),
            "child_index": child_index,
            "parent_child_context": before_child,
            "result_child_context": after_child,
            "parent_product_states": len(before_states),
            "result_product_states": len(after_states),
            "active_mixed_atoms_before": [
                [list(edge) for edge in triple] for triple in before_active
            ],
            "active_mixed_atoms_after": [
                [list(edge) for edge in triple] for triple in after_active
            ],
            "claims": {
                "active_atom_occurrence_box_exact": 1,
                "selected_edge_nonessential": 1,
                "child_matchability_preserved": 1,
                "product_matchability_preserved": 1,
                "selected_atom_deactivated": 1,
                "active_mixed_atom_set_strictly_decreased": 1,
                "single_edge_deletion_context_exact": 1,
            },
        }
        step["step_sha256"] = digest(step)
        steps.append(step)
        previous_active = set(after_active)
    else:
        raise MixedChildDeletionAncestryError("mixed deletion exceeded initial edge stock")

    require(terminal_kind in {"mixed-clean-product", "forced-mixed-certificate"},
            "mixed deletion has no terminal kind")
    require(len(steps) <= initial_edge_stock,
            "mixed deletion exceeds initial child-edge stock")
    final_children = tuple(children)
    final_families = child_families(final_children)
    final_states = generated_product(final_families)
    final_active = mixed_triples(final_states, final_children)
    if terminal_kind == "mixed-clean-product":
        require(not final_active, "mixed-clean terminal still has active mixed atom")
    else:
        require(terminal_atom is not None and terminal_atom in final_active,
                "forced terminal atom is not active")
        require(all(set(terminal_atom) <= set(state) for state in final_states),
                "forced terminal atom is absent from a product state")

    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "prime-power-mixed-child-deletion-ancestry-v1",
        "source_theorems": [
            "CMR677", "CMR678", "CMR679", "CMR680", "CMR681",
            "CMR2920", "CMR2921", "CMR2922",
        ],
        "parent_product_manifest_sha256": product_manifest["manifest_sha256"],
        "initial_child_edge_stock": initial_edge_stock,
        "deletion_steps": steps,
        "terminal_kind": terminal_kind,
        "forced_terminal_atom": (
            None if terminal_atom is None else [list(edge) for edge in terminal_atom]
        ),
        "final_child_contexts": [context_record(ambient_side, child)
                                 for child in final_children],
        "final_product_states": len(final_states),
        "final_active_mixed_atoms": [
            [list(edge) for edge in triple] for triple in final_active
        ],
        "claims": {
            "active_mixed_atom_criterion_exact": 1,
            "active_occurrence_box_exact": 1,
            "forced_or_nonessential_split_exact": 1,
            "mixed_atom_deletion_preserves_product": 1,
            "deletion_cannot_activate_mixed_atom": 1,
            "active_mixed_atom_set_monotone": 1,
            "mixed_deletion_edge_stock_bound_exact": 1,
            "mixed_clean_or_forced_terminal_exact": 1,
            "mixed_atom_deletion_ancestry_proved": 1,
            "forced_mixed_certificate_escape_proved": 0,
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
    expected = exact_mixed_deletion_manifest(*args)
    require(isinstance(manifest, dict) and manifest == expected,
            "mixed-child deletion manifest mismatch")
    return copy.deepcopy(expected["claims"])


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "prime-power-mixed-child-deletion-ancestry-v1",
        "source_theorems": [
            "CMR677", "CMR678", "CMR679", "CMR680", "CMR681",
            "CMR2920", "CMR2921", "CMR2922",
        ],
        "claims": {
            "active_mixed_atom_criterion_exact": 1,
            "active_occurrence_box_exact": 1,
            "forced_or_nonessential_split_exact": 1,
            "mixed_atom_deletion_preserves_product": 1,
            "deletion_cannot_activate_mixed_atom": 1,
            "active_mixed_atom_set_monotone": 1,
            "mixed_deletion_edge_stock_bound_exact": 1,
            "mixed_clean_or_forced_terminal_exact": 1,
            "mixed_atom_deletion_ancestry_proved": 1,
            "forced_mixed_certificate_escape_proved": 0,
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
    scenarios = deletion_steps = mixed_clean = forced = 0
    p, h = 2, 2
    x = y = (0, 1, 2, 3)
    family = routing.generate_factor_family(x, y, ())
    seen = set()
    for matching in family:
        beta = min(routing.delta(x, p, h), routing.delta(y, p, h))
        skeleton = routing.routing_skeleton(matching, x, y, p, beta)
        key = skeleton["routing_sha256"]
        if key in seen or len(skeleton["routing_cells"]) < 2:
            continue
        seen.add(key)
        manifest = exact_mixed_deletion_manifest(p, h, x, y, (), matching)
        scenarios += 1
        deletion_steps += len(manifest["deletion_steps"])
        mixed_clean += int(manifest["terminal_kind"] == "mixed-clean-product")
        forced += int(manifest["terminal_kind"] == "forced-mixed-certificate")

    require(scenarios > 0 and mixed_clean + forced == scenarios,
            "mixed deletion regression terminal census failed")
    return {
        "mixed_product_scenarios": scenarios,
        "mixed_atom_deletion_steps": deletion_steps,
        "mixed_clean_terminals": mixed_clean,
        "forced_mixed_certificate_terminals": forced,
    }


def mutation_tests() -> int:
    p, h = 2, 2
    x = y = (0, 1, 2, 3)
    matching = ((0, 0), (1, 1), (2, 2), (3, 3))
    good = exact_mixed_deletion_manifest(p, h, x, y, (), matching)
    bad_calls = [
        lambda: exact_mixed_deletion_manifest(p, h, (0,), (0,), (), ((0, 0),)),
        lambda: exact_mixed_deletion_manifest(p, h, x, y, ((0, 0),), matching),
    ]
    rejected = 0
    for call in bad_calls:
        try:
            call()
        except (ValueError, factor.FactorChildProductAncestryError,
                routing.RoutingChangeContextAncestryError):
            rejected += 1
        else:
            raise MixedChildDeletionAncestryError("malformed mixed product accepted")
    for field, value in (
        ("all_construction_ancestry_proved", 1),
        ("global_termination_proved", 1),
        ("mixed_atom_deletion_ancestry_proved", 0),
        ("forced_mixed_certificate_escape_proved", 1),
    ):
        bad = copy.deepcopy(good)
        bad["claims"][field] = value
        try:
            validate_manifest(bad, p, h, x, y, (), matching)
        except MixedChildDeletionAncestryError:
            rejected += 1
        else:
            raise MixedChildDeletionAncestryError("corrupted mixed manifest accepted")
    bad = copy.deepcopy(good)
    bad["manifest_sha256"] = "0" * 64
    try:
        validate_manifest(bad, p, h, x, y, (), matching)
    except MixedChildDeletionAncestryError:
        rejected += 1
    else:
        raise MixedChildDeletionAncestryError("bad mixed seal accepted")
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
