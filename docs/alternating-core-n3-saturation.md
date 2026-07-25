# Exact `3 x 3` split-saturation exception

**Branch:** `research/alternating-core-chain`

AC3gv--AC3gy use the empty partner menu of a saturated pivot. AC3gs shows that the only saturated pivot with no empty partner is the split pattern at `n=3`. This note closes that finite exception exactly.

## Normal form

Relabel rows so the pivot layer is

$$
M_0=\{(0,0),(1,1),(2,2)\}
$$

with pivot `z=(0,0)`. The opposite layer is one of the two derangements

$$
b=(1,2,0)
\qquad\text{or}\qquad
b=(2,0,1).
$$

Both partner rectangles have blocker occupancy one. Apply the canonical AC3fs singleton repair to each partner.

Define

$$
A=\{(0,1),(1,0),(2,2)\},
$$

$$
B=\{(0,2),(1,1),(2,0)\}.
$$

## AC3gz -- exact two-choice union collapse -- PROVED

For either initial blocker derangement, the two canonical partner choices produce the layer states

$$
(A,B)
\qquad\text{and}\qquad
(B,A).
$$

Consequently both choices produce the same final union

$$
\boxed{A\cup B.}
$$

The two local states differ only by swapping the names of the permutation layers.

### Proof

There are only two normalized derangements. For `b=(1,2,0)`, partner `1` has the pivot-column cross blocked. Switching the active diagonal and transposing the blocker rows in columns `0,1` gives `(A,B)`. Partner `2` has the partner-column cross blocked; the unique outside column is `1`, and the canonical singleton transposition gives `(B,A)`.

For `b=(2,0,1)`, the two blocker roles are interchanged and the same two layer states occur in the opposite partner order. QED.

## Exact created support

Relative to either parent union, the common final union removes the pivot and one additional parent cell and inserts exactly two cells absent from the parent. Explicitly:

- for `b=(1,2,0)`, the new cells are `(1,0),(0,2)`;
- for `b=(2,0,1)`, the new cells are `(0,1),(2,0)`.

Thus every newly created union triple has created-cell rank one or two.

## AC3ha -- finite exception pivot continuation -- PROVED

Let the original saturated pivot bucket have private paid weight `W`. The common final union from AC3gz destroys the pivot and hence destroys the entire bucket.

Exactly one of the following holds.

1. The common final union creates total triple weight smaller than `W`, and it improves.
2. Its created triple weight is at least `W`. Orient those current created triples by AC3gg. For every `K>=1`, AC3gi returns an explicit overload or an executable pivot family with private payment at least
   $$
   \boxed{W/K.}
   $$
   If that pivot product fails, AC3gj returns one next-generation rank of expected weight at least
   $$
   \boxed{W/(3K).}
   $$

### Proof

AC3gz gives one common final union, so there is no unresolved choice. Both canonical local states remove the pivot from the union. The exact support audit above shows that every new certificate has rank one or two, although AC3gg--AC3gj require only that its rank be nonzero. The comparison and constants follow directly from AC3gi--AC3gj. QED.

## Consequence

Every full partner-saturation record now has a concrete continuation:

- for `n>=4`, AC3gv--AC3gy use the nonempty empty-partner menu;
- for `n=3`, AC3gz--AC3ha use the unique common final union.

The remaining global saturation issue is recurrence of the resulting row/column-arm pivots or same-role overload labels, not a missing local move.

## Finite check

`scripts/verify_ac_n3_saturation.py` exhausts both normalized derangements, both partner choices, the singleton blocker repairs, layer-swap identity, common final union, exact two-cell support change and the `1/K,1/(3K)` continuation constants.