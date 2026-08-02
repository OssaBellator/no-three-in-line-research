#!/usr/bin/env python3
"""Validate normalized selected-response provenance for the side-four residual kernel.

This proves an exact deterministic selector/provenance projection only. It does
not populate physical backgrounds, deletion causes, legal repairs, child rows,
or a global Lyapunov certificate.
"""
from __future__ import annotations

import argparse
import copy
import json
from collections import Counter
from pathlib import Path
from typing import Any


class SelectedProjectionError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise SelectedProjectionError(message)


def edge_key(values: Any, context: str) -> tuple[str, ...]:
    require(isinstance(values, list) and values, f"{context}: edges required")
    require(
        all(
            isinstance(value, str)
            and len(value) == 2
            and value.isdigit()
            for value in values
        ),
        f"{context}: invalid edge",
    )
    require(len(values) == len(set(values)), f"{context}: duplicate edge")
    return tuple(sorted(values))


def validate(
    kernel: dict[str, Any],
    lineage_projection: dict[str, Any],
    selected_projection: dict[str, Any],
) -> dict[str, Any]:
    require(
        kernel.get("schema") == "exact-recurrent-side-four-host-kernel/v1",
        "kernel schema mismatch",
    )
    require(
        lineage_projection.get("schema")
        == "exact-recurrent-side-four-lineage-projection/v1",
        "lineage projection schema mismatch",
    )
    require(
        selected_projection.get("schema")
        == "exact-recurrent-side-four-selected-provenance-projection/v1",
        "selected projection schema mismatch",
    )

    source = selected_projection.get("source")
    require(isinstance(source, dict), "source required")
    require(
        source.get("source_schema")
        == "prime-power-side-four-selected-response-provenance-manifest/v1",
        "source schema mismatch",
    )
    require(
        source.get("lineage_manifest_sha256")
        == "84ad1c92a9e0bcfb4d1f613e05edec20c4300022d96269ed561b45d32bf7432f",
        "lineage digest mismatch",
    )
    require(
        source.get("selected_manifest_sha256")
        == "0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6",
        "selected manifest digest mismatch",
    )
    require(
        source.get("selection_rule")
        == "minimum triple count then lexicographically least response permutation",
        "selection rule mismatch",
    )
    require(
        source.get("source_honesty")
        == {
            "global_provenance_complete": 0,
            "compulsory_coefficients_complete": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
        "source honesty mismatch",
    )

    require(
        selected_projection.get("normalized_provenance")
        == {
            "owner_scope": "side-four-raw-host",
            "local_line_class": "minimum-response-energy",
            "interface": "target-01",
            "crt_scope": "not-applied",
            "collision_key": "host deletion trace",
        },
        "normalized provenance mismatch",
    )

    local_by_edges: dict[tuple[str, ...], dict[str, Any]] = {}
    for host in kernel.get("residual_hosts", []):
        require(isinstance(host, dict), "kernel host object required")
        host_id = host.get("id")
        require(isinstance(host_id, str) and host_id, "kernel host id required")
        deletions = edge_key(host.get("deletions"), f"kernel host {host_id}")
        require(deletions not in local_by_edges, f"duplicate local deletions {deletions}")
        local_by_edges[deletions] = host
    require(len(local_by_edges) == 11, "eleven local residual hosts required")

    lineage_by_upstream: dict[str, dict[str, Any]] = {}
    for host in lineage_projection.get("residual_hosts", []):
        require(isinstance(host, dict), "lineage host object required")
        upstream_id = host.get("upstream_id")
        require(
            isinstance(upstream_id, str) and upstream_id.startswith("s4-"),
            "lineage upstream id required",
        )
        require(
            upstream_id not in lineage_by_upstream,
            f"duplicate lineage upstream id {upstream_id}",
        )
        lineage_by_upstream[upstream_id] = host
    require(len(lineage_by_upstream) == 11, "eleven lineage hosts required")

    selected_hosts = selected_projection.get("residual_hosts")
    require(
        isinstance(selected_hosts, list) and len(selected_hosts) == 11,
        "eleven selected hosts required",
    )

    selector_census: Counter[str] = Counter()
    energy_census: Counter[int] = Counter()
    positive_gaps = 0
    no_higher = 0
    seen_ids: set[str] = set()
    seen_edges: set[tuple[str, ...]] = set()

    for index, selected in enumerate(selected_hosts):
        require(isinstance(selected, dict), f"selected host[{index}] object required")
        upstream_id = selected.get("upstream_id")
        require(
            isinstance(upstream_id, str) and upstream_id in lineage_by_upstream,
            f"selected host[{index}] unknown upstream id",
        )
        require(upstream_id not in seen_ids, f"duplicate selected id {upstream_id}")
        seen_ids.add(upstream_id)

        deletions = edge_key(selected.get("deletions"), f"selected host {upstream_id}")
        require(deletions not in seen_edges, f"duplicate selected deletions {deletions}")
        seen_edges.add(deletions)
        require(deletions in local_by_edges, f"selected deletions absent locally {deletions}")

        lineage = lineage_by_upstream[upstream_id]
        require(
            edge_key(lineage.get("deletions"), f"lineage host {upstream_id}")
            == deletions,
            f"lineage deletion mismatch for {upstream_id}",
        )
        require(
            selected.get("contained_blockers") == lineage.get("contained_blockers"),
            f"blocker mismatch for {upstream_id}",
        )
        require(
            selected.get("collision_key") == ",".join(deletions),
            f"collision key mismatch for {upstream_id}",
        )

        local = local_by_edges[deletions]
        responses = local.get("surviving_bad_responses")
        require(
            isinstance(responses, list) and responses,
            f"local response list missing for {upstream_id}",
        )
        energies = {
            item.get("permutation"): item.get("intrinsic_triples")
            for item in responses
            if isinstance(item, dict)
        }
        require(
            len(energies) == len(responses)
            and all(
                isinstance(permutation, str)
                and isinstance(energy, int)
                and energy > 0
                for permutation, energy in energies.items()
            ),
            f"invalid local responses for {upstream_id}",
        )

        minimum = min(energies.values())
        face = sorted(
            permutation
            for permutation, energy in energies.items()
            if energy == minimum
        )
        selector = min(face)
        levels = sorted(set(energies.values()))
        gap: int | str = levels[1] - levels[0] if len(levels) > 1 else "-"

        require(
            selected.get("minimum_energy") == minimum,
            f"minimum energy mismatch for {upstream_id}",
        )
        require(
            selected.get("minimizer_face") == face,
            f"minimizer face mismatch for {upstream_id}",
        )
        require(
            selected.get("selector") == selector,
            f"selector mismatch for {upstream_id}",
        )
        require(
            selected.get("next_energy_gap") == gap,
            f"energy gap mismatch for {upstream_id}",
        )
        require(
            selected.get("fate") == "B",
            f"residual fate mismatch for {upstream_id}",
        )

        selector_census[selector] += 1
        energy_census[minimum] += 1
        if isinstance(gap, int):
            require(gap > 0, f"nonpositive gap for {upstream_id}")
            positive_gaps += 1
        else:
            no_higher += 1

    require(seen_ids == set(lineage_by_upstream), "selected projection not bijective")
    require(seen_edges == set(local_by_edges), "selected deletion projection not bijective")

    expected_aggregate = {
        "residual_hosts": 11,
        "selector_census": {"3012": 9, "3210": 2},
        "minimum_energy_census": {"1": 9, "4": 2},
        "unique_minimum": 11,
        "positive_next_energy_gap": 9,
        "no_higher_energy_response": 2,
    }
    require(
        selected_projection.get("aggregate") == expected_aggregate,
        "aggregate mismatch",
    )
    require(
        selector_census == Counter({"3012": 9, "3210": 2}),
        "selector census mismatch",
    )
    require(
        energy_census == Counter({1: 9, 4: 2}),
        "energy census mismatch",
    )
    require(positive_gaps == 9, "positive gap count mismatch")
    require(no_higher == 2, "no-higher count mismatch")
    require(
        all(len(host.get("minimizer_face", [])) == 1 for host in selected_hosts),
        "every residual selector must be unique",
    )

    expected_honesty = {
        "normalized_selected_response_provenance_complete": 1,
        "physical_backgrounds_complete": 0,
        "physical_deletion_causes_complete": 0,
        "actual_owner_identity_complete": 0,
        "global_collision_lineage_complete": 0,
        "legal_operations_complete": 0,
        "recurrent_offspring_rows_complete": 0,
        "strict_lyapunov_certificate_proved": 0,
        "all_n_proved_by_checker": 0,
    }
    require(
        selected_projection.get("honesty") == expected_honesty,
        "selected projection honesty mismatch",
    )

    return {
        "joined_residual_hosts": 11,
        "unique_selected_responses": 11,
        "selector_3012_hosts": selector_census["3012"],
        "selector_3210_hosts": selector_census["3210"],
        "minimum_energy_one_hosts": energy_census[1],
        "minimum_energy_four_hosts": energy_census[4],
        "positive_gap_hosts": positive_gaps,
        "no_higher_response_hosts": no_higher,
        "normalized_selected_response_provenance_complete": 1,
        "physical_provenance_complete": 0,
        "legal_operations_complete": 0,
        "recurrent_offspring_rows_complete": 0,
        "strict_lyapunov_certificate_proved": 0,
        "all_n_proved_by_checker": 0,
    }


def mutation_audit(
    kernel: dict[str, Any],
    lineage_projection: dict[str, Any],
    selected_projection: dict[str, Any],
) -> int:
    mutations = [
        lambda item: item.update(schema="wrong"),
        lambda item: item["residual_hosts"].pop(),
        lambda item: item["residual_hosts"][1].update(
            upstream_id=item["residual_hosts"][0]["upstream_id"]
        ),
        lambda item: item["residual_hosts"][0].update(selector="3210"),
        lambda item: item["residual_hosts"][0].update(
            minimizer_face=["3012", "3210"]
        ),
        lambda item: item["residual_hosts"][0].update(minimum_energy=4),
        lambda item: item["residual_hosts"][0].update(next_energy_gap="-"),
        lambda item: item["residual_hosts"][0].update(fate="Z"),
        lambda item: item["residual_hosts"][0].update(collision_key="anonymous"),
        lambda item: item["normalized_provenance"].update(
            owner_scope="global-owner"
        ),
        lambda item: item["honesty"].update(actual_owner_identity_complete=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(selected_projection)
        mutate(candidate)
        try:
            validate(kernel, lineage_projection, candidate)
        except (SelectedProjectionError, KeyError, TypeError, ValueError):
            rejected += 1
    require(
        rejected == len(mutations),
        "mutation audit accepted a corrupted selected projection",
    )
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kernel", type=Path, required=True)
    parser.add_argument("--lineage-projection", type=Path, required=True)
    parser.add_argument("--selected-projection", type=Path, required=True)
    args = parser.parse_args()

    kernel = json.loads(args.kernel.read_text(encoding="utf-8"))
    lineage_projection = json.loads(
        args.lineage_projection.read_text(encoding="utf-8")
    )
    selected_projection = json.loads(
        args.selected_projection.read_text(encoding="utf-8")
    )

    result = validate(kernel, lineage_projection, selected_projection)
    result["mutation_corruptions_rejected"] = mutation_audit(
        kernel,
        lineage_projection,
        selected_projection,
    )
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
