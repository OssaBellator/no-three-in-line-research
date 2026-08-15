#!/usr/bin/env python3
"""Validate exact one-count routing for the populated side-four sample credits."""
from __future__ import annotations

import copy
import hashlib
import json
from collections import Counter, defaultdict
from itertools import combinations
from math import gcd
from pathlib import Path
from typing import Any


class SampleCreditRoutingError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise SampleCreditRoutingError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


SAMPLE_PATH = "data/prime_power_side_four_actual_background_sample_batch.json"
ROUTING_PATH = "data/prime_power_side_four_sample_credit_routing_contract.json"
EXPECTED_SAMPLE_SHA256 = "71ba5fcea70f61c5e94e40a635b7eddaa8cb72c8c0cdda9fb78f0f56a84609a0"
EXPECTED_ROUTING_SHA256 = "f4920483e99ed4d53da28fc5a752391e570cfceab828937e5d63ac36d91553b5"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise SampleCreditRoutingError("unable to locate repository root")


def canonical_line(
    first: tuple[int, int], second: tuple[int, int]
) -> tuple[int, int, int]:
    require(first != second, "distinct points required")
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
    owner: str,
    background_id: str,
) -> dict[str, Any]:
    line_text = ",".join(str(value) for value in line)
    return {
        "structural_owner": f"return:{predecessor}",
        "fate": "repeated-return",
        "collision_class": "-",
        "local_line_class": f"rank{rank}:{line_text}:h2:k2",
        "interface_label": "side4-target01",
        "remaining_provenance": {
            "background_id": background_id,
            "credit_class": f"rank{rank}",
            "crt_provenance": "not-applied/sample-profile/v1",
            "entering_owner": owner,
        },
    }


def compile_credits(sample: dict[str, Any]) -> list[dict[str, Any]]:
    require(digest(sample) == EXPECTED_SAMPLE_SHA256, "sample digest")
    profile = sample["profile"]
    selector = profile["selected_response"]
    response = tuple((source, int(selector[source])) for source in range(4))
    background = tuple(tuple(point) for point in profile["background_points"])
    background_codes = {point: edge(point) for point in background}
    background_id = profile["background_id"]
    credits: list[dict[str, Any]] = []

    for response_point in response:
        for first, second in combinations(background, 2):
            line = canonical_line(first, second)
            if line[0] == 0 or line[1] == 0 or not on_line(line, response_point):
                continue
            owner = edge(response_point)
            predecessor = f"{response_point[0]}{response_point[0]}"
            weight = f"w_return_{predecessor}_rank1"
            points = sorted((background_codes[first], background_codes[second]))
            credits.append({
                "credit_id": f"r1-{owner}-{points[0]}-{points[1]}",
                "rank": 1,
                "response_edges": [owner],
                "background_points": points,
                "line_equation": list(line),
                "entering_owner": owner,
                "returned_predecessor": predecessor,
                "coefficient": 1,
                "child_key": child_key(
                    predecessor=predecessor,
                    rank=1,
                    line=line,
                    owner=owner,
                    background_id=background_id,
                ),
                "weight_symbol": weight,
                "positive_weight_required": 1,
            })

    for first, second in combinations(response, 2):
        line = canonical_line(first, second)
        response_edges = sorted((edge(first), edge(second)))
        owner_point = max(first, second)
        owner = edge(owner_point)
        predecessor = f"{owner_point[0]}{owner_point[0]}"
        weight = f"w_return_{predecessor}_rank2"
        for background_point in background:
            if not on_line(line, background_point):
                continue
            background_code = background_codes[background_point]
            credits.append({
                "credit_id": (
                    f"r2-{response_edges[0]}-{response_edges[1]}-{background_code}"
                ),
                "rank": 2,
                "response_edges": response_edges,
                "background_points": [background_code],
                "line_equation": list(line),
                "entering_owner": owner,
                "returned_predecessor": predecessor,
                "coefficient": 1,
                "child_key": child_key(
                    predecessor=predecessor,
                    rank=2,
                    line=line,
                    owner=owner,
                    background_id=background_id,
                ),
                "weight_symbol": weight,
                "positive_weight_required": 1,
            })
    return sorted(credits, key=lambda item: item["credit_id"])


def compress_credits(credits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], int] = defaultdict(int)
    for credit in credits:
        key = credit["child_key"]
        class_id = f"{key['structural_owner']}|{key['local_line_class']}"
        grouped[(class_id, credit["weight_symbol"])] += credit["coefficient"]
    return [
        {"class_id": class_id, "coefficient": coefficient, "weight_symbol": weight}
        for (class_id, weight), coefficient in sorted(grouped.items())
    ]


def validate(sample: dict[str, Any], routing: dict[str, Any]) -> list[dict[str, Any]]:
    require(
        routing["sample_contract_sha256"] == EXPECTED_SAMPLE_SHA256,
        "sample binding",
    )
    require(digest(routing) == EXPECTED_ROUTING_SHA256, "routing contract digest")
    credits = compile_credits(sample)
    require(routing["credits"] == credits, "exact routed credit list")
    require(len(credits) == 4, "credit count")
    require(len({credit["credit_id"] for credit in credits}) == 4, "unique credits")
    require(Counter(credit["rank"] for credit in credits) == Counter({1: 2, 2: 2}), "rank census")
    require(
        Counter(credit["returned_predecessor"] for credit in credits)
        == Counter({"22": 3, "00": 1}),
        "returned predecessor census",
    )
    require(
        all(
            credit["coefficient"] == 1
            and credit["positive_weight_required"] == 1
            and credit["weight_symbol"]
            and set(credit["child_key"]) == {
                "structural_owner",
                "fate",
                "collision_class",
                "local_line_class",
                "interface_label",
                "remaining_provenance",
            }
            for credit in credits
        ),
        "complete child keys and symbolic positive weights",
    )
    compressed = compress_credits(credits)
    require(routing["compressed_child_classes"] == compressed, "compressed child classes")
    terms = [
        [item["weight_symbol"], item["coefficient"]]
        for item in compressed
    ]
    require(
        routing["weighted_return_expression"]
        == {"terms": terms, "strict_parent_budget": None},
        "symbolic weighted expression",
    )
    require(routing["accounting"] == {
        "line_category_role": "certificate-source-only",
        "return_category_role": "offspring-charge",
        "credit_counting_rule": "each recreated credit occurs in exactly one return child charge; line coefficients certify but do not add a second offspring term",
        "rank_three_rule": "rank-three total is zero for this sample",
    }, "non-double-counting accounting")
    require(routing["aggregate"] == {
        "credits": 4,
        "rank_one_credits": 2,
        "rank_two_credits": 2,
        "rank_three_credits": 0,
        "child_classes": 3,
        "line_certificate_total": 4,
        "return_charge_total": 4,
        "returned_predecessor_census": {"00": 1, "22": 3},
        "unresolved_positive_weight_symbols": 3,
    }, "routing aggregate")
    require(routing["honesty"] == {
        "sample_credit_partition_complete": 1,
        "sample_child_routing_complete": 1,
        "sample_child_keys_complete_for_populated_credits": 1,
        "sample_child_weights_complete": 0,
        "sample_weighted_row_strict": 0,
        "global_child_provenance_complete": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, "routing honesty")
    return credits


def mutation_audit(sample: dict[str, Any], routing: dict[str, Any]) -> int:
    mutations = [
        lambda item: item["credits"].pop(),
        lambda item: item["credits"][0].update(returned_predecessor="22"),
        lambda item: item["credits"][0].update(coefficient=2),
        lambda item: item["credits"][0]["child_key"].pop("fate"),
        lambda item: item["credits"][0]["child_key"].update(collision_class="projected"),
        lambda item: item["credits"][0].update(weight_symbol=""),
        lambda item: item["credits"][0].update(positive_weight_required=0),
        lambda item: item["compressed_child_classes"][2].update(coefficient=1),
        lambda item: item["weighted_return_expression"].update(strict_parent_budget=4),
        lambda item: item["accounting"].update(line_category_role="offspring-charge"),
        lambda item: item["aggregate"].update(return_charge_total=3),
        lambda item: item["honesty"].update(sample_child_weights_complete=1),
        lambda item: item["honesty"].update(sample_weighted_row_strict=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(routing)
        mutate(bad)
        try:
            validate(sample, bad)
        except SampleCreditRoutingError:
            rejected += 1
    require(rejected == len(mutations), "routing corruption accepted")
    return rejected


def main() -> None:
    root = repository_root()
    sample = json.loads((root / SAMPLE_PATH).read_text(encoding="utf-8"))
    routing = json.loads((root / ROUTING_PATH).read_text(encoding="utf-8"))
    credits = validate(sample, routing)
    print(json.dumps({
        "checker": "prime-power-side-four-sample-credit-routing",
        "routing_contract_sha256": EXPECTED_ROUTING_SHA256,
        "credit_count": len(credits),
        "child_class_count": len(routing["compressed_child_classes"]),
        "returned_predecessor_census": routing["aggregate"]["returned_predecessor_census"],
        "rejected_corruptions": mutation_audit(sample, routing),
        "sample_credit_partition_complete": 1,
        "sample_child_routing_complete": 1,
        "sample_child_keys_complete_for_populated_credits": 1,
        "sample_child_weights_complete": 0,
        "sample_weighted_row_strict": 0,
        "global_child_provenance_complete": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
