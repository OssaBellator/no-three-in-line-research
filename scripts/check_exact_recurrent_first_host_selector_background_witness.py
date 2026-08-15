#!/usr/bin/env python3
"""Validate an exact background-completion selector witness for the first host.

The checker proves non-identifiability from omitted background data. It does not
assert that the nonempty completion is a globally legal construction state.
"""
from __future__ import annotations

import argparse
import copy
import json
from itertools import combinations
from pathlib import Path
from typing import Any


Point = tuple[int, int]


class BackgroundWitnessError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise BackgroundWitnessError(message)


def response_points(permutation: str) -> tuple[Point, ...]:
    require(
        isinstance(permutation, str)
        and len(permutation) == 4
        and set(permutation) == set("0123"),
        f"invalid response permutation {permutation!r}",
    )
    return tuple((row, int(column)) for row, column in enumerate(permutation))


def parse_background(values: Any, context: str) -> tuple[Point, ...]:
    require(isinstance(values, list), f"{context}: background must be a list")
    parsed: list[Point] = []
    for index, value in enumerate(values):
        require(
            isinstance(value, list)
            and len(value) == 2
            and all(isinstance(coordinate, int) for coordinate in value),
            f"{context}[{index}]: invalid point",
        )
        parsed.append((value[0], value[1]))
    require(len(parsed) == len(set(parsed)), f"{context}: duplicate point")
    return tuple(parsed)


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def complete_score(permutation: str, background: tuple[Point, ...]) -> int:
    response = response_points(permutation)
    response_set = set(response)
    require(
        response_set.isdisjoint(background),
        f"background overlaps response {permutation}",
    )
    points = response + background
    return sum(
        1
        for triple in combinations(points, 3)
        if collinear(*triple) and any(point in response_set for point in triple)
    )


def line_value(signature: tuple[int, int, int], point: Point) -> int:
    return signature[0] * point[0] + signature[1] * point[1] + signature[2]


def validate(witness: dict[str, Any]) -> dict[str, Any]:
    require(
        witness.get("schema")
        == "exact-recurrent-first-host-selector-background-witness/v1",
        "schema mismatch",
    )
    require(
        witness.get("score_rule")
        == "number of collinear triples in response union background containing at least one response point",
        "score rule mismatch",
    )

    host = witness.get("host")
    require(isinstance(host, dict), "host object required")
    require(host.get("upstream_id") == "s4-75b04c45c1c8eac2", "host id mismatch")
    require(host.get("deletions") == ["02", "20"], "deletion trace mismatch")
    require(host.get("blocker") == "b4-8a44614df456", "blocker mismatch")
    require(host.get("response_family") == ["3012", "3210"], "response family mismatch")
    require(host.get("intrinsic_selector") == "3012", "intrinsic selector mismatch")
    require(host.get("intrinsic_gap") == 3, "intrinsic gap mismatch")

    perturbation = witness.get("perturbation")
    require(isinstance(perturbation, dict), "perturbation object required")
    point_value = perturbation.get("point")
    require(
        isinstance(point_value, list)
        and len(point_value) == 2
        and all(isinstance(value, int) for value in point_value),
        "perturbation point invalid",
    )
    point = (point_value[0], point_value[1])
    selected_signature = tuple(perturbation.get("selected_line_signature", []))
    competitor_signature = tuple(perturbation.get("competitor_line_signature", []))
    require(selected_signature == (1, -1, -1), "selected line signature mismatch")
    require(competitor_signature == (1, 1, -3), "competitor line signature mismatch")
    require(perturbation.get("selected_line") == "x-y-1=0", "selected line text mismatch")
    require(perturbation.get("competitor_line") == "x+y-3=0", "competitor line text mismatch")
    require(line_value(selected_signature, point) == 0, "point is not on selected line")
    require(line_value(competitor_signature, point) != 0, "point lies on competitor line")

    completions = witness.get("background_completions")
    require(
        isinstance(completions, list) and len(completions) == 2,
        "two background completions required",
    )
    expected_ids = ["empty-background", "one-point-on-selected-line"]
    observed_faces: list[tuple[str, ...]] = []
    observed_scores: list[dict[str, int]] = []

    for index, completion in enumerate(completions):
        require(isinstance(completion, dict), f"completion[{index}] object required")
        require(completion.get("id") == expected_ids[index], f"completion[{index}] id mismatch")
        background = parse_background(completion.get("background"), f"completion[{index}] background")
        if index == 0:
            require(background == (), "first completion must have empty background")
        else:
            require(background == (point,), "second completion must contain perturbation point")

        scores = {
            permutation: complete_score(permutation, background)
            for permutation in host["response_family"]
        }
        require(completion.get("scores") == scores, f"completion[{index}] score mismatch")
        minimum = min(scores.values())
        face = tuple(sorted(permutation for permutation, score in scores.items() if score == minimum))
        require(completion.get("minimizer_face") == list(face), f"completion[{index}] face mismatch")
        require(completion.get("selector") == min(face), f"completion[{index}] selector mismatch")
        observed_faces.append(face)
        observed_scores.append(scores)

    require(observed_scores[0] == {"3012": 1, "3210": 4}, "baseline scores mismatch")
    require(observed_faces[0] == ("3012",), "baseline minimizer must be unique")
    require(observed_scores[1] == {"3012": 4, "3210": 4}, "perturbed scores mismatch")
    require(observed_faces[1] == ("3012", "3210"), "perturbed minimizer must be a tie")
    require(
        observed_scores[1]["3012"] - observed_scores[0]["3012"] == host["intrinsic_gap"],
        "selected perturbation must consume the intrinsic gap exactly",
    )
    require(
        observed_scores[1]["3210"] - observed_scores[0]["3210"] == 0,
        "competitor score must remain unchanged",
    )

    interpretation = witness.get("interpretation")
    require(isinstance(interpretation, dict), "interpretation required")
    require(
        interpretation.get("claim")
        == "The populated first-host record does not determine a unique complete-score selector: two completions of its omitted background field give different minimizer faces.",
        "claim changed",
    )
    require(
        interpretation.get("nonclaim")
        == "The nonempty completion is an exact affine schema witness; this manifest does not assert that it occurs in every or any globally legal repair state.",
        "nonclaim changed",
    )

    expected_honesty = {
        "background_selector_nonidentifiability_proved": 1,
        "global_physical_realizability_of_background_completions": 0,
        "global_selector_instability_proved": 0,
        "legal_repair_transition_proved": 0,
        "recurrent_offspring_row_complete": 0,
        "strict_lyapunov_certificate_proved": 0,
        "all_n_proved_by_checker": 0,
    }
    require(witness.get("honesty") == expected_honesty, "honesty mismatch")

    return {
        "host": host["upstream_id"],
        "baseline_selector": "3012",
        "baseline_gap": 3,
        "perturbation_point": list(point),
        "baseline_score_3012": observed_scores[0]["3012"],
        "baseline_score_3210": observed_scores[0]["3210"],
        "perturbed_score_3012": observed_scores[1]["3012"],
        "perturbed_score_3210": observed_scores[1]["3210"],
        "perturbed_minimizer_face_size": len(observed_faces[1]),
        "background_selector_nonidentifiability_proved": 1,
        "global_selector_instability_proved": 0,
        "legal_repair_transition_proved": 0,
        "all_n_proved_by_checker": 0,
    }


def mutation_audit(witness: dict[str, Any]) -> int:
    mutations = [
        lambda item: item.update(schema="wrong"),
        lambda item: item["host"].update(upstream_id="wrong"),
        lambda item: item["host"].update(intrinsic_gap=2),
        lambda item: item["perturbation"].update(point=[4, 2]),
        lambda item: item["perturbation"].update(selected_line_signature=[1, 1, -3]),
        lambda item: item["background_completions"].pop(),
        lambda item: item["background_completions"][0]["scores"].update(**{"3012": 2}),
        lambda item: item["background_completions"][1].update(minimizer_face=["3012"]),
        lambda item: item["background_completions"][1].update(selector="3210"),
        lambda item: item["interpretation"].update(nonclaim="globally realized"),
        lambda item: item["honesty"].update(global_selector_instability_proved=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(witness)
        mutate(candidate)
        try:
            validate(candidate)
        except (BackgroundWitnessError, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "mutation audit accepted corrupted witness")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--witness", type=Path, required=True)
    args = parser.parse_args()
    witness = json.loads(args.witness.read_text(encoding="utf-8"))
    result = validate(witness)
    result["mutation_corruptions_rejected"] = mutation_audit(witness)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
