#!/usr/bin/env python3
from __future__ import annotations
import hashlib, itertools, json
from collections import deque
from typing import Any

EXPECTED_CONTRACT_SHA256 = "b97b2553cf5548cfc32a022172d2e011bc60952021d87178ae0e0fdc673ecc23"

class CheckError(ValueError): pass

def require(ok: bool, msg: str) -> None:
    if not ok: raise CheckError(msg)

def digest(v: Any) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode()).hexdigest()

def edges_for_perm(p): return frozenset((i,p[i]) for i in range(len(p)))
def all_matchings(n, host):
    return [tuple(p) for p in itertools.permutations(range(n)) if edges_for_perm(p) <= host]
def cost(p, marked): return sum((i,p[i]) in marked for i in range(len(p)))
def sccs(n, arcs):
    adj=[[] for _ in range(n)]; radj=[[] for _ in range(n)]
    for a,b in arcs: adj[a].append(b); radj[b].append(a)
    seen=[False]*n; order=[]
    def dfs(v):
        seen[v]=True
        for w in adj[v]:
            if not seen[w]: dfs(w)
        order.append(v)
    for v in range(n):
        if not seen[v]: dfs(v)
    comp=[-1]*n; comps=[]
    def rdfs(v,c):
        comp[v]=c; comps[c].append(v)
        for w in radj[v]:
            if comp[w]<0: rdfs(w,c)
    for v in reversed(order):
        if comp[v]<0:
            comps.append([]); rdfs(v,len(comps)-1)
    return comp, comps

def shortest_path(n, arcs, start, goal):
    adj=[[] for _ in range(n)]
    for a,b in sorted(arcs): adj[a].append(b)
    q=deque([start]); prev={start:None}
    while q:
        v=q.popleft()
        if v==goal: break
        for w in adj[v]:
            if w not in prev: prev[w]=v; q.append(w)
    require(goal in prev, "return path missing")
    path=[]; v=goal
    while v is not None: path.append(v); v=prev[v]
    return list(reversed(path))

def bellman_potential(n, weighted):
    d=[0]*n
    for _ in range(n-1):
        changed=False
        for a,b,w in weighted:
            if d[b] > d[a]+w:
                d[b]=d[a]+w; changed=True
        if not changed: break
    for a,b,w in weighted: require(d[b] <= d[a]+w, "negative cycle")
    return d

def optimal_face(n, host, marked):
    pms=all_matchings(n,host); require(pms,"no matching")
    k=min(cost(p,marked) for p in pms)
    opts=sorted(p for p in pms if cost(p,marked)==k)
    base=opts[0]; inv={base[i]:i for i in range(n)}
    weighted=[]
    for i,t in sorted(host):
        j=inv[t]
        if i==j: continue
        weighted.append((i,j,int((i,t) in marked)-int((j,base[j]) in marked)))
    phi=bellman_potential(n,weighted)
    tight=set(edges_for_perm(base)); tight_arcs=set()
    for i,j,w in weighted:
        if w+phi[i]-phi[j]==0:
            tight.add((i,base[j])); tight_arcs.add((i,j))
    tight_pms=sorted(all_matchings(n,frozenset(tight)))
    require(tight_pms==opts,"tight family mismatch")
    comp, comps=sccs(n,tight_arcs)
    allowed=set(edges_for_perm(base))
    for i,j in tight_arcs:
        if comp[i]==comp[j]: allowed.add((i,base[j]))
    allowed_pms=sorted(all_matchings(n,frozenset(allowed)))
    require(allowed_pms==opts,"allowed core mismatch")
    return k,base,inv,phi,frozenset(allowed),opts

def local_matchings(sources, targets, edges):
    sources=tuple(sorted(sources)); targets=tuple(sorted(targets))
    out=[]
    for perm in itertools.permutations(targets):
        m=tuple(zip(sources,perm))
        if all(e in edges for e in m): out.append(m)
    return sorted(out)

def cartesian_local(level_parts):
    states=[tuple()]
    for part in level_parts:
        states=[tuple(sorted(a+b)) for a in states for b in part]
    return sorted(states)

def analyse_pair(n, host, marked, selected_edge):
    k,base,inv,phi,allowed,opts=optimal_face(n,host,marked)
    require(k>=1,"rollback cost unexpectedly zero")
    skeleton_groups={}
    all_cross=0
    for p in opts:
        sigma={i:inv[p[i]] for i in range(n)}
        levels=range(min(phi),max(phi))
        up=down=0
        for r in levels:
            U=sum(phi[i]==r and phi[sigma[i]]==r+1 for i in range(n))
            D=sum(phi[i]==r+1 and phi[sigma[i]]==r for i in range(n))
            require(U==D,"cut imbalance")
            up+=U; down+=D
        require(up==down and up<=k,"cross-level stock")
        sk=tuple(sorted((i,sigma[i]) for i in range(n) if phi[i]!=phi[sigma[i]]))
        require(len(sk)<=2*k and len(sk)%2==0,"skeleton bound")
        all_cross += len(sk)
        for i,j in sk:
            delta=phi[j]-phi[i]
            require(abs(delta)==1,"nonadjacent tight move")
            ec=int((i,base[j]) in marked); bc=int((j,base[j]) in marked)
            require(delta==ec-bc,"level equation")
        for s in sorted(set(phi)):
            O={i for i,j in sk if phi[i]==s}
            I={j for i,j in sk if phi[j]==s}
            require(len(O)==len(I),"level residual imbalance")
            same={(i,inv[p[i]]) for i in range(n) if phi[i]==s and phi[inv[p[i]]]==s}
            require({i for i,j in same}=={i for i in range(n) if phi[i]==s}-O,"residual sources")
            require({j for i,j in same}=={j for j in range(n) if phi[j]==s}-I,"residual targets")
        skeleton_groups.setdefault(sk,[]).append(p)
    local_hosts=0; mixed_hosts=0; separated_hosts=0; boundary_arcs=0; witness_cycles=0
    sparse_tail_deletions=0; batch_flips=0; concentration_hosts=0
    for sk, group in skeleton_groups.items():
        used_s={i for i,j in sk}; used_t={j for i,j in sk}
        level_parts=[]
        for s in sorted(set(phi)):
            S={i for i in range(n) if phi[i]==s and i not in used_s}
            T={j for j in range(n) if phi[j]==s and j not in used_t}
            E={(i,j) for i in S for j in T if (i,base[j]) in allowed}
            pms=local_matchings(S,T,E)
            require(pms,"empty residual level")
            level_parts.append(pms)
            local_hosts += 1
            beta={j:int((j,base[j]) in marked) for j in T}
            for i,j in E: require(int((i,base[j]) in marked)==beta[j],"right polarization")
            split_groups={}
            R1={j for j in T if beta[j]}
            for pm in pms:
                X=frozenset(i for i,j in pm if j in R1)
                split_groups.setdefault(X,[]).append(pm)
            for X, states in split_groups.items():
                a=local_matchings(X,R1,E)
                b=local_matchings(S-set(X),T-R1,E)
                prod=sorted(tuple(sorted(x+y)) for x in a for y in b)
                require(prod==states,"source split product mismatch")
            P=pms[0]; srcs=tuple(sorted(S)); pos={src:i for i,src in enumerate(srcs)}
            target_at={src:t for src,t in P}; target_pos={t:pos[src] for src,t in P}
            arcs=set()
            for i,j in E:
                a=pos[i]; b=target_pos[j]
                if a!=b: arcs.add((a,b))
            colors={pos[src]:beta[target_at[src]] for src in srcs}
            comp, comps=sccs(len(srcs),arcs)
            mixed=any(len({colors[v] for v in C})>1 for C in comps)
            unique_split=len(split_groups)==1
            require(unique_split == (not mixed),"mixed-cycle criterion")
            if mixed: mixed_hosts+=1
            else: separated_hosts+=1
            B=sorted((a,b) for a,b in arcs if colors[a]!=colors[b] and comp[a]==comp[b])
            require((len(B)>0)==mixed,"boundary criterion")
            boundary_arcs += len(B)
            cycles=[]
            for a,b in B:
                path=shortest_path(len(srcs),arcs,b,a)
                cyc=tuple([a]+path[:-1])
                require(len(set(cyc))==len(cyc),"cycle not simple")
                require(len({colors[v] for v in cyc})>1,"cycle not mixed")
                cycles.append(cyc); witness_cycles+=1
            mu={v:sum(v in cyc for cyc in cycles) for v in range(len(srcs))}
            if cycles and max(mu.values(),default=0)>=3:
                concentration_hosts += 1
            else:
                chosen=[]; used=set()
                for cyc in cycles:
                    if not used.intersection(cyc): chosen.append(cyc); used.update(cyc)
                bound=(len(B)+2*len(srcs)-1)//(2*len(srcs)) if len(srcs) else 0
                require(len(chosen)>=bound,"packing bound")
                if chosen:
                    seen=set(); seenX=set()
                    for mask in range(1<<len(chosen)):
                        mapping={pos[src]:target_pos[t] for src,t in P}
                        for q,cyc in enumerate(chosen):
                            if mask>>q & 1:
                                for idx,v in enumerate(cyc): mapping[v]=cyc[(idx+1)%len(cyc)]
                        state=tuple(sorted((srcs[v], target_at[srcs[mapping[v]]]) for v in mapping))
                        require(all(e in E for e in state),"flipped edge absent")
                        seen.add(state)
                        seenX.add(frozenset(i for i,j in state if j in R1))
                    require(len(seen)==1<<len(chosen),"batch states not distinct")
                    require(len(seenX)==1<<len(chosen),"batch splits not distinct")
                    batch_flips += len(chosen)
            Z={a for a,b in B}
            if Z:
                keep=[v for v in range(len(srcs)) if v not in Z]
                remap={v:i for i,v in enumerate(keep)}
                rarcs={(remap[a],remap[b]) for a,b in arcs if a in remap and b in remap}
                rcomp,rcomps=sccs(len(keep),rarcs)
                for C in rcomps:
                    require(len({colors[keep[v]] for v in C})<=1,"mixed cycle survived tail deletion")
                sparse_tail_deletions += len(Z)
        sk_edges=tuple(sk)
        prod=cartesian_local(level_parts)
        rec=sorted(tuple(base[j] for i,j in sorted(sk_edges+state)) for state in prod)
        require(rec==sorted(group),"conditional level product mismatch")
    return {
        "minimum_cost":k,"optimum_states":len(opts),"skeletons":len(skeleton_groups),
        "cross_level_edge_incidences":all_cross,"local_level_hosts":local_hosts,
        "mixed_level_hosts":mixed_hosts,"colour_separated_hosts":separated_hosts,
        "boundary_arcs":boundary_arcs,"witness_cycles":witness_cycles,
        "sparse_tail_deletions":sparse_tail_deletions,"batch_cycle_count":batch_flips,
        "concentration_hosts":concentration_hosts,
    }

def validate_record(record):
    require(record["contract_sha256"]==EXPECTED_CONTRACT_SHA256,"contract")
    require(record["record_sha256"]==digest({k:v for k,v in record.items() if k!="record_sha256"}),"seal")
    require(record["matchable_final_hosts"]==247,"host census")
    require(record["essential_rollback_pairs"]==513,"pair census")
    for key in ("optimum_states","skeletons","local_level_hosts","colour_separated_hosts","mixed_level_hosts","boundary_arcs","witness_cycles","sparse_tail_deletions","batch_cycle_count","concentration_hosts"):
        require(isinstance(record[key],int) and record[key]>=0,f"{key}: nonnegative integer")
    require(record["optimum_states"]>=record["essential_rollback_pairs"],"optimum incidence")
    require(record["witness_cycles"]==record["boundary_arcs"],"witness indexing")
    require(record["mixed_level_hosts"]>0 and record["colour_separated_hosts"]>0,"both colour endpoints")
    require(record["batch_cycle_count"]>0 and record["concentration_hosts"]>0,"both packing endpoints")
    require(record["rollback_level_skeleton_ancestry_proved"]==1,"level flag")
    require(record["same_level_colour_split_ancestry_proved"]==1,"colour flag")
    require(record["mixed_cycle_packing_ancestry_proved"]==1,"cycle flag")
    require(record["global_transition_kind_bank_exhaustive"]==0,"global exhaustiveness honesty")
    require(record["global_termination_proved"]==0,"termination honesty")
    require(record["actual_global_parent_rule_complete"]==0,"parent-rule honesty")
    require(record["all_n_proved_by_checker"]==0,"all-n honesty")

def main():
    n=3; full=frozenset(itertools.product(range(n),repeat=2))
    hosts=0; pairs=0; totals={k:0 for k in ["optimum_states","skeletons","cross_level_edge_incidences","local_level_hosts","mixed_level_hosts","colour_separated_hosts","boundary_arcs","witness_cycles","sparse_tail_deletions","batch_cycle_count","concentration_hosts"]}
    for mask in range(1,1<<(n*n)):
        host=frozenset(e for idx,e in enumerate(sorted(full)) if mask>>idx&1)
        pms=all_matchings(n,host)
        if not pms: continue
        hosts+=1
        essential=[e for e in host if not all_matchings(n,host-{e})]
        for e in essential:
            marked=full-host
            if not all_matchings(n,full-{e}): continue
            report=analyse_pair(n,full-{e},marked,e)
            if report["minimum_cost"]<1: continue
            pairs+=1
            for k in totals: totals[k]+=report[k]
    require(pairs==513,"unexpected pair census")
    claims={
        "checker":"prime-power-rollback-level-colour-cycle-ancestry",
        "contract_sha256":EXPECTED_CONTRACT_SHA256,
        "matchable_final_hosts":hosts,
        "essential_rollback_pairs":pairs,
        **totals,
        "corruption_rejections":8,
        "rollback_level_skeleton_ancestry_proved":1,
        "same_level_colour_split_ancestry_proved":1,
        "mixed_cycle_packing_ancestry_proved":1,
        "global_transition_kind_bank_exhaustive":0,
        "global_termination_proved":0,
        "actual_global_parent_rule_complete":0,
        "all_n_proved_by_checker":0,
    }
    claims["record_sha256"]=digest(claims)
    validate_record(claims)
    mutations=[
        ("contract_sha256","0"*64),
        ("rollback_level_skeleton_ancestry_proved",0),
        ("all_n_proved_by_checker",1),
        ("essential_rollback_pairs",512),
        ("skeletons",-1),
        ("same_level_colour_split_ancestry_proved",0),
        ("mixed_cycle_packing_ancestry_proved",0),
        ("witness_cycles",claims["witness_cycles"]+1),
    ]
    rejected=0
    for key,val in mutations:
        bad=dict(claims); bad[key]=val
        bad["record_sha256"]=digest({k:v for k,v in bad.items() if k!="record_sha256"})
        try: validate_record(bad)
        except CheckError: rejected+=1
    require(rejected==8,"corruption rejection")
    print(json.dumps(claims,sort_keys=True))
if __name__=="__main__": main()
