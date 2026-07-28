#!/usr/bin/env python3
"""Execute the T05 geometry/selector frontier with corrected closure-record lookup.

The original T05 checker correctly constructs the finite geometry and selector banks but reads the
``closed`` flag from raw obligation records.  The closure checker publishes that flag in the separate
``obligation_closure_records`` bank.  This compatibility layer supplies the exact merged view only to
the T05 module, leaving the underlying closure and obligation validators unchanged.

This module is the canonical executable endpoint for T05.  It changes no certificate fields or proof
claims and permanently preserves ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import copy
import json
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_geometry_selector_frontier as legacy


class GeometrySelectorFrontierV2Error(ValueError):
    """Raised when the corrected T05 execution layer is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GeometrySelectorFrontierV2Error(message)


class _ClosureView:
    @staticmethod
    def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
        exact = closure.exact_certificate(certificate)
        closure_by_id = {
            record["obligation_id"]: record
            for record in exact["obligation_closure_records"]
        }
        merged = []
        for obligation in exact["proof_obligations"]:
            obligation_id = obligation["obligation_id"]
            require(
                obligation_id in closure_by_id,
                f"closure view: missing closure record for {obligation_id}",
            )
            record = copy.deepcopy(obligation)
            record["closed"] = closure_by_id[obligation_id]["closed"]
            merged.append(record)
        output = copy.deepcopy(exact)
        output["proof_obligations"] = merged
        return output


@contextmanager
def corrected_closure_view() -> Iterator[None]:
    original = legacy.closure
    legacy.closure = _ClosureView
    try:
        yield
    finally:
        legacy.closure = original


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    with corrected_closure_view():
        return legacy.exact_certificate(certificate)


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    with corrected_closure_view():
        summary = legacy.validate_certificate(certificate)
    require(
        summary.get("all_n") == 0,
        "corrected T05 execution must preserve all_n_proved_by_checker = 0",
    )
    return summary


def build_certificate(
    t04_certificate: dict[str, Any],
    records: list[dict[str, Any]],
    geometry_certificates: list[dict[str, Any]],
    artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    with corrected_closure_view():
        return legacy.build_certificate(
            t04_certificate,
            records,
            geometry_certificates,
            artifacts,
        )


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_geometry_selector_frontier_v2.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
