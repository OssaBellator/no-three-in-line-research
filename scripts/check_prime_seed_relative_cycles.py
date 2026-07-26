#!/usr/bin/env python3
"""Check relative-permutation cycles and maximal-line constraints for seed certificates."""
from __future__ import annotations
import argparse, json, math
from itertools import combinations
from pathlib import Path
from typing import Any

Point=tuple[int,int]

def is_prime(p:int)->bool:
    if p<2:return False
    if p%2==0:return p==2
    d=3
    while d*d<=p:
        if p%d==0:return False
        d+=2
    return True

def norm_line(a:Point,b:Point)->tuple[int,int,int]:
    x1,y1=a;x2,y2=b
    A=y2-y1;B=x1-x2;C=-(A*x1+B*y1)
    g=math.gcd(math.gcd(abs(A),abs(B)),abs(C))
    A//=g;B//=g;C//=g
    if A<0 or (A==0 and B<0):
        A=-A;B=-B;C=-C
    return A,B,C

def maximal_lines(n:int)->list[tuple[Point,...]]:
    pts=[(x,y) for x in range(1,n+1) for y in range(1,n+1)]
    keys={norm_line(a,b) for a,b in combinations(pts,2)}
    lines=[]
    for A,B,C in keys:
        line=tuple(p for p in pts if A*p[0]+B*p[1]+C==0)
        if len(line)>=3:
            lines.append(line)
    return lines

def cycles(pi:list[int])->list[list[int]]:
    seen=set();out=[]
    for start in range(1,len(pi)+1):
        if start in seen:continue
        cyc=[];x=start
        while x not in seen:
            seen.add(x);cyc.append(x);x=pi[x-1]
        out.append(cyc)
    return out

def analyse_case(case:dict[str,Any])->dict[str,Any]:
    p=int(case["p"]);n=p-1
    sigma=list(map(int,case["sigma"]));tau=list(map(int,case["tau"]))
    expected=list(range(1,n+1))
    if not is_prime(p):raise ValueError(f"p={p} is not prime")
    if sorted(sigma)!=expected or sorted(tau)!=expected:raise ValueError(f"p={p}: not permutations")
    if any(a==b for a,b in zip(sigma,tau)):raise ValueError(f"p={p}: layers share a cell")
    inv_sigma={v:i+1 for i,v in enumerate(sigma)}
    pi=[inv_sigma[v] for v in tau]
    if any(pi[i]==i+1 for i in range(n)):raise ValueError(f"p={p}: relative permutation has a fixed point")
    cyc=cycles(pi)
    pts={(i+1,sigma[i]) for i in range(n)}|{(i+1,tau[i]) for i in range(n)}
    lines=maximal_lines(n)
    occ=[len(pts.intersection(line)) for line in lines]
    max_occ=max(occ,default=0)
    violating=sum(v>=3 for v in occ)
    reconstruction=[sigma[pi[i]-1] for i in range(n)]
    return {
        "p":p,"n":n,"relative_permutation":pi,
        "relative_derangement":all(pi[i]!=i+1 for i in range(n)),
        "relative_cycle_lengths":sorted((len(c) for c in cyc),reverse=True),
        "incidence_component_lengths":sorted((2*len(c) for c in cyc),reverse=True),
        "tau_reconstruction_ok":reconstruction==tau,
        "maximal_grid_lines_checked":len(lines),
        "maximum_selected_points_on_one_line":max_occ,
        "violating_maximal_lines":violating,
        "compressed_line_system_satisfied":violating==0,
    }

def main()->None:
    ap=argparse.ArgumentParser();ap.add_argument("input",type=Path);args=ap.parse_args()
    raw=json.loads(args.input.read_text(encoding="utf-8"));cases=raw if isinstance(raw,list) else [raw]
    result=[analyse_case(c) for c in cases]
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=="__main__":main()
