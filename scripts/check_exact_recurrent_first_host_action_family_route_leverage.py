#!/usr/bin/env python3
"""Classify source-closed action families for the first residual host."""
from __future__ import annotations

import argparse
import copy
import itertools
import json
from pathlib import Path

STATES = ("00", "01", "10", "11")
SELECTED = {"00": "3012", "01": "3201", "10": "2031", "11": "2031"}
UNDIRECTED = (("00", "01"), ("00", "10"), ("01", "11"), ("10", "11"))
FAMILIES = {
    "restore_02": (("00", "10"), ("01", "11")),
    "delete_02": (("10", "00"), ("11", "01")),
    "restore_20": (("00", "01"), ("10", "11")),
    "delete_20": (("01", "00"), ("11", "10")),
}


class FamilyError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise FamilyError(message)


def root() -> Path:
    here = Path(__file__).resolve()
    for candidate in (here.parent, *here.parents):
        if (candidate / "STATUS.md").is_file():
            return candidate
    raise FamilyError("repository root")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def edge_code(edge: tuple[str, str]) -> str:
    return f"{edge[0]}->{edge[1]}"


def directed_edges() -> tuple[tuple[str, str], ...]:
    return tuple(sorted(
        [(a, b) for a, b in UNDIRECTED]
        + [(b, a) for a, b in UNDIRECTED]
    ))


def menu_covers() -> set[frozenset[tuple[str, str]]]:
    covers = set()
    for order in itertools.permutations(STATES):
        rank = {state: index for index, state in enumerate(order)}
        paid = {
            (a, b) if rank[a] > rank[b] else (b, a)
            for a, b in UNDIRECTED
        }
        covers.add(frozenset((b, a) for a, b in paid))
    require(len(covers) == 14, "menu covers")
    return covers


def label_covers() -> set[frozenset[tuple[str, str]]]:
    changing = {
        edge for edge in directed_edges()
        if SELECTED[edge[0]] != SELECTED[edge[1]]
    }
    covers = set()
    labels = tuple(sorted(set(SELECTED.values())))
    for order in itertools.permutations(labels):
        rank = {label: index for index, label in enumerate(order)}
        paid = {
            edge for edge in changing
            if rank[SELECTED[edge[0]]] > rank[SELECTED[edge[1]]]
        }
        covers.add(frozenset(changing - paid))
    require(len(covers) == 6, "label covers")
    return covers


def min_deficit(mask: set[tuple[str, str]], covers: set[frozenset[tuple[str, str]]]) -> int:
    return min(len(set(cover) - mask) for cover in covers)


def compile_manifest(repository: Path) -> dict:
    transition = load(
        repository / "data/exact_recurrent_first_host_transition_domain_source_audit.json"
    )
    require(transition["aggregate"]["symbolic_directed_edges"] == 8, "symbolic edges")
    require(transition["aggregate"]["physical_directed_edges"] == 0, "physical edges changed")
    require(transition["aggregate"]["exact_edge_legality_proofs"] == 0, "legality changed")
    require(transition["aggregate"]["exact_edge_operation_kind_mappings"] == 0, "mapping changed")

    label = label_covers()
    menu = menu_covers()
    names = tuple(FAMILIES)
    rows = []
    minimal_label = []
    minimal_menu = []

    for flags in itertools.product((0, 1), repeat=len(names)):
        chosen = tuple(name for name, flag in zip(names, flags) if flag)
        mask = {edge for name in chosen for edge in FAMILIES[name]}
        label_count = sum(cover <= mask for cover in label)
        menu_count = sum(cover <= mask for cover in menu)
        label_deficit = min_deficit(mask, label)
        menu_deficit = min_deficit(mask, menu)
        row = {
            "families": list(chosen),
            "family_count": len(chosen),
            "route_closed_edges": sorted(edge_code(edge) for edge in mask),
            "route_closed_edge_count": len(mask),
            "contained_label_covers": label_count,
            "contained_menu_covers": menu_count,
            "minimum_additional_label_edges": label_deficit,
            "minimum_additional_menu_edges": menu_deficit,
        }
        rows.append(row)
        if label_count and not any(
            set(other) < set(chosen)
            and sum(
                cover <= {edge for name in other for edge in FAMILIES[name]}
                for cover in label
            )
            for size in range(len(chosen))
            for other in itertools.combinations(chosen, size)
        ):
            minimal_label.append(list(chosen))
        if menu_count and not any(
            set(other) < set(chosen)
            and sum(
                cover <= {edge for name in other for edge in FAMILIES[name]}
                for cover in menu
            )
            for size in range(len(chosen))
            for other in itertools.combinations(chosen, size)
        ):
            minimal_menu.append(list(chosen))

    expected_minimal = [
        ["delete_02", "delete_20"],
        ["delete_02", "restore_20"],
        ["restore_02", "delete_20"],
        ["restore_02", "restore_20"],
    ]
    normalize = lambda values: sorted((sorted(value) for value in values))
    require(normalize(minimal_label) == normalize(expected_minimal), "minimal label families")
    require(normalize(minimal_menu) == normalize(expected_minimal), "minimal menu families")

    same_bit = {
        "02": {"restore_02", "delete_02"},
        "20": {"restore_20", "delete_20"},
    }
    for bit, chosen in same_bit.items():
        row = next(item for item in rows if set(item["families"]) == chosen)
        require(row["contained_label_covers"] == 0, f"same-bit label {bit}")
        require(row["contained_menu_covers"] == 0, f"same-bit menu {bit}")
        require(row["minimum_additional_label_edges"] in (1, 2), f"same-bit label deficit {bit}")
        require(row["minimum_additional_menu_edges"] == 2, f"same-bit menu deficit {bit}")

    two_family_rows = [row for row in rows if row["family_count"] == 2]
    require(len(two_family_rows) == 6, "two-family rows")
    require(sum(row["contained_menu_covers"] > 0 for row in two_family_rows) == 4,
            "two-family menu shortcuts")
    require(sum(row["contained_label_covers"] > 0 for row in two_family_rows) == 4,
            "two-family label shortcuts")

    return {
        "schema": "exact-recurrent-first-host-action-family-route-leverage/v1",
        "host_id": "s4-75b04c45c1c8eac2",
        "source_transition_audit":
            "data/exact_recurrent_first_host_transition_domain_source_audit.json",
        "family_contract": {
            name: {
                "bit": name.split("_")[1],
                "action": name.split("_")[0],
                "directed_edges": sorted(edge_code(edge) for edge in edges),
                "uniform_source_certificate_required": 1,
                "current_source_certificate": 0,
            }
            for name, edges in FAMILIES.items()
        },
        "patterns": rows,
        "minimal_complete_family_sets": expected_minimal,
        "criterion": {
            "two_family_shortcut":
                "one directed action family for bit 02 and one directed action family for bit 20",
            "same_bit_bidirectional_failure":
                "closing restore and delete families for only one bit leaves the other bit reversal pairs uncovered",
            "uniformity_warning":
                "a family certificate must source-close both context edges; one edge cannot stand in for the family",
        },
        "aggregate": {
            "directed_action_families": 4,
            "edges_per_family": 2,
            "family_subsets": 16,
            "two_family_subsets": 6,
            "two_family_label_shortcuts": 4,
            "two_family_menu_shortcuts": 4,
            "minimum_families_for_label_cover": 2,
            "minimum_families_for_menu_cover": 2,
            "minimal_label_family_sets": 4,
            "minimal_menu_family_sets": 4,
            "current_source_closed_families": 0,
            "current_source_closed_edges": 0,
            "current_complete_scalar_covers": 0,
        },
        "conclusion": {
            "action_family_classification_complete": 1,
            "one_family_closes_scalar_cover": 0,
            "one_directed_family_per_bit_suffices": 1,
            "both_directions_of_one_bit_suffice": 0,
            "all_restore_families_form_menu_cover": 1,
            "all_delete_families_form_menu_cover": 1,
            "mixed_action_families_can_form_menu_cover": 1,
            "current_source_family_certificate_complete": 0,
            "promotion_to_recurrent_closure_allowed": 0,
        },
        "honesty": {
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


def validate(manifest: dict, repository: Path) -> None:
    require(manifest == compile_manifest(repository), "manifest mismatch")


def mutation_audit(manifest: dict, repository: Path) -> int:
    mutations = [
        lambda item: item["aggregate"].update(directed_action_families=3),
        lambda item: item["aggregate"].update(family_subsets=15),
        lambda item: item["aggregate"].update(two_family_menu_shortcuts=3),
        lambda item: item["aggregate"].update(minimum_families_for_menu_cover=1),
        lambda item: item["minimal_complete_family_sets"].pop(),
        lambda item: item["patterns"][0].update(minimum_additional_menu_edges=3),
        lambda item: item["patterns"][5].update(contained_menu_covers=0),
        lambda item: item["family_contract"]["restore_02"].update(current_source_certificate=1),
        lambda item: item["criterion"].update(same_bit_bidirectional_failure=""),
        lambda item: item["conclusion"].update(one_family_closes_scalar_cover=1),
        lambda item: item["conclusion"].update(both_directions_of_one_bit_suffice=1),
        lambda item: item["conclusion"].update(current_source_family_certificate_complete=1),
        lambda item: item["conclusion"].update(promotion_to_recurrent_closure_allowed=1),
        lambda item: item["honesty"].update(physical_transition_legality_proved=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate, repository)
        except FamilyError:
            rejected += 1
    require(rejected == len(mutations), "mutation audit")
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
        "checker": "exact-recurrent-first-host-action-family-route-leverage",
        **manifest["aggregate"],
        "mutation_corruptions_rejected": mutation_audit(manifest, repository),
        **manifest["conclusion"],
        **manifest["honesty"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
