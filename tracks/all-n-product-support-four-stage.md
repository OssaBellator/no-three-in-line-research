# All-n product track: scale-sensitive support-four stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`tracks/all-n-product-recursive-rematching-stage.md`](all-n-product-recursive-rematching-stage.md)
after PX201--PX206.  Rank-two replacement collateral has been reduced to three
endpoint-support sectors.  Support two is constant-scale after thinning,
support three is linear, and support four was the only apparently superlinear
sector.

PX207--PX209 add the bounded integer grid to the analysis.  For one background
anchor, every support-four collision is an equal-product equation, so divisor
multiplicity controls the complete anchor pencil.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Fixed-anchor support four | **CONTROLLED** | PX207 bounds every anchor pencil by `mathfrak d(N)t^2`, where `mathfrak d(N)=N^(o(1))` is the ambient divisor envelope. |
| Summed background load | **CONTROLLED** | PX208 gives `W_(2,4)<=|Z|mathfrak d(N)t^2`, and `<=2Nmathfrak d(N)t^2` for a saturated background. |
| Large endpoint blocks | **CLOSED ASYMPTOTICALLY** | At fixed recursion depth, `t>=N^(2/3+epsilon)` makes the square-root-thinned support-four expectation `o(s)`. |
| Arithmetic sharpness | **CLASSIFIED** | PX209 gives a geometric-progression endpoint family with one anchor supporting `Theta(t^3)` support-four pairs. |
| Medium and small blocks | **OPEN** | The remaining range is `t<=N^(2/3+o(1))`. |
| Absolute recursion depth | **OPEN** | No theorem yet forces bounded-depth termination across the remaining scales. |
| Infinite exact closure | **OPEN** | No all-side exact doubling theorem follows yet. |

## 1. Equal-product normal form

For an anchor `z=(a,b)`, put

\[
A_i=x_i-a,
\qquad
B_j=y_j-b.
\]

Collinearity of compatible candidate cells `e_(ij)` and `e_(k ell)` is

\[
A_iB_\ell=A_kB_j.
\]

If `r_z(p)` counts representations `A_iB_ell=p`, then

\[
r_z(p)\le2\tau(|p|)
\le2\mathfrak d(N).
\]

Since there are at most `t^2` representations in total, PX207 gives

\[
Q_z\le\mathfrak d(N)t^2.
\]

This bound controls all compatible rank-two pairs through the anchor, not only
support four.

## 2. Large-block payment

Summing the fixed-anchor estimate over the background gives

\[
W_{2,4}
\le
|Z|\mathfrak d(N)t^2.
\]

PX203a and square-root thinning therefore give

\[
\frac{\mathbb E T_{2,4}}s
\le
512e^{4\Delta}
\frac{|Z|\mathfrak d(N)}{t^{3/2}}.
\]

For a saturated background, `|Z|<=2N`, so

\[
\frac{\mathbb E T_{2,4}}s
\le
1024e^{4\Delta}
\frac{N\mathfrak d(N)}{t^{3/2}}.
\]

At fixed recursive depth, `Delta=O(1)` and
`mathfrak d(N)=N^(o(1))`.  Hence every block with

\[
t\ge N^{2/3+\epsilon}
\]

has `o(s)` support-four collateral.  Such blocks no longer need a separate
support-four decoder.

## 3. Sharpness boundary

The fixed-anchor factor cannot be replaced by an absolute constant.  For

\[
x_i=y_i=2^i,
\qquad z=(0,0),
\]

the cells on each fixed ratio line form a long directed-diagonal class.  PX209
counts exactly

\[
2\sum_{d=1}^{t-1}
\left[
\binom{t-d}{2}-\max(t-2d,0)
\right]
=
\Theta(t^3)
\]

support-four pairs through one anchor.

Thus the remaining theorem cannot ignore ambient arithmetic or decoder scale.

## 4. Remaining proof tasks

1. **Medium-block support-four decoder.** For
   `t<=N^(2/3+o(1))`, show that large equal-product energy forces a common ratio
   class, anchor pencil, endpoint-disjoint star, or bounded-support batch.
2. **Block aggregation.** Combine many medium endpoint blocks so their total
   destroyed mass pays the sum of their divisor-controlled collateral.
3. **Extraction amplification.** Prove that repeated PX195 extraction either
   terminates or reaches a block above the `N^(2/3+epsilon)` threshold.
4. **Ratio-structure conversion.** Apply multiplicative-energy or quotient-set
   inverse results to a heavy fixed-anchor product class and convert it to an
   executable rematching bank.
5. **Rank-one and rank-three sectors.** Complete the analogous scale-sensitive
   bounds needed by PX204.
6. **Constant accounting.** Replace the crude `e^(4Delta)` spread factor on the
   actual union-of-few-matchings forbidden graphs.
7. **Depth-two theorem.** Combine the scale split with destroyed-mass estimates
   to prove a bounded recursion depth.
8. **Closure conversion.** Insert the terminating decoder into PX63 while
   preserving factor transport and exact row-column saturation.

The immediate frontier is item 1 or item 2.  The support-four problem is no
longer an all-scale counting problem; it is a medium-block structural problem.

## 5. Verification

```bash
python scripts/verify_product_support_four_divisor.py
```

The verifier checks random fixed-anchor equal-product bounds, exact small-side
divisor envelopes, the geometric-progression cubic formula, and the
`N^(2/3+epsilon)` exponent saving.

The classical no-three-in-line conjecture and infinite product closure remain
open.