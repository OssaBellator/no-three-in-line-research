# Line-energy fan splitting and the full carry-token endpoint

CMR359 leaves three outputs: a matching-vertex fan, a heavy full prefix cell,
or many occupied full prefix cells. The heavy cell is executable by CMR342.
This chapter resolves the fan geometry and records the finite full-token ledger
for the dispersed branch.

## 1. A matching-vertex fan is a wall or a secant star

Let `A` distinct chosen line pairs from CMR355 be incident with one fixed source
or target matching vertex. Each pair uses one candidate cell on that vertex.

### Theorem CMR390 — PROVED

At least one of the following holds.

1. **Distinct-cell wall.** The fan uses at least
   \[
   \boxed{\left\lceil\sqrt A\right\rceil}
   \]
   distinct cells on the fixed matching vertex.
2. **Repeated-cell secant star.** One candidate cell `z` belongs to more than
   \[
   \boxed{\sqrt A}
   \]
   chosen line pairs. The two other cells of the corresponding triples form
   pairwise cell-disjoint outside pairs whose joining lines all pass through
   `z`.

### Proof

Let `C` be the number of distinct cells used on the fixed matching vertex. If
`C\ge\lceil\sqrt A\rceil`, the first alternative holds. Otherwise one cell
occurs more than `A/C>\sqrt A` times.

If two distinct lines through that cell shared an outside point, they would
contain the same two grid points and hence be equal. Thus the outside pairs are
cell-disjoint. ∎

The wall is the CMR202 candidate wall. The repeated-cell alternative is the
CMR111 secant-star geometry, already equipped with endpoint-disjoint outside
pairs.

## 2. Exact full-prefix token count

Fix an inherited parent block of size

\[
t=p^h,
\]

one layer, and one direction `\theta\in\mathbb P^1(\mathbb F_p)`. A full prefix
token is

\[
\tau=(b,a,c,\theta),
\qquad
0\le b<h,
\qquad
(a,c)\in(\mathbb Z/p^b\mathbb Z)^2.
\]

### Theorem CMR391 — PROVED

For one fixed direction, the exact number of full prefix tokens is

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
\boxed{(p+1)Q_p^{(2)}(t).}
\]

### Proof

At depth `b` there are `p^b` column prefixes and `p^b` row prefixes. Sum the
geometric series. ∎

## 3. Fresh-token packing and temporal reuse

### Theorem CMR392 — PROVED

Let `E_1,\ldots,E_J` be dispersed line-energy episodes in the same inherited
parent block, layer, and direction. Suppose every episode occupies at least `R`
full prefix tokens.

If the token sets are pairwise disjoint, then

\[
\boxed{
J\le\left\lfloor\frac{Q_p^{(2)}(t)}{R}\right\rfloor.
}
\]

Without disjointness, some exact full token occurs in at least

\[
\boxed{
\operatorname{ceil}\left(\frac{JR}{Q_p^{(2)}(t)}\right)
}
\]

episodes.

### Proof

Count episode-token incidences and distribute them among the exact token set
from CMR391. ∎

Attach the envelope depth, absolute prefix coordinates, layer, and direction to
obtain absolute tokens. Fine repairs below a token preserve its coarser
coordinates; envelope expansion changes the namespace and is charged to CMR174.

## 4. Complete structural endpoint

### Corollary CMR393 — PROVED

A frozen, anchored-free two-slice line-clean bank of size `t=p^h\ge20` exposes
at least one of:

1. a distinct-cell candidate wall;
2. a repeated-cell secant star with cell-disjoint outside pairs;
3. an executable heavy full prefix cell;
4. a dispersed family of full prefix tokens;
5. repeated occurrence of one exact absolute full prefix token.

### Proof

Apply CMR359. Split its matching-vertex fan by CMR390. The heavy cell is
executable by CMR342. Apply CMR391--CMR392 to the dispersed alternative. ∎

Thus the remaining fixed-envelope obstruction has one exact form: repeated
visits to one absolute full prefix token, or one of the already executable
wall, secant-star, or heavy-cell outputs.

No all-`n` theorem is claimed here. The fan split, token counts, and temporal
incidence bounds are checked in
[`scripts/verify_prime_power_line_energy_tokens.py`](../scripts/verify_prime_power_line_energy_tokens.py).
