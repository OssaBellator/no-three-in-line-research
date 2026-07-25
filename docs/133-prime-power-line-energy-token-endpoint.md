# Line-energy fan splitting and the full carry-token endpoint

CMR359 leaves three outputs: a matching-vertex fan, a heavy full prefix cell,
or many occupied full prefix cells. The heavy cell is executable by CMR342.
This chapter resolves the internal geometry of the fan and records the exact
finite ledger for the dispersed full cells.

## 1. A matching-vertex fan is a wall or a secant star

Let `A` distinct chosen line pairs from CMR355 be incident with one fixed source
vertex or target vertex. Each pair uses exactly one candidate cell on that
matching vertex.

### Theorem CMR385 — PROVED

At least one of the following holds.

1. **Distinct-cell wall.** The fan uses at least
   \[
   \boxed{\left\lceil\sqrt A\right\rceil}
   \]
   distinct candidate cells on the fixed source row or target column.
2. **Repeated-cell secant star.** One candidate cell `z` belongs to more than
   \[
   \boxed{\sqrt A}
   \]
   of the chosen line pairs. For those lines, the two other cells of the
   selected candidate triple form pairwise cell-disjoint outside pairs, all
   whose real joining lines pass through `z`.

### Proof

Let `C` be the number of distinct cells used on the fixed matching vertex. If
`C>=ceil(sqrt A)`, the first alternative holds. Otherwise one cell `z` occurs
in more than `A/C>sqrt A` chosen pairs.

For every such occurrence, let the selected triple on its real line be

\[
\{z,u_L,v_L\}.
\]

If two distinct lines through `z` shared either `u_L` or `v_L`, the two lines
would contain the same two grid points and would therefore be equal. Hence the
outside two-cell sets are pairwise disjoint. ∎

The distinct-cell alternative is precisely the candidate-only wall of CMR202.
The repeated-cell alternative is the one-point secant-star geometry used by
CMR111: it has already supplied the endpoint-disjoint outside pairs, so only
the matching-layer extraction and collateral comparison remain.

## 2. Exact full-prefix token count

Fix one inherited parent block of size

\[
t=p^h,
\]

one permutation layer, and one projective direction

\[
\theta\in\mathbb P^1(\mathbb F_p).
\]

A **full prefix token** is

\[
\tau=(b,a,c,\theta),
\]

where

\[
0\le b<h,
\qquad
(a,c)\in(\mathbb Z/p^b\mathbb Z)^2.
\]

### Theorem CMR386 — PROVED

For one fixed direction, the number of full prefix tokens is exactly

\[
\boxed{
Q_p^{(2)}(t)
=
\sum_{b=0}^{h-1}p^{2b}
=
\frac{t^2-1}{p^2-1}.
}
\]

Across all `p+1` projective directions it is

\[
\boxed{
(p+1)Q_p^{(2)}(t).
}
\]

### Proof

At depth `b` there are `p^b` column prefixes and `p^b` row prefixes. Sum the
resulting geometric series. ∎

## 3. Fresh-token packing and temporal reuse

### Theorem CMR387 — PROVED

Let `E_1,...,E_J` be dispersed line-energy episodes in the same inherited
parent block, layer, and projective direction. Suppose every episode occupies
at least `R` full prefix tokens.

If the token sets are pairwise disjoint, then

\[
\boxed{
J
\le
\left\lfloor
\frac{Q_p^{(2)}(t)}{R}
\right\rfloor.
}
\]

Without pairwise disjointness, some exact full prefix token occurs in at least

\[
\boxed{
\operatorname{ceil}\left(
\frac{JR}{Q_p^{(2)}(t)}
\right)
}

episodes.

### Proof

Count episode-token incidences and distribute them among the exact token set
from CMR386. ∎

Attach the parent envelope depth, absolute prefix coordinates, layer, and
direction to obtain absolute tokens. Fine repairs below a token preserve its
coarser coordinates; envelope expansion changes the namespace and is charged
to CMR174.

## 4. Complete structural endpoint for a frozen two-slice bank

### Corollary CMR388 — PROVED

A frozen, anchored-free two-slice line-clean bank of size `t=p^h>=20` exposes at
least one of the following.

1. a distinct-cell candidate wall on one source row or target column;
2. a repeated-cell secant star with pairwise cell-disjoint outside pairs;
3. an executable heavy full prefix cell;
4. a dispersed family of full prefix tokens;
5. repeated occurrence of one exact absolute full prefix token.

For the dyadic band of CMR354, the fan size and the heavy/dispersed populations
are given explicitly by CMR359. Fresh dispersed episodes are bounded by
CMR387; a long closure therefore reduces to the repeated-token alternative.

### Proof

Apply CMR359. Split its matching-vertex fan by CMR385. The heavy prefix-cell
alternative is executable by CMR342. Apply CMR386--CMR387 to the dispersed
alternative. ∎

Thus the remaining fixed-envelope obstruction has one exact form: repeated
visits to the same absolute full prefix token, or the already explicit
candidate-wall/secant-star alternatives. Generic matching-space spread,
height localization, and fresh carry dispersion are no longer open.

No all-`n` theorem is claimed here. The square-root fan split, token counts,
and temporal incidence bounds are checked in
[`scripts/verify_prime_power_line_energy_tokens.py`](../scripts/verify_prime_power_line_energy_tokens.py).
