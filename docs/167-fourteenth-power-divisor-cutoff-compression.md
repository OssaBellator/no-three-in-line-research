# A fourteenth-power divisor witness further compresses the cutoff

PX466 permits any exponent `alpha`.  The first effective cutoff used
`alpha=1/12`, giving divisor exponent `1/6` in the ambient parameter.  That
choice has a relatively small Euler-product constant, but it is not optimal for
the actual cutoff.  Taking

\[
\alpha=\frac1{14}
\]

increases the finite constant while improving the polynomial retained-order
margin from `1/30` to `2/35`.  The exponent gain dominates.

## 1. Exact local maxima

Only primes

\[
p<2^{14}=16384
\]

contribute to the finite Euler product.  For each such prime define

\[
a_{14}(p)
=
\min\left\{a\ge0:(a+2)^{14}\le p(a+1)^{14}\right\}.
\]

### Theorem PX483 -- PROVED FINITE/ARITHMETIC

For every prime `p<16384`, the local maximum is attained at `a_14(p)`:

\[
\boxed{
\max_{a\ge0}\frac{a+1}{p^{a/14}}
=
\frac{a_{14}(p)+1}{p^{a_{14}(p)/14}}.
}
\]

There are exactly `1900` contributing primes and

\[
1\le a_{14}(p)\le19.
\]

### Proof

For

\[
f_p(a)=\frac{a+1}{p^{a/14}},
\]

the fourteenth power of the consecutive ratio is

\[
\left(\frac{f_p(a+1)}{f_p(a)}\right)^{14}
=
\frac{(a+2)^{14}}{p(a+1)^{14}}.
\]

Thus the sequence increases until the first displayed inequality holds and is
nonincreasing afterward.  Exact integer enumeration gives the prime and exponent
counts. \(\square\)

## 2. Finite Euler-product certificate

### Theorem PX484 -- PROVED FINITE/ARITHMETIC

The exact integer products satisfy

\[
\boxed{
\prod_{p<16384}(a_{14}(p)+1)^{14}
<
10^{1008}
\prod_{p<16384}p^{a_{14}(p)}.
}
\]

Consequently

\[
\boxed{C_{1/14}<10^{72}.}
\]

### Proof

The left product has 8218 decimal digits and the prime-power denominator has
7218 decimal digits.  Direct arbitrary-precision integer comparison proves the
stated inequality.  Taking fourteenth roots gives the result.  The sharper
numerical logarithm is approximately `71.421 log(10)`, leaving visible slack.
\(\square\)

## 3. Improved ambient divisor cap

### Corollary PX485 -- PROVED

For every integer `N>=2`,

\[
\boxed{
\mathfrak d(N)\le10^{72}N^{1/7}.
}
\]

### Proof

Every integer in the defining maximum satisfies `m<N^2`.  Apply PX466 and
PX484:

\[
\tau(m)
<10^{72}(N^2)^{1/14}
=10^{72}N^{1/7}.
\]

\(\square\)

## 4. Improved retained-order exponent

Keep

\[
T(N)=\lceil N^{3/5}\rceil.
\]

### Theorem PX486 -- PROVED REDUCTION

With PX485, the divisor-controlled retained-order quantity satisfies

\[
\boxed{
\frac{T(N)^2}{N\mathfrak d(N)}
\ge
10^{-72}N^{2/35}.
}
\]

The exponent improves because

\[
\frac65-1-\frac17
=
\boxed{\frac2{35}}.
\]

### Proof

Use `T(N)>=N^(3/5)` and PX485. \(\square\)

## 5. New common cutoff

### Theorem PX487 -- PROVED FINITE/ARITHMETIC

All active paired asymptotic repair inequalities hold for every

\[
\boxed{N\ge10^{2950}.}
\]

Hence the common cutoff in PX482 may be replaced by

\[
\boxed{N_2=10^{2950}.}
\]

### Proof

At `N_2`, the exact nested depth remains

\[
d_*(N_2)=15,
\qquad
\Delta_*(N_2)=33.
\]

The logarithm of the divisor-controlled retained-order ratio is

\[
-\log12+
\frac{2}{35}(2950\log10)
-
\log32768-\log256-72\log10-198,
\]

which is greater than `5.9`.  The logarithmic retained-order ratio has log
margin greater than `3900`; the four-return ratio has margin greater than `13`;
and the terminal partner ratio has margin greater than `6700`.

On the interval from `10^2950` to `e^9000`, the exact degree stays thirty-three.
The divisor-controlled ratio increases with derivative `2/35`, and the other
ratios have positive derivatives as in PX481.

For `log N>=9000`, use the smooth degree envelope PX474.  The divisor-controlled
logarithmic derivative is bounded below by

\[
\frac2{35}-6\overline\Delta'(\log N)
>
\frac2{35}-\frac{18}{\log N}>0.
\]

The smooth lower-bound ratio is already positive at the handoff.  Therefore all
inequalities remain valid for every larger order. \(\square\)

This is still far from a practical finite census.  It demonstrates that the
finite frontier is sensitive to the optimized divisor witness, and that further
choices of `alpha` should be compared before pursuing enumeration.

## 6. Verification

Run

```bash
python scripts/verify_product_fourteenth_divisor_cutoff.py
```

The verifier enumerates the 1900 primes below 16384, checks every exact local
maximum and the 14th-power integer certificate, verifies the `2/35` exponent,
and checks the log-domain cutoff margins and monotonicity at `10^2950`.
