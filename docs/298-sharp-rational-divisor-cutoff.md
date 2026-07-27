# The sharp `8/109` product certificate lowers the cutoff to `10^2875`

PX488--PX492 use the rational divisor exponent

\[
\alpha=\frac8{109}
\]

and round its finite Euler-product constant up to `10^59`. The exact integer
product has enough slack to retain the same exponent while replacing that coarse
rounding by the rational decimal exponent `6425/109`. This is a numerical
compression of the active asymptotic path; it does not address the finite range.

## 1. Sharp exact product interval

For every contributing prime `p<2^(109/8)`, let

\[
a_*(p)=\min\{a\ge0:(a+2)^{109}\le p^8(a+1)^{109}\}.
\]

### Theorem PX952 -- PROVED FINITE/ARITHMETIC

With the same `1508` primes and local maximizers as PX488, the exact products
satisfy

\[
10^{6424}\prod_p p^{8a_*(p)}
\le
\prod_p(a_*(p)+1)^{109}
<
10^{6425}\prod_p p^{8a_*(p)}.
\]

Consequently the Euler-product constant lies in the certified interval

\[
10^{6424/109}
\le C_{8/109}<
\boxed{10^{6425/109}}.
\]

The upper exponent is approximately `58.944954`, compared with the previous
integer exponent `59`.

### Proof

The verifier constructs both integer products exactly. The numerator and
prime-power denominator have `50,941` and `44,516` decimal digits. Direct
arbitrary-precision comparison proves the two displayed inequalities. The local
maximum checks are unchanged from PX488. \(\square\)

## 2. Sharpened divisor cap

### Corollary PX953 -- PROVED

For every integer `N>=2`,

\[
\boxed{
\mathfrak d(N)
<10^{6425/109}N^{16/109}.
}
\]

### Proof

Every integer in the ambient divisor maximum is below `N^2`. Apply the universal
Euler-product argument PX466 with `alpha=8/109` and PX952. \(\square\)

## 3. New common cutoff

Keep

\[
T(N)=\lceil N^{3/5}\rceil,
\qquad
\eta=\frac1{12}.
\]

### Theorem PX954 -- PROVED FINITE/ARITHMETIC

Every active paired asymptotic repair inequality holds for every

\[
\boxed{N\ge10^{2875}}.
\]

Thus the common cutoff in PX492 may be replaced by

\[
\boxed{N_4=10^{2875}}.
\]

### Proof

At `N_4`, the exact nested-depth plateau still gives

\[
d_*(N_4)=15,
\qquad
\Delta_*(N_4)=33.
\]

Using PX953, the logarithm of the divisor-controlled retained-order ratio is
strictly greater than `0.09`. The other starting margins are:

- logarithmic retained-order margin greater than `3800`;
- four-return margin greater than `12`;
- two-variable-return margin greater than `420`;
- terminal-partner margin greater than `6600`.

Across the exact-depth plateau, the divisor-controlled ratio increases with
derivative

\[
\frac{29}{545}>0.
\]

For `log N>=9000`, the smooth-envelope derivative remains positive because

\[
\frac{29}{545}-6\overline\Delta'(\log N)>0,
\]

and the handoff margin is greater than `118`. Hence every inequality remains
valid for all larger orders. \(\square\)

## 4. Revised frontier

### Corollary PX955 -- PROVED REDUCTION

The active dependency root may use `N_4=10^2875` and the divisor witness

\[
\mathfrak d(N)<10^{6425/109}N^{16/109}.
\]

The remaining all-side frontier is still the finite interval below `10^2875`.
Further universal exponent optimization can save only a small number of decimal
orders; structural finite-range bridges, exact extension chains, or
interval-specific divisor bounds remain the material targets.

This cutoff result is independent of the finite side-seven selector census.
Neither result proves the classical no-three-in-line conjecture.

## 5. Verification

Run

```bash
python scripts/verify_product_sharp_rational_divisor_cutoff.py
```

The verifier checks all `1508` local maxima, both exact 109th-power product
comparisons, the depth plateau, every starting cutoff margin, and the smooth
handoff derivative.
