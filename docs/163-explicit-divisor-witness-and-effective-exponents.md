# An explicit divisor witness and effective repair exponents

PX455 leaves one non-effective cutoff input: a numerical bound for

\[
\mathfrak d(N)
=
\max_{1\le m\le(N-1)^2}\tau(m).
\]

A finite Euler-product argument supplies the uniform estimate

\[
\boxed{
\tau(m)\le10^{27}m^{1/12}
}
\]

for every positive integer `m`.  Consequently

\[
\boxed{
\mathfrak d(N)\le10^{27}N^{1/6}.
}
\]

The exponent `1/6` is compatible with an effective large-block threshold
`N^(3/5)`: the support-four retained-order margin grows like `N^(1/30)` after
all fixed and polylogarithmic losses.  The stronger threshold requires four
one-variable return amplifications rather than three.  Their clean-star
exponent is `29/48`, which exceeds `3/5` by `1/240`.

## 1. A finite-prime divisor bound

Fix `alpha>0`.  For a prime `p`, put

\[
c_p(\alpha)
=
\max_{a\ge0}
\frac{a+1}{p^{\alpha a}}.
\]

### Theorem PX466 -- PROVED

For every positive integer

\[
m=\prod_p p^{a_p},
\]

one has

\[
\boxed{
\tau(m)
\le
C_\alpha m^\alpha,
\qquad
C_\alpha
=
\prod_{p<2^{1/\alpha}}c_p(\alpha).
}
\]

The product is finite.

### Proof

Factor the normalized divisor count:

\[
\frac{\tau(m)}{m^\alpha}
=
\prod_{p\mid m}
\frac{a_p+1}{p^{\alpha a_p}}.
\]

If `p>=2^(1/alpha)`, then `p^alpha>=2`.  Since

\[
a+1\le2^a
\]

for every integer `a>=0`, the corresponding local factor is at most one.
For every smaller prime, bound by its local maximum and multiply. \(\square\)

## 2. Exact twelfth-power certificate

Take

\[
\alpha=\frac1{12}.
\]

Only primes `p<4096` contribute.  Define

\[
a(p)
=
\min\left\{
a\ge0:
(a+2)^{12}
\le
p(a+1)^{12}
\right\}.
\]

### Theorem PX467 -- PROVED FINITE/ARITHMETIC

For every prime `p<4096`, the maximum local factor is attained at `a(p)`:

\[
\boxed{
c_p(1/12)
=
\frac{a(p)+1}{p^{a(p)/12}}.
}
\]

There are exactly `564` such primes, and their exact integer certificate
satisfies

\[
\boxed{
\prod_{p<4096}(a(p)+1)^{12}
<
10^{324}
\prod_{p<4096}p^{a(p)}.
}
\]

Consequently

\[
\boxed{C_{1/12}<10^{27}.}
\]

### Proof

For

\[
f_p(a)=\frac{a+1}{p^{a/12}},
\]

the consecutive ratio obeys

\[
\left(\frac{f_p(a+1)}{f_p(a)}\right)^{12}
=
\frac{(a+2)^{12}}{p(a+1)^{12}}.
\]

Thus the sequence increases until `a(p)` and is nonincreasing afterward.
The displayed product inequality is an exact comparison of integers, checked
by `verify_product_explicit_divisor_witness.py`; no floating-point estimate is
used in the certificate.  Taking twelfth roots gives the result. \(\square\)

For reference, the numerical logarithm of the sharper finite product is about
`26.447 log(10)`, so the integer constant `10^27` retains visible slack.

## 3. Effective ambient divisor cap

### Corollary PX468 -- PROVED

For every integer `N>=2`,

\[
\boxed{
\mathfrak d(N)
\le
10^{27}N^{1/6}.
}
\]

### Proof

Every integer in the defining maximum satisfies

\[
m\le(N-1)^2<N^2.
\]

Apply PX466--PX467:

\[
\tau(m)
<
10^{27}(N^2)^{1/12}
=
10^{27}N^{1/6}.
\]

\(\square\)

## 4. An effective large-block exponent

Choose

\[
\epsilon=\frac1{10},
\qquad
T(N)=\left\lceil N^{3/5}\right\rceil.
\]

### Theorem PX469 -- PROVED REDUCTION

Insert the divisor witness PX468 into the paired thinning probability PX445.
Ignoring only fixed and explicit polylogarithmic factors, the divisor-controlled
retained-order quantity has growth

\[
\boxed{
\frac{T(N)^2}{N\mathfrak d(N)}
\ge
10^{-27}N^{1/30}.
}
\]

Thus the paired spread and support-four inequalities eventually hold at the
effective threshold exponent `3/5`.

### Proof

Use `T(N)>=N^(3/5)` and PX468:

\[
\frac{T(N)^2}{N\mathfrak d(N)}
\ge
\frac{N^{6/5}}{10^{27}N^{7/6}}
=
10^{-27}N^{1/30}.
\]

The exponent is positive because

\[
\frac15>\frac16.
\]

The remaining losses in PX453 are explicit powers of `log N` after substituting
PX465.  A positive power `N^(1/30)` eventually dominates them. \(\square\)

This theorem proves effectivity of the exponent comparison, not a practical
cutoff size.

## 5. Four returns cross the effective threshold

The channel-free one-variable recurrence PX418 gives, from initial weight
`D_0>=1`,

\[
D_j
\ge
\left(\frac n{96}\right)^{1-2^{-j}}.
\]

The actual selected-line threshold is

\[
K=n^{1/3+o(1)}.
\]

### Theorem PX470 -- PROVED REDUCTION

After four one-variable high-source returns,

\[
\boxed{
D_4
\ge
\left(\frac n{96}\right)^{15/16}
=
n^{15/16-o(1)}.
}
\]

Every coordinate or generic rank-one outcome then yields a clean star of order

\[
\boxed{
\frac{D_4}{O(K)}
=
n^{29/48-o(1)}.
}
\]

Moreover,

\[
\boxed{
\frac{29}{48}-\frac35
=
\frac1{240}>0.
}
\]

Hence the returned star eventually exceeds the effective large-block threshold
`n^(3/5)`.  A two-variable return gives star exponent

\[
\boxed{\frac23>\frac35.}
\]

### Proof

The fourth recurrence exponent is

\[
1-2^{-4}=\frac{15}{16}.
\]

Subtract the line-occupancy exponent `1/3`:

\[
\frac{15}{16}-\frac13
=
\frac{45-16}{48}
=
\frac{29}{48}.
\]

The two displayed comparisons are exact rational arithmetic. \(\square\)

### Corollary PX470a -- PROVED REDUCTION

The asymptotic return theorem PX449 can be made compatible with the explicit
divisor witness by replacing the earlier square-root-plus-unspecified-excess
threshold with `N^(3/5)` and permitting four one-variable high-source returns.

The only remaining effective-cutoff inputs are now explicit constants and the
finite search itself.  In particular:

- `A_3=320` by PX460;
- `d_*(N)` is explicit by PX465;
- `mathfrak d(N)<=10^27N^(1/6)` by PX468.

## 6. Verification

Run

```bash
python scripts/verify_product_explicit_divisor_witness.py
```

The verifier enumerates the `564` primes below `4096`, locates every exact local
maximum using twelfth-power integer comparisons, checks the global integer
certificate below `10^27`, tests the divisor inequality on a large finite
range, and verifies the exponent comparisons `1/5>1/6`, `29/48>3/5`, and
`2/3>3/5`.
