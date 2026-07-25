# All-n product track: optimized bounded-forbidden spread stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`tracks/all-n-product-small-sector-constants-stage.md`](all-n-product-small-sector-constants-stage.md).
PX228--PX231 close the rank-one and minimal-support asymptotic gaps.  PX232--
PX234 now improve the universal allowed-matching cylinder factor from
`e^(4Delta)` to an order-sensitive constant tending to `e^Delta`.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Bounded-forbidden family density | **SHARPENED** | PX232 gives density at least `1/mathcal C(t,Delta)` with `mathcal C(t,Delta)=(1-1/(t-4Delta))^(-Delta t)`. |
| Uniform fixed-depth spread | **SHARPENED** | `mathcal C(t,Delta)<=e^(2Delta)` for `t>=8Delta+2`, and tends to `e^Delta`. |
| Conditioned spread | **SHARPENED** | PX233 preserves the optimized factor after arbitrary compatible exposure. |
| Adaptive support four | **UPGRADED** | PX234 replaces the `e^(4Delta)` threshold loss by `e^(2Delta)`. |
| Rank-one sector | **DECODER-OR-LINEAR** | PX228--PX229, now with the improved cylinder factor. |
| Rank-two support two | **CONSTANT SCALE** | At most `mathcal C(s,Delta)L_Z/2`. |
| Rank-two support three | **LINEAR** | At most `mathcal C(s,Delta)L_Z(s-2)`. |
| Rank-three support three | **CONSTANT SCALE** | At most `mathcal C(s,Delta)/3`. |
| Strict net descent | **OPEN** | The spread exponent is improved, but exact destruction coefficients are still needed. |
| Infinite exact closure | **OPEN** | No terminating all-side doubling theorem follows yet. |

## 1. Optimized witness

For the canonical singleton bad events, PX232 uses

\[
x=\frac1{t-4\Delta}.
\]

At `t>=8Delta`, Bernoulli's inequality gives

\[
x(1-x)^{2\Delta}
\ge
\frac1t.
\]

The resulting family density is at least

\[
\left(1-\frac1{t-4\Delta}\right)^{\Delta t}
=
\frac1{\mathcal C(t,\Delta)}.
\]

Hence every compatible rank-`r` cylinder satisfies

\[
\Pr(E\subseteq M)
\le
\frac{\mathcal C(t,\Delta)}{(t)_r}.
\]

At fixed `Delta`,

\[
\mathcal C(t,\Delta)
=
e^{\Delta+O(\Delta^2/t)}.
\]

## 2. Uniform and conditioned envelopes

When `t>=8Delta+2`,

\[
\mathcal C(t,\Delta)\le e^{2\Delta}.
\]

After exposing a compatible partial matching, the same formula applies in the
residual order.  Thus all sequential estimates retain the improved constant.

## 3. Updated sector constants

For retained order `s>=8Delta+2`, PX234 gives

\[
\mathbb E T_{1,2}
<
e^{2\Delta}Km(s-1),
\]

\[
\mathbb E T_{2,2}
\le
\frac12e^{2\Delta}L_Z,
\]

\[
\mathbb E T_{2,3}
\le
e^{2\Delta}L_Z(s-2),
\]

and

\[
\mathbb E T_{3,3}
\le
\frac13e^{2\Delta}.
\]

The adaptive support-four probability becomes

\[
q_*
=
\min\left\{
\frac1{\log(2t)},
\frac{t}{1024e^{2\Delta}N\mathfrak d(N)}
\right\}.
\]

## 4. Remaining proof tasks

1. **Exact destruction ledger.** Record the minimum old-triple mass destroyed by
   every clean star, loaded line, radial core, and packet release.
2. **Linear sign theorem.** Compare those destruction coefficients against the
   optimized rank-one and support-three creation constants.
3. **Actual degree-two constant.** Specialize further to the union of two
   forbidden permutation layers, where the exact density may be closer to
   `e^(-2)`.
4. **Small-block packet descent.** Resolve diffuse selected defects for
   `t<=N^(1/2+o(1))`.
5. **Depth-two negative drift.** Assemble all sectors under the conditioned
   optimized spread law.
6. **Closure conversion.** Insert a terminating decoder into PX63.

The immediate frontier is item 1.  The probabilistic constant is no longer the
four-exponent loss used by the earlier ledger.

## 5. Verification

```bash
python scripts/verify_product_optimized_spread.py
```

The verifier checks the optimized witness, exact density factor, monotonicity,
`e^(2Delta)` envelope, conditioned residual constants, and every substitution
in PX234.

The classical no-three-in-line conjecture and infinite product closure remain
open.
