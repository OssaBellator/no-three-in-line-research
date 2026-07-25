# Recurrent target lines consume a simultaneous full-envelope line reserve

CMR698--CMR747 reduce repeated target motion to owner-labelled entering cells,
returned-edge deletion or contraction, and finite unit-wall factorisation. A
recurrent cell-target pair also fixes one real line. Inside a closure envelope,
that line can be protected directly by rematching the complete layer while
forbidding every board cell on each protected nonaxis line.

Old cells and the opposite permutation layer contribute forbidden degree at
most two. Every nonaxis line contributes degree at most one. Thus `r` protected
lines have total forbidden degree at most `r+2`, and Hall applies whenever

\[
q\ge2r+4.
\]

Fix one closure envelope `E` of side `q`. In one permutation layer, take all `q`
selected points whose columns lie in `E`; their current row set also has size
`q`, giving a balanced rematching board.

## 1. Universal protected-line matching

Let `F_0` be the old selected matching, let `F_1` be the opposite-layer cells
which lie in the board, and let

\[
\mathcal L=\{L_1,\ldots,L_r\}
\]

be distinct nonaxis real lines. Forbid every board cell on those lines.

### Theorem CMR748 -- PROVED

If

\[
\boxed{q\ge2r+4,}
\]

then the allowed board has a perfect matching. Every such matching

1. avoids all old cells and moves all `q` selected points;
2. avoids opposite-layer cells and preserves layer disjointness;
3. selects no board cell on a protected line;
4. preserves the layer row and column sets and hence saturation.

### Proof

`F_0` and `F_1` are matchings or partial matchings, so they contribute degree at
most two. A nonaxis line meets each grid row and column at most once, so its board
intersection is a partial matching. Every allowed vertex therefore has degree at
least

\[
q-r-2\ge q/2.
\]

The Hall argument of CMR128 gives a perfect matching. The four properties are the
forbidden-cell and row-column conditions. ∎

Line overlaps only reduce forbidden degree.

## 2. Exact simultaneous capacity

Define

\[
R(q)=\max\{r\ge0:q\ge2r+4\}
=\left\lfloor\frac{q-4}{2}\right\rfloor.
\]

### Theorem CMR749 -- PROVED

Every envelope board of side `q` can simultaneously avoid any prescribed family
of at most

\[
\boxed{R(q)=\left\lfloor\frac{q-4}{2}\right\rfloor}
\]

nonaxis lines in addition to the old and opposite-layer matchings. For `q>=6`,
at least one complete target line can always be protected.

### Proof

Substitute `r<=R(q)` into CMR748. ∎

## 3. Full-envelope target-line handoff

Let `T` be a current internal real triple with all point columns in `E`, and let
`L(T)` be its line. Choose a cell `e` of `T` and its permutation layer. The line
is nonaxis because a saturated state contains only two selected points in each
grid row and column.

### Theorem CMR750 -- PROVED

Let `mathcal L` be a previously protected family not containing `L(T)`. If

\[
|\mathcal L|+1\le R(q),
\]

there is a complete-layer bank over `E` such that every state

1. moves `e` and destroys `T`;
2. moves every chosen-layer point over `E`;
3. selects no chosen-layer board cell on any line in
   `mathcal L\cup\{L(T)\}`;
4. preserves saturation, layer disjointness, and the envelope row set.

### Proof

Apply CMR748 to `mathcal L\cup\{L(T)\}`. The old cell `e` is forbidden, and
CMR172 preserves the inherited row set. ∎

This is line cleanliness inside the complete moved-layer board, not a claim that
the other layer or points outside the envelope are globally absent from the
line.

## 4. Reappearance on a protected line is entering-edge payment

Suppose a target `T` on a protected line `L` was destroyed and later reappears in
the same envelope. Use its first recreation transition.

### Theorem CMR751 -- PROVED

At least one cell of `T` is an entering selected edge on `L`. Every recreation of
an existing protected target line therefore pays

1. one entering-edge occurrence on that line;
2. exact labelled nonroot full-token incidence `(p+1)(h-1)`;
3. the target-cell reintroduction ledger CMR707--CMR710.

### Proof

CMR707 gives an entering cell of `T`, and every cell of `T` lies on `L`. Apply
CMR413 and CMR710. ∎

A repeated protected line is not fresh reserve stock.

## 5. Growing reserve or exact saturation

Within one fixed envelope, append every new target line to the protected family
and apply CMR750 while capacity remains.

### Theorem CMR752 -- PROVED

Before one of the following endpoints occurs, at most `R(q)` distinct target
lines are added.

1. A bank state strictly lowers triple potential.
2. An existing protected line recurs and pays CMR751.
3. A crossing target spends a strict envelope expansion by CMR193.
4. The protected family reaches size
   
   \[
   \boxed{R(q)+1,}
   \]
   
   giving a linear family of distinct internal target-line signatures beyond the
   guaranteed capacity of CMR748.

### Proof

Every new line raises the family size by one; CMR750 works through size `R(q)`.
Use CMR751 for recurrence and CMR193 for crossing targets. ∎

The fourth branch is a reserve-saturation certificate, not a sharp impossibility
claim for all stronger matching methods.

## 6. Dyadic localization of a saturated reserve

Every internal nonaxis line has primitive direction height between one and
`q-1` after dividing the common prefix spacing.

### Theorem CMR753 -- PROVED

At reserve saturation, some dyadic primitive-height band contains at least

\[
\boxed{
\operatorname{ceil}\left(
\frac{R(q)+1}{\lceil\log_2 q\rceil}
\right)
}
\]

distinct protected target-line signatures.

### Proof

At most `ceil(log_2 q)` dyadic bands cover heights `1,...,q-1`. Partition the
`R(q)+1` lines by band and average. ∎

This feeds the line-energy, low-height, quotient, carry-cell, and
matching-vertex-wall machinery without losing target-line ownership.

## 7. Envelope-chain endpoint

A closure branch has at most `h+1` envelope epochs and at most `h` strict
expansions in a parent of side `N=p^h`.

### Corollary CMR754 -- PROVED

Every target-line-driven prime-power closure reaches at least one of:

1. a strict triple-potential improvement;
2. an existing protected line recreated through an entering edge, with token and
   target-cell reintroduction payment;
3. a fixed-envelope reserve of `R(q)+1` distinct target lines, with CMR753 dyadic
   concentration;
4. one of at most `h` strict envelope expansions;
5. a finite small-envelope case with `q<6`;
6. the deletion, contraction, product, or owner-stock alternatives CMR713--CMR747.

If no epoch saturates and no line recurs, the number of new protected target
lines over the branch is at most

\[
\boxed{
\sum_E R(|E|)
\le
(h+1)\left\lfloor\frac{N-4}{2}\right\rfloor.
}
\]

Thus recurrence pays entering-edge churn, while novelty consumes finite linear
line capacity and then yields a height-localised line family.

### Proof

Apply CMR752 in each epoch, CMR751 to repeated lines, CMR753 at saturation, and
CMR174--CMR175 to the envelope chain. ∎

No all-`n` theorem is claimed. Degree bounds, Hall existence, reserve capacity,
recurrence payment, and dyadic arithmetic are checked in
[`scripts/verify_prime_power_recurrent_target_line_reserve.py`](../scripts/verify_prime_power_recurrent_target_line_reserve.py).
