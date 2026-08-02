# Exact depth plateau compresses the common cutoff

PX478 uses the smooth degree envelope

\[
\overline\Delta(\log N)
\]

throughout the cutoff calculation and obtains the conservative value
\(10^{4000}\).  Before \(\log N=9000\), however, the exact nested-depth function
is constant on a long interval.  Using that staircase value removes more than
three hundred decimal exponents from the cutoff without changing the repair
path or any geometric argument.

## 1. Exact depth plateau

Recall

\[
d_*(N)=1+\left\lceil\log_2(\log_2N+2)\right\rceil,
\qquad
\Delta_*(N)=3+2d_*(N).
\]

### Theorem PX479 -- PROVED FINITE/ARITHMETIC

For every

\[
10^{3650}\le N\le e^{9000},
\]

one has

\[
\boxed{d_*(N)=15,\qquad \Delta_*(N)=33.}
\]

### Proof

It is enough to check the endpoints.  Using

\[
3.321<\log_2 10<3.322
\]

gives

\[
8192<3650\log_2 10+2<16384.
\]

At the upper endpoint,

\[
\frac{9000}{\log2}+2<16384.
\]

Thus throughout the interval

\[
13<\log_2(\log_2N+2)<14,
\]

so the ceiling is fourteen and \(d_*=15\). \(\square\)

## 2. Retained-order margin at the new starting point

Fix

\[
\eta=\frac1{12},
\qquad
T(N)=\lceil N^{3/5}\rceil.
\]

On the plateau, the divisor-controlled lower thinning candidate satisfies

\[
q_2(N)
\ge
\frac{\eta N^{3/5}}
{32768\cdot10^{27}e^{132}N^{7/6}}.
\]

The retained-order target is

\[
B(33)=256e^{66}.
\]

### Theorem PX480 -- PROVED FINITE/ARITHMETIC

At

\[
N_1=10^{3650},
\]

one has

\[
\boxed{
\frac{q_2(N_1)N_1^{3/5}}{B(33)}>e^{3/2}>1.
}
\]

The logarithmic thinning candidate has much larger slack:

\[
\boxed{
\frac{q_1(N_1)N_1^{3/5}}{B(33)}>e^{4000}.
}
\]

The terminal-partner, four-return, and two-variable-return inequalities also
hold at \(N_1\).

### Proof

The logarithm of the divisor-controlled ratio is

\[
-\log12+
\frac{3650}{30}\log10
-\log32768-\log256-27\log10-198.
\]

Direct outward-rounded decimal arithmetic gives a value greater than \(3/2\).
The logarithmic candidate exceeds \(4000\) in log scale.  The return and partner
comparisons are evaluated by the same explicit formulas as PX477; their log
margins exceed nineteen and eight thousand respectively.  All calculations are
checked by `verify_product_compressed_common_cutoff.py`. \(\square\)

## 3. Propagation beyond the plateau

### Theorem PX481 -- PROVED

Every common-cutoff inequality remains valid for all \(N\ge N_1\).

### Proof

On

\[
\log N\in[3650\log10,9000],
\]

PX479 fixes \(\Delta_*=33\).  The logarithmic retained-order ratio has derivative

\[
\frac35-
\frac{3/5}{\log4+(3/5)\log N}>0,
\]

and the divisor-controlled ratio has derivative exactly \(1/30\).  The
four-return and terminal-partner ratios have the positive derivative bounds of
PX477.  Hence all inequalities increase across the plateau.

For \(\log N\ge9000\), PX475 and PX477 apply with the smooth upper degree
envelope and propagate the already positive inequalities to every larger order.
\(\square\)

## 4. Compressed common cutoff

### Corollary PX482 -- PROVED REDUCTION

The common numerical cutoff in PX478 may be replaced by

\[
\boxed{N_1=10^{3650}.}
\]

For every \(N\ge10^{3650}\), all active paired asymptotic repair hypotheses hold
simultaneously:

1. the retained paired label block has sufficient order;
2. support-four and internal rank-three margins hold;
3. terminal transpositions have allowed partners;
4. four one-variable returns and every two-variable return cross \(N^{3/5}\);
5. the exact depth and degree envelopes apply;
6. the active packet path carries no growing packet-family parameter.

This is a cutoff compression only.  It does not solve the finite range below
\(10^{3650}\).

## 5. Verification

Run

```bash
python scripts/verify_product_compressed_common_cutoff.py
```

The verifier checks the exact depth plateau, the outward-rounded starting
margins, the plateau derivatives, and the handoff to the PX475/PX477 smooth
envelope regime.
