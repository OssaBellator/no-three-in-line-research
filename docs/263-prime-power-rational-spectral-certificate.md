# Subcritical collateral policies have exact rational certificates

CMR1262--CMR1269 reduce the target-versus-collateral problem at one finite owner to
an offspring matrix `A` with spectral radius below one.  For proof and computation,
a numerical eigenvalue estimate is not enough.  This chapter gives exact finite
certificates using positive rational weights, integer-scaled inequalities,
perturbation slack and constructive block gluing.

Let `A` be a finite nonnegative rational matrix indexed by credit classes
`Sigma={1,...,s}`.

## 1. Rational Lyapunov certificate

### Theorem CMR1270 -- PROVED

Suppose there are rational vectors

\[
v\in\mathbb Q_{>0}^s,
\qquad
\delta\in\mathbb Q_{>0}^s
\]

such that

\[
\boxed{
Av\le v-\delta
}
\]

componentwise.  Then

\[
\boxed{\rho(A)<1.}
\]

Every target response policy represented by `A` strictly decreases the expected
weighted live-credit potential by at least `delta_sigma` when class `sigma` is
targeted.

### Proof

Put

\[
\alpha
=
\max_\sigma\frac{v_\sigma-\delta_\sigma}{v_\sigma}<1.
\]

Then `Av<=alpha v`.  Diagonal similarity by `diag(v)` produces a nonnegative
matrix with every row sum at most `alpha`, hence spectral radius at most `alpha`.
The credit-descent statement is CMR1263 with the displayed quantitative slack. ∎

Thus a finite list of rational inequalities is a complete subcriticality
certificate.

## 2. Integer-scaled verification

### Theorem CMR1271 -- PROVED

Every rational certificate of CMR1270 can be converted to integer data.  There are
positive integers

\[
D,
\qquad
u\in\mathbb Z_{>0}^s,
\qquad
\eta\in\mathbb Z_{>0}^s
\]

such that `B=DA` is a nonnegative integer matrix and

\[
\boxed{
B\nu\le D\nu-\eta.
}
\]

Conversely any such integer inequality yields the rational certificate

\[
A\nu\le\nu-\eta/D.
\]

### Proof

Choose `D` divisible by every denominator of `A`, `v` and `delta`, and then scale
`v,delta` further by a common denominator so that the resulting vectors are
integral.  Multiplying the rational inequality by the common positive scale gives
the integer inequality.  Division proves the converse. ∎

This certificate is checkable using exact integer arithmetic only.

## 3. Robustness under bounded collateral errors

Let `E` be a nonnegative error matrix accounting for omitted line, interface,
carry or finite-enumeration offspring.

### Theorem CMR1272 -- PROVED

If

\[
Av\le v-\delta
\]

and

\[
Ev\le\theta\delta
\qquad(0\le\theta<1),
\]

then

\[
\boxed{
(A+E)v
\le
v-(1-\theta)\delta
<v.
}
\]

Hence `rho(A+E)<1`.

### Proof

Add the two componentwise inequalities.  The remaining slack is positive because
`theta<1`.  Apply CMR1270. ∎

A strict rational certificate therefore tolerates quantitatively bounded
unclassified collateral.

## 4. Constructive gluing of two product blocks

Consider a block upper-triangular offspring bound

\[
\widehat A
=
\begin{pmatrix}
A_1&C\\
0&A_2
\end{pmatrix},
\qquad C\ge0.
\]

Assume rational certificates

\[
A_iv_i\le v_i-\delta_i
\qquad(i=1,2).
\]

### Theorem CMR1273 -- PROVED

For every rational `t>0` satisfying

\[
\boxed{
t\delta_1>Cv_2}
\]

componentwise, the vector

\[
\boxed{v=(tv_1,v_2)}
\]

satisfies

\[
\widehat Av<v.
\]

Such a rational `t` always exists.  Consequently subcritical diagonal blocks glue
across arbitrary finite upper collateral `C`.

### Proof

The lower block gives

\[
A_2v_2\le v_2-\delta_2<v_2.
\]

The upper block gives

\[
tA_1v_1+Cv_2
\le
tv_1-t\delta_1+Cv_2<tv_1.
\]

Choose `t` larger than every finite ratio `(Cv_2)_j/(delta_1)_j`. ∎

Iterating from the last diagonal block upward glues any finite block-upper-
triangular product or wall system.

## 5. Rowwise randomization is unnecessary for a fixed weight

For one parent class `sigma`, let the available feasible bank laws have expected
offspring rows

\[
a^{(1)},\ldots,a^{(r)}\ge0.
\]

### Theorem CMR1274 -- PROVED

Fix `v>0`.  If a convex combination

\[
\bar a=\sum_j\lambda_ja^{(j)},
\qquad
\lambda_j\ge0,
\quad
\sum_j\lambda_j=1,
\]

satisfies

\[
\bar a\cdot v<v_\sigma,
\]

then at least one deterministic row satisfies

\[
\boxed{a^{(j)}\cdot v<v_\sigma.}
\]

### Proof

If every deterministic row had dot product at least `v_sigma`, their convex
combination would also. ∎

Thus once a Lyapunov vector is proposed, one may select a single bank law in every
row.  Randomization is useful for discovering weights but is not required in the
final policy certificate.

## 6. Exact certificates from finite bank enumeration

Suppose class `sigma` uses a finite bank with `q_sigma` equally weighted response
states, and let `n_{sigma tau}` be the total number of class-`tau` offspring across
that bank.  Then

\[
A_{\sigma\tau}
=
\frac{n_{\sigma\tau}}{q_\sigma}.
\]

### Theorem CMR1275 -- PROVED

For a positive integer weight vector `nu`, the row inequality

\[
( A\nu)_\sigma<\nu_\sigma
\]

is exactly the integer inequality

\[
\boxed{
\sum_\tau n_{\sigma\tau}\nu_\tau
<
q_\sigma\nu_\sigma.
}
\]

Therefore an enumerated finite spectral certificate can be verified without
floating-point arithmetic or explicit permanent division.

### Proof

Multiply the rational row inequality by the positive integer `q_sigma`. ∎

Nonuniform rational bank laws are handled by clearing their denominators.

## 7. Coarse-class certificates lift to exact triples

Let `pi` map exact physical triple classes onto a finite coarse signature set
`Sigma`.  Give every exact class `T` the weight `v_{pi(T)}`.  Suppose an upper
matrix `Ahat` bounds, for every targeted exact class of coarse type `sigma`, the
expected number of new exact credits of each coarse type `tau`.

### Theorem CMR1276 -- PROVED

If

\[
\boxed{\widehat Av<v,}
\]

then the lifted exact-triple weight strictly decreases under every targeted
response covered by the upper matrix.

### Proof

The expected total weight of exact offspring is at most the coarse offspring row
dotted with `v`.  The destroyed parent has weight `v_sigma`.  The displayed row
inequality makes the difference negative. ∎

This validates line, height, carry, owner or product signatures as long as their
matrix entries are honest upper bounds on exact offspring counts.

## 8. Exact-certificate endpoint

### Corollary CMR1277 -- PROVED

A successful target-versus-collateral proof at a canonical owner may be certified
by finite data:

1. a finite credit signature set;
2. one deterministic feasible bank law for every active signature;
3. an exact rational or integer upper offspring matrix;
4. a positive rational or integer weight vector;
5. strict componentwise inequalities `Av<v`;
6. optional error bounds absorbed by CMR1272; and
7. product or wall blocks glued by CMR1273.

The remaining open task is to construct these data from the corrected local
envelopes, line/height/carry inventories, fixed interfaces and CRT projection
classes.  Numerical evidence alone is insufficient, but any discovered candidate
can be converted into this exact certificate format.

No all-`n` theorem is claimed.  Rational solves, integer scaling, perturbation
slack, deterministic row selection, finite-bank integer checks, coarse-class lifts
and constructive block gluing are checked in
[`scripts/verify_prime_power_rational_spectral_certificate.py`](../scripts/verify_prime_power_rational_spectral_certificate.py).
