#!/usr/bin/env python3
"""Verify the signed orbit cycle-cover CSP for swapped quarter-turn seed codes."""
from __future__ import annotations
import argparse, json, math, sys
from itertools import combinations
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_quarter_turn_seed_normal_forms as qt

Point = tuple[int, int]
LineKey = tuple[int, int, int]

def orbit(i:int,j:int,e:int,n:int)->set[Point]:
    I=n-1-i; J=n-1-j
    if e==0:return {(i,j),(I,J),(j,I),(J,i)}
    return {(i,J),(I,j),(j,i),(J,I)}

def line_key(a:Point,b:Point)->LineKey|None:
    dx=b[0]-a[0];dy=b[1]-a[1]
    if dx==0 or dy==0:return None
    g=math.gcd(abs(dx),abs(dy));dx//=g;dy//=g
    if dx<0:dx=-dx;dy=-dy
    return dx,dy,dy*a[0]-dx*a[1]

def on_line(point:Point,key:LineKey)->bool:
    dx,dy,c=key
    return dy*point[0]-dx*point[1]==c

def occupied_nonaxis_lines(points:set[Point])->set[LineKey]:
    return {key for a,b in combinations(sorted(points),2) if (key:=line_key(a,b)) is not None}

def partition(p:list[int])->list[int]:
    seen=[False]*len(p);out=[]
    for x in range(len(p)):
        if seen[x]:continue
        y=x;k=0
        while not seen[y]:seen[y]=True;k+=1;y=p[y]
        out.append(k)
    return sorted(out,reverse=True)

def verify_case(raw:Any,index:int)->dict[str,Any]:
    if not isinstance(raw,dict):raise ValueError(f"case {index}: object expected")
    p=raw.get("p");code=raw.get("code")
    if isinstance(p,bool) or not isinstance(p,int) or not qt.prime(p):raise ValueError(f"case {index}: bad prime")
    if not isinstance(code,str):raise ValueError(f"case {index}: code expected")
    n=p-1;m=n//2
    tag,points=qt.decode(code,n)
    determinant_checks=qt.verify_seed(points,n)
    answer=qt.colour(points,n,1)
    if answer is None:raise ValueError(f"case {index}: no swapped-equivariant colouring")
    sigma,tau=answer
    rho=[];sign=[]
    for i in range(m):
        y=sigma[i]
        rho.append(y if y<m else n-1-y)
        sign.append(0 if y<m else 1)
    if sorted(rho)!=list(range(m)):raise ValueError(f"case {index}: rho is not a permutation")

    blocks=[];reconstructed:set[Point]=set()
    for i,(j,e) in enumerate(zip(rho,sign)):
        block=orbit(i,j,e,n)
        if len(block)!=4:raise ValueError(f"case {index}: orbit block does not have four cells")
        if i==j and block!=orbit(i,j,1-e,n):raise ValueError(f"case {index}: self-loop orientation quotient failed")
        if reconstructed & block:raise ValueError(f"case {index}: duplicate orbit block")
        reconstructed |= block;blocks.append(block)
    if reconstructed!=points:raise ValueError(f"case {index}: orbit union changed selected set")

    for i in range(m):
        j=rho[i]
        if i<j and rho[j]==i and (sign[i]^sign[j]):
            raise ValueError(f"case {index}: opposite-sign two-cycle")

    lines=occupied_nonaxis_lines(points);maximum=0
    for key in lines:
        linear=sum(sum(on_line(point,key) for point in block) for block in blocks)
        direct=sum(on_line(point,key) for point in points)
        if linear!=direct:raise ValueError(f"case {index}: line coefficient sum mismatch")
        maximum=max(maximum,linear)
        if linear>2:raise ValueError(f"case {index}: maximal-line capacity exceeded")

    pair_cycles=partition(rho)
    expected=raw.get("expected_pair_cycles")
    if expected is not None:
        if not isinstance(expected,list) or sorted(expected,reverse=True)!=pair_cycles:
            raise ValueError(f"case {index}: pair cycles {pair_cycles} != {expected}")
    return {
        "p":p,"n":n,"pair_vertices":m,"symmetry_tag":tag,
        "canonical_binary_variables":2*m*m-m,
        "duplicate_orbit_inequalities":m*(m-1),
        "chosen_orbits":m,"selected_points":len(points),
        "pair_cycle_partition":pair_cycles,"orientation_one_count":sum(sign),
        "occupied_nonaxis_lines":len(lines),"maximum_line_occupancy":maximum,
        "determinant_checks":determinant_checks,
        "orbit_cycle_cover_valid":True
    }

def main()->None:
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("input",type=Path);args=parser.parse_args()
    try:
        raw=json.loads(args.input.read_text(encoding="utf-8"));cases=raw if isinstance(raw,list) else [raw]
        if not cases:raise ValueError("empty input")
        checked=[verify_case(value,i+1) for i,value in enumerate(cases)]
    except (OSError,ValueError,json.JSONDecodeError) as exc:raise SystemExit(f"verification failed: {exc}") from exc
    print(json.dumps({"outcome":"swapped_quarter_turn_orbit_csp_verified","case_count":len(checked),"cases":checked,"total_determinant_checks":sum(c["determinant_checks"] for c in checked),"asymptotic_seed_theorem_proved":False},indent=2,sort_keys=True))
if __name__=="__main__":main()
