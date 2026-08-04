#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
NODES = {
    'P0': ((0,0),(0,2),(1,1),(1,3),(2,1),(2,3),(3,0),(3,2)),
    'P1': ((0,0),(0,3),(1,1),(1,2),(2,0),(2,3),(3,1),(3,2)),
    'P2': ((0,1),(0,3),(1,0),(1,2),(2,0),(2,2),(3,1),(3,3)),
    'P3': ((0,1),(0,2),(1,0),(1,3),(2,1),(2,2),(3,0),(3,3)),
}

def parse_state(path):
    text=path.read_text(); m=re.search(r'vector<Pt>\s*T=\{(.*?)\};\s*sort',text,re.S); assert m
    return {tuple(map(int,p)) for p in re.findall(r'\{(-?\d+),(-?\d+)\}',m.group(1))}
def cross(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def legal(s): return all(cross(*t) for t in combinations(sorted(s),3))
def block(name,x,off): return {(x+a,213+off+b) for a,b in NODES[name]}
def apply(state,b,d,a):
    d=set(d);a=set(a); assert d<=state|b
    assert Counter(x for x,_ in d)==Counter(x for x,_ in a)
    assert Counter(y for _,y in d)==Counter(y for _,y in a)
    r=(state|b)-d|a; assert len(r)==len(state)+len(b) and legal(r); return r
def compile(name,td):
    out=td/name.replace('.cpp',''); subprocess.run(['c++','-O3','-std=c++17',str(HERE/name),'-o',str(out)],check=True); return out
def spectrum(binary,jobs):
    inp=[str(len(jobs))]
    for label,state,origin,limit in jobs:
        inp.append(f'{label} {len(state)} {origin} {limit}'); inp += [f'{x} {y}' for x,y in sorted(state)]
    lines=subprocess.run([str(binary)],input='\n'.join(inp)+'\n',text=True,capture_output=True,check=True).stdout.splitlines()
    ans={};i=0
    while i<len(lines):
        label=lines[i].split()[1];i+=1;ats=[]
        while lines[i].startswith('ATT '):
            _,name,off,tr,m,c=lines[i].split();i+=1;cores=[]
            for _ in range(int(c)):
                cores.append(tuple(tuple(map(int,p.split(','))) for p in lines[i].split()[1:]));i+=1
            ats.append((name,int(off),int(tr),int(m),cores))
        p=lines[i].split();b=p.index('BEST');h={int(k):int(v) for k,v in (q.split(':') for q in p[1:b])};best=int(p[b+1]);i+=2
        ans[label]=(h,best,ats)
    return ans
def correction(binary,jid,state,name,origin,off,core,budgets):
    allp=sorted(state|block(name,origin,off)); inp=[str(len(budgets))]
    for b in budgets:
        inp.append(f'{jid}b{b} {len(allp)} {b} {len(core)}');inp += [f'{x} {y}' for x,y in allp];inp += [f'{x} {y}' for x,y in core]
    lines=subprocess.run([str(binary)],input='\n'.join(inp)+'\n',text=True,capture_output=True,check=True).stdout.splitlines();out={};i=0
    while i<len(lines):
        _,key,found,subsets,nodes=lines[i].split();i+=1;r={'found':bool(int(found)),'subsets':int(subsets),'nodes':int(nodes)}
        if r['found']:
            r['D']={tuple(map(int,p.split(','))) for p in lines[i].split()[1:]};i+=1
            r['A']={tuple(map(int,p.split(','))) for p in lines[i].split()[1:]};i+=1
        out[int(key.rsplit('b',1)[1])]=r
    return out
def find(ats,name,off,core):
    a=next(x for x in ats if x[0]==name and x[1]==off); assert core in a[4]; return core

state18=parse_state(HERE/'check_boundary_nineteenth_spectrum.cpp');assert len(state18)==144 and legal(state18)
with tempfile.TemporaryDirectory() as d:
    td=Path(d);sp=compile('boundary_spectrum_kernel.cpp',td);co=compile('boundary_exact_cover_kernel.cpp',td)
    s19=spectrum(sp,[('s19',state18,72,4)])['s19'];assert s19[0]=={4:2,5:9,6:47,7:175,8:283,9:3,10:16,11:63,12:121,13:176,14:137}
    core19=find(s19[2],'P2',-64,((33,101),(73,151),(75,150),(75,152)))
    r19=correction(co,'r19',state18,'P2',72,-64,core19,(4,5,6,7));assert [r19[b]['found'] for b in (4,5,6,7)]==[False,False,False,True]
    D19={(1,113),(33,101),(57,347),(62,106),(73,151),(75,150),(75,152)};A19={(1,150),(33,347),(57,151),(62,152),(73,101),(75,106),(75,113)}
    assert r19[7]['D']==D19 and r19[7]['A']==A19
    state19=apply(state18,block('P2',72,-64),D19,A19)
    first19=apply(state18,block('P2',72,-64),{(8,34),(13,77),(16,76),(46,1),(73,151),(75,150),(75,152)},{(8,77),(13,152),(16,151),(46,150),(73,34),(75,1),(75,76)})
    s20s=spectrum(sp,[('first',first19,76,4),('second',state19,76,4)])
    assert s20s['first'][0]=={4:3,5:21,6:73,7:195,8:224,9:4,10:35,11:98,12:140,13:153,14:86}
    s20=s20s['second'];assert s20[0]=={4:2,5:14,6:74,7:199,8:227,9:2,10:23,11:91,12:160,13:149,14:91}
    assert sum(s20[0][k] for k in (4,5,6)) < sum(s20s['first'][0][k] for k in (4,5,6))
    core20=find(s20[2],'P3',-27,((62,309),(70,214),(76,188),(78,187)))
    r20=correction(co,'r20',state19,'P3',76,-27,core20,(4,5,6));assert [r20[b]['found'] for b in (4,5,6)]==[False,False,True]
    D20={(4,33),(7,32),(62,309),(70,214),(76,188),(78,187)};A20={(4,188),(7,187),(62,33),(70,309),(76,214),(78,32)}
    assert r20[6]['D']==D20 and r20[6]['A']==A20
    state20=apply(state19,block('P3',76,-27),D20,A20)
    s21=spectrum(sp,[('s21',state20,80,4)])['s21'];assert s21[0]=={4:3,5:11,6:63,7:184,8:255,9:3,10:13,11:51,12:117,13:180,14:152}
    core21=find(s21[2],'P3',60,((10,58),(29,111),(81,276),(83,276)))
    r21=correction(co,'r21',state20,'P3',80,60,core21,(4,5,6));assert [r21[b]['found'] for b in (4,5,6)]==[False,False,True]
    D21={(10,58),(18,76),(29,111),(53,376),(81,276),(83,276)};A21={(10,276),(18,276),(29,376),(53,58),(81,111),(83,76)}
    assert r21[6]['D']==D21 and r21[6]['A']==A21
    state21=apply(state20,block('P3',80,60),D21,A21)
    s22=spectrum(sp,[('s22',state21,84,6)])['s22'];assert s22[0]=={6:26,7:205,8:285,9:1,10:3,11:38,12:100,13:199,14:175}
    mins=[a for a in s22[2] if a[3]==6];assert len(mins)==26 and sum(len(a[4]) for a in mins)==178
print({'canonical_nineteenth_repair':'P2/-64 core 2 budget 7','corrected_state_sizes':(152,160,168),'twentysecond_minimum':6,'twentysecond_minimum_attempts':26,'twentysecond_minimum_cores':178,'status':'passed'})
