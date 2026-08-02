#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory() as directory:
    directory = Path(directory)
    outputs = {}
    for stem in ("check_prefix_13_to_14_neighbourhood","check_prefix_14_two_swap_neighbourhood"):
        source = HERE / f"{stem}.cpp"
        binary = directory / stem
        subprocess.run(["c++","-O3","-std=c++17",str(source),"-o",str(binary)],check=True)
        outputs[stem] = subprocess.run([str(binary)],check=True,capture_output=True,text=True)

first = outputs["check_prefix_13_to_14_neighbourhood"]
assert "checked=23273 best=3" in first.stderr
assert "hist 3:1 4:5 5:26" in first.stderr
assert first.stdout.splitlines() == [
    "P 9 4 7 13 0 1 12 8 11 10 2 6 5 3",
    "Q 7 12 9 11 4 3 8 13 2 1 5 10 6 0",
]

second = outputs["check_prefix_14_two_swap_neighbourhood"]
assert "checked 25229 best 3" in second.stderr
assert second.stdout == first.stdout

print({
    "base_thirteen_pair_source": "docs/642 canonical witness",
    "insertion_and_at_most_one_transposition_candidates": 23273,
    "no_three_candidates_in_first_neighbourhood": 0,
    "minimum_collinear_triples": 3,
    "minimum_candidates": 1,
    "valid_ordered_move_sequences_of_length_at_most_two_from_minimum": 25229,
    "minimum_after_second_neighbourhood": 3,
    "conclusion": "the canonical thirteen-pair witness cannot be extended to fourteen pairs by one row-column insertion plus one layer transposition, nor repaired from its unique minimum by two further transpositions",
    "remaining_gap": "a fourteen-pair source requires a nonlocal rearrangement or a different source family",
    "evidence_level": "exact_local_extension_obstruction_at_fourteen_pairs",
    "status": "passed",
})
