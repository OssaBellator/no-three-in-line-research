#!/usr/bin/env python3
"""Canonical T32--T43 endpoint with globally installed exact T19--T21 roots.

Importing the canonical-root audit before the legacy final endpoint installs the exact T19, T20 and T21
proof/research dependencies and removes their obsolete special-certificate support for the entire nested
T01--T43 validation stack.  The certificate schema is unchanged; stale certificates carrying the former
target-definition or support digests must be regenerated.

This wrapper preserves the documentary honesty boundary and permanently reports
``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import check_prime_power_canonical_frontier_roots as canonical_roots
import check_prime_power_final_support_handoff_frontiers as legacy


FinalSupportHandoffFrontierV2Error = legacy.FinalSupportHandoffFrontierError


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    canonical_roots.exact_audit()
    return legacy.exact_certificate(certificate)


def validate_certificate(certificate: Any) -> dict[str, Any]:
    canonical_roots.exact_audit()
    summary = legacy.validate_certificate(certificate)
    if summary.get("all_n") != 0:
        raise FinalSupportHandoffFrontierV2Error(
            "canonical T32--T43 endpoint must preserve all_n_proved_by_checker = 0"
        )
    return summary


def build_certificate(
    t31_certificate: dict[str, Any],
    records: list[dict[str, Any]],
    semantics: list[dict[str, Any]],
) -> dict[str, Any]:
    canonical_roots.exact_audit()
    return legacy.build_certificate(t31_certificate, records, semantics)


def main() -> None:
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test-roots":
        print(canonical_roots.validate_audit(canonical_roots.exact_audit()))
        return
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_final_support_handoff_frontiers_v2.py "
            "certificate.json | --self-test-roots"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
