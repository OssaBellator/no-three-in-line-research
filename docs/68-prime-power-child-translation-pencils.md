# Child-translation pencils for recursive-compatible rank-one collateral

CMR101 isolates the remaining weak class in the recursive-compatible node bank:
one or two replacement points from a single child subtree, together with at
least one fixed point outside the parent node. This class cannot be identified
with ordinary finer-prefix collateral. The parent-node move changes the child's
row residue modulo the finer quotient, whereas a finer prefix rematching
preserves that residue.

Let

\[
N=p^k,
\qquad 1\le s<k,
\qquad L=p^{k-s-1}.
\]

Fix one layer-prefix node `(s,a,ell)`. A column in child digit `xi` has the form

\[
x=a+p^s\xi+p^{s+1}q,
\qquad 0\le q<L.
\]

Write the unchanged descendant row map as `q -> H_q`. For every possible child
output digit `eta`, define the rigid translated child set

\[
A_{\xi,\eta}
=
\left\{
\left(
 a+p^s\xi+p^{s+1}q,
 P_{\ell,s}(a)+p^s\eta+p^{s+1}H_q
\right):0\le q<L
\right\}.
\]

Let `A` be the old full parent-node block and put `Z=S\setminus A`.

## 1. Direct descent to the finer rematching bank is impossible

### Theorem CMR102 — PROVED

Suppose the old child output is `eta_0` and a parent-node replacement uses
`eta!=eta_0`. Then every point of `A_{xi,eta}` has row residue

\[
P_{\ell,s}(a)+p^s\eta\pmod {p^{s+1}},
\]

which differs from the old child row residue

\[
P_{\ell,s}(a)+p^s\eta_0\pmod {p^{s+1}}.
\]

Every scale-`s+1` prefix rematching of the original child block preserves the
old row set and therefore preserves the second residue. Consequently the new
parent-node cells with output `eta` do not belong to the candidate universe of
the original finer prefix-rematching bank.

### Proof

A scale-`s+1` child block is matched to one fixed row fibre modulo `p^{s+1}`.
CMR75 changes only the perfect matching between its columns and that same row
set. A parent-node parameter change replaces the child row digit itself. Since
`eta-eta_0` is nonzero modulo `p`, the two residues differ modulo `p^{s+1}`. ∎

Thus the weak `U_1` term is a cross-fibre translation shadow, not the rank-one
term of CMR78 one level lower.

## 2. Exact child-load profiles

For one child digit and one output digit, define:

- `W_1(xi,eta)` as the number of real collinear triples containing exactly one
  point of `A_{xi,eta}` and two points of `Z`;
- `W_2(xi,eta)` as the number containing exactly two points of `A_{xi,eta}` and
  one point of `Z`.

Put

\[
W(\xi,\eta)=W_1(\xi,\eta)+W_2(\xi,\eta).
\]

### Theorem CMR103 — PROVED

For any replacement node map `F'`, the number of non-invariant node-rank-one
triples in `Z` together with the replacement node is exactly

\[
\sum_{\xi\in\mathbb F_p}W(\xi,F'(\xi)).
\]

The triples wholly inside one child subtree are the invariant contribution from
CMR100 and are not included in `W`.

### Proof

A node-rank-one triple uses replacement points from one unique child input
`xi`. If it uses one replacement point, its other two points lie in `Z` and it
is counted by `W_1`. If it uses two replacement points, its remaining point lies
in `Z` and it is counted by `W_2`. The only other possibility is three
replacement points in one child subtree; CMR100 makes those invariant, and they
were explicitly removed in CMR101. The child output in state `F'` is
`F'(xi)`, giving the displayed sum. ∎

## 3. Geometry-free pencil mass bounds

### Theorem CMR104 — PROVED

For every child digit `xi`,

\[
\sum_{\eta\in\mathbb F_p}W_1(\xi,\eta)
\le
L\binom{|Z|}{2},
\]

and

\[
\sum_{\eta\in\mathbb F_p}W_2(\xi,\eta)
\le
|Z|\binom L2.
\]

Consequently, with

\[
\mathcal V(A)
=
\sum_{\xi,\eta}W(\xi,\eta),
\]

one has

\[
\mathcal V(A)
\le
pL\binom{|Z|}{2}
+p|Z|\binom L2.
\]

Since `pL=|A|`, the coarse bound

\[
\mathcal V(A)
<
2|A|N^2+
\frac{N|A|^2}{p}
\]

also holds.

### Proof

Fix a pair of points in `Z`. For each of the `L` columns in one child subtree,
the real line through the pair has at most one row. As `eta` varies, the point in
that column runs through `p` distinct rows, so at most one `eta` contributes.
This proves the `W_1` bound.

For `W_2`, fix one point of `Z` and two distinct child columns. Translating both
child points by changing `eta` changes their common row offset by `p^s eta`.
The determinant with the fixed outside point is an affine function of `eta`
whose coefficient is `p^s` times the nonzero difference of the two child
columns. Hence at most one `eta` works. Sum over outside points and child-column
pairs.

Finally sum over the `p` child inputs and use `|Z|<2N` and `L=|A|/p`. ∎

## 4. Corrected recursive-compatible repair endpoint

Let

\[
D_p=h(p-2)+1,
\qquad h=(p-1)/2,
\]

be the CMR96 bank size. The one-child output atom is at most `h/D_p`, while
node rank two or three has atom at most `1/D_p`.

### Corollary CMR105 — PROVED

For the uniform CMR96 node bank,

\[
\mathbb E\bigl[\Phi(S_{F'})-\Phi(Z)-I(A)\bigr]
\le
\frac{h}{D_p}\mathcal V(A)
+
\frac{U_2+U_3}{D_p}.
\]

Thus some recursive-compatible state improves whenever

\[
D(A)-I(A)
>
\frac{h}{D_p}\mathcal V(A)
+
\frac{U_2+U_3}{D_p}.
\]

### Proof

By CMR103, the external node-rank-one load of state `F'` is

\[
\sum_\xi W(\xi,F'(\xi)).
\]

For each fixed `(xi,eta)`, CMR96 gives probability at most `h/D_p` that
`F'(xi)=eta`. Sum the profiles. Apply the rank-two and rank-three atom
`1/D_p` from CMR96 and use the invariant cancellation CMR101. ∎

The direct child-prefix descent target is therefore replaced by a precise
vertical-pencil target: control `V(A)` through secant-shadow structure or add a
bank that randomizes these child translations more efficiently. The finite
identity checks are in
[`scripts/verify_prime_power_child_translation_pencils.py`](../scripts/verify_prime_power_child_translation_pencils.py).
