# Recursive quotient structure of the prime-power bank

The top-digit blocks are not merely collision containers. Contracting them
recovers the same completed-reciprocal companion pair at the next smaller
prime-power exponent.

Let

\[
N=p^k,
\qquad k\ge2,
\qquad a=p^{k-1},
\]

and let

\[
f_k=R_{(c_0,\ldots,c_{k-1})},
\qquad
g_k=\sigma_p\circ f_k.
\]

Write

\[
\rho:[N]\to[a],
\qquad \rho(z)=z\bmod a.
\]

For a residue \(\bar x\in[a]\), its top-digit fibre is

\[
X_{\bar x}=\{\bar x+ja:0\le j<p\}.
\]

## 1. Exact quotient self-similarity

### Theorem CMR25 — PROVED

For every \(x\in[N]\),

\[
\rho(f_k(x))
=
f_{k-1}(\rho(x)),
\]

where \(f_{k-1}\) uses the truncated parameter sequence
\((c_0,\ldots,c_{k-2})\). Likewise,

\[
\rho(g_k(x))
=
g_{k-1}(\rho(x)).
\]

Moreover, the restriction of each layer to a column fibre is a bijection onto
the corresponding row fibre. Hence contracting every top-digit fibre in rows
and columns turns the two-layer host \(f_k\cup g_k\) exactly into
\(f_{k-1}\cup g_{k-1}\).

### Proof

If \(\rho(x)=0\), then `x` lies in the terminal fibre and both sides of the
first identity are zero.

Otherwise write

\[
x=p^ru,
\qquad r<k-1.
\]

Reducing

\[
p^rc_ru^{-1}\pmod {p^k}
\]

modulo \(a=p^{k-1}\) is exactly the completed reciprocal formula modulo
\(p^{k-1}\), with the unit inverse reduced modulo \(p^{k-r-1}\). This proves
the first identity. The companion identity follows by reducing

\[
[(1+e_p)f_k(x)+1]_N
\]

modulo `a`.

CMR19–CMR20 prove that every fibre restriction uses all `p` rows of the target
row fibre exactly once. ∎

## 2. Lifting arbitrary saturated quotient states

A saturated state at modulus `a` is represented by two permutations

\[
P_0,P_1:[a]\to[a]
\]

such that

\[
P_0(\bar x)\ne P_1(\bar x)
\qquad(\bar x\in[a]).
\]

### Theorem CMR26 — PROVED

Every saturated quotient state \((P_0,P_1)\) has exactly

\[
(p!)^{2a}
\]

saturated lifts to modulus `N` obtained as follows:

- for each quotient column \(\bar x\), assign the `p` columns in
  \(X_{\bar x}\) bijectively to the `p` rows in the row fibre
  \(\rho^{-1}(P_0(\bar x))\);
- independently assign the same columns bijectively to the row fibre
  \(\rho^{-1}(P_1(\bar x))\) in the second layer.

### Proof

For each layer, the quotient permutation uses every row-fibre label exactly
once. The lifted row fibres are therefore pairwise disjoint and cover all
rows. A bijection inside every fibre makes each layer a permutation of `[N]`.

At one column fibre, the two quotient row labels are distinct. Their row
fibres are disjoint, so the two lifted cells in every actual column are
distinct. Thus the union is saturated. There are `p!` independent bijections
for each of two layers and each of `a` column fibres. ∎

## 3. Recursive multiscale bank

Start with any nonempty family \(\Omega_1\) of saturated states at modulus
`p`. Define \(\Omega_k\) recursively by taking every state in
\(\Omega_{k-1}\) and all its CMR26 lifts.

### Corollary CMR27 — PROVED

The recursive bank contains

\[
|\Omega_k|
=
|\Omega_1|
(p!)^{2(p+p^2+\cdots+p^{k-1})}
=
|\Omega_1|
(p!)^{2(N-p)/(p-1)}
\]

saturated states.

Under uniform recursive choices, every compatible cell prescription has an
exact probability obtained by multiplying a factor

\[
\frac1{(p)_r}
\]

for each constrained layer-fibre bijection at every level of the `p`-adic
quotient tree, together with the probability of the induced base prescription
in \(\Omega_1\).

### Proof

The state count follows by multiplying the CMR26 lift factor at every exponent.
The probability law follows because all fibre bijections are independent and
uniform, and a compatible prescription of `r` distinct images in one
bijection occurs with probability `1/(p)_r`. ∎

## 4. Significance

The composite-modulus repair space is now genuinely multiscale:

- deterministic top-digit collision blocks form the finest scale;
- contracting one scale recovers the identical algebraic host;
- quotient states can be changed and lifted, rather than keeping block labels
  frozen;
- the complete cylinder law is signature-aware along the `p`-adic tree.

The remaining concentration theorem should therefore use a recursive
certificate potential, charging a collinear triple at the first quotient level
where its three column or row paths separate. A one-level uniform first moment
cannot see this hierarchy and is obstructed by CMR23.

The finite checks are in
[`scripts/verify_prime_power_recursive_quotient.py`](../scripts/verify_prime_power_recursive_quotient.py).
