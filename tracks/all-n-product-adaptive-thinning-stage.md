# All-n product track: adaptive ambient thinning stage

**Branch:** `research/all-n-product-construction`

This stage continues the packet and support-sector program through PX224.  The
new observation is scale-sensitive: endpoint thinning need not use the fixed
probability `t^(-1/2)`.  Because support-four creation is quadratic in the
retention probability while guaranteed endpoint destruction is linear, an
ambient-dependent choice lowers the arithmetic support-four threshold to the
square-root scale.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| General-`q` weighted thinning | **COMPLETE** | PX201 already works for every `q`; PX225 inserts the sharper rank-two denominator and ambient divisor weight. |
| Ambient support four above `N^(1/2+epsilon)` | **CONTROLLED** | PX226 chooses `q=min(1/log(2t),t/(1024e^(4Delta)N mathfrak d(N)))` and obtains expected support four at most `s/2`. |
| Internal rank three under adaptive thinning | **CONTROLLED ASYMPTOTICALLY** | PX227 gives `O(e^(4Delta)s)` expected internal collateral. |
| Rank-two support two | **CONTROLLED** | PX227 gives an order-independent `64e^(4Delta)L_Z` bound. |
| Rank-two support three | **CONTROLLED ASYMPTOTICALLY** | PX227 gives at most `256e^(4Delta)L_Zs`. |
| Packet range | **REDUCED** | Packet extraction and diffuse-defect analysis are required only for `t<=N^(1/2+o(1))`. |
| Rank-one external load | **OPEN** | One replacement plus two background points still lacks a usable strict-descent constant. |
| Minimal-support rank three | **OPEN** | Directed three-cycle and other constant-scale coefficients are not yet paid. |
| Strict depth-two descent | **OPEN** | Linear-order bounds are known, but constants do not yet force net improvement. |
| Infinite exact closure | **OPEN** | No terminating all-side doubling theorem follows yet. |

## 1. Adaptive support-four estimate

For any `q` with `qt>=32`, PX225 selects a block of order

\[
s\ge\frac{qt}{2}
\]

and proves

\[
\mathbb E T_{2,4}
\le
128e^{4\Delta}q^2|Z|\mathfrak d(N).
\]

For a saturated background,

\[
\frac{\mathbb E T_{2,4}}s
\le
512e^{4\Delta}\frac{qN\mathfrak d(N)}t.
\]

The gain relative to destroyed endpoint mass is therefore linear in `q`.

## 2. Optimized thinning probability

Set

\[
B_\Delta=\max(32,16\Delta),
\qquad
C_\Delta=1024e^{4\Delta}
\]

and choose

\[
q_*
=
\min\left\{
\frac1{\log(2t)},
\frac{t}{C_\Delta N\mathfrak d(N)}
\right\}.
\]

If

\[
\frac{t}{\log(2t)}\ge B_\Delta
\]

and

\[
t^2\ge B_\Delta C_\Delta N\mathfrak d(N),
\]

then the retained order is large enough for spread and

\[
\mathbb E T_{2,4}\le\frac{s}{2}.
\]

At fixed depth, `mathfrak d(N)=N^(o(1))`, so every block with

\[
t\ge N^{1/2+\epsilon}
\]

lies in the controlled range for sufficiently large `N`.

## 3. Other sectors

The cap `q<=1/log(2t)` simultaneously controls the internal rank-three support
sectors.  PX227 combines PX189, PX201, and PX196 to obtain scales

\[
O(1),
\qquad
O(qt),
\qquad
O(q^2t\log t),
\qquad
O(q^3t\log t),
\]

all of which are `O(s)`.

The same calculation gives

\[
\mathbb E T_{2,2}
\le64e^{4\Delta}L_Z
\]

and

\[
\mathbb E T_{2,3}
\le256e^{4\Delta}L_Zs.
\]

Thus support four is no longer the asymptotic rank-two obstruction above the
square-root ambient scale.

## 4. Remaining proof tasks

1. **Adaptive rank-one estimate.** Apply the general support-sector thinning law
   to one-cell/two-background certificates and obtain an ambient or packet bound
   on their original weighted count.
2. **Constant sharpening.** Replace the crude `e^(4Delta)` cylinder constant on
   unions of two or three partial matchings.
3. **Support-three constant descent.** Use decoder geometry to improve the
   coefficient of the linear support-three term.
4. **Directed three-cycle core.** Bound or explicitly forbid the undamped
   rank-three support-three sector.
5. **Small-block packet descent.** Continue the defect-heavy/diffuse packet
   analysis only in the reduced range `t<=N^(1/2+o(1))`.
6. **Depth-two accounting.** Combine adaptive thinning, packet release, and
   loaded-line/clean-star destruction with exact constants.
7. **Closure conversion.** Insert a terminating decoder into PX63.

The immediate frontier is item 1 or item 4.  The former
`N^(1/2+epsilon)<t<N^(2/3+epsilon)` support-four interval is now closed.

## 5. Verification

```bash
python scripts/verify_product_adaptive_thinning.py
```

The verifier checks the general-`q` rank-two denominator, optimized retention
probability, square-root ambient exponent, and all rank-two/rank-three sector
scales used by PX225--PX227.

The classical no-three-in-line conjecture and infinite product closure remain
open.
