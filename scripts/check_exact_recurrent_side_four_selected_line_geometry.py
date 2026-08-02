#!/usr/bin/env python3
"""Validate exact selected-line geometry for the side-four residual kernel."""
from __future__ import annotations

import argparse
import copy
import json
from collections import Counter
from itertools import combinations
from math import gcd
from pathlib import Path
from typing import Any


class SelectedLineGeometryError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise SelectedLineGeometryError(message)


def parse_point(value: Any, context: str) -> tuple[int, int]:
    require(
        isinstance(value, list)
        and len(value) == 2
        and all(
            isinstance(item, str) and item.lstrip("-").isdigit()
            for item in value
        ),
        f"{context}: invalid point",
    )
    return int(value[0]), int(value[1])


def points_for_permutation(permutation: str) -> list[tuple[int, int]]:
    require(
        isinstance(permutation, str)
        and len(permutation) == 4
        and set(permutation) == set("0123"),
        "invalid permutation",
    )
    return [(row, int(column)) for row, column in enumerate(permutation)]


def collinear(
    first: tuple[int, int],
    second: tuple[int, int],
    third: tuple[int, int],
) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def primitive_line_signature(
    first: tuple[int, int],
    second: tuple[int, int],
) -> tuple[int, int, int]:
    require(first != second, "distinct points required")
    x1, y1 = first
    x2, y2 = second
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    divisor = gcd(gcd(abs(a), abs(b)), abs(c))
    require(divisor > 0, "zero line signature")
    a //= divisor
    b //= divisor
    c //= divisor
    for value in (a, b, c):
        if value:
            if value < 0:
                a, b, c = -a, -b, -c
            break
    return a, b, c


def signature_text(signature: tuple[int, int, int]) -> str:
    return ",".join(str(value) for value in signature)


def validate(
    selected_projection: dict[str, Any],
    geometry: dict[str, Any],
) -> dict[str, Any]:
    require(
        selected_projection.get("schema")
        == "exact-recurrent-side-four-selected-provenance-projection/v1",
        "selected projection schema mismatch",
    )
    require(
        geometry.get("schema")
        == "exact-recurrent-side-four-selected-line-geometry/v1",
        "geometry schema mismatch",
    )

    classes = geometry.get("classes")
    require(
        isinstance(classes, list) and len(classes) == 2,
        "two line classes required",
    )
    class_by_id: dict[str, dict[str, Any]] = {}
    class_by_selector: dict[str, dict[str, Any]] = {}

    for index, item in enumerate(classes):
        require(isinstance(item, dict), f"class[{index}] object required")
        class_id = item.get("id")
        selector = item.get("selector")
        require(isinstance(class_id, str) and class_id, f"class[{index}] id")
        require(
            isinstance(selector, str) and selector in {"3012", "3210"},
            f"class[{index}] selector",
        )
        require(class_id not in class_by_id, f"duplicate class id {class_id}")
        require(
            selector not in class_by_selector,
            f"duplicate selector class {selector}",
        )

        expected_points = points_for_permutation(selector)
        declared_points = [
            parse_point(value, f"class {class_id} response point")
            for value in item.get("response_points", [])
        ]
        require(
            declared_points == expected_points,
            f"response points mismatch for {class_id}",
        )

        exact_triples = [
            tuple(triple)
            for triple in combinations(expected_points, 3)
            if collinear(*triple)
        ]
        declared_triples = [
            tuple(
                parse_point(point, f"class {class_id} triple")
                for point in triple
            )
            for triple in item.get("collinear_triples", [])
        ]
        require(
            declared_triples == exact_triples,
            f"collinear triple list mismatch for {class_id}",
        )
        require(
            item.get("triple_count") == len(exact_triples),
            f"triple count mismatch for {class_id}",
        )
        require(exact_triples, f"selected class {class_id} must be bad")

        signatures = {
            primitive_line_signature(triple[0], triple[1])
            for triple in exact_triples
        }
        require(
            len(signatures) == 1,
            f"selected triples use more than one line for {class_id}",
        )
        signature = next(iter(signatures))
        declared_signature = tuple(
            int(value) for value in item.get("line_signature", [])
        )
        require(
            declared_signature == signature,
            f"line signature mismatch for {class_id}",
        )
        require(
            all(
                signature[0] * point[0]
                + signature[1] * point[1]
                + signature[2]
                == 0
                for triple in exact_triples
                for point in triple
            ),
            f"line equation fails for {class_id}",
        )

        class_by_id[class_id] = item
        class_by_selector[selector] = item

    require(
        set(class_by_selector) == {"3012", "3210"},
        "selector class coverage mismatch",
    )

    selected_hosts = selected_projection.get("residual_hosts")
    hosts = geometry.get("hosts")
    require(
        isinstance(selected_hosts, list) and len(selected_hosts) == 11,
        "selected projection must contain eleven hosts",
    )
    require(
        isinstance(hosts, list) and len(hosts) == 11,
        "geometry must contain eleven hosts",
    )

    selected_by_id = {
        host.get("upstream_id"): host
        for host in selected_hosts
        if isinstance(host, dict)
    }
    require(len(selected_by_id) == 11, "selected host ids must be unique")

    seen: set[str] = set()
    selector_census: Counter[str] = Counter()
    signature_census: Counter[str] = Counter()
    triple_incidences = 0

    for index, host in enumerate(hosts):
        require(isinstance(host, dict), f"host[{index}] object required")
        upstream_id = host.get("upstream_id")
        selector = host.get("selector")
        class_id = host.get("class_id")
        require(
            isinstance(upstream_id, str) and upstream_id in selected_by_id,
            f"host[{index}] unknown upstream id",
        )
        require(upstream_id not in seen, f"duplicate geometry host {upstream_id}")
        seen.add(upstream_id)
        selected = selected_by_id[upstream_id]
        require(
            selector == selected.get("selector"),
            f"selector join mismatch for {upstream_id}",
        )
        require(class_id in class_by_id, f"unknown class for {upstream_id}")
        line_class = class_by_id[class_id]
        require(
            line_class.get("selector") == selector,
            f"class selector mismatch for {upstream_id}",
        )
        require(
            line_class.get("triple_count") == selected.get("minimum_energy"),
            f"energy/triple mismatch for {upstream_id}",
        )

        signature = tuple(
            int(value) for value in line_class["line_signature"]
        )
        selector_census[selector] += 1
        signature_census[signature_text(signature)] += 1
        triple_incidences += int(line_class["triple_count"])

    require(seen == set(selected_by_id), "geometry host join is not bijective")
    require(
        selector_census == Counter({"3012": 9, "3210": 2}),
        "selector census mismatch",
    )
    require(
        signature_census == Counter({"1,-1,-1": 9, "1,1,-3": 2}),
        "line signature census mismatch",
    )
    require(
        triple_incidences == 17,
        "selected triple incidence count mismatch",
    )

    expected_aggregate = {
        "residual_hosts": 11,
        "selected_line_classes": 2,
        "single_line_supported_hosts": 11,
        "selector_3012_hosts": 9,
        "selector_3210_hosts": 2,
        "selected_triple_incidences": 17,
        "line_signature_census": {"1,-1,-1": 9, "1,1,-3": 2},
    }
    require(geometry.get("aggregate") == expected_aggregate, "aggregate mismatch")

    expected_honesty = {
        "selected_coordinate_line_geometry_complete": 1,
        "background_line_interactions_complete": 0,
        "physical_line_owner_complete": 0,
        "legal_line_repair_operations_complete": 0,
        "recurrent_offspring_rows_complete": 0,
        "strict_lyapunov_certificate_proved": 0,
        "all_n_proved_by_checker": 0,
    }
    require(geometry.get("honesty") == expected_honesty, "honesty mismatch")

    return {
        "residual_hosts": 11,
        "selected_line_classes": 2,
        "single_line_supported_hosts": 11,
        "selector_3012_hosts": selector_census["3012"],
        "selector_3210_hosts": selector_census["3210"],
        "selected_triple_incidences": triple_incidences,
        "selected_coordinate_line_geometry_complete": 1,
        "physical_line_owner_complete": 0,
        "legal_line_repair_operations_complete": 0,
        "recurrent_offspring_rows_complete": 0,
        "strict_lyapunov_certificate_proved": 0,
        "all_n_proved_by_checker": 0,
    }


def mutation_audit(
    selected_projection: dict[str, Any],
    geometry: dict[str, Any],
) -> int:
    mutations = [
        lambda item: item.update(schema="wrong"),
        lambda item: item["classes"].pop(),
        lambda item: item["classes"][0].update(selector="3210"),
        lambda item: item["classes"][0].update(response_points=[["0", "0"]]),
        lambda item: item["classes"][0].update(collinear_triples=[]),
        lambda item: item["classes"][0].update(triple_count=4),
        lambda item: item["classes"][0].update(
            line_signature=["1", "1", "-3"]
        ),
        lambda item: item["hosts"].pop(),
        lambda item: item["hosts"][0].update(class_id="selected-line-3210"),
        lambda item: item["aggregate"].update(
            selected_triple_incidences=16
        ),
        lambda item: item["honesty"].update(
            physical_line_owner_complete=1
        ),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(geometry)
        mutate(candidate)
        try:
            validate(selected_projection, candidate)
        except (SelectedLineGeometryError, KeyError, TypeError, ValueError):
            rejected += 1
    require(
        rejected == len(mutations),
        "mutation audit accepted corrupted selected-line geometry",
    )
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected-projection", type=Path, required=True)
    parser.add_argument("--geometry", type=Path, required=True)
    args = parser.parse_args()

    selected_projection = json.loads(
        args.selected_projection.read_text(encoding="utf-8")
    )
    geometry = json.loads(args.geometry.read_text(encoding="utf-8"))
    result = validate(selected_projection, geometry)
    result["mutation_corruptions_rejected"] = mutation_audit(
        selected_projection,
        geometry,
    )
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
