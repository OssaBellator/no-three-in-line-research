#!/usr/bin/env python3
"""Verify quarter-turn-equivariant two-permutation normal forms for seed codes."""
from __future__ import annotations
import argparse, json
from collections import Counter, defaultdict, deque
from itertools import combinations
from pathlib import Path
from typing import Any

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$%&@?!()[]<>{}=*+|-/~^_:;,."
Point = tuple[int, int]

def prime(p:int)->bool:
    if p<2:return False
    if p%2==0:return p==2
    d=3
    while d*d<=p:
        if p%d==0:return False
        d+=2
    return True

def decode(code:str,n:int)->tuple[str,set[Point]]:
    if len(code)!=1+2*n: raise ValueError(f"code length {len(code)} != {1+2*n}")
    pts:set[Point]=set()
    for y in range(n):
        xs=[]
        for ch in code[1+2*y:3+2*y]:
            if ch not in ALPHABET: raise ValueError(f"unknown symbol {ch!r}")
            x=ALPHABET.index(ch)
            if x>=n: raise ValueError(f"row {y+1}: column {x+1}>n")
            xs.append(x)
        if xs[0]==xs[1]: raise ValueError(f"row {y+1}: duplicate cell")
        pts.update((x,y) for x in xs)
    return code[0],pts

def det(a:Point,b:Point,c:Point)->int:
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def verify_seed(pts:set[Point],n:int)->int:
    if len(pts)!=2*n: raise ValueError("not 2n distinct cells")
    rows=Counter(y for _,y in pts); cols=Counter(x for x,_ in pts)
    if any(rows[i]!=2 or cols[i]!=2 for i in range(n)): raise ValueError("not saturated")
    checks=0
    for a,b,c in combinations(sorted(pts),3):
        checks+=1
        if det(a,b,c)==0: raise ValueError(f"collinear triple {a},{b},{c}")
    return checks

def rot(e:Point,n:int)->Point: return n-1-e[1],e[0]

def qperm(s:list[int])->list[int]:
    n=len(s); inv=[0]*n
    for x,y in enumerate(s): inv[y]=x
    return [inv[n-1-x] for x in range(n)]

def rel(s:list[int],t:list[int])->list[int]:
    inv=[0]*len(s)
    for x,y in enumerate(s): inv[y]=x
    return [inv[t[x]] for x in range(len(s))]

def cycles(p:list[int])->list[int]:
    seen=[False]*len(p); out=[]
    for x in range(len(p)):
        if seen[x]: continue
        y=x;k=0
        while not seen[y]: seen[y]=True;k+=1;y=p[y]
        out.append(k)
    return sorted(out,reverse=True)

def colour(pts:set[Point],n:int,eps:int)->tuple[list[int],list[int]]|None:
    if {rot(e,n) for e in pts}!=pts:return None
    rows:dict[int,list[Point]]=defaultdict(list); cols:dict[int,list[Point]]=defaultdict(list)
    for e in pts: cols[e[0]].append(e); rows[e[1]].append(e)
    if any(len(rows[i])!=2 or len(cols[i])!=2 for i in range(n)):return None
    adj:dict[Point,list[tuple[Point,int]]]=defaultdict(list)
    for e in pts:
        for f in rows[e[1]]+cols[e[0]]:
            if f!=e: adj[e].append((f,1))
        adj[e].append((rot(e,n),eps))
    c:dict[Point,int]={}
    for start in sorted(pts):
        if start in c:continue
        c[start]=0;q=deque([start])
        while q:
            e=q.popleft()
            for f,d in adj[e]:
                want=c[e]^d
                if f in c:
                    if c[f]!=want:return None
                else:c[f]=want;q.append(f)
    layers=[[-1]*n,[-1]*n]
    for (x,y),z in c.items():
        if layers[z][x]!=-1:return None
        layers[z][x]=y
    if any(sorted(s)!=list(range(n)) for s in layers):return None
    return layers[0],layers[1]

def case(raw:Any,i:int)->dict[str,Any]:
    if not isinstance(raw,dict):raise ValueError(f"case {i}: object expected")
    p=raw.get("p")
    if isinstance(p,bool) or not isinstance(p,int) or not prime(p):raise ValueError(f"case {i}: bad prime")
    n=p-1; code=raw.get("code")
    if not isinstance(code,str):raise ValueError(f"case {i}: code expected")
    tag,pts=decode(code,n); checks=verify_seed(pts,n)
    if {rot(e,n) for e in pts}!=pts:raise ValueError(f"case {i}: not quarter-turn invariant")
    J=[n-1-x for x in range(n)]; modes=[]; details={}
    for eps,mode in ((0,"fixed"),(1,"swapped")):
        ans=colour(pts,n,eps)
        if ans is None:continue
        s,t=ans
        if {(x,s[x]) for x in range(n)}|{(x,t[x]) for x in range(n)}!=pts:raise ValueError("reconstruction failed")
        if mode=="fixed":
            if qperm(s)!=s or qperm(t)!=t or any(s[s[x]]!=J[x] or t[t[x]]!=J[x] for x in range(n)):raise ValueError("fixed normal form failed")
            if n%4:raise ValueError("fixed mode with 4 not dividing n")
        else:
            if qperm(s)!=t or qperm(t)!=s:raise ValueError("swapped action failed")
            if any(s[J[x]]!=J[s[x]] for x in range(n)):raise ValueError("centralizer identity failed")
            inv=[0]*n
            for x,y in enumerate(s):inv[y]=x
            if t!=[inv[J[x]] for x in range(n)]:raise ValueError("forced second layer failed")
            if any((s[x]==t[x])!=(s[s[x]]==J[x]) for x in range(n)):raise ValueError("disjointness equivalence failed")
        pi=rel(s,t)
        if any(pi[J[x]]!=J[pi[x]] for x in range(n)):raise ValueError("relative centralizer failed")
        part=cycles(pi); mult=Counter(part)
        if any(k%2 and v%2 for k,v in mult.items()):raise ValueError("odd-cycle parity failed")
        modes.append(mode);details[mode]={"sigma":[v+1 for v in s],"tau":[v+1 for v in t],"relative_cycle_partition":part}
    exp=raw.get("expected_quarter_turn_modes")
    if exp is not None and sorted(modes)!=sorted(exp):raise ValueError(f"case {i}: modes {modes} != {exp}")
    if not modes:raise ValueError(f"case {i}: no equivariant colouring")
    return {"p":p,"n":n,"symmetry_tag":tag,"equivariant_modes":modes,"determinant_checks":checks,"details":details}

def main()->None:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("input",type=Path);args=ap.parse_args()
    try:
        raw=json.loads(args.input.read_text()); cases=raw if isinstance(raw,list) else [raw]
        if not cases:raise ValueError("empty input")
        out=[case(v,i+1) for i,v in enumerate(cases)]
    except (OSError,ValueError,json.JSONDecodeError) as e:raise SystemExit(f"verification failed: {e}") from e
    print(json.dumps({"outcome":"quarter_turn_seed_normal_forms_verified","case_count":len(out),"cases":out,"total_determinant_checks":sum(v["determinant_checks"] for v in out),"asymptotic_seed_theorem_proved":False},indent=2,sort_keys=True))
if __name__=="__main__":main()
