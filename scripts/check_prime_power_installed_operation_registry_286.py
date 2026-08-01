#!/usr/bin/env python3
"""Extend the installed operation registry through CMR925."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any

class Registry286Error(RuntimeError): pass
def require(ok: bool, message: str) -> None:
    if not ok: raise Registry286Error(message)
def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

BASE_REGISTRY_SHA256 = "bed729b09d8a1706da4fc2a5848fb2cca4b1092caeba348fed4f92108f61d145"
BASE_OPERATION_KIND_COUNT = 239
BASE_CONTRACT_COUNT = 25
BASE_OWNER_CHANGING_KIND_COUNT = 77
NEW_CONTRACT_SHA256 = "3ec89baac0450290c3dbe3a340af76aaea95bf7f4c84342a9aac8f7c31862498"

def e(kind: str, sources: list[str], owner: str, payment: str, continuation: str) -> dict[str, Any]:
    return {"operation_kind": kind, "source_theorems": sources, "owner_effect": owner,
            "payment_class": payment, "continuation": continuation,
            "contract_sha256": NEW_CONTRACT_SHA256}

NEW_ENTRIES = [
 e("matching-inactive-cross-scc-pruning", ["CMR854","CMR855"], "host-owner-change", "local-family-equivalence", "delete matching-inactive cross-SCC edges without changing the matching family"),
 e("exchange-scc-product-factorization", ["CMR856"], "factor-child-owner-change", "factor-product-dispatch", "exact independent matching factors on SCC child blocks"),
 e("exchange-scc-width-additivity", ["CMR857"], "same-owner", "owner-witness-stock", "local feedback widths add over exact SCC factors"),
 e("exchange-scc-width-concentration-dispatch", ["CMR858"], "same-owner", "scheduler-dispatch", "scheduler recurses into one high-width SCC or many flexible factors"),
 e("exchange-scc-minimum-branch-cover", ["CMR859"], "same-owner", "branch-cover-dispatch", "componentwise minimum edge sets assemble an exact global branch cover"),
 e("exchange-scc-low-rank-richness-dispatch", ["CMR860"], "same-owner", "scheduler-dispatch", "scheduler converts high local width to low-rank exchange richness"),
 e("exchange-scc-recursive-child-handoff", ["CMR861"], "factor-child-owner-change", "strict-child-descent", "continue in one strict SCC factor or independent flexible product"),
 e("prescription-single-edge-deletion-child", ["CMR862","CMR863"], "host-owner-change", "local-family-restriction", "one prescription edge defines an exact viable deletion child"),
 e("prescription-conditioned-family-child", ["CMR862","CMR863"], "host-owner-change", "local-family-restriction", "conditioned child contains exactly states retaining the full prescription"),
 e("conditioned-prescription-contraction", ["CMR864","CMR865"], "factor-child-owner-change", "strict-factor-contraction", "fixed prescription contracts and preserves residual distinguishing rank"),
 e("new-triple-constant-arity-branch-cover", ["CMR866","CMR867"], "same-owner", "branch-cover-dispatch", "three deletion children plus one conditioned child cover the family"),
 e("forced-triple-conditioned-dispatch", ["CMR868","CMR869"], "same-owner", "scheduler-dispatch", "scheduler handles the fixed labelled triple by handoff contraction or escape"),
 e("new-triple-support-signature-extraction", ["CMR870","CMR871"], "same-owner", "owner-witness-stock", "canonical nine-atom support and exact signature multiplicity stock"),
 e("support-disjoint-bank-extraction", ["CMR872"], "same-owner", "support-packing", "extract pairwise disjoint supports or a bounded support cover"),
 e("support-cover-concentration", ["CMR873"], "same-owner", "owner-witness-stock", "one physical cell or labelled matching vertex carries many signatures"),
 e("matching-vertex-wall-star-refinement", ["CMR874"], "same-owner", "scheduler-dispatch", "scheduler refines a matching-vertex fan to a wall or repeated-cell star"),
 e("support-disjoint-deletion-payment", ["CMR875","CMR876"], "host-owner-change", "host-edge-deletion", "disjoint support signatures consume distinct deleted edges"),
 e("support-disjoint-forced-certificate-packing", ["CMR875","CMR876","CMR877"], "same-owner", "scheduler-dispatch", "scheduler processes compatible disjoint forced-triple certificates"),
 e("constant-arity-deletion-budget", ["CMR878","CMR879"], "same-owner", "history-budget", "distinct deletion resolutions consume the finite nonanchor edge stock"),
 e("rank-three-contraction-budget", ["CMR878","CMR879"], "same-owner", "history-budget", "rank-three conditioned contractions consume finite state cardinality"),
 e("path-support-cover-extraction", ["CMR880","CMR881"], "same-owner", "owner-witness-stock", "a maximal support matching yields a polynomial path support cover"),
 e("path-support-concentration-dispatch", ["CMR882","CMR884"], "same-owner", "scheduler-dispatch", "scheduler sends a concentrated atom to cell wall or star machinery"),
 e("constant-arity-episode-bound", ["CMR883","CMR885"], "same-owner", "history-budget", "finite episode bound unless a triple or support atom recurs"),
 e("support-cell-layer-label-stabilization", ["CMR886","CMR888"], "same-owner", "owner-witness-stock", "physical-cell concentration stabilises one labelled layer edge"),
 e("support-vertex-edge-stabilization", ["CMR887","CMR888"], "same-owner", "owner-witness-stock", "matching-vertex concentration stabilises one incident labelled edge"),
 e("concentrated-edge-binary-deletion-child", ["CMR889"], "host-owner-change", "local-family-restriction", "edge-omitting child simultaneously removes all batched signatures using the edge"),
 e("concentrated-edge-conditioned-child", ["CMR889"], "host-owner-change", "local-family-restriction", "edge-conditioned child retains exactly states using the concentrated edge"),
 e("concentrated-edge-contraction", ["CMR890","CMR891"], "factor-child-owner-change", "strict-factor-contraction", "conditioned edge contracts and transfers every triple to rank two"),
 e("residual-pair-multiplicity-dispatch", ["CMR892","CMR893"], "same-owner", "scheduler-dispatch", "scheduler handles recurrent residual pair or a large compatible pair bank"),
 e("ordered-prescription-first-missing-child", ["CMR894"], "host-owner-change", "local-family-restriction", "first missing prescription edge gives one disjoint child"),
 e("ordered-prescription-fixed-prefix-contraction", ["CMR895"], "factor-child-owner-change", "strict-factor-contraction", "the common ordered prefix contracts exactly in its child"),
 e("target-resolution-tree-progress", ["CMR896","CMR897"], "same-owner", "history-budget", "each tree step fixes or deletes one previously undecided edge"),
 e("terminal-physical-target-class-compression", ["CMR898","CMR899"], "same-owner", "branch-cover-dispatch", "disjoint terminal leaves merge into polynomial physical-target classes"),
 e("terminal-labelled-triple-class-contraction", ["CMR900","CMR901"], "factor-child-owner-change", "strict-factor-contraction", "layer assignment fixes and contracts one labelled target triple"),
 e("minimum-anchor-nonanchor-edge-deletion", ["CMR902","CMR903","CMR904"], "host-owner-change", "local-family-restriction", "delete a new-triple edge outside the known minimum anchor"),
 e("minimum-anchor-target-prescription-forcing", ["CMR904","CMR905"], "same-owner", "history-budget", "finite nonanchor deletion pool forces the target and chosen anchor prescription"),
 e("minimum-anchor-induced-objective-contraction", ["CMR906","CMR907"], "factor-child-owner-change", "strict-factor-contraction", "common anchor prescription contracts while preserving induced minimality"),
 e("minimum-anchor-restored-edge-bulk-redeletion", ["CMR908","CMR909"], "host-owner-change", "edge-reintroduction", "genuinely restored nonanchor edges are bulk redeleted against the stored minimum"),
 e("minimum-face-avoiding-edge-deletion", ["CMR910","CMR911"], "host-owner-change", "local-family-restriction", "a minimum-face witness omitting the edge authorises minimum-preserving deletion"),
 e("minimum-face-complete-core-contraction", ["CMR912","CMR913"], "factor-child-owner-change", "strict-factor-contraction", "the full minimum core contracts to a core-free residual minimum family"),
 e("minimum-face-core-growth-budget", ["CMR916"], "same-owner", "history-budget", "strict minimum-core growth has finite total rank"),
 e("minimum-face-restoration-response", ["CMR914","CMR915","CMR917"], "restoration-owner-change", "edge-reintroduction", "restored edge redeletes against the minimum face or enters the minimum core"),
 e("edge-owner-first-closure", ["CMR918"], "same-owner", "owner-witness-stock", "one uncharged first closure is allowed at each structural owner slot"),
 e("edge-lineage-restoration-budget", ["CMR919","CMR920"], "same-owner", "history-budget", "active appearances beyond owner slots require genuine restorations"),
 e("edge-lineage-token-payment", ["CMR921","CMR922"], "same-owner", "full-token-payment", "restorations carry exact labelled nonroot full-token incidence"),
 e("global-active-edge-episode-bound", ["CMR923","CMR924"], "same-owner", "history-budget", "sum per-edge owner bounds and finite minimum-core rank"),
 e("fixed-owner-recurrent-edge-dispatch", ["CMR922","CMR925"], "same-owner", "scheduler-dispatch", "scheduler redeletes contracts or exits on a recurrent fixed-owner edge"),
]

CONTRACT = {"schema":"prime-power-installed-operation-registry-286/v1",
            "base_registry_sha256":BASE_REGISTRY_SHA256,
            "base_operation_kind_count":BASE_OPERATION_KIND_COUNT,
            "base_contract_count":BASE_CONTRACT_COUNT,
            "base_owner_changing_kind_count":BASE_OWNER_CHANGING_KIND_COUNT,
            "new_contract_sha256":NEW_CONTRACT_SHA256,
            "new_entries":NEW_ENTRIES,
            "honesty_flags":{"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,
                             "actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST = "46f989ec87e87fb4a4bff9302bb5ca00a396d7e84861f9df6f0cab58bb6e38dc"

ALLOWED_OWNERS={"same-owner","host-owner-change","factor-child-owner-change","restoration-owner-change"}
ALLOWED_PAYMENTS={"local-family-equivalence","factor-product-dispatch","owner-witness-stock","scheduler-dispatch",
                  "branch-cover-dispatch","strict-child-descent","local-family-restriction","strict-factor-contraction",
                  "support-packing","host-edge-deletion","history-budget","edge-reintroduction","full-token-payment"}

def validate(entries: list[dict[str,Any]]) -> dict[str,Any]:
    require(len(entries)==47,"forty-seven operations required")
    kinds=set(); owner_changes=BASE_OWNER_CHANGING_KIND_COUNT; payments={}
    for i,x in enumerate(entries):
        p=f"entry[{i}]"; kind=x.get("operation_kind")
        require(isinstance(kind,str) and kind and kind not in kinds,f"{p}: unique kind"); kinds.add(kind)
        require(x.get("contract_sha256")==NEW_CONTRACT_SHA256,f"{p}: contract")
        src=x.get("source_theorems"); require(isinstance(src,list) and src and all(s.startswith("CMR") for s in src),f"{p}: sources")
        owner=x.get("owner_effect"); payment=x.get("payment_class"); cont=x.get("continuation")
        require(owner in ALLOWED_OWNERS,f"{p}: owner"); require(payment in ALLOWED_PAYMENTS,f"{p}: payment")
        require(isinstance(cont,str) and cont,f"{p}: continuation")
        if payment=="scheduler-dispatch": require("scheduler" in cont,f"{p}: scheduler")
        if payment=="local-family-restriction": require(owner=="host-owner-change" and ("child" in cont or "delet" in cont),f"{p}: restriction")
        if payment=="strict-factor-contraction": require(owner=="factor-child-owner-change" and "contract" in cont,f"{p}: contraction")
        if payment=="edge-reintroduction": require(owner in {"host-owner-change","restoration-owner-change"} and ("restored" in cont or "redelet" in cont),f"{p}: reintroduction")
        owner_changes += owner!="same-owner"; payments[payment]=payments.get(payment,0)+1
    total=BASE_OPERATION_KIND_COUNT+len(kinds); require(total==286,"286 kinds required")
    return {"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"new_operation_kind_count":len(kinds),
            "installed_operation_kind_count":total,"bound_contract_count":BASE_CONTRACT_COUNT+1,
            "owner_changing_operation_kinds":owner_changes,"same_owner_operation_kinds":total-owner_changes,
            "new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}

def mutation_audit()->int:
    muts=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]["operation_kind"]),
          lambda x:x[0].update(contract_sha256="0"*64),lambda x:x[0].update(source_theorems=[]),
          lambda x:x[0].update(owner_effect="anonymous"),lambda x:x[0].update(payment_class="free"),
          lambda x:x[0].update(continuation=""),lambda x:x[3].update(continuation="recurse"),
          lambda x:x[7].update(owner_effect="same-owner"),lambda x:x[9].update(owner_effect="same-owner"),
          lambda x:x[41].update(owner_effect="same-owner"),lambda x:x.pop()]
    rejected=0
    for m in muts:
        bad=copy.deepcopy(NEW_ENTRIES); m(bad)
        try: validate(bad)
        except Registry286Error: rejected+=1
    require(rejected==len(muts),"corruption accepted"); return rejected

def main()->None:
    cd=digest(CONTRACT)
    if EXPECTED_CONTRACT_DIGEST!="TO_FILL": require(cd==EXPECTED_CONTRACT_DIGEST,"contract digest")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    print(json.dumps({"contract_digest":cd,"census":census,"installed_transition_kind_bank_286_exhaustive":1,
                      "scc_branch_minimum_face_operations_registered":1,"installed_payment_assignment_286_complete":1,
                      "all_owner_operations_proved":0,"all_scheduler_operations_proved":0,
                      "all_restoration_operations_proved":0,"all_construction_ancestry_proved":0,
                      "global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,
                      "actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))
if __name__=="__main__":main()
