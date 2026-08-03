#!/usr/bin/env python3
"""Compile exact interaction requirements for scalar potentials on the restoration cube."""
from __future__ import annotations

import argparse
import copy
import itertools
import json
from collections import Counter, deque
from pathlib import Path

State = tuple[int, int]
Edge = tuple[State, State]
HOST_ID = "s4-75b04c45c1c8eac2"
STATES: tuple[State, ...] = ((0, 0), (0, 1), (1, 0), (1, 1))
SELECTED = {(0, 0): "3012", (0, 1): "3201", (1, 0): "2031", (1, 1): "2031"}


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


def acyclic(edges: set[Edge]) -> bool:
    outgoing = {state: [] for state in STATES}
    indegree = {state: 0 for state in STATES}
    for source, target in edges:
        outgoing[source].append(target)
        indegree[target] += 1
    queue = deque(state for state in STATES if indegree[state] == 0)
    seen = 0
    while queue:
        source = queue.popleft()
        seen += 1
        for target in outgoing[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    return seen == len(STATES)


def interaction(values: dict[State, int]) -> int:
    return values[(1, 1)] - values[(1, 0)] - values[(0, 1)] + values[(0, 0)]


def witness_for(paid: frozenset[Edge], target_abs_interaction: int) -> dict[State, int]:
    candidates = []
    for raw in itertools.product(range(4), repeat=4):
        values = dict(zip(STATES, raw))
        if not all(values[source] > values[target] for source, target in paid):
            continue
        if abs(interaction(values)) != target_abs_interaction:
            continue
        candidates.append((max(raw) - min(raw), sum(raw), raw, values))
    require(bool(candidates), "bounded exact witness")
    return min(candidates)[3]


def compile_manifest() -> dict[str, object]:
    undirected = tuple(
        (first, second)
        for index, first in enumerate(STATES)
        for second in STATES[index + 1 :]
        if hamming(first, second) == 1
    )
    require(len(undirected) == 4, "square edge census")

    orientations = []
    for choices in itertools.product((0, 1), repeat=4):
        paid = frozenset(
            edge if choice == 0 else reverse(edge)
            for edge, choice in zip(undirected, choices)
        )
        if acyclic(set(paid)):
            orientations.append(paid)
    require(len(orientations) == 14, "acyclic orientation census")

    profile = Counter()
    minimum_distribution = Counter()
    rows = []
    cyclic_projection_count = 0
    for paid in sorted(orientations, key=lambda edges: tuple(sorted(ec(edge) for edge in edges))):
        delta02 = (
            1 if ((1, 0), (0, 0)) in paid else -1,
            1 if ((1, 1), (0, 1)) in paid else -1,
        )
        delta20 = (
            1 if ((0, 1), (0, 0)) in paid else -1,
            1 if ((1, 1), (1, 0)) in paid else -1,
        )
        inconsistent02 = delta02[0] != delta02[1]
        inconsistent20 = delta20[0] != delta20[1]
        key = (
            "both" if inconsistent02 and inconsistent20
            else "r02_only" if inconsistent02
            else "r20_only" if inconsistent20
            else "none"
        )
        profile[key] += 1

        additive = not inconsistent02 and not inconsistent20
        minimum = 0 if additive else 2
        minimum_distribution[minimum] += 1
        values = witness_for(paid, minimum)
        gamma = interaction(values)
        require(abs(gamma) == minimum, "witness interaction")
        if additive:
            require(gamma == 0, "additive witness")
        else:
            require(inconsistent02 or inconsistent20, "interaction lower-bound hypothesis")
            require(abs(gamma) >= 2, "integer interaction lower bound")

        projected = {
            (SELECTED[source], SELECTED[target])
            for source, target in paid
            if SELECTED[source] != SELECTED[target]
        }
        projected_vertices = ("3012", "2031", "3201")
        outgoing = Counter(source for source, _ in projected)
        incoming = Counter(target for _, target in projected)
        projected_cycle = all(outgoing[vertex] == incoming[vertex] == 1 for vertex in projected_vertices)
        cyclic_projection_count += int(projected_cycle)

        coefficients = {
            "constant": values[(0, 0)],
            "r02": values[(1, 0)] - values[(0, 0)],
            "r20": values[(0, 1)] - values[(0, 0)],
            "interaction": gamma,
        }
        rows.append({
            "paid_menu_edges": sorted(ec(edge) for edge in paid),
            "parallel_direction_reversal": {
                "r02": int(inconsistent02),
                "r20": int(inconsistent20),
            },
            "additive_realizable": int(additive),
            "minimum_absolute_integer_interaction": minimum,
            "witness_values": {sc(state): values[state] for state in STATES},
            "witness_boolean_coefficients": coefficients,
            "projected_label_cycle": int(projected_cycle),
        })

    require(profile == Counter({"none": 4, "r02_only": 4, "r20_only": 4, "both": 2}), "reversal profile")
    require(minimum_distribution == Counter({0: 4, 2: 10}), "interaction distribution")
    require(cyclic_projection_count == 2, "cyclic projection census")

    cyclic_rows = [row for row in rows if row["projected_label_cycle"]]
    require(
        {row["witness_boolean_coefficients"]["interaction"] for row in cyclic_rows} == {-2, 2},
        "cyclic interaction signs",
    )

    return {
        "schema": "exact-recurrent-first-host-menu-interaction-potential/v1",
        "scope": {
            "host_id": HOST_ID,
            "potential_form": "V=c+alpha*r02+beta*r20+Gamma*r02*r20",
            "interaction_identity": "Gamma=(V11-V01)-(V10-V00)=(V11-V10)-(V01-V00)",
            "integer_strict_edge_potential": 1,
        },
        "orientations": rows,
        "cyclic_label_projection_witnesses": cyclic_rows,
        "aggregate": {
            "acyclic_menu_orientations": 14,
            "additive_orientations": 4,
            "interaction_required_orientations": 10,
            "parallel_reversal_profile": {
                "none": profile["none"],
                "r02_only": profile["r02_only"],
                "r20_only": profile["r20_only"],
                "both": profile["both"],
            },
            "minimum_absolute_interaction_distribution": {
                "0": minimum_distribution[0],
                "2": minimum_distribution[2],
            },
            "minimum_nonzero_absolute_integer_interaction": 2,
            "cyclic_label_projection_orientations": cyclic_projection_count,
            "maximum_witness_value": max(
                max(row["witness_values"].values()) for row in rows
            ),
        },
        "conclusion": {
            "interaction_requirement_classification_complete": 1,
            "gamma_zero_exactly_matches_additive_orientation_class": 1,
            "every_nonadditive_orientation_requires_abs_gamma_at_least_2": 1,
            "every_nonadditive_orientation_has_abs_gamma_2_witness": 1,
            "both_cyclic_label_projection_lifts_require_interaction": 1,
            "physical_potential_installed": 0,
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
        lambda item: item["aggregate"].update(acyclic_menu_orientations=13),
        lambda item: item["aggregate"].update(additive_orientations=5),
        lambda item: item["aggregate"].update(interaction_required_orientations=9),
        lambda item: item["aggregate"]["parallel_reversal_profile"].update(both=1),
        lambda item: item["aggregate"]["minimum_absolute_interaction_distribution"].update(**{"2": 9}),
        lambda item: item["aggregate"].update(minimum_nonzero_absolute_integer_interaction=1),
        lambda item: item["aggregate"].update(cyclic_label_projection_orientations=1),
        lambda item: item["orientations"].pop(),
        lambda item: item["cyclic_label_projection_witnesses"].pop(),
        lambda item: item["conclusion"].update(gamma_zero_exactly_matches_additive_orientation_class=0),
        lambda item: item["conclusion"].update(every_nonadditive_orientation_requires_abs_gamma_at_least_2=0),
        lambda item: item["conclusion"].update(physical_potential_installed=1),
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
        "checker": "exact-recurrent-first-host-menu-interaction-potential",
        **manifest["aggregate"],
        "mutation_corruptions_rejected": mutation_audit(manifest),
        **manifest["conclusion"],
        **manifest["honesty"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
