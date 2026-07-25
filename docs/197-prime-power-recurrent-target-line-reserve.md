# Recurrent target lines consume a simultaneous full-envelope line reserve

CMR698--CMR747 reduce repeated target motion to owner-labelled entering cells,
returned-edge deletion or contraction, and finite unit-wall factorisation. A
recurrent cell-target pair also fixes one real line. Inside a closure envelope,
that line can be protected directly: rematch the complete layer over the
envelope while forbidding all board cells on every protected nonaxis line.

The matching existence threshold is exact at the degree level. Old cells and the
opposite permutation layer contribute forbidden degree at most two. Every
nonaxis real line contributes at most one forbidden cell in each matching-board
row and column. Thus `r` protected lines give total forbidden degree at most
`r+2`, and Hall applies whenever the envelope side `q` satisfies

\[
q\ge2r+4.
\]

Fix one closure envelope `E` of side `q`. In one permutation layer, take all `q`
selected points whose columns lie in `E`. Their current row set also has size
`q`, giving a balanced `q` by `q` rematching board.

## 1. Universal degree-r protected-line matching

Let `F_0` be the old selected matching on the board and let `F_1` be the cells
occupied by the opposite layer which lie in the same board. Let

\[
\mathcal L=\{L_1,\ldots,L_r\}
\]

be distinct nonaxis real lines. For each line, forbid every board cell lying on
that line.

### Theorem CMR748 -- PROVED

If

\[
\boxed{q\ge2r+4,}
\]

then the allowed board has a perfect matching. Every such matching

1. avoids every old cell in `F_0` and therefore moves all `q` selected points;
2. avoids the opposite-layer cells `F_1` and preserves layer disjointness;
3. selects no board cell on any line in `mathcal L`;
4. preserves the layer row and column sets and hence saturation.

### Proof

The sets `F_0` and `F_1` are matchings or partial matchings, so their union has
row and column degree at most two. A nonaxis real line meets each grid column and
each grid row in at most one cell, so its intersection with the board is a
partial matching. The union of `r` protected line intersections has degree at
most `r`.

Hence every vertex of the allowed bipartite graph has degree at least

\[
q-r-2\ge q/2.
\]

The Hall argument of CMR128 applies: a balanced bipartite graph with minimum
degree at least half its side has a perfect matching. The four conclusions are
exactly the forbidden-cell conditions and the row-column matching property. ∎

The theorem allows arbitrary overlaps among the protected lines; overlaps only
lower forbidden degree.

## 2. Exact simultaneous protected-line capacity

Define

\[
R(q)=\max\{r\ge0:q\ge2r+4\}
=\left\lfloor\frac{q-4}{2}\right\rfloor.
\]

### Theorem CMR749 -- PROVED

Every envelope board of side `q` admits a complete-layer rematching which
simultaneously avoids any prescribed family of at most

\[
\boxed{R(q)=\left\lfloor\frac{q-4}{2}\right\rfloor}
\]

nonaxis real lines, in addition to the old and opposite-layer matchings.

For `q>=6`, at least one complete target line can always be protected.

### Proof

Substitute `r<=R(q)` into CMR748. The final assertion is `R(q)>=1` exactly when
`q>=6`. ∎

This is a linear reserve in the envelope side.

## 3. Full-envelope target-line handoff

Let `T` be a current internal real triple whose point columns all lie in `E`, and
let `L(T)` be its real line. Choose one cell `e` of `T` and the permutation layer
containing it. No real triple in a saturated state is horizontal or vertical,
because every grid row and column contains only two selected points, so `L(T)`
is nonaxis.

### Theorem CMR750 -- PROVED

Let `mathcal L` be a previously protected family not containing `L(T)`. If

\[
|\mathcal L|+1\le R(q),
\]

then there is a complete-layer bank over `E` such that every bank state

1. moves `e` and destroys `T`;
2. moves every point of the chosen layer over `E`;
3. selects no chosen-layer board cell on any line in
   `mathcal L\cup\{L(T)\}`;
4. preserves saturation, layer disjointness, and the closure-envelope row set.

### Proof

Apply CMR748 to the protected line family `mathcal L\cup\{L(T)\}`. The old cell
`e` is forbidden by `F_0`, so `T` is destroyed. CMR172 preserves the inherited
row set because the rematching is internal to `E`. ∎

This bank protects the line inside the complete moved layer board; it does not
claim that points in the other layer or outside the envelope are globally absent
from the line.

## 4. Reappearance on a protected line is entering-edge payment

Suppose a target `T` on a line `L` has been destroyed by a bank which protected
`L`. If a later internal state in the same envelope contains the same physical
target again, take its first recreation transition.

### Theorem CMR751 -- PROVED

At least one cell of `T` is an entering selected edge on the already protected
line `L`. Therefore every recreation of an existing protected target line pays

1. one entering-edge occurrence on that line;
2. exact labelled nonroot full-token incidence `(p+1)(h-1)` for that edge;
3. the target-cell reintroduction ledger CMR707--CMR710.

### Proof

CMR707 gives an entering cell of `T` at its first recreation transition. Every
cell of `T` lies on `L`. The token and reintroduction charges are CMR413 and
CMR710. ∎

Thus a repeated protected line is not charged as a fresh reserve line.

## 5. Growing reserve or exact saturation

Run a target-driven closure inside one fixed envelope. Whenever the current
target line is new, append it to the protected family and use CMR750 while the
capacity condition holds.

### Theorem CMR752 -- PROVED

Before one of the following endpoints occurs, at most `R(q)` distinct target
lines are added.

1. A bank state strictly lowers the triple potential.
2. A target line already in the protected family recurs and pays CMR751.
3. A crossing target spends a strict envelope expansion by CMR193.
4. The protected family reaches size
   
   \[
   \boxed{R(q)+1,}
   \]
   
   giving a linear family of distinct internal target-line signatures beyond the
   simultaneous-avoidance capacity of CMR748.

### Proof

Every genuinely new line increases the family size by one. CMR750 remains
available through size `R(q)`. Existing-line recurrence is CMR751, and crossing
targets are handled before the internal bank by CMR193. ∎

The fourth branch is a protected-line reserve saturation certificate, not a
claim that no matching avoiding those lines exists by some stronger theorem.

## 6. Dyadic localization of a saturated line reserve

Every internal nonaxis line in an envelope of side `q` has a primitive direction
height between one and `q-1` after dividing the common prefix spacing.

### Theorem CMR753 -- PROVED

If the reserve saturation branch of CMR752 occurs, some dyadic primitive-height
band contains at least

\[
\boxed{
\left\lceil
\frac{R(q)+1}{\lceil\log_2 q\rceil}
\rightceil
}
\]

distinct protected target-line signatures.

### Proof

There are at most `ceil(log_2 q)` dyadic bands covering heights `1,...,q-1`.
Partition the `R(q)+1` distinct lines by band and average. ∎

This feeds the existing line-energy, low-height, quotient, carry-cell, and
matching-vertex wall machinery without losing the target-line owner.

## 7. Envelope-chain protected-line endpoint

A closure branch has at most `h+1` envelope epochs and at most `h` strict
expansions in a parent of side `N=p^h`.

### Corollary CMR754 -- PROVED

Every target-line-driven prime-power closure reaches at least one of:

1. a strict triple-potential improvement;
2. an existing protected line recreated through an entering edge, with exact
   token and target-cell reintroduction payment;
3. a fixed-envelope protected reserve of `R(q)+1` distinct target lines, with the
   dyadic concentration CMR753;
4. one of the at most `h` strict closure-envelope expansions;
5. a finite small-envelope case with `q<6`;
6. the deletion, contraction, product-factorisation, or finite owner-stock
   alternatives CMR713--CMR747.

If no epoch saturates and no protected line recurs, the total number of new
protected target lines over the branch is at most

\[
\boxed{
\sum_{E}R(|E|)
\le
(h+1)\left\lfloor\frac{N-4}{2}\right\rfloor.
}
\]

Thus the recurrent target-edge frontier now enters an explicit protected-line
reserve: recurrence pays entering-edge churn, while novelty consumes a finite
linear line capacity and then yields a height-localised line family.

### Proof

Apply CMR752 in each envelope epoch, CMR751 to repeated lines, CMR753 at
saturation, and CMR174--CMR175 to the envelope chain. The final structural branch
uses the indexed target-edge and unit-wall endpoints. ∎

No all-`n` theorem is claimed. Degree bounds, Hall existence, reserve capacity,
recurrence payment, and dyadic arithmetic are checked in
[`scripts/verify_prime_power_recurrent_target_line_reserve.py`](../scripts/verify_prime_power_recurrent_target_line_reserve.py).
