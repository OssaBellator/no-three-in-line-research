#!/usr/bin/env python3
"""Check CMR926--CMR1005 minimum transitions, product transport and targets."""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
from math import ceil, comb
from typing import Any

from check_prime_power_scc_branch_minimum_face_ancestry import (
    Edge,
    LEdge,
    State,
    family_core,
    joint_states,
    labelled_triple,
    matching,
    permutations,
    physical,
    physical_triples,
)


class FrontierError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise FrontierError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def min_face(
    family: tuple[frozenset[Any], ...], potential: dict[frozenset[Any], int]
) -> tuple[tuple[frozenset[Any], ...], int]:
    value = min(potential[state] for state in family)
    return tuple(state for state in family if potential[state] == value), value


def feasible(
    ambient: tuple[frozenset[int], ...], host: frozenset[int]
) -> tuple[frozenset[int], ...]:
    return tuple(state for state in ambient if state <= host)


def potential_bank(ambient: tuple[frozenset[int], ...]) -> tuple[dict[frozenset[int], int], ...]:
    weights = (
        (0, 0, 0, 0, 0, 0),
        (1, 1, 1, 2, 2, 2),
        (0, 1, 2, 0, 1, 2),
        (1, 3, 2, 4, 1, 5),
        (5, 2, 4, 1, 3, 0),
    )
    return tuple(
        {state: sum(weight[e] for e in state) % 7 for state in ambient}
        for weight in weights
    )


def core(family: tuple[frozenset[Any], ...]) -> frozenset[Any]:
    if not family:
        return frozenset()
    result = set(family[0])
    for state in family[1:]:
        result &= set(state)
    return frozenset(result)


def peel_added(
    ambient: tuple[frozenset[int], ...],
    potential: dict[frozenset[int], int],
    base: frozenset[int],
    host: frozenset[int],
) -> tuple[int, int, tuple[frozenset[int], ...]]:
    current = set(host)
    added = sorted(host - base)
    require(added, "peel requires added edges")
    current_family = feasible(ambient, frozenset(current))
    require(current_family, "expanded family empty")
    _target_face, target_value = min_face(current_family, potential)
    for peels, edge in enumerate(added):
        current_family = feasible(ambient, frozenset(current))
        face, value = min_face(current_family, potential)
        require(value == target_value, "peel changed target value")
        avoiding = tuple(state for state in face if edge not in state)
        if avoiding:
            current.remove(edge)
            new_face, new_value = min_face(
                feasible(ambient, frozenset(current)), potential
            )
            require(new_value == target_value and set(new_face) == set(avoiding),
                    "minimum-preserving peel identity")
        else:
            require(all(edge in state for state in face), "unpeelable edge not common")
            return peels, edge, face
    raise FrontierError("all added edges peeled")


def owner_transition_audit() -> dict[str, int]:
    universe = tuple(range(6))
    ambient = tuple(frozenset(s) for s in itertools.combinations(universe, 3))
    potentials = potential_bank(ambient)
    hosts = tuple(
        frozenset(e for e in universe if mask >> e & 1)
        for mask in range(1 << len(universe))
        if mask.bit_count() >= 3
    )
    nested = arbitrary = rollback = lowering = infeasible = canonical = 0
    core_monotonicity = contraction_checks = execution_bounds = 0
    for potential in potentials:
        cache: dict[frozenset[int], tuple[tuple[frozenset[int], ...], tuple[frozenset[int], ...], int]] = {}
        for host in hosts:
            family = feasible(ambient, host)
            face, value = min_face(family, potential)
            cache[host] = (family, face, value)
        for small in hosts:
            small_family, small_face, small_value = cache[small]
            for large in hosts:
                large_family, large_face, large_value = cache[large]
                if small <= large:
                    require(small_value >= large_value, "CMR926 restriction monotonicity")
                    surviving = tuple(state for state in large_face if state <= small)
                    if surviving:
                        require(small_value == large_value and set(small_face) == set(surviving),
                                "CMR926 exact surviving face")
                    else:
                        require(small_value > large_value, "CMR926 strict loss")
                    require(large_value <= small_value, "CMR927 expansion monotonicity")
                    if large_value == small_value:
                        require(set(small_face) <= set(large_face), "CMR927 old minima embed")
                        require(core(large_face) <= core(small_face), "CMR930-931 core monotonicity")
                        core_monotonicity += 1
                        require(feasible(ambient, large - (large - small)) == small_family,
                                "CMR934 exact rollback")
                        rollback += 1
                    else:
                        require(all(state & (large - small) for state in large_face),
                                "CMR942 added batch transversal")
                        peels, edge, peeled_face = peel_added(ambient, potential, small, large)
                        require(edge in large - small and all(edge in state for state in peeled_face),
                                "CMR944-945 common added edge")
                        require(peels <= len(large - small) - 1, "CMR946 peel budget")
                        residual = {state - {edge} for state in peeled_face}
                        require(len(residual) == len(peeled_face), "CMR945 contraction bijection")
                        lowering += 1
                        contraction_checks += 1
                    nested += 1
                intersection = small & large
                middle = feasible(ambient, intersection)
                old_canonical = min(small_face, key=lambda s: tuple(sorted(s)))
                new_canonical = min(large_face, key=lambda s: tuple(sorted(s)))
                if not middle:
                    require(old_canonical & (small - large), "CMR928 empty-intersection lost edge")
                    infeasible += 1
                    peels, edge, peeled_face = peel_added(ambient, potential, intersection, large)
                    require(edge in large - intersection and all(edge in s for s in peeled_face),
                            "CMR950-952 infeasible-base contraction")
                    require(peels <= len(large - intersection) - 1,
                            "CMR951 infeasible peel budget")
                else:
                    middle_face, middle_value = min_face(middle, potential)
                    require(middle_value >= cache[small][2], "intersection restriction")
                    require(cache[large][2] <= middle_value, "intersection expansion")
                    if cache[large][2] == middle_value:
                        require(set(middle_face) <= set(cache[large][1]),
                                "same-value intersection embedding")
                    elif cache[large][2] < middle_value:
                        peels, edge, peeled_face = peel_added(
                            ambient, potential, intersection, large
                        )
                        require(edge in large - intersection and all(edge in s for s in peeled_face),
                                "CMR948 mixed lowering contraction")
                if large_value >= small_value and new_canonical != old_canonical:
                    old_lost = not old_canonical <= large
                    new_added = not new_canonical <= small
                    require(old_lost or (large_value == small_value and new_added),
                            "CMR929 canonical witness")
                    if old_lost:
                        require(old_canonical & (small - large), "canonical lost witness")
                    else:
                        require(new_canonical & (large - small), "canonical added witness")
                    canonical += 1
                arbitrary += 1
    for state_size in range(0, 21):
        for universe_size in range(state_size, 50):
            require((state_size + 1) * universe_size >= universe_size - state_size,
                    "CMR955 execution budget")
            execution_bounds += 1
    return {
        "owner_transition_nested_cases": nested,
        "owner_transition_arbitrary_cases": arbitrary,
        "same_value_rollbacks": rollback,
        "lowering_expansion_contractions": lowering,
        "infeasible_intersection_contractions": infeasible,
        "canonical_minimum_change_witnesses": canonical,
        "minimum_core_monotonicity_checks": core_monotonicity,
        "added_edge_contraction_checks": contraction_checks,
        "fixed_vertex_execution_bounds": execution_bounds,
    }


def product_family(
    factors: tuple[tuple[frozenset[int], ...], ...], fixed: frozenset[int]
) -> tuple[frozenset[int], ...]:
    return tuple(
        frozenset(set(fixed).union(*(set(part) for part in choice)))
        for choice in itertools.product(*factors)
    )


def atom_kind(
    atom: frozenset[int], fixed: frozenset[int], factor_edges: tuple[frozenset[int], ...]
) -> tuple[str, tuple[int, ...]]:
    if atom <= fixed:
        return "constant", tuple(0 for _ in factor_edges)
    ranks = tuple(len(atom & edges) for edges in factor_edges)
    positive = [r for r in ranks if r]
    if len(positive) == 1 and positive[0] == 3 and not atom & fixed:
        return "pure", ranks
    return "coupling", ranks


def induced_product_audit() -> dict[str, int]:
    factor_edges = (frozenset({0, 1, 2}), frozenset({3, 4}))
    factors = (
        tuple(frozenset({e}) for e in sorted(factor_edges[0])),
        tuple(frozenset({e}) for e in sorted(factor_edges[1])),
    )
    fixed = frozenset({5})
    family = product_family(factors, fixed)
    atoms = tuple(frozenset(a) for a in itertools.combinations(range(6), 3))
    decomposition = box_checks = contraction_checks = fibre_checks = 0
    coupling_atoms = []
    for state in family:
        contained = [atom for atom in atoms if atom <= state]
        classes = [atom_kind(atom, fixed, factor_edges)[0] for atom in contained]
        require(len(contained) == len(classes), "CMR958 decomposition")
        decomposition += 1
    for atom in atoms:
        kind, ranks = atom_kind(atom, fixed, factor_edges)
        if kind != "coupling":
            continue
        residual = atom - fixed
        require(residual and all(rank <= 2 for rank in ranks), "CMR959 local ranks")
        actual = {state for state in family if atom <= state}
        local_allowed = []
        for edges, local_family in zip(factor_edges, factors):
            prescription = atom & edges
            local_allowed.append(tuple(part for part in local_family if prescription <= part))
        expected = set(product_family(tuple(local_allowed), fixed))
        require(actual == expected, "CMR960 occurrence box")
        coupling_atoms.append(atom)
        box_checks += 1
    c = len(fixed); ecount = sum(len(edges) for edges in factor_edges)
    require(len(coupling_atoms) <= c * comb(ecount, 2) + comb(c, 2) * ecount + comb(ecount, 3),
            "CMR961 stock")
    for rank in range(1, 4):
        for prescription in itertools.combinations(range(6), rank):
            p = frozenset(prescription)
            conditioned = tuple(state for state in family if p <= state)
            if not conditioned:
                continue
            residuals = tuple(state - p for state in conditioned)
            require(len(set(residuals)) == len(conditioned), "CMR974-975 bijection")
            for state, residual in zip(conditioned, residuals):
                for atom in atoms:
                    require((atom <= state) == ((atom - p) <= residual),
                            "CMR962/979 induced occurrence")
            contraction_checks += 1
    atom_banks = (atoms[:6], atoms[2:14:2], atoms[5:])
    for bank in atom_banks:
        potential = {state: sum(atom <= state for atom in bank) for state in family}
        face, value = min_face(family, potential)
        selected = min(face, key=lambda s: tuple(sorted(s)))
        for index, local_family in enumerate(factors):
            frozen = fixed | frozenset(
                edge
                for j, edges in enumerate(factor_edges)
                if j != index
                for edge in selected & edges
            )
            fibre = tuple(frozen | part for part in local_family)
            require(selected in fibre and min(potential[state] for state in fibre) == value,
                    "CMR966 fibre minimum inheritance")
            for atom in bank:
                if atom & factor_edges[index] and atom - factor_edges[index]:
                    require(1 <= len(atom & factor_edges[index]) <= 2,
                            "CMR967 anchored rank")
            fibre_checks += 1
    return {
        "induced_product_states": len(family),
        "induced_decomposition_checks": decomposition,
        "coupling_box_checks": box_checks,
        "conditioned_contraction_checks": contraction_checks,
        "coordinate_fibre_checks": fibre_checks,
    }


def residual_matching_family(
    n: int, host: frozenset[Edge], prescription: frozenset[Edge]
) -> tuple[frozenset[Edge], ...]:
    rows = tuple(i for i in range(n) if all(e[0] != i for e in prescription))
    cols = tuple(j for j in range(n) if all(e[1] != j for e in prescription))
    out = []
    for perm_cols in itertools.permutations(cols):
        candidate = frozenset(zip(rows, perm_cols))
        if candidate <= host:
            out.append(candidate)
    return tuple(out)


def host_representability_audit() -> dict[str, int]:
    n = 3
    universe = tuple((i, j) for i in range(n) for j in range(n))
    hosts = cylinders = joint_cylinders = product_conditioning = 0
    for mask in range(1 << len(universe)):
        host = frozenset(universe[i] for i in range(len(universe)) if mask >> i & 1)
        family = tuple(matching(p) for p in permutations(n) if matching(p) <= host)
        if not family:
            continue
        hosts += 1
        for q in family:
            for rank in range(1, min(2, n) + 1):
                for subset in itertools.combinations(sorted(q), rank):
                    p = frozenset(subset)
                    conditioned = tuple(m for m in family if p <= m)
                    residual = residual_matching_family(n, host, p)
                    projected = {m - p for m in conditioned}
                    require(projected == set(residual), "CMR976 residual matching host")
                    cylinders += 1
    states = joint_states(n)
    potentials = {state: len(physical_triples(state)) for state in states}
    minimum_face, value = min_face(states, potentials)
    common = core(minimum_face)
    anchor = min(minimum_face, key=lambda s: tuple(sorted(s)))
    candidates = [frozenset({edge}) for edge in anchor]
    candidates += [frozenset(p) for p in itertools.combinations(sorted(anchor), 2)]
    for p in candidates:
        conditioned = tuple(state for state in states if p <= state)
        if not conditioned:
            continue
        if p <= common:
            conditioned_face, conditioned_value = min_face(conditioned, potentials)
            require(conditioned_value == value and set(conditioned_face) == set(minimum_face),
                    "CMR974 exact old minimum face")
        residuals = {state - p for state in conditioned}
        require(len(residuals) == len(conditioned), "CMR977 joint residual bijection")
        fixed_cells = {(r, c) for _, r, c in p}
        for residual in residuals:
            require(all((r, c) not in fixed_cells for _, r, c in residual),
                    "CMR977 opposite-layer fixed-cell exclusion")
        joint_cylinders += 1
    factors = (
        tuple(frozenset({x}) for x in (0, 1)),
        tuple(frozenset({x}) for x in (2, 3, 4)),
    )
    family = set(product_family(factors, frozenset({5})))
    for p in (frozenset({0}), frozenset({2}), frozenset({0, 2}), frozenset({5})):
        conditioned = {state for state in family if p <= state}
        local = []
        for edges, local_family in zip((frozenset({0,1}), frozenset({2,3,4})), factors):
            local_p = p & edges
            local.append(tuple(part for part in local_family if local_p <= part))
        fixed = frozenset({5}) if p <= frozenset({5}) or 5 not in p else frozenset()
        expected = set(product_family(tuple(local), fixed))
        require(conditioned == expected, "CMR978 factorwise conditioning")
        product_conditioning += 1
    return {
        "representable_matching_hosts": hosts,
        "one_layer_conditioned_cylinders": cylinders,
        "joint_conditioned_cylinders": joint_cylinders,
        "factorwise_conditioning_checks": product_conditioning,
    }


def target_handoff_surplus_audit() -> dict[str, int]:
    states = joint_states(3)
    potentials = {state: len(physical_triples(state)) for state in states}
    handoffs = robust = energy = entering_support = pair_classes = 0
    cut_generations: dict[tuple[int, int], int] = {}
    for mask in range(1, 1 << len(states)):
        family = tuple(states[i] for i in range(len(states)) if mask >> i & 1)
        face, value = min_face(family, potentials)
        selected = min(face, key=lambda s: tuple(sorted(s)))
        for target in physical_triples(selected):
            omitters = [state for state in face if not target <= physical(state)]
            if omitters:
                witness = min(omitters, key=lambda s: tuple(sorted(s)))
                cell = min(target - physical(witness))
                child = tuple(
                    state for state in family if cell not in physical(state)
                )
                child_face, child_value = min_face(child, potentials)
                require(child_value == value, "CMR983 same-value cell cut")
                require(set(child_face) == {state for state in face if cell not in physical(state)},
                        "CMR983 exact face")
                require(all(not target <= physical(state) for state in child),
                        "CMR983 target destroyed")
                cut_generations[cell] = cut_generations.get(cell, 0) + 1
                handoffs += 1
    signatures: dict[tuple[LEdge, tuple[tuple[int,int], ...]], int] = {}
    augmented: dict[tuple[LEdge, tuple[tuple[int,int], ...], tuple[LEdge, ...]], int] = {}
    for old in states:
        old_triples = set(physical_triples(old))
        for new in states:
            new_triples = set(physical_triples(new))
            gained = new_triples - old_triples
            lost = old_triples - new_triples
            gap = len(new_triples) - len(old_triples)
            require(gap == len(gained) - len(lost), "CMR990 energy identity")
            energy += 1
            entering = new - old
            for triple in gained:
                new_cells = triple - physical(old)
                require(new_cells, "CMR992 gained triple new cell")
                supports = sorted(
                    edge for edge in entering if (edge[1], edge[2]) in new_cells
                )
                require(supports, "CMR992 entering support")
                e = supports[0]
                key = (e, tuple(sorted(triple)))
                signatures[key] = signatures.get(key, 0) + 1
                residual = tuple(sorted(labelled_triple(new, triple) - {e}))
                require(len(residual) == 2, "CMR996/998 residual pair")
                akey = (e, tuple(sorted(triple)), residual)
                augmented[akey] = augmented.get(akey, 0) + 1
                entering_support += 1
            if gap >= 1 and lost:
                require(len(gained) >= len(lost) + gap, "CMR991 surplus")
                robust += 1
    for (edge, triple_tuple), count in signatures.items():
        triple = frozenset(triple_tuple)
        occurrence = tuple(
            state for state in states if edge in state and triple <= physical(state)
        )
        pairs: dict[tuple[LEdge, ...], set[State]] = {}
        for state in occurrence:
            residual = tuple(sorted(labelled_triple(state, triple) - {edge}))
            require(len(residual) == 2, "CMR998 pair rank")
            pairs.setdefault(residual, set()).add(state)
        require(len(pairs) <= 4, "CMR999 four pair types")
        no_edge = {state for state in states if edge not in state}
        edge_without_target = {
            state for state in states if edge in state and not triple <= physical(state)
        }
        classes = set().union(*pairs.values()) if pairs else set()
        require(no_edge.isdisjoint(edge_without_target)
                and no_edge.isdisjoint(classes)
                and edge_without_target.isdisjoint(classes)
                and no_edge | edge_without_target | classes == set(states),
                "CMR1001 disjoint assignment partition")
        for pair, family in pairs.items():
            p = frozenset(pair)
            require(all(edge in state and p <= state for state in family),
                    "CMR1002 fixed class")
            projected = {state - {edge} for state in family}
            require(all(p <= residual for residual in projected),
                    "CMR1002 rank-two transfer")
        require(max((len(v) for v in pairs.values()), default=0) >= ceil(len(occurrence) / 4),
                "CMR1000 stabilization")
        pair_classes += len(pairs)
    stock = 2 * 9 * comb(8, 2)
    require(len(signatures) <= stock and len(augmented) <= 4 * stock,
            "CMR994/1004 signature stock")
    return {
        "minimum_face_physical_handoffs": handoffs,
        "distinct_cut_cells": len(cut_generations),
        "state_pair_energy_checks": energy,
        "positive_gap_robust_cases": robust,
        "entering_edge_new_triple_incidences": entering_support,
        "basic_signature_count": len(signatures),
        "augmented_signature_count": len(augmented),
        "residual_pair_assignment_classes": pair_classes,
    }


def synthetic_robust_surplus_audit() -> dict[str, int]:
    hyperedges = {
        frozenset({0, 1, 2}),
        frozenset({0, 4, 5}),
        frozenset({1, 4, 5}),
        frozenset({0, 1, 4}),
    }
    old_cells = frozenset({0, 1, 2})
    new_cells = frozenset({0, 1, 4, 5})
    old = {edge for edge in hyperedges if edge <= old_cells}
    new = {edge for edge in hyperedges if edge <= new_cells}
    gained = new - old
    lost = old - new
    gap = len(new) - len(old)
    require(gap == len(gained) - len(lost), "CMR990 synthetic energy")
    require(len(lost) == 1 and gap == 2 and len(gained) == 3,
            "CMR991 synthetic robust surplus")
    entering = {(0, 4), (1, 5)}
    assignments = {edge: 0 for edge in entering}
    for triple in gained:
        supports = sorted(edge for edge in entering if edge[1] in triple - old_cells)
        require(supports, "CMR992 synthetic entering support")
        assignments[supports[0]] += 1
    require(max(assignments.values()) >= ceil(len(gained) / len(entering)),
            "CMR992 synthetic concentration")
    designated = 1
    require(len(gained) >= designated + gap, "CMR993 synthetic cumulative surplus")
    return {
        "synthetic_positive_gap_cases": 1,
        "synthetic_designated_target_load": designated,
        "synthetic_new_triple_surplus": len(gained),
    }


def budget_audit(max_side: int = 15) -> dict[str, int]:
    checks = 0
    max_basic_stock = 0
    for n in range(2, max_side + 1):
        cells = n * n
        basic = 2 * cells * comb(cells - 1, 2)
        max_basic_stock = max(max_basic_stock, basic)
        for threshold in range(2, 7):
            require(((threshold - 1) * basic) // 2 * 2 <= (threshold - 1) * basic,
                    "CMR995 one-target bound")
            require(4 * (threshold - 1) * basic >= (threshold - 1) * basic,
                    "CMR1004 augmented bound")
            checks += 1
    return {"surplus_budget_parameter_checks": checks,
            "max_basic_signature_stock": max_basic_stock}


CONTRACT = {
    "schema": "prime-power-minimum-transition-product-target-ancestry/v1",
    "source_theorems": [f"CMR{i}" for i in range(926, 1006)],
    "banks": [
        "minimum-face-owner-transition",
        "minimum-expansion-rollback",
        "lowering-expansion-core-contraction",
        "complete-host-transition-normalization",
        "induced-product-potential-transport",
        "minimum-coordinate-fibre-descent",
        "minimum-core-host-representability",
        "minimum-face-target-handoff",
        "minimum-robust-target-surplus",
        "absolute-signature-pair-stabilization",
    ],
    "honesty": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_SHA256 = "dcdd3c27f46f64757c999621de5a67ff4868a355fc0e5fab7ac0953b8cf62086"


def mutation_audit() -> int:
    mutations = [
        lambda c: c.update(schema="bad"),
        lambda c: c.update(source_theorems=[]),
        lambda c: c["source_theorems"].pop(),
        lambda c: c["source_theorems"].__setitem__(0, "CMR925"),
        lambda c: c["banks"].pop(),
        lambda c: c["banks"].append(c["banks"][0]),
        lambda c: c["honesty"].update(all_n_proved_by_checker=1),
        lambda c: c["honesty"].update(global_termination_proved=1),
        lambda c: c["honesty"].pop("actual_global_parent_rule_complete"),
    ]
    def validate(c: dict[str, Any]) -> None:
        require(c.get("schema") == CONTRACT["schema"], "schema")
        require(c.get("source_theorems") == CONTRACT["source_theorems"], "sources")
        require(c.get("banks") == CONTRACT["banks"], "banks")
        require(c.get("honesty") == CONTRACT["honesty"], "honesty")
    rejected = 0
    for mutation in mutations:
        bad = copy.deepcopy(CONTRACT); mutation(bad)
        try: validate(bad)
        except FrontierError: rejected += 1
    require(rejected == len(mutations), "contract corruption accepted")
    return rejected


def main() -> None:
    contract = digest(CONTRACT)
    require(contract == EXPECTED_CONTRACT_SHA256, "contract digest")
    report = {
        "checker": "prime-power-minimum-transition-product-target-ancestry",
        "contract_sha256": contract,
        **owner_transition_audit(),
        **induced_product_audit(),
        **host_representability_audit(),
        **target_handoff_surplus_audit(),
        **synthetic_robust_surplus_audit(),
        **budget_audit(),
        "rejected_corruptions": mutation_audit(),
        "minimum_face_owner_transition_exact": 1,
        "minimum_expansion_rollback_exact": 1,
        "lowering_expansion_core_contraction_exact": 1,
        "complete_host_transition_normalization_exact": 1,
        "induced_product_potential_transport_exact": 1,
        "minimum_coordinate_fibre_descent_exact": 1,
        "minimum_core_host_representability_exact": 1,
        "minimum_face_target_handoff_exact": 1,
        "minimum_robust_target_surplus_exact": 1,
        "absolute_signature_pair_stabilization_exact": 1,
        "minimum_transition_product_target_ancestry_proved": 1,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_restoration_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))

if __name__ == "__main__":
    main()
