# Created-cell rank for RI fixed closure and rectangle collateral

**Branch:** `research/alternating-core-chain`

AC3cc--AC3da classify every state-independent term in the closed I6 bank by closure cells, one universal two-closure crossed rectangle, or one exceptional `mh=2` transfer rectangle. Earlier frontier summaries described the remaining task as “payment for closure and transfer outputs.” That wording is incorrect. These objects are newly created collateral of an already paid failed bank; a boundary closure or transferred cell is not automatically a destroyed current defect. The correct next invariant is the pre-transition created-cell rank of AC3fa.

## Initial configuration

Let `M` be the union of the active and blocker permutation layers before the closed I6 transition. Every cell called **new** in AC3cc--AC3da lies outside `M`. Unchanged context cells lie in `M`.

For a state-independent new triple `C`, put

$$
\operatorname{nrk}_M(C)=|C\setminus M|.
$$

## AC3fe -- closure count equals created-cell rank -- PROVED

For the state-independent active closure term of AC3cc--AC3cg, a triple containing exactly `j` closure cells has

$$
\boxed{
\operatorname{nrk}_M(C)=j,
\qquad j\in\{1,2,3\}.
}
$$

Consequently the closure-count decomposition

$$
F_{\rm act}=F_1+F_2+F_3
$$

is exactly the AC3fa created-cell-rank decomposition, not a separate classification.

### Proof

Every closure cell in `Q` is inserted by the RI5f boundary closure and is absent from the pre-transition active layer. It is also disjoint from the current blocker layer after the legal closure construction, so it lies outside `M`. AC3cf shows that every other cell in a one- or two-closure triple is an unchanged current context cell. A three-closure triple has no other cells. Therefore the number of cells outside `M` is exactly the number of closure cells. QED.

The three geometric meanings are therefore canonical:

1. rank one: one closure cell completing a current context pair;
2. rank two: one closure-pair secant through a current context cell;
3. rank three: one all-new collinear closure triple.

## AC3ff -- total fixed term has an exact support-type/rank grid -- PROVED

Let the support type be one of

$$
\mathsf{cl},
\qquad
\mathsf{cr},
\qquad
\mathsf{tr},
$$

for active closure, universal closure-crossed rectangle and two-state transfer rectangle. For `k=1,2,3`, let `F_{s,k}` be the total weight of state-independent new triples of support type `s` and created-cell rank `k`.

Then

$$
\boxed{
F=
\sum_{s\in\{\mathsf{cl},\mathsf{cr},\mathsf{tr}\}}
\sum_{k=1}^3 F_{s,k}.
}
$$

If `F>=D`, one exact support-type/rank class has weight at least

$$
\boxed{D/9.}
$$

If only the rank is required, one created-cell rank has weight at least

$$
\boxed{D/3.}
$$

### Proof

AC3cy--AC3da partition every new union-fixed cell and every state-independent new triple by the three support mechanisms. AC3fa independently partitions every created triple by the number of cells outside the fixed initial union `M`. Intersecting the two partitions gives the nine classes. Weighted pigeonhole gives the bounds. QED.

For the pure active closure term, AC3fe removes the redundant support-type split and retains the sharper `F_act/3` closure-rank bound already present in AC3cd.

## AC3fg -- finite fixed-support literal alphabet -- PROVED

After normalized local roles are recorded, the fixed-support mechanisms use at most nine new-cell role labels:

1. one generic boundary-closure role `Q`, retaining its exact boundary-path address;
2. at most four normalized roles for a universal two-closure rectangle: two closure-anchor roles and two crossed-corner roles;
3. at most four normalized roles for the two-state transfer rectangle.

Thus one may use a combined role alphabet with

$$
\boxed{\ell_{\rm fixed}\le9.}
$$

For created-cell rank `k`, AC3fb therefore localizes one exact fixed-support role multiset with loss at most

$$
\boxed{
\binom{8+k}{k}.
}
$$

The three counts are

$$
\boxed{9,\ 45,\ 165}
$$

for ranks one, two and three.

Every selected occurrence retains the full exact data already recorded by AC3cg and AC3da: boundary-path endpoints, released row, closure cell, rectangle orientation, layer-transfer word, physical scale, channel labels and carry data.

### Proof

The normalized role lists are the finite corner/closure positions in AC3cf, AC3cz and AC3da. Different physical boundary paths or rectangles may reuse the same normalized role, which is why AC3fb uses multisets with repetition while preserving exact addresses on each occurrence. The multiset count is `binom(ell+k-1,k)` with `ell=9`. QED.

## AC3fh -- corrected payment and ticket interpretation -- PROVED

A state-independent closure, crossed-rectangle or transfer profile is collateral charged against the certified payment of the closed I6 bank which created it. It is not itself assigned a destroyed current-factor charge merely because it is geometrically explicit.

Therefore:

1. no Hall eligibility theorem is required for the closure cell or boundary path at the moment it is returned as collateral;
2. no reuse ticket is consumed merely by recording the collateral profile;
3. payment and ticketing are required only after a later executable transition is chosen to remove that profile;
4. such a later transition must identify an actual current certificate it destroys, exactly as AC3ey corrected the companion-anchor interpretation.

### Proof

The closed I6 comparison already accounts for the old paid factors destroyed by the bank and the newly created triples appearing in its states. A closure path is a matching-completion mechanism, not necessarily a current collinear certificate. Assigning it payment without a destroyed current factor would violate AC3f. Recording a failed-bank collateral class performs no state transition and cannot consume a no-recycling ticket. QED.

## Quantitative consequence

Suppose a failed closed I6 or multiscale product returns a state-independent term of weight `D_fixed`.

- One created-cell rank has weight at least `D_fixed/3`.
- One exact support-type/rank class has weight at least `D_fixed/9`.
- After a finite arithmetic profile split of size `L`, one exact support-type/rank/profile class has weight at least
  $$
  \boxed{D_{\rm fixed}/(9L).}
  $$
- For the active closure term alone, the corresponding bound remains the sharper
  $$
  \boxed{D_{\rm act}/(3L).}
  $$
  because closure count and rank coincide.

The remaining RI fixed-term work is termination of rank-one current-pair completions, rank-two current-centred secants and rank-three all-new tuples, together with their finite arithmetic overload labels. “Payment for a boundary closure” is no longer an open lemma.

## Finite check

`scripts/verify_ac_ri_fixed_term_rank_router.py` exhausts abstract closure/rectangle support words, verifies that closure count equals pre-transition new-cell rank, checks the nine support-type/rank partition, the `1/3` and `1/9` weighted bounds, and the role-multiset counts `9,45,165`.
