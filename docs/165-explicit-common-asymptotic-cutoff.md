# An explicit common asymptotic cutoff

PX460, PX465, and PX468 instantiate the three witnesses isolated by PX455:

\[
A_3=320,
\]

\[
d_*(N)=1+\left\lceil\log_2(\log_2\max\{N,2\}+2)\right\rceil,
\]

and

\[
\mathfrak d(N)\le10^{27}N^{1/6}.
\]

Together with the corrected PX445 constants, they give the conservative common
cutoff

\[
\boxed{N_0=10^{4000}.}
\]

The cutoff is not computationally useful.  Its purpose is to make the
asymptotic branch effective and to separate it honestly from the still-open
finite range.

## 1. Smooth degree envelope

Put `x=log N` and define

\[
\overline d(x)
=2+\log_2\left(\frac{x}{\log2}+2\right),
\]

\[
\overline\Delta(x)
=3+2\overline d(x)
=7+2\log_2\left(\frac{x}{\log2}+2\right).
\]

### Theorem PX474 -- PROVED

For every `N>=2`,

\[
\boxed{
\Delta_*(N)=3+2d_*(N)
\le\overline\Delta(\log N).
}
\]

Moreover,

\[
\boxed{
\overline\Delta'(x)
=\frac{2}{(\log2)(x+2\log2)}
<\frac3x.
}
\]

### Proof

Use `ceil(y)<=y+1` in PX465 and differentiate.  Since `2/log2<3` and
`x+2log2>x`, the derivative bound follows. \(\square\)

## 2. Conservative thinning lower bounds

Fix

\[
\eta=\frac1{12},
\qquad
T(N)=\left\lceil N^{3/5}\right\rceil.
\]

Write

\[
L(\Delta)=1{,}310{,}720e^{2\Delta},
\qquad
B(\Delta)=256e^{2\Delta}.
\]

Because

\[
N^{3/5}\le T(N)\le2N^{3/5},
\]

we have

\[
\log(2T(N))\le\log(4N^{3/5}).
\]

Define the genuine lower bounds

\[
q_1(N)
=\frac{\eta}
{16L(\overline\Delta)\log(4N^{3/5})},
\]

\[
q_2(N)
=\frac{\eta N^{3/5}}
{32768\cdot10^{27}e^{4\overline\Delta}N^{7/6}}.
\]

The actual PX445 thinning probability is at least

\[
\min\{q_1(N),q_2(N)\}.
\]

### Theorem PX475 -- PROVED

For `x=log N>=9000`, both logarithmic retained-order ratios

\[
\log\left(\frac{q_1(N)N^{3/5}}{B(\overline\Delta(x))}\right)
\]

and

\[
\log\left(\frac{q_2(N)N^{3/5}}{B(\overline\Delta(x))}\right)
\]

are strictly increasing.

### Proof

For `Delta>=0`,

\[
256e^{2\Delta}\ge\max\{32,16\Delta+4\}.
\]

The derivative of the first ratio is greater than

\[
\frac35-\frac{12}{x}-\frac1x>0.
\]

The logarithm of the second ratio is

\[
\frac{x}{30}-6\overline\Delta(x)+\text{constant},
\]

whose derivative is greater than

\[
\frac1{30}-\frac{18}{x}>0.
\]

\(\square\)

## 3. Retained-order check at the cutoff

### Theorem PX476 -- PROVED FINITE/ARITHMETIC

At `N_0=10^4000`,

\[
\boxed{
q_i(N_0)N_0^{3/5}
>B(\overline\Delta(\log N_0))
}
\]

for `i=1,2`.  Therefore, for every `N>=N_0`,

\[
q_\eta(N)T(N)
\ge
\max\{32,16\Delta_*(N)+4,256e^{2\Delta_*(N)}\}.
\]

### Proof

Use

\[
2.3<\log10<2.303,
\qquad
0.69<\log2<0.7.
\]

These bounds give

\[
\overline\Delta(\log N_0)<35.
\]

The divisor-controlled ratio is at least

\[
\frac{\eta N_0^{1/30}}
{32768\cdot256\cdot10^{27}e^{210}},
\]

which exceeds one: the numerator contributes `10^(400/3)` and the denominator
is below `10^127`.  The logarithmic candidate has much larger slack.  The
exact log-domain comparison is encoded in
`verify_product_explicit_common_cutoff.py`, and PX475 propagates the result.
\(\square\)

## 4. Terminal and return thresholds

For `N>=4`, the explicit PX63 seed bound implies

\[
D_{\rm seed}(N)
\le32780N(1+\log(2N)).
\]

Set

\[
K_*(N)
=2+\left(6\cdot32780N(1+\log(2N))\right)^{1/3}.
\]

### Theorem PX477 -- PROVED

For every `N>=N_0`:

1. `N-1-2Delta_*(N)>0`;
2. four one-variable returns cross the threshold:
   
   \[
   \boxed{
   \frac{(N/96)^{15/16}}{48K_*(N)}>N^{3/5};
   }
   \]
3. a two-variable return also crosses it:
   
   \[
   \boxed{
   \frac{N/64}{48K_*(N)}>N^{3/5}.
   }
   \]

### Proof

The first ratio divided by `N^(3/5)` has logarithmic derivative greater than

\[
\frac1{240}-\frac1{3\log N}>0
\]

for `log N>=9000`.  It is therefore enough to check `N_0`.

At `N_0`,

\[
D_{\rm seed}(N_0)<10^{4009},
\qquad
K_*(N_0)<2\cdot10^{1337}.
\]

Using `96<10^2` and `48<10^2`, the four-return star has order greater than

\[
10^{(3998)(15/16)-2-1338}>10^{2400}=N_0^{3/5}.
\]

The two-variable estimate has the larger exponent margin `2/3-3/5=1/15`.
The terminal partner ratio is increasing because `Delta_*` grows only
logarithmic-logarithmically. \(\square\)

## 5. Common numerical cutoff

### Corollary PX478 -- PROVED REDUCTION

For every

\[
\boxed{N\ge10^{4000},}
\]

the following numerical hypotheses hold simultaneously:

1. adaptive paired thinning retains the required order;
2. paired support-four creation is at most `eta s/8`;
3. internal support-five/six creation is at most `eta s/8`;
4. internal support-three/four creation is at most `11s/96`;
5. atomic terminal label transpositions have allowed partners;
6. four one-variable returns and every two-variable return cross `N^(3/5)`;
7. the explicit nested-depth and label-degree envelopes apply;
8. the active packet path needs no growing joint-release parameter by PX473.

Thus `10^4000` is a common numerical cutoff for PX445--PX450.

This does **not** solve the finite range.  Exact all-side closure still requires
an absorber or construction chain covering all orders below the cutoff, plus
the final dependency audit of every reduction edge used by PX449.

## 6. Verification

Run

```bash
python scripts/verify_product_explicit_common_cutoff.py
```

The verifier checks the starting inequalities in the log domain, their
monotonic derivative bounds, the seed-line return estimates, and the corrected
paired margins.
