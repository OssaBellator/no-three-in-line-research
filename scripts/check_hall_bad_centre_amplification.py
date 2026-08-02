#!/usr/bin/env python3
from fractions import Fraction

GOOD_PER_MOTIF = 3
TOTAL_PER_MOTIF = 4
REQUIRED_GOOD = 28

def good_centres(motifs, extra_corruptions=0):
    return GOOD_PER_MOTIF * motifs - extra_corruptions

def minimum_motifs(extra_corruptions=0):
    return (REQUIRED_GOOD + extra_corruptions + GOOD_PER_MOTIF - 1) // GOOD_PER_MOTIF

assert minimum_motifs(0) == 10
assert good_centres(9) == 27
assert good_centres(10) == 30
assert minimum_motifs(1) == 10
assert minimum_motifs(2) == 10
assert minimum_motifs(3) == 11
assert good_centres(10,2) == 28
assert good_centres(10,3) == 27

rate_examples = {}
for rho in (Fraction(0), Fraction(1,4), Fraction(1,2), Fraction(1), Fraction(2)):
    if rho >= 3:
        continue
    threshold = Fraction(REQUIRED_GOOD,1) / (3-rho)
    smallest = (threshold.numerator + threshold.denominator - 1) // threshold.denominator
    while Fraction(3)*smallest - rho*smallest < REQUIRED_GOOD:
        smallest += 1
    rate_examples[str(rho)] = smallest
assert rate_examples == {"0":10,"1/4":11,"1/2":12,"1":14,"2":28}

for motifs in range(1,40):
    for extra in range(0,10):
        assert (TOTAL_PER_MOTIF*motifs >= REQUIRED_GOOD + motifs + extra) == (good_centres(motifs,extra) >= REQUIRED_GOOD)

print({
    "good_centres_per_source_motif": GOOD_PER_MOTIF,
    "total_centres_per_source_motif": TOTAL_PER_MOTIF,
    "required_good_centres": REQUIRED_GOOD,
    "exact_good_count_with_t_motifs_and_e_extra_corruptions": "3t-e",
    "exact_pool_condition": "3t-e >= 28",
    "minimum_motifs_without_extra_corruption": 10,
    "ten_motif_extra_corruption_tolerance": 2,
    "minimum_motifs_by_corruption_rate": rate_examples,
    "remaining_gap": "the asymptotic geometry must produce resource-disjoint motifs and bound cross-motif corruption of the good centre fibres",
    "evidence_level": "exact_bad_centre_amplification_interface",
    "status": "passed",
})
