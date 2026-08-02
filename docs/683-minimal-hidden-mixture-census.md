# Minimal hidden-mixture census

`docs/677` proves that the separator lower bound is algebraically sharp: three
copies of the hidden state `4I_4` and five legal score-zero states can average to
eight copies of the source. This chapter classifies every equal-weight equality
batch of that minimum size.

Let `F` be the set of 495 legal four-layer matrices on the separator facet. A
minimal equality batch is a multiset

```text
{L_1,...,L_5} subseteq F
```

satisfying

```text
3*(4I_4) + L_1+...+L_5 = 8S.
```

## PP3ddh — Exact number of minimal equality batches

There are exactly

```text
19,834
```

five-element multisets on the facet satisfying the equality equation.

The support-size histogram is

```text
2:       5,
3:     210,
4:   2,255,
5:  17,364.
```

In particular, no one-state exposed support works. Most equality witnesses use
five distinct legal matrices, but the equality face also contains five highly
compressed two-state witnesses.

## PP3ddi — Exact multiplicity partitions

The complete multiplicity-partition census is

```text
1+1+1+1+1: 17,364,
2+1+1+1:     2,255,
2+2+1:         175,
3+1+1:          35,
4+1:             5.
```

Thus every two-support solution has multiplicities `4+1`, and there are exactly
five such compressed batches. There is no `3+2` solution and no fivefold repeat
of one legal state.

This gives a finite menu of algebraic endpoint profiles for any future geometric
hidden primitive. It does not make any profile executable.

## PP3ddj — Meet-in-the-middle exact audit

`scripts/check_threshold_minimal_hidden_mixture_census.cpp` reconstructs the
eighteen legal permutation layers, all 4,475 legal four-layer matrices, and the
495 facet matrices. It forms all 12,870 distinct pair sums and matches them against
nondecreasing triples whose total is

```text
8S-3*(4I_4).
```

The ordering condition counts each multiset exactly once. The checker verifies the
19,834 total, the support histogram, and every multiplicity partition above.

## Evidence boundary

The sharp hidden mass is not unique algebraically, but every equality witness
still requires three hidden copies of `4I_4`. No coordinate construction realizes
that hidden state, exposes the five legal endpoints in a compatible order, or
repeats the eight-state batch without creating geometric defects.
