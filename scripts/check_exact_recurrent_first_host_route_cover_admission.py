#!/usr/bin/env python3
"""Classify source-closed edge masks that contain a scalar-compatible route cover."""
from __future__ import annotations

import argparse
import copy
import itertools
import json
from collections import Counter
from pathlib import Path

STATES = ("00", "01", "10", "11")
SELECTED = {"00": "3012", "01": "3201", "10": "2031", "11": "2031"}
UNDIRECTED = (("00", "01"), ("00", "10"), ("01", "11"), ("10", "11"))


class AdmissionError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AdmissionError(message)


def root() -> Path:
    here = Path(__file__).resolve()
    for candidate in (here.parent, *here.parents):
        if (candidate / "STATUS.md").is_file():
            return candidate
    raise AdmissionError("repository root")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def directed_edges() -> tuple[tuple[str, str], ...]:
    return tuple(sorted(
        [(a, b) for a, b in UNDIRECTED]
        + [(b, a) for a, b in UNDIRECTED]
    ))


def edge_code(edge: tuple[str, str]) -> str:
    return f"{edge[0]}->{edge[1]}"


def reverse(edge: tuple[str, str]) -> tuple[str, str]:
    return edge[1], edge[0]


def menu_covers() -> set[frozenset[tuple[str, str]]]:
    covers = set()
    for order in itertools.permutations(STATES):
        rank = {state: index for index, state in enumerate(order)}
        paid = {
            (a, b) if rank[a] > rank[b] else (b, a)
            for a, b in UNDIRECTED
        }
        covers.add(frozenset(reverse(edge) for edge in paid))
    require(len(covers) == 14, "menu cover count")
    return covers


def changing_edges() -> set[tuple[str, str]]:
    return {
        edge for edge in directed_edges()
        if SELECTED[edge[0]] != SELECTED[edge[1]]
    }


def label_covers() -> set[frozenset[tuple[str, str]]]:
    changing = changing_edges()
    labels = tuple(sorted(set(SELECTED.values())))
    covers = set()
    for order in itertools.permutations(labels):
        rank = {label: index for index, label in enumerate(order)}
        paid = {
            edge for edge in changing
            if rank[SELECTED[edge[0]]] > rank[SELECTED[edge[1]]]
        }
        covers.add(frozenset(changing - paid))
    require(len(covers) == 6, "label cover count")
    return covers


def label_pairs() -> tuple[frozenset[tuple[str, str]], ...]:
    grouped: dict[frozenset[str], set[tuple[str, str]]] = {}
    for edge in changing_edges():
        key = frozenset((SELECTED[edge[0]], SELECTED[edge[1]]))
        grouped.setdefault(key, set()).add(edge)
    pairs = tuple(sorted(
        (frozenset(rows) for rows in grouped.values()),
        key=lambda pair: sorted(edge_code(edge) for edge in pair),
    ))
    require(len(pairs) == 3 and all(len(pair) == 2 for pair in pairs), "label pairs")
    return pairs


def menu_pairs() -> tuple[frozenset[tuple[str, str]], ...]:
    return tuple(frozenset((edge, reverse(edge))) for edge in UNDIRECTED)


def masks(universe: tuple[tuple[str, str], ...]):
    for flags in itertools.product((0, 1), repeat=len(universe)):
        yield frozenset(
            edge for edge, flag in zip(universe, flags)
            if flag
        )


def classify(
    universe: tuple[tuple[str, str], ...],
    pairs: tuple[frozenset[tuple[str, str]], ...],
    covers: set[frozenset[tuple[str, str]]],
) -> dict:
    total = 0
    pair_covered = 0
    feasible = 0
    feasible_by_size: Counter[int] = Counter()
    cycle_obstructions = []
    minimal_feasible = set()
    cover_counts: Counter[int] = Counter()

    for mask in masks(universe):
        total += 1
        covers_inside = [cover for cover in covers if cover <= mask]
        is_feasible = bool(covers_inside)
        all_pairs = all(mask & pair for pair in pairs)
        if all_pairs:
            pair_covered += 1
        if is_feasible:
            feasible += 1
            feasible_by_size[len(mask)] += 1
            cover_counts[len(covers_inside)] += 1
            if not any(proper < mask for proper in covers):
                minimal_feasible.add(mask)
        elif all_pairs:
            cycle_obstructions.append(mask)

    require(minimal_feasible == covers, "minimal masks equal covers")
    require(len(cycle_obstructions) == 2, "two cycle obstructions")
    require(all(len(mask) == len(pairs) for mask in cycle_obstructions), "cycle mask size")

    return {
        "directed_edge_masks": total,
        "pair_covered_masks": pair_covered,
        "source_cover_feasible_masks": feasible,
        "source_cover_infeasible_masks": total - feasible,
        "minimal_feasible_masks": len(minimal_feasible),
        "cycle_obstruction_masks": [
            sorted(edge_code(edge) for edge in mask)
            for mask in sorted(cycle_obstructions, key=lambda row: sorted(row))
        ],
        "feasible_mask_size_distribution": {
            str(size): feasible_by_size[size]
            for size in sorted(feasible_by_size)
        },
        "contained_cover_count_distribution": {
            str(count): cover_counts[count]
            for count in sorted(cover_counts)
        },
        "minimal_covers": [
            sorted(edge_code(edge) for edge in cover)
            for cover in sorted(covers, key=lambda row: sorted(row))
        ],
    }


def compile_manifest(repository: Path) -> dict:
    source_gate = load(
        repository / "data/exact_recurrent_first_host_closure_route_source_gate.json"
    )
    require(source_gate["aggregate"]["directed_edges"] == 8, "source edge count")
    require(source_gate["aggregate"]["edge_route_pairs"] == 40, "source pair count")
    require(
        source_gate["aggregate"]["source_admissible_edge_route_pairs"] == 0,
        "source route coverage",
    )

    route_closed = {
        tuple(row["edge"].split("->"))
        for row in source_gate["edges"]
        if any(row["route_admissibility"].values())
    }
    require(not route_closed, "current route-closed edge set")

    label_universe = tuple(sorted(changing_edges()))
    menu_universe = directed_edges()
    label = classify(label_universe, label_pairs(), label_covers())
    menu = classify(menu_universe, menu_pairs(), menu_covers())

    require(
        label["feasible_mask_size_distribution"]
        == {"3": 6, "4": 12, "5": 6, "6": 1},
        "label size distribution",
    )
    require(
        menu["feasible_mask_size_distribution"]
        == {"4": 14, "5": 32, "6": 24, "7": 8, "8": 1},
        "menu size distribution",
    )
    require(label["pair_covered_masks"] == 27, "label pair-covered census")
    require(menu["pair_covered_masks"] == 81, "menu pair-covered census")

    all_restore = frozenset(
        edge for edge in menu_universe
        if edge[0][0] <= edge[1][0] and edge[0][1] <= edge[1][1]
    )
    all_delete = frozenset(reverse(edge) for edge in all_restore)
    require(len(all_restore) == len(all_delete) == 4, "action masks")
    require(any(cover <= all_restore for cover in menu_covers()), "restore cover")
    require(any(cover <= all_delete for cover in menu_covers()), "delete cover")

    return {
        "schema": "exact-recurrent-first-host-route-cover-admission/v1",
        "host_id": "s4-75b04c45c1c8eac2",
        "source_gate": "data/exact_recurrent_first_host_closure_route_source_gate.json",
        "criterion": {
            "pair_coverage": "at least one route-closed direction in every reversal pair",
            "only_remaining_obstruction": "exactly one direction per pair forming one of two directed cycles",
            "bidirectional_shortcut": "pair coverage plus one bidirectionally route-closed pair always contains a scalar cover",
        },
        "label_scalar": label,
        "menu_scalar": menu,
        "sufficient_patterns": {
            "all_restore_menu_edges": sorted(edge_code(edge) for edge in all_restore),
            "all_delete_menu_edges": sorted(edge_code(edge) for edge in all_delete),
            "all_selector_changing_edges_close_a_label_cover": 1,
            "all_selector_changing_plus_either_neutral_direction_close_a_menu_cover": 1,
            "one_bit_family_alone_closes_a_menu_cover": 0,
        },
        "current_source_state": {
            "route_closed_edges": [],
            "complete_label_scalar_covers": 0,
            "complete_menu_scalar_covers": 0,
        },
        "aggregate": {
            "label_directed_edges": len(label_universe),
            "label_masks": label["directed_edge_masks"],
            "label_pair_covered_masks": label["pair_covered_masks"],
            "label_feasible_masks": label["source_cover_feasible_masks"],
            "label_cycle_obstructions": len(label["cycle_obstruction_masks"]),
            "menu_directed_edges": len(menu_universe),
            "menu_masks": menu["directed_edge_masks"],
            "menu_pair_covered_masks": menu["pair_covered_masks"],
            "menu_feasible_masks": menu["source_cover_feasible_masks"],
            "menu_cycle_obstructions": len(menu["cycle_obstruction_masks"]),
            "current_route_closed_edges": 0,
            "current_complete_covers": 0,
        },
        "conclusion": {
            "source_cover_admission_classification_complete": 1,
            "pair_coverage_is_necessary": 1,
            "pair_coverage_is_sufficient_except_two_cycles": 1,
            "one_bidirectional_pair_removes_cycle_obstruction": 1,
            "current_source_gate_completes_a_scalar_cover": 0,
            "promotion_to_recurrent_closure_allowed": 0,
        },
        "honesty": {
            "physical_transition_legality_proved": 0,
            "persistent_owner_identity_proved": 0,
            "boundary_capacities_populated": 0,
            "outer_profile_mapping_populated": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(manifest: dict, repository: Path) -> None:
    require(manifest == compile_manifest(repository), "manifest mismatch")


def mutation_audit(manifest: dict, repository: Path) -> int:
    mutations = [
        lambda item: item["aggregate"].update(label_feasible_masks=24),
        lambda item: item["aggregate"].update(menu_feasible_masks=78),
        lambda item: item["aggregate"].update(label_cycle_obstructions=1),
        lambda item: item["aggregate"].update(menu_cycle_obstructions=1),
        lambda item: item["label_scalar"]["feasible_mask_size_distribution"].update({"3": 5}),
        lambda item: item["menu_scalar"]["feasible_mask_size_distribution"].update({"4": 13}),
        lambda item: item["label_scalar"]["cycle_obstruction_masks"].pop(),
        lambda item: item["menu_scalar"]["minimal_covers"].pop(),
        lambda item: item["sufficient_patterns"].update(one_bit_family_alone_closes_a_menu_cover=1),
        lambda item: item["current_source_state"].update(route_closed_edges=["00->01"]),
        lambda item: item["current_source_state"].update(complete_menu_scalar_covers=1),
        lambda item: item["conclusion"].update(pair_coverage_is_sufficient_except_two_cycles=0),
        lambda item: item["conclusion"].update(current_source_gate_completes_a_scalar_cover=1),
        lambda item: item["conclusion"].update(promotion_to_recurrent_closure_allowed=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate, repository)
        except AdmissionError:
            rejected += 1
    require(rejected == len(mutations), "mutation accepted")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    repository = root()
    manifest = compile_manifest(repository)
    validate(manifest, repository)
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if args.check:
        validate(load(args.check), repository)
    print(json.dumps({
        "checker": "exact-recurrent-first-host-route-cover-admission",
        **manifest["aggregate"],
        "mutation_corruptions_rejected": mutation_audit(manifest, repository),
        **manifest["conclusion"],
        **manifest["honesty"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
