#!/usr/bin/env python3
"""Prove that current side-four records do not determine complete line energy.

The witness is contract-level: the selected-line background load is absent from
the populated manifests, and two values of that omitted variable give different
exact CMR1918 complete line kernels. It does not assert global realizability of
both completions.
"""
from __future__ import annotations

import argparse
import copy
import json
from math import comb
from pathlib import Path
from typing import Any


class NonidentifiabilityError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise NonidentifiabilityError(message)


def kernel(h: int, k: int) -> int:
    require(isinstance(h, int) and h >= 0, "background load must be nonnegative")
    require(isinstance(k, int) and k >= 0, "response load must be nonnegative")
    return k * comb(h, 2) + comb(k, 2) * h + comb(k, 3)


def validate(geometry: dict[str, Any], witness: dict[str, Any]) -> dict[str, Any]:
    require(
        geometry.get("schema")
        == "exact-recurrent-side-four-selected-line-geometry/v1",
        "geometry schema mismatch",
    )
    require(
        witness.get("schema")
        == "exact-recurrent-side-four-line-kernel-nonidentifiability/v1",
        "witness schema mismatch",
    )

    formula = witness.get("formula")
    require(
        formula
        == {
            "kernel": "K(h,k)=k*C(h,2)+C(k,2)*h+C(k,3)",
            "identity": "K(h,k)=C(h+k,3)-C(h,3)",
            "source": "CMR1918--CMR1925",
        },
        "kernel formula declaration mismatch",
    )

    geometry_classes = geometry.get("classes")
    require(
        isinstance(geometry_classes, list) and len(geometry_classes) == 2,
        "two geometry classes required",
    )
    geometry_by_id: dict[str, dict[str, Any]] = {}
    for item in geometry_classes:
        require(isinstance(item, dict), "geometry class object required")
        class_id = item.get("id")
        require(isinstance(class_id, str) and class_id, "geometry class id required")
        require(class_id not in geometry_by_id, f"duplicate geometry class {class_id}")
        geometry_by_id[class_id] = item

    classes = witness.get("classes")
    require(isinstance(classes, list) and len(classes) == 2, "two witness classes required")
    seen: set[str] = set()
    host_census: dict[str, int] = {}
    minimum_difference: int | None = None

    geometry_hosts = geometry.get("hosts")
    require(isinstance(geometry_hosts, list) and len(geometry_hosts) == 11, "eleven geometry hosts required")
    actual_host_census: dict[str, int] = {}
    for host in geometry_hosts:
        require(isinstance(host, dict), "geometry host object required")
        class_id = host.get("class_id")
        require(class_id in geometry_by_id, "unknown geometry host class")
        actual_host_census[class_id] = actual_host_census.get(class_id, 0) + 1

    for index, item in enumerate(classes):
        require(isinstance(item, dict), f"class[{index}] object required")
        class_id = item.get("id")
        require(class_id in geometry_by_id, f"unknown witness class {class_id}")
        require(class_id not in seen, f"duplicate witness class {class_id}")
        seen.add(class_id)

        geometry_class = geometry_by_id[class_id]
        selector = item.get("selector")
        require(selector == geometry_class.get("selector"), f"selector mismatch for {class_id}")

        response_points = geometry_class.get("response_points")
        triples = geometry_class.get("collinear_triples")
        require(isinstance(response_points, list), f"response points missing for {class_id}")
        require(isinstance(triples, list) and triples, f"triples missing for {class_id}")

        line_points = {
            tuple(point)
            for triple in triples
            for point in triple
        }
        k = item.get("response_line_occupancy")
        require(k == len(line_points), f"response line occupancy mismatch for {class_id}")
        require(k in {3, 4}, f"unexpected response line occupancy for {class_id}")

        completions = item.get("background_load_witnesses")
        require(
            isinstance(completions, list) and len(completions) == 2,
            f"two load completions required for {class_id}",
        )
        loads: list[int] = []
        energies: list[int] = []
        for completion_index, completion in enumerate(completions):
            require(
                isinstance(completion, dict),
                f"completion {completion_index} for {class_id} must be object",
            )
            h = completion.get("h")
            energy = completion.get("complete_line_energy")
            require(
                isinstance(h, int) and h >= 0,
                f"invalid h for completion {completion_index} of {class_id}",
            )
            require(
                energy == kernel(h, k),
                f"kernel mismatch for h={h}, class {class_id}",
            )
            require(
                energy == comb(h + k, 3) - comb(h, 3),
                f"binomial identity mismatch for h={h}, class {class_id}",
            )
            loads.append(h)
            energies.append(energy)

        require(loads == [0, 1], f"canonical witness loads must be [0,1] for {class_id}")
        require(energies[0] != energies[1], f"witness energies must differ for {class_id}")
        difference = energies[1] - energies[0]
        require(difference > 0, f"kernel must increase for {class_id}")
        require(
            item.get("energy_difference") == difference,
            f"energy difference mismatch for {class_id}",
        )
        minimum_difference = difference if minimum_difference is None else min(minimum_difference, difference)
        host_census[class_id] = actual_host_census.get(class_id, 0)

    require(seen == set(geometry_by_id), "witness classes do not cover geometry classes")
    require(host_census == witness.get("host_census"), "host census mismatch")
    require(host_census == {"selected-line-3012": 9, "selected-line-3210": 2}, "unexpected host census")

    interpretation = witness.get("interpretation")
    require(isinstance(interpretation, dict), "interpretation required")
    require(
        interpretation.get("claim")
        == "The populated host/selector/selected-line records omit background line load h, so they do not determine even the selected-line contribution to the complete coupled response kernel.",
        "claim changed",
    )
    require(
        interpretation.get("nonclaim")
        == "The two line-load completions are schema witnesses; this manifest does not assert that both occur as globally legal construction states.",
        "nonclaim changed",
    )

    expected_honesty = {
        "line_kernel_nonidentifiability_proved": 1,
        "host_selector_records_determine_complete_line_energy": 0,
        "global_physical_realizability_of_witness_completions": 0,
        "complete_weighted_rows_determined": 0,
        "recurrent_offspring_rows_complete": 0,
        "strict_lyapunov_certificate_proved": 0,
        "all_n_proved_by_checker": 0,
    }
    require(witness.get("honesty") == expected_honesty, "honesty mismatch")

    return {
        "selected_line_classes": len(classes),
        "covered_residual_hosts": sum(host_census.values()),
        "class_3012_energy_h0": kernel(0, 3),
        "class_3012_energy_h1": kernel(1, 3),
        "class_3210_energy_h0": kernel(0, 4),
        "class_3210_energy_h1": kernel(1, 4),
        "minimum_witness_energy_difference": minimum_difference,
        "line_kernel_nonidentifiability_proved": 1,
        "complete_weighted_rows_determined": 0,
        "strict_lyapunov_certificate_proved": 0,
        "all_n_proved_by_checker": 0,
    }


def mutation_audit(geometry: dict[str, Any], witness: dict[str, Any]) -> int:
    mutations = [
        lambda item: item.update(schema="wrong"),
        lambda item: item["classes"].pop(),
        lambda item: item["classes"][0].update(selector="3210"),
        lambda item: item["classes"][0].update(response_line_occupancy=4),
        lambda item: item["classes"][0]["background_load_witnesses"][0].update(complete_line_energy=2),
        lambda item: item["classes"][0]["background_load_witnesses"][1].update(h=0),
        lambda item: item["classes"][0].update(energy_difference=4),
        lambda item: item["host_census"].update(**{"selected-line-3012": 8}),
        lambda item: item["interpretation"].update(nonclaim="both globally realized"),
        lambda item: item["honesty"].update(global_physical_realizability_of_witness_completions=1),
        lambda item: item["honesty"].update(complete_weighted_rows_determined=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(witness)
        mutate(candidate)
        try:
            validate(geometry, candidate)
        except (NonidentifiabilityError, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "mutation audit accepted corrupted witness")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--geometry", type=Path, required=True)
    parser.add_argument("--witness", type=Path, required=True)
    args = parser.parse_args()

    geometry = json.loads(args.geometry.read_text(encoding="utf-8"))
    witness = json.loads(args.witness.read_text(encoding="utf-8"))
    result = validate(geometry, witness)
    result["mutation_corruptions_rejected"] = mutation_audit(geometry, witness)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
