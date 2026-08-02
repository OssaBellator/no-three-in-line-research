# Minimal hidden-mixture census and layer obstruction

`docs/677` proves that the separator lower bound is algebraically sharp: three
copies of hidden state `4I_4` and five legal score-zero states can average to eight
copies of the source. This chapter classifies every minimum equality batch and its
primitive layer content.

Let `F` be the 495 legal four-layer matrices on the separator facet. A minimum
equality batch is a multiset

```text
{L_1,...,L_5} subseteq F
```

satisfying

```text
3*(4I_4) + L_1+...+L_5 = 8S.
```

## PP3ddh — Exact matrix-level equality census

There are exactly

```text
19,834
```

five-element facet multisets satisfying the equality equation. Their support-size
histogram is

```text
2:       5,
3:     210,
4:   2,255,
5:  17,364.
```

The complete multiplicity-partition census is

```text
1+1+1+1+1: 17,364,
2+1+1+1:     2,255,
2+2+1:         175,
3+1+1:          35,
4+1:             5.
```

Thus the minimum equality witness is highly nonunique at the four-layer matrix
level, although every witness still uses three hidden copies of `4I_4`.

## PP3ddi — Unique aggregate primitive-layer content

At permutation-layer scale, the target `8S` contains 32 layers and has separator
score `-24`. Legal layers have score at least zero, while every illegal layer has
score at least `-2`. Hence at least twelve illegal layers are necessary. The
identity permutation

```text
I=(0,1,2,3)
```

is the unique layer of score `-2`, so equality forces twelve identity layers and
twenty legal score-zero layers.

After subtracting the twelve identities, the exact integer count problem on the
nine legal score-zero permutation types has a unique solution: four copies of each
of

```text
P1=(2,3,0,1),
P2=(2,1,3,0),
P3=(1,3,2,0),
P4=(1,2,0,3),
P5=(0,2,3,1),
```

and zero copies of the other four types. Therefore all 19,834 matrix-level batches
have the same aggregate primitive content. Dividing multiplicities by four gives

```text
3I + P1 + P2 + P3 + P4 + P5 = 2S.
```

The identity layer is illegal because its four points are collinear.

## PP3ddj — No cyclic four-window concealment

Consider the primitive multiset

```text
{I,I,I,P1,P2,P3,P4,P5}.
```

Among its thirty admissible four-layer submultisets, exactly five are legal: the
subsets containing four distinct `Pi` layers and no identity. Every submultiset
containing an identity lies outside the complete 4,475-matrix legal catalogue.

There are `8!/3!=6,720` cyclically labelled orderings. Inspecting all eight cyclic
windows of four consecutive layers gives the exact histogram

```text
0 legal windows: 3,840 orderings,
1 legal window:  1,920 orderings,
2 legal windows:   960 orderings.
```

No ordering has more than two legal windows, so a rolling four-layer schedule
cannot conceal the minimum identity phase.

## Verification

- `scripts/check_threshold_minimal_hidden_mixture_census.cpp` uses exact
  meet-in-the-middle enumeration to verify all 19,834 matrix batches and their
  support/multiplicity histograms.
- `scripts/check_threshold_minimal_layer_decomposition.py` proves the twelve-layer
  lower bound and the unique aggregate legal-layer count vector.
- `scripts/check_threshold_hidden_layer_windows.py` checks all primitive
  submultisets and all 6,720 cyclic orders.

## Evidence boundary

The minimum hidden mass is nonunique at endpoint level but rigid at aggregate layer
level, and every minimum execution contains twelve collinear identity layers. No
coordinate construction hides those layers, enlarges the memory safely, or repeats
the batch as an all-length recurrence.
