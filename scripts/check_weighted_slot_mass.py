#!/usr/bin/env python3
"""Verify the PP3fi weighted slot-mass local-lemma endpoint.

Input is a JSON object with a unique string list ``slots`` and an ``events``
list.  Every event has a unique ``name``, a list of one to three distinct slot
names, and an exact rational ``probability`` encoded as an integer, a string
accepted by fractions.Fraction, or an object with integer numerator and
denominator fields.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_fraction(raw: Any, context: str) -> Fraction:
    if isinstance(raw, bool):
        raise ValueError(f"{context}: booleans are not probabilities")
    if isinstance(raw, int):
        value = Fraction(raw)
    elif isinstance(raw, str):
        try:
            value = Fraction(raw)
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError(f"{context}: invalid rational string") from exc
    elif isinstance(raw, dict):
        numerator = raw.get("numerator")
        denominator = raw.get("denominator")
        if (
            isinstance(numerator, bool)
            or isinstance(denominator, bool)
            or not isinstance(numerator, int)
            or not isinstance(denominator, int)
        ):
            raise ValueError(f"{context}: malformed rational object")
        try:
            value = Fraction(numerator, denominator)
        except ZeroDivisionError as exc:
            raise ValueError(f"{context}: zero denominator") from exc
    else:
        raise ValueError(f"{context}: unsupported probability encoding")
    if value < 0 or value > 1:
        raise ValueError(f"{context}: probability outside [0,1]")
    return value


def fraction_json(value: Fraction) -> dict[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value),
        "decimal": float(value),
    }


def load_instance(path: Path) -> tuple[tuple[str, ...], tuple[dict[str, Any], ...]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON value must be an object")

    raw_slots = payload.get("slots")
    raw_events = payload.get("events")
    if not isinstance(raw_slots, list) or not raw_slots:
        raise ValueError("slots must be a nonempty list")
    if not isinstance(raw_events, list):
        raise ValueError("events must be a list")

    slots: list[str] = []
    for index, slot in enumerate(raw_slots):
        if not isinstance(slot, str) or not slot:
            raise ValueError(f"slot {index}: expected a nonempty string")
        slots.append(slot)
    if len(set(slots)) != len(slots):
        raise ValueError("slot names must be unique")
    slot_set = set(slots)

    events: list[dict[str, Any]] = []
    names: set[str] = set()
    for index, raw in enumerate(raw_events):
        if not isinstance(raw, dict):
            raise ValueError(f"event {index}: expected an object")
        name = raw.get("name")
        event_slots = raw.get("slots")
        if not isinstance(name, str) or not name:
            raise ValueError(f"event {index}: invalid name")
        if name in names:
            raise ValueError(f"event {index}: duplicate name {name!r}")
        names.add(name)
        if not isinstance(event_slots, list) or not 1 <= len(event_slots) <= 3:
            raise ValueError(f"event {name}: slots must have length one to three")
        if any(not isinstance(slot, str) or slot not in slot_set for slot in event_slots):
            raise ValueError(f"event {name}: unknown or malformed slot")
        if len(set(event_slots)) != len(event_slots):
            raise ValueError(f"event {name}: repeated slot")
        probability = parse_fraction(raw.get("probability"), f"event {name}")
        events.append(
            {
                "name": name,
                "slots": tuple(event_slots),
                "probability": probability,
            }
        )
    return tuple(slots), tuple(events)


def analyze(slots: tuple[str, ...], events: tuple[dict[str, Any], ...]) -> dict[str, Any]:
    incident_mass = {slot: Fraction(0) for slot in slots}
    incident_events = {slot: 0 for slot in slots}
    for event in events:
        probability: Fraction = event["probability"]
        for slot in event["slots"]:
            incident_mass[slot] += probability
            incident_events[slot] += 1

    maximum_probability = max(
        (event["probability"] for event in events), default=Fraction(0)
    )
    maximum_mass = max(incident_mass.values(), default=Fraction(0))
    simple_criterion = (
        maximum_probability <= Fraction(1, 4)
        and maximum_mass <= Fraction(1, 12)
    )

    exact_checks: list[dict[str, Any]] = []
    exact_all_hold = True
    for index, event in enumerate(events):
        event_slot_set = set(event["slots"])
        neighbor_indices = [
            other_index
            for other_index, other in enumerate(events)
            if other_index != index and event_slot_set.intersection(other["slots"])
        ]
        product = Fraction(1)
        neighbor_activity_sum = Fraction(0)
        for other_index in neighbor_indices:
            activity = 2 * events[other_index]["probability"]
            product *= 1 - activity
            neighbor_activity_sum += activity
        activity = 2 * event["probability"]
        right_side = activity * product
        holds = event["probability"] <= right_side
        exact_all_hold = exact_all_hold and holds
        exact_checks.append(
            {
                "name": event["name"],
                "rank": len(event["slots"]),
                "neighbor_count": len(neighbor_indices),
                "neighbor_activity_sum": fraction_json(neighbor_activity_sum),
                "lll_right_side": fraction_json(right_side),
                "holds": holds,
            }
        )

    return {
        "slot_count": len(slots),
        "event_count": len(events),
        "maximum_event_probability": fraction_json(maximum_probability),
        "maximum_incident_probability_mass": fraction_json(maximum_mass),
        "PP3fi_simple_criterion": simple_criterion,
        "exact_activity_inequalities_hold": exact_all_hold,
        "slots": {
            slot: {
                "incident_event_count": incident_events[slot],
                "incident_probability_mass": fraction_json(incident_mass[slot]),
            }
            for slot in slots
        },
        "events": exact_checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("instance", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        slots, events = load_instance(args.instance)
        result = analyze(slots, events)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
