# Top-digit collision blocks and permutation banks

The linear displacement obstruction from CMR14 is highly structured. This
chapter identifies the exact blocks carrying it and installs a full local
permutation bank on those blocks.

Let

\[
N=p^k,
\qquad p\text{ odd},
\qquad k\ge2,
\qquad a=p^{k-1}=N/p,
\]

and let \(R_{\mathbf c}\) be a completed reciprocal channel. Write \(c_0\)
for its unit-stratum parameter.

## 1. Unit columns split into top-digit blocks

For each unit residue

\[
\xi\in\{0,\ldots,a-1\},
\qquad p\nmid\xi,
\]

define

\[
X_\xi=\{\xi+ja:0\le j<p\}.
\]

These sets partition the unit columns of \(\mathbb Z_N\).

Choose an inverse `u` of \(\xi\) modulo `N`. Since

\[
a^2=p^{2k-2}\equiv0\pmod {p^k},
\]

the first-order inverse expansion is exact modulo `N`:

\[
(\xi+ja)^{-1}
\equiv
u-ja u^2
\pmod N.
\]

Put

\[
q_\xi\equiv c_0u^2\pmod p.
\]

Then

\[
R_{\mathbf c}(\xi+ja)
\equiv
c_0u-jq_\xi a
\pmod N.
\]

## 2. Exact block decomposition

### Theorem CMR15 — PROVED

The unit-stratum graph of \(R_{\mathbf c}\) decomposes into

\[
\varphi(a)=(p-1)p^{k-2}
\]

pairwise row- and column-disjoint blocks

\[
B_\xi
=
\{(x,R_{\mathbf c}(x)):x\in X_\xi\},
\]

each containing exactly `p` points.

For each block:

1. its columns are one residue class modulo `a`;
2. its rows are one residue class modulo `a`;
3. the high base-`p` row digit is an affine permutation of the high column
   digit with slope \(-q_\xi\);
4. every pair with column difference `a` lies inside one block.

Distinct column blocks have distinct row blocks.

### Proof

The sets \(X_\xi\) plainly partition the unit columns. The displayed inverse
expansion shows that every row in `B_ξ` has the same residue

\[
c_0u\pmod a,
\]

while its high digit changes by the nonzero slope \(-q_\xi\) modulo `p`.
Hence the `p` rows are distinct.

Reduction modulo `a` sends the row block of `ξ` to

\[
c_0\xi^{-1}\pmod a.
\]

Inversion and multiplication by the unit `c_0` permute the unit residues
modulo `a`, so distinct column blocks have distinct row blocks. Finally,
columns differing by `a` have the same residue modulo `a`, hence belong to the
same block. ∎

Thus the repeated displacements from CMR14 are internal block collisions, not
an unstructured global codegree failure.

## 3. Full local permutation bank

For a permutation \(\pi\in S_p\), define the block state

\[
B_{\xi,\pi}
=
\left\{
\bigl(\xi+ja,
R_{\mathbf c}(\xi+\pi(j)a)
\bigr):0\le j<p
\right\}.
\]

### Theorem CMR16 — PROVED

Every block state uses exactly the same `p` columns and the same `p` rows as
the original block. Choices on distinct blocks are independent and may be
combined arbitrarily. Consequently the unit stratum supports

\[
(p!)^{\varphi(a)}
\]

row-column-preserving global states.

Under the product measure that chooses an independent uniform permutation in
each block, a compatible prescription of `r_ξ` distinct cells in block `ξ`
has exact probability

\[
\prod_\xi\frac{1}{(p)_{r_\xi}},
\]

where

\[
(p)_r=p(p-1)\cdots(p-r+1).
\]

### Proof

A block permutation only reassigns its existing row set to its existing
column set. CMR15 gives pairwise disjoint column and row supports, so block
choices cannot interfere and their union remains a permutation of all unit
rows and columns.

For a uniform permutation on `p` symbols, `r` compatible prescribed images
occur with probability

\[
\frac{(p-r)!}{p!}=\frac1{(p)_r}.
\]

Independence across blocks gives the product formula. ∎

## 4. Decoder significance

CMR14 rules out a global bounded-displacement theorem, but CMR15–CMR16 replace
that failed endpoint by a collision-aware block model:

- the offending top-digit vectors never connect different blocks;
- every block has a full `p!` executable state space;
- the state measure has exact finite-rank spread;
- contracting each block removes the deterministic multiplicity before the
  remaining cross-block secants are counted.

The unresolved theorem is now precise: prove that after contracting or
randomizing the top-digit blocks, the cross-block secant shadow and mixed
triple load satisfy a repairable weighted bound. For the two-layer companion
host, one must additionally avoid the companion matching inside each block.

The finite checks are in
[`scripts/verify_prime_power_top_digit_blocks.py`](../scripts/verify_prime_power_top_digit_blocks.py).
