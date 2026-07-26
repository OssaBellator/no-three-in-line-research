#!/usr/bin/env python3
"""Check the finite call-matrix invariants for complete second-host cancellation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_OUTCOMES = {
    "independent_cycle",
    "current_structure",
    "source_host",
    "explicit_host_failure",
    "robust_final_completion",
}
REQUIRED_TERMINAL_INTERFACES = {
    "conditional_hall",
    "alternating_component",
    "non_superregular_host",
    "distinguished_endpoint",
    "role_host_failure",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def require_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{label}: expected object")
    return value


def require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{label}: expected list")
    return value


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{label}: expected nonempty string")
    return value


def main() -> None:
    args = parse_args()
    try:
        payload = require_object(
            json.loads(args.input.read_text(encoding="utf-8")), "top-level JSON"
        )
        if payload.get("potential") != "Theta_E_plus":
            raise ValueError("potential must be Theta_E_plus")

        maximum_marked_size = require_int(
            payload.get("maximum_marked_size"), "maximum_marked_size", minimum=1
        )
        domain_loss_constant = require_int(
            payload.get("domain_loss_constant"),
            "domain_loss_constant",
            minimum=1,
        )

        raw_allowed = {
            require_string(item, "allowed_outcomes item")
            for item in require_list(payload.get("allowed_outcomes"), "allowed_outcomes")
        }
        if raw_allowed != REQUIRED_OUTCOMES:
            raise ValueError(
                "allowed_outcomes must equal the five exhaustive second-host outcomes"
            )

        raw_terminal = {
            require_string(item, "terminal_interfaces item")
            for item in require_list(
                payload.get("terminal_interfaces"), "terminal_interfaces"
            )
        }
        if raw_terminal != REQUIRED_TERMINAL_INTERFACES:
            raise ValueError(
                "terminal_interfaces must equal the five named interface classes"
            )

        blocks = require_list(payload.get("blocks"), "blocks")
        if not blocks:
            raise ValueError("blocks must be nonempty")

        total_marked = 0
        sum_squares = 0
        observed_outcomes: set[str] = set()
        normalized_blocks: list[dict[str, Any]] = []
        for pos, raw_block in enumerate(blocks):
            block = require_object(raw_block, f"blocks[{pos}]")
            name = require_string(block.get("name"), f"blocks[{pos}].name")
            marked = require_int(
                block.get("marked_size"), f"blocks[{pos}].marked_size", minimum=1
            )
            if marked > maximum_marked_size:
                raise ValueError(f"blocks[{pos}]: marked_size exceeds maximum")
            helpers = require_int(
                block.get("available_helpers"),
                f"blocks[{pos}].available_helpers",
                minimum=1,
            )
            if helpers < marked * marked:
                raise ValueError(
                    f"blocks[{pos}]: available_helpers is below marked_size^2"
                )
            role_loss = require_int(
                block.get("role_domain_loss"),
                f"blocks[{pos}].role_domain_loss",
            )
            punctures = require_int(
                block.get("controller_punctures"),
                f"blocks[{pos}].controller_punctures",
            )
            linear_cap = domain_loss_constant * marked
            if role_loss > linear_cap:
                raise ValueError(f"blocks[{pos}]: role-domain loss is not linear")
            if punctures > linear_cap:
                raise ValueError(f"blocks[{pos}]: controller punctures are not linear")
            support_rank = require_int(
                block.get("support_rank"), f"blocks[{pos}].support_rank", minimum=1
            )
            if support_rank > 3:
                raise ValueError(f"blocks[{pos}]: support rank exceeds three")
            outcome = require_string(block.get("outcome"), f"blocks[{pos}].outcome")
            if outcome not in REQUIRED_OUTCOMES:
                raise ValueError(f"blocks[{pos}]: unknown outcome {outcome!r}")

            total_marked += marked
            sum_squares += marked * marked
            observed_outcomes.add(outcome)
            normalized_blocks.append(
                {
                    "name": name,
                    "marked_size": marked,
                    "available_helpers": helpers,
                    "role_domain_loss": role_loss,
                    "controller_punctures": punctures,
                    "support_rank": support_rank,
                    "outcome": outcome,
                }
            )

        if sum_squares > total_marked * total_marked:
            raise ValueError("sum of block squares exceeds square of total marked size")

        payment = require_object(
            payload.get("all_independent_payment_example"),
            "all_independent_payment_example",
        )
        removal_credit = require_int(
            payment.get("first_removal_credit"),
            "all_independent_payment_example.first_removal_credit",
            minimum=1,
        )
        first_insertion = require_int(
            payment.get("first_insertion_multiplicity"),
            "all_independent_payment_example.first_insertion_multiplicity",
        )
        later_removal = require_int(
            payment.get("later_removal_multiplicity"),
            "all_independent_payment_example.later_removal_multiplicity",
        )
        later_insertion = require_int(
            payment.get("later_insertion_multiplicity"),
            "all_independent_payment_example.later_insertion_multiplicity",
        )
        if later_removal < first_insertion:
            raise ValueError("later removals do not cover first insertion multiplicity")
        if later_insertion != 0:
            raise ValueError("independent second host must have zero later insertion")

        composite_change_upper_bound = (
            first_insertion
            - removal_credit
            - later_removal
            + later_insertion
        )
        if composite_change_upper_bound > -removal_credit:
            raise ValueError("composite payment bound is weaker than -removal_credit")

    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    result = {
        "outcome": "second_host_call_matrix_verified",
        "potential": "Theta_E_plus",
        "block_count": len(normalized_blocks),
        "total_marked_size": total_marked,
        "sum_block_squares": sum_squares,
        "total_marked_square": total_marked * total_marked,
        "observed_outcomes": sorted(observed_outcomes),
        "required_outcomes": sorted(REQUIRED_OUTCOMES),
        "terminal_interfaces": sorted(REQUIRED_TERMINAL_INTERFACES),
        "composite_change_upper_bound": composite_change_upper_bound,
        "negative_original_credit": -removal_credit,
        "blocks": normalized_blocks,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
