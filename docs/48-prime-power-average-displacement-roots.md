# Exact average root counts for reciprocal displacement quadratics

CMR7 reduces every same-stratum fixed displacement to one square-root
congruence. After correcting its discriminant sign, the family of congruences
obtained by scaling one primitive direction has an exact complete-residue
average.

Let `p` be odd, let `M=p^m`, and fix units `R,S,c` modulo `M`. Define

\[
D(\lambda)
=
(\lambda R)^2-4cRS^{-1}
\pmod M,
\]

and let `rho_M(d)` denote the number of square roots of `d` modulo `M`.

## 1. Complete scalar average

### Theorem CMR47 — PROVED

One has the exact identity

\[
\sum_{\lambda\bmod M}\rho_M(D(\lambda))
=
\varphi(M).
\]

In particular, the mean root multiplicity over all scalar residues is

\[
\frac{\varphi(M)}M=1-\frac1p.
\]

### Proof

The left side counts pairs `(z,lambda)` satisfying

\[
z^2-(\lambda R)^2
\equiv
-4cRS^{-1}
\pmod M.
\]

Put

\[
u=z-\lambda R,
\qquad
v=z+\lambda R.
\]

Because `2R` is a unit, this is a bijective linear change of variables, with

\[
z=(u+v)/2,
\qquad
\lambda=(v-u)/(2R).
\]

The congruence becomes

\[
uv\equiv-4cRS^{-1}\pmod M.
\]

The right side is a unit. Hence `u` may be any of the `phi(M)` units, and then
`v` is uniquely determined. ∎

## 2. Unit scalar average

Let

\[
A=-4cRS^{-1}.
\]

### Theorem CMR48 — PROVED

Restricting to unit scalars gives

\[
\sum_{\lambda\in(\mathbb Z/M\mathbb Z)^\times}
\rho_M(D(\lambda))
=
\begin{cases}
\varphi(M),&A\text{ is a nonsquare modulo }p,\\
\varphi(M)-2p^{m-1},&A\text{ is a square modulo }p.
\end{cases}
\]

The restricted mean is therefore at most one.

### Proof

Under the preceding bijection, `lambda` is a unit exactly when `v-u` is a unit.
Since `v=A/u`, failure occurs precisely when

\[
u^2\equiv A\pmod p.
\]

If `A` is a nonsquare, no unit `u` is excluded. If it is a square, exactly two
residue classes modulo `p` are excluded, each with `p^(m-1)` lifts modulo `M`.
∎

## 3. Consequence for CMR7 displacement classes

Fix an endpoint valuation stratum `r` and a primitive direction `(R,S)` with
`p` dividing neither coordinate. Put `m=k-r`. For scalar displacements with
additional valuation `w`, write

\[
(a,b)=p^{r+w}\tau(R,S),
\qquad p\nmid\tau.
\]

The corrected CMR7 discriminant modulo `p^(m-w)` is

\[
(\tau R)^2-4c_rRS^{-1}.
\]

### Corollary CMR49 — PROVED

Across a complete unit residue system for `tau` modulo `p^(m-w)`, the total
number of reduced CMR7 endpoint classes is at most

\[
\varphi(p^{m-w}).
\]

After allowing the `p^w` lifts from the reduced modulus back to the full
stratum parameter, the total candidate endpoint residues are at most

\[
p^w\varphi(p^{m-w})<p^m.
\]

Summing over all `w=0,...,m-1` gives fewer than

\[
mp^m
\]

candidate endpoint residues for one stratum and one primitive direction when
all scalar residues are included.

### Proof

Apply CMR48 at modulus `p^(m-w)` and then multiply by the maximum number `p^w`
of lifts of one reduced endpoint class. ∎

## 4. The remaining analytic gap

Exact real secants do not use a complete scalar residue system. The grid box
restricts the scalar to a short signed interval of length approximately

\[
\frac{p^m}{H},
\]

where `H=max(|R|,|S|)` is the direction height. CMR47--CMR49 show that the large
Hensel multiplicities cannot persist on average around the full residue ring.
The harmonic-energy problem is now reduced more sharply to an **incomplete
average-root estimate** for these short scalar intervals.

A bound of the form

\[
\sum_{|\tau|\le p^m/H}\rho_{p^m}(D(\tau))
\ll
\frac{p^m}{H}\log^C p^m+p^{m/2}\log^C p^m
\]

would substantially improve CMR38 and may lead to near-linear harmonic energy
after summing directions and valuation strata.

The exact identities are checked in
[`scripts/verify_prime_power_average_roots.py`](../scripts/verify_prime_power_average_roots.py).