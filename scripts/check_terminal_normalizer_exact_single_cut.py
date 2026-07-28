#!/usr/bin/env python3
"""Regenerate or verify the exact best one-cut terminal-normalizer envelopes.

Regeneration instruments the already committed correlated-bin implementation in
a temporary directory. It records the exact normalizer support, builds the
complete target-by-normalizer count matrix, and minimizes the worst-target
lower-edge envelope over every cut between consecutive observed normalizers.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import tempfile
from fractions import Fraction
from pathlib import Path

EXPECTED = {
    8: {
        "distinct_normalizers": 166,
        "cut": [3152, 3168],
        "envelope": Fraction(2852, 4521),
        "low_labels": 160,
        "high_labels": 1536,
        "target_components": 6,
        "target_cycles_tied": 2,
        "clean_bound": Fraction(2, 3),
    },
    9: {
        "distinct_normalizers": 704,
        "cut": [9648, 9664],
        "envelope": Fraction(13760, 14043),
        "low_labels": 1024,
        "high_labels": 6144,
        "target_components": 8,
        "target_cycles_tied": 2,
        "clean_bound": Fraction(49, 50),
    },
    10: {
        "distinct_normalizers": 684,
        "cut": [39584, 39824],
        "envelope": Fraction(415800, 1535713),
        "low_labels": 896,
        "high_labels": 7168,
        "target_components": 9,
        "target_cycles_tied": 2,
        "clean_bound": Fraction(3, 10),
    },
}


def instrument(parts: list[str]) -> str:
    text = "\n".join(parts)
    text = text.replace("#include <queue>\n", "#include <queue>\n#include <set>\n")
    text = text.replace(
        "  long long correlated_bin_target_cycles_tied=0;\n};",
        """  long long correlated_bin_target_cycles_tied=0;
  long long exact_cut_lower=0,exact_cut_upper=0;
  long long exact_cut_num=0,exact_cut_den=1;
  long long exact_cut_low_labels=0,exact_cut_high_labels=0;
  int exact_cut_target_components=0;
  long long exact_cut_target_cycles_tied=0;
  long long distinct_normalizers=0;
};""",
    )
    text = text.replace(
        "long long observed_min_normalizer=LLONG_MAX,observed_max_normalizer=0;",
        "long long observed_min_normalizer=LLONG_MAX,observed_max_normalizer=0; set<long long> observed_normalizers;",
    )
    text = text.replace(
        "if(mult==0) continue;\n      observed_min_normalizer",
        "if(mult==0) continue;\n      observed_normalizers.insert(capacity_sum);\n      observed_min_normalizer",
    )
    marker = "  // A two-scale envelope separates the low-normalizer harmonic tail from the\n"
    calculation = r'''  // Optimize one exact global normalizer cut. The low segment uses the
  // global minimum normalizer; the high segment begins at one observed value.
  vector<long long> exact_z(observed_normalizers.begin(),observed_normalizers.end());
  int DZ=exact_z.size();
  unordered_map<long long,int> zpos;zpos.reserve(DZ*2);
  for(int i=0;i<DZ;i++)zpos[exact_z[i]]=i;
  vector<uint16_t> exact_target_counts((size_t)NC*DZ,0);
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
        auto &cell=exact_target_counts[(size_t)g.target*DZ+zi];
        if(cell==numeric_limits<uint16_t>::max()){
          cerr<<"exact threshold count overflow\n";return R;
        }
        cell++;
      }
    }
  }
  vector<long long> low_count(NC,0);
  long long optNum=0,optDen=1,optLower=0,optUpper=0,optLow=0,optHigh=0,optTies=0;
  int optTarget=-1;
  for(int k=1;k<DZ;k++){
    for(int y=0;y<NC;y++)low_count[y]+=exact_target_counts[(size_t)y*DZ+(k-1)];
    long long L0=exact_z[0],L1=exact_z[k];
    long long worstNum=0,worstDen=1,worstLow=0,worstHigh=0,worstTies=0;int worstTarget=-1;
    for(int y=0;y<NC;y++){
      long long lo=low_count[y],hi=raw_incoming[y]-lo;
      long long num=lo*L1+hi*L0,den=L0*L1;
      boost::multiprecision::int128_t left=boost::multiprecision::int128_t(num)*worstDen;
      boost::multiprecision::int128_t right=boost::multiprecision::int128_t(worstNum)*den;
      if(worstTarget<0||left>right){
        worstNum=num;worstDen=den;worstLow=lo;worstHigh=hi;worstTarget=y;worstTies=1;
      }else if(left==right)worstTies++;
    }
    boost::multiprecision::int128_t left=boost::multiprecision::int128_t(worstNum)*optDen;
    boost::multiprecision::int128_t right=boost::multiprecision::int128_t(optNum)*worstDen;
    if(optTarget<0||left<right){
      long long g=std::gcd(worstNum,worstDen);
      optNum=worstNum/g;optDen=worstDen/g;optLower=exact_z[k-1];optUpper=L1;
      optLow=worstLow;optHigh=worstHigh;optTarget=worstTarget;optTies=worstTies;
    }
  }
  R.exact_cut_lower=optLower;R.exact_cut_upper=optUpper;
  R.exact_cut_num=optNum;R.exact_cut_den=optDen;
  R.exact_cut_low_labels=optLow;R.exact_cut_high_labels=optHigh;
  R.exact_cut_target_components=infos[optTarget].components;
  R.exact_cut_target_cycles_tied=optTies;R.distinct_normalizers=DZ;

'''
    if marker not in text:
        raise RuntimeError("could not locate two-scale marker")
    text = text.replace(marker, calculation + marker)
    main_index = text.index("int main(int argc,char**argv){")
    text = text[:main_index] + r'''int main(int argc,char**argv){
  if(argc!=2){cerr<<"usage: checker m\n";return 2;}
  int m=atoi(argv[1]);Result r=run_case(m);
  cout<<"{\"m\":"<<m
      <<",\"distinct_normalizers\":"<<r.distinct_normalizers
      <<",\"cut\":["<<r.exact_cut_lower<<","<<r.exact_cut_upper<<"]"
      <<",\"envelope\":\""<<r.exact_cut_num<<"/"<<r.exact_cut_den<<"\""
      <<",\"low_labels\":"<<r.exact_cut_low_labels
      <<",\"high_labels\":"<<r.exact_cut_high_labels
      <<",\"target_components\":"<<r.exact_cut_target_components
      <<",\"target_cycles_tied\":"<<r.exact_cut_target_cycles_tied<<"}\n";
}
'''
    return text


def regenerate(root: Path, threads: int) -> dict:
    scripts = root / "scripts"
    names = [f"terminal_normalizer_bin_envelope_part{i}.inc" for i in range(1, 5)]
    parts = [(scripts / name).read_text(encoding="utf-8") for name in names]
    source = instrument(parts)
    cases = []
    with tempfile.TemporaryDirectory(prefix="terminal-exact-cut-") as temp_name:
        temp = Path(temp_name)
        cpp = temp / "checker.cpp"
        binary = temp / "checker"
        cpp.write_text(source, encoding="utf-8")
        subprocess.run(
            ["g++", "-O3", "-std=c++17", "-Wall", "-Wextra", "-pedantic", "-fopenmp", str(cpp), "-o", str(binary)],
            check=True,
            cwd=temp,
        )
        for m in (8, 9, 10):
            output = subprocess.check_output(
                [str(binary), str(m)],
                text=True,
                cwd=temp,
                env={**os.environ, "OMP_NUM_THREADS": str(threads)},
            )
            raw = json.loads(output)
            value = Fraction(raw["envelope"])
            clean = EXPECTED[m]["clean_bound"]
            cases.append({
                "m": m,
                "distinct_normalizers": raw["distinct_normalizers"],
                "best_cut_between_consecutive_observed_normalizers": raw["cut"],
                "best_two_segment_envelope": str(value),
                "best_two_segment_envelope_decimal": float(value),
                "maximizing_target_low_labels": raw["low_labels"],
                "maximizing_target_high_labels": raw["high_labels"],
                "maximizing_target_components": raw["target_components"],
                "maximizing_target_cycles_tied": raw["target_cycles_tied"],
                "clean_upper_bound": str(clean),
                "margin_below_clean_upper_bound": str(clean - value),
            })
    return {
        "cases": cases,
        "cut_definition": "low segment uses the global minimum normalizer; high segment begins at the upper cut value, the next observed normalizer after the lower cut value",
        "all_best_exact_two_segment_envelopes_contractive": True,
        "asymptotic_single_cut_theorem_proved": False,
        "all_exact_regressions_verified": True,
    }


def verify(ledger: dict) -> None:
    assert len(ledger["cases"]) == 3
    for case in ledger["cases"]:
        m = int(case["m"])
        expected = EXPECTED[m]
        value = Fraction(case["best_two_segment_envelope"])
        assert int(case["distinct_normalizers"]) == expected["distinct_normalizers"]
        assert list(case["best_cut_between_consecutive_observed_normalizers"]) == expected["cut"]
        assert value == expected["envelope"]
        assert int(case["maximizing_target_low_labels"]) == expected["low_labels"]
        assert int(case["maximizing_target_high_labels"]) == expected["high_labels"]
        assert int(case["maximizing_target_components"]) == expected["target_components"]
        assert int(case["maximizing_target_cycles_tied"]) == expected["target_cycles_tied"]
        assert Fraction(case["clean_upper_bound"]) == expected["clean_bound"]
        assert Fraction(case["margin_below_clean_upper_bound"]) == expected["clean_bound"] - value
        assert value < 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    parser.add_argument("--regenerate", action="store_true")
    parser.add_argument("--threads", type=int, default=8)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    ledger_path = root / "experiments/terminal-normalizer-exact-single-cut-through-m10-audit.json"
    if args.regenerate:
        ledger = regenerate(root, args.threads)
        output = args.output or ledger_path
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
    else:
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    verify(ledger)
    print("terminal exact single-cut profile verified")
    print("best envelopes: m8=2852/4521 m9=13760/14043 m10=415800/1535713")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
