#!/usr/bin/env python3
"""Track one exact proof disposition for every exceptional selector chamber.

The canonical CMR2110 worklist contains 232 zero-selector chambers and 20 hard-core chambers.
This checker requires one open/closed disposition for every chamber and optionally binds a
closed chamber directly to a theorem record in the final quotient semantic refinement.

Passing proves exact worklist coverage and documentary linkage only. It does not prove any
chamber feasible, infeasible, recurrently contracting, or mathematically closed.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_exceptional_selector_chamber_worklist as worklist
import check_prime_power_global_quotient_semantic_refinement as refinement


class ExceptionalChamberDispositionError(ValueError):
    """Raised when exceptional chamber dispositions are incomplete or inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ExceptionalChamberDispositionError(message)


CLOSED_PROOF_KINDS = {
    "global-row-theorem",
    "direct-chamber-proof",
    "signature-infeasibility",
    "host-union-proof",
}


def canonical_chambers() -> list[dict[str, Any]]:
    source = worklist.build_worklist()
    worklist.validate_worklist(source)
    records = []
    for host in source["hosts"]:
        kind = "zero-selector" if host["worklist_kind"] == "zero-rank3-selector-union" else "hard-core"
        for selector in host["selector_chambers"]:
            core = {
                "host_id": host["host_id"],
                "chamber_kind": kind,
                "selected_index": selector["selected_index"],
                "selected_row_sha256": selector["selected_row_sha256"],
                "selected_permutation": selector["selected_permutation"],
                "selected_rank3_triples": selector["selected_rank3_triples"],
                "rank3_minimum": selector["rank3_minimum"],
                "selector_chamber_sha256": selector["selector_chamber_sha256"],
                "host_worklist_sha256": host["host_worklist_sha256"],
            }
            chamber_id = f"exceptional-chamber-{catalogue.canonical_digest(core)[:24]}"
            record = {"chamber_id": chamber_id, **core}
            record["canonical_chamber_record_sha256"] = catalogue.canonical_digest(record)
            records.append(record)
    records.sort(key=lambda item: (item["chamber_kind"], item["host_id"], item["selected_index"]))
    return records


def exact_disposition(
    record: dict[str, Any],
    path: str,
    expected: dict[str, dict[str, Any]],
    semantic_rows: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    chamber_id = record.get("chamber_id")
    status = record.get("status")
    proof_kind = record.get("proof_kind")
    row_id = record.get("row_id")
    theorem_id = record.get("theorem_id")
    locator = record.get("artifact_locator")
    digest = record.get("artifact_digest")
    note = record.get("note")
    require(isinstance(chamber_id, str) and chamber_id in expected, f"{path}.chamber_id: unknown")
    require(status in {"open", "closed"}, f"{path}.status: bad status")
    require(isinstance(note, str) and note, f"{path}.note: required")

    if status == "open":
        require(
            proof_kind is None and row_id is None and theorem_id is None
            and locator is None and digest is None,
            f"{path}: open disposition requires null proof fields",
        )
    else:
        require(proof_kind in CLOSED_PROOF_KINDS, f"{path}.proof_kind: bad closed proof kind")
        require(isinstance(locator, str) and locator, f"{path}.artifact_locator: required")
        require(isinstance(digest, str) and digest, f"{path}.artifact_digest: required")
        if proof_kind == "global-row-theorem":
            require(isinstance(row_id, str) and row_id in semantic_rows, f"{path}.row_id: unknown")
            semantic = semantic_rows[row_id]
            require(theorem_id == semantic["theorem_id"], f"{path}.theorem_id: mismatch")
            require(locator == semantic["theorem_locator"], f"{path}.artifact_locator: theorem locator mismatch")
            require(digest == semantic["theorem_digest"], f"{path}.artifact_digest: theorem digest mismatch")
        else:
            require(row_id is None and theorem_id is None, f"{path}: non-row proof requires null row fields")

    output = {
        **expected[chamber_id],
        "status": status,
        "proof_kind": proof_kind,
        "row_id": row_id,
        "theorem_id": theorem_id,
        "artifact_locator": locator,
        "artifact_digest": digest,
        "note": note,
    }
    output["chamber_disposition_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    refinement_certificate = certificate.get("global_quotient_semantic_refinement_certificate")
    raw_dispositions = certificate.get("chamber_dispositions")
    require(
        isinstance(refinement_certificate, dict),
        "global_quotient_semantic_refinement_certificate: expected object",
    )
    require(isinstance(raw_dispositions, list), "chamber_dispositions: expected list")
    refinement.validate_certificate(refinement_certificate)
    refinement_exact = refinement.exact_certificate(refinement_certificate)
    semantic_rows = {
        record["row_id"]: record for record in refinement_exact["row_semantic_records"]
    }

    chambers = canonical_chambers()
    expected = {record["chamber_id"]: record for record in chambers}
    dispositions = [
        exact_disposition(
            record,
            f"chamber_dispositions[{index}]",
            expected,
            semantic_rows,
        )
        for index, record in enumerate(raw_dispositions)
    ]
    require(raw_dispositions == dispositions, "chamber_dispositions: canonical enriched records required")
    require(
        [record["chamber_id"] for record in dispositions]
        == [record["chamber_id"] for record in chambers],
        "chamber_dispositions: must cover the canonical worklist in exact order",
    )

    proof_kind_counts: Counter[str] = Counter(
        record["proof_kind"] for record in dispositions if record["proof_kind"] is not None
    )
    zero_records = [record for record in dispositions if record["chamber_kind"] == "zero-selector"]
    hard_records = [record for record in dispositions if record["chamber_kind"] == "hard-core"]
    closed_zero = sum(record["status"] == "closed" for record in zero_records)
    closed_hard = sum(record["status"] == "closed" for record in hard_records)
    zero_ready = int(closed_zero == len(zero_records))
    hard_ready = int(closed_hard == len(hard_records))
    claims = {
        "exceptional_hosts": 89,
        "exceptional_chambers": len(dispositions),
        "zero_selector_chambers": len(zero_records),
        "hard_core_selector_chambers": len(hard_records),
        "closed_zero_selector_chambers": closed_zero,
        "open_zero_selector_chambers": len(zero_records) - closed_zero,
        "closed_hard_core_chambers": closed_hard,
        "open_hard_core_chambers": len(hard_records) - closed_hard,
        "exceptional_zero_rows_ready": zero_ready,
        "hard_core_rows_ready": hard_ready,
        "complete_exceptional_chamber_disposition": int(zero_ready and hard_ready),
        "proof_kind_distribution": [[kind, proof_kind_counts[kind]] for kind in sorted(proof_kind_counts)],
        "worklist_sha256": worklist.build_worklist()["worklist_sha256"],
        "semantic_refinement_sha256": refinement_certificate["certificate_sha256"],
        "canonical_chambers_sha256": catalogue.canonical_digest(chambers),
        "zero_dispositions_sha256": catalogue.canonical_digest(zero_records),
        "hard_core_dispositions_sha256": catalogue.canonical_digest(hard_records),
        "chamber_dispositions_sha256": catalogue.canonical_digest(dispositions),
    }
    require(
        (claims["zero_selector_chambers"], claims["hard_core_selector_chambers"])
        == (232, 20),
        "canonical exceptional chamber census drift",
    )
    return {
        "canonical_chamber_records": chambers,
        "chamber_dispositions": dispositions,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("canonical_chamber_records", "chamber_dispositions", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(
        certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
        "certificate_sha256: incorrect",
    )
    claims = exact["claims"]
    return {
        "chambers": claims["exceptional_chambers"],
        "open_zero": claims["open_zero_selector_chambers"],
        "open_hard": claims["open_hard_core_chambers"],
        "complete": claims["complete_exceptional_chamber_disposition"],
    }


def build_certificate(
    refinement_certificate: dict[str, Any],
    dispositions: list[dict[str, Any]],
) -> dict[str, Any]:
    semantic_rows = {
        record["row_id"]: record
        for record in refinement.exact_certificate(refinement_certificate)["row_semantic_records"]
    }
    chambers = canonical_chambers()
    expected = {record["chamber_id"]: record for record in chambers}
    canonical = [
        exact_disposition(record, "chamber_disposition", expected, semantic_rows)
        for record in dispositions
    ]
    canonical.sort(key=lambda item: (item["chamber_kind"], item["host_id"], item["selected_index"]))
    certificate: dict[str, Any] = {
        "version": 1,
        "global_quotient_semantic_refinement_certificate": refinement_certificate,
        "chamber_dispositions": canonical,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_exceptional_chamber_disposition_registry.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
