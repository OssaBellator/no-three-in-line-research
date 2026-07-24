# A no-double-charge ledger for joint parent blocks

CMR166--CMR168 bound the total collateral of all inherited joint-parent banks.
The remaining packing question is how often one current triple is charged when
parent blocks are summed over the prefix tree. The answer is exact: at one
scale, a triple is counted once for each distinct column-prefix block occupied
by its three points, and therefore at most three times.

## 1. Exact scale ledger

Fix a saturated recursive state `S` and one nonroot scale `s`. For each column
prefix `a mod p^s`, let

\[
J_{s,a}=A_{s,a,0}\cup A_{s,a,1}
\]

be the two-layer joint block. Define its exact destroyed population

\[
D_{s,a}
=
\Phi(S)-\Phi(S\setminus J_{s,a}).
\]

For a real triple `Q` selected by `S`, let `b_s(Q)` be the number of distinct
scale-`s` column-prefix blocks occupied by its three points.

### Theorem CMR169 — PROVED

At every scale,

\[
\boxed{
\sum_{a\bmod p^s}D_{s,a}
=
\sum_{Q\in\mathcal T(S)}b_s(Q).
}
\]

Consequently

\[
\boxed{
\Phi(S)
\le
\sum_aD_{s,a}
\le
3\Phi(S).
}
\]

### Proof

A triple contributes to `D_{s,a}` exactly when at least one of its points lies
in `J_{s,a}`. The joint blocks partition the selected points according to their
column prefix. Hence the number of blocks to which one triple contributes is
exactly `b_s(Q)`. Since a three-point set occupies between one and three
blocks, the inequalities follow. ∎

This is the canonical no-double-charge rule; it does not depend on how a
terminal four-core chose its target point.

## 2. Frozen-block inequality

Let `C_{s,a}` be the expected new-triple collateral of the appropriate
old-cell-clean joint bank on `J_{s,a}`:

- CMR165 for a nonroot disjoint-fibre block;
- CMR156 for a root or other general block where that bank is used.

### Theorem CMR170 — PROVED

If no state of the joint bank on any scale-`s` block lowers the current triple
potential, then

\[
\boxed{
\Phi(S)
\le
\sum_aD_{s,a}
\le
\sum_aC_{s,a}.
}
\]

If no nonroot joint-parent bank lowers the current potential at any scale, then

\[
\boxed{
(k-1)\Phi(S)
\le
\sum_{s=1}^{k-1}\sum_aC_{s,a}.
}
\]

### Proof

For one block, exact old-cell destruction gives expected potential change

\[
-D_{s,a}+C_{s,a}.
\]

If every bank state is nonimproving, its expectation is nonnegative, so
`D_{s,a}<=C_{s,a}`. Sum the blocks and use CMR169. Summing the first inequality
over the `k-1` nonroot scales proves the multiscale statement. ∎

No target or quotient signature is charged more than three times at one scale.
The only repetition left is the intentional one copy per ancestor scale.

## 3. Explicit frozen-state endpoints

### Corollary CMR171 — PROVED

For a corrected balanced reciprocal bank at fixed `p=1 mod 4`, choose a state
whose total nonroot joint-parent collateral is no greater than the CMR166
expectation. If that state is frozen under every nonroot joint-parent bank, then

\[
\boxed{
\Phi(S)
<
\left[
4\left(6k+p+1+\frac1{3p}\right)
+
16\left(2+\frac1p\right)
\right]N^2.
}
\]

For the balanced prime-seven bank, the corresponding frozen endpoint is

\[
\boxed{
\Phi(S)
<
\frac{216k+360}{7}N^2.
}
\]

### Proof

Apply CMR170 and divide the CMR166 or CMR167 all-scale collateral bound by
`k-1`. The strict signs inherit the strict one-scale rank-one and cross-rank
bounds. ∎

These estimates are the same quadratic-logarithmic order as the initial
syndrome, but their meaning is stronger: they apply after ruling out every
inherited joint-parent improvement, and the accounting has no hidden overlap.

## 4. Revised remaining endpoint

The joint-parent packing problem is closed. The remaining obstruction is not
repeated charging; it is the absence of a strict gap between

- the exact destroyed population `D_{s,a}`; and
- the expected collateral `C_{s,a}`

for at least one ancestor block.

A complete escape theorem now needs one additional structural input, for
example:

1. a target-rich block in which `D_{s,a}` exceeds the rank-one quotient shadow;
2. a strict inherited carry-signature loss on a terminal component;
3. a product resampling of several disjoint joint blocks which beats the sum of
   their separate expectations;
4. a reverse-scale potential which values destruction at the target's owner
   more highly than fine collateral.

No all-`n` theorem is claimed here. The exact block-occupancy identity and the
explicit divisions of the all-scale bounds are checked in
[`scripts/verify_prime_power_joint_parent_packing.py`](../scripts/verify_prime_power_joint_parent_packing.py).
