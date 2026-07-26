# Marked high-support source diagnostic

Run

```text
python scripts/check_marked_high_support_source.py \
  experiments/marked-high-support-source-example.json
```

The stored instance uses

```text
N=40,
b=6,
tau=0.05
```

and the complete `k`-uniform link on the other 39 endpoint indices for each source
class.

The exact output is

```text
N 40
b 6
tau 0.05
p_P 0.000054710581
p_4 0.000018236860
p_5 0.000001013159
p_6 0.000000028947
combined support expectation 0.766666666667
anchored_pair signatures 9139
anchored_pair density threshold 228.475
anchored_pair fixed core size 2
anchored_pair petal count 37
anchored_pair theorem lower bound 3.485
rank4_triple signatures 9139
rank4_triple density threshold 685.425
rank4_triple fixed core size 2
rank4_triple petal count 37
rank4_triple theorem lower bound 3.485
rank5_triple signatures 82251
rank5_triple density threshold 12337.650
rank5_triple fixed core size 3
rank5_triple petal count 36
rank5_triple theorem lower bound 0.706
rank6_triple signatures 575757
rank6_triple density threshold 431817.750
rank6_triple fixed core size 4
rank6_triple petal count 35
rank6_triple theorem lower bound 0.118
outcome marked_high_support_source_sunflowers
```

The four probabilities are the exact cancellations from PP3amr.  Their combined
expectation exceeds the residual-slack threshold, and every complete link exceeds
its PP3amt density lower bound.

The recursive decomposition repeatedly takes a high-degree link.  It terminates
in fixed-resource pencils whose residual singleton petals are pairwise disjoint:

- two fixed resources for the rank-four links;
- three for the rank-five link;
- four for the rank-six link.

The checker verifies the general `E^(1/k)/k!` lower bound at every rank, not merely
the stronger counts specific to complete hypergraphs.
