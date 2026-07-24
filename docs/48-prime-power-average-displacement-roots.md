# Exact average root counts for reciprocal displacement quadratics

CMR7 reduces every same-stratum fixed displacement to one corrected square-root
congruence. Scaling one primitive direction gives an exact complete-residue
average.

Let `p` be odd, `M=p^m`, and fix units `R,S,c` modulo `M`. Define

\[
D(\lambda)=(\lambda R)^2-4cRS^{-1}\pmod M,
\]

and let `rho_M(d)` be the number of square roots of `d` modulo `M`.

## 1. Complete scalar average

### Theorem CMR47 — PROVED

\[
\sum_{\lambda\bmod M}\rho_M(D(\lambda))=\varphi(M).
\]

### Proof

The sum counts pairs satisfying

\[
z^2-(\lambda R)^2\equiv-4cRS^{-1}\pmod M.
\]

The invertible change

\[
u=z-\lambda R,
\qquad v=z+\lambda R
\]

turns this into `uv=-4cRS^{-1}`. The right side is a unit, so `u` has
`phi(M)` choices and determines `v`. ∎

## 2. Unit scalar average

Put `A=-4cRS^{-1}`.

### Theorem CMR48 — PROVED

\[
\sum_{\lambda\in(\mathbb Z/M\mathbb Z)^\times}\rho_M(D(\lambda))
=
\begin{cases}
\varphi(M),&A\text{ nonsquare modulo }p,\\
\varphi(M)-2p^{m-1},&A\text{ square modulo }p.
\end{cases}
\]

Thus the unit-scalar mean is at most one.

### Proof

Under the same change of variables, `lambda` is a unit exactly when `v-u` is a
unit. Since `v=A/u`, failure occurs precisely when `u^2=A` modulo `p`. A
nonsquare excludes no unit residue; a square excludes two residue classes, each
with `p^(m-1)` lifts. ∎

## 3. Displacement consequence

Fix endpoint valuation `r`, a primitive direction `(R,S)` with unit coordinates,
and write `m=k-r`. For additional scalar valuation `w`, the corrected CMR7
discriminant modulo `p^(m-w)` is

\[
(\tau R)^2-4c_rRS^{-1}.
\]

### Corollary CMR49 — PROVED

Across a complete unit residue system for `tau`, the reduced endpoint classes
total at most `phi(p^(m-w))`. After the maximum `p^w` lifts, fewer than `p^m`
full endpoint residues occur. Summing `w=0,...,m-1` gives fewer than `mp^m`
candidates for one stratum and primitive direction over a complete scalar
system.

### Proof

Apply CMR48 at modulus `p^(m-w)` and multiply by the lift factor. ∎

Real secants use a short signed interval of scalar values, not a complete
residue system. The remaining analytic target is therefore an incomplete
average-root bound for intervals of length about `p^m/H`.

The checker is
[`scripts/verify_prime_power_average_roots.py`](../scripts/verify_prime_power_average_roots.py).
