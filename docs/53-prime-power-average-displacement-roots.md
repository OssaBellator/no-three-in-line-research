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

### Theorem CMR59 — PROVED

One has

\[
\sum_{\lambda\bmod M}\rho_M(D(\lambda))
=
\varphi(M).
\]

Thus the mean root multiplicity is `1-1/p`.

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

Because `2R` is a unit, this is bijective, with

\[
z=(u+v)/2,
\qquad
\lambda=(v-u)/(2R).
\]

The congruence becomes

\[
uv\equiv-4cRS^{-1}\pmod M.
\]

The right side is a unit. Hence `u` may be any of the `phi(M)` units, and `v`
is then uniquely determined. ∎

## 2. Unit scalar average

Let

\[
A=-4cRS^{-1}.
\]

### Theorem CMR60 — PROVED

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

The restricted mean is at most one.

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

### Corollary CMR61 — PROVED

Across a complete unit residue system for `tau` modulo `p^(m-w)`, the total
number of reduced CMR7 endpoint classes is at most

\[
\varphi(p^{m-w}).
\]

After allowing the `p^w` lifts to the full stratum parameter, the total
candidate endpoint residues are fewer than `p^m`. Summing all
`w=0,...,m-1` gives fewer than `mp^m` candidates for one stratum and one
primitive direction when all scalar residues are included.

### Proof

Apply CMR60 at modulus `p^(m-w)` and multiply by the maximum `p^w` lifts of one
reduced endpoint class. ∎

## 4. Remaining analytic gap

Exact real secants use a short signed scalar interval of length approximately

\[
\frac{p^m}{H},
\]

not a complete residue system. CMR59--CMR61 show that large Hensel
multiplicities cannot persist on average around the whole ring. The harmonic-
energy problem is thereby reduced to an **incomplete average-root estimate**
for these real-box intervals.

The exact identities are checked in
[`scripts/verify_prime_power_average_roots.py`](../scripts/verify_prime_power_average_roots.py).