# A no-three fibrewise recursive bank

The conic terminal family CMR35 can be used in every quotient fibre, not only
at the terminal block. Let `N=pa`, with `p` odd and `a` a power of `p`, and fix
a saturated quotient state

\[
P_0,P_1:[a]\to[a],
\qquad P_0(\bar x)\ne P_1(\bar x).
\]

For every quotient column and layer, independently choose one `F_{b,c}` from
CMR35 and lift

\[
x=\bar x+a\xi
\]

to

\[
y=P_\ell(\bar x)+aF_{b,c}(\xi).
\]

Put `h=(p-1)/2`.

## 1. Saturation and state count

### Theorem CMR43 — PROVED

Every choice gives two pointwise-disjoint permutation layers. Over one fixed
quotient state the bank has

\[
(h^2)^{2a}=h^{4a}
\]

states.

### Proof

Each `F_{b,c}` bijects the `p` column digits to the prescribed row fibre. The
quotient permutations make those fibres partition all rows. The two quotient
row labels at one column are distinct, so their full row fibres are disjoint.
∎

## 2. Cylinder law

### Theorem CMR44 — PROVED

A compatible prescription has probability at most

\[
\prod_{\bar x,\ell}\psi(r_{\bar x,\ell}),
\]

where

\[
\psi(0)=1,
\qquad
\psi(1)=1/h,
\qquad
\psi(r)=1/h^2\quad(r\ge2).
\]

### Proof

Multiply the independent CMR36 bounds over all layer-fibres. ∎

## 3. One-fibre triples

### Theorem CMR45 — PROVED

No state contains a real triple whose three columns lie in one quotient column
fibre.

### Proof

A same-layer triple scales to one CMR35 graph. For a mixed triple write the
points as

\[
(\bar x+a\xi_i,\bar y_{\ell_i}+a\eta_i).
\]

Two points lie in one layer. Put

\[
\delta=\bar y_1-\bar y_0.
\]

The determinant is

\[
\Delta=a(aD+\delta E),
\]

where, up to sign, `E` is the difference of the two distinct same-layer column
digits. Thus `p` does not divide `E`. Since the quotient row labels are
distinct, `delta` is nonzero and has smaller `p`-adic valuation than `a`.
Therefore `a` does not divide `delta E`, while it divides `aD`; cancellation is
impossible. ∎

## 4. First-separating-fibre anti-concentration

### Theorem CMR46 — PROVED

Fix three actual column/layer positions not all in one quotient column fibre.
Conditional on all other fibre choices, their collinearity probability is at
most

\[
1/h=2/(p-1).
\]

If two positions use one actual column, the probability is zero.

### Proof

A vertical pair and a point in another column are not collinear. Otherwise one
fibre key occurs exactly once. After all other choices are exposed, the
determinant is a nonconstant affine function of the remaining exact row,
because its coefficient is the nonzero difference of the other two columns.
At most one row works, and CMR36 assigns any prescribed row probability at most
`1/h`. ∎

The checker is
[`scripts/verify_prime_power_lift_anti_concentration.py`](../scripts/verify_prime_power_lift_anti_concentration.py).
