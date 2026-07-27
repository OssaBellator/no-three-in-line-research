# The `3/41` divisor witness lowers the cutoff to `10^2874`

PX952--PX955 sharpen the exact product constant for `alpha=8/109` and reach the
least integral decimal cutoff certified by that fixed witness. A nearby rational
exponent improves the balance between the finite Euler-product constant and the
retained-order exponent.

Take

\[
\alpha=\frac3{41}.
\]

Only primes satisfying

\[
p^3<2^{41}
\]

contribute.

## 1. Exact local maxima and product interval

For each contributing prime define

\[
a_{3/41}(p)
=
\min\{a\ge0:(a+2)^{41}\le p^3(a+1)^{41}\}.
\]

### Theorem PX962 -- PROVED FINITE/ARITHMETIC

There are exactly `1549` contributing primes, the largest is `13003`, and

\[
1\le a_{3/41}(p)\le19.
\]

The exact integer products satisfy

\[
10^{2468}\prod_p p^{3a_{3/41}(p)}
\le
\prod_p(a_{3/41}(p)+1)^{41}
<
10^{2469}\prod_p p^{3a_{3/41}(p)}.
\]

Consequently

\[
10^{2468/41}
\le C_{3/41}<
\boxed{10^{2469/41}}.
\]

### Proof

The forty-first power of the consecutive local ratio is

\[
\frac{(a+2)^{41}}{p^3(a+1)^{41}},
\]

so each local sequence increases up to the stated threshold and is
nonincreasing afterward. Exact prime enumeration gives the counts and exponent
range. Direct arbitrary-precision comparison of the two integer products proves
the decimal interval. \(\square\)

## 2. Improved ambient divisor cap

### Corollary PX963 -- PROVED

For every integer `N>=2`,

\[
\boxed{
\mathfrak d(N)<10^{2469/41}N^{6/41}.
}
\]

### Proof

Every integer in the ambient divisor maximum is below `N^2`. Apply the universal
Euler-product theorem PX466 with `alpha=3/41` and PX962. \(\square\)

## 3. Retained-order exponent

The divisor-controlled retained-order quantity now has polynomial exponent

\[
\frac65-1-rac6{41}
=
\boxed{\frac{11}{205}}.
\]

This exponent is slightly larger than `29/545` from the `8/109` witness, while
the exact product constant remains small enough to improve the cutoff.

## 4. New common cutoff

### Theorem PX964 -- PROVED FINITE/ARITHMETIC

Every active paired asymptotic repair inequality holds for every

\[
\boxed{N\ge10^{2874}}.
\]

Thus the common cutoff may be replaced by

\[
\boxed{N_5=10^{2874}}.
\]

### Proof

At `N_5`, the exact nested-depth plateau gives

\[
d_*(N_5)=15,
\qquad
\Delta_*(N_5)=33.
\]

Using PX963, the starting logarithmic margins are:

- logarithmic retained-order margin greater than `3805.40`;
- divisor-controlled retained-order margin greater than `0.00447`;
- four-return margin greater than `12.427`;
- two-variable-return margin greater than `426.14`;
- terminal-partner margin greater than `6613.41`.

Across the exact-depth plateau, the divisor-controlled ratio increases with
derivative `11/205`. At the smooth-envelope handoff its margin is greater than
`119.86`, and

\[
\frac{11}{205}-6\overline\Delta'(9000)>0.
\]

The other derivative bounds are unchanged from PX954. Hence every inequality
persists for all larger orders. \(\square\)

At `N=10^2873`, the same divisor-controlled logarithmic margin is less than
`-0.119`. Therefore `2874` is the least integral decimal exponent certified by
the fixed `3/41` witness and the current paired inequalities.

## 5. Revised finite-range frontier

### Corollary PX965 -- PROVED REDUCTION

The active asymptotic path may use

\[
\mathfrak d(N)<10^{2469/41}N^{6/41}
\]

and the cutoff

\[
\boxed{N\ge10^{2874}}.
\]

The remaining all-side obstruction is the finite interval below `10^2874`.
This one-decimal improvement confirms that universal divisor-exponent tuning is
near a flat optimum. Material progress now requires a structural finite-range
bridge, a produced-base iteration theorem, interval-specific divisor estimates,
or a stronger retained-order inequality.

This arithmetic reduction is independent of the side-seven finite selector
census and does not prove the no-three-in-line conjecture.

## 6. Verification

```bash
python scripts/verify_product_three_forty_first_divisor_cutoff.py
```

The verifier checks all `1549` local maxima, both exact forty-first-power product
comparisons, the cutoff margins at `10^2874`, the failure at `10^2873`, and the
smooth-envelope handoff.
