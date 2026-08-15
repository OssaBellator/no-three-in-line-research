#!/usr/bin/env python3
"""Compile exact scalar route covers for the first-host restoration cube."""
from __future__ import annotations

import argparse
import copy
import itertools
import json
from collections import Counter, defaultdict, deque
from pathlib import Path

State = tuple[int, int]
Edge = tuple[State, State]
HOST_ID = "s4-75b04c45c1c8eac2"
STATES: tuple[State, ...] = ((0, 0), (0, 1), (1, 0), (1, 1))
LABELS = ("3012", "2031", "3201")
SELECTED = {(0, 0): "3012", (0, 1): "3201", (1, 0): "2031", (1, 1): "2031"}
MENUS = {(0, 0): "blocked", (0, 1): "restore_20", (1, 0): "restore_02", (1, 1): "restore_both"}


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def sc(state: State) -> str:
    return f"{state[0]}{state[1]}"


def ec(edge: Edge) -> str:
    return f"{sc(edge[0])}->{sc(edge[1])}"


def reverse(edge: Edge) -> Edge:
    return edge[1], edge[0]


def hamming(first: State, second: State) -> int:
    return sum(a != b for a, b in zip(first, second))


def bit(edge: Edge) -> str:
    require(hamming(*edge) == 1, "single-bit edge")
    return "r02" if edge[0][0] != edge[1][0] else "r20"


def direction(edge: Edge) -> str:
    index = 0 if bit(edge) == "r02" else 1
    return "restore" if edge[0][index] == 0 else "delete"


def acyclic(vertices: tuple[object, ...], edges: set[tuple[object, object]]) -> bool:
    outgoing = {vertex: [] for vertex in vertices}
    indegree = {vertex: 0 for vertex in vertices}
    for source, target in edges:
        outgoing[source].append(target)
        indegree[target] += 1
    queue = deque(vertex for vertex in vertices if indegree[vertex] == 0)
    seen = 0
    while queue:
        source = queue.popleft()
        seen += 1
        for target in outgoing[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    return seen == len(vertices)


def paid_from_order(order: tuple[State, ...], undirected: tuple[Edge, ...]) -> frozenset[Edge]:
    rank = {state: index for index, state in enumerate(order)}
    return frozenset(
        (first, second) if rank[first] > rank[second] else (second, first)
        for first, second in undirected
    )


def compile_manifest() -> dict[str, object]:
    undirected = tuple(
        (first, second)
        for index, first in enumerate(STATES)
        for second in STATES[index + 1 :]
        if hamming(first, second) == 1
    )
    directed = {orientation for edge in undirected for orientation in (edge, reverse(edge))}
    changing = {edge for edge in directed if SELECTED[edge[0]] != SELECTED[edge[1]]}
    neutral = directed - changing
    require((len(undirected), len(directed), len(changing), len(neutral)) == (4, 8, 6, 2), "cube census")

    label_orders = []
    label_paid_sets: set[frozenset[Edge]] = set()
    for order in itertools.permutations(LABELS):
        rank = {label: index for index, label in enumerate(order)}
        paid = frozenset(
            edge for edge in changing
            if rank[SELECTED[edge[0]]] > rank[SELECTED[edge[1]]]
        )
        residual = frozenset(changing - set(paid))
        require(len(paid) == len(residual) == 3, "label split")
        require(Counter(bit(edge) for edge in residual) == Counter({"r02": 2, "r20": 1}), "label bit split")
        label_paid_sets.add(paid)
        label_orders.append({
            "low_to_high": list(order),
            "paid": sorted(ec(edge) for edge in paid),
            "external_routes": sorted(ec(edge) for edge in residual),
        })
    require(len(label_paid_sets) == 6, "label orientations")

    pair_groups: dict[frozenset[str], list[Edge]] = defaultdict(list)
    for edge in changing:
        pair_groups[frozenset((SELECTED[edge[0]], SELECTED[edge[1]]))].append(edge)
    groups = [tuple(sorted(rows, key=ec)) for _, rows in sorted(pair_groups.items(), key=lambda row: sorted(row[0]))]
    label_choices = {
        frozenset(groups[index][choice] for index, choice in enumerate(bits))
        for bits in itertools.product((0, 1), repeat=3)
    }
    label_compatible = {frozenset(changing - set(paid)) for paid in label_paid_sets}
    require((len(label_choices), len(label_compatible), len(label_choices - label_compatible)) == (8, 6, 2), "label covers")

    menu_orientations: dict[frozenset[Edge], list[tuple[State, ...]]] = defaultdict(list)
    for order in itertools.permutations(STATES):
        menu_orientations[paid_from_order(order, undirected)].append(order)
    require(len(menu_orientations) == 14 and sum(map(len, menu_orientations.values())) == 24, "menu orientations")

    projection_counts: Counter[tuple[str, ...]] = Counter()
    restore_distribution: Counter[int] = Counter()
    cyclic_lifts = []
    for paid, orders in menu_orientations.items():
        residual = frozenset(reverse(edge) for edge in paid)
        paid_changing = {edge for edge in paid if edge in changing}
        residual_changing = {edge for edge in residual if edge in changing}
        require((len(paid_changing), len(residual_changing)) == (3, 3), "menu changing split")
        require(sum(edge in neutral for edge in residual) == 1, "menu neutral route")
        require(Counter(bit(edge) for edge in residual) == Counter({"r02": 2, "r20": 2}), "menu bit split")
        projected = {(SELECTED[edge[0]], SELECTED[edge[1]]) for edge in paid_changing}
        key = tuple(sorted(f"{source}->{target}" for source, target in projected))
        projection_counts[key] += 1
        restore_distribution[sum(direction(edge) == "restore" for edge in paid)] += 1
        if not acyclic(LABELS, projected):
            cyclic_lifts.append({
                "paid_menu_edges": sorted(ec(edge) for edge in paid),
                "external_route_edges": sorted(ec(edge) for edge in residual),
                "low_to_high_orders": [[sc(state) for state in order] for order in sorted(orders)],
                "projected_label_cycle": list(key),
            })
    require(Counter(projection_counts.values()) == Counter({2: 6, 1: 2}), "projection multiplicities")
    require(len(cyclic_lifts) == 2, "cyclic lifts")
    require(restore_distribution == Counter({0: 1, 1: 4, 2: 4, 3: 4, 4: 1}), "restore distribution")

    menu_choices = {
        frozenset(edge if choice == 0 else reverse(edge) for edge, choice in zip(undirected, bits))
        for bits in itertools.product((0, 1), repeat=4)
    }
    menu_compatible = {frozenset(reverse(edge) for edge in paid) for paid in menu_orientations}
    require((len(menu_choices), len(menu_compatible), len(menu_choices - menu_compatible)) == (16, 14, 2), "menu covers")

    additive = []
    additive_paid: set[frozenset[Edge]] = set()
    for coefficient_r02, coefficient_r20 in itertools.product((-1, 1), repeat=2):
        value = {state: coefficient_r02 * state[0] + coefficient_r20 * state[1] for state in STATES}
        paid = frozenset(
            (first, second) if value[first] > value[second] else (second, first)
            for first, second in undirected
        )
        additive_paid.add(paid)
        projected = {
            (SELECTED[edge[0]], SELECTED[edge[1]])
            for edge in paid if edge in changing
        }
        require(paid in menu_orientations and acyclic(LABELS, projected), "additive orientation")
        additive.append({
            "coefficient_signs": {"r02": coefficient_r02, "r20": coefficient_r20},
            "paid_menu_edges": sorted(ec(edge) for edge in paid),
            "external_route_edges": sorted(ec(reverse(edge)) for edge in paid),
        })
    require(len(additive_paid) == 4, "additive orientation census")

    return {
        "schema": "exact-recurrent-first-host-scalar-route-cover/v1",
        "scope": {
            "host_id": HOST_ID,
            "descent_convention": "paid iff potential(source) > potential(target)",
            "states": [
                {"state": sc(state), "menu": MENUS[state], "selected_response": SELECTED[state]}
                for state in STATES
            ],
        },
        "selected_label_scalar_orders": label_orders,
        "cyclic_label_projection_menu_lifts": sorted(cyclic_lifts, key=lambda row: row["paid_menu_edges"]),
        "additive_bit_potentials": additive,
        "aggregate": {
            "selected_label_total_orders": 6,
            "selected_label_scalar_compatible_route_covers": 6,
            "selected_label_one_per_pair_route_choices": 8,
            "selected_label_cyclic_incompatible_route_covers": 2,
            "selected_label_paid_edges": 3,
            "selected_label_minimum_external_routes": 3,
            "residual_selector_routes_flipping_r02": 2,
            "residual_selector_routes_flipping_r20": 1,
            "menu_total_orders": 24,
            "distinct_menu_scalar_orientations": 14,
            "menu_scalar_compatible_route_covers": 14,
            "menu_one_per_pair_route_choices": 16,
            "menu_cyclic_incompatible_route_covers": 2,
            "menu_paid_edges": 4,
            "menu_minimum_external_routes": 4,
            "residual_menu_routes_selector_changing": 3,
            "residual_menu_routes_selector_neutral": 1,
            "residual_menu_routes_flipping_r02": 2,
            "residual_menu_routes_flipping_r20": 2,
            "distinct_projected_label_tournaments": 8,
            "menu_orientations_with_transitive_label_projection": 12,
            "menu_orientations_with_cyclic_label_projection": 2,
            "additive_bit_potential_orientations": 4,
            "arbitrary_menu_scalar_orientations": 14,
            "restore_paid_orientation_distribution": {str(key): restore_distribution[key] for key in range(5)},
        },
        "conclusion": {
            "label_scalar_route_cover_classification_complete": 1,
            "menu_scalar_route_cover_classification_complete": 1,
            "menu_refinement_increases_maximum_paid_selector_edges": 0,
            "menu_refinement_expands_paid_selector_patterns_from_6_to_8": 1,
            "two_cyclic_label_tournaments_lift_to_acyclic_menu_orders": 1,
            "additive_bit_potentials_realize_all_menu_scalar_patterns": 0,
            "interaction_sensitive_menu_state_needed_for_cyclic_projection": 1,
            "physical_route_assignment_proved": 0,
            "promotion_to_recurrent_closure_allowed": 0,
        },
        "honesty": {
            "physical_chart_confinement_proved": 0,
            "physical_occurrence_coverage_proved": 0,
            "physical_transition_legality_proved": 0,
            "persistent_owner_identity_proved": 0,
            "boundary_capacities_populated": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(manifest: dict[str, object]) -> None:
    require(manifest == compile_manifest(), "manifest differs from compiler")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(selected_label_scalar_compatible_route_covers=5),
        lambda item: item["aggregate"].update(residual_selector_routes_flipping_r02=1),
        lambda item: item["aggregate"].update(distinct_menu_scalar_orientations=13),
        lambda item: item["aggregate"].update(menu_scalar_compatible_route_covers=13),
        lambda item: item["aggregate"].update(residual_menu_routes_selector_neutral=0),
        lambda item: item["aggregate"].update(distinct_projected_label_tournaments=7),
        lambda item: item["aggregate"].update(menu_orientations_with_cyclic_label_projection=1),
        lambda item: item["aggregate"].update(additive_bit_potential_orientations=5),
        lambda item: item["selected_label_scalar_orders"].pop(),
        lambda item: item["cyclic_label_projection_menu_lifts"].pop(),
        lambda item: item["conclusion"].update(menu_refinement_increases_maximum_paid_selector_edges=1),
        lambda item: item["conclusion"].update(additive_bit_potentials_realize_all_menu_scalar_patterns=1),
        lambda item: item["conclusion"].update(physical_route_assignment_proved=1),
        lambda item: item["conclusion"].update(promotion_to_recurrent_closure_allowed=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate)
        except (AuditError, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "mutation audit")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    arguments = parser.parse_args()
    manifest = compile_manifest()
    if arguments.write:
        arguments.write.parent.mkdir(parents=True, exist_ok=True)
        arguments.write.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if arguments.check:
        validate(json.loads(arguments.check.read_text(encoding="utf-8")))
    print(json.dumps({
        "checker": "exact-recurrent-first-host-scalar-route-cover",
        **manifest["aggregate"],
        "mutation_corruptions_rejected": mutation_audit(manifest),
        **manifest["conclusion"],
        **manifest["honesty"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
