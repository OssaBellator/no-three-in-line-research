#!/usr/bin/env python3

REQUIRED_GOOD = 28
GOOD_PER_MOTIF = 3

def selected_motifs(candidate_motifs, overlap_degree):
    return (candidate_motifs + overlap_degree) // (overlap_degree + 1)

def required_selected_motifs(matching_bound):
    return (REQUIRED_GOOD + matching_bound + GOOD_PER_MOTIF - 1) // GOOD_PER_MOTIF

def minimum_candidates(overlap_degree, matching_bound):
    selected = required_selected_motifs(matching_bound)
    return (selected - 1) * (overlap_degree + 1) + 1

def retained_good(candidate_motifs, overlap_degree, matching_bound):
    return GOOD_PER_MOTIF * selected_motifs(candidate_motifs, overlap_degree) - matching_bound

for degree in range(8):
    for matching in range(10):
        threshold = minimum_candidates(degree, matching)
        assert retained_good(threshold, degree, matching) >= REQUIRED_GOOD
        assert retained_good(threshold - 1, degree, matching) < REQUIRED_GOOD

assert {m: minimum_candidates(2,m) for m in (0,2,3,5,6)} == {0:28,2:28,3:31,5:31,6:34}
assert retained_good(28,2,2) == 28
assert retained_good(28,2,3) == 27
assert retained_good(31,2,5) == 28
assert retained_good(31,2,6) == 27

print({
    "motif_overlap_graph": "maximum degree Delta",
    "resource_disjoint_motifs": "ceil(M/(Delta+1))",
    "centre_conflict_graph": "H",
    "exact_retainable_good_centres": "3*ceil(M/(Delta+1))-tau(H)",
    "bipartite_reduction": "tau(H)=nu(H)",
    "required_selected_motifs_under_matching_bound_m": "ceil((28+m)/3)",
    "sharp_candidate_threshold": "(ceil((28+m)/3)-1)*(Delta+1)+1",
    "degree_two_examples": {"m=0":28,"m=2":28,"m=3":31,"m=5":31,"m=6":34},
    "sharpness": "motif cliques K_(Delta+1) plus a centre-conflict matching",
    "remaining_gap": "the conditional host must realize both graph certificates and both degree-two restrictions geometrically",
    "evidence_level": "exact_two_level_hall_packing_interface",
    "status": "passed",
})
