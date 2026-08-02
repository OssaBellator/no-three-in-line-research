#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1389."""
from __future__ import annotations
import copy
import hashlib
import json
from typing import Any

class Registry608Error(RuntimeError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok:
        raise Registry608Error(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()

BASE_REGISTRY_SHA256 = "890827174d7c40a37b23c8c5ccba673ddd3ab39a7e3ae7cef4f88df5c1b0387b"
BASE_OPERATION_KIND_COUNT = 552
BASE_CONTRACT_COUNT = 32
BASE_OWNER_CHANGING_KIND_COUNT = 159
NEW_CONTRACT_SHA256 = "bff27495eef9188b3d90e5f36ee66ed889b0606c7fa92f8b3391a3114e03d826"

def e(kind, sources, owner, payment, continuation):
    return {"operation_kind": kind, "source_theorems": sources, "owner_effect": owner, "payment_class": payment, "continuation": continuation, "contract_sha256": NEW_CONTRACT_SHA256}

NEW_ENTRIES = [
 e("canonical-structural-credit-owner",["CMR1318"],"same-owner","owner-witness-stock","record one persistent structural owner for every live physical credit"),
 e("one-coordinate-entering-edge-owner",["CMR1319"],"same-owner","owner-witness-stock","assign every newly created product credit to the active factor entering edge"),
 e("fixed-interface-owner-persistence",["CMR1320"],"same-owner","history-budget","preserve the previous owner through restriction conditioning and contraction"),
 e("structural-owner-forward-exit",["CMR1321"],"factor-child-owner-change","strict-child-descent","continue every strict child wall host or envelope exit forward in the owner DAG"),
 e("owner-block-upper-triangular-assembly",["CMR1322"],"same-owner","spectral-certificate","bind same-owner offspring to diagonal blocks and descendant offspring to upper blocks"),
 e("same-owner-spectral-block-reduction",["CMR1323"],"same-owner","spectral-certificate","reduce the global spectral radius to the maximum diagonal owner block"),
 e("rational-owner-block-certificate-gluing",["CMR1324","CMR1325"],"same-owner","spectral-certificate","glue finite rational diagonal certificates by backward owner scaling"),
 e("exact-state-credit-class-enumeration",["CMR1326"],"same-owner","finite-base-dispatch","dispatch the finite state-target class set of one structural owner"),
 e("exact-same-owner-offspring-row",["CMR1327"],"same-owner","spectral-certificate","bind each selected response law to its exact rational same-owner offspring row"),
 e("geometric-credit-class-projection",["CMR1328"],"same-owner","local-family-equivalence","project exact offspring rows onto arbitrary finite geometric credit fibres"),
 e("componentwise-credit-upper-quotient",["CMR1329"],"same-owner","spectral-certificate","certificate-lift componentwise worst-fibre rows to every exact credit class"),
 e("host-uniform-credit-upper-quotient",["CMR1330"],"same-owner","spectral-certificate","certificate-dominate every exact host row assigned to one coarse parent class"),
 e("weight-dependent-deterministic-row-selection",["CMR1331"],"same-owner","scheduler-dispatch","scheduler selects one strict deterministic bank law for each exact row"),
 e("integer-offspring-row-certificate",["CMR1332","CMR1333"],"same-owner","spectral-certificate","certificate-clear row and weight denominators into strict integer inequalities"),
 e("exact-line-profile-candidate-count",["CMR1334","CMR1335","CMR1336"],"same-owner","local-family-equivalence","replace line-local compatibility counts by exact nonaxis profile binomials"),
 e("line-profile-histogram-aggregation",["CMR1337"],"same-owner","finite-base-dispatch","bind exact collateral to the lossless integer line-profile histogram"),
 e("dyadic-rank-profile-classification",["CMR1338"],"same-owner","owner-witness-stock","record every collateral credit in one residual-rank dyadic profile class"),
 e("dyadic-profile-upper-coefficient",["CMR1339"],"same-owner","spectral-certificate","certificate-dominate each exact profile coefficient by its dyadic band maximum"),
 e("profile-band-concentration",["CMR1340","CMR1341"],"same-owner","owner-witness-stock","localize any large same-owner row to one explicit rank-profile band"),
 e("exact-line-pair-moment-stock",["CMR1342"],"same-owner","owner-witness-stock","record the exact opposite response-graph and old-layer pair moments"),
 e("profile-population-tail-bound",["CMR1343"],"same-owner","history-budget","bound high-population line tails by the exact pair moments"),
 e("dyadic-profile-multiplicity-envelope",["CMR1344"],"same-owner","spectral-certificate","certificate-bound every dyadic profile multiplicity by applicable pair moments"),
 e("rank-one-profile-envelope",["CMR1345"],"same-owner","spectral-certificate","certificate-bound one rank-one profile band by opposite-layer pair stock"),
 e("rank-two-profile-envelope",["CMR1346"],"same-owner","spectral-certificate","certificate-bound one rank-two profile band by response-graph pair stock"),
 e("rank-three-profile-envelope",["CMR1347"],"same-owner","spectral-certificate","certificate-bound one rank-three profile band by response-graph pair stock"),
 e("explicit-profile-upper-quotient",["CMR1348","CMR1349"],"same-owner","spectral-certificate","bind all rank-profile bands into one explicit rational upper quotient"),
 e("extension-free-doubly-stochastic-scaling",["CMR1350","CMR1351"],"same-owner","spectral-certificate","certificate-scale the target-omitting response graph with bounded entries"),
 e("extension-free-permanent-denominator",["CMR1352"],"same-owner","owner-witness-stock","record the extension-free perfect-matching denominator lower bound"),
 e("extension-free-prescription-probability",["CMR1353"],"same-owner","spectral-certificate","certificate-bound rank-one through rank-three prescription probabilities"),
 e("extension-free-collateral-response-criterion",["CMR1354"],"same-owner","scheduler-dispatch","scheduler accepts a strict extension-free target response when the collateral criterion holds"),
 e("extension-free-restricted-availability-penalty",["CMR1355"],"same-owner","spectral-certificate","certificate-charge unavailable host edges in the extension-free response row"),
 e("canonical-response-extension-realization",["CMR1356","CMR1357"],"same-owner","scheduler-dispatch","scheduler realizes every selected response by its first compatible forbidden extension"),
 e("exact-extension-free-bank-size",["CMR1358","CMR1359"],"same-owner","owner-witness-stock","record the exact derangement response-bank size and universal constant"),
 e("extension-free-rank-one-marginal",["CMR1360"],"same-owner","spectral-certificate","certificate-use the sharp one-over-n-minus-two edge marginal"),
 e("extension-free-higher-rank-marginal",["CMR1361"],"same-owner","spectral-certificate","certificate-use the exact derangement factor for rank-two and rank-three prescriptions"),
 e("sharpened-extension-free-offspring-row",["CMR1362"],"same-owner","spectral-certificate","bind corrected candidate counts to the sharpened expected offspring row"),
 e("sharpened-restricted-host-row",["CMR1363"],"same-owner","spectral-certificate","certificate-combine sharpened collateral and unavailable-edge penalties"),
 e("sharpened-line-profile-upper-quotient",["CMR1364","CMR1365"],"same-owner","spectral-certificate","bind exact derangement marginals into every line-profile quotient row"),
 e("extension-free-line-composition-kernel",["CMR1366","CMR1367","CMR1368","CMR1370"],"same-owner","local-family-equivalence","replace the sum over target-cell banks by exact line-composition kernels"),
 e("symmetric-target-incidence-row",["CMR1369"],"same-owner","owner-witness-stock","record exact destroyed target incidence over both selected layers"),
 e("symmetric-target-cell-kernel-selection",["CMR1371"],"same-owner","scheduler-dispatch","scheduler selects an improving target cell when the symmetric kernel is strict"),
 e("independent-line-kernel-obstruction-record",["CMR1372","CMR1373"],"same-owner","finite-base-dispatch","record the realizable side-five obstruction to independent line domination"),
 e("opposite-matching-counting-normalization",["CMR1374"],"same-owner","local-family-equivalence","normalize the opposite matching for counting while preserving physical geometry"),
 e("exact-cylinder-incidence-type",["CMR1375","CMR1377"],"same-owner","owner-witness-stock","record every residual prescription in one finite row-column incidence type"),
 e("exact-cylinder-extension-count",["CMR1376"],"same-owner","finite-base-dispatch","bind every cylinder type to its exact inclusion-exclusion extension count"),
 e("exact-created-credit-cylinder-row",["CMR1378"],"same-owner","spectral-certificate","bind created-credit histograms to exact rational extension-free expectations"),
 e("exact-destroyed-credit-cylinder-row",["CMR1379"],"same-owner","spectral-certificate","bind surviving old targets to exact destroyed-load expectations"),
 e("weighted-cylinder-upper-quotient",["CMR1380","CMR1381"],"same-owner","spectral-certificate","certificate-lift weighted cylinder histograms to strict integer quotient rows"),
 e("candidate-prescription-edge-selector",["CMR1382","CMR1383"],"same-owner","owner-witness-stock","assign each candidate credit to one residual response edge and its load"),
 e("selector-weighted-matching-row",["CMR1383"],"same-owner","spectral-certificate","certificate-dominate true collateral by one edge-weighted matching cost"),
 e("exact-selector-matching-optimization",["CMR1384"],"same-owner","local-family-equivalence","replace minimum collateral by joint selector and minimum-cost matching optimization"),
 e("fractional-response-profile",["CMR1385"],"same-owner","spectral-certificate","certificate-bound deterministic collateral through one fractional perfect matching"),
 e("selector-fractional-duality",["CMR1386"],"same-owner","local-family-equivalence","assign each candidate to a least-coordinate residual edge of the fractional profile"),
 e("deterministic-cross-line-response-selection",["CMR1387"],"same-owner","scheduler-dispatch","scheduler selects a deterministic strict response from a fractional cross-line certificate"),
 e("blocked-cross-line-unit-wall-descent",["CMR1388"],"factor-child-owner-change","strict-child-descent","continue a matching-free response host through its exact deficiency-one unit wall"),
 e("side-five-cross-line-zero-collateral-witness",["CMR1389"],"same-owner","finite-base-dispatch","record the exact side-five deterministic response and zero selector cost witness"),
]

CONTRACT = {"schema":"prime-power-installed-operation-registry-608/v1","base_registry_sha256":BASE_REGISTRY_SHA256,"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"base_contract_count":BASE_CONTRACT_COUNT,"base_owner_changing_kind_count":BASE_OWNER_CHANGING_KIND_COUNT,"new_contract_sha256":NEW_CONTRACT_SHA256,"new_entries":NEW_ENTRIES,"scope":"installed inherited-coordinate diagonal-block reductions and policies through CMR1389","honesty_flags":{"same_owner_diagonal_blocks_subcritical":0,"independent_line_kernel_sufficient":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST = "3271d30e50a8e2ff6147b316cb9a9e78b4bf9bfe4d82eb170058b0405902d194"
ALLOWED_OWNERS={"same-owner","factor-child-owner-change"}
ALLOWED_PAYMENTS={"owner-witness-stock","history-budget","spectral-certificate","finite-base-dispatch","local-family-equivalence","scheduler-dispatch","strict-child-descent"}

def validate(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries)==56,"fifty-six operations required")
    kinds=set(); owner_changes=BASE_OWNER_CHANGING_KIND_COUNT; payments={}
    for index,entry in enumerate(entries):
        path=f"entry[{index}]"; kind=entry.get("operation_kind")
        require(isinstance(kind,str) and kind and kind not in kinds,f"{path}: unique kind"); kinds.add(kind)
        require(entry.get("contract_sha256")==NEW_CONTRACT_SHA256,f"{path}: contract")
        sources=entry.get("source_theorems"); require(isinstance(sources,list) and sources and all(isinstance(source,str) and source.startswith("CMR") for source in sources),f"{path}: source ancestry")
        owner=entry.get("owner_effect"); payment=entry.get("payment_class"); continuation=entry.get("continuation")
        require(owner in ALLOWED_OWNERS,f"{path}: owner"); require(payment in ALLOWED_PAYMENTS,f"{path}: payment"); require(isinstance(continuation,str) and continuation,f"{path}: continuation")
        if payment=="scheduler-dispatch": require("scheduler" in continuation,f"{path}: scheduler continuation")
        if payment=="strict-child-descent": require(owner=="factor-child-owner-change" and "continue" in continuation,f"{path}: child descent")
        if payment=="spectral-certificate": require("certificate" in continuation or "bind" in continuation or "reduce" in continuation or "glue" in continuation,f"{path}: spectral certificate")
        if payment=="finite-base-dispatch": require("dispatch" in continuation or "bind" in continuation or "record" in continuation,f"{path}: finite base")
        owner_changes += owner!="same-owner"; payments[payment]=payments.get(payment,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==608,"608 kinds required"); require(owner_changes==161,"161 owner-changing kinds required")
    return {"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"new_operation_kind_count":len(kinds),"installed_operation_kind_count":608,"bound_contract_count":BASE_CONTRACT_COUNT+1,"owner_changing_operation_kinds":owner_changes,"same_owner_operation_kinds":608-owner_changes,"new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}

def mutation_audit() -> int:
    mutations=[lambda entries:entries.append(copy.deepcopy(entries[0])),lambda entries:entries[0].update(operation_kind=entries[1]["operation_kind"]),lambda entries:entries[0].update(contract_sha256="0"*64),lambda entries:entries[0].update(source_theorems=[]),lambda entries:entries[0].update(owner_effect="anonymous"),lambda entries:entries[0].update(payment_class="free"),lambda entries:entries[0].update(continuation=""),lambda entries:entries[12].update(continuation="select"),lambda entries:entries[3].update(owner_effect="same-owner"),lambda entries:entries[54].update(owner_effect="same-owner"),lambda entries:entries[4].update(payment_class="scheduler-dispatch"),lambda entries:entries[7].update(payment_class="strict-child-descent"),lambda entries:entries.pop(),lambda entries:entries.clear()]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(NEW_ENTRIES); mutate(bad)
        try: validate(bad)
        except Registry608Error: rejected+=1
    require(rejected==len(mutations),"registry corruption accepted"); return rejected

def main() -> None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest mismatch")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    print(json.dumps({"contract_digest":contract,"census":census,"installed_transition_kind_bank_608_exhaustive":1,"inherited_coordinate_diagonal_block_operations_registered":1,"installed_payment_assignment_608_complete":1,"same_owner_diagonal_blocks_subcritical":0,"independent_line_kernel_sufficient":0,"global_target_collateral_inequality_proved":0,"all_owner_operations_proved":0,"all_scheduler_operations_proved":0,"all_construction_ancestry_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))

if __name__=="__main__": main()
