# Dynamic-pool excess-shadow potential

The fixed-infrastructure potential PP3ij treats controller edges as immutable.
That makes a source-star centre inside a controller pool appear captive. The
candidate **cells**, however, depend only on the old column set and old row set
of each pool, not on the current pairing between them. Permuting row endpoints
inside a pool therefore preserves a larger cell universe exactly.

Subtracting the one automatic axis blocker at every candidate cell gives a
nonnegative potential that counts precisely the additional nonaxis blocker
incidences. This potential permits controller pairings to evolve while the pool
coordinate infrastructure remains fixed.

## 1. Fixed pool coordinate sets

Let the selected perfect-matching layer be partitioned into disjoint pools

\[
E_i\subseteq X_i\times Y_i,
\qquad i\in[M],
\]

where `E_i` is a perfect matching between its old-column set `X_i` and old-row
set `Y_i`, both of size `R`. Let the complete movement and refill label sets both
have size `T`.

Define the candidate-cell universe

\[
\mathcal V_{\rm cell}
=
\bigcup_i
\left(
  \{(x,A):x\in X_i,\ A\in\mathcal A\}
  \cup
  \{(B,y):B\in\mathcal B,\ y\in Y_i\}
\right).
\]

It has size `2MRT`.

### Proposition PP3ku -- PROVED

Permuting the row endpoints of the matching edges inside any collection of pools
preserves:

1. saturation of the selected matching layer;
2. every set `X_i` and `Y_i`;
3. pairwise disjointness of the pools;
4. the complete candidate-cell universe `V_cell`.

#### Proof

Inside one pool, a permutation replaces a perfect matching between `X_i` and
`Y_i` by another perfect matching between the same sets. Every old column and
row still occurs once in the selected layer. Different pools have disjoint
column and row sets because they are disjoint subsets of one perfect matching.
The displayed candidate cells depend only on `X_i,Y_i` and the numerical label
sets. ∎

Controller identities may change, but the geometric candidate cells do not.

## 2. Automatic axis blocker and nonaxis equivalence

For a candidate cell `z`, let

\[
b_S(z)
=
|\{\{p,q\}\subseteq S:p,q,z\text{ are collinear}\}|.
\]

### Proposition PP3kv -- PROVED

For every saturated source `S` and every movement or refill candidate cell `z`:

1. `b_S(z)>=1`;
2. exactly one blocker pair through `z` is horizontal or vertical;
3. that axis pair contains the current controller point of `z`;
4. every additional blocker pair is nonaxis and is disjoint from the current
   controller point.

Consequently a controller-aware cell entry is bad if and only if

\[
\boxed{b_S(z)-1>0.}
\]

#### Proof

For a movement cell `(x,A)`, the saturated source contains exactly two old-grid
points in column `x`; they form the unique vertical blocker pair. One is the
selected-layer matching point in column `x`, hence the controller point. Any
line through that controller point and `(x,A)` is vertical, so a blocker pair
containing the controller must be this axis pair. Every other blocker pair is
therefore nonaxis and controller-disjoint. The refill statement is the
transposed horizontal argument. ∎

Thus nonaxis cell safety is independent of the current pairing inside the pool.

## 3. Excess-shadow potential

Define

\[
\boxed{
\Xi(S)
=
\sum_{z\in\mathcal V_{\rm cell}}
\bigl(b_S(z)-1\bigr).
}
\]

### Proposition PP3kw -- PROVED

The potential `Xi` is a nonnegative integer. If `U_cell(S)` is the number of
controller-aware bad movement/refill cell entries in the complete pool-label
universe, then

\[
\boxed{U_{\rm cell}(S)\le\Xi(S).}
\]

Moreover `Xi(S)=0` if and only if every movement and refill candidate cell is
controller-aware safe against retained-retained-patch triples.

#### Proof

Proposition PP3kv makes every summand a nonnegative integer and identifies
positive summands with bad entries. Each positive summand is at least one, so the
number of positive summands is at most their sum. Equality to zero is exactly
absence of additional nonaxis blocker pairs. ∎

In particular, `Xi=o(MRT)` implies `o(1)` bad cell-entry density.

## 4. Exact pair-weight identity

For source points `p,q`, put

\[
\omega(p,q)
=
|\{z\in\mathcal V_{\rm cell}:p,q,z\text{ are collinear}\}|.
\]

Then

\[
\Xi(S)
=
\sum_{\{p,q\}\subseteq S}\omega(p,q)
-
|\mathcal V_{\rm cell}|.
\]

### Proposition PP3kx -- PROVED

Let `R_0` be endpoints removed by a source-admissible endpoint permutation and
let `R_pi` be their replacements. Suppose the permutation preserves every pool
coordinate set `X_i,Y_i` containing removed controller-layer points. Then

\[
\boxed{
\Xi(S_\pi)-\Xi(S)
=
\mathcal I_\Xi(\pi)-\mathcal C_\Xi(R_0).
}
\]

Here

\[
\mathcal C_\Xi(R_0)
=
\sum_{r\in R_0}\sum_{p\in S\setminus R_0}\omega(r,p)
+
\sum_{\{r,s\}\subseteq R_0}\omega(r,s),
\]

and `I_Xi` is the analogous sum over inserted points.

#### Proof

Proposition PP3ku keeps `V_cell` and its cardinality fixed. Expand the pair-weight
sum before and after the trade. Pairs wholly in the unchanged source cancel,
leaving exactly the removal-credit and insertion-cost terms. ∎

This is the PP3ib identity with a controller-pairing-invariant weight.

## 5. Captive source-star credit

Let `p` be a source-star centre from PP3hx lying in a controller pool. Every
chosen star blocker pair `{p,s}` is nonaxis and blocks its associated candidate
cell.

### Theorem PP3ky -- PROVED

Suppose `p` belongs to pool `E_i` and is a blocker endpoint in `C_star` bad
entries. Choose any tied endpoint set `R_0 subseteq E_i` containing `p`, and
apply a source-admissible endpoint permutation inside `E_i` that moves every
point of `R_0`. Then:

1. all pool coordinate sets and `V_cell` are preserved;
2. the removal credit satisfies

   \[
   \boxed{\mathcal C_\Xi(R_0)\ge C_{\rm star};}
   \]

3. if

   \[
   \mathcal I_\Xi(\pi)<C_{\rm star},
   \]

   then `Xi` strictly decreases.

#### Proof

Pool preservation is PP3ku. Each selected star entry contributes one incidence
unit to `omega(p,s)`, and moving `p` removes all of them. They are included in
`C_Xi(R_0)`. Apply PP3kx. ∎

The controller matching inside `E_i` may change, but the potential and candidate
cell universe do not.

## 6. Dynamic monotone termination

Call a trade **pool-compatible** when every changed selected-layer endpoint is
permuted only with endpoints from its own pool. Opposite-layer or unused-layer
endpoint trades are also allowed because they leave all `X_i,Y_i` unchanged.

### Theorem PP3kz -- PROVED UNDER A CONVERSION HYPOTHESIS

Fix a threshold `eta>0`. Assume that whenever

\[
U_{\rm cell}(S)\ge\eta|\mathcal V_{\rm cell}|,
\]

the current source supplies a source-admissible pool-compatible trade satisfying

\[
\mathcal I_\Xi<\mathcal C_\Xi.
\]

Then finitely many such trades produce a source satisfying

\[
\boxed{U_{\rm cell}(S)<\eta|\mathcal V_{\rm cell}|.}
\]

If the conversion hypothesis is available uniformly for a sequence
`eta_m=o(1)`, the resulting sources have `o(1)` bad cell-entry density. If it
applies whenever `Xi>0`, the process terminates at `Xi=0`.

#### Proof

Every trade preserves `V_cell` and strictly decreases the nonnegative integer
`Xi`. Hence no state repeats and only finitely many trades occur. If the process
stopped above the fixed threshold, the conversion hypothesis would supply
another decreasing trade. The asymptotic and zero-shadow conclusions follow by
applying the fixed-threshold statement with `eta=eta_m` and by PP3kw. ∎

This termination theorem permits dynamic controller pairings while retaining
fixed pool coordinate infrastructure.

## 7. Consequence for the captive-star bottleneck

The captive source-star problem is no longer blocked by loss of a fixed
candidate universe. It is reduced to the same geometric endpoint issue as the
free star:

- construct a source-admissible within-pool endpoint permutation moving the star
  centre;
- keep its excess-shadow insertion cost below the linear star credit.

A zero-unary Hall/superregular host may be built inside the pool using `Xi`-shadow
supports. The remaining obstruction is geometric conversion of that host or its
Hall rectangle, not dynamic relabelling of controller edges.

The same dynamic potential can be used for resource-bank trades that permute
controller-layer endpoints within their original pools. Same-slot
movement/refill anchor restrictions still depend on the current edge pairing and
must be recomputed after a trade; their divisor-energy treatment is separate
from the cell-shadow potential.
