# A no-three fibrewise recursive bank

The full `S_p` lift bank from CMR26 is flexible but creates many triples wholly
inside one quotient column fibre. The reciprocal spread family of CMR35 can be
used at every fibre instead of only at the terminal block. This removes all
fibre-internal triples while retaining an explicit product measure.

Let `N=pa`, where `p` is an odd prime and `a` is a power of `p`. Fix a saturated
quotient state

\[
P_0,P_1:[a]\to[a],
\qquad
P_0(\bar x)\ne P_1(\bar x).
\]

For every quotient column `bar x` and layer `ell`, choose independently one map
`F_{b,c}` from CMR35. Lift the column

\[
x=\bar x+a\xi
\]

to the row

\[
y=P_\ell(\bar x)+aF_{b,c}(\xi).
\]

For `p=2`, use either fixed permutation of the two fibre digits; all statements
below that concern saturation and internal triples remain valid, while the
spread formula is stated only for odd `p`.

## 1. Saturation and state count

### Theorem CMR43 — PROVED

Every fibrewise choice gives two pointwise-disjoint permutation layers at
modulus `N`. For odd `p`, with `h=(p-1)/2`, the restricted lift bank has

\[
(h^2)^{2a}=h^{4a}
\]

states over each fixed quotient state.

### Proof

Each `F_{b,c}` is a permutation of the `p` fibre digits, so one layer bijects
each column fibre onto its prescribed row fibre. Since the quotient layer is a
permutation, those row fibres partition all rows, and the lifted layer is a
permutation.

At one quotient column, the two quotient row labels are distinct. Their full
row fibres are therefore disjoint, so the two lifted cells in every actual
column are distinct. There are `h^2` independent choices for each layer and
each of the `a` quotient columns. ∎

## 2. Exact cylinder law

### Theorem CMR44 — PROVED

Under independent uniform fibre choices, a compatible prescription has
probability at most

\[
\prod_{\bar x,\ell}\psi(r_{\bar x,\ell}),
\]

where `r_{bar x,ell}` is the number of prescribed cells in that layer-fibre and

\[
\psi(0)=1,
\qquad
\psi(1)=1/h,
\qquad
\psi(r)=1/h^2\quad(r\ge2).
\]

### Proof

This is the product of the CMR36 cylinder bounds, because all layer-fibre
parameters are independent. ∎

## 3. Every one-fibre triple is excluded

### Theorem CMR45 — PROVED

No restricted lift state contains a real collinear triple whose three columns
belong to one quotient column fibre.

### Proof

Fix a quotient column `bar x`. Write the selected points as

\[
(\bar x+a\xi_i,\ \bar y_{\ell_i}+a\eta_i),
\]

where `bar y_ell=P_ell(bar x)` and `eta_i` is supplied by the chosen
`F_{b,c}` in layer `ell_i`.

A same-layer triple scales to one graph from CMR35 and is therefore not
collinear.

For a mixed triple, two points lie in one layer and the third in the other.
Translate the common column residue and one row-fibre residue. Put

\[
\delta=\bar y_1-\bar y_0.
\]

The exact determinant has the form

\[
\Delta=a(aD+\delta E),
\]

where `D` is an integer digit determinant and, up to sign, `E` is the difference
of the two distinct same-layer column digits. Thus `p` does not divide `E`.
Since the quotient row labels are distinct, `delta` is nonzero with

\[
v_p(\delta)<v_p(a).
\]

Consequently `a` does not divide `delta E`, while `aD` is divisible by `a`.
The parenthesis cannot vanish. ∎

This theorem removes the terminal-block first-moment obstruction at every
scale, rather than only at the final fibre.

## 4. First-separating-fibre anti-concentration

### Theorem CMR46 — PROVED

Fix a quotient state and three actual column/layer positions that do not all lie
in one quotient column fibre. In a uniform restricted lift, conditional on all
other fibre choices, the probability that the three selected points are real
collinear is at most

\[
\frac1h=\frac{2}{p-1}.
\]

If two of the positions use the same actual column, the probability is zero.

### Proof

If two positions use one actual column, they form the vertical pair from the
two layers. A third point in another column cannot lie on that vertical line.

Otherwise the three actual columns are distinct. Because the quotient column
fibres are not all equal, one fibre contains exactly one of the three points.
Its layer-fibre parameter is independent of the choices controlling the other
two points.

Condition on every other choice. The determinant is a nonconstant linear
function of the remaining point's exact row, since its coefficient is the
nonzero difference of the other two columns. Hence at most one row in its
`p`-point row fibre can make the determinant zero. CMR36 bounds the probability
of any prescribed row at the fixed fibre digit by `1/h`. ∎

CMR46 is only a one-level anti-concentration statement; summing it over all
first-separation signatures remains open. Its significance is that every
surviving certificate is now cross-fibre and pays an explicit `O(1/p)` factor.

The finite checker is
[`scripts/verify_prime_power_restricted_bank.py`](../scripts/verify_prime_power_restricted_bank.py).