# Exact line-count profiles for degree-two bank collateral

CMR1222--CMR1237 express corrected fixed-target collateral through line-local
compatibility counts.  In the permutation-layer geometry these counts simplify:
axis lines contribute no triples, while every subset of a nonaxis line is
matching-compatible.  Hence the score is determined by the integer profile
`(o_L,g_L,m_L)`.

Retain

\[
S=O\cup M,
\qquad
G=K_{n,n}\setminus(O\cup F),
\qquad
M_G=M\cap E(G),
\]

and put

\[
o_L=|O\cap L|,
\qquad
g_L=|E(G)\cap L|,
\qquad
m_L=|M_G\cap L|.
\]

## Axis exclusion

### Theorem CMR1334 -- PROVED

Every horizontal or vertical line contains at most two cells of `O union R` for
any response matching `R`.  Therefore no response-state collinear triple lies on
an axis line.

### Proof

Each perfect matching uses exactly one cell in each row and column.  The union of
two matchings uses at most two. ∎

## Nonaxis compatibility

### Theorem CMR1335 -- PROVED

Distinct cells on a nonhorizontal, nonvertical line have distinct rows and
columns.  Every finite subset of such a line is therefore matching-compatible.
In particular,

\[
\boxed{
c_2(G_L)=\binom{g_L}{2},
\qquad
c_3(G_L)=\binom{g_L}{3}.
}
\]

### Proof

Two cells sharing a row determine a horizontal line, and two sharing a column
determine a vertical line. ∎

## Corrected exact profile formula

### Theorem CMR1336 -- PROVED

The genuinely new collateral counts are

\[
\boxed{
V_1=\sum_L\binom{o_L}{2}(g_L-m_L),
}
\]

\[
\boxed{
V_2=\sum_Lo_L
\left[\binom{g_L}{2}-\binom{m_L}{2}\right],
}
\]

and

\[
\boxed{
V_3=\sum_L
\left[\binom{g_L}{3}-\binom{m_L}{3}\right],
}
\]

where the sums may be restricted to nonaxis lines.

### Proof

Apply the corrected old-state subtraction of CMR1222--CMR1224, then use
CMR1334--CMR1335. ∎

## Exact profile histogram

For `0<=m<=g<=n` and `0<=o<=n`, let

\[
H(o,g,m)=|\{L:(o_L,g_L,m_L)=(o,g,m)\}|.
\]

Define

\[
\psi_1(o,g,m)=\frac{\binom o2(g-m)}n,
\]

\[
\psi_2(o,g,m)=
\frac{o[\binom g2-\binom m2]}{(n)_2},
\]

and

\[
\psi_3(o,g,m)=
\frac{\binom g3-\binom m3}{(n)_3}.
\]

### Theorem CMR1337 -- PROVED

\[
\boxed{
\mathcal C(S;O,F)
=
\sum_{o,g,m}H(o,g,m)
\sum_{r=1}^3\psi_r(o,g,m).
}
\]

The rank-`r` contribution is obtained by retaining `psi_r`.

### Proof

Group the exact line sums of CMR1336 by their common count profile. ∎

Thus exact count profiles are lossless coarse classes in the sense of CMR1328.

## Dyadic profile classes

For `0<=x<=n`, put

\[
b_n(x)=0\quad(x=0),
\qquad
b_n(x)=1+\lfloor\log_2x\rfloor\quad(x>0),
\]

and let

\[
B_n=1+\lceil\log_2n\rceil.
\]

### Theorem CMR1338 -- PROVED

The class

\[
(r,b_n(o_L),b_n(g_L),b_n(m_L))
\]

has at most

\[
\boxed{3B_n^3}
\]

values.  Every new collateral triple belongs to one such class and to one
absolute entering-edge owner.

### Proof

There are three residual ranks and at most `B_n` bands for each count.  Exact
profiles partition the lines and last-entering ownership is unique. ∎

## Honest upper coefficients

For a band triple `(i,j,k)`, define

\[
\widehat\psi_r(i,j,k)
=
\max\{\psi_r(o,g,m):
 b_n(o)=i,\ b_n(g)=j,\ b_n(m)=k,\ 0\le m\le g\le n\}.
\]

### Theorem CMR1339 -- PROVED

If `H_bar(i,j,k)` is the number of lines in a dyadic profile band, then

\[
\boxed{
\mathcal C(S;O,F)
\le
\sum_{i,j,k}\overline H(i,j,k)
\sum_{r=1}^3\widehat\psi_r(i,j,k).
}
\]

The same componentwise domination applies to expected coarse offspring rows, so
these coefficients define an honest CMR1329 upper quotient.

### Proof

Every exact profile coefficient is at most the maximum of its band.  Sum over
lines and then over bands. ∎

## Band concentration

### Theorem CMR1340 -- PROVED

If total normalized collateral is at least `C_0`, then one residual-rank/profile
band contributes at least

\[
\boxed{
\frac{C_0}{3B_n^3}.
}
\]

The same conclusion holds for any grouped expected offspring row.

### Proof

The class contributions are nonnegative and there are at most `3B_n^3` of them.
∎

## Endpoint

### Corollary CMR1341 -- PROVED

Degree-two bank collateral in inherited coordinates has a lossless exact
`(o,g,m)` histogram and an honest `O(log^3 n)` dyadic rank/profile upper quotient.
Large same-owner reproduction localizes to one explicit profile band, while
CMR1318--CMR1325 keep strict product descendants off the diagonal.

The remaining quantitative task is to bound each band by primitive-height,
prefix, quotient/carry and thin-regime estimates and then verify a subcritical
upper-quotient certificate.  No all-`n` theorem is claimed.

The identities and band bounds are checked in
[`scripts/verify_prime_power_degree_two_bank_line_profiles.py`](../scripts/verify_prime_power_degree_two_bank_line_profiles.py).
