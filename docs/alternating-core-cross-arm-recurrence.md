# Cross-arm pivot exposure and old-axis saturation

**Branch:** `research/alternating-core-chain`

AC3gx--AC3gy turn every nonimproving saturated empty-partner menu into one heavy created-cell rank on one fixed row or column arm. The target pivots in that arm are distinct physical cells. This note adds those pivot addresses to the exposure potential. A heavy arm therefore gives either a quantitatively heavy new pivot cell or an exact historical old-axis saturation fan.

## Weighted arm records

Retain the AC3gx setup. There are `m>0` empty partner states. One fixed arm/rank class has target weights

$$
w_c\ge0
\qquad(c\in E_z)
$$

with

$$
\boxed{
\sum_{c\in E_z}w_c\ge\frac{mW}{4}.
}
$$

Every target with positive `w_c` has one oriented pivot cell `p_c`:

- on the column arm, `p_c=X_c=(c_0,r_c)`;
- on the row arm, `p_c=Y_c=(c,r_0)`.

## AC3hb -- exact distinct axis pivots -- PROVED

Within one arm, the physical pivot cells `p_c` are pairwise distinct. They all lie on one fixed grid column or one fixed grid row through the original pivot.

### Proof

For the column arm, the pivot-layer rows `r_c` are distinct because that layer is a permutation, so the cells `(c_0,r_c)` are distinct. For the row arm, the partner columns `c` are distinct, so the cells `(c,r_0)` are distinct. QED.

## New and old pivot cells

Let `E_cell` be the set of physical pivot cells already exposed during the current closure attempt. Partition the arm targets into

$$
T_{\rm new}=\{c:p_c\notin E_{\rm cell}\},
$$

$$
T_{\rm old}=\{c:p_c\in E_{\rm cell}\}.
$$

Put

$$
W_{\rm new}=\sum_{c\in T_{\rm new}}w_c,
\qquad
W_{\rm old}=\sum_{c\in T_{\rm old}}w_c.
$$

## AC3hc -- heavy new pivot or old-axis saturation -- PROVED

Exactly one of the following quantitative alternatives can be selected.

1. **Heavy new pivot.** `W_new` is at least half of the arm weight. Then one target `c in T_new` satisfies
   $$
   \boxed{
   w_c\ge\frac W8.
   }
   $$
2. **Old-axis saturation.** `W_old` is more than half of the arm weight. Then the distinct previously exposed pivot cells on one fixed row or column carry total raw weight
   $$
   \boxed{
   W_{\rm old}\ge\frac{mW}{8}.
   }
   $$

The old-axis record retains the original pivot, fixed arm, created-cell rank, all target cells, target weights, fused/split blocker type, exact line/source/channel/closure/blocker decoration and the retained arithmetic role.

### Proof

The new and old target weights partition the arm weight, which is at least `mW/4`. If the new part is at least half, it is at least `mW/8`; averaging over at most `m` targets gives one weight at least `W/8`. Otherwise the old part is greater than half and hence at least `mW/8`. Distinctness is AC3hb. QED.

## AC3hd -- new-axis-pivot continuation -- PROVED

In the heavy-new-pivot alternative, fix the realizing target state and its current certificate class of weight at least `W/8`. Add its pivot cell to `E_cell` and apply AC3gi--AC3gj. For every `K>=1`, one of the following holds.

1. AC3fr returns an explicit role-labelled overload at the new axis pivot.
2. An executable union-safe pivot family has private payment at least
   $$
   \boxed{
   \frac{W}{8K}.
   }
   $$
3. A failed pivot product returns one next-generation created-cell rank of expected weight at least
   $$
   \boxed{
   \frac{W}{24K}.
   }
   $$

### Proof

AC3hc gives a legal state with current certificate weight at least `W/8` at a previously unexposed pivot cell. AC3gi retains a `1/K` fraction or returns an overload. AC3gj loses a further factor `1/3` on failure. QED.

## AC3he -- combined support, signature and pivot-cell potential -- PROVED

Fix one finite AC2d object universe `O` of size

$$
N=|\mathcal O|.
$$

Let `E_sig` be the exposed decorated pivot-signature set in any fixed finite signature universe `Sigma`, and let `E_cell` be the exposed physical pivot-cell set. During one epoch allow only:

1. a strict labelled AC2d support descent;
2. a transition exposing a new decorated pivot signature;
3. a transition exposing a new physical pivot cell;
4. a terminal improvement, compatible bank, overload output, carry/BDA/RI delegation, affine output, full line saturation or old-axis saturation.

Then

$$
\boxed{
\Xi_{\rm axis}(U,E_{\rm sig},E_{\rm cell})
=
N\bigl(|E_{\rm sig}|+|E_{\rm cell}|\bigr)+N-|U|
}
$$

increases by at least one at every nonterminal transition and satisfies

$$
\boxed{
0\le\Xi_{\rm axis}
\le
N\bigl(|\Sigma|+n^2\bigr)+N-1.
}
$$

Thus such an epoch has at most

$$
\boxed{
N\bigl(|\Sigma|+n^2\bigr)+N-1
}
$$

nonterminal steps.

### Proof

A support descent increases `N-|U|`. A new signature or new pivot cell increases the exposure term by `N`; replacing one nonempty support by another can reduce `N-|U|` by at most `N-1`, so the net increase is at least one. There are at most `|Sigma|` signatures and `n^2` physical pivot cells. QED.

## The `3 x 3` exception

AC3ha produces one common final union with at most two new pivot cells. If the final union is nonimproving, orient its created triples. Splitting by created-cell rank and the at most two new pivot addresses gives one class of weight at least `W/4`. The same new/old cell partition therefore yields either:

- a new pivot continuation at scale `W/(4K)` and failed return `W/(12K)`; or
- an old-cell recurrence record of weight at least `W/4`.

No separate infinite local menu occurs at `n=3`.

## Consequence

Cross-arm pivot recurrence is now finite until one exact output occurs:

- a compatible/improving pivot bank;
- an explicit same-role overload;
- a new decorated signature;
- a new physical pivot cell;
- a full line-partner saturation record;
- or an old-axis saturation fan on one fixed row or column.

The remaining global no-recycling frontier is classification of the last two historical saturation records and the same-role overloads they retain. Local pivot existence, payment, partner saturation and new-cell exposure are no longer open.

## Finite check

`scripts/verify_ac_cross_arm_recurrence.py` exhausts small weighted arm records, every partition into new and old pivot cells, the `W/8`, `mW/8`, `W/(8K)`, `W/(24K)` constants and every transition inequality for `Xi_axis`.