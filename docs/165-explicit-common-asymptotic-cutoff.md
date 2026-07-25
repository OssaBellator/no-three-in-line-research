# An explicit common asymptotic cutoff

PX460, PX465, and PX468 instantiate the three numerical witnesses isolated by
PX455:

\[
A_3=320,
\]

\[
d_*(N)
=
1+
\left\lceil
\log_2(\log_2\max\{N,2\}+2)
\right\rceil,
\]

and

\[
\mathfrak d(N)
\le
10^{27}N^{1/6}.
\]

This chapter combines them with the corrected PX445 constants.  The resulting
cutoff is intentionally conservative:

\[
\boxed{N_0=10^{4000}.}
\]

It is not computationally useful, but it is an explicit certified expression
above which every numerical hypothesis in the paired asymptotic repair loop is
simultaneously satisfied.

## 1. Smooth upper envelopes

Put

\[
x=\log N
\]

and define

\[
\overline d(x)
=
2+
\log_2\left(\frac{x}{\log2}+2\right).
\]

Since `ceil(y)<=y+1`, PX465 gives

\[
d_*(N)
\le
\overline d(x).
\]

Use the smooth label-degree envelope

\[
\boxed{
\overline\Delta(x)
=
3+2\overline d(x)
=
7+2\log_2\left(\frac{x}{\log2}+2\right).
}
\]

### Theorem PX474 -- PROVED

For every `N>=2`,

\[
\Delta_*(N)
=
3+2d_*(N)
\le
\overline\Delta(\log N).
\]

Moreover

\[
\boxed{
\overline\Delta'(x)
=
\frac{2}{(\log2)(x+2\log2)}
<
\frac3x.
}
\]

### Proof

The first statement is the ceiling inequality.  Differentiate the displayed
smooth formula.  Since `2/log2<3` and `x+2log2>x`, the derivative bound follows.
\(\square\)

## 2. Effective threshold and thinning probability

Fix

\[
\eta=\frac1{12},
\qquad
T(N)=\left\lceil N^{3/5}\right\rceil.
\]

For the monotonic lower-bound calculation replace `T(N)` by `N^(3/5)` and
`Delta_*(N)` by `overline Delta(log N)`.  This can only make the retained-order
inequalities harder.

Put

\[
L(\Delta)=1{,}310{,}720e^{2\Delta},
\]

\[
B(\Delta)=256e^{2\Delta},
\]

and define the two lower thinning candidates

\[
q_1(N)
=
\frac{\eta}
{16L(\overline\Delta)\log(2N^{3/5})},
\]

\[
q_2(N)
=
\frac{\eta N^{3/5}}
{32768\cdot10^{27}e^{4\overline\Delta}N^{7/6}}.
\]

The actual PX445 probability is at least

\[
\min\{q_1(N),q_2(N)\}
\]

when evaluated with the divisor upper bound.

### Theorem PX475 -- PROVED

For

\[
x=\log N\ge9000,
\]

both functions

\[
\log\frac{q_1(N)N^{3/5}}{B(\overline\Delta(x))}
\]

and

\[
\log\frac{q_2(N)N^{3/5}}{B(\overline\Delta(x))}
\]

are strictly increasing.

### Proof

Because

\[
256e^{2\Delta}
\ge
\max\{32,16\Delta+4\}
\]

for `Delta>=0`, this `B` dominates every PX445 retained-order condition.

For the first ratio, differentiation gives

\[
\frac35
-4\overline\Delta'(x)
-
\frac{3/5}{\log2+3x/5}
>
\frac35-rac{12}{x}-\frac1x
>0.
\]

For the second ratio, the logarithm is

\[
\frac{x}{30}-6\overline\Delta(x)+\text{constant},
\]

whose derivative is greater than

\[
\frac1{30}-rac{18}{x}>0.
\]

\(\square\)

Thus it is enough to check the retained-order inequalities at one starting
value.

## 3. Numerical retained-order certificate at `10^4000`

### Theorem PX476 -- PROVED FINITE/ARITHMETIC

At

\[
N_0=10^{4000},
\]

one has

\[
\boxed{
q_i(N_0)N_0^{3/5}
>
B(\overline\Delta(\log N_0))
}
\]

for `i=1,2`.  Hence for every `N>=N_0`,

\[
q_\eta(N)T(N)
\ge
\max\{32,16\Delta_*(N)+4,256e^{2\Delta_*(N)}\}.
\]

### Proof

Use the elementary bounds

\[
2.3<\log10<2.303,
\qquad
0.69<\log2<0.7.
\]

At `N_0`, these imply

\[
\overline\Delta(\log N_0)<35.
\]

The divisor-controlled ratio has the lower bound

\[
\frac{\eta N_0^{1/30}}
{32768\cdot256\cdot10^{27}e^{210}}.
\]

Its numerator contributes `10^(400/3)`, while the denominator is less than
`10^127`; hence the ratio is greater than one.  The logarithmic candidate has
far larger slack: its numerator contains `N_0^(3/5)=10^2400`, while all fixed,
exponential-degree, and logarithmic denominator factors together are below
`10^100`.

The exact log-domain comparison is checked by
`verify_product_explicit_common_cutoff.py`.  PX475 propagates the inequalities
to every larger `N`. \(\square\)

The estimates are intentionally rounded outward.

## 4. Terminal-transposition and return thresholds

Let `D_seed(N)` be the explicit PX63 defect upper bound.  For `N>=4`,

\[
D_{\rm seed}(N)
\le
32780N(1+\log(2N)).
\]

Therefore PX64 gives the explicit line cap

\[
K_*(N)
=
2+
\left(6\cdot32780N(1+\log(2N))\right)^{1/3}.
\]

### Theorem PX477 -- PROVED

For every `N>=N_0`:

1. `N-1-2Delta_*(N)>0`, so every atomic terminal label source has an allowed
   transposition partner;
2. four one-variable high-source returns produce a clean star larger than
   `T(N)`:
   
   \[
   \boxed{
   \frac{(N/96)^{15/16}}
   {48K_*(N)}
   >
   N^{3/5};
   }
   \]
3. a two-variable return also exceeds the threshold:
   
   \[
   \boxed{
   \frac{N/64}{48K_*(N)}
   >
   N^{3/5}.
   }
   \]

### Proof

The first inequality is immediate at `N_0` and remains increasing because
`Delta_*` is logarithmic-logarithmic.

For the one-variable ratio, write `x=log N`.  An upper bound for the derivative
of `log K_*` is

\[
\frac13\left(1+\frac1{1+\log2+x}\right).
\]

Hence the derivative of the logarithm of the first displayed ratio divided by
`N^(3/5)` is greater than

\[
\frac{15}{16}-\frac35-rac13-rac1{3x}
=
\frac1{240}-\frac1{3x}>0
\]

for `x>=9000`.  It is enough to check `N_0`.

At `N_0`, the seed bound gives `D_seed<10^4009`, so

\[
K_*(N_0)<2\cdot10^{1337}.
\]

Using `96<10^2` and `48<10^2`, the returned star has order greater than

\[
10^{(3998)(15/16)-2-1338}
>
10^{2400}
=
N_0^{3/5}.
\]

The two-variable estimate has much larger exponent margin `2/3-3/5=1/15` and
is checked similarly. \(\square\)

## 5. The common numerical cutoff

### Corollary PX478 -- PROVED REDUCTION

For every

\[
\boxed{N\ge10^{4000},}
\]

the following numerical conditions used by the paired asymptotic repair loop
hold simultaneously:

1. adaptive paired thinning retains the required order;
2. paired support-four creation is at most `eta s/8`;
3. internal support-five/six creation is at most `eta s/8`;
4. internal support-three/four creation is at most `11s/96`;
5. atomic terminal label transpositions have allowed partners;
6. four one-variable returns and every two-variable return cross the effective
   `N^(3/5)` threshold;
7. the explicit nested-depth and label-degree envelopes apply;
8. the active packet route needs no growing joint-release parameter by PX473.

Thus `10^4000` is a common numerical cutoff for PX445--PX450.

This does **not** solve the finite range.  Exact all-side closure still requires
an absorber or construction chain covering all orders below the cutoff, and the
final dependency audit must certify every reduction edge used by PX449.

## 6. Verification

Run

```bash
python scripts/verify_product_explicit_common_cutoff.py
```

The verifier evaluates all inequalities in the log domain at `N_0`, checks the
monotonic derivative lower bounds, verifies the seed-line return estimates, and
confirms the corrected paired margins.
