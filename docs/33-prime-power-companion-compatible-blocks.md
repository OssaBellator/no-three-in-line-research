# Companion-compatible top-digit permutation banks

CMR15–CMR16 install full permutation banks on the top-digit unit blocks of a
completed reciprocal channel. This chapter proves that every one of those
states remains executable when the universal companion layer is fixed.

Let

\[
f=R_{\mathbf c},
\qquad g=\sigma_p\circ f
\]

be the saturated companion pair from CMR4 at the prime power \(N=p^k\), with
\(k\ge2\). Put

\[
a=p^{k-1}.
\]

For odd `p`, recall

\[
\sigma_p(y)=[(1+p)y+1]_N;
\]

for `p=2`, the multiplier increment is `4` instead of `2`.

## 1. The companion leaves every top-digit row block

Each top-digit block \(B_\xi\) from CMR15 has a first-layer row set
\(Y_\xi\) contained in one residue class modulo `a`.

### Theorem CMR17 — PROVED

For every row `y`, the companion row \(\sigma_p(y)\) is not congruent to `y`
modulo `a`. Consequently

\[
\sigma_p(y)\notin Y_\xi
\qquad (y\in Y_\xi).
\]

Therefore every one of the `p!` local permutation states from CMR16 is
disjoint from the fixed companion layer. Independent choices on all unit
blocks preserve exact two-per-row and two-per-column saturation and give

\[
(p!)^{\varphi(a)}
\]

executable two-layer states.

Under the product measure choosing a uniform permutation in every block, a
compatible prescription of `r_ξ` cells in block `ξ` has exact probability

\[
\prod_\xi\frac1{(p)_{r_\xi}}.
\]

### Proof

For odd `p`,

\[
\sigma_p(y)-y\equiv py+1\pmod a.
\]

If this difference vanished modulo `a`, reduction modulo `p` would give
\(1\equiv0\pmod p\), impossible. For `p=2`, the same argument uses

\[
\sigma_2(y)-y\equiv4y+1\pmod a,
\]

which is also odd and therefore nonzero modulo the power of two `a`.

All rows in one block \(Y_\xi\) are congruent modulo `a`. Hence a companion
row of any block row cannot return to the same block row set. Reassigning the
rows inside \(Y_\xi\) therefore cannot select a companion-occupied cell.

CMR16 already proves that arbitrary block permutations retain the same first
layer row and column sets and combine independently. The exact cylinder
probability is unchanged from the full uniform permutation measure. ∎

## 2. Decoder significance

The deterministic linear codegree from CMR14 is now equipped with an exact
executable two-layer repair bank:

- the repeated top-digit vectors are confined to disjoint `p`-point blocks;
- every block supports all `p!` row permutations;
- no state collides with the universal companion layer;
- the product measure has exact \(1/(p)_r\) finite-rank spread.

The next theorem no longer needs to construct or thin a bank. It must bound
the expected cross-block and mixed-layer collateral under this explicit
product measure. The relevant data are normalized one-, two-, and three-cell
certificate counts, matching the collision-aware bank endpoint used elsewhere
in the notebook.

The finite checks are in
[`scripts/verify_prime_power_companion_blocks.py`](../scripts/verify_prime_power_companion_blocks.py).
