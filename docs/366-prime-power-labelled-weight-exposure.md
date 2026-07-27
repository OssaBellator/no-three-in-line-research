# Exact positive-weight support and convex obstruction for labelled responses

CMR2078--CMR2085 prove that every strictly-positive weighted minimizer lies on the
componentwise Pareto frontier. This chapter determines which Pareto vectors can
actually be selected by positive linear child weights and supplies an exact obstruction
when they cannot.

For one accepted geometric assignment bundle, let

\[
V=\{v(Q):Q\in\operatorname{PM}(H)\}\subseteq\mathbf Z_{\ge0}^{C}
\]

be the finite set of labelled child vectors after duplicate compression.

## Theorem CMR2102 -- PROVED

Every response vector is reconstructed directly from the exact coefficient bins, and
its coordinate sum equals the exported all-ones scalar score. Equal vectors form one
weight-indistinguishable response class; componentwise dominated vectors are removed
before weight analysis.

## Theorem CMR2103 -- PROVED

A Pareto vector `v` is **positive-weight supported** when there is an integer vector

\[
w\in\mathbf Z_{>0}^{C}
\]

such that

\[
\boxed{w\cdot v\le w\cdot u\quad\text{for every }u\in V.}
\]

The stored weight vector is a direct exact certificate. The checker recomputes every
score difference and records whether the supported vector is the unique vector minimum
or belongs to a tie face.

## Theorem CMR2104 -- PROVED

A Pareto vector `v` is **convexly unsupported** when there are nonnegative rational
coefficients `lambda_u`, summing to one over `u in V\{v}`, such that

\[
\boxed{
 \sum_{u\ne v}\lambda_u u\le v
}
\]

componentwise, with strict inequality in at least one coordinate.

The checker stores one common positive denominator, all nonnegative integer numerators,
and the exact coordinate slack vector.

## Theorem CMR2105 -- PROVED

Positive support and convex obstruction are mutually exclusive.

### Proof

If `w>0` supports `v`, then `w dot u >= w dot v` for every competing vector. Averaging
with the convex coefficients gives

\[
w\cdot\sum_u\lambda_u u\ge w\cdot v.
\]

A componentwise smaller convex combination with one strict coordinate instead has
strictly smaller positive weighted score, a contradiction. ∎

## Theorem CMR2106 -- PROVED

For a finite Pareto set, the two certificates form the standard exact alternative from
finite-dimensional separation: a Pareto vector either has a strictly positive
supporting normal or lies strictly above a convex combination of the remaining vectors
in at least one coordinate.

The executable checker does not trust an optimizer's status as proof. A support claim
is accepted only after direct integer score verification; an unsupported claim is
accepted only after direct rational convex-combination verification. Every Pareto
vector must carry one of the two certificate forms.

## Theorem CMR2107 -- PROVED

A positive-weight supported vector need not be uniquely selected. The certificate
therefore records the complete number of minimum vector classes. Duplicate responses
inside one vector class remain separate transitions unless a later semantic theorem
identifies them.

Likewise, a Pareto vector is only a candidate until it receives either a positive weight
certificate or a recurrent-row proof. Pareto minimality alone is not a Lyapunov
certificate.

## Theorem CMR2108 -- PROVED

A deterministic 120-system suite contains 767 responses, 699 distinct labelled vectors
and 275 Pareto vectors. In that suite all 275 Pareto vectors are positive-weight
supported: 96 uniquely and 179 with ties. There are 68 duplicate responses.

A separate exact regression uses the Pareto set

\[
(0,3),\quad(3,0),\quad(2,2),
\]

and certifies `(2,2)` as convexly unsupported via the midpoint of the first two vectors.
Additional regressions exercise one tied support and one unique support. The random
suite counts are interface tests, not claims about the genuine parent-rule fibres.

## Corollary CMR2109 -- PROVED

`scripts/check_prime_power_labelled_weight_exposure.py` reconstructs the complete
response-vector table, duplicate quotient, Pareto set and exact support/obstruction
certificates, and rejects twelve independent corruptions.

Passing this checker proves only finite linear-weight support. It does not route
unlabelled destroyed-triple credit, prove state semantics, or establish strict
contraction of a recurrent labelled block.
