# Maximal-deficiency terminal Hall cores admit principal trimming

PX270 shows that an order-`m` forbidden graph of maximum degree `Delta` has
matching deficiency at most `2Delta-m`. PX281 treats the first nontrivial case
`m=2Delta-1`. The same cross-block absorber works whenever the Hall deficiency
attains its maximum possible value.

Write

\[
m=2\Delta-r,
\qquad 1\le r<\Delta.
\]

## 1. Extremal Hall geometry

### Theorem PX284 -- PROVED

Assume the allowed graph has deficiency

\[
\boxed{\delta(G)=r=2\Delta-m.}
\]

Then every maximum-deficiency Hall witness from PX270 has sides

\[
\boxed{|S|=|B|=\Delta}
\]

and the forbidden rectangle `S times B` saturates every vertex of `S union B`.
Moreover

\[
\boxed{|S\cap B|\ge r.}
\]

For every set `X subseteq S cap B` of size `r`, the principal residual label set

\[
J=[m]\setminus X
\]

has an allowed perfect matching.

More explicitly,

\[
(S\setminus X)\times([m]\setminus B)
\]

and

\[
([m]\setminus S)\times(B\setminus X)
\]

are complete allowed bipartite graphs with equal side size

\[
\boxed{\Delta-r=m-\Delta.}
\]

### Proof

PX270 gives

\[
|S|+|B|=m+\delta(G)=2\Delta.
\]

Since both side sizes are at most `Delta`, both equal `Delta`. Hence every row
of `S` and every column of `B` is saturated inside the complete forbidden
rectangle. Also

\[
|S\cap B|
\ge |S|+|B|-m
=2\Delta-(2\Delta-r)
=r.
\]

Choose `X subseteq S cap B` with `|X|=r`. Saturation makes both displayed
cross-blocks completely allowed, and

\[
|S\setminus X|=\Delta-r=|[m]\setminus B|,
\]

\[
|[m]\setminus S|=\Delta-r=|B\setminus X|.
\]

Perfectly match each cross-block and take the union. \(\square\)

## 2. Decoder consequence

### Corollary PX285 -- PROVED

A maximally deficient terminal endpoint block can leave exactly `r` common
Hall-core labels fixed and rematch every other endpoint. The number moved is

\[
\boxed{m-r=2(m-\Delta).}
\]

If one designated certificate is assigned injectively to every endpoint, the
causal designated coordinate decreases by at least `m-r`, and no paid ancestor
certificate returns.

### Proof

Apply PX284 and then PX278. \(\square\)

Thus the worst Hall deficiency is the easiest near-threshold case
geometrically: it exposes a saturated core and an explicit principal absorber.

## 3. Extremal-or-compressed dichotomy

### Corollary PX286 -- PROVED

For `m=2Delta-r`, every terminal forbidden graph satisfies one of the following.

1. **Extremal deficiency.** `delta(G)=r`, and PX284 gives a principal absorber
   moving `m-r` endpoints.
2. **Subextremal deficiency.** `delta(G)<=r-1`, so an allowed maximum matching
   covers at least

   \[
   \boxed{m-r+1}
   \]

   rows and columns.

The second matching need not be principal, but its unmatched support is
strictly smaller than the worst Hall bound and can be passed to the coupled-
block optimizer PX274.

### Proof

PX270 gives `delta(G)<=r`. Separate equality from strict inequality. \(\square\)

PX284--PX286 reduce the nonprincipal terminal frontier to subextremal Hall
cores. Every maximally deficient core is now absorbed explicitly.

## 4. Verification

Run

```bash
python scripts/verify_product_maximal_deficiency_absorber.py
```

The verifier exhausts all forbidden graphs through order four, checks every
near-threshold graph whose deficiency reaches `2Delta-m`, and verifies the
principal matching after deleting every admissible common-label set `X`.
