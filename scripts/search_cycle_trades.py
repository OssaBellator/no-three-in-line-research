#!/usr/bin/env python3
"""Extract real cross-channel syndrome cycles and score cyclic matching states."""
from __future__ import annotations
import argparse
from collections import defaultdict, deque
from itertools import combinations
from math import gcd


def inv(x, p):
    return pow(x, p-2, p)


def point(c, x, p):
    return (x, (c*inv(x, p)) % p)


def collinear(P, Q, R):
    return (Q[0]-P[0])*(R[1]-P[1]) == (Q[1]-P[1])*(R[0]-P[0])


def line_key(a, b):
    x1,y1=a; x2,y2=b
    A=y2-y1; B=x1-x2; C=A*x1+B*y1
    g=gcd(gcd(abs(A),abs(B)),abs(C))
    if g: A//=g; B//=g; C//=g
    if A<0 or (A==0 and B<0): A,B,C=-A,-B,-C
    return A,B,C


def syndrome_graph(p, a, b):
    red={x: point(a,x,p) for x in range(1,p)}
    blue={z: point(b,z,p) for z in range(1,p)}
    edges=[]
    adj=defaultdict(list)
    for x,u in combinations(range(1,p),2):
        for z in range(1,p):
            if collinear(red[x],red[u],blue[z]):
                idx=len(edges); edges.append((x,u,z))
                adj[x].append(idx); adj[u].append(idx)
    return red, blue, edges, adj


def peel_core(edges, adj):
    active_v=set(adj)
    active_e=set(range(len(edges)))
    deg={v:len(adj[v]) for v in active_v}
    q=deque(v for v,d in deg.items() if d<=1)
    while q:
        v=q.popleft()
        if v not in active_v or deg[v]>1: continue
        active_v.remove(v)
        for ei in adj[v]:
            if ei not in active_e: continue
            active_e.remove(ei)
            x,u,_=edges[ei]
            w=u if x==v else x
            if w in active_v:
                deg[w]-=1
                if deg[w]<=1: q.append(w)
    return active_v, active_e


def find_cycle(edges, adj, active_v, active_e):
    parent={}; parent_e={}; seen=set()
    def dfs(v, pv=None):
        seen.add(v)
        for ei in adj[v]:
            if ei not in active_e: continue
            x,u,z=edges[ei]; w=u if x==v else x
            if w==pv: continue
            if w not in seen:
                parent[w]=v; parent_e[w]=ei
                found=dfs(w,v)
                if found: return found
            else:
                path_v=[v]; path_e=[]; cur=v
                while cur!=w and cur in parent:
                    path_e.append(parent_e[cur]); cur=parent[cur]; path_v.append(cur)
                if cur==w:
                    return path_v, path_e+[ei]
        return None
    for v in active_v:
        if v not in seen:
            found=dfs(v)
            if found: return found
    return None


def triple_potential(points):
    lines=defaultdict(set)
    for P,Q in combinations(points,2):
        k=line_key(P,Q); lines[k].add(P); lines[k].add(Q)
    return sum(len(s)*(len(s)-1)*(len(s)-2)//6 for s in lines.values())


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--prime',type=int,default=17)
    ap.add_argument('--a',type=int,default=1)
    ap.add_argument('--b',type=int,default=3)
    args=ap.parse_args(); p,a,b=args.prime,args.a,args.b
    red,blue,edges,adj=syndrome_graph(p,a,b)
    V,E=peel_core(edges,adj)
    cyc=find_cycle(edges,adj,V,E)
    print(f'p={p}, cross triples={len(edges)}, core vertices={len(V)}, core edges={len(E)}')
    if not cyc:
        print('no cycle core')
        return
    verts,_=cyc
    # Remove repeated closing artefacts and use unique cyclic order as obtained.
    seen=[]
    for v in verts:
        if v not in seen: seen.append(v)
    xs=seen
    ys=[red[x][1] for x in xs]
    outside=[red[x] for x in range(1,p) if x not in set(xs)] + list(blue.values())
    scores=[]
    for s in range(len(xs)):
        state=[(xs[i],ys[(i+s)%len(xs)]) for i in range(len(xs))]
        scores.append(triple_potential(outside+state))
    print(f'cycle length={len(xs)}; state potentials={scores}; best shift={min(range(len(scores)), key=scores.__getitem__)}')


if __name__=='__main__':
    main()
