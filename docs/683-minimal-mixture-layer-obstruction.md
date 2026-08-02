# Minimal-mixture layer obstruction

The algebraically sharp threshold witness in `docs/677` uses three copies of the
hidden state `4I_4` and five exposed score-zero facet matrices. This chapter
classifies their primitive permutation-layer decompositions and proves that the
hidden phase cannot be concealed by a cyclic four-layer exposure window.

Let `I=(0,1,2,3)` be the identity permutation layer and let

```text
P1=(2,3,0,1),
P2=(2,1,3,0),
P3=(1,3,2,0),
P4=(1,2,0,3),
P5=(0,2,3,1).
```

## PP3ddh — Unique primitive decompositions

Each exposed witness matrix `Li` from `docs/677` has the unique permutation-layer
decomposition

```text
Li = Pi + Pi + Pi + Pi.
```

All five `Pi` are legal no-three-in-line permutation layers and are pairwise
distinct. Consequently the five exposed matrices have no common primitive layer.

The hidden matrix has the unique decomposition

```text
4I_4 = I + I + I + I.
```

The identity permutation is illegal because its four points are collinear. Thus
there is no alternative legal Birkhoff decomposition of the hidden endpoint.

## PP3ddi — Primitive eight-layer identity

Dividing the eight-state matrix identity by four gives the sharper primitive
identity

```text
3I + P1 + P2 + P3 + P4 + P5 = 2S.
```

Therefore the minimum hidden mixture consists, at primitive layer scale, of three
illegal identity layers and five legal witness layers. The separator mass cannot
be redistributed among different hidden permutation types at equality: the score
minimum forces the identity layer.

## PP3ddj — No legal cyclic four-window realization

Consider the multiset

```text
{I,I,I,P1,P2,P3,P4,P5}.
```

There are thirty admissible four-layer submultisets respecting these
multiplicities. Exactly five are legal four-layer matrices: the five subsets that
contain four distinct `Pi` layers and no identity layer. Every submultiset
containing one, two, or three identity layers lies outside the complete catalogue
of 4,475 legal four-layer matrices.

There are `8!/3!=6,720` cyclically labelled orderings of the primitive multiset.
For each ordering, inspect all eight cyclic windows of four consecutive layers.
The exact histogram of the number of legal windows is

```text
0:3,840, 1:1,920, 2:960.
```

In particular, no ordering has more than two legal windows, and none has all
windows legal. A rolling four-layer schedule therefore cannot hide the identity
phase of the minimal mixture.

`scripts/check_threshold_hidden_layer_windows.py` reconstructs all 24 permutation
layers, all eighteen legal layers, all 4,475 legal four-layer matrices, the unique
decompositions, all thirty admissible submultisets, and all 6,720 cyclic orders.

## Evidence boundary

This is an exact obstruction for the algebraically minimal three-hidden/five-legal
mixture. A geometric threshold mechanism must use a larger memory window, a state
outside the present four-layer transportation model, or a genuinely unexposed
operation that prevents every identity-containing four-window from becoming an
endpoint. No such primitive or recurrence is currently known.
