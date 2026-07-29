#!/usr/bin/env python3
from fractions import Fraction as F

# tail, head, shared attenuation index, baseline
E=[(0,1,0,F(1)),(1,0,0,F(0)),(1,2,1,F(1)),(2,1,1,F(0)),(2,0,2,F(1)),(0,2,2,F(0))]
C=[(0,1),(2,3),(4,5),(0,2,4),(5,3,1)]

def s(c,x): return sum(E[i][3]-x[E[i][2]] for i in c)
def mean(x): return max(s(c,x)/len(c) for c in C)

trial=(F(1,2),)*3
assert len(C)==5 and max(s(c,trial) for c in C)==F(3,2) and mean(trial)==F(1,2)
opt=(F(1),)*3
assert sum(opt)==F(3) and all(s(c,opt)<=0 for c in C) and mean(opt)==0
h=(F(0),)*3
assert all(h[v]-h[u]>=b-opt[r] for u,v,r,b in E)
y=[F(1),F(0),F(1),F(0),F(1),F(0)]
assert all(sum(y[i] for i,(u,_,_,_) in enumerate(E) if u==v)==sum(y[i] for i,(_,w,_,_) in enumerate(E) if w==v) for v in range(3))
assert all(sum(y[i] for i,(_,_,q,_) in enumerate(E) if q==r)<=1 for r in range(3))
assert sum(y[i]*E[i][3] for i in range(6))==3
print({"simple_cycles":5,"trial_positive_cycle_sum":"3/2","trial_maximum_cycle_mean":"1/2","compact_primal_optimum":"3","potential_certificate":["0","0","0"],"circulation_dual_value":"3"})
