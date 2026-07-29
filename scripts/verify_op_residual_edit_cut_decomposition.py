TITLE='OP residual-edit cut decomposition audit'
SEED=1805
SYSTEMS=5200
STAGES=1
ORDER=['systems','capacity_classes','terminal_classes','compatibility_arcs','demand_units','paid_units','unpaid_units','deficient_systems','outside_terminal_classes','type0_outside_units','type1_outside_units','stage0_cut_units']

from collections import deque, defaultdict
import random, math

class Dinic:
    def __init__(self,n): self.g=[[] for _ in range(n)]
    def add(self,u,v,c):
        a=[v,c,None,c]; b=[u,0,a,0]; a[2]=b; self.g[u].append(a); self.g[v].append(b)
    def maxflow(self,s,t):
        flow=0
        while True:
            level=[-1]*len(self.g); level[s]=0; q=deque([s])
            while q:
                u=q.popleft()
                for e in self.g[u]:
                    if e[1] and level[e[0]]<0: level[e[0]]=level[u]+1; q.append(e[0])
            if level[t]<0: return flow
            it=[0]*len(self.g)
            def dfs(u,f):
                if u==t: return f
                while it[u]<len(self.g[u]):
                    e=self.g[u][it[u]]
                    if e[1] and level[e[0]]==level[u]+1:
                        z=dfs(e[0],min(f,e[1]))
                        if z: e[1]-=z; e[2][1]+=z; return z
                    it[u]+=1
                return 0
            while True:
                z=dfs(s,10**18)
                if not z: break
                flow+=z
    def reachable(self,s):
        seen=[False]*len(self.g); seen[s]=True; q=deque([s])
        while q:
            u=q.popleft()
            for e in self.g[u]:
                if e[1] and not seen[e[0]]: seen[e[0]]=True; q.append(e[0])
        return seen

def run():
    rng=random.Random(SEED); z=defaultdict(int)
    for _ in range(SYSTEMS):
        sizes=[rng.randint(2,5)]; nt=rng.randint(2,5)
        caps=[[rng.randint(0,6) for _ in range(sizes[0])]]
        demand=[rng.randint(1,6) for _ in range(nt)]; kinds=[rng.randrange(2) for _ in range(nt)]
        src=0; idx=1; ins=[[]]; outs=[[]]
        for _ in range(sizes[0]): ins[0].append(idx); idx+=1; outs[0].append(idx); idx+=1
        terms=list(range(idx,idx+nt)); idx+=nt; sink=idx; g=Dinic(sink+1)
        INF=sum(demand)+sum(caps[0])+1
        for j in range(sizes[0]): g.add(src,ins[0][j],INF); g.add(ins[0][j],outs[0][j],caps[0][j])
        E={(rng.randrange(sizes[0]),v) for v in range(nt)}
        for u in range(sizes[0]):
            if not any(a==u for a,b in E): E.add((u,rng.randrange(nt)))
        for u in range(sizes[0]):
            for v in range(nt):
                if rng.random()<.45: E.add((u,v))
        for u,v in E: g.add(outs[0][u],terms[v],INF)
        for v,q in enumerate(demand): g.add(terms[v],sink,q)
        f=g.maxflow(src,sink); R=g.reachable(src)
        cut=sum(caps[0][j] for j in range(sizes[0]) if R[ins[0][j]] and not R[outs[0][j]])
        din=sum(demand[v] for v in range(nt) if R[terms[v]]); dout=sum(demand)-din
        assert din+cut==f
        unpaid=sum(demand)-f; assert unpaid==dout-cut
        for u,row in enumerate(g.g):
            for e in row:
                if e[3]==INF and R[u] and not R[e[0]]: raise AssertionError('guarded compatibility crossed')
        z['systems']+=1; z['capacity_classes']+=sizes[0]; z['terminal_classes']+=nt; z['compatibility_arcs']+=len(E)
        z['demand_units']+=sum(demand); z['paid_units']+=f; z['unpaid_units']+=unpaid; z['stage0_cut_units']+=cut
        if unpaid:
            z['deficient_systems']+=1; z['outside_terminal_classes']+=sum(not R[x] for x in terms)
            a=sum(demand[v] for v in range(nt) if not R[terms[v]] and kinds[v]==0)
            b=sum(demand[v] for v in range(nt) if not R[terms[v]] and kinds[v]==1)
            assert max(a,b)>=math.ceil(dout/2)
            z['type0_outside_units']+=a; z['type1_outside_units']+=b
    print(TITLE)
    for key in ORDER: print(f'{key}: {z[key]:,}')
if __name__=='__main__': run()
