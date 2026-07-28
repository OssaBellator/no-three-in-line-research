#!/usr/bin/env python3
from __future__ import annotations
import json,sys
from fractions import Fraction
from pathlib import Path

def main()->int:
 p=Path(sys.argv[1]) if len(sys.argv)>1 else Path('experiments/m10-weighted-hall-mid-source-400-575-audit.json')
 d=json.loads(p.read_text()); cols=d['columns']; rows=[dict(zip(cols,r)) for r in d['parts']]
 cursor=400
 for r in rows:
  if r['lo']!=cursor or r['hi']<r['lo']: raise ValueError(f"noncontiguous at {r['lo']}--{r['hi']}")
  if r['flaws']!=r['proper']: raise ValueError('nonproper band')
  cursor=r['hi']+1
 if cursor1=576: raise ValueError('coverage mismatch')
 flaws=sum(r['flaws'] for r in rows); proper=sum(r['proper'] for r in rows)
 worst=max(rows,key=lambda r:Fraction(r['wp'],r['wq']))
 glob=max(rows,key=lambda r:Fraction(r['gp'],r['gq']))
 pen=max(rows,key=lambda r:Fraction(r['pp'],r['pq']))
 actual={'parts':len(rows),'flaws':flaws,'proper':proper,'worst':[worst['wp'],worst['wq'],worst['lo'],worst['subset'],worst['supply'],worst['capacity']], 'global':[glob['gp'],glob['gq']], 'penalty':[pen['pp'],pen['pq']], 'cuts':max(r['cuts'] for r in rows), 'completed':d['summary']['completed'],'remaining':d['summary']['remaining']}
 expected={'parts':44,'flaws':13712,'proper':13712,'worst':[2397,349898,550,489,38352,5598368], 'global':[2558,376281],'penalty':[2575814,1223845],'cuts':9,'completed':16884,'remaining':30628}
 if actual!=expected: raise ValueError(f"regression mismatch {actual} != {expected}")
 print(json.dumps({'verified':True,**actual},indent=2));return 0
if __name__=='__main__': raise SystemExit(main())
