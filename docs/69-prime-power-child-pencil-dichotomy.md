# Diffuse-or-alternating dichotomy for child-translation pencils

CMR102--CMR105 isolate the weak recursive-compatible collateral in the vertical
child-translation pencil. This chapter proves that the pencil is either diffuse
at quadratic aggregate cost or contains a concrete secant star to which the
alternating matching bank AN1--AN4 applies.

Retain one nonroot node `A` at depth `s`, with

\[
N=p^k,
\qquad
L=p^{k-s-1},
\qquad
|A|=pL,
\qquad
Z=S\setminus A.
\]

Let `Omega` be one CMR96 two-endpoint-forbidden reciprocal node bank, and put

\[
D_p=|\Omega|=h(p-2)+1,
\qquad
h=(p-1)/2.
\]

A profile `(xi,eta)` is **supported** when some map in `Omega` sends `xi` to
`eta`. Let

\[
\mathcal V_\Omega(A)
=
\sum_{(\xi,\eta)\text{ supported}}W(\xi,\eta)
=
\mathcal V_{1,\Omega}(A)+\mathcal V_{2,\Omega}(A),
\]

where `V_1` and `V_2` are the sums of the CMR103 loads `W_1` and `W_2`.
The support restriction is essential: forbidden child outputs have probability
zero and should not be charged as collateral.

## 1. Support-pruned node inequality

### Theorem CMR106 — PROVED

For the uniform CMR96 node bank,

\[
\mathbb E\bigl[\Phi(S_{F'})-\Phi(Z)-I(A)\bigr]
\le
\frac{h}{D_p}\mathcal V_\Omega(A)
+
\frac{U_2+U_3}{D_p}.
\]

### Proof

By CMR103, the external node-rank-one load of a state is

\[
\sum_\xi W(\xi,F'(\xi)).
\]

If `(xi,eta)` is unsupported, its probability is zero. Every supported cell is
contained in at most `h` maps of `Omega`, by the one-cell count in CMR96. Thus
its probability is at most `h/D_p`. Sum only over the supported profiles and
apply the rank-two and rank-three atom `1/D_p` from CMR96. CMR101 removes the
invariant child core. ∎

## 2. One-child-point stars

For one supported pencil cell `z`, let `G_z` be the graph on the fixed point set
`Z` whose edges are the outside pairs collinear with `z`. Its edge count is the
contribution of `z` to `V_{1,Omega}`.

A maximal matching with `nu` edges has a vertex cover of size `2nu`, so

\[
|E(G_z)|\le 2\nu(|Z|-1).
\]

If `nu>=13`, at least seven matching edges have an endpoint in one fixed
permutation layer: among the two layers, one is incident with at least half the
matching edges. Choosing one such endpoint from each of seven edges gives seven
points with distinct rows and columns.

### Theorem CMR107 — PROVED

At least one of the following holds.

1. There is a supported pencil cell `z` and seven endpoint-disjoint outside
   secants through `z` from which one endpoint per secant can be chosen in one
   fixed permutation layer. Conditional on any parent-node state containing
   `z`, AN1--AN4 give an alternating endpoint-rematching bank that preserves
   saturation and destroys all seven prospective triples in every state.
2. The one-point pencil mass satisfies
   \[
   \mathcal V_{1,\Omega}(A)
   \le
   24p^2L(|Z|-1).
   \]

### Proof

There are at most `p^2L` supported pencil cells. If the first alternative fails,
every `G_z` has a maximal matching of size at most twelve. Hence every one has
at most `24(|Z|-1)` edges. Sum over the pencil cells.

If a matching has at least thirteen edges, one layer is represented on at least
seven of them. The selected endpoints are distinct because the matching edges
are vertex-disjoint; within one permutation layer they also have distinct rows
and columns. The original endpoint cell and the cell occupied by the other
layer are the only possible forbidden positions in each selected row or column,
so AN1 applies. Moving every selected endpoint destroys the corresponding old
outside pair through `z`. ∎

## 3. Two-child-point stars

Fix a supported profile `(xi,eta)` and an outside point `P` in `Z`. Let
`H_{P,xi,eta}` be the graph on the `L` points of `A_{xi,eta}` whose edges are
pairs collinear with `P`. Its edge count contributes to `V_{2,Omega}`.

### Theorem CMR108 — PROVED

At least one of the following holds.

1. There are a supported profile `(xi,eta)`, one outside point `P`, and seven
   endpoint-disjoint secants inside `A_{xi,eta}` through `P`. After choosing a
   parent-node state containing the profile, AN1 gives a nested endpoint bank
   inside the translated child subtree. Every state preserves saturation and
   destroys all seven prospective triples.
2. The two-point pencil mass satisfies
   \[
   \mathcal V_{2,\Omega}(A)
   \le
   12p^2|Z|(L-1).
   \]

### Proof

There are at most `p^2|Z|` graphs of the displayed type. If the first
alternative fails, every graph has a maximal matching of size at most six, and
therefore at most `12(L-1)` edges.

In the first alternative all matching endpoints lie in one translated child
subtree and hence in one permutation layer with distinct rows and columns. A
rematching of the chosen endpoint columns to their existing rows preserves the
child row fibre. The opposite layer has a different parent row residue modulo
`p^s`, so disjointness is automatic; forbidding the old diagonal moves every
chosen endpoint. AN1 supplies the nested bank and its spread. ∎

## 4. Quadratic aggregate endpoint

### Corollary CMR109 — PROVED

For every node, either CMR107 or CMR108 produces an explicit alternating
absorber of size at least seven, or

\[
\mathcal V_\Omega(A)
\le
24p^2L(|Z|-1)+12p^2|Z|(L-1)
<
36p^2L|Z|.
\]

In the absorber-free case,

\[
\frac{h}{D_p}\mathcal V_\Omega(A)
<
120|A|N.
\]

At a fixed depth `s`, the `2p^s` layer-prefix nodes satisfy

\[
\sum_A |A|=2N.
\]

Therefore, if every node at that depth is absorber-free, their total expected
support-pruned rank-one pencil collateral is less than

\[
240N^2.
\]

### Proof

Add CMR107 and CMR108. Since `|Z|<2N`, `pL=|A|`, and

\[
\frac{h}{D_p}<\frac1{p-2},
\qquad
\frac p{p-2}\le\frac53
\quad(p\ge5),
\]

one obtains

\[
\frac{h}{D_p}\mathcal V_\Omega(A)
<
\frac{72p}{p-2}|A|N
\le
120|A|N.
\]

Summing the equal-size node partition at depth `s` gives the final estimate. ∎

## 5. Consequence

The vertical-pencil concentration problem is closed as a dichotomy:

- diffuse pencils cost only `O(N^2)` per depth in the recursive-compatible
  first moment;
- concentrated pencils expose a literal alternating secant-star bank, either on
  outside endpoints or nested inside one translated child.

The remaining theorem is no longer a pencil-mass estimate. It is a termination
or collateral-conversion theorem for the extracted alternating banks, together
with control of fine mass recreated by later coarse repairs.

The extraction identities and maximal-matching bounds are checked in
[`scripts/verify_prime_power_child_pencil_dichotomy.py`](../scripts/verify_prime_power_child_pencil_dichotomy.py).
