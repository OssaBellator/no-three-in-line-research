#!/usr/bin/env python3
"""Deterministic replay audit for BDA5gl--BDA5gp."""
from collections import Counter
from random import Random

FAULTS=("source_less","split","reuse","hidden_deposit","class_mismatch")
SEED,SYSTEMS=2701,2700
EXPECTED={"systems":2700,"initial":20056,"events":53143,"deposits":18530,"transitions":8282,"selected":26042,"class_checks":266235,"invalid":1526,"valid":1174}
EXPECTED_FAULTS={"source_less":301,"class_mismatch":324,"hidden_deposit":289,"split":312,"reuse":300}

def system(rng,sid):
    k=rng.randint(3,7); initial=[]; live={}; events=[]; nxt=0
    for c in range(k):
        for _ in range(rng.randint(0,3)):
            t=f"s{sid}_{nxt}"; nxt+=1; initial.append((t,c)); live[t]=c
    for _ in range(rng.randint(4,9)):
        for _ in range(rng.randint(0,2)):
            t=f"s{sid}_{nxt}"; nxt+=1; c=rng.randrange(k); events.append(("deposit",t,c,0)); live[t]=c
        if live and rng.random()<.45:
            old=rng.choice(sorted(live)); c=live.pop(old); new=f"s{sid}_{nxt}"; nxt+=1; events.append(("transition",old,new,c)); live[new]=c
        for t in rng.sample(sorted(live),min(len(live),rng.randint(0,3))):
            c=live.pop(t); events.append(("debit",t,c,0))
    fault=None
    if rng.random()<.55:
        fault=rng.choice(FAULTS)
        if fault=="source_less": events.append(("debit",f"ghost{sid}",rng.randrange(k),0))
        elif fault=="split":
            t=f"s{sid}_{nxt}"; nxt+=1; c=rng.randrange(k); events.append(("deposit",t,c,0)); a=f"s{sid}_{nxt}"; nxt+=1; b=f"s{sid}_{nxt}"; nxt+=1; events += [("transition",t,a,c),("transition",t,b,c)]
        elif fault=="reuse":
            t=f"s{sid}_{nxt}"; nxt+=1; c=rng.randrange(k); events += [("deposit",t,c,0),("debit",t,c,0),("debit",t,c,0)]
        elif fault=="hidden_deposit":
            t=f"s{sid}_{nxt}"; c=rng.randrange(k); events += [("hidden",t,c,0),("debit",t,c,0)]
        else:
            t=f"s{sid}_{nxt}"; c=rng.randrange(k); events += [("deposit",t,c,0),("debit",t,(c+1)%k,0)]
    return k,initial,events,fault

def replay(k,initial,events):
    live=dict(initial); pred=set(); used=set(); ini=Counter(c for _,c in initial); dep=Counter(); out=Counter()
    for e in events:
        kind=e[0]
        if kind=="deposit":
            _,t,c,_=e
            if t in live or t in used:return "hidden_deposit"
            live[t]=c; dep[c]+=1
        elif kind=="hidden": _,t,c,_=e; live[t]=c
        elif kind=="transition":
            _,old,new,c=e
            if old in pred:return "split"
            if old not in live:return "source_less"
            if live[old]!=c:return "class_mismatch"
            pred.add(old); del live[old]
            if new in live or new in used:return "hidden_deposit"
            live[new]=c
        else:
            _,t,c,_=e
            if t in used:return "reuse"
            if t not in live:return "source_less"
            if live[t]!=c:return "class_mismatch"
            del live[t]; used.add(t); out[c]+=1
        now=Counter(live.values())
        if any(now[c]+out[c]!=ini[c]+dep[c] for c in range(k)):return "hidden_deposit"
    return None

def main():
    rng=Random(SEED); totals=Counter(); faults=Counter()
    for sid in range(SYSTEMS):
        k,initial,events,injected=system(rng,sid); observed=replay(k,initial,events); assert observed==injected
        totals.update(systems=1,initial=len(initial),events=len(events)); totals["deposits"]+=sum(e[0]=="deposit" for e in events); totals["transitions"]+=sum(e[0]=="transition" for e in events); totals["selected"]+=sum(e[0]=="debit" for e in events); totals["class_checks"]+=len(events)*k; totals["valid" if observed is None else "invalid"]+=1
        if observed:faults[observed]+=1
    assert dict(totals)==EXPECTED and dict(faults)==EXPECTED_FAULTS
    print("BDA repair-potential audit:",dict(totals)); print("first failures:",dict(faults))

if __name__=="__main__":main()
