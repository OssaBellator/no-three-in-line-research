#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1277."""
from __future__ import annotations
import copy
import hashlib
import json
from typing import Any


class Registry525Error(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise Registry525Error(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


BASE_REGISTRY_SHA256 = "754a91a7c1e978756b97d01576095763d8d7249f01d137acf8c5b7a174283ee1"
BASE_OPERATION_KIND_COUNT = 472
BASE_CONTRACT_COUNT = 30
BASE_OWNER_CHANGING_KIND_COUNT = 148
NEW_CONTRACT_SHA256 = "26e224413ed320276f50e0852b64291c11994861d21b35bb4bec9077179b7577"


def e(
    kind: str,
    sources: list[str],
    owner: str,
    payment: str,
    continuation: str,
) -> dict[str, Any]:
    return {
        "operation_kind": kind,
        "source_theorems": sources,
        "owner_effect": owner,
        "payment_class": payment,
        "continuation": continuation,
        "contract_sha256": NEW_CONTRACT_SHA256,
    }


NEW_ENTRIES = [
    e("disjoint-forbidden-extension-selection", ["CMR1198"], "same-owner", "scheduler-dispatch", "scheduler selects a forbidden perfect matching containing the target and disjoint from the opposite layer"),
    e("degree-two-response-bank-formation", ["CMR1199"], "same-owner", "local-family-equivalence", "replace the target response family by perfect matchings of the regular degree-two-forbidden graph"),
    e("degree-two-bank-permanent-lower-bound", ["CMR1199"], "same-owner", "probabilistic-bank-bound", "bind the response-bank size to the van der Waerden permanent lower bound"),
    e("rank-r-response-cylinder-probability", ["CMR1200"], "same-owner", "probabilistic-bank-bound", "bound each compatible rank-one through rank-three response prescription by an exact residual cylinder ratio"),
    e("physical-collateral-rank-classification", ["CMR1201"], "same-owner", "owner-witness-stock", "classify every possible new triple by its exact residual response prescription rank"),
    e("degree-two-bank-collateral-expectation", ["CMR1202"], "same-owner", "probabilistic-bank-bound", "upper-bound expected created collateral by the normalized three-rank score"),
    e("fixed-target-destroyed-load-certificate", ["CMR1203"], "same-owner", "target-collateral-credit", "charge every response with the full old target load through the removed physical cell"),
    e("fixed-target-average-strict-improvement", ["CMR1204"], "same-owner", "scheduler-dispatch", "scheduler selects a negative-average response when collateral is below destroyed load"),
    e("positive-minimum-collateral-barrier", ["CMR1205"], "same-owner", "target-collateral-credit", "record the reverse target-versus-collateral inequality at a positive minimum"),
    e("unavailable-bank-edge-expectation", ["CMR1206"], "same-owner", "probabilistic-bank-bound", "bound expected unavailable response-edge use by rank-one cylinder marginals"),
    e("weighted-feasibility-forcing", ["CMR1207"], "same-owner", "scheduler-dispatch", "scheduler converts a negative weighted response into a feasible strict improvement"),
    e("restricted-host-bank-improvement", ["CMR1208", "CMR1209"], "host-owner-change", "local-family-restriction", "restrict the ambient response bank to the current host under the availability-collateral criterion"),
    e("target-cell-incidence-aggregation", ["CMR1210", "CMR1211"], "same-owner", "target-collateral-credit", "sum selected-cell target loads exactly as three times the current potential"),
    e("optimized-forbidden-extension-selection", ["CMR1212", "CMR1213"], "same-owner", "scheduler-dispatch", "scheduler minimizes availability-penalized collateral over forbidden extensions"),
    e("new-triple-entering-edge-support", ["CMR1214"], "same-owner", "owner-witness-stock", "attach every created physical triple to at least one genuinely entering labelled edge"),
    e("absolute-last-entering-owner-partition", ["CMR1215", "CMR1216"], "same-owner", "target-collateral-credit", "partition created collateral by the least absolute entering-edge owner"),
    e("fixed-core-collateral-owner-transfer", ["CMR1217"], "factor-child-owner-change", "factor-product-dispatch", "transfer anchored collateral ownership to the unique residual entering-edge factor"),
    e("product-collateral-owner-uniqueness", ["CMR1218"], "same-owner", "factor-product-dispatch", "assign each entering collateral owner to one unique exact product factor"),
    e("historical-owner-contraction-invariance", ["CMR1219"], "same-owner", "history-budget", "preserve the absolute creation owner through later contraction and lifting"),
    e("bank-edge-owner-score-decomposition", ["CMR1220", "CMR1221"], "same-owner", "target-collateral-credit", "split every normalized bank collateral score into absolute edge-owner summands"),
    e("corrected-rank-one-line-energy", ["CMR1222"], "same-owner", "line-energy-bound", "count genuinely new rank-one collateral by opposite-line pairs and nonold response edges"),
    e("corrected-rank-two-line-energy", ["CMR1223"], "same-owner", "line-energy-bound", "subtract old compatible response pairs from the rank-two line energy"),
    e("corrected-rank-three-line-energy", ["CMR1224"], "same-owner", "line-energy-bound", "subtract old response triples from the rank-three line energy"),
    e("degree-two-compatible-pair-stock", ["CMR1225"], "same-owner", "owner-witness-stock", "bind the complete and genuinely new compatible-pair stocks exactly"),
    e("corrected-line-cap-upper-bound", ["CMR1226", "CMR1227"], "same-owner", "line-energy-bound", "route a line-cap collateral bound into the restricted-host strict-improvement criterion"),
    e("edge-local-line-owner-score", ["CMR1228", "CMR1229"], "same-owner", "target-collateral-credit", "localize every corrected rank score to one absolute response edge and one real line"),
    e("rank-one-response-matching-cost", ["CMR1230"], "same-owner", "line-energy-bound", "represent corrected rank-one collateral as an edge-weighted response matching cost"),
    e("response-bank-doubly-stochastic-marginal", ["CMR1231"], "same-owner", "probabilistic-bank-bound", "average bank matchings to a doubly stochastic supported edge-marginal matrix"),
    e("rank-one-assignment-envelope", ["CMR1232", "CMR1233"], "same-owner", "line-energy-bound", "bound rank-one expectation by maximum matching and row-column assignment envelopes"),
    e("rank-one-refined-restricted-improvement", ["CMR1234"], "host-owner-change", "local-family-restriction", "restrict the current host using the refined rank-one and higher-rank bank criterion"),
    e("heavy-new-edge-secant-load", ["CMR1235", "CMR1236", "CMR1237"], "same-owner", "scheduler-dispatch", "scheduler routes a large rank-one assignment barrier to a loaded line or rooted secant star"),
    e("allowed-edge-bank-extension", ["CMR1238"], "same-owner", "local-family-equivalence", "extend every allowed response edge to at least one regular-bank perfect matching"),
    e("rank-two-three-local-incidence", ["CMR1239"], "same-owner", "line-energy-bound", "express genuinely new rank-two and rank-three collateral through exact local edge incidences"),
    e("full-local-collateral-envelope", ["CMR1240", "CMR1241"], "same-owner", "line-energy-bound", "dominate every response pointwise by summed local edge envelopes and row-column maxima"),
    e("pointwise-bank-improvement-or-blockage", ["CMR1242"], "same-owner", "scheduler-dispatch", "scheduler accepts any feasible pointwise-improving response or dispatches complete blockage"),
    e("blocked-envelope-unit-wall-descent", ["CMR1242", "CMR1246"], "factor-child-owner-change", "strict-child-descent", "continue a completely blocked envelope bank through the deficiency-one unit wall"),
    e("rank-two-envelope-assignment", ["CMR1243"], "same-owner", "line-energy-bound", "compute the rank-two local envelope as a residual maximum-weight matching"),
    e("large-local-envelope-line-star-dispatch", ["CMR1244", "CMR1245"], "same-owner", "scheduler-dispatch", "scheduler routes large rank-two or rank-three envelopes to loaded lines or rooted response stars"),
    e("host-feasible-extension-decision", ["CMR1246"], "same-owner", "scheduler-dispatch", "scheduler selects a host-feasible extension or enters blocked wall descent"),
    e("best-feasible-target-envelope", ["CMR1247", "CMR1248"], "same-owner", "target-collateral-credit", "minimize the full collateral envelope over host-feasible target extensions"),
    e("optimized-envelope-target-concentration", ["CMR1249", "CMR1250", "CMR1251"], "same-owner", "scheduler-dispatch", "scheduler concentrates the global target barrier on one edge and one collateral rank"),
    e("extension-law-envelope-averaging", ["CMR1252", "CMR1253"], "same-owner", "probabilistic-bank-bound", "average host-feasible extension envelopes and select one strict-improvement bank when the global sum is low"),
    e("last-creation-time-selection", ["CMR1254"], "same-owner", "history-budget", "select the unique last physical zero-to-one creation time of every live triple"),
    e("physical-credit-owner-assignment", ["CMR1255", "CMR1256"], "same-owner", "target-collateral-credit", "assign each nonroot live triple one physical owner cell and partition the current potential"),
    e("live-credit-transition-update", ["CMR1257"], "same-owner", "target-collateral-credit", "retire lost credits preserve survivors and issue exactly one credit per new triple"),
    e("owner-cell-credit-retirement", ["CMR1258", "CMR1259"], "same-owner", "scheduler-dispatch", "scheduler targets an owner cell to retire every live credit assigned to it"),
    e("physical-credit-layer-invariance", ["CMR1260", "CMR1261"], "same-owner", "history-budget", "preserve live credits through layer reassignment and structural refactorization"),
    e("collateral-offspring-matrix-construction", ["CMR1262"], "same-owner", "spectral-certificate", "form the finite nonnegative expected offspring matrix for chosen response laws"),
    e("lyapunov-weighted-credit-descent", ["CMR1263", "CMR1264"], "same-owner", "spectral-certificate", "use a positive subinvariant weight or spectral radius below one to force expected credit descent"),
    e("upper-offspring-matrix-domination", ["CMR1265", "CMR1266", "CMR1267"], "same-owner", "spectral-certificate", "dominate exact offspring by a finite upper policy matrix and select subcritical rows"),
    e("block-triangular-offspring-assembly", ["CMR1268", "CMR1269"], "factor-child-owner-change", "factor-product-dispatch", "assemble strict-child and wall offspring blocks under a genuine upper-triangular owner order"),
    e("exact-rational-spectral-certificate", ["CMR1270", "CMR1271", "CMR1272"], "same-owner", "spectral-certificate", "certify subcriticality with rational or integer Lyapunov inequalities and perturbation slack"),
    e("constructive-block-certificate-gluing", ["CMR1273", "CMR1274", "CMR1275", "CMR1276", "CMR1277"], "factor-child-owner-change", "spectral-certificate", "glue triangular blocks select deterministic rows and lift coarse exact integer certificates"),
]

CONTRACT = {
    "schema": "prime-power-installed-operation-registry-525/v1",
    "base_registry_sha256": BASE_REGISTRY_SHA256,
    "base_operation_kind_count": BASE_OPERATION_KIND_COUNT,
    "base_contract_count": BASE_CONTRACT_COUNT,
    "base_owner_changing_kind_count": BASE_OWNER_CHANGING_KIND_COUNT,
    "new_contract_sha256": NEW_CONTRACT_SHA256,
    "new_entries": NEW_ENTRIES,
    "open_target": "global target-versus-collateral subcriticality",
    "honesty_flags": {
        "global_target_collateral_inequality_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_DIGEST = "f37bbd867d6f72b2b30630eb27a15b6001156f65b30f6c1e5457350ce7458775"

ALLOWED_OWNERS = {
    "same-owner",
    "host-owner-change",
    "factor-child-owner-change",
}
ALLOWED_PAYMENTS = {
    "scheduler-dispatch",
    "local-family-equivalence",
    "local-family-restriction",
    "probabilistic-bank-bound",
    "owner-witness-stock",
    "target-collateral-credit",
    "factor-product-dispatch",
    "history-budget",
    "line-energy-bound",
    "strict-child-descent",
    "spectral-certificate",
}


def validate(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries) == 53, "fifty-three operations required")
    kinds: set[str] = set()
    owner_changes = BASE_OWNER_CHANGING_KIND_COUNT
    payments: dict[str, int] = {}
    for index, entry in enumerate(entries):
        path = f"entry[{index}]"
        kind = entry.get("operation_kind")
        require(
            isinstance(kind, str) and kind and kind not in kinds,
            f"{path}: unique kind",
        )
        kinds.add(kind)
        require(
            entry.get("contract_sha256") == NEW_CONTRACT_SHA256,
            f"{path}: contract",
        )
        sources = entry.get("source_theorems")
        require(
            isinstance(sources, list)
            and sources
            and all(
                isinstance(source, str) and source.startswith("CMR")
                for source in sources
            ),
            f"{path}: source ancestry",
        )
        owner = entry.get("owner_effect")
        payment = entry.get("payment_class")
        continuation = entry.get("continuation")
        require(owner in ALLOWED_OWNERS, f"{path}: owner effect")
        require(payment in ALLOWED_PAYMENTS, f"{path}: payment class")
        require(
            isinstance(continuation, str) and continuation,
            f"{path}: continuation",
        )
        if payment == "scheduler-dispatch":
            require(
                "scheduler" in continuation,
                f"{path}: scheduler continuation",
            )
        if payment == "local-family-restriction":
            require(
                owner == "host-owner-change"
                and "restrict" in continuation,
                f"{path}: host restriction",
            )
        if payment == "strict-child-descent":
            require(
                owner == "factor-child-owner-change"
                and "continue" in continuation,
                f"{path}: child descent",
            )
        if owner == "factor-child-owner-change":
            require(
                payment
                in {
                    "factor-product-dispatch",
                    "strict-child-descent",
                    "spectral-certificate",
                },
                f"{path}: factor payment",
            )
        owner_changes += owner != "same-owner"
        payments[payment] = payments.get(payment, 0) + 1
    require(
        BASE_OPERATION_KIND_COUNT + len(kinds) == 525,
        "525 kinds required",
    )
    require(
        owner_changes == 154,
        "154 owner-changing kinds required",
    )
    return {
        "base_operation_kind_count": BASE_OPERATION_KIND_COUNT,
        "new_operation_kind_count": len(kinds),
        "installed_operation_kind_count": 525,
        "bound_contract_count": BASE_CONTRACT_COUNT + 1,
        "owner_changing_operation_kinds": owner_changes,
        "same_owner_operation_kinds": 525 - owner_changes,
        "new_payment_counts": payments,
        "registry_sha256": digest(
            {"base": BASE_REGISTRY_SHA256, "new": entries}
        ),
    }


def mutation_audit() -> int:
    mutations = [
        lambda entries: entries.append(copy.deepcopy(entries[0])),
        lambda entries: entries[0].update(
            operation_kind=entries[1]["operation_kind"]
        ),
        lambda entries: entries[0].update(
            contract_sha256="0" * 64
        ),
        lambda entries: entries[0].update(source_theorems=[]),
        lambda entries: entries[0].update(owner_effect="anonymous"),
        lambda entries: entries[0].update(payment_class="free"),
        lambda entries: entries[0].update(continuation=""),
        lambda entries: entries[0].update(continuation="select"),
        lambda entries: entries[11].update(owner_effect="same-owner"),
        lambda entries: entries[35].update(owner_effect="same-owner"),
        lambda entries: entries[50].update(owner_effect="same-owner"),
        lambda entries: entries.pop(),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(NEW_ENTRIES)
        mutate(bad)
        try:
            validate(bad)
        except Registry525Error:
            rejected += 1
    require(
        rejected == len(mutations),
        "registry corruption accepted",
    )
    return rejected


def main() -> None:
    contract = digest(CONTRACT)
    require(
        contract == EXPECTED_CONTRACT_DIGEST,
        "contract digest mismatch",
    )
    census = validate(copy.deepcopy(NEW_ENTRIES))
    census["rejected_corruptions"] = mutation_audit()
    report = {
        "contract_digest": contract,
        "census": census,
        "installed_transition_kind_bank_525_exhaustive": 1,
        "collateral_spectral_operations_registered": 1,
        "installed_payment_assignment_525_complete": 1,
        "global_target_collateral_inequality_proved": 0,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_restoration_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
