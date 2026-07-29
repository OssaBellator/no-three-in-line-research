#!/usr/bin/env python3
from collections import defaultdict, deque
import random

class Dinic:
    def __init__(self,n): self.g=[[] for _ in range(n)]
    def add(self,u,v,c):
        a=[v,c,None]; b=[u,0,a]; a[2]=b; self.g[u].append(a); self.g[v].append(b)
    def flow(self,s,t):
        ans=0
        while True:
            lv=[-1]*len(self.g); lv[s]=0; q=deque([s])
            while q:
                u=q.popleft()
                for e in self.g[u]:
                    if e[1] and lv[e[0]]<0: lv[e[0]]=lv[u]+1; q.append(e[0])
            if lv[t]<0: return ans
            it=[0]*len(self.g)
            def dfs(u,f):
                if u==t: return f
                while it[u]<len(self.g[u]):
                    e=self.g[u][it[u]]
                    if e[1] and lv[e[0]]==lv[u]+1:
                        z=dfs(e[0],min(f,e[1]))
                        if z: e[1]-=z; e[2][1]+=z; return z
                    it[u]+=1
                return 0
            while True:
                z=dfs(s,10**9)
                if not z: break
                ans+=z

def flow(dem,cap,E):
    nl,nr=len(dem),len(cap); s=nl+nr; t=s+1; D=Dinic(t+1)
    for i,x in enumerate(dem): D.add(s,i,x)
    for i,j in E: D.add(i,nl+j,sum(dem)+1)
    for j,x in enumerate(cap): D.add(nl+j,t,x)
    return D.flow(s,t)

def hall(dem,cap,E):
    N=[set() for _ in dem]
    for i,j in E: N[i].add(j)
    best=0
    for mask in range(1<<len(dem)):
        d=0; ns=set()
        for i,x in enumerate(dem):
            if mask>>i&1: d+=x; ns|=N[i]
        best=max(best,d-sum(cap[j] for j in ns))
    return max(0,best)

rng=random.Random(20260730); S=defaultdict(int)
for _ in range(5000):
    no,ns=rng.randint(1,5),rng.randint(1,6)
    labels=[(o,t) for o in range(no) for t in range(2)]
    dem=[rng.randint(0,4) for _ in labels]; cap=[rng.randint(0,6) for _ in range(ns)]
    E={(i,s) for i,(_,t) in enumerate(labels) for s in range(ns) if rng.random()<(.55 if t==0 else .45)}
    f=flow(dem,cap,E); deficit=hall(dem,cap,E)
    assert sum(dem)-f==deficit
    d0=[dem[i] if labels[i][1]==0 else 0 for i in range(len(dem))]
    d1=[dem[i] if labels[i][1]==1 else 0 for i in range(len(dem))]
    if flow(d0,cap,E)+flow(d1,cap,E)>f: S['double_spend_witnesses']+=1
    S['systems']+=1; S['owners']+=no; S['sources']+=ns; S['demand_nodes']+=len(dem); S['arcs']+=len(E)
    S['demand_units']+=sum(dem); S['paid_units']+=f; S['subset_checks']+=1<<len(dem)
    if deficit: S['deficient_systems']+=1; S['deficient_units']+=deficit
    else: S['fully_paid']+=1
print(dict(S))
