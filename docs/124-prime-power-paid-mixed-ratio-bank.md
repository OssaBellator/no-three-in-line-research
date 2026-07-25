# A recycled mixed fan supports an exact paid ratio bank

CMR309 extracts a linear common-ratio population from a fully recycled mixed
singleton fan.  The remaining weighting issue is that a Hall blocker line may
intersect a parent permutation in only one cell; that intersection alone does
not certify a new collinear triple.  The sharp source-fan structure resolves
this locally.  Every blocker line contains a compatible rank-three certificate,
and one may choose such a certificate to include the line's unique fan cell.
Those prescriptions have equal completion counts and disjoint matching
cylinders.

Work in the source/source/target orientation of CMR309.  Fix the target-specific
parent bank which omits the old endpoint

\[
z_1=(x_1,y_1).
\]

Let `mathcal R` be a subfamily of sharp source-fan lines at `z_1`.  Every line
`L in mathcal R` contains one unique fan cell

\[
f_L=(x_1,a_L),
\qquad
a_L\ne y_1,
\]

and the rows `a_L` are distinct across the family.

Assume every `L` is a candidate-only certificate line, as in the CMR246
extraction.  Thus it contains at least one compatible available rank-three
prescription.

## 1. Fan-anchored certificate selection

### Theorem CMR322 — PROVED

For every `L in mathcal R`, there is a compatible three-cell prescription

\[
Q_L\subseteq E_*(L)
\]

such that

\[
\boxed{f_L\in Q_L.}
\]

### Proof

Choose any compatible candidate-only triple `T_L` on `L`, whose existence is
part of the certificate-line hypothesis.  If `f_L` belongs to `T_L`, take
`Q_L=T_L`.  Otherwise `L` contains the three cells of `T_L` and the additional
cell `f_L`.  A nonaxis real line meets each source column and target row at most
once, so `f_L` together with any two cells of `T_L` is still a compatible
three-cell matching prescription.  Every chosen cell is available because
`f_L` is not `z_1` and `T_L` came from the target-specific host. ∎

## 2. Exact completion count

### Theorem CMR323 — PROVED

Every prescription `Q_L` extends to exactly

\[
\boxed{(t-3)!}
\]

perfect matchings of the target-specific host

\[
K_{t,t}\setminus\{z_1\}.
\]

Every such completion omits `z_1` and contains a candidate-only collinear
triple on `L`.

### Proof

The three cells of `Q_L` use three distinct source and target vertices.  One of
the used source vertices is `x_1`, because `f_L in Q_L`.  Delete the six used
vertices.  The only forbidden target-specific edge was `(x_1,y_1)`, and its
source vertex has already been deleted.  The remaining host is therefore the
complete bipartite graph `K_{t-3,t-3}`, with exactly `(t-3)!` perfect matchings.
Every extension contains `Q_L`, hence contains its collinear triple and omits
the old target endpoint. ∎

## 3. Disjoint ratio cylinders

### Theorem CMR324 — PROVED

For distinct fan lines `L,L' in mathcal R`, the completion cylinders

\[
\Omega(Q_L)
\qquad\text{and}\qquad
\Omega(Q_{L'})
\]

are disjoint.  Consequently the union bank

\[
\mathcal B(\mathcal R)
=
\bigcup_{L\in\mathcal R}\Omega(Q_L)
\]

has exact state count

\[
\boxed{
|\mathcal B(\mathcal R)|
=
|\mathcal R|(t-3)!.
}
\]

### Proof

The two prescriptions contain different cells in the same source column
`x_1`, because the sharp fan assigns distinct rows `a_L`.  No perfect matching
can contain both cells.  CMR323 gives the equal size of each disjoint cylinder.
∎

## 4. Paid common-ratio bank

### Corollary CMR325 — PROVED

Suppose a fully recycled mixed fan lies in a block of size `t=p^h`, and let
`mathcal R` be the common unit-ratio population supplied by CMR309.  Then

\[
|\mathcal R|
\ge
\operatorname{ceil}\left(
\frac{t-3-2t/p}{p-1}
\right),
\]

and the exact bank `mathcal B(mathcal R)` has at least

\[
\boxed{
\operatorname{ceil}\left(
\frac{t-3-2t/p}{p-1}
\right)(t-3)!
}
\]

states.

Every bank state simultaneously:

1. omits `z_1`, and hence destroys the selected old target triple containing
   `z_1`;
2. realizes one rank-three candidate-only certificate on a line from the common
   modular-ratio class;
3. belongs to exactly one ratio-line cylinder.

The same statement holds in the coordinate-dual mixed orientation.

### Proof

Apply CMR322--CMR324 to the ratio population from CMR309.  The target triple is
destroyed because every target-specific state omits its endpoint `z_1`.
Cylinder uniqueness follows from CMR324.  Coordinate duality gives the final
statement. ∎

## 5. What this weighting does and does not prove

CMR325 resolves one precise weighting gap: the common-ratio population is not
merely a collection of line signatures.  It supports an explicit equal-weight
bank, and every state in that bank pays for its ratio certificate by destroying
one fixed old target.

This is not yet a decreasing bank.  A state may create additional collateral
beyond the guaranteed ratio-line triple, and the guaranteed destroyed load is
one target.  The remaining conversion theorem must use the ratio signature,
the opposite-deviation pair from CMR319, or a collateral average over this bank
to produce an improving state or a boundedly reusable carry charge.

No all-`n` theorem is claimed here.  Fan-anchored triples, exact completion
counts, cylinder disjointness, and bank sizes are checked in
[`scripts/verify_prime_power_paid_mixed_ratio.py`](../scripts/verify_prime_power_paid_mixed_ratio.py).
