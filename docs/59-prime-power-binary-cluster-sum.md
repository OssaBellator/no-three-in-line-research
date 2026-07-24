# The binary-cluster separation factor

CMR71 localizes the logarithmic first-separation loss to triples whose closest
p-adic column pair lies in one layer.  The local reciprocal parameter at the
pair's actual separation node supplies one additional independent factor.  An
exact count of p-adic clustering types then removes the factor `p` from the
logarithmic term.

Continue with the balanced recursive bank for

\[
N=p^k,
\qquad
p\equiv1\pmod4,
\qquad
h=(p-1)/2.
\]

Write

\[
\tau(0)=0,
\qquad
\tau(x)=x^{-1}\quad(x\ne0),
\]

so every local map has the form

\[
F_{b,c}(x)=b+c\tau(x)\pmod p.
\]

## 1. The closest-pair separation digit

Fix a nontransverse triple with

\[
r=\min_{i<j}v_p(x_i-x_j)
<
s=\max_{i<j}v_p(x_i-x_j).
\]

Its unique closest pair has valuation `s` and uses one common layer.  The two
columns share a prefix modulo `p^s` and have distinct depth-`s` digits
`xi_1,xi_2`.

### Theorem CMR73 — PROVED

For a fixed nontransverse binary-cluster triple,

\[
\Pr(\text{real collinearity})
\le
\frac1h\,p^{-(k-s-1)}.
\]

### Proof

Divide the determinant coefficients by their common minimum power `p^r`.  The
unit coefficients are exactly those attached to the two endpoints of the
closest pair, and modulo `p` they are opposites.  The third coefficient is
zero modulo `p`.

At row-digit depth `s`, the closest pair uses one common layer-prefix node but
enters it through the two distinct column digits `xi_1,xi_2`.  Conditional on
all lower digits and every other depth-`s` node, the next determinant congruence
has the form

\[
C+u\bigl(F_{b,c}(\xi_1)-F_{b,c}(\xi_2)\bigr)
\equiv0\pmod p,
\]

where `u` is a unit.  The shift `b` cancels, while

\[
F_{b,c}(\xi_1)-F_{b,c}(\xi_2)
=
c\bigl(\tau(\xi_1)-\tau(\xi_2)\bigr).
\]

The completed inverse `tau` is a permutation, so the final parenthesis is
nonzero.  Therefore at most one value of the nonsquare parameter `c` can satisfy
the congruence.  Since `c` is uniform on `h` values, the separation depth costs
a factor `1/h`.

At every depth above `s`, the three column prefixes are distinct.  CMR68 then
supplies `k-s-1` independent factors of `1/p`. ∎

This argument also applies to the original CMR35 restricted family, with its
uniform nonsquare parameter.  The balanced family is needed below for the exact
`1/p` factors above the separation node.

## 2. Exact p-adic clustering populations

There are two nontransverse column patterns.

### Equilateral clusters

If all three pair valuations equal `s`, the columns share one prefix modulo
`p^s` and occupy three distinct children at depth `s`.  Put

\[
L=p^{k-s-1}.
\]

The number of unordered column triples of this type is exactly

\[
E_s
=
p^s\binom p3L^3
=
\binom p3\frac{N^3}{p^{2s+3}}.
\]

Only the two monochromatic layer assignments are nontransverse.  CMR68 bounds
each by `p^{-(k-s-1)}`.  Hence their total expected contribution over all
levels is less than

\[
\begin{aligned}
2\sum_{s=0}^{k-1}
E_s p^{-(k-s-1)}
&=
\frac{2\binom p3}{p^2}N^2
\sum_{s=0}^{k-1}p^{-s}\\
&<
\frac{p-2}{3}N^2.
\end{aligned}
\]

### Binary clusters

The number of unordered column pairs with exact valuation `s` is

\[
P_s
=
p^s\binom p2L^2
=
\binom p2\frac{N^2}{p^{s+2}}
=
\frac{hN^2}{p^{s+1}}.
\]

Every triple with a unique closest pair of valuation `s` is obtained from one
such pair and a third column, so there are fewer than `P_sN` column triples of
this type.  There are four layer assignments in which the closest pair uses one
common layer.  CMR73 therefore gives expected mass at most

\[
4P_sN\frac1h p^{-(k-s-1)}
=
4N^2
\]

at every valuation level.

## 3. Sharpened first-separation sum

### Corollary CMR74 — PROVED

The balanced recursive bank satisfies

\[
\mathbb E T_k
<
4kN^2+
\frac{p+2}{3}N^2.
\]

Consequently it contains a saturated state with

\[
T_k
=
O(N^2\log_pN)
\]

whose logarithmic coefficient is absolute rather than proportional to `p`.

### Proof

CMR70--CMR71 bound all layer-transverse triples by less than `4N^2/3` in
expectation.  The equilateral nontransverse clusters contribute less than
`(p-2)N^2/3`.  The binary nontransverse clusters contribute at most `4N^2` at
each of the `k` possible closest-pair valuations.  Adding the three terms gives
the result. ∎

The remaining logarithm is now completely explicit.  It comes from binary
same-layer stars: one close pair at scale `s`, together with a third point
outside that pair's prefix block.  Equilateral clusters and every
layer-transverse pattern have only quadratic total mass.  Any improvement below
`N^2 log N` must therefore neutralize these external pair-stars across scales,
rather than improving generic digit anti-concentration.

The exact clustering formulas are checked in
[`scripts/verify_prime_power_binary_clusters.py`](../scripts/verify_prime_power_binary_clusters.py).
