# Extension-free line-clean responses have exact component rook rows

CMR1510--CMR1517 prove that deleting the complete allowed trace of one nonaxis
line from the extension-free host leaves at least one perfect matching.  This
chapter makes that response family exact.

The forbidden board is the union of:

1. the opposite perfect matching `O`;
2. the deleted line trace `X`, which is a partial matching;
3. the target edge `e`.

The graph `O union X` has maximum degree two and therefore decomposes into
alternating paths and even cycles.  One matching-polynomial deletion--contraction
step handles `e`.  Exact response counts and all rank-one through rank-three
prescription probabilities follow without enumerating perfect matchings.

Fix `d>=4`, a perfect matching `O`, a target edge `e notin O`, and a partial
matching

\[
X\subseteq E(H_e),
\qquad
H_e=K_{d,d}\setminus(O\cup\{e\}).
\]

For the line-clean application, `X=E(H_e) cap K` for one nonaxis line `K`.
Put

\[
F=O\cup X\cup\{e\}.
\]

## 1. Rook polynomials and response counts

For a bipartite forbidden graph `J`, let `r_j(J)` be the number of size-`j`
matchings in `J` and define

\[
\mathcal R_J(z)=\sum_{j\ge0}r_j(J)z^j.
\]

### Theorem CMR1526 -- PROVED

The number of perfect matchings avoiding `J` on a side-`m` board is

\[
\boxed{
N_m(J)=
\sum_{j=0}^{m}(-1)^jr_j(J)(m-j)!.
}
\]

### Proof

Apply inclusion--exclusion to the forbidden cells.  A chosen set of forbidden
cells can occur in a permutation only when it is a partial matching.  Every
size-`j` forbidden matching is contained in exactly `(m-j)!` permutations. ∎

## 2. Degree-two component factorisation

Put

\[
D=O\cup X.
\]

### Theorem CMR1527 -- PROVED

`D` has maximum degree at most two.  Every nontrivial connected component is an
alternating path or an even cycle, and

\[
\boxed{
\mathcal R_D(z)=
\prod_{C\in\operatorname{Comp}(D)}
\mathcal R_C(z).
}
\]

### Proof

Both `O` and `X` are matchings, so each vertex has at most one incident edge of
each type.  A finite graph of maximum degree two is a disjoint union of paths
and cycles; bipartiteness makes every cycle even.  A matching in a disjoint
union is an independent choice of a matching in each component, so the
generating polynomials multiply. ∎

For a path with `ell` edges write `P_ell(z)` for its matching polynomial, and
for an even cycle with `ell` edges write `C_ell(z)`.

### Theorem CMR1528 -- PROVED

The component polynomials satisfy

\[
P_0(z)=1,
\qquad
P_1(z)=1+z,
\]

\[
\boxed{
P_\ell(z)=P_{\ell-1}(z)+zP_{\ell-2}(z)
\quad(\ell\ge2),
}
\]

and

\[
\boxed{
C_\ell(z)=P_{\ell-1}(z)+zP_{\ell-3}(z)
}
\]

for every even `ell>=4`.

### Proof

For a path, split matchings according to whether the final edge is absent or
present.  In the present case its adjacent edge is unavailable, leaving a path
with `ell-2` edges.  For a cycle, split on one fixed edge.  Omitting it leaves a
path with `ell-1` edges; using it removes its two neighbours and leaves a path
with `ell-3` edges. ∎

## 3. One target-edge deletion--contraction

Write `e=uv`.  Since `e notin D`, matching-polynomial deletion--contraction gives
one exact reduction to degree-two graphs.

### Theorem CMR1529 -- PROVED

\[
\boxed{
\mathcal R_F(z)
=
\mathcal R_D(z)
+
z\mathcal R_{D-u-v}(z).
}
\]

### Proof

A forbidden matching either omits `e`, contributing a matching of `D`, or uses
`e`, after which no edge incident with `u` or `v` may be used.  Removing `e`
from the latter matching gives a matching of `D-u-v` and lowers its size by one.
The factor `z` restores that size. ∎

### Corollary CMR1530 -- PROVED

The exact line-clean response count is

\[
\boxed{
|\operatorname{PM}(K_{d,d}\setminus F)|
=
N_d(F),
}
\]

where `mathcal R_F` is computed by CMR1527--CMR1529.  Moreover

\[
\boxed{N_d(F)>0.}
\]

### Proof

The counting formula is CMR1526.  Positivity is CMR1512 because `X` is a
partial matching in the extension-free host. ∎

## 4. Exact prescription probabilities after line cleaning

Let `P` be any compatible allowed prescription of rank `r`, disjoint from `F`.
Delete its used rows and columns from the forbidden board and denote the
residual graph by `F/P`.  Its board side is `d-r`.

### Theorem CMR1531 -- PROVED

For uniform

\[
R\in\operatorname{PM}(K_{d,d}\setminus F),
\]

one has

\[
\boxed{
\Pr(P\subseteq R)
=
\frac{N_{d-r}(F/P)}{N_d(F)}.
}
\]

The numerator is computed by the same component method.  After contraction,
the residual pieces of `O` and `X` remain partial matchings.  If the target edge
survives, use CMR1529; if one of its endpoints was contracted, only the
degree-two polynomial remains.

### Proof

Contracting a compatible prescription gives a bijection between response
matchings containing `P` and perfect matchings of the residual allowed board.
Apply CMR1526--CMR1529 to that board. ∎

## 5. Finite component signatures

For a prescription `P`, record:

1. the residual side `d-r`;
2. the multiset of path and cycle edge lengths in the residual graph
   `(O union X)/P`;
3. whether the target edge survives;
4. when it survives, the path/cycle multisets after deleting its two endpoints.

Call this the **line-clean rook signature** `kappa(P)`.

### Theorem CMR1532 -- PROVED

The probability in CMR1531 depends only on `kappa(P)`.  For fixed `d`, every
line-clean response count and every rank-at-most-three prescription probability
is computable using integer polynomial arithmetic in time polynomial in `d`.

### Proof

CMR1527--CMR1529 show that the two required rook polynomials are products of the
path/cycle factors specified by the signature.  Their degrees are at most `d`.
Sequential polynomial multiplication and the final inclusion--exclusion sum use
polynomially many integer operations. ∎

This is an exact finite classification, not a claim that the number of
signatures is bounded independently of `d`.

## 6. Exact off-line collateral row

Let `V_kappa` count genuinely new candidate triples whose residual prescription
has line-clean rook signature `kappa`.  Prescriptions using a deleted response
cell of `K` have probability zero and are omitted.

### Theorem CMR1533 -- PROVED

For the uniform extension-free line-clean response,

\[
\boxed{
\mathbb E N_{\rm off}(R)
=
\sum_\kappa
V_\kappa
\frac{N_{d-r(\kappa)}(F/\kappa)}{N_d(F)}.
}
\]

Thus the off-line row left open by CMR1517 is an exact rational rook-class dot
product.  No perfect-matching enumeration is needed.

### Proof

Each candidate triple occurs exactly when its compatible residual prescription
is contained in the sampled response.  Apply linearity of expectation and group
prescriptions by CMR1532. ∎

The remaining task is no longer to define the line-clean coefficient.  It is to
bound this exact dot product uniformly by inherited line/height/carry classes
and compare it with destroyed parent credit.  No all-`n` theorem is claimed.

Degree-two component polynomials, line-clean response counts and prescription
completion ratios are checked in
[`scripts/verify_prime_power_extension_free_line_clean_rook_rows.py`](../scripts/verify_prime_power_extension_free_line_clean_rook_rows.py).
