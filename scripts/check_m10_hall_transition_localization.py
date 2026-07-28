#!/usr/bin/env python3
"""Regenerate or verify the m=10 Hall transition localization audit."""
from __future__ import annotations
import argparse, json, os, subprocess, tempfile
from fractions import Fraction
from pathlib import Path

EXPECTED = {
    'global': 8, 'localized': 60, 'non': 216,
    'types': [(40,8,4,4),(124,20,4,16),(120,40,0,40)],
    'max_global': (Fraction(713904,596453),278),
    'max_local_a': (Fraction(1984,1563),248),
    'max_local_penalty': (Fraction(46304896,23735187),215),
    'max_penalty': (Fraction(1500597,656230),222),
}

def instrument(src: str) -> str:
    old='  struct TypeAcc{long long flaws=0,violations=0;long long np=0,nq=1;int sourceCount=0;Candidate worst{};};\n'
    add=old+'''  struct Record{
    int sourceCount=0,pathComponents=0,targets=0,minSourceDegree=0,maxSourceDegree=0;
    long long incidences=0,globalSupply=0,globalCapacity=0;
    long long p=0,q=1;int subset=0;long long subsetSupply=0,subsetCapacity=1;
    Candidate candidate{};
  };
'''
    if old not in src: raise RuntimeError('TypeAcc marker missing')
    src=src.replace(old,add,1)
    old='  vector<vector<int>> positions(threads, vector<int>(C,-1));\n'
    if old not in src: raise RuntimeError('positions marker missing')
    src=src.replace(old,old+'  vector<vector<Record>> records(threads);\n',1)
    old='    long long gs=accumulate(weights.begin(),weights.end(),0LL),gc=accumulate(caps.begin(),caps.end(),0LL),d=gcd(gs,gc),gp=gs/d,gq=gc/d;\n'
    add=old+'''    long long edgeCount=0;int minDeg=INT_MAX,maxDeg=0;
    for(auto const&v:nbr){edgeCount+=v.size();minDeg=min(minDeg,(int)v.size());maxDeg=max(maxDeg,(int)v.size());}
    records[tid].push_back({(int)sources.size(),arc_path_components(c,triples),(int)all.size(),
      minDeg,maxDeg,edgeCount,gs,gc,r.p,r.q,r.subset,r.supply,r.capacity,c});
'''
    if old not in src: raise RuntimeError('global ratio marker missing')
    src=src.replace(old,add,1)
    marker='  bool ok=C==362880&&cleanCycles==297886&&cleanStates==115586396&&\n'
    aggregate=r'''  vector<Record> allRecords;
  for(auto &v:records)allRecords.insert(allRecords.end(),v.begin(),v.end());
  sort(allRecords.begin(),allRecords.end(),[](Record const&a,Record const&b){
    return tie(a.sourceCount,a.candidate.s,a.candidate.ta,a.candidate.tb,a.candidate.tc,a.candidate.mask)<
           tie(b.sourceCount,b.candidate.s,b.candidate.ta,b.candidate.tb,b.candidate.tc,b.candidate.mask);
  });
  struct Category{long long total=0,violations=0,global=0,localized=0;};
  array<Category,3> categories{};long long globalViolations=0,localizedViolations=0,nonviolations=0;
  auto crossGreater=[](long long an,long long ad,long long bn,long long bd){
    return boost::multiprecision::int128_t(an)*bd>boost::multiprecision::int128_t(bn)*ad;
  };
  Record maxGlobal{},maxLocalA{},maxLocalPenalty{},maxPenalty{};bool haveGlobal=false,haveLocalA=false,haveLocalPenalty=false,havePenalty=false;
  for(auto const&r:allRecords){
    long long an=(long long)r.sourceCount*r.p,ad=r.q;
    long long gn=(long long)r.sourceCount*r.globalSupply,gd=r.globalCapacity;
    bool violation=an>ad,global=gn>gd;auto &cat=categories[r.pathComponents-1];cat.total+=2;
    if(violation){cat.violations+=2;if(global){cat.global+=2;globalViolations+=2;}else{cat.localized+=2;localizedViolations+=2;}}
    else nonviolations+=2;
    if(!haveGlobal||crossGreater(gn,gd,(long long)maxGlobal.sourceCount*maxGlobal.globalSupply,maxGlobal.globalCapacity)){maxGlobal=r;haveGlobal=true;}
    if(violation&&!global&&(!haveLocalA||crossGreater(an,ad,(long long)maxLocalA.sourceCount*maxLocalA.p,maxLocalA.q))){maxLocalA=r;haveLocalA=true;}
    long long pn=r.p*r.globalCapacity,pd=r.q*r.globalSupply;
    if(violation&&!global&&(!haveLocalPenalty||crossGreater(pn,pd,maxLocalPenalty.p*maxLocalPenalty.globalCapacity,maxLocalPenalty.q*maxLocalPenalty.globalSupply))){maxLocalPenalty=r;haveLocalPenalty=true;}
    if(!havePenalty||crossGreater(pn,pd,maxPenalty.p*maxPenalty.globalCapacity,maxPenalty.q*maxPenalty.globalSupply)){maxPenalty=r;havePenalty=true;}
  }
  auto reduced=[](long long n,long long d){long long g=std::gcd(n,d);return pair<long long,long long>{n/g,d/g};};
  auto gMax=reduced((long long)maxGlobal.sourceCount*maxGlobal.globalSupply,maxGlobal.globalCapacity);
  auto aLocal=reduced((long long)maxLocalA.sourceCount*maxLocalA.p,maxLocalA.q);
  auto pLocal=reduced(maxLocalPenalty.p*maxLocalPenalty.globalCapacity,maxLocalPenalty.q*maxLocalPenalty.globalSupply);
  auto pAll=reduced(maxPenalty.p*maxPenalty.globalCapacity,maxPenalty.q*maxPenalty.globalSupply);
'''
    if marker not in src: raise RuntimeError('regression marker missing')
    src=src.replace(marker,aggregate+marker,1)
    old='''      countMaxByType[0]==4&&countMaxByType[1]==17&&countMaxByType[2]==22&&
      violatingCountMaxByType[0]==1&&violatingCountMaxByType[1]==2&&violatingCountMaxByType[2]==10;
'''
    new='''      countMaxByType[0]==4&&countMaxByType[1]==17&&countMaxByType[2]==22&&
      violatingCountMaxByType[0]==1&&violatingCountMaxByType[1]==2&&violatingCountMaxByType[2]==10&&
      globalViolations==8&&localizedViolations==60&&nonviolations==216&&
      categories[0].total==40&&categories[0].violations==8&&categories[0].global==4&&categories[0].localized==4&&
      categories[1].total==124&&categories[1].violations==20&&categories[1].global==4&&categories[1].localized==16&&
      categories[2].total==120&&categories[2].violations==40&&categories[2].global==0&&categories[2].localized==40&&
      gMax.first==713904&&gMax.second==596453&&maxGlobal.sourceCount==278&&
      aLocal.first==1984&&aLocal.second==1563&&maxLocalA.sourceCount==248&&
      pLocal.first==46304896&&pLocal.second==23735187&&maxLocalPenalty.sourceCount==215&&
      pAll.first==1500597&&pAll.second==656230&&maxPenalty.sourceCount==222;
'''
    if old not in src: raise RuntimeError('transition regression marker missing')
    src=src.replace(old,new,1)
    old='  cout<<"],\\n  \\\"transition_nonempty_source_counts\\\":"<<nonemptyCountRows\n'
    output=r'''  cout<<"],\n  \"localization_decomposition\":{\"global_mass_violations\":"<<globalViolations
      <<",\"proper_subset_only_violations\":"<<localizedViolations
      <<",\"nonviolations\":"<<nonviolations<<"},\n"
      <<"  \"localization_by_arc_type\":[";
  for(int t=0;t<3;t++){
    if(t)cout<<",";
    auto const&c=categories[t];
    cout<<"{\"path_components\":"<<(t+1)<<",\"path_type\":\""<<arc_path_type(t+1)<<"\""
        <<",\"signed_flaws\":"<<c.total<<",\"violations\":"<<c.violations
        <<",\"global_mass_violations\":"<<c.global
        <<",\"proper_subset_only_violations\":"<<c.localized<<"}";
  }
  auto emitWitness=[&](char const*name,Record const&r,long long n,long long q){
    auto S=triples[r.candidate.s];
    cout<<"  \""<<name<<"\":{\"value\":\""<<n<<"/"<<q<<"\",\"source_cycles\":"<<r.sourceCount
        <<",\"path_components\":"<<r.pathComponents<<",\"targets\":"<<r.targets
        <<",\"incidences\":"<<r.incidences<<",\"min_source_degree\":"<<r.minSourceDegree
        <<",\"max_source_degree\":"<<r.maxSourceDegree
        <<",\"global_supply\":"<<r.globalSupply<<",\"global_capacity\":"<<r.globalCapacity
        <<",\"optimal_charge\":\""<<r.p<<"/"<<r.q<<"\""
        <<",\"hall_subset_size\":"<<r.subset<<",\"hall_subset_supply\":"<<r.subsetSupply
        <<",\"hall_subset_capacity\":"<<r.subsetCapacity
        <<",\"source_owners\":["<<S[0]<<","<<S[1]<<","<<S[2]<<"]"
        <<",\"targets_assignment\":["<<int(r.candidate.ta)<<","<<int(r.candidate.tb)<<","<<int(r.candidate.tc)<<"]}";
  };
  cout<<"],\n";emitWitness("maximum_global_support_normalized_ratio",maxGlobal,gMax.first,gMax.second);cout<<",\n";
  emitWitness("maximum_localized_violation",maxLocalA,aLocal.first,aLocal.second);cout<<",\n";
  emitWitness("maximum_localization_factor_among_localized_violations",maxLocalPenalty,pLocal.first,pLocal.second);cout<<",\n";
  emitWitness("maximum_localization_factor_overall",maxPenalty,pAll.first,pAll.second);cout<<",\n";
  cout<<"  \"transition_nonempty_source_counts\":"<<nonemptyCountRows
'''
    if old not in src: raise RuntimeError('output marker missing')
    return src.replace(old,output,1)

def enrich(r: dict) -> dict:
    s=int(r['source_cycles']); charge=Fraction(r['optimal_charge'])
    out=dict(r); out['support_normalized_charge']=str(s*charge)
    out['global_support_normalized_ratio']=str(Fraction(s*r['global_supply'],r['global_capacity']))
    out['localization_factor']=str(charge*Fraction(r['global_capacity'],r['global_supply']))
    return out

def compact(raw: dict) -> dict:
    return {
      'm':10,'source_cycle_window':[209,287],'nonempty_source_counts':43,
      'supported_signed_flaws':284,'proper_hall_bottlenecks':284,
      'definitions':{'A_f':'s(f) * gamma(f)','G_f':'s(f) * total_source_supply / total_reached_target_capacity','Lambda_f':'gamma(f) / (total_source_supply / total_reached_target_capacity)','identity':'A_f = G_f * Lambda_f'},
      'decomposition':{**raw['localization_decomposition'],'global_fraction_of_all_violations':'2/17','proper_subset_only_fraction_of_all_violations':'15/17'},
      'by_arc_path_type':raw['localization_by_arc_type'],
      'maximum_global_support_normalized_ratio':enrich(raw['maximum_global_support_normalized_ratio']),
      'maximum_localized_violation':enrich(raw['maximum_localized_violation']),
      'maximum_localization_factor_among_localized_violations':enrich(raw['maximum_localization_factor_among_localized_violations']),
      'maximum_localization_factor_overall':enrich(raw['maximum_localization_factor_overall']),
      'all_three_arc_types_have_proper_subset_only_violations':True,
      'all_three_disjoint_arc_violations_are_proper_subset_only':True,
      'source_count_and_arc_connectivity_sufficient_statistics':False,
      'asymptotic_localization_theorem_proved':False,'all_exact_regressions_verified':True,
    }

def regenerate(root: Path, threads: int) -> dict:
    source=instrument((root/'scripts/check_m10_hall_transition_arc_path_type.cpp').read_text())
    with tempfile.TemporaryDirectory(prefix='hall-localization-') as td:
      td=Path(td); cpp=td/'checker.cpp'; binary=td/'checker'; cpp.write_text(source)
      subprocess.run(['g++','-O3','-std=c++17','-Wall','-Wextra','-pedantic','-fopenmp',str(cpp),'-o',str(binary)],check=True,cwd=td)
      raw=json.loads(subprocess.check_output([str(binary),'209','287'],text=True,cwd=td,env={**os.environ,'OMP_NUM_THREADS':str(threads)}))
    return compact(raw)

def verify(d: dict) -> None:
    assert d['m']==10 and d['source_cycle_window']==[209,287] and d['supported_signed_flaws']==284 and d['proper_hall_bottlenecks']==284
    dec=d['decomposition']; assert (dec['global_mass_violations'],dec['proper_subset_only_violations'],dec['nonviolations'])==(8,60,216)
    assert Fraction(dec['global_fraction_of_all_violations'])==Fraction(2,17) and Fraction(dec['proper_subset_only_fraction_of_all_violations'])==Fraction(15,17)
    for row,e in zip(d['by_arc_path_type'],EXPECTED['types']): assert (row['signed_flaws'],row['violations'],row['global_mass_violations'],row['proper_subset_only_violations'])==e
    keys=[('maximum_global_support_normalized_ratio','max_global'),('maximum_localized_violation','max_local_a'),('maximum_localization_factor_among_localized_violations','max_local_penalty'),('maximum_localization_factor_overall','max_penalty')]
    for key,ek in keys:
      r=d[key]; val,s=EXPECTED[ek]; assert Fraction(r['value'])==val and r['source_cycles']==s
      A=Fraction(r['support_normalized_charge']);G=Fraction(r['global_support_normalized_ratio']);L=Fraction(r['localization_factor']);assert A==G*L
    assert Fraction(d['maximum_localized_violation']['global_support_normalized_ratio'])<1<Fraction(d['maximum_localized_violation']['support_normalized_charge'])
    assert Fraction(d['maximum_localization_factor_overall']['support_normalized_charge'])<1
    assert d['all_three_disjoint_arc_violations_are_proper_subset_only'] and not d['source_count_and_arc_connectivity_sufficient_statistics']
    assert not d['asymptotic_localization_theorem_proved'] and d['all_exact_regressions_verified']

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('root',type=Path,nargs='?',default=Path('.'));ap.add_argument('--regenerate',action='store_true');ap.add_argument('--threads',type=int,default=8);ap.add_argument('--output',type=Path);a=ap.parse_args()
    root=a.root.resolve();path=root/'experiments/m10-hall-transition-neighborhood-localization-audit.json'
    if a.regenerate:
      ledger=regenerate(root,a.threads);out=a.output or path;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(ledger,indent=2)+'\n')
    else: ledger=json.loads(path.read_text())
    verify(ledger);print('m10 Hall transition localization verified: 8 global, 60 proper-subset-only');return 0
if __name__=='__main__':raise SystemExit(main())
