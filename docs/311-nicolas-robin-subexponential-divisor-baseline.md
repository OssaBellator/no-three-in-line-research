# The Nicolas--Robin subexponential divisor bound does not improve the active cutoff

The Euler-product power-law family is optimized at decimal cutoff `10^2874` by
PX966--PX969. A qualitatively different possibility is to replace the power-law
divisor estimate by the classical explicit Nicolas--Robin subexponential bound.
This chapter audits that route exactly against the active paired repair
inequalities.

The result is negative but useful: the subexponential estimate becomes effective
too slowly and yields the much worse decimal cutoff `10^14104`.

## 1. External divisor theorem

Nicolas and Robin proved that for every integer `m>=3`,

\[
\frac{\log \tau(m)\,\log\log m}{\log 2\,\log m}<1.538.
\]

The sharp maximum is approximately `1.537939860675...`; the rational constant
`769/500=1.538` is therefore a valid strict upper bound. See J.-L. Nicolas and
G. Robin, *Majorations explicites pour le nombre de diviseurs de N*, Canadian
Mathematical Bulletin 26 (1983), 485--492, DOI `10.4153/CMB-1983-078-5`.

Every integer entering the ambient divisor maximum is below `N^2`. Hence, with
`x=log N`,

\[
\log \mathfrak d(N)
<
\frac{2(769/500)\log 2}{\log(2x)}x.
\]

### Theorem PX994 -- PROVED USING NICOLAS--ROBIN

For every order in the active range,

\[
\boxed{
\log \mathfrak d(N)
<
\frac{(769/250)\log 2}{\log(2\log N)}\log N.
}
\]

This estimate is universal and subexponential, but its effective coefficient is
larger than the optimized power-law coefficient throughout the current cutoff
range.

## 2. Exact retained-order audit

Above the smooth-depth handoff, put

\[
\overline\Delta(x)=7+2\log_2(x/\log2+2).
\]

The divisor-controlled logarithmic margin becomes

\[
M(x)=
\frac{x}{5}
-rac{(769/250)\log2}{\log(2x)}x
-\log\!\left(\frac{32768\cdot256}{\eta}\right)
-6\overline\Delta(x),
\qquad \eta=\frac1{12}.
\]

The verifier evaluates all five active margins with directed high-precision
decimal arithmetic.

### Theorem PX995 -- PROVED FINITE/ARITHMETIC

At consecutive integral decimal orders,

\[
M(14103\log10)<-0.037,
\qquad
M(14104\log10)>0.019.
\]

At `N=10^14104`, every other active paired repair margin exceeds `119`.
Moreover

\[
M'(14104\log10)>0.024.
\]

All negative derivative corrections decrease thereafter, while the other four
margin derivatives have explicit positive lower bounds. Consequently every
active inequality persists for all larger orders.

Thus the Nicolas--Robin input alone gives the valid but weak cutoff

\[
\boxed{N\ge10^{14104}}.
\]

## 3. Route barrier

### Corollary PX996 -- PROVED REDUCTION

The classical universal Nicolas--Robin subexponential divisor estimate does not
improve the active `10^2874` cutoff. It worsens the decimal exponent by more than
a factor of four.

Therefore the finite-range frontier should not be pursued by inserting the
baseline `1.538 log m/log log m` divisor theorem unchanged. Material progress
requires at least one of:

- a substantially sharper interval-specific divisor estimate in the relevant
  range;
- a stronger retained-order inequality with less than one full ambient divisor
  loss;
- a structural extension or absorber chain;
- a produced-base recursive closure theorem.

This audit does not weaken the existing `10^2874` theorem and does not prove an
all-side result.

## 4. Verification

```bash
python scripts/verify_product_nicolas_robin_divisor_baseline.py
```

The verifier checks the failure at decimal order `14103`, success at `14104`,
all four auxiliary margins, and positive derivative bounds ensuring persistence.
