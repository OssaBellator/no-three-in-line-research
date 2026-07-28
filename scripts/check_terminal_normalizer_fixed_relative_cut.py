#!/usr/bin/env python3
"""Regenerate or verify the fixed 16/5-relative terminal-normalizer cut."""
from __future__ import annotations
import argparse, json, os, subprocess, tempfile
from fractions import Fraction
from pathlib import Path

Q = Fraction(16, 5)
EXPECTED = {
  8: dict(zmin=1096, cut=[3488,3524], envelope=Fraction(87030,120697), relaxed=Fraction(99,137), low=432, high=1152, components=7, ties=2, bound=Fraction(3,4)),
  9: dict(zmin=2976, cut=[9520,9536], envelope=Fraction(13696,13857), relaxed=Fraction(92,93), low=1024, high=6144, components=8, ties=2, bound=Fraction(1,1)),
  10: dict(zmin=9872, cut=[31520,31648], envelope=Fraction(193592,610213), relaxed=Fraction(196,617), low=896, high=7168, components=9, ties=2, bound=Fraction(1,3)),
}

def instrument(parts: list[str]) -> str:
    text='\n'.join(parts)
    text=text.replace('#include <queue>\n','#include <queue>\n#include <set>\n')
    text=text.replace('  long long correlated_bin_target_cycles_tied=0;\n};', '''  long long correlated_bin_target_cycles_tied=0;
  long long fixed_cut_lower=0,fixed_cut_upper=0;
  long long fixed_cut_num=0,fixed_cut_den=1;
  long long fixed_cut_low_labels=0,fixed_cut_high_labels=0;
  long long fixed_relaxed_num=0,fixed_relaxed_den=1;
  long long fixed_relaxed_low_labels=0,fixed_relaxed_high_labels=0;
  int fixed_cut_target_components=0;
  long long fixed_cut_target_cycles_tied=0;
};''')
    text=text.replace('long long observed_min_normalizer=LLONG_MAX,observed_max_normalizer=0;',
                      'long long observed_min_normalizer=LLONG_MAX,observed_max_normalizer=0; set<long long> observed_normalizers;')
    text=text.replace('if(mult==0) continue;\n      observed_min_normalizer',
                      'if(mult==0) continue;\n      observed_normalizers.insert(capacity_sum);\n      observed_min_normalizer')
    marker='  // A two-scale envelope separates the low-normalizer harmonic tail from the\n'
    calc=r'''  vector<long long> exact_z(observed_normalizers.begin(),observed_normalizers.end());
  int DZ=exact_z.size(),selected=-1;
  for(int k=1;k<DZ;k++) if(5*exact_z[k]>=16*exact_z[0]){selected=k;break;}
  if(selected<0){cerr<<"no 16/5 threshold\n";return R;}
  unordered_map<long long,int> zpos;zpos.reserve(DZ*2);
  for(int i=0;i<DZ;i++)zpos[exact_z[i]]=i;
  vector<uint16_t> target_counts((size_t)NC*DZ,0);
  for(int x=0;x<NC;x++)if(cmin[x]==h){
    int cc=infos[x].components;vector<Gate> gates;
    for(int ti=0;ti<K;ti++){
      int y=neighbour[(size_t)x*K+ti];if(y<0||cmin[y]!=h-1)continue;auto T=triples[ti];
      array<uint64_t,MAXW> elig{};bool nonempty=false;
      for(int w=0;w<WORDS;w++){
        elig[w]=ownerbits[obase(x,T[0])+w]|ownerbits[obase(x,T[1])+w]|ownerbits[obase(x,T[2])+w];
        nonempty|=elig[w]!=0;
      }
      if(nonempty)gates.push_back({elig,y});
    }
    for(int root=0;root<(1<<cc);root++){
      long long capacity_sum=0;
      for(auto const&g:gates)if((g.elig[root>>6]>>(root&63))&1ULL)
        capacity_sum+=1LL<<infos[g.target].components;
      if(!capacity_sum)continue;
      int zi=zpos.at(capacity_sum);
      for(auto const&g:gates)if((g.elig[root>>6]>>(root&63))&1ULL){
        auto &cell=target_counts[(size_t)g.target*DZ+zi];
        if(cell==numeric_limits<uint16_t>::max()){cerr<<"threshold count overflow\n";return R;}
        cell++;
      }
    }
  }
  long long worstNum=0,worstDen=1,worstLow=0,worstHigh=0,worstTies=0;int worstTarget=-1;
  long long relaxedNum=0,relaxedDen=16*exact_z[0],relaxedLow=0,relaxedHigh=0;
  long long L0=exact_z[0],L1=exact_z[selected];
  for(int y=0;y<NC;y++){
    long long lo=0;for(int j=0;j<selected;j++)lo+=target_counts[(size_t)y*DZ+j];
    long long hi=raw_incoming[y]-lo;
    long long num=lo*L1+hi*L0,den=L0*L1;
    boost::multiprecision::int128_t left=boost::multiprecision::int128_t(num)*worstDen;
    boost::multiprecision::int128_t right=boost::multiprecision::int128_t(worstNum)*den;
    if(worstTarget<0||left>right){worstNum=num;worstDen=den;worstLow=lo;worstHigh=hi;worstTarget=y;worstTies=1;}
    else if(left==right)worstTies++;
    long long rn=16*lo+5*hi;
    if(rn>relaxedNum){relaxedNum=rn;relaxedLow=lo;relaxedHigh=hi;}
  }
  long long gg=std::gcd(worstNum,worstDen);
  R.fixed_cut_lower=exact_z[selected-1];R.fixed_cut_upper=L1;
  R.fixed_cut_num=worstNum/gg;R.fixed_cut_den=worstDen/gg;
  long long rg=std::gcd(relaxedNum,relaxedDen);R.fixed_relaxed_num=relaxedNum/rg;R.fixed_relaxed_den=relaxedDen/rg;
  R.fixed_relaxed_low_labels=relaxedLow;R.fixed_relaxed_high_labels=relaxedHigh;
  R.fixed_cut_low_labels=worstLow;R.fixed_cut_high_labels=worstHigh;
  R.fixed_cut_target_components=infos[worstTarget].components;
  R.fixed_cut_target_cycles_tied=worstTies;

'''
    if marker not in text: raise RuntimeError('two-scale marker missing')
    text=text.replace(marker,calc+marker)
    main=text.index('int main(int argc,char**argv){')
    text=text[:main]+r'''int main(int argc,char**argv){
  if(argc!=2){cerr<<"usage: checker m\n";return 2;}
  int m=atoi(argv[1]);Result r=run_case(m);
  cout<<"{\"m\":"<<m
      <<",\"minimum_normalizer\":"<<r.normalizer_min
      <<",\"cut\":["<<r.fixed_cut_lower<<","<<r.fixed_cut_upper<<"]"
      <<",\"envelope\":\""<<r.fixed_cut_num<<"/"<<r.fixed_cut_den<<"\""
      <<",\"relaxed_envelope\":\""<<r.fixed_relaxed_num<<"/"<<r.fixed_relaxed_den<<"\""
      <<",\"relaxed_low_labels\":"<<r.fixed_relaxed_low_labels
      <<",\"relaxed_high_labels\":"<<r.fixed_relaxed_high_labels
      <<",\"low_labels\":"<<r.fixed_cut_low_labels
      <<",\"high_labels\":"<<r.fixed_cut_high_labels
      <<",\"target_components\":"<<r.fixed_cut_target_components
      <<",\"target_cycles_tied\":"<<r.fixed_cut_target_cycles_tied<<"}\n";
}
'''
    return text

def regenerate(root: Path, threads: int) -> dict:
    scripts=root/'scripts'
    parts=[(scripts/f'terminal_normalizer_bin_envelope_part{i}.inc').read_text() for i in range(1,5)]
    source=instrument(parts); cases=[]
    with tempfile.TemporaryDirectory(prefix='terminal-fixed-relative-') as td:
      td=Path(td); cpp=td/'checker.cpp'; binary=td/'checker'; cpp.write_text(source)
      subprocess.run(['g++','-O3','-std=c++17','-Wall','-Wextra','-pedantic','-fopenmp',str(cpp),'-o',str(binary)],check=True,cwd=td)
      for m in (8,9,10):
        raw=json.loads(subprocess.check_output([str(binary),str(m)],text=True,cwd=td,env={**os.environ,'OMP_NUM_THREADS':str(threads)}))
        value=Fraction(raw['envelope']); bound=EXPECTED[m]['bound']
        cases.append({'m':m,'minimum_normalizer':raw['minimum_normalizer'],'relative_threshold':'16/5',
          'relative_threshold_times_minimum':str(Q*raw['minimum_normalizer']),
          'selected_consecutive_observed_normalizers':raw['cut'],'selected_threshold':raw['cut'][1],
          'worst_target_envelope':str(value),'worst_target_envelope_decimal':float(value),
          'dimensionless_relaxed_envelope':raw['relaxed_envelope'],'dimensionless_relaxed_envelope_decimal':float(Fraction(raw['relaxed_envelope'])),
          'dimensionless_clean_upper_bound':str(bound),'dimensionless_margin_below_clean_upper_bound':str(bound-Fraction(raw['relaxed_envelope'])),
          'maximizing_target_low_labels':raw['low_labels'],'maximizing_target_high_labels':raw['high_labels'],
          'maximizing_target_components':raw['target_components'],'maximizing_target_cycles_tied':raw['target_cycles_tied'],
          'clean_upper_bound':str(bound),'margin_below_clean_upper_bound':str(bound-value)})
    return {'relative_threshold':'16/5','threshold_selection':'first observed normalizer at least (16/5) times the global minimum normalizer','cases':cases,
      'all_fixed_relative_threshold_envelopes_contractive':True,'same_dimensionless_threshold_used_for_all_sizes':True,
      'asymptotic_fixed_relative_threshold_theorem_proved':False,'all_exact_regressions_verified':True}

def verify(ledger: dict) -> None:
    assert Fraction(ledger['relative_threshold'])==Q and len(ledger['cases'])==3
    for c in ledger['cases']:
      m=int(c['m']); e=EXPECTED[m]; val=Fraction(c['worst_target_envelope'])
      assert int(c['minimum_normalizer'])==e['zmin']
      assert list(c['selected_consecutive_observed_normalizers'])==e['cut']
      assert int(c['selected_threshold'])==e['cut'][1] and val==e['envelope'] and Fraction(c['dimensionless_relaxed_envelope'])==e['relaxed']
      assert int(c['maximizing_target_low_labels'])==e['low'] and int(c['maximizing_target_high_labels'])==e['high']
      assert int(c['maximizing_target_components'])==e['components'] and int(c['maximizing_target_cycles_tied'])==e['ties']
      assert Fraction(c['clean_upper_bound'])==e['bound'] and Fraction(c['margin_below_clean_upper_bound'])==e['bound']-val
      assert Fraction(c['dimensionless_clean_upper_bound'])==e['bound'] and Fraction(c['dimensionless_margin_below_clean_upper_bound'])==e['bound']-e['relaxed']
      assert e['relaxed']<1 and val<1

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('root',type=Path,nargs='?',default=Path('.')); ap.add_argument('--regenerate',action='store_true'); ap.add_argument('--threads',type=int,default=8); ap.add_argument('--output',type=Path); a=ap.parse_args()
    root=a.root.resolve(); path=root/'experiments/terminal-normalizer-fixed-relative-cut-through-m10-audit.json'
    if a.regenerate:
      ledger=regenerate(root,a.threads); out=a.output or path; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(ledger,indent=2)+'\n')
    else: ledger=json.loads(path.read_text())
    verify(ledger); print('terminal fixed 16/5-relative cut verified'); return 0
if __name__=='__main__': raise SystemExit(main())
