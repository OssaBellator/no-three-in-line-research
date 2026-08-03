#!/usr/bin/env python3
"""Reject-by-default source gate for first-host minimizer-face congruence."""
from __future__ import annotations
import argparse, copy, hashlib, itertools, json
from pathlib import Path

HOST="s4-75b04c45c1c8eac2"
WORK=Path("data/exact_recurrent_first_host_selector_face_congruence_worklist.json")
DOCS=(
 ("owner-fate-lineage-kernel-ancestry",Path("docs/554-prime-power-owner-fate-lineage-kernel-ancestry.md"),
  ("common_owner","child_row","payment"),
  ("Every recurrent child coefficient has one exact compression key containing structural owner",
   "A compulsory weighted assignment certificate contains every declared return",
   "Ties retain an exact minimizer face and selector switches require an explicit threshold crossing.",
   "owner_fate_rows_populated_all_recurrent_states = 0")),
 ("installed-operation-registry-1166",Path("docs/555-prime-power-installed-operation-registry-1166.md"),
  ("common_owner","operation","payment","closure_route"),
  ("Every entry has a literal nonempty CMR1894--CMR1965 source list and nonempty continuation rule.",
   "All 72 operations preserve structural owner.",
   "Nineteen local-family equivalences bind lossless class compression",
   "Installed-bank exhaustiveness applies only to the declared 1166-kind registry.")))
COMP=("common_owner","operation","child_row","payment","closure_route")
SIG_FIELDS=("physical_occurrence_domain_ref","legal_menu_state_ref","operation_signature_domain_ref",
 "common_owner_ref","operation_congruence_ref","child_row_congruence_ref","payment_congruence_ref",
 "closure_route_congruence_ref","realization_status")
PAR_FIELDS=("physical_occurrence_domain_ref","legal_menu_state_domain_ref","signature_domain_completeness_ref",
 "common_owner_schema_ref","operation_congruence_ref","child_row_congruence_ref","payment_congruence_ref",
 "closure_route_congruence_ref","theorem_ref","realization_status")
LABELS=("2031","2301","2310","3201")

class AuditError(RuntimeError): pass
def req(x,m):
 if not x: raise AuditError(m)
def ident(prefix,payload):
 s=json.dumps(payload,sort_keys=True,separators=(",",":"))
 return prefix+"-"+hashlib.sha256(s.encode()).hexdigest()[:12]
def load(root,path):
 p=root/path; req(p.is_file(),f"missing {path}")
 x=json.loads(p.read_text()); req(isinstance(x,dict),f"object {path}"); return x

def compile_manifest(root):
 w=load(root,WORK); a=w.get("aggregate",{}); b=w.get("source_boundary",{})
 req(w.get("schema")=="exact-recurrent-first-host-selector-face-congruence-worklist/v1","schema")
 req(w.get("host_id")==HOST,"host")
 req((a.get("signature_pair_obligations"),a.get("menu_parametric_pair_theorem_domains"),
      a.get("cross_menu_pair_theorem_types"),a.get("total_signature_evidence_slots"),
      a.get("populated_signature_evidence_slots"),a.get("accepted_signature_obligations"))
     ==(32,4,3,288,0,0),"worklist census")
 req((b.get("selector_tie_break_substitution_allowed"),b.get("operation_signature_physically_complete"))==(0,0),"boundary")
 sources=[]; union=set(); combined=""
 for sid,path,components,markers in DOCS:
  text=(root/path).read_text()
  req(all(m in text for m in markers),f"markers {sid}")
  found=[x for x in LABELS if x in text]; req(not found,f"labels {sid}")
  union.update(components); combined+=text
  sources.append({"source_id":sid,"path":str(path),"abstract_components":list(components),
   "abstract_component_count":len(components),"first_host_response_labels_found":found,
   "occurrence_faithful_pair_join_found":0})
 req(union==set(COMP) and all(x not in combined for x in LABELS),"source union")
 sig=[]; pairmenus={}; slots=0
 for cell in w["cells"]:
  for ob in cell["basis_obligations"]:
   ev=ob["evidence"]; req(set(ev)==set(SIG_FIELDS) and all(ev[x] is None for x in SIG_FIELDS),"evidence")
   req((ob["evidence_fields_populated"],ob["congruence_accepted"])==(0,0),"obligation")
   st={"menu":cell["menu"],"operation_signature":cell["operation_signature"],
       "response_pair":ob["response_pair"],"background_count":cell["background_count"]}
   sig.append({"record_id":ident("fc-sig",st),**st,"source_import_accepted":0})
   pairmenus.setdefault(tuple(ob["response_pair"]),set()).add(cell["menu"]); slots+=len(SIG_FIELDS)
 req(len(sig)==32 and slots==288,"signature records")
 menu=[]
 for r in w["menu_parametric_domains"]:
  st={k:r[k] for k in ("menu","response_pair","signature_classes","background_cases")}
  menu.append({"record_id":ident("fc-menu",st),**st,"source_import_accepted":0})
 req(len(menu)==4,"menu records")
 census={tuple(r["response_pair"]):r for r in w["pair_type_census"]}; req(set(census)==set(pairmenus),"pairs")
 cross=[]
 for p in sorted(census):
  r=census[p]; st={"response_pair":list(p),"menus":sorted(pairmenus[p]),
   "signature_obligations":r["signature_obligations"],
   "raw_background_comparisons":r["raw_background_comparisons"]}
  cross.append({"record_id":ident("fc-cross",st),**st,"source_import_accepted":0})
 req(len(cross)==3 and next(r for r in cross if r["response_pair"]==["2031","2310"])["menus"]
     ==["restore_02","restore_both"],"cross records")
 covers=[]
 for mask in range(1,1<<len(sources)):
  chosen=[sources[i] for i in range(len(sources)) if mask>>i&1]
  if set().union(*(set(x["abstract_components"]) for x in chosen))==set(COMP):
   covers.append([x["source_id"] for x in chosen])
 req(covers==[[x["source_id"] for x in sources]],"source cover")
 modes={
  "signature_specific":{"record_registry":sig,"record_count":32,"evidence_fields":list(SIG_FIELDS),
   "evidence_fields_per_record":9,"evidence_slots":288,"populated_evidence_slots":0,"accepted_records":0,"mode_accepted":0},
  "menu_parametric":{"record_registry":menu,"record_count":4,"evidence_fields":list(PAR_FIELDS),
   "evidence_fields_per_record":10,"evidence_slots":40,"populated_evidence_slots":0,"accepted_records":0,"mode_accepted":0},
  "cross_menu_parametric":{"record_registry":cross,"record_count":3,"evidence_fields":list(PAR_FIELDS),
   "evidence_fields_per_record":10,"evidence_slots":30,"populated_evidence_slots":0,"accepted_records":0,"mode_accepted":0}}
 return {"schema":"exact-recurrent-first-host-selector-face-source-import-gate/v1","host_id":HOST,
  "sources":{"face_congruence_worklist":str(WORK),"audited_abstract_sources":sources,
   "required_abstract_components":list(COMP),"minimum_abstract_source_cover_size":2,
   "minimum_abstract_source_covers":covers},"acceptance_modes":modes,
  "aggregate":{"source_documents_audited":2,"abstract_components_required":5,
   "abstract_components_covered_by_union":5,"minimum_abstract_source_cover_size":2,
   "first_host_response_labels_found_in_sources":0,"occurrence_faithful_pair_joins_found":0,
   "acceptance_modes":3,"accepted_modes":0,"signature_specific_records":32,
   "signature_specific_evidence_slots":288,"menu_parametric_records":4,
   "menu_parametric_evidence_slots":40,"cross_menu_parametric_records":3,
   "cross_menu_parametric_evidence_slots":30,"populated_evidence_slots_all_modes":0,
   "accepted_import_records_all_modes":0},
  "source_boundary":{"abstract_schema_component_union_complete":1,"single_abstract_source_complete":0,
   "abstract_source_cover_occurrence_faithful":0,"response_pair_specific_source_theorem_found":0,
   "signature_specific_import_available":0,"menu_parametric_import_available":0,
   "cross_menu_import_available":0,"face_congruence_source_import_accepted":0,
   "selector_tie_break_substitution_allowed":0},
  "honesty":{"physical_occurrence_coverage_proved":0,"legal_restoration_operation_proved":0,
   "persistent_owner_identity_proved":0,"recurrent_child_rows_populated":0,
   "payment_congruence_proved":0,"closure_route_congruence_proved":0,
   "strict_lyapunov_certificate_proved":0,"global_termination_proved":0,
   "all_n_proved_by_checker":0}}

def validate(root,x): req(x==compile_manifest(root),"manifest")
def mutations(root,x):
 edits=[
  lambda y:y["aggregate"].__setitem__("abstract_components_covered_by_union",4),
  lambda y:y["aggregate"].__setitem__("minimum_abstract_source_cover_size",1),
  lambda y:y["aggregate"].__setitem__("first_host_response_labels_found_in_sources",1),
  lambda y:y["aggregate"].__setitem__("occurrence_faithful_pair_joins_found",1),
  lambda y:y["aggregate"].__setitem__("accepted_modes",1),
  lambda y:y["aggregate"].__setitem__("signature_specific_records",31),
  lambda y:y["aggregate"].__setitem__("menu_parametric_records",3),
  lambda y:y["aggregate"].__setitem__("cross_menu_parametric_records",2),
  lambda y:y["aggregate"].__setitem__("populated_evidence_slots_all_modes",1),
  lambda y:y["acceptance_modes"]["signature_specific"]["record_registry"][0].__setitem__("source_import_accepted",1),
  lambda y:y["acceptance_modes"]["menu_parametric"].__setitem__("populated_evidence_slots",1),
  lambda y:y["acceptance_modes"]["cross_menu_parametric"]["record_registry"][1]["menus"].pop(),
  lambda y:y["sources"]["audited_abstract_sources"][0]["abstract_components"].append("closure_route"),
  lambda y:y["source_boundary"].__setitem__("single_abstract_source_complete",1),
  lambda y:y["source_boundary"].__setitem__("face_congruence_source_import_accepted",1),
  lambda y:y["source_boundary"].__setitem__("selector_tie_break_substitution_allowed",1),
  lambda y:y["honesty"].__setitem__("payment_congruence_proved",1),
  lambda y:y["honesty"].__setitem__("all_n_proved_by_checker",1)]
 rejected=0
 for edit in edits:
  y=copy.deepcopy(x); edit(y)
  try: validate(root,y)
  except AuditError: rejected+=1
 req(rejected==len(edits),"mutations"); return rejected

def main():
 p=argparse.ArgumentParser(); p.add_argument("--root",type=Path,default=Path("."))
 p.add_argument("--check",type=Path); p.add_argument("--write",type=Path); q=p.parse_args()
 x=compile_manifest(q.root); mutations(q.root,x)
 if q.check: validate(q.root,json.loads(q.check.read_text()))
 if q.write: q.write.write_text(json.dumps(x,indent=2,sort_keys=True)+"\n")
 if not q.check and not q.write: print(json.dumps(x,indent=2,sort_keys=True))
if __name__=="__main__": main()
