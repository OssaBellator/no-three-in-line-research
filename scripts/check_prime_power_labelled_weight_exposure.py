#!/usr/bin/env python3
"""Exact positive-weight support or convex obstruction for labelled response vectors."""
from __future__ import annotations
import copy, json, math, sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from random import Random
from scipy.optimize import linprog
import check_geometric_assignment_bundle as assignment
import check_geometric_owner_fate_manifest as owner_fate

class ExposureError(ValueError): pass
def require(c: bool, m: str) -> None:
    if not c: raise ExposureError(m)
def contains(q, p): return set(p).issubset(q)
def dominates(a,b): return all(x<=y for x,y in zip(a,b)) and any(x<y for x,y in zip(a,b))
def bins(bundle):
    out=[]
    for name,r in (("edge",1),("pair",2),("triple",3)):
        for e in bundle["coefficient_table"][name]:
            p=(tuple(e["edge"]),) if r==1 else tuple(sorted(tuple(x) for x in e["edges"]))
            out.append((e["child"],p,e["value"]))
    return out
def rationalize(xs, limit=100000):
    fs=[Fraction(float(x)).limit_denominator(limit) for x in xs]
    d=math.lcm(*(x.denominator for x in fs)) if fs else 1
    ns=[x.numerator*(d//x.denominator) for x in fs]
    g=d
    for n in ns: g=math.gcd(g,abs(n))
    return (d//g,[n//g for n in ns]) if g>1 else (d,ns)
def verify_support(t, others, proof):
    w=proof.get("weights")
    require(isinstance(w,list) and len(w)==len(t) and all(type(x)is int and x>0 for x in w),"bad support weights")
    ds=[sum((u[i]-t[i])*w[i] for i in range(len(t))) for u in others]
    require(all(x>=0 for x in ds),"support inequality failed")
    ties=1+sum(x==0 for x in ds); unique=int(all(x>0 for x in ds))
    require(proof.get("minimum_ties")==ties and proof.get("unique")==unique,"support claims failed")
    return ties,unique
def support(t, others):
    if not others: return {"weights":[1]*len(t),"minimum_ties":1,"unique":1}
    A=[[t[i]-u[i] for i in range(len(t))] for u in others]
    r=linprog([1]*len(t),A_ub=A,b_ub=[0]*len(A),bounds=[(1,None)]*len(t),method="highs")
    if not r.success: return None
    _,w=rationalize(list(r.x)); proof={"weights":w,"minimum_ties":0,"unique":0}
    try:
        ds=[sum((u[i]-t[i])*w[i] for i in range(len(t))) for u in others]
        proof.update(minimum_ties=1+sum(x==0 for x in ds),unique=int(all(x>0 for x in ds)))
        verify_support(t,others,proof); return proof
    except ExposureError: return None
def verify_obstruction(t, others, proof):
    d=proof.get("coefficient_denominator"); ns=proof.get("coefficient_numerators")
    require(type(d)is int and d>0 and isinstance(ns,list) and len(ns)==len(others),"bad obstruction coefficients")
    require(all(type(x)is int and x>=0 for x in ns) and sum(ns)==d,"obstruction simplex failed")
    mix=[sum(ns[j]*others[j][i] for j in range(len(others))) for i in range(len(t))]
    sl=[d*t[i]-mix[i] for i in range(len(t))]
    require(all(x>=0 for x in sl) and any(x>0 for x in sl),"obstruction dominance failed")
    require(proof.get("coordinate_slacks")==sl,"obstruction slacks failed")
def obstruction(t, others):
    require(others,"no competitors")
    m=len(others); d=len(t)
    A=[[others[j][i] for j in range(m)]+[1] for i in range(d)]
    r=linprog([0]*m+[-1],A_ub=A,b_ub=list(t),A_eq=[[1]*m+[0]],b_eq=[1],bounds=[(0,None)]*(m+1),method="highs")
    require(r.success and r.x[-1]>1e-9,"no support or obstruction")
    den,ns=rationalize(list(r.x[:-1]),10**7)
    mix=[sum(ns[j]*others[j][i] for j in range(m)) for i in range(d)]
    proof={"coefficient_denominator":den,"coefficient_numerators":ns,"coordinate_slacks":[den*t[i]-mix[i] for i in range(d)]}
    verify_obstruction(t,others,proof); return proof
def exact(bundle):
    s=assignment.validate_bundle(bundle); src=bundle["source_manifest"]
    qs=owner_fate.perfect_matchings(src["side"],{tuple(x) for x in src["allowed_edges"]})
    require(len(qs)==s["responses"],"denominator mismatch")
    children=sorted(x["id"] for x in src["states"]); require(len(children)==len(set(children)),"duplicate child")
    bs=bins(bundle); by={}; rr=[]
    for q in qs:
        v={c:0 for c in children}
        for c,p,n in bs:
            if contains(q,p): v[c]+=n
        x=tuple(v[c] for c in children); rendered=[list(e) for e in q]
        by.setdefault(x,[]).append(rendered); rr.append({"response":rendered,"child_vector":list(x),"coordinate_sum":sum(x)})
    vectors=sorted(by); pareto=[v for v in vectors if not any(dominates(u,v) for u in vectors)]
    cls=[]; supported=unique=tied=unsupported=max_ties=0
    for t in pareto:
        others=[u for u in vectors if u!=t]; p=support(t,others)
        if p is not None:
            ties,un=verify_support(t,others,p); supported+=1; unique+=un; tied+=1-un; max_ties=max(max_ties,ties); kind="positive-weight-supported"
        else:
            p=obstruction(t,others); unsupported+=1; kind="convexly-unsupported"
        cls.append({"child_vector":list(t),"responses":sorted(by[t]),"classification":kind,"certificate":p})
    vrec=[{"child_vector":list(v),"responses":sorted(by[v]),"pareto":int(v in set(pareto))} for v in vectors]
    claims={"responses":len(qs),"children":len(children),"unique_vectors":len(vectors),"pareto_vectors":len(pareto),"dominated_vectors":len(vectors)-len(pareto),"duplicate_responses":len(qs)-len(vectors),"positive_weight_supported":supported,"unique_positive_weight_supported":unique,"tied_positive_weight_supported":tied,"convexly_unsupported":unsupported,"maximum_supported_ties":max_ties,"response_vectors_sha256":assignment.canonical_digest(rr),"vector_records_sha256":assignment.canonical_digest(vrec),"classifications_sha256":assignment.canonical_digest(cls)}
    return {"children":children,"response_vectors":rr,"vector_records":vrec,"pareto_classifications":cls,"claims":claims}
def build_certificate(bundle):
    c={"version":1,"geometric_bundle":bundle}; c.update(exact(bundle)); c["certificate_sha256"]=assignment.canonical_digest(c); return c
def validate_certificate(c):
    require(isinstance(c,dict) and c.get("version")==1,"bad certificate")
    e=exact(c.get("geometric_bundle"))
    for k in ("children","response_vectors","vector_records","pareto_classifications","claims"): require(c.get(k)==e[k],f"{k} mismatch")
    p={k:v for k,v in c.items() if k!="certificate_sha256"}; require(c.get("certificate_sha256")==assignment.canonical_digest(p),"digest")
    x=e["claims"]; return {"responses":x["responses"],"vectors":x["unique_vectors"],"pareto":x["pareto_vectors"],"supported":x["positive_weight_supported"],"unique":x["unique_positive_weight_supported"],"tied":x["tied_positive_weight_supported"],"unsupported":x["convexly_unsupported"],"duplicates":x["duplicate_responses"]}
def random_bundle(r):
    side=r.randint(3,5); p=list(range(side)); r.shuffle(p); allowed={(i,p[i]) for i in range(side)}
    for i in range(side):
        for j in range(side):
            if r.random()<.56: allowed.add((i,j))
    grid={(i,j) for i in range(side) for j in range(side)}; B=[]; target=r.randint(3,7)
    while len(B)<target:
        q=(r.randint(-3,side+2),r.randint(-3,side+2))
        if q not in grid and q not in B: B.append(q)
    return assignment.build_bundle(owner_fate.make_manifest(side,allowed,B,r))
def regressions():
    require(support((2,2),[(0,3),(3,0)]) is None,"unsupported regression")
    verify_obstruction((2,2),[(0,3),(3,0)],obstruction((2,2),[(0,3),(3,0)]))
    p=support((1,1),[(0,2),(2,0)]); require(p is not None and verify_support((1,1),[(0,2),(2,0)],p)==(3,0),"tie regression")
    p=support((0,0),[(1,0),(0,1)]); require(p is not None and verify_support((0,0),[(1,0),(0,1)],p)==(1,1),"unique regression")
def random_tests():
    r=Random(2102); totals=Counter(); dist=Counter()
    for _ in range(120):
        x=validate_certificate(build_certificate(random_bundle(r))); totals.update(x); dist[x["unsupported"]]+=1
    return totals,dist
def mutations():
    r=Random(127); c=build_certificate(random_bundle(r)); bad=[]
    def add(f): x=copy.deepcopy(c); f(x); bad.append(x)
    add(lambda x:x.update(certificate_sha256="0"*64)); add(lambda x:x.update(version=2)); add(lambda x:x["children"].reverse()); add(lambda x:x["response_vectors"][0]["child_vector"].append(9)); add(lambda x:x["vector_records"].pop()); add(lambda x:x["pareto_classifications"][0]["certificate"].update(weights=[0])); add(lambda x:x["claims"].update(pareto_vectors=999)); add(lambda x:x["geometric_bundle"].update(denominator=999)); add(lambda x:x["claims"].update(convexly_unsupported=-1)); add(lambda x:x["response_vectors"].reverse()); add(lambda x:x["pareto_classifications"][0].update(classification="bad")); add(lambda x:x.update(certificate_sha256="f"*64))
    n=0
    for x in bad:
        try: validate_certificate(x)
        except (ExposureError,assignment.BundleError,owner_fate.FateError): n+=1
    require(n==len(bad),"mutation accepted"); return n
def main():
    if len(sys.argv)==2:
        c=json.loads(Path(sys.argv[1]).read_text()); print(validate_certificate(c)); return
    require(len(sys.argv)==1,"usage: check_prime_power_labelled_weight_exposure.py [certificate.json]")
    totals,dist=random_tests(); regressions(); rejected=mutations()
    print(f"verified labelled weight exposure: 120 systems, {totals['responses']} responses, {totals['vectors']} unique vectors, {totals['pareto']} Pareto vectors, {totals['supported']} supported ({totals['unique']} unique and {totals['tied']} tied), {totals['unsupported']} unsupported, {totals['duplicates']} duplicates, unsupported distribution {sorted(dist.items())}, three exact vector regressions, and {rejected} corruptions rejected")
if __name__=="__main__": main()
