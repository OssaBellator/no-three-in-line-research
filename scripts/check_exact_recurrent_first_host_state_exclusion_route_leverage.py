#!/usr/bin/env python3
"""Classify route-cover leverage from source-backed impossible menu states."""
from __future__ import annotations

import argparse
import copy
import itertools
import json
from pathlib import Path

HOST = "s4-75b04c45c1c8eac2"
STATES = ("00", "01", "10", "11")
SELECTED = {"00": "3012", "01": "3201", "10": "2031", "11": "2031"}
UNDIRECTED = (("00", "01"), ("00", "10"), ("01", "11"), ("10", "11"))


class ExclusionAuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ExclusionAuditError(message)


def root() -> Path:
    here = Path(__file__).resolve()
    for candidate in (here.parent, *here.parents):
        if (candidate / "STATUS.md").is_file():
            return candidate
    raise ExclusionAuditError("repository root not found")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def directed_edges() -> set[tuple[str, str]]:
    return set(UNDIRECTED) | {(target, source) for source, target in UNDIRECTED}


def edge_code(edge: tuple[str, str]) -> str:
    return f"{edge[0]}->{edge[1]}"


def changing_edges() -> set[tuple[str, str]]:
    return {
        edge
        for edge in directed_edges()
        if SELECTED[edge[0]] != SELECTED[edge[1]]
    }


def label_covers() -> set[frozenset[tuple[str, str]]]:
    changing = changing_edges()
    labels = tuple(sorted(set(SELECTED.values())))
    covers: set[frozenset[tuple[str, str]]] = set()
    for order in itertools.permutations(labels):
        rank = {label: index for index, label in enumerate(order)}
        paid = {
            edge
            for edge in changing
            if rank[SELECTED[edge[0]]] > rank[SELECTED[edge[1]]]
        }
        covers.add(frozenset(changing - paid))
    require(len(covers) == 6, "label cover count")
    return covers


def menu_covers() -> set[frozenset[tuple[str, str]]]:
    covers: set[frozenset[tuple[str, str]]] = set()
    for order in itertools.permutations(STATES):
        rank = {state: index for index, state in enumerate(order)}
        paid = {
            (source, target)
            if rank[source] > rank[target]
            else (target, source)
            for source, target in UNDIRECTED
        }
        covers.add(frozenset((target, source) for source, target in paid))
    require(len(covers) == 14, "menu cover count")
    return covers


def compile_manifest(repository: Path) -> dict:
    transition = load(
        repository
        / "data/exact_recurrent_first_host_transition_domain_source_audit.json"
    )
    admission = load(
        repository / "data/exact_recurrent_first_host_route_cover_admission.json"
    )
    require(
        transition["aggregate"]["physical_menu_states"] == 0,
        "physical state coverage changed",
    )
    require(
        transition["aggregate"]["physical_directed_edges"] == 0,
        "physical edge coverage changed",
    )
    require(
        admission["aggregate"]["current_route_closed_edges"] == 0,
        "route-closed edge state changed",
    )

    directed = directed_edges()
    label = label_covers()
    menu = menu_covers()
    patterns = []
    for size in range(len(STATES) + 1):
        for excluded_tuple in itertools.combinations(STATES, size):
            excluded = set(excluded_tuple)
            closed = frozenset(
                edge
                for edge in directed
                if edge[0] in excluded or edge[1] in excluded
            )
            complete_label = sum(cover <= closed for cover in label)
            complete_menu = sum(cover <= closed for cover in menu)
            additional_label = min(len(cover - closed) for cover in label)
            additional_menu = min(len(cover - closed) for cover in menu)
            patterns.append(
                {
                    "excluded_states": list(excluded_tuple),
                    "excluded_state_count": size,
                    "incident_edges_physically_excluded": sorted(
                        edge_code(edge) for edge in closed
                    ),
                    "incident_edge_count": len(closed),
                    "complete_label_covers": complete_label,
                    "complete_menu_covers": complete_menu,
                    "minimum_additional_label_routes": additional_label,
                    "minimum_additional_menu_routes": additional_menu,
                }
            )

    by_key = {
        tuple(row["excluded_states"]): row
        for row in patterns
    }
    require(len(patterns) == 16, "state subset count")
    require(
        all(
            by_key[(state,)]["complete_label_covers"] == 0
            and by_key[(state,)]["complete_menu_covers"] == 0
            for state in STATES
        ),
        "single-state shortcut",
    )
    require(
        by_key[("11",)]["minimum_additional_label_routes"] == 2
        and by_key[("11",)]["minimum_additional_menu_routes"] == 2,
        "restore-both exclusion deficit",
    )
    label_two = [
        row
        for row in patterns
        if row["excluded_state_count"] == 2 and row["complete_label_covers"] > 0
    ]
    menu_two = [
        row
        for row in patterns
        if row["excluded_state_count"] == 2 and row["complete_menu_covers"] > 0
    ]
    require(
        [row["excluded_states"] for row in label_two]
        == [["00", "01"], ["00", "11"], ["01", "10"]],
        "two-state label shortcuts",
    )
    require(
        [row["excluded_states"] for row in menu_two]
        == [["00", "11"], ["01", "10"]],
        "two-state menu shortcuts",
    )
    all_edge_patterns = [
        row
        for row in patterns
        if row["incident_edge_count"] == 8
    ]
    require(len(all_edge_patterns) == 7, "all-edge state patterns")

    return {
        "schema": "exact-recurrent-first-host-state-exclusion-route-leverage/v1",
        "scope": {
            "host_id": HOST,
            "states": list(STATES),
            "conditional_rule": (
                "a source-backed impossible state physically excludes every "
                "incident directed edge"
            ),
        },
        "patterns": patterns,
        "aggregate": {
            "state_exclusion_patterns": 16,
            "single_state_patterns": 4,
            "single_state_patterns_completing_label_cover": 0,
            "single_state_patterns_completing_menu_cover": 0,
            "two_state_patterns": 6,
            "two_state_patterns_completing_label_cover": len(label_two),
            "two_state_patterns_completing_menu_cover": len(menu_two),
            "minimum_state_exclusions_for_label_cover_without_edge_routes": 2,
            "minimum_state_exclusions_for_menu_cover_without_edge_routes": 2,
            "patterns_closing_all_eight_edges": len(all_edge_patterns),
        },
        "distinguished_patterns": {
            "exclude_restore_both_only": {
                "excluded_states": ["11"],
                "incident_edges": by_key[("11",)][
                    "incident_edges_physically_excluded"
                ],
                "minimum_additional_label_routes": 2,
                "minimum_additional_menu_routes": 2,
                "complete_label_covers": 0,
                "complete_menu_covers": 0,
            },
            "label_only_two_state_shortcut": {
                "excluded_states": ["00", "01"],
                "complete_label_covers": 6,
                "complete_menu_covers": 0,
                "minimum_additional_menu_routes": 1,
            },
            "menu_complete_opposite_pairs": [["00", "11"], ["01", "10"]],
        },
        "current_source_state": {
            "source_backed_impossible_states": [],
            "incident_route_closed_edges": [],
            "complete_label_covers": 0,
            "complete_menu_covers": 0,
        },
        "conclusion": {
            "state_impossibility_can_route_incident_edges_by_physical_exclusion": 1,
            "exclude_state_11_alone_completes_label_cover": 0,
            "exclude_state_11_alone_completes_menu_cover": 0,
            "exclude_state_11_alone_still_needs_two_routes": 1,
            "two_state_exclusion_shortcuts_classified": 1,
            "current_source_supplies_state_impossibility_proof": 0,
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
        lambda item: item["aggregate"].update(state_exclusion_patterns=15),
        lambda item: item["aggregate"].update(
            single_state_patterns_completing_label_cover=1
        ),
        lambda item: item["aggregate"].update(
            two_state_patterns_completing_menu_cover=3
        ),
        lambda item: item["aggregate"].update(
            minimum_state_exclusions_for_menu_cover_without_edge_routes=1
        ),
        lambda item: item["distinguished_patterns"][
            "exclude_restore_both_only"
        ].update(minimum_additional_label_routes=1),
        lambda item: item["distinguished_patterns"][
            "exclude_restore_both_only"
        ].update(complete_menu_covers=1),
        lambda item: item["distinguished_patterns"].update(
            menu_complete_opposite_pairs=[["00", "01"]]
        ),
        lambda item: item["patterns"][4].update(complete_label_covers=1),
        lambda item: item["patterns"][4].update(
            minimum_additional_menu_routes=1
        ),
        lambda item: item["current_source_state"].update(
            source_backed_impossible_states=["11"]
        ),
        lambda item: item["conclusion"].update(
            exclude_state_11_alone_completes_label_cover=1
        ),
        lambda item: item["conclusion"].update(
            current_source_supplies_state_impossibility_proof=1
        ),
        lambda item: item["conclusion"].update(
            promotion_to_recurrent_closure_allowed=1
        ),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate, repository)
        except ExclusionAuditError:
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
    print(
        json.dumps(
            {
                "checker": "exact-recurrent-first-host-state-exclusion-route-leverage",
                **manifest["aggregate"],
                "mutation_corruptions_rejected": mutation_audit(
                    manifest, repository
                ),
                **manifest["conclusion"],
                **manifest["honesty"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
