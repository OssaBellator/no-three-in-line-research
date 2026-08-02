#!/usr/bin/env python3
"""Prove first-host background non-identifiability under the side-four projection."""
from __future__ import annotations
import argparse, copy, hashlib, json, math
from itertools import combinations
from pathlib import Path
from typing import Iterable

Point=tuple[int,int]
Line=tuple[int,int,int]
Perm=tuple[int,...]

HOST_ID="s4-75b04c45c1c8eac2"
BLOCKER_ID="b4-8a44614df456"
RESPONSES={
    "3012":(3,0,1,2),
    "3210":(3,2,1,0),
    "2031":(2,0,3,1),
    "2310":(2,3,1,0),
    "3201":(3,2,0,1),
}
SAFE_BACKGROUND:tuple[Point,...]=()
STRICT_BACKGROUND:tuple[Point,...]=((-3,5),(5,-3))

class AuditError(RuntimeError): pass
def require(ok:bool,message:str)->None:
    if not ok: raise AuditError(message)

def response_points(permutation:Perm)->tuple[Point,...]:
    return tuple((row,permutation[row]) for row in range(4))

def normalize_line(first:Point,second:Point)->Line:
    require(first!=second,"line")
    x1,y1=first;x2,y2=second
    a,b,c=y1-y2,x2-x1,x1*y2-x2*y1
    divisor=math.gcd(math.gcd(abs(a),abs(b)),abs(c))
    require(divisor>0,"zero line")
    a,b,c=a//divisor,b//divisor,c//divisor
    if a<0 or (a==0 and b<0): a,b,c=-a,-b,-c
    return a,b,c

def on_line(point:Point,line:Line)->bool:
    x,y=point;a,b,c=line
    return a*x+b*y+c==0

def triple_count(points:Iterable[Point])->int:
    sequence=tuple(points)
    return sum(
        1 for first,second,third in combinations(sequence,3)
        if on_line(third,normalize_line(first,second))
    )

def score(name:str,background:tuple[Point,...])->int:
    response=response_points(RESPONSES[name])
    require(not set(background)&set(response),f"{name}: overlap")
    return triple_count((*background,*response))-triple_count(background)

def score_vector(background:tuple[Point,...])->dict[str,int]:
    return {name:score(name,background) for name in RESPONSES}

def minimizer_face(scores:dict[str,int])->list[str]:
    minimum=min(scores.values())
    return [name for name,value in scores.items() if value==minimum]

def side_four_projection()->dict[str,object]:
    return {
        "host_id":HOST_ID,
        "deletion_edges":"02,20",
        "responses":["3012:1","3210:4"],
        "dispatch":"blocker-alternative",
        "contained_blockers":[BLOCKER_ID],
    }

def lineage_identifier(background:tuple[Point,...])->str:
    payload={
        "side":4,
        "host_id":HOST_ID,
        "deletion_edges":["02","20"],
        "target":"01",
        "background":[list(point) for point in background],
    }
    return hashlib.sha256(
        json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
    ).hexdigest()

def compile_manifest()->dict[str,object]:
    projection=side_four_projection()
    safe_scores=score_vector(SAFE_BACKGROUND)
    strict_scores=score_vector(STRICT_BACKGROUND)
    require(safe_scores=={"3012":1,"3210":4,"2031":0,"2310":0,"3201":0},"safe scores")
    require(strict_scores=={"3012":1,"3210":4,"2031":2,"2310":2,"3201":2},"strict scores")
    require(minimizer_face(safe_scores)==["2031","2310","3201"],"safe face")
    require(minimizer_face(strict_scores)==["3012"],"strict face")
    require(lineage_identifier(SAFE_BACKGROUND)!=lineage_identifier(STRICT_BACKGROUND),"complete identifiers")
    require(projection==side_four_projection(),"same projection")

    return {
        "schema":"exact-recurrent-first-host-side-four-projection-nonidentifiability/v1",
        "scope":{
            "host_id":HOST_ID,
            "side_four_projection_encoding":"host_id,deletion_edges,intrinsic response energies,dispatch,blockers",
        },
        "projected_record":projection,
        "completions":[
            {
                "kind":"safe-empty-background",
                "background":[],
                "complete_lineage_identifier":lineage_identifier(SAFE_BACKGROUND),
                "complete_score_vector":safe_scores,
                "minimizer_face":minimizer_face(safe_scores),
            },
            {
                "kind":"strict-two-point-reversal",
                "background":[list(point) for point in STRICT_BACKGROUND],
                "complete_lineage_identifier":lineage_identifier(STRICT_BACKGROUND),
                "complete_score_vector":strict_scores,
                "minimizer_face":minimizer_face(strict_scores),
            },
        ],
        "aggregate":{
            "projected_records":1,
            "distinct_complete_lineage_identifiers":2,
            "distinct_complete_score_vectors":2,
            "distinct_minimizer_faces":2,
            "background_coordinates_present_in_projection":0,
            "physical_deletion_causes_present_in_projection":0,
            "physical_owner_labels_present_in_projection":0,
        },
        "missing_fields_required_for_physical_exclusion":[
            "coordinate-labelled background",
            "physical deletion causes for 02 and 20",
            "owner/fate/collision/line/interface/CRT ancestry",
            "installed legal operations and intermediate states",
            "labelled child multiplicities and weights",
        ],
        "honesty":{
            "projection_noninjectivity_for_complete_scores_proved":1,
            "strict_reversal_physically_realizable":0,
            "strict_reversal_physically_excluded":0,
            "physical_background_coverage_proved":0,
            "recurrent_child_rows_populated":0,
            "strict_lyapunov_certificate_proved":0,
            "all_n_proved_by_checker":0,
        },
    }

def validate(manifest:dict[str,object])->None:
    require(manifest==compile_manifest(),"manifest differs from compiler")
    honesty=manifest.get("honesty")
    require(isinstance(honesty,dict),"honesty")
    require(honesty.get("projection_noninjectivity_for_complete_scores_proved")==1,"noninjectivity")
    require(honesty.get("strict_reversal_physically_realizable")==0,"realizability")
    require(honesty.get("strict_reversal_physically_excluded")==0,"exclusion")
    require(honesty.get("all_n_proved_by_checker")==0,"all-n")

def mutation_audit(manifest:dict[str,object])->int:
    mutations=[
        lambda item:item["aggregate"].update(projected_records=2),
        lambda item:item["aggregate"].update(distinct_complete_score_vectors=1),
        lambda item:item["aggregate"].update(background_coordinates_present_in_projection=1),
        lambda item:item["projected_record"].update(deletion_edges="02"),
        lambda item:item["completions"][0]["complete_score_vector"].update({"2031":1}),
        lambda item:item["completions"][1]["complete_score_vector"].update({"3012":2}),
        lambda item:item["completions"][1].update(minimizer_face=["2031"]),
        lambda item:item["missing_fields_required_for_physical_exclusion"].pop(),
        lambda item:item["honesty"].update(strict_reversal_physically_excluded=1),
        lambda item:item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected=0
    for mutate in mutations:
        candidate=copy.deepcopy(manifest);mutate(candidate)
        try: validate(candidate)
        except (AuditError,KeyError,TypeError,ValueError): rejected+=1
    require(rejected==len(mutations),"mutation audit")
    return rejected

def main()->None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--write",type=Path)
    parser.add_argument("--check",type=Path)
    arguments=parser.parse_args()
    manifest=compile_manifest()
    if arguments.write:
        arguments.write.parent.mkdir(parents=True,exist_ok=True)
        arguments.write.write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    if arguments.check:
        validate(json.loads(arguments.check.read_text(encoding="utf-8")))
    print(json.dumps({
        "checker":"exact-recurrent-first-host-side-four-projection-nonidentifiability",
        **manifest["aggregate"],
        "mutation_corruptions_rejected":mutation_audit(manifest),
        **manifest["honesty"],
    },sort_keys=True))

if __name__=="__main__": main()
