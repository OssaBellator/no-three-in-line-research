# Pair moments give explicit envelopes for line-profile classes

CMR1334--CMR1341 compress fixed-target collateral into residual rank and dyadic
line-count profiles.  The line populations are not arbitrary.  Every pair in a
partial matching determines one unique nonaxis line, and every pair of response-
graph cells counted below is matching-compatible.  This gives exact second
moments and rigorous tail bounds for the profile histogram.

Retain the notation

\[
o_L=|O\cap L|,
\qquad
g_L=|E(G)\cap L|,
\qquad
m_L=|M_G\cap L|.
\]

Let

\[
P_2(G)=\frac{n(n-2)(n^2-4n+5)}2
\]

be the exact compatible-pair stock from CMR1225.

## Exact pair moments

### Theorem CMR1342 -- PROVED

Over nonaxis lines,

\[
\boxed{
\sum_L\binom{o_L}{2}=\binom n2,
}
\]

\[
\boxed{
\sum_L\binom{g_L}{2}=P_2(G),
}
\]

and

\[
\boxed{
\sum_L\binom{m_L}{2}=\binom{|M_G|}{2}.
}
\]

### Proof

`O` and `M_G` are partial matchings.  Every unordered pair of their distinct
cells lies on one nonaxis line by CMR1335, and every line pair is counted once.
For `G`, the compatible pairs are exactly the pairs with distinct rows and
columns.  CMR1335 places each such pair on one nonaxis line, while every pair on
a nonaxis line is compatible.  Use CMR1225 for the total. ∎

## Population tail bounds

For an integer `t>=2`, define

\[
N_o(t)=|\{L:o_L\ge t\}|,
\quad
N_g(t)=|\{L:g_L\ge t\}|,
\quad
N_m(t)=|\{L:m_L\ge t\}|.
\]

### Theorem CMR1343 -- PROVED

\[
\boxed{
N_o(t)\le\frac{\binom n2}{\binom t2},
\qquad
N_g(t)\le\frac{P_2(G)}{\binom t2},
\qquad
N_m(t)\le\frac{\binom{|M_G|}{2}}{\binom t2}.
}
\]

### Proof

Every line in a tail contributes at least `binom(t,2)` to the corresponding
nonnegative exact moment of CMR1342. ∎

## Dyadic profile multiplicity

For a positive dyadic band `b`, put

\[
L(b)=2^{b-1},
\qquad
U_n(b)=\min(n,2^b-1),
\]

and set `L(0)=U_n(0)=0`.

Let `H_bar(i,j,k)` be the number of lines with

\[
b_n(o_L)=i,
\qquad
b_n(g_L)=j,
\qquad
b_n(m_L)=k.
\]

### Theorem CMR1344 -- PROVED

Whenever the denominator is nonzero,

\[
\boxed{
\overline H(i,j,k)
\le
\min\left\{
\frac{\binom n2}{\binom{L(i)}2},
\frac{P_2(G)}{\binom{L(j)}2},
\frac{\binom{|M_G|}{2}}{\binom{L(k)}2}
\right\}.
}
\]

Terms with `L=0` or `1` are simply omitted from the minimum.

### Proof

A line in the band lies in every applicable population tail.  Apply CMR1343. ∎

For rank one the `o` bound is always applicable, since `binom(o_L,2)>0` requires
`o_L>=2`.  For ranks two and three the `g` bound is applicable whenever the
contribution is positive.

## Rank-one band envelope

Let `H=H_bar(i,j,k)` and abbreviate

\[
O_i=U_n(i),
\quad G_j=U_n(j),
\quad M_k=L(k).
\]

### Theorem CMR1345 -- PROVED

The normalized rank-one contribution of one band is at most

\[
\boxed{
\frac{G_j-M_k}{n}
\min\left\{
H\binom{O_i}{2},
\binom n2
\right\}.
}
\]

### Proof

On every line in the band, `g_L-m_L<=G_j-M_k`.  Sum
`binom(o_L,2)` over the band.  It is bounded both by
`H binom(O_i,2)` and by the complete opposite-layer moment `binom(n,2)`. ∎

## Rank-two band envelope

### Theorem CMR1346 -- PROVED

The normalized rank-two contribution of one band is at most

\[
\boxed{
\frac{O_i}{(n)_2}
\min\left\{
H\left[\binom{G_j}{2}-\binom{M_k}{2}\right],
P_2(G)
\right\}.
}
\]

### Proof

Use `o_L<=O_i`.  The bracket on each line is at most the displayed band maximum.
Its sum is also at most `sum_L binom(g_L,2)=P_2(G)` after discarding the
nonnegative old subtraction. ∎

## Rank-three band envelope

### Theorem CMR1347 -- PROVED

The normalized rank-three contribution of one band is at most

\[
\boxed{
\frac1{(n)_3}
\min\left\{
H\left[\binom{G_j}{3}-\binom{M_k}{3}\right],
\frac{(G_j-2)_+}{3}P_2(G)
\right\}.
}
\]

### Proof

The first term is the bandwise maximum times the line count.  For the second,

\[
\binom{g_L}{3}
=
\frac{g_L-2}{3}\binom{g_L}{2}
\le
\frac{(G_j-2)_+}{3}\binom{g_L}{2}.
\]

Sum and use CMR1342; the old subtraction only reduces the contribution. ∎

## Explicit profile upper quotient

Let `Xi_r(i,j,k)` denote the right side of CMR1345, CMR1346 or CMR1347, using
the multiplicity bound of CMR1344 when the exact band count is unavailable.

### Theorem CMR1348 -- PROVED

For every exact host and fixed-extension bank,

\[
\boxed{
\mathcal C(S;O,F)
\le
\sum_{r=1}^3\sum_{i,j,k}\Xi_r(i,j,k).
}
\]

The `Xi_r` also give componentwise upper bounds for the rank/profile offspring
classes of CMR1338.  All entries are explicit rational functions of `n`,
`|M_G|`, the dyadic endpoints and the exact pair stock `P_2(G)`.

### Proof

Apply the rank-specific envelope to every band and sum.  Each exact line belongs
to one band and each collateral prescription to one rank. ∎

## Pair-moment endpoint

### Corollary CMR1349 -- PROVED

The same-owner dyadic profile quotient now has explicit rigorous row envelopes
from three exact pair moments.  Any failure of a subcritical certificate must
come from a profile band whose line multiplicity is substantially below these
coarse pair-moment bounds only if additional primitive-height, prefix, quotient
or carry structure is used.

Thus the remaining diagonal-block problem is narrowed to improving the explicit
`Xi_r` entries with arithmetic line-distribution information; product and fixed-
interface off-diagonal terms are already triangular by CMR1318--CMR1325.

No all-`n` theorem is claimed.  Pair moments, tail bounds, dyadic multiplicities
and rankwise profile envelopes are checked in
[`scripts/verify_prime_power_line_profile_pair_moments.py`](../scripts/verify_prime_power_line_profile_pair_moments.py).
