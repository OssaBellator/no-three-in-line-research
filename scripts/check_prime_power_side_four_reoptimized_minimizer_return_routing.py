#!/usr/bin/env python3
"""Validate return routing on the complete-line minimizer responses."""
from __future__ import annotations

import copy
import hashlib
import json
from collections import Counter, defaultdict
from itertools import combinations
from math import gcd
from pathlib import Path
from typing import Any


class ReoptimizedReturnRoutingError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ReoptimizedReturnRoutingError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


SCORES_PATH = "data/prime_power_side_four_joint_sample_complete_line_selector_scores.json"
ZERO_SAMPLE_PATH = "data/prime_power_side_four_actual_background_sample_batch.json"
BLOCKER_SAMPLE_PATH = "data/prime_power_side_four_blocker_actual_background_sample_batch.json"
ROUTING_PATH = "data/prime_power_side_four_reoptimized_minimizer_return_routing.json"
EXPECTED_SCORES_SHA256 = "c5a7f78ddef889aacdffc152b40945ed4b798f850c9aecbd20d4428f9ea63d0e"
EXPECTED_ZERO_SAMPLE_SHA256 = "71ba5fcea70f61c5e94e40a635b7eddaa8cb72c8c0cdda9fb78f0f56a84609a0"
EXPECTED_BLOCKER_SAMPLE_SHA256 = "39677a7e68826f9bf9702d3af8f3b4218138fa0bb1d885c6801d220dddcabeaf"
EXPECTED_ROUTING_SHA256 = "de7742146a77134b97d3ccb36c6112bd458cf8920e346c2e9e515777a9c5b2b6"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "data").is_dir():
            return candidate
    raise ReoptimizedReturnRoutingError("unable to locate repository root")


def canonical_line(
    first: tuple[int, int], second: tuple[int, int]
) -> tuple[int, int, int]:
    require(first != second, "distinct points")
    x1, y1 = first
    x2, y2 = second
    a, b, c = y1 - y2, x2 - x1, x1 * y2 - x2 * y1
    common = 0
    for value in (a, b, c):
        common = gcd(common, abs(value))
    require(common > 0, "nonzero line")
    a, b, c = a // common, b // common, c // common
    if a < 0 or (a == 0 and b < 0) or (a == 0 and b == 0 and c < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def on_line(line: tuple[int, int, int], point: tuple[int, int]) -> bool:
    a, b, c = line
    x, y = point
    return a * x + b * y + c == 0


def edge(point: tuple[int, int]) -> str:
    return f"{point[0]}{point[1]}"


def child_key(
    *,
    predecessor: str,
    rank: int,
    line: tuple[int, int, int],
    height: int,
    occupancy: int,
    owner: str,
    response: str,
    profile: dict[str, Any],
) -> dict[str, Any]:
    line_text = ",".join(str(value) for value in line)
    return {
        "structural_owner": f"return:{predecessor}",
        "fate": "repeated-return",
        "collision_class": profile.get("collision_key", "-"),
        "local_line_class": f"rank{rank}:{line_text}:h{height}:k{occupancy}",
        "interface_label": "side4-target01",
        "remaining_provenance": {
            "background_id": profile["background_id"],
            "blockers": profile.get("blockers", []),
            "credit_class": f"rank{rank}",
            "crt_provenance": profile["crt_provenance"],
            "entering_owner": owner,
            "response": response,
            "source_host_fate": profile.get("selected_fate", "zero-response"),
        },
    }


def compile_credits(response: str, profile: dict[str, Any]) -> list[dict[str, Any]]:
    require(len(response) == 4 and set(response) == set("0123"), "response permutation")
    points = tuple((source, int(response[source])) for source in range(4))
    background = tuple(tuple(point) for point in profile["background_points"])
    credits: list[dict[str, Any]] = []

    for response_point in points:
        for first, second in combinations(background, 2):
            line = canonical_line(first, second)
            if line[0] == 0 or line[1] == 0 or not on_line(line, response_point):
                continue
            owner = edge(response_point)
            predecessor = f"{response_point[0]}{response_point[0]}"
            occupancy = sum(on_line(line, point) for point in points)
            key = child_key(
                predecessor=predecessor,
                rank=1,
                line=line,
                height=2,
                occupancy=occupancy,
                owner=owner,
                response=response,
                profile=profile,
            )
            credits.append({
                "credit_id": f"rr1-{owner}-bg0-bg1",
                "rank": 1,
                "response_edges": [owner],
                "background_points": ["bg0", "bg1"],
                "line_equation": list(line),
                "entering_owner": owner,
                "returned_predecessor": predecessor,
                "coefficient": 1,
                "child_key": key,
                "weight_symbol": f"w_reopt_return_{predecessor}_rank1_k{occupancy}",
                "positive_weight_required": 1,
            })

    for first, second in combinations(points, 2):
        line = canonical_line(first, second)
        response_edges = sorted((edge(first), edge(second)))
        owner_point = max(first, second)
        owner = edge(owner_point)
        predecessor = f"{owner_point[0]}{owner_point[0]}"
        occupancy = sum(on_line(line, point) for point in points)
        height = sum(on_line(line, point) for point in background)
        for index, background_point in enumerate(background):
            if not on_line(line, background_point):
                continue
            key = child_key(
                predecessor=predecessor,
                rank=2,
                line=line,
                height=height,
                occupancy=occupancy,
                owner=owner,
                response=response,
                profile=profile,
            )
            credits.append({
                "credit_id": f"rr2-{response_edges[0]}-{response_edges[1]}-bg{index}",
                "rank": 2,
                "response_edges": response_edges,
                "background_points": [f"bg{index}"],
                "line_equation": list(line),
                "entering_owner": owner,
                "returned_predecessor": predecessor,
                "coefficient": 1,
                "child_key": key,
                "weight_symbol": f"w_reopt_return_{predecessor}_rank2_k{occupancy}",
                "positive_weight_required": 1,
            })

    for triple in combinations(points, 3):
        line = canonical_line(triple[0], triple[1])
        if not all(on_line(line, point) for point in triple[2:]):
            continue
        response_edges = sorted(edge(point) for point in triple)
        owner_point = max(triple)
        owner = edge(owner_point)
        predecessor = f"{owner_point[0]}{owner_point[0]}"
        occupancy = sum(on_line(line, point) for point in points)
        height = sum(on_line(line, point) for point in background)
        key = child_key(
            predecessor=predecessor,
            rank=3,
            line=line,
            height=height,
            occupancy=occupancy,
            owner=owner,
            response=response,
            profile=profile,
        )
        credits.append({
            "credit_id": "rr3-" + "-".join(response_edges),
            "rank": 3,
            "response_edges": response_edges,
            "background_points": [],
            "line_equation": list(line),
            "entering_owner": owner,
            "returned_predecessor": predecessor,
            "coefficient": 1,
            "child_key": key,
            "weight_symbol": f"w_reopt_return_{predecessor}_rank3_k{occupancy}",
            "positive_weight_required": 1,
        })
    return sorted(credits, key=lambda item: item["credit_id"])


def compress(credits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], int] = defaultdict(int)
    for credit in credits:
        key = credit["child_key"]
        class_id = (
            f"{key['structural_owner']}|{key['local_line_class']}"
            + (f"|collision:{key['collision_class']}" if key["collision_class"] != "-" else "")
        )
        grouped[(class_id, credit["weight_symbol"])] += credit["coefficient"]
    return [
        {"class_id": class_id, "coefficient": coefficient, "weight_symbol": weight}
        for (class_id, weight), coefficient in sorted(grouped.items())
    ]


def charge(credits: list[dict[str, Any]]) -> dict[str, int]:
    result = {f"{source}{source}": 0 for source in range(4)}
    for credit in credits:
        result[credit["returned_predecessor"]] += credit["coefficient"]
    return result


def validate(
    scores: dict[str, Any],
    zero_sample: dict[str, Any],
    blocker_sample: dict[str, Any],
    routing: dict[str, Any],
) -> None:
    require(digest(scores) == EXPECTED_SCORES_SHA256, "selector scores digest")
    require(digest(zero_sample) == EXPECTED_ZERO_SAMPLE_SHA256, "zero sample digest")
    require(digest(blocker_sample) == EXPECTED_BLOCKER_SAMPLE_SHA256, "blocker sample digest")
    require(digest(routing) == EXPECTED_ROUTING_SHA256, "routing digest")
    require(
        routing["inputs"]
        == {
            "selector_score_contract_sha256": EXPECTED_SCORES_SHA256,
            "zero_sample_sha256": EXPECTED_ZERO_SAMPLE_SHA256,
            "blocker_sample_sha256": EXPECTED_BLOCKER_SAMPLE_SHA256,
        },
        "routing input bindings",
    )

    zero_candidates = scores["rows"]["zero"]["complete_line_minimizer_face"]
    require(zero_candidates == ["2301", "2310", "3201"], "zero minimizer face")
    compiled_zero = []
    for response in zero_candidates:
        credits = compile_credits(response, zero_sample["profile"])
        require(not credits, f"{response}: unexpected zero-sample credit")
        compiled_zero.append({
            "response": response,
            "credits": [],
            "compressed_child_classes": [],
            "return_charge_by_predecessor": charge([]),
            "weighted_return_expression": [],
        })
    require(routing["rows"]["zero"] == {
        "host_id": zero_sample["profile"]["host_id"],
        "candidate_responses": compiled_zero,
        "candidate_return_rows_equal": 1,
        "return_terms_break_line_tie": 0,
    }, "zero reoptimized rows")

    blocker_response = scores["rows"]["blocker"]["complete_line_minimizer_face"]
    require(blocker_response == ["3210"], "blocker minimizer response")
    blocker_credits = compile_credits("3210", blocker_sample["profile"])
    require(len(blocker_credits) == 4, "four blocker rank-three credits")
    require(Counter(item["rank"] for item in blocker_credits) == Counter({3: 4}), "blocker rank census")
    require(charge(blocker_credits) == {"00": 0, "11": 0, "22": 1, "33": 3}, "blocker charge")
    blocker_compressed = compress(blocker_credits)
    require(blocker_compressed == [
        {
            "class_id": "return:22|rank3:1,1,-3:h0:k4|collision:02,20",
            "coefficient": 1,
            "weight_symbol": "w_reopt_return_22_rank3_k4",
        },
        {
            "class_id": "return:33|rank3:1,1,-3:h0:k4|collision:02,20",
            "coefficient": 3,
            "weight_symbol": "w_reopt_return_33_rank3_k4",
        },
    ], "blocker compressed classes")
    require(routing["rows"]["blocker"] == {
        "host_id": blocker_sample["profile"]["host_id"],
        "collision_key": "02,20",
        "candidate_response": "3210",
        "credits": blocker_credits,
        "compressed_child_classes": blocker_compressed,
        "return_charge_by_predecessor": charge(blocker_credits),
        "weighted_return_expression": [
            ["w_reopt_return_22_rank3_k4", 1],
            ["w_reopt_return_33_rank3_k4", 3],
        ],
    }, "blocker reoptimized row")

    require(routing["accounting"] == {
        "line_role": "certificate-source-only",
        "return_role": "offspring-charge",
        "credit_counting": "each recreated credit appears exactly once",
        "owner_rule": "absolute lexicographically maximal entering response edge in each recreated credit",
        "returned_predecessor_rule": "same-source identity edge",
    }, "accounting")
    require(routing["aggregate"] == {
        "candidate_responses": 4,
        "zero_candidate_responses": 3,
        "blocker_candidate_responses": 1,
        "recreated_credits": 4,
        "compressed_child_classes": 2,
        "unresolved_positive_weight_symbols": 2,
    }, "aggregate")
    require(routing["comparison"] == {
        "obsolete_zero_response": "2031",
        "obsolete_blocker_response": "3012",
        "obsolete_routing_reusable": 0,
        "zero_reoptimized_return_total": 0,
        "blocker_old_return_total": 5,
        "blocker_reoptimized_return_total": 4,
    }, "comparison")
    require(routing["conclusion"] == {
        "reoptimized_return_rows_complete": 1,
        "zero_return_terms_preserve_line_tie": 1,
        "complete_coupled_selector_resolved": 0,
        "remaining_terms": ["collision", "interface", "global child weights"],
    }, "conclusion")
    require(routing["honesty"] == {
        "joint_sample_reoptimized_return_routing_complete": 1,
        "zero_reoptimized_return_rows_complete": 1,
        "blocker_reoptimized_return_row_complete": 1,
        "reoptimized_child_weights_complete": 0,
        "joint_sample_complete_coupled_selector_terms_complete": 0,
        "joint_sample_full_compulsory_rows_complete": 0,
        "global_binding_constructed": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, "honesty")


def mutation_audit(
    scores: dict[str, Any],
    zero_sample: dict[str, Any],
    blocker_sample: dict[str, Any],
    routing: dict[str, Any],
) -> int:
    mutations = [
        lambda item: item["rows"]["zero"]["candidate_responses"].pop(),
        lambda item: item["rows"]["zero"].update(return_terms_break_line_tie=1),
        lambda item: item["rows"]["blocker"]["credits"].pop(),
        lambda item: item["rows"]["blocker"]["credits"][0].update(rank=2),
        lambda item: item["rows"]["blocker"]["credits"][0].update(returned_predecessor="33"),
        lambda item: item["rows"]["blocker"]["credits"][0]["child_key"].update(collision_class="-"),
        lambda item: item["rows"]["blocker"]["compressed_child_classes"][1].update(coefficient=2),
        lambda item: item["rows"]["blocker"]["return_charge_by_predecessor"].update({"33": 2}),
        lambda item: item["rows"]["blocker"].update(candidate_response="3012"),
        lambda item: item["accounting"].update(line_role="offspring-charge"),
        lambda item: item["aggregate"].update(recreated_credits=3),
        lambda item: item["comparison"].update(obsolete_routing_reusable=1),
        lambda item: item["conclusion"].update(complete_coupled_selector_resolved=1),
        lambda item: item["honesty"].update(reoptimized_child_weights_complete=1),
        lambda item: item["honesty"].update(complete_weighted_rows_strict=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(routing)
        mutate(bad)
        try:
            validate(scores, zero_sample, blocker_sample, bad)
        except ReoptimizedReturnRoutingError:
            rejected += 1
    require(rejected == len(mutations), "reoptimized routing corruption accepted")
    return rejected


def main() -> None:
    root = repository_root()
    scores = json.loads((root / SCORES_PATH).read_text(encoding="utf-8"))
    zero_sample = json.loads((root / ZERO_SAMPLE_PATH).read_text(encoding="utf-8"))
    blocker_sample = json.loads((root / BLOCKER_SAMPLE_PATH).read_text(encoding="utf-8"))
    routing = json.loads((root / ROUTING_PATH).read_text(encoding="utf-8"))
    validate(scores, zero_sample, blocker_sample, routing)
    print(json.dumps({
        "checker": "prime-power-side-four-reoptimized-minimizer-return-routing",
        "contract_sha256": EXPECTED_ROUTING_SHA256,
        "candidate_response_count": 4,
        "recreated_credit_count": 4,
        "compressed_child_class_count": 2,
        "zero_return_terms_break_line_tie": 0,
        "blocker_return_charge_by_predecessor": {"00": 0, "11": 0, "22": 1, "33": 3},
        "rejected_corruptions": mutation_audit(scores, zero_sample, blocker_sample, routing),
        "joint_sample_reoptimized_return_routing_complete": 1,
        "zero_reoptimized_return_rows_complete": 1,
        "blocker_reoptimized_return_row_complete": 1,
        "reoptimized_child_weights_complete": 0,
        "joint_sample_complete_coupled_selector_terms_complete": 0,
        "joint_sample_full_compulsory_rows_complete": 0,
        "global_binding_constructed": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
