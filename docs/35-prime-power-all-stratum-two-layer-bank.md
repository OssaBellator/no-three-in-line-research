# All-stratum two-layer top-digit bank

The unit-block analysis extends without loss to every valuation stratum. This
chapter partitions the entire completed-reciprocal companion pair into
`p`-point column blocks and installs an independent full permutation bank in
both layers.

Let

\[
N=p^k,
\qquad k\ge2,
\qquad a=p^{k-1}=N/p,
\]

and let

\[
f=R_{\mathbf c},
\qquad g=\sigma_p\circ f.
\]

## 1. Blocks in every nonterminal valuation stratum

Fix \(0\le r\le k-2\), put

\[
m=k-r,
\qquad s=m-1,
\]

and choose a unit residue

\[
\xi\in\{0,\ldots,p^s-1\}.
\]

Define

\[
X_{r,\xi}
=
\left\{
 p^r(\xi+jp^s):0\le j<p
\right\}.
\]

Choose an inverse `u` of \(\xi\) modulo \(p^m\). Since the square of
\(p^s\) is divisible by \(p^m\),

\[
(\xi+jp^s)^{-1}
\equiv
u-jp^su^2
\pmod {p^m}.
\]

Therefore

\[
f\bigl(p^r(\xi+jp^s)\bigr)
\equiv
p^rc_ru-jq_{r,\xi}a
\pmod N,
\]

where

\[
q_{r,\xi}\equiv c_ru^2\pmod p.
\]

Thus the `p` rows in one block are one residue class modulo `a`, with an
affine high-digit permutation.

## 2. The terminal block

The remaining columns are

\[
X_*=\{0,a,2a,\ldots,(p-1)a\}.
\]

The origin maps to the origin. On the nonzero terminal-stratum columns,

\[
f(ja)=a[c_{k-1}j^{-1}]_p.
\]

Inversion and multiplication by the unit \(c_{k-1}\) permute the nonzero
multiples of `a`. Hence the terminal block also uses exactly `p` columns and
`p` rows.

## 3. Complete block partition

### Theorem CMR19 — PROVED

The graph of `f` decomposes into exactly

\[
a=N/p
\]

pairwise row- and column-disjoint blocks of size `p`:

- \(\varphi(p^{k-r-1})\) blocks in each stratum
  \(0\le r\le k-2\);
- one terminal block containing the origin and valuation-\(k-1\) points.

These blocks partition every column and every first-layer row.

### Proof

Every nonzero column has a unique valuation `r`. For `r<k-1`, its unit part
has a unique lower `m-1` digit residue `ξ` and a unique top digit `j`, placing
it in exactly one \(X_{r,\xi}\). The terminal columns are exactly the multiples
of `a`.

The inverse expansion proves row distinctness inside a nonterminal block. In
one fixed valuation stratum, reduction modulo `a` maps the block label `ξ` to

\[
p^rc_r\xi^{-1}\pmod a,
\]

which is injective on the unit residues modulo \(p^{k-r-1}\). Different
valuation strata have different row valuations. The terminal rows are the
multiples of `a`. Thus all row supports are disjoint.

Finally,

\[
1+\sum_{t=1}^{k-1}\varphi(p^t)
=1+(p^{k-1}-1)
=p^{k-1}=a.
\]

So the listed blocks account for all `N=pa` columns and rows. ∎

## 4. Companion row blocks

For a first-layer row block `Y_B`, define

\[
Z_B=\sigma_p(Y_B).
\]

### Theorem CMR20 — PROVED

The sets \(Z_B\) form a partition of all rows into `a` blocks of size `p`.
For every block `B`,

\[
Y_B\cap Z_B=\varnothing.
\]

### Proof

The map \(\sigma_p\) is a permutation, so it carries the partition
\(\{Y_B\}\) to another row partition. CMR17 proves that no row and its
companion image are congruent modulo `a`. Since every `Y_B` is one residue
class modulo `a`, its image block is disjoint from it. ∎

## 5. Independent full bank in both layers

For every column block `X_B`, choose independently

\[
\pi_B,\tau_B\in S_p.
\]

Assign the first-layer rows `Y_B` to `X_B` according to \(\pi_B\), and the
companion rows `Z_B` to the same columns according to \(\tau_B\).

### Theorem CMR21 — PROVED

Every such choice gives a saturated two-layer configuration with exactly two
distinct points in every row and column. The bank contains

\[
(p!)^{2N/p}
\]

states.

Under independent uniform choices, a compatible cell prescription using
\(r_{B,0}\) first-layer cells and \(r_{B,1}\) companion-layer cells in block
`B` has exact probability

\[
\prod_B
\frac1{(p)_{r_{B,0}}(p)_{r_{B,1}}}.
\]

### Proof

Within each layer, every block retains its row and column sets, and CMR19–20
show those supports partition all rows and columns. Hence each layer remains a
permutation.

At a column in block `B`, the first selected row belongs to `Y_B` and the
second belongs to `Z_B`. These sets are disjoint, so the two cells are
distinct. Thus the union is saturated.

There are `p!` independent choices for each of two layers in each of `N/p`
blocks. The probability formula is the product of the exact uniform
permutation cylinder probabilities. ∎

## 6. Global certificate endpoint

### Corollary CMR22 — PROVED

Let \(\mathcal T\) be the set of all real-collinear triples of candidate cells
in the complete two-layer block universe. Give a compatible certificate `T`
weight

\[
w(T)=
\prod_B
\frac1{(p)_{r_{B,0}(T)}(p)_{r_{B,1}(T)}},
\]

and incompatible certificates weight zero. Then the expected number of real
triples in the random bank state is exactly

\[
\sum_{T\in\mathcal T}w(T).
\]

In particular, a weighted certificate mass below one proves an exact
saturated no-three state.

This removes the fixed-only obstruction present in the unit-only bank: every
point in both layers is now movable. The remaining theorem is purely a
normalized certificate-count bound for this explicit product space.

The finite checks are in
[`scripts/verify_prime_power_all_stratum_bank.py`](../scripts/verify_prime_power_all_stratum_bank.py).
