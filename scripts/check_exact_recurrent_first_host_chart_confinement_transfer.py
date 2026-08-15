#!/usr/bin/env python3
"""Transfer first-host safety from chart confinement and response disjointness."""
from __future__ import annotations

import argparse
import copy
import json
from itertools import combinations, permutations
from pathlib import Path
from typing import Any

HOST_ID = "s4-75b04c45c1c8eac2"
SAFE_PATH = "data/exact_recurrent_first_host_forbidden_background_invariance.json"
STRICT_PATH = "data/exact_recurrent_first_host_global_integer_two_point_strict_reversal.json"
RESPONSES: dict[str, tuple[int, ...]] = {
    "3012": (3, 0, 1, 2),
    "3210": (3, 2, 1, 0),
    "2031": (2, 0, 3, 1),
    "2310": (2, 3, 1, 0),
    "3201": (3, 2, 0, 1),
}
REOPENINGS = ("2031", "2310", "3201")


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise AuditError("unable to locate repository root")


def load_json(root: Path, relative: str) -> dict[str, Any]:
    path = root / relative
    require(path.is_file(), f"missing source artifact: {relative}")
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"source object required: {relative}")
    return value


def points(response: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple((row, response[row]) for row in range(4))


def code(point: tuple[int, int]) -> str:
    return f"{point[0]}{point[1]}"


def collinear(first: tuple[int, int], second: tuple[int, int], third: tuple[int, int]) -> bool:
    return (second[0] - first[0]) * (third[1] - first[1]) == (second[1] - first[1]) * (third[0] - first[0])


def triple_count(point_set: set[tuple[int, int]]) -> int:
    return sum(collinear(*triple) for triple in combinations(sorted(point_set), 3))


def scores(background: set[tuple[int, int]]) -> dict[str, int]:
    result = {}
    for name, response in RESPONSES.items():
        response_set = set(points(response))
        require(background.isdisjoint(response_set), f"background overlaps response {name}")
        result[name] = triple_count(background | response_set) - triple_count(background)
    return result


def minimizers(score: dict[str, int]) -> tuple[str, ...]:
    minimum = min(score.values())
    return tuple(name for name in RESPONSES if score[name] == minimum)


def expected_manifest() -> dict[str, Any]:
    chart = {(row, column) for row in range(4) for column in range(4)}
    union = {point for response in RESPONSES.values() for point in points(response)}
    complement = chart - union
    rows = []
    for mask in range(1 << len(complement)):
        ordered = sorted(complement)
        background = {ordered[index] for index in range(len(ordered)) if mask & (1 << index)}
        score = scores(background)
        rows.append({"background": [code(point) for point in sorted(background)], "scores": score, "minimizer_face": list(minimizers(score))})
    strict_backgrounds = [[[-3, 5], [5, -3]], [[-2, 6], [4, 0]], [[-2, 6], [6, -2]], [[-1, 3], [5, -3]]]
    cap_census = {str(cap): sum(max(abs(value) for point in background for value in point) <= cap for background in strict_backgrounds) for cap in (4, 5, 6)}
    return {
        "schema": "exact-recurrent-first-host-chart-confinement-transfer/v1",
        "scope": {"host_id": HOST_ID, "chart": "integer cells [0,3] x [0,3]", "hypotheses": ["background chart-confined", "background disjoint from five-response union"], "responses": list(RESPONSES)},
        "chart_decomposition": {"chart_points": [code(point) for point in sorted(chart)], "response_union": [code(point) for point in sorted(union)], "response_disjoint_complement": [code(point) for point in sorted(complement)]},
        "background_rows": rows,
        "strict_reversal_cap_census": cap_census,
        "aggregate": {
            "chart_points": len(chart),
            "response_union_points": len(union),
            "response_disjoint_chart_points": len(complement),
            "chart_response_disjoint_backgrounds": len(rows),
            "safe_backgrounds": sum(tuple(row["minimizer_face"]) == REOPENINGS for row in rows),
            "strict_reversals_global": len(strict_backgrounds),
            "strict_reversals_chart_confined": sum(all(0 <= value <= 3 for point in background for value in point) for background in strict_backgrounds),
        },
        "conclusion": {"chart_complement_equals_safe_five_cell_class": 1, "chart_confinement_and_response_disjointness_excludes_strict_reversals": 1, "chart_confinement_and_response_disjointness_excludes_original_response_ties": 1, "conditional_selector_face": list(REOPENINGS)},
        "honesty": {"physical_source_proves_chart_confinement": 0, "physical_source_proves_response_disjointness": 0, "physical_background_coverage_proved": 0, "legal_reopening_proved": 0, "recurrent_child_rows_populated": 0, "strict_lyapunov_certificate_proved": 0, "all_n_proved_by_checker": 0},
    }


def audit_sources(root: Path, manifest: dict[str, Any]) -> None:
    safe = load_json(root, SAFE_PATH)
    strict = load_json(root, STRICT_PATH)
    complement = manifest["chart_decomposition"]["response_disjoint_complement"]
    require(complement == ["00", "01", "11", "22", "33"], "chart complement")
    require(safe.get("scope", {}).get("background_universe") == complement, "safe universe linkage")
    require(safe.get("aggregate", {}).get("background_subsets") == 32, "safe subset census")
    require(safe.get("aggregate", {}).get("selector_order_preserved_subsets") == 32, "safe selector census")
    require(safe.get("honesty", {}).get("all_physical_backgrounds_lie_in_declared_class") == 0, "safe physical honesty")

    observed_strict = [row.get("background") for row in strict.get("strict_reversals", [])]
    expected_strict = [[[-3, 5], [5, -3]], [[-2, 6], [4, 0]], [[-2, 6], [6, -2]], [[-1, 3], [5, -3]]]
    require(observed_strict == expected_strict, "strict background linkage")
    require(strict.get("aggregate", {}).get("radius_census") == {"5": 2, "6": 2}, "strict radius census")
    require(strict.get("honesty", {}).get("physical_two_point_background_coverage_proved") == 0, "strict physical honesty")


def compile_manifest(root: Path) -> dict[str, Any]:
    manifest = expected_manifest()
    audit_sources(root, manifest)
    require(manifest["aggregate"]["safe_backgrounds"] == 32, "safe chart census")
    require(manifest["aggregate"]["strict_reversals_chart_confined"] == 0, "strict chart exclusion")
    require(manifest["strict_reversal_cap_census"] == {"4": 0, "5": 2, "6": 4}, "cap transfer")
    return manifest


def validate(manifest: dict[str, Any], root: Path) -> None:
    require(manifest == compile_manifest(root), "manifest differs from exact chart transfer")
    require(all(tuple(row["minimizer_face"]) == REOPENINGS for row in manifest["background_rows"]), "chart minimizer face")
    require(manifest.get("honesty", {}).get("physical_source_proves_chart_confinement") == 0, "chart-source honesty")
    require(manifest.get("honesty", {}).get("all_n_proved_by_checker") == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, Any], root: Path) -> int:
    mutations = [
        lambda item: item["aggregate"].update(chart_points=15),
        lambda item: item["aggregate"].update(response_union_points=10),
        lambda item: item["aggregate"].update(safe_backgrounds=31),
        lambda item: item["chart_decomposition"]["response_disjoint_complement"].pop(),
        lambda item: item["background_rows"].pop(),
        lambda item: item["background_rows"][0].update(minimizer_face=["3012"]),
        lambda item: item["strict_reversal_cap_census"].update({"4": 1}),
        lambda item: item["conclusion"].update(chart_complement_equals_safe_five_cell_class=0),
        lambda item: item["conclusion"].update(chart_confinement_and_response_disjointness_excludes_original_response_ties=0),
        lambda item: item["honesty"].update(physical_source_proves_chart_confinement=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate, root)
        except (AuditError, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "mutation audit")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    arguments = parser.parse_args()
    root = repository_root()
    manifest = compile_manifest(root)
    if arguments.write:
        arguments.write.parent.mkdir(parents=True, exist_ok=True)
        arguments.write.write_text(json.dumps(manifest, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    if arguments.check:
        observed = json.loads(arguments.check.read_text(encoding="utf-8"))
        validate(observed, root)
    print(json.dumps({"checker": "exact-recurrent-first-host-chart-confinement-transfer", **manifest["aggregate"], "mutation_corruptions_rejected": mutation_audit(manifest, root), **manifest["honesty"]}, sort_keys=True))


if __name__ == "__main__":
    main()
