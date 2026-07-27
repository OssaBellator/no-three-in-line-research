# The universal Euler-product divisor family cannot reach `10^2873`

PX962--PX965 show that the rational witness `alpha=3/41` certifies every active
paired asymptotic inequality from `10^2874`. This chapter optimizes the entire
one-parameter Euler-product family used by PX466 and proves that no choice of
`alpha` in that family reaches the next lower integral decimal order.

## 1. The cutoff margin functional

For `alpha>0`, define

\[
C_\alpha
=
\prod_p\max_{a\ge0}\frac{a+1}{p^{\alpha a}}.
\]

Only primes with `p^alpha<2` contribute. At decimal order `D`, the logarithm of
the divisor-controlled retained-order ratio, with the current paired constants
and `Delta=33`, is

\[
M_D(\alpha)
=
\log\frac1{12}
-\log(32768\cdot256)
-198
+\left(\frac15-2\alpha\right)D\log10
-\log C_\alpha.
\]

### Theorem PX966 -- PROVED

For every fixed `D`, the function `M_D(alpha)` is concave and piecewise affine on
`alpha>0`.

### Proof

For each prime,

\[
\log\max_{a\ge0}\frac{a+1}{p^{\alpha a}}
=
\max_{a\ge0}\bigl(\log(a+1)-\alpha a\log p\bigr)
\]

is a maximum of affine functions and hence is convex. Only finitely many terms
are nonzero on every compact positive-alpha interval. Therefore
`log C_alpha` is convex and piecewise affine, while the remaining part of
`M_D` is affine. Negating the convex term proves the claim. \(\square\)

For `alpha>=1/10`, the polynomial retained-order exponent `1/5-2alpha` is
nonpositive and all other displayed contributions are negative, so such
parameters cannot certify the cutoff. It is enough to optimize on
`0<alpha<1/10`.

## 2. Exact maximizing pivot at decimal order 2873

Set

\[
P=13033,
\qquad
\alpha_*=\frac{\log2}{\log P}.
\]

At `alpha_*`, the prime `P` has a tie between local exponents zero and one. Every
other local exponent is unique. For primes `p<P`, let `a_p` be that unique
maximizer and put

\[
A=\prod_{p<P}(a_p+1),
\qquad
B=\prod_{p<P}p^{a_p}.
\]

### Theorem PX967 -- PROVED FINITE/ARITHMETIC

The exact local census has `1551` primes below `P`, with

\[
1\le a_p\le19.
\]

Moreover the exact integer products satisfy

\[
\boxed{
B<10^{5746}<P B.
}
\]

Consequently the right derivative of `M_2873` at `alpha_*` is negative and the
left derivative is positive. Hence `alpha_*` is a global maximizer of
`M_2873`.

### Proof

Away from a breakpoint,

\[
M_D'(\alpha)
=-2D\log10+\sum_p a_p\log p.
\]

Immediately to the right of `alpha_*`, the pivot prime has exponent zero, so the
derivative sign is the sign of

\[
\log B-5746\log10,
\]

which is negative by `B<10^5746`. Immediately to the left, the pivot contributes
one additional `log P`, and `PB>10^5746` makes the derivative positive.

The verifier locates every `a_p` using directed 100-digit logarithmic intervals.
The smallest separation from a competing local exponent exceeds `0.000046`, so
no nonpivot comparison is ambiguous. The two derivative inequalities are then
checked as exact integer comparisons. Concavity from PX966 makes the local pivot
a global maximizer. \(\square\)

## 3. Negative global maximum

### Theorem PX968 -- PROVED FINITE/ARITHMETIC

The global maximum cutoff margin at decimal order `2873` satisfies

\[
\boxed{
\sup_{\alpha>0}M_{2873}(\alpha)<-0.0934.
}
\]

In particular no universal Euler-product divisor witness of the PX466 form can
certify all active paired inequalities from `10^2873`.

### Proof

By PX967 it suffices to evaluate at `alpha_*`. Since

\[
\log C_{\alpha_*}
=
\log A-\alpha_*\log B,
\]

the margin is a fixed combination of `log 2`, `log 10`, `log P`, `log A`, and
`log B`. The verifier brackets every logarithm using separate `ROUND_FLOOR` and
`ROUND_CEILING` Decimal contexts at precision 100 and propagates interval signs
through every operation. The resulting rigorous upper endpoint is less than
`-0.0934`. \(\square\)

## 4. Optimal decimal cutoff inside the family

### Corollary PX969 -- PROVED REDUCTION

The least integral decimal cutoff obtainable from the universal one-parameter
Euler-product divisor family, with the current paired repair inequalities and
constants, is

\[
\boxed{10^{2874}}.
\]

### Proof

PX964 supplies the positive `3/41` certificate at decimal order `2874`. PX968
rules out every parameter at decimal order `2873`. \(\square\)

Thus further work on the active all-side path should not search for another
universal exponent merely to reduce the decimal cutoff. Any improvement below
`10^2874` must alter at least one substantive ingredient:

- use interval-specific divisor information;
- sharpen a retained-order or blocker constant;
- build a finite-range extension or absorber chain;
- prove recursive closure from a produced base;
- or replace the universal divisor framework.

This optimality statement concerns only the current proof family. It is not a
lower bound on the true no-three-in-line problem and does not prove the
conjecture.

## 5. Verification

```bash
python scripts/verify_product_universal_divisor_cutoff_optimality.py
```

The verifier checks the pivot prime, all `1551` unique nonpivot local maxima,
the exact derivative product bracket, the directed-rounding margin interval, and
the final negative global upper bound.
