#!/usr/bin/env python3
from fractions import Fraction

REQUIRED_GOOD = 28
GOOD_PER_MOTIF = 3

def selected_motifs(candidate_motifs, overlap_degree):
    return (candidate_motifs + overlap_degree) // (overlap_degree + 1)

def guaranteed_good(candidate_motifs, overlap_degree, extra_corruptions=0):
    return GOOD_PER_MOTIF * selected_motifs(candidate_motifs, overlap_degree) - extra_corruptions

def required_selected(extra_corruptions=0):
    return (REQUIRED_GOOD + extra_corruptions + GOOD_PER_MOTIF - 1) // GOOD_PER_MOTIF

def minimum_candidates(overlap_degree, extra_corruptions=0):
    q = required_selected(extra_corruptions)
    return (q - 1) * (overlap_degree + 1) + 1

for degree in range(8):
    threshold = minimum_candidates(degree)
    assert guaranteed_good(threshold, degree) >= REQUIRED_GOOD
    assert guaranteed_good(threshold - 1, degree) < REQUIRED_GOOD

assert {d: minimum_candidates(d) for d in range(5)} == {0:10,1:19,2:28,3:37,4:46}
assert minimum_candidates(2, 0) == 28
assert minimum_candidates(2, 2) == 28
assert minimum_candidates(2, 3) == 31

rate_examples = {}
for rho in (Fraction(0), Fraction(1,4), Fraction(1,2), Fraction(1), Fraction(2)):
    q = Fraction(REQUIRED_GOOD, 1) / (3-rho)
    q = (q.numerator + q.denominator - 1) // q.denominator
    rate_examples[str(rho)] = {
        "selected_motifs": q,
        "candidate_motifs_at_overlap_degree_two": (q-1)*3+1,
    }
assert rate_examples["0"] == {"selected_motifs":10,"candidate_motifs_at_overlap_degree_two":28}
assert rate_examples["1"] == {"selected_motifs":14,"candidate_motifs_at_overlap_degree_two":40}
assert rate_examples["2"] == {"selected_motifs":28,"candidate_motifs_at_overlap_degree_two":82}

print({
    "candidate_overlap_graph_maximum_degree": "Delta",
    "guaranteed_resource_disjoint_motifs": "ceil(M/(Delta+1))",
    "guaranteed_good_centres_after_e_corruptions": "3*ceil(M/(Delta+1))-e",
    "exact_required_selected_motifs": "ceil((28+e)/3)",
    "sharp_minimum_candidate_motifs": "(ceil((28+e)/3)-1)*(Delta+1)+1",
    "degree_two_examples": {"e=0":28,"e=2":28,"e=3":31},
    "corruption_rate_examples": rate_examples,
    "sharpness_model": "disjoint unions of cliques K_(Delta+1)",
    "remaining_gap": "the conditional host must generate a motif family with bounded resource-overlap degree and retain the source and host-defect degree-two restrictions on the selected centres",
    "evidence_level": "exact_bounded_overlap_hall_packing_interface",
    "status": "passed",
})
