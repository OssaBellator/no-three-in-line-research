#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
from pathlib import Path
import re,subprocess,tempfile
HERE=Path(__file__).resolve().parent
N={'P0':((0,0),(0,2),(1,1),(1,3),(2,1),(2,3),(3,0),(3,2)),'P2':((0,1),(0,3),(1,0),(1,2),(2,0),(2,2),(3,1),(3,3)),'P3':((0,1),(0,2),(1,0),(1,3),(2,1),(2,2),(3,0),(3,3))}
def parse():
 t=(HERE/'check_boundary_nineteenth_spectrum.cpp').read_text();m=re.search(r'vector<Pt>\s*T=\{(.*?)\};\s*sort',t,re.S);return {tuple(map(int,p)) for p in re.findall(r'\{(-?\d+),(-?\d+)\}',m.group(1))}
def cross(a,b,c):return(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def legal(s):return all(cross(*x) for x in combinations(sorted(s),3))
def block(k,x,o):return{(x+a,213+o+b)for a,b in N[k]}
def apply(s,b,d,a):
 d=set(d);a=set(a);assert Counter(x for x,_ in d)==Counter(x for x,_ in a);assert Counter(y for _,y in d)==Counter(y for _,y in a);r=(s|b)-d|a;assert legal(r);return r
def compile(f,d):
 o=d/f[:-4];subprocess.run(['c++','-O3','-std=c++17',str(HERE/f),'-o',str(o)],check=True);return o
def spectra(bin,jobs):
 z=[str(len(jobs))]
 for l,s,x,q in jobs:z+=[f'{l} {len(s)} {x} {q}',*[f'{a} {b}'for a,b in sorted(s)]]
 L=subprocess.run([str(bin)],input='\n'.join(z)+'\n',text=True,capture_output=True,check=True).stdout.splitlines();R={};i=0
 while i<len(L):
  l=L[i].split()[1];i+=1;A=[]
  while L[i].startswith('ATT '):
   _,n,o,t,m,c=L[i].split();i+=1;C=[]
   for _ in range(int(c)):C.append(tuple(tuple(map(int,p.split(',')))for p in L[i].split()[1:]));i+=1
   A.append((n,int(o),int(m),C))
  p=L[i].split();b=p.index('BEST');h={int(k):int(v)for k,v in(q.split(':')for q in p[1:b])};i+=2;R[l]=(h,A)
 return R
def corrections(bin,jobs):
 z=[str(len(jobs))]
 for l,s,n,x,o,c in jobs:
  a=sorted(s|block(n,x,o));z+=[f'{l} {len(a)} 6 {len(c)}',*[f'{u} {v}'for u,v in a],*[f'{u} {v}'for u,v in c]]
 L=subprocess.run([str(bin)],input='\n'.join(z)+'\n',text=True,capture_output=True,check=True).stdout.splitlines();R={};i=0
 while i<len(L):
  _,l,f,ss,nn=L[i].split();i+=1;r={'found':int(f)}
  if int(f):r['D']={tuple(map(int,p.split(',')))for p in L[i].split()[1:]};i+=1;r['A']={tuple(map(int,p.split(',')))for p in L[i].split()[1:]};i+=1
  R[l]=r
 return R
s=parse();s=apply(s,block('P2',72,-64),{(1,113),(33,101),(57,347),(62,106),(73,151),(75,150),(75,152)},{(1,150),(33,347),(57,151),(62,152),(73,101),(75,106),(75,113)});s=apply(s,block('P3',76,-27),{(4,33),(7,32),(62,309),(70,214),(76,188),(78,187)},{(4,188),(7,187),(62,33),(70,309),(76,214),(78,32)})
with tempfile.TemporaryDirectory()as d:
 d=Path(d);sp=compile('boundary_spectrum_kernel.cpp',d);co=compile('boundary_exact_cover_kernel.cpp',d);base=spectra(sp,[('base',s,80,4)])['base'];jobs=[]
 for n,o,m,C in base[1]:
  for j,c in enumerate(C):jobs.append((f'{n}/{o}-core{j+1}',s,n,80,o,c))
 rr=corrections(co,jobs);states=[]
 for l,st,n,x,o,c in jobs:
  if rr[l]['found']:states.append((l,apply(st,block(n,x,o),rr[l]['D'],rr[l]['A'])))
 assert len(states)==11
 out=spectra(sp,[(l,st,84,6)for l,st in states]);table=[]
 for l,st in states:
  h,A=out[l];best=min(h);ats=[a for a in A if a[2]==best];table.append((l,best,len(ats),sum(len(a[3])for a in ats)))
 expected=[('P0/59-core1',5,3,9),('P2/60-core2',4,1,1),('P3/60-core3',5,4,4),('P3/60-core4',5,2,2),('P3/60-core5',5,2,2),('P3/60-core6',5,2,2),('P3/60-core7',5,2,2),('P3/60-core8',6,26,178),('P3/60-core12',5,2,2),('P3/60-core20',5,1,9),('P3/60-core23',6,37,167)]
 assert table==expected
print({'budget_six_repairs':11,'selected':'P3/60-core8','selection_rule':'maximize minimum, then minimize minimum attempts','status':'passed'})
