# Matching normalization does not quotient Euclidean geometry

CMR1654--CMR1661 normalize the opposite matching and forbidden target, then use
the residual simultaneous permutation group `S_{d-2}` to deduplicate matching
response boards. This is exact for matching counts and contracted prescription
probabilities. It is not automatically exact for geometric offspring rows.

An arbitrary permutation of coordinate labels does not preserve real
collinearity. Therefore the 45 side-four and 124 side-five canonical hosts are a
matching-level census only. A geometric census must retain the full line-
incidence structure, expand the matching orbit into geometric fibres, or take an
honest componentwise maximum over those fibres.

This chapter formalizes that correction and identifies the exact geometric
stabilizer of the normalized standard grid.

Let

\[
\Omega_d=\{0,\ldots,d-1\}^2
\]

with its ordinary real-affine collinearity relation. A simultaneous permutation
`pi in S_d` acts by

\[
(i,j)\longmapsto(\pi(i),\pi(j)).
\]

After normalizing `(O,e)=(I_d,(0,1))`, the matching stabilizer consists of the
permutations fixing `0` and `1`.

## 1. Residual matching symmetry is not geometric

### Theorem CMR1774 -- PROVED

For every `d>=4`, the residual matching stabilizer contains permutations which
do not preserve Euclidean collinearity.

For example, let `pi` exchange `2` and `3` and fix every other coordinate. The
three points

\[
(0,1),
\qquad
(1,2),
\qquad
(2,3)
\]

are collinear, while their images

\[
(0,1),
\qquad
(1,3),
\qquad
(3,2)
\]

are not.

### Proof

The original points lie on `y=x+1`. The determinant of the two displacement
vectors of the image triple is

\[
\det((1,2),(3,1))=1-6=-5\ne0.
\]

The permutation fixes `0,1`, so it preserves the normalized identity matching
and target edge, but not the geometric line relation. ∎

Thus matching-orbit equivalence is strictly coarser than geometric equivalence.

## 2. The exact residual geometric stabilizer is trivial

Call a residual simultaneous permutation **geometric** when it preserves the
collinearity relation on all triples of `Omega_d`.

### Theorem CMR1775 -- PROVED

For every `d>=3`, the only geometric residual permutation fixing `0` and `1` is
the identity.

### Proof

For `d=3`, fixing `0,1` already fixes the remaining coordinate.

Assume `d>=4`. The points

\[
(n,n+1),
\qquad
0\le n\le d-2,
\]

lie on one real line. Their images must lie on the line through

\[
(0,1)
\quad\text{and}\quad
(1,\pi(2)).
\]

Put `a=pi(2)-1`. Since `pi(2)` is neither `0` nor `1`, one has `a>=1`. Linearity
gives, for `0<=n<=d-2`,

\[
\pi(n+1)=1+a\pi(n).
\]

With `pi(0)=0`, this recurrence gives

\[
\pi(n)=1+a+\cdots+a^{n-1}
\qquad(n\ge1).
\]

If `a>=2`, then

\[
\pi(d-1)\ge2^{d-1}-1>d-1,
\]

contradicting `pi(d-1) in {0,...,d-1}`. Hence `a=1`, and the recurrence gives
`pi(n)=n` for every `n`. ∎

No nontrivial `S_{d-2}` reduction remains after standard-grid collinearity is
required.

## 3. Matching invariants and geometric invariants separate

### Theorem CMR1776 -- PROVED

Under every simultaneous source-target permutation:

1. perfect-matching counts;
2. rook numbers;
3. contracted prescription counts; and
4. uniform prescription probabilities

are invariant, as in CMR1654.

However the following need not be invariant under the residual matching
stabilizer:

1. collinear-triple status;
2. primitive direction and line height;
3. the multiplicities of CMR1734--CMR1765;
4. the line-energy profile `(h_ell,k_ell)`; and
5. absolute geometric offspring rows.

### Proof

The first list depends only on bipartite incidence and follows from CMR1654. The
counterexample of CMR1774 changes collinearity, and every item in the second list
is determined in part by that relation. ∎

Thus matching denominators may be reused across a fibre even when geometric row
numerators differ.

## 4. Exact geometric state signature

For a normalized matching state, define its geometric signature

\[
\Gamma=(X,P,\lambda,\mathcal L),
\]

where:

- `X` is the deleted matching trace;
- `P` is the retained interface prescription;
- `lambda` contains owner, collision, local-line, root, thin and CRT provenance;
- `mathcal L` is the complete collinearity or line-incidence structure needed to
  compute multiplicities and future rows.

### Theorem CMR1777 -- PROVED

Two states may be identified in an exact geometric orbit table only when there is
a bijection preserving all four coordinates of `Gamma`, including
`mathcal L`, and transporting the response law and offspring labels
equivariantly.

On the standard normalized grid with fixed coordinate values, the residual
simultaneous coordinate action supplies no nontrivial such identification for
`d>=3` unless additional geometric automorphisms are proved for the particular
restricted state.

### Proof

Exact row equality requires a probability-preserving response bijection and a
bijection of every genuinely new labelled offspring. The line-incidence relation
determines which triples exist and must therefore be preserved. The final
statement is CMR1775; a restricted state may have extra accidental symmetries,
but each must be verified directly. ∎

This is stronger than retaining only a direction label attached to already known
candidates: future line incidences must also remain determined.

## 5. Honest geometric fibre expansion

Let `bar sigma` be one matching-level canonical state from CMR1658. Let

\[
\mathcal F(\bar\sigma)
\]

be the finite fibre of exact geometric states which project to it after geometry
is forgotten.

### Theorem CMR1778 -- PROVED

There are three honest ways to use a matching-level orbit in the final quotient.

1. **Fibre expansion:** retain every exact state in `F(bar sigma)` separately.
2. **Geometric orbit reduction:** quotient the fibre only by explicitly verified
   automorphisms preserving `Gamma`.
3. **Upper-fibre row:** define, for each child class `j`,
   \[
   \bar A_{\bar\sigma j}
   =
   \max_{\sigma\in\mathcal F(\bar\sigma)}A_{\sigma j}.
   \]

The third construction is an honest componentwise upper quotient. Simply using
one arbitrary geometric representative is not valid in general.

### Proof

The first two preserve exact rows by definition. In the third construction,
every exact parent row is componentwise bounded by the displayed maximum, so it
is an honest upper quotient. CMR1774 shows why an arbitrary representative need
not dominate the rest of the fibre. ∎

A fibre maximum may be spectrally coarse but is logically safe.

## 6. Certificate lifting and domination

### Theorem CMR1779 -- PROVED

Let `A_geo` be the fully geometric labelled matrix.

1. A strict certificate on an exact geometric orbit quotient lifts by assigning
   equal weights within each verified geometric orbit.
2. A strict certificate for a componentwise upper-fibre matrix also certifies
   every exact geometric row it dominates.
3. A certificate for the matching-only orbit matrix need not certify
   `A_geo` unless one of these two conditions is proved.

### Proof

Part one is the usual orbit-row identity of CMR1660 with the stronger signature
`Gamma`. Part two follows from monotonicity of weighted row sums for nonnegative
matrices. Part three follows from CMR1774--CMR1778. ∎

This is the geometric specialization of the honest quotient rule in CMR1622.

## 7. Finite geometric census compiler

### Theorem CMR1780 -- PROVED

For every fixed thin side `d`, the complete geometric fixed-interface table is
finite and may be constructed by the following procedure.

1. Use matching normalization to compute matching denominators and identify the
   matching-level fibres.
2. For each fibre, enumerate every retained standard-grid embedding or complete
   line-incidence signature.
3. Compute `R_2`, `K_3`, `Psi(Q)`, exact prescription multiplicities, owners and
   child provenance for every response.
4. Quotient only by verified automorphisms of the full geometric signature.
5. Otherwise retain the fibre or take an explicit componentwise maximum.
6. Form exact rational rows using the shared matching denominators.
7. Search and publish a strict rational or integer certificate.

### Proof

Every side, board, response matching, retained label and line-incidence relation
is finite. CMR1776 permits denominator reuse; CMR1778--CMR1779 give the honest
row and certificate operations. ∎

The 45 side-four and 124 side-five matching hosts remain useful denominator
classes, but they are not by themselves the final geometric row count.

## 8. Geometric-fibre endpoint

### Corollary CMR1781 -- PROVED

The canonical thin frontier has the following corrected form.

1. Matching normalization remains exact for response counts and prescription
   probabilities.
2. The full residual `S_{d-2}` action cannot quotient standard-grid geometry.
3. For `d>=3`, its geometric stabilizer is trivial.
4. Geometric line profiles and owner labels must be expanded, exactly quotiented,
   or honestly dominated over every matching fibre.
5. Final certificates must be built on that geometric table or an explicit upper
   quotient.

The next thin computation is therefore a geometric fibre census over the known
matching denominator classes, not one row per matching orbit. No all-`n` theorem
is claimed.

Residual matching invariance, explicit collinearity failure, geometric stabilizer
triviality, fibre maxima and certificate domination are checked in
[`scripts/verify_prime_power_geometric_orbit_fibre_correction.py`](../scripts/verify_prime_power_geometric_orbit_fibre_correction.py).
