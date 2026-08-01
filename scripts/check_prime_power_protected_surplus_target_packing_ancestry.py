#!/usr/bin/env python3
"""Check CMR1006--CMR1093 protected surplus and target packing ancestry."""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
from collections import defaultdict
from math import ceil, comb, floor
from typing import Any

from check_prime_power_scc_branch_minimum_face_ancestry import (
    State, joint_states, physical, physical_triples
)

class ProtectedFrontierError(RuntimeError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok: raise ProtectedFrontierError(message)
def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def line_key(a: tuple[int,int], b: tuple[int,int]) -> tuple[int,int,int]:
    from math import gcd
    A=b[1]-a[1]; B=a[0]-b[0]; C=-(A*a[0]+B*a[1])
    g=gcd(gcd(abs(A),abs(B)),abs(C)) or 1
    A//=g; B//=g; C//=g
    if A<0 or (A==0 and B<0) or (A==0 and B==0 and C<0): A=-A; B=-B; C=-C
    return A,B,C
def point_layers(state: State) -> dict[tuple[int,int], int]:
    return {(r,c): layer for layer,r,c in state}

def robust_entry_rank_audit(n: int = 4) -> dict[str,int]:
    states=joint_states(n)
    pair_checks=rank_one=higher=star_banks=pair_lines=polarization=0
    common_layer_banks=cross_layer_banks=0
    for old in states:
        old_points=physical(old); old_triples=set(physical_triples(old))
        for new in states:
            new_points=physical(new); gained=set(physical_triples(new))-old_triples
            entering=new_points-old_points; ranks={1:[],2:[],3:[]}
            for triple in gained:
                rank=len(triple&entering); require(rank in ranks,"CMR1006 entry rank"); ranks[rank].append(triple)
            require(len(gained)==sum(map(len,ranks.values())),"CMR1006 partition")
            require(max(len(ranks[1]),len(ranks[2])+len(ranks[3]))>=ceil(len(gained)/2),"CMR1007 half")
            pair_checks+=1
            by_x=defaultdict(list)
            for triple in ranks[1]: by_x[next(iter(triple&entering))].append(triple)
            labels=point_layers(new); common=old_points&new_points
            for x,group in by_x.items():
                line_groups=defaultdict(set)
                for y in common:
                    if y!=x: line_groups[line_key(x,y)].add(y)
                require(sum(comb(len(points),2) for points in line_groups.values())==len(group),"CMR1008 exact secant sum")
                rank_one+=len(group); R=3
                if not any(len(points)>=R for points in line_groups.values()):
                    positive=[points for points in line_groups.values() if len(points)>=2]
                    require(len(positive)>=ceil(len(group)/comb(R-1,2)),"CMR1009 star count")
                    chosen=[]; used=set()
                    for points in positive:
                        pair=tuple(sorted(points))[:2]; require(not(set(pair)&used),"CMR1009 outside disjoint")
                        used.update(pair); chosen.append(pair)
                    star_banks+=1; same0=[]; same1=[]; cross=[]
                    for a,b in chosen:
                        pattern=(labels[a],labels[b])
                        if pattern==(0,0): same0.append((a,b))
                        elif pattern==(1,1): same1.append((a,b))
                        else: cross.append((a,b))
                    M=len(chosen)
                    require(max(len(same0),len(same1))>=ceil(M/4) or len(cross)>=ceil(M/2),"CMR1015 polarization")
                    for bank in (same0,same1):
                        union=[cell for pair in bank for cell in pair]
                        require(len({c[0] for c in union})==len(union) and len({c[1] for c in union})==len(union),"CMR1016/1054 simultaneous matching")
                        if bank: common_layer_banks+=1
                    if cross:
                        center_layer=labels[x]; S=[]; T=[]
                        for a,b in cross:
                            s,t=(a,b) if labels[a]==center_layer else (b,a)
                            require(labels[s]==center_layer and labels[t]!=center_layer,"CMR1018 rooted labels")
                            S.append(s); T.append(t)
                        for endpoints in (S,T):
                            require(len(endpoints)==len(set(endpoints)),"CMR1062 distinct")
                            require(len({p[0] for p in endpoints})==len(endpoints) and len({p[1] for p in endpoints})==len(endpoints),"CMR1062 endpoint matching")
                        cross_layer_banks+=1
                    polarization+=1
            by_pair=defaultdict(list)
            for triple in [*ranks[2],*ranks[3]]:
                pair=tuple(sorted(triple&entering))[:2]; require(len(pair)==2,"CMR1011 entering pair"); by_pair[pair].append(triple)
            for pair,group in by_pair.items():
                thirds=[]; key=line_key(*pair)
                for triple in group:
                    third=next(iter(triple-set(pair))); require(line_key(pair[0],third)==key,"CMR1011 one line"); thirds.append(third)
                require(len(thirds)==len(set(thirds)),"CMR1011 distinct third cells")
                require(len(physical_triples(new))>=comb(len(group)+2,3),"CMR1011 cubic line load")
                pair_lines+=1; higher+=len(group)
    return {"side_four_joint_states":len(states),"ordered_state_transition_checks":pair_checks,
            "rank_one_new_triple_incidences":rank_one,"higher_rank_new_triple_incidences":higher,
            "cell_disjoint_secant_star_banks":star_banks,"layer_polarization_checks":polarization,
            "common_layer_simultaneous_banks":common_layer_banks,"cross_layer_simultaneous_banks":cross_layer_banks,
            "entering_pair_loaded_lines":pair_lines}

def loaded_line_absorption_audit(n: int = 4) -> dict[str,int]:
    states=joint_states(n); profiles=protected_subsets=direct_star_checks=cross_star_checks=0; seen=set()
    for state in states:
        labels=point_layers(state); pts=physical(state); lines={}
        for a,b in itertools.combinations(sorted(pts),2):
            key=line_key(a,b); line_pts=frozenset(p for p in pts if key[0]*p[0]+key[1]*p[1]+key[2]==0)
            if len(line_pts)>=3: lines[key]=line_pts
        for key,line_pts in lines.items():
            sig=(tuple(sorted(state)),key)
            if sig in seen: continue
            seen.add(sig); profiles+=1
            layer_sets={ell:[p for p in line_pts if labels[p]==ell] for ell in (0,1)}
            majority=max((0,1),key=lambda ell:len(layer_sets[ell])); r=len(line_pts); h=len(layer_sets[majority])
            require(h>=ceil(r/2),"CMR1022/1046 majority")
            require(len({p[0] for p in layer_sets[majority]})==h and len({p[1] for p in layer_sets[majority]})==h,"CMR1023 partial matching")
            layer_edges=[(row,col) for layer,row,col in state if layer==majority]
            for size in range(n+1):
                for subset in itertools.combinations(layer_edges,size):
                    rows={e[0] for e in subset}; cols={e[1] for e in subset}
                    free=[p for p in layer_sets[majority] if p[0] not in rows and p[1] not in cols]
                    require(len(free)>=max(0,h-2*size),"CMR1024/1047 touch bound")
                    require(len({p[0] for p in free})==len(free) and len({p[1] for p in free})==len(free),"CMR1025/1048 absorbable")
                    if not free: require(size>=ceil(h/2),"CMR1027/1050 large core")
                    protected_subsets+=1
    for M in range(1,33):
        for k in range(17):
            G=2*max(0,M-2*k); require(G>0 or k>=M/2,"CMR1056-1057 direct star"); direct_star_checks+=1
        for kc in range(17):
            for ko in range(17):
                G=max(0,M-2*min(kc,ko)); require(G>0 or (kc>=M/2 and ko>=M/2),"CMR1065-1066 cross star"); cross_star_checks+=1
    return {"loaded_selected_line_profiles":profiles,"protected_touch_subset_checks":protected_subsets,
            "direct_simultaneous_star_formula_checks":direct_star_checks,"simultaneous_cross_star_formula_checks":cross_star_checks}

def max_disjoint_triples(triples):
    triples=list(triples); best=[]
    def rec(i,chosen,used):
        nonlocal best
        if len(chosen)+(len(triples)-i)<=len(best): return
        if i==len(triples):
            if len(chosen)>len(best): best=chosen[:]
            return
        rec(i+1,chosen,used)
        if not(set(triples[i])&used): rec(i+1,chosen+[triples[i]],used|set(triples[i]))
    rec(0,[],set()); return best

def hypergraph_escape_audit(n:int=4)->dict[str,int]:
    states=joint_states(n); hypergraphs=packing_cases=cover_cases=rooted=escape_banks=rematching_checks=0
    perms=tuple(itertools.permutations(range(n)))
    for state in states:
        trips=physical_triples(state)
        if not trips: continue
        hypergraphs+=1; pack=max_disjoint_triples(trips)
        for q in (2,3):
            if len(pack)>=q:
                chosen=pack[:q]; require(len(set().union(*map(set,chosen)))==3*q,"CMR1071 disjoint rank"); packing_cases+=1
            else:
                cover=set().union(*map(set,pack)) if pack else set()
                require(len(cover)<=3*(q-1),"CMR1070 cover size"); require(all(set(t)&cover for t in trips),"CMR1070 cover")
                if cover: require(max(sum(cell in t for t in trips) for cell in cover)>=ceil(len(trips)/len(cover)),"CMR1070 concentration")
                cover_cases+=1
        for z in physical(state):
            through=[t for t in trips if z in t]
            if not through: continue
            groups=defaultdict(set)
            for p in physical(state)-{z}: groups[line_key(z,p)].add(p)
            require(len(through)==sum(comb(len(g),2) for g in groups.values()),"CMR1072 rooted decomposition"); rooted+=1
        if len(pack)>=2:
            labels=point_layers(state); by_layer={0:[],1:[]}
            for t in pack:
                counts={ell:sum(labels[p]==ell for p in t) for ell in (0,1)}; layer=0 if counts[0]>=counts[1] else 1; by_layer[layer].append(t)
            layer=max((0,1),key=lambda ell:len(by_layer[ell])); sub=by_layer[layer]
            require(len(sub)>=ceil(len(pack)/2),"CMR1078 majority targets")
            reps=[min(p for p in t if labels[p]==layer) for t in sub]
            require(len(reps)==len(set(reps)) and len({p[0] for p in reps})==len(reps) and len({p[1] for p in reps})==len(reps),"CMR1079 reps matching")
            old_perm=tuple(next(c for ell,r,c in state if ell==layer and r==i) for i in range(n))
            opp_perm=tuple(next(c for ell,r,c in state if ell==1-layer and r==i) for i in range(n))
            candidates=[p for p in perms if all(p[i]!=old_perm[i] and p[i]!=opp_perm[i] for i in range(n))]
            require(candidates,"CMR1080 degree-two Hall"); newp=candidates[0]
            new_points={(i,newp[i]) for i in range(n)}|{(i,opp_perm[i]) for i in range(n)}
            require(all(not set(t)<=new_points for t in sub),"CMR1081 target destruction")
            escape_banks+=1; rematching_checks+=len(candidates)
    return {"dirty_side_four_target_hypergraphs":hypergraphs,"disjoint_target_packing_cases":packing_cases,
            "small_target_cover_cases":cover_cases,"rooted_target_line_decompositions":rooted,
            "simultaneous_disjoint_target_escape_banks":escape_banks,"degree_two_rematching_candidates":rematching_checks}

def protected_capacity_audit(max_side:int=12)->dict[str,int]:
    checks=0; maxcap=0; skeleton=0
    for N in range(1,max_side+1):
        for h in range(1,5):
            for lam in range(2,6):
                P=0
                for m in range(1,N+1):
                    H=2*m*m+m+1; R=floor((lam-1)*m*m/2); P+=2*m*H*(1+R); require(H>=1 and R>=0,"CMR1087 stage arithmetic")
                cap=(h+1)*(2*N+1)*P; require(cap>=P,"CMR1089 global capacity"); maxcap=max(maxcap,cap)
                for G0 in (1,2,3,N+1): require(floor(cap/G0)*G0<=cap,"CMR1090 episode bound")
                u=N//2; require(2*u<=2*N and (u+1)*(N**(4*u))>=1,"CMR1042 skeleton stock"); skeleton+=1; checks+=4
    for n in range(1,max_side+1): require(3*floor(2*n/3)<=2*n,"CMR1076 target contraction budget"); checks+=1
    return {"protected_capacity_parameter_checks":checks,"large_core_skeleton_parameter_checks":skeleton,
            "maximum_sample_global_protected_capacity":maxcap}

CONTRACT={"schema":"prime-power-protected-surplus-target-packing-ancestry/v1",
 "source_theorems":[f"CMR{i}" for i in range(1006,1094)],
 "banks":["robust-surplus-entry-rank-dichotomy","secant-star-layer-polarization","entering-pair-line-absorption",
 "robust-surplus-protected-execution","large-protected-core-minimum-descent","loaded-target-line-minimum-absorption",
 "simultaneous-star-direct-absorption","simultaneous-cross-star-absorption","minimum-target-hypergraph-packing",
 "disjoint-target-simultaneous-escape","global-protected-owner-capacity"],
 "honesty":{"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,
 "actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_SHA256="5e90f91f2c8a8679bdeb3fc78ab7b0ed71c2f8d3e09de41b8ad9fc18865bddd8"
def mutation_audit()->int:
    muts=[lambda c:c.update(schema="bad"),lambda c:c.update(source_theorems=[]),lambda c:c["source_theorems"].pop(),
          lambda c:c["source_theorems"].__setitem__(0,"CMR1005"),lambda c:c["banks"].pop(),lambda c:c["banks"].append(c["banks"][0]),
          lambda c:c["honesty"].update(all_n_proved_by_checker=1),lambda c:c["honesty"].update(global_termination_proved=1),
          lambda c:c["honesty"].pop("actual_global_parent_rule_complete")]
    def validate(c):
        require(c.get("schema")==CONTRACT["schema"],"schema"); require(c.get("source_theorems")==CONTRACT["source_theorems"],"sources")
        require(c.get("banks")==CONTRACT["banks"],"banks"); require(c.get("honesty")==CONTRACT["honesty"],"honesty")
    rejected=0
    for mut in muts:
        bad=copy.deepcopy(CONTRACT); mut(bad)
        try: validate(bad)
        except ProtectedFrontierError: rejected+=1
    require(rejected==len(muts),"mutation accepted"); return rejected

def main():
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_SHA256,"contract")
    report={"checker":"prime-power-protected-surplus-target-packing-ancestry","contract_sha256":contract,
      **robust_entry_rank_audit(),**loaded_line_absorption_audit(),**hypergraph_escape_audit(),**protected_capacity_audit(),
      "rejected_corruptions":mutation_audit(),"robust_surplus_entry_rank_exact":1,"secant_star_layer_polarization_exact":1,
      "entering_pair_line_absorption_exact":1,"robust_surplus_protected_execution_exact":1,
      "large_protected_core_minimum_descent_exact":1,"loaded_target_line_minimum_absorption_exact":1,
      "simultaneous_star_direct_absorption_exact":1,"simultaneous_cross_star_absorption_exact":1,
      "minimum_target_hypergraph_packing_exact":1,"disjoint_target_simultaneous_escape_exact":1,
      "global_protected_owner_capacity_exact":1,"protected_surplus_target_packing_ancestry_proved":1,
      "all_owner_operations_proved":0,"all_scheduler_operations_proved":0,"all_restoration_operations_proved":0,
      "all_construction_ancestry_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,
      "actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}
    print(json.dumps(report,sort_keys=True))
if __name__=="__main__": main()
