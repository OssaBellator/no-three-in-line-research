#!/usr/bin/env python3
"""Regenerate or verify contiguous terminal-normalizer coarsening profiles.

Regeneration instruments the already committed correlated-bin checker in a
temporary directory. It changes only the bin boundaries and replaces the
hard-coded regression main with a generic exact-output main.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import tempfile
from fractions import Fraction
from pathlib import Path

FINE_UPPER = {
    8: [2048, 4096, 8192],
    9: [4096, 8192, 16384, 32768],
    10: [16384, 32768, 65536, 131072],
}


def partitions(bin_count: int):
    for mask in range(1 << (bin_count - 1)):
        ends = [j for j in range(bin_count - 1) if (mask >> j) & 1]
        ends.append(bin_count - 1)
        yield mask, ends


def patch_part3(text: str, m: int, segment_ends: list[int]) -> str:
    upper = FINE_UPPER[m]
    chosen = [upper[index] for index in segment_ends]
    padded = chosen + [0] * (5 - len(chosen))
    replacement = f"bin_upper={{{','.join(map(str, padded))}}};bin_count={len(chosen)};"
    old = {
        8: "bin_upper={2048,4096,8192,0,0};bin_count=3;",
        9: "bin_upper={4096,8192,16384,32768,0};bin_count=4;",
        10: "bin_upper={16384,32768,65536,131072,0};bin_count=4;",
    }[m]
    if old not in text:
        raise RuntimeError("could not locate fine-bin definition")
    return text.replace(old, replacement)


def generic_part4(text: str) -> str:
    prefix = text[:text.index("int main(int argc,char**argv){")]
    return prefix + r'''
int main(int argc,char**argv){
  if(argc!=2){cerr<<"usage: checker m\n";return 2;}
  int m=atoi(argv[1]);Result r=run_case(m);
  cout<<"{\"m\":"<<m
      <<",\"bin_count\":"<<r.normalizer_bin_count
      <<",\"correlated_bin_envelope\":\""<<r.correlated_bin_num<<"/"<<r.correlated_bin_den<<"\""
      <<",\"correlated_bin_counts\":[";
  for(int j=0;j<r.normalizer_bin_count;j++)cout<<r.correlated_bin_counts[j]<<(j+1<r.normalizer_bin_count?",":"");
  cout<<"],\"target_components\":"<<r.correlated_bin_target_components
      <<",\"target_cycles_tied\":"<<r.correlated_bin_target_cycles_tied<<"}\n";
}
'''


def regenerate(root: Path, threads: int) -> dict:
    scripts = root / "scripts"
    cases = []
    with tempfile.TemporaryDirectory(prefix="terminal-coarsening-") as temp_name:
        temp = Path(temp_name)
        for name in (
            "terminal_normalizer_bin_envelope_part1.inc",
            "terminal_normalizer_bin_envelope_part2.inc",
            "terminal_normalizer_bin_envelope_part3.inc",
            "terminal_normalizer_bin_envelope_part4.inc",
            "check_terminal_normalizer_correlated_bin_envelope.cpp",
        ):
            shutil.copy2(scripts / name, temp / name)
        original_part3 = (temp / "terminal_normalizer_bin_envelope_part3.inc").read_text()
        original_part4 = (temp / "terminal_normalizer_bin_envelope_part4.inc").read_text()
        (temp / "terminal_normalizer_bin_envelope_part4.inc").write_text(generic_part4(original_part4))

        for m in (8, 9, 10):
            profile = []
            best_by_segments: dict[int, tuple[Fraction, dict]] = {}
            for mask, ends in partitions(len(FINE_UPPER[m])):
                (temp / "terminal_normalizer_bin_envelope_part3.inc").write_text(
                    patch_part3(original_part3, m, ends)
                )
                binary = temp / "checker"
                subprocess.run([
                    "g++", "-O3", "-std=c++17", "-Wall", "-Wextra",
                    "-pedantic", "-fopenmp",
                    str(temp / "check_terminal_normalizer_correlated_bin_envelope.cpp"),
                    "-o", str(binary),
                ], check=True, cwd=temp)
                output = subprocess.check_output(
                    [str(binary), str(m)],
                    cwd=temp,
                    env={**dict(os.environ), "OMP_NUM_THREADS": str(threads)},
                    text=True,
                )
                row = json.loads(output)
                value = Fraction(row["correlated_bin_envelope"])
                segments = len(ends)
                candidate = {
                    "segment_count": segments,
                    "cut_mask": mask,
                    "maximum_envelope": str(value),
                    "maximum_envelope_decimal": float(value),
                    "contractive": value < 1,
                    "maximizing_segment_counts": row["correlated_bin_counts"],
                    "target_components": row["target_components"],
                    "target_cycles_tied": row["target_cycles_tied"],
                }
                if segments not in best_by_segments or value < best_by_segments[segments][0]:
                    best_by_segments[segments] = (value, candidate)
            for segments in sorted(best_by_segments):
                profile.append(best_by_segments[segments][1])
            minimum = min(row["segment_count"] for row in profile if row["contractive"])
            cases.append({
                "m": m,
                "fine_bin_count": len(FINE_UPPER[m]),
                "coarsening_profile": profile,
                "minimum_contractive_segment_count": minimum,
            })
    return {"cases": cases}


def verify(ledger: dict) -> None:
    expected_minimum = {8: 2, 9: 3, 10: 1}
    expected = {
        (8, 1): Fraction(218, 137),
        (8, 2): Fraction(390310, 561289),
        (8, 3): Fraction(203200918, 383360387),
        (9, 1): Fraction(1429, 496),
        (9, 2): Fraction(279706, 253983),
        (9, 3): Fraction(3478755928, 4161511455),
        (9, 4): Fraction(148937290752, 183330241195),
        (10, 1): Fraction(560, 617),
        (10, 2): Fraction(6257720, 20218473),
        (10, 3): Fraction(348002942008, 1325058065001),
        (10, 4): Fraction(7972033929088, 35188130299905),
    }
    for case in ledger["cases"]:
        m = int(case["m"])
        assert int(case["minimum_contractive_segment_count"]) == expected_minimum[m]
        previous = None
        for row in case["coarsening_profile"]:
            key = (m, int(row["segment_count"]))
            value = Fraction(row["maximum_envelope"])
            assert value == expected[key]
            assert bool(row["contractive"]) == (value < 1)
            if previous is not None:
                assert value <= previous
            previous = value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    parser.add_argument("--regenerate", action="store_true")
    parser.add_argument("--threads", type=int, default=8)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    ledger_path = root / "experiments/terminal-normalizer-coarsening-profile-through-m10-audit.json"
    if args.regenerate:
        ledger = regenerate(root, args.threads)
        output = args.output or ledger_path
        with output.open("w", encoding="utf-8") as handle:
            json.dump(ledger, handle, indent=2)
            handle.write("\n")
    else:
        with ledger_path.open(encoding="utf-8") as handle:
            ledger = json.load(handle)
    verify(ledger)
    print("terminal normalizer coarsening profile verified")
    print("minimum segments: m8=2 m9=3 m10=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
