# Exact collateral formula for the top-digit block bank

CMR17 supplies an executable product measure on saturated two-layer states.
This chapter records the exact first-moment decoder associated with that
measure.

Fix a prime power \(N=p^k\), \(k\ge2\). Keep the companion layer
\(g=\sigma_p\circ R_{\mathbf c}\) fixed. In the first layer, keep every
nonunit point fixed and independently choose a uniform permutation state in
every top-digit unit block from CMR15.

Let \(\mathcal B\) denote the family of movable blocks. For a block `B`, its
candidate cells form the complete bipartite graph between its `p` columns and
its `p` rows.

## 1. Compatible triple certificates

A **certificate** is a real-collinear triple of cells drawn from:

- fixed companion cells;
- fixed nonunit first-layer cells;
- movable block candidate cells.

A certificate is compatible if, inside every movable block, its prescribed
cells have distinct columns and distinct rows. For a compatible certificate
`T`, let

\[
r_B(T)\in\{0,1,2,3\}
\]

be the number of its movable cells in block `B`, and define

\[
w(T)=\prod_{B\in\mathcal B}\frac1{(p)_{r_B(T)}}.
\]

For an incompatible certificate, put \(w(T)=0\).

## 2. Exact product-bank expectation

### Theorem CMR18 — PROVED

Let \(\Phi\) be the number of real collinear triples in the random saturated
state described above. Then

\[
\mathbb E\Phi
=
\sum_T w(T),
\]

where the sum runs over all real-collinear cell triples in the fixed-plus-
candidate universe.

Consequently there exists an executable saturated state with at most

\[
\mathcal M
:=
\sum_T w(T)
\]

real collinear triples. If a current block state has more than \(\mathcal M\)
triples, some block-bank state strictly improves it. If \(\mathcal M<1\), an
exact saturated no-three state exists.

### Proof

For a compatible certificate `T`, CMR17 gives the exact probability

\[
\Pr[T\text{ is selected}]
=
\prod_B\frac1{(p)_{r_B(T)}}
=w(T).
\]

An incompatible certificate has probability zero. Write \(I_T\) for the
indicator that `T` is selected. Since every selected real triple corresponds
to exactly one certificate,

\[
\Phi=\sum_T I_T.
\]

Linearity of expectation gives the identity. At least one state has potential
at most the average. Since \(\Phi\) is integer-valued, an average below one
forces a state with \(\Phi=0\). ∎

## 3. Normalized certificate classes

The sum naturally splits by movable rank:

\[
\mathcal M=\mathcal M_0+\mathcal M_1+\mathcal M_2+\mathcal M_3.
\]

- \(\mathcal M_0\) counts fixed-only triples and cannot be changed by this
  bank.
- \(\mathcal M_1\) is the one-cell outside secant shadow divided by `p`.
- \(\mathcal M_2\) uses weight `1/(p(p-1))` when both cells lie in one block,
  and `1/p^2` when they lie in two blocks.
- \(\mathcal M_3\) uses `1/(p)_3`, `1/((p)_2p)`, or `1/p^3` according to the
  block collision pattern.

Thus the remaining composite-modulus decoder theorem is fully quantitative:
bound these four normalized masses after the deterministic top-digit
collisions are contracted. The construction of the bank, its executability,
and its probability law are no longer open.

The finite identity check is in
[`scripts/verify_prime_power_block_collateral.py`](../scripts/verify_prime_power_block_collateral.py).
