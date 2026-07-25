# A rational divisor exponent compresses the cutoff to `10^2900`

PX483--PX487 optimize among simple reciprocal exponents by using `alpha=1/14`.
The finite Euler-product method does not require a reciprocal exponent.  A nearby
rational value substantially lowers the finite product constant while retaining
a positive polynomial margin.

Take

\[
\alpha=\frac8{109}.
\]

Then only primes

\[
p<2^{109/8}<12620
\]

contribute.

## 1. Exact rational local maxima

For each contributing prime define

\[
a_*(p)=
\min\left\{a\ge0:(a+2)^{109}\le p^8(a+1)^{109}\right\}.
\]

### Theorem PX488 -- PROVED FINITE/ARITHMETIC

For every prime `p<2^(109/8)`,

\[
\boxed{
\max_{a\ge0}\frac{a+1}{p^{8a/109}}
=
\frac{a_*(p)+1}{p^{8a_*(p)/109}}.
}
\]

There are exactly `1508` contributing primes, the largest is `12619`, and

\[
1\le a_*(p)\le19.
\]

### Proof

For `f_p(a)=(a+1)/p^(8a/109)`, the 109th power of the consecutive ratio is

\[
\left(\frac{f_p(a+1)}{f_p(a)}\right)^{109}
=
\frac{(a+2)^{109}}{p^8(a+1)^{109}}.
\]

Thus the sequence increases to the first displayed threshold and is
nonincreasing afterward.  The finite counts are exact. \(\square\)

## 2. Exact product certificate

### Theorem PX489 -- PROVED FINITE/ARITHMETIC

The integer products satisfy

\[
\boxed{
\prod_{p<2^{109/8}}(a_*(p)+1)^{109}
<
10^{6431}
\prod_{p<2^{109/8}}p^{8a_*(p)}.
}
\]

Consequently

\[
\boxed{C_{8/109}<10^{59}.}
\]

### Proof

Since `6431=59*109`, the displayed exact integer comparison is precisely the
109th power of the desired bound.  The numerator and denominator have 50941 and
44516 decimal digits respectively.  Arbitrary-precision comparison proves the
certificate.  The sharper numerical value is approximately
`58.945 log(10)`. \(\square\)

## 3. Improved ambient divisor cap

### Corollary PX490 -- PROVED

For every integer `N>=2`,

\[
\boxed{
\mathfrak d(N)\le10^{59}N^{16/109}.
}
\]

### Proof

Every integer in the divisor maximum is below `N^2`.  Apply PX466 and PX489:

\[
\tau(m)
<10^{59}(N^2)^{8/109}
=10^{59}N^{16/109}.
\]

\(\square\)

## 4. Retained-order margin

Keep `T(N)=ceil(N^(3/5))`.

### Theorem PX491 -- PROVED REDUCTION

The divisor-controlled retained-order quantity satisfies

\[
\boxed{
\frac{T(N)^2}{N\mathfrak d(N)}
\ge
10^{-59}N^{29/545}.
}
\]

Indeed,

\[
\frac65-1-\frac{16}{109}
=
\boxed{\frac{29}{545}}>0.
\]

Although `29/545` is slightly smaller than the `2/35` exponent from PX486, the
Euler-product constant drops from `10^72` to `10^59`.

## 5. New common cutoff

### Theorem PX492 -- PROVED FINITE/ARITHMETIC

Every active paired asymptotic repair inequality holds for every

\[
\boxed{N\ge10^{2900}.}
\]

Thus the current common cutoff is

\[
\boxed{N_3=10^{2900}.}
\]

### Proof

At `N_3`, the exact nested values remain

\[
d_*(N_3)=15,
\qquad
\Delta_*(N_3)=33.
\]

The divisor-controlled retained-order ratio has logarithm greater than `3.0`.
The logarithmic retained-order ratio has margin greater than `3800`; the
four-return ratio has margin greater than `12`; and the terminal partner ratio
has margin greater than `6600`.

Across the exact-depth plateau, the divisor-controlled ratio increases with
derivative `29/545`.  For `log N>=9000`, the smooth-envelope derivative is at
least

\[
\frac{29}{545}-6\overline\Delta'(\log N)
>
\frac{29}{545}-\frac{18}{\log N}>0.
\]

The smooth lower-bound ratio is already positive at the handoff, so the
inequalities persist for every larger order. \(\square\)

This improvement is modest compared with the remaining finite range.  It
indicates diminishing returns from universal divisor exponents: a structural
finite-range bridge is now more important than further decimal optimization.

## 6. Verification

Run

```bash
python scripts/verify_product_rational_divisor_cutoff.py
```

The verifier checks the 1508-prime local maxima, the exact 109th-power product
certificate, the exponent `29/545`, and all cutoff margins and derivatives at
`10^2900`.
