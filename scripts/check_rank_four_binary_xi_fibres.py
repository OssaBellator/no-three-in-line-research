#!/usr/bin/env python3
"""Check fixed-centre rank-four binary-Xi conditional fibres."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial
from pathlib import Path
from typing import Any

Pattern = tuple[int, int, int, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--enumeration-limit", type=int, default=8)
    return parser.parse_args()


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def parse_indices(raw: Any, label: str, n: int, centre: int) -> set[int]:
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected list")
    result: set[int] = set()
    for pos, value in enumerate(raw):
        value = require_int(value, f"{label}[{pos}]")
        if value >= n or value == centre:
            raise ValueError(f"{label}[{pos}]: expected noncentre index in [0,n)")
        if value in result:
            raise ValueError(f"{label}: duplicate index {value}")
        result.add(value)
    return result


def parse_patterns(raw: Any, label: str, n: int, centre: int) -> list[Pattern]:
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected list")
    result: list[Pattern] = []
    seen: set[tuple[int, int, int]] = set()
    for pos, item in enumerate(raw):
        if not isinstance(item, list) or len(item) != 4:
            raise ValueError(f"{label}[{pos}]: expected [incident,tail,head,weight]")
        incident = require_int(item[0], f"{label}[{pos}][0]")
        tail = require_int(item[1], f"{label}[{pos}][1]")
        head = require_int(item[2], f"{label}[{pos}][2]")
        weight = require_int(item[3], f"{label}[{pos}][3]", minimum=1)
        if any(index >= n or index == centre for index in (incident, tail, head)):
            raise ValueError(f"{label}[{pos}]: indices must be noncentre members of [0,n)")
        if len({incident, tail, head}) != 3:
            raise ValueError(f"{label}[{pos}]: incident, tail, head must be distinct")
        key = (incident, tail, head)
        if key in seen:
            raise ValueError(f"{label}: duplicate pattern {key}")
        seen.add(key)
        result.append((incident, tail, head, weight))
    return result


def fibre_map(patterns: list[Pattern]) -> dict[int, list[tuple[int, int, int]]]:
    result: dict[int, list[tuple[int, int, int]]] = {}
    for incident, tail, head, weight in patterns:
        result.setdefault(incident, []).append((tail, head, weight))
    return result


def cycle_orders(block: tuple[int, ...]):
    first = min(block)
    rest = [x for x in block if x != first]
    for tail in permutations(rest):
        order = (first,) + tail
        yield order


def has_arc(order: tuple[int, ...], source: int, target: int) -> bool:
    size = len(order)
    return any(order[i] == source and order[(i + 1) % size] == target for i in range(size))


def enumerate_conditioned_expectation(
    n: int,
    centre: int,
    block_size: int,
    orientation: str,
    incident: int,
    fibre: list[tuple[int, int, int]],
) -> tuple[int, Fraction]:
    fixed_source, fixed_target = (
        (incident, centre) if orientation == "incoming" else (centre, incident)
    )
    available = [x for x in range(n) if x not in {centre, incident}]
    state_count = 0
    total_cost = 0
    for extras in combinations(available, block_size - 2):
        block = tuple(sorted((centre, incident, *extras)))
        for order in cycle_orders(block):
            if not has_arc(order, fixed_source, fixed_target):
                continue
            state_count += 1
            total_cost += sum(
                weight
                for tail, head, weight in fibre
                if has_arc(order, tail, head)
            )
    if state_count == 0:
        raise ValueError("conditioned family is empty")
    return state_count, Fraction(total_cost, state_count)


def choose_dyadic_level(fibre: list[tuple[int, int, int]]) -> dict[str, int]:
    total = sum(weight for _, _, weight in fibre)
    max_weight = max(weight for _, _, weight in fibre)
    levels = max_weight.bit_length()
    counts: dict[int, int] = {}
    for _, _, weight in fibre:
        level = weight.bit_length() - 1
        counts[level] = counts.get(level, 0) + 1
    level = max(counts, key=lambda j: (1 << j) * counts[j])
    lower = 1 << level
    count = counts[level]
    if 2 * levels * lower * count < total:
        raise ValueError("dyadic mass bound failed")
    return {
        "level": level,
        "lower_weight": lower,
        "upper_weight_exclusive": 2 * lower,
        "level_size": count,
        "level_count": levels,
        "fibre_weight": total,
    }


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        n = require_int(payload.get("n"), "n", minimum=4)
        centre = require_int(payload.get("centre"), "centre")
        if centre >= n:
            raise ValueError("centre must lie in [0,n)")
        block_size = require_int(payload.get("block_size"), "block_size", minimum=3)
        if block_size > n:
            raise ValueError("block_size must not exceed n")
        budget = require_int(payload.get("budget"), "budget", minimum=1)
        target_fan = require_int(payload.get("target_fan"), "target_fan", minimum=1)
        incoming_admissible = parse_indices(
            payload.get("incoming_source_admissible"),
            "incoming_source_admissible",
            n,
            centre,
        )
        outgoing_admissible = parse_indices(
            payload.get("outgoing_source_admissible"),
            "outgoing_source_admissible",
            n,
            centre,
        )
        incoming = parse_patterns(
            payload.get("incoming_patterns"), "incoming_patterns", n, centre
        )
        outgoing = parse_patterns(
            payload.get("outgoing_patterns"), "outgoing_patterns", n, centre
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    incoming_fibres = fibre_map(incoming)
    outgoing_fibres = fibre_map(outgoing)
    denominator = (n - 2) * (n - 3)
    numerator_factor = block_size - 3
    if numerator_factor <= 0:
        raise SystemExit("check failed: block_size must be at least 4 for rank four")

    def fibre_weight(fibres, incident):
        return sum(weight for _, _, weight in fibres.get(incident, []))

    light_incoming = sorted(
        r for r in incoming_admissible
        if numerator_factor * fibre_weight(incoming_fibres, r) < budget * denominator
    )
    light_outgoing = sorted(
        s for s in outgoing_admissible
        if numerator_factor * fibre_weight(outgoing_fibres, s) < budget * denominator
    )

    result: dict[str, Any] = {
        "n": n,
        "centre": centre,
        "block_size": block_size,
        "kappa": f"{numerator_factor}/{denominator}",
        "budget": budget,
        "incoming_admissible_count": len(incoming_admissible),
        "outgoing_admissible_count": len(outgoing_admissible),
        "light_incoming": light_incoming,
        "light_outgoing": light_outgoing,
        "incoming_total_weight": sum(weight for _, _, _, weight in incoming),
        "outgoing_total_weight": sum(weight for _, _, _, weight in outgoing),
        "D_B4_total_weight": sum(weight for _, _, _, weight in incoming + outgoing),
    }

    if light_incoming or light_outgoing:
        orientation = "incoming" if light_incoming else "outgoing"
        incident = (light_incoming or light_outgoing)[0]
        fibres = incoming_fibres if orientation == "incoming" else outgoing_fibres
        weight = fibre_weight(fibres, incident)
        result.update({
            "outcome": "cheap_conditioned_fibre",
            "orientation": orientation,
            "incident_index": incident,
            "fibre_weight": weight,
            "normalized_fibre_load": str(Fraction(numerator_factor * weight, denominator)),
        })
    else:
        heavy = []
        for orientation, admissible, fibres in (
            ("incoming", incoming_admissible, incoming_fibres),
            ("outgoing", outgoing_admissible, outgoing_fibres),
        ):
            for incident in admissible:
                weight = fibre_weight(fibres, incident)
                if numerator_factor * weight < budget * denominator:
                    raise SystemExit("check failed: heavy-fibre alternative violated")
                heavy.append((weight, orientation, incident))
        if not heavy:
            raise SystemExit("check failed: no admissible heavy fibre")
        weight, orientation, incident = max(heavy)
        fibres = incoming_fibres if orientation == "incoming" else outgoing_fibres
        fibre = fibres.get(incident, [])
        dyadic = choose_dyadic_level(fibre)
        if dyadic["level_size"] >= target_fan:
            outcome = "uniform_partner_fan"
        else:
            outcome = "multiplicity_core"
            if 2 * dyadic["level_count"] * target_fan * dyadic["lower_weight"] <= weight:
                raise SystemExit("check failed: multiplicity lower bound violated")
        result.update({
            "outcome": outcome,
            "heavy_incoming_count": len(incoming_admissible),
            "heavy_outgoing_count": len(outgoing_admissible),
            "orientation": orientation,
            "incident_index": incident,
            "target_fan": target_fan,
            **dyadic,
        })

    orientation = result["orientation"]
    incident = result["incident_index"]
    fibres = incoming_fibres if orientation == "incoming" else outgoing_fibres
    fibre = fibres.get(incident, [])
    expected_formula = Fraction(
        numerator_factor * sum(weight for _, _, weight in fibre),
        denominator,
    )
    result["expected_fibre_cost_formula"] = str(expected_formula)

    if n <= args.enumeration_limit:
        states, expected_enum = enumerate_conditioned_expectation(
            n, centre, block_size, orientation, incident, fibre
        )
        formula_states = comb(n - 2, block_size - 2) * factorial(block_size - 2)
        if states != formula_states:
            raise SystemExit(
                f"check failed: conditioned state count {states} != {formula_states}"
            )
        if expected_enum != expected_formula:
            raise SystemExit(
                f"check failed: expected cost {expected_enum} != {expected_formula}"
            )
        result["conditioned_state_count"] = states
        result["conditioned_state_count_formula"] = formula_states
        result["expected_fibre_cost_enumerated"] = str(expected_enum)

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
