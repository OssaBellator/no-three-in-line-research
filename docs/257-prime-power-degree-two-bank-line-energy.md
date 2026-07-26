# Degree-two bank collateral is an exact three-rank line energy

CMR1198--CMR1221 reduce one fixed-target response to a normalized collateral score
and assign every created triple to one entering edge.  The score can be written
exactly in the line language used by the prefix, primitive-height and carry
chapters, but the unchanged part of the old rematched layer must be subtracted.

Retain the complete degree-two bank

\[
G=K_{n,n}\setminus(O\cup F),
\qquad n\ge4,
\]

where `O,F` are disjoint perfect matchings.  Let `M` be the old rematched-layer
perfect matching, so the old physical state is `S=O union M`.  Put

\[
M_G=M\cap E(G),
\qquad
k=|M_G|.
\]

For every real line `L` meeting the `n x n` board, put

\[
o_L=|O\cap L|,
\qquad
g_L=|E(G)\cap L|,
\qquad
m_L=|M_G\cap L|,
\qquad
g_L^+=g_L-m_L.
\]

Let `c_r(G_L)` be the number of rank-`r` compatible edge subsets of
`E(G) cap L`.  Since `M_G` is a partial matching, every subset of `M_G cap L` is
compatible.

Only finitely many lines contribute.

## 1. Exact rank-one line energy

### Theorem CMR1222 -- PROVED

The rank-one candidate count of CMR1201 is

\[
\boxed{
V_1
=
\sum_L\binom{o_L}{2}g_L^+.
}
\]

### Proof

A rank-one response triple contains two fixed opposite-layer cells and one allowed
response edge `a`.  It is new exactly when `a` was not already selected by `M`.
The allowed old edges are precisely `M_G`, so on one line there are `g_L-m_L`
eligible response edges.  Choose the two `O` cells and that one genuinely new edge.
Every resulting triple has a unique line and is counted once. ∎

The earlier uncorrected expression with `g_L` would also count surviving old
triples supported by `M_G`.

## 2. Exact rank-two line energy

### Theorem CMR1223 -- PROVED

\[
\boxed{
V_2
=
\sum_L
 o_L
\left[
 c_2(G_L)-\binom{m_L}{2}
\right].
}
\]

### Proof

A rank-two response triple has one fixed `O` cell and one compatible response pair
on the same line.  It is old exactly when both response edges belonged to `M`.
The old allowed response edges on the line are `M_G cap L`, and every pair among
them is compatible.  Subtract those `binom(m_L,2)` old pairs from all compatible
pairs on the line. ∎

## 3. Exact rank-three line energy

### Theorem CMR1224 -- PROVED

\[
\boxed{
V_3
=
\sum_L
\left[
 c_3(G_L)-\binom{m_L}{3}
\right].
}
\]

### Proof

A rank-three candidate is a compatible three-edge subset of `G` on one line.  It is
already present in the old state exactly when all three edges lie in `M_G`.  The
old collinear triples on `L` are therefore the `binom(m_L,3)` triples of
`M_G cap L`. ∎

Combining CMR1222--CMR1224 gives the exact functional

\[
\boxed{
\mathcal C(S;O,F)
=
\sum_L
\left[
\frac{\binom{o_L}{2}g_L^+}{n}
+
\frac{o_L\left(c_2(G_L)-\binom{m_L}{2}\right)}{(n)_2}
+
\frac{c_3(G_L)-\binom{m_L}{3}}{(n)_3}
\right].
}
\]

## 4. Exact compatible-pair stocks

Let

\[
P_2(G)=\sum_Lc_2(G_L).
\]

Every compatible pair determines one real line.

### Theorem CMR1225 -- PROVED

\[
\boxed{
P_2(G)
=
\binom{n(n-2)}2
-2n\binom{n-2}2
=
\frac{n(n-2)(n^2-4n+5)}2.
}
\]

The number of compatible response pairs which are not wholly old is exactly

\[
\boxed{
P_2^+(G,M)
=
P_2(G)-\binom{k}{2}.
}
\]

### Proof

The `(n-2)`-regular graph has `n(n-2)` edges.  From all unordered edge pairs,
subtract pairs sharing a source and pairs sharing a target.  Each of the `n`
source and `n` target vertices contributes `binom(n-2,2)` incompatible pairs, and
those classes are disjoint.

Every pair of edges of the partial matching `M_G` is compatible and determines one
line.  Hence

\[
\sum_L\binom{m_L}{2}=\binom{k}{2},
\]

which gives the second identity. ∎

## 5. Corrected line-cap upper bound

Put

\[
\rho=\max_Lo_L,
\qquad
\gamma=\max_Lg_L,
\qquad
\gamma_+=\max_Lg_L^+.
\]

### Theorem CMR1226 -- PROVED

\[
\boxed{
\mathcal C(S;O,F)
\le
\frac{\gamma_+\binom n2}{n}
+
\frac{\rho P_2^+(G,M)}{(n)_2}
+
\frac{(\gamma-2)_+}{(n)_3}
\min\left\{
\frac{P_2(G)}3,
\frac{P_2^+(G,M)}2
\right\}.
}
\]

### Proof

Every unordered pair of `O` cells determines one line, so

\[
\sum_L\binom{o_L}{2}=\binom n2.
\]

Use `g_L^+<=gamma_+` for rank one.

For rank two, use `o_L<=rho` and

\[
\sum_L\left[c_2(G_L)-\binom{m_L}{2}\right]=P_2^+(G,M).
\]

For rank three, every compatible pair on a line has at most `(gamma-2)_+` possible
third `G` edges.  Counting all three pairs of each response triple gives

\[
3V_3\le(\gamma-2)_+P_2(G).
\]

Alternatively count only pairs not wholly in `M_G`.  Every new rank-three triple
has at least two such pairs, because it has at most two old edges.  Hence

\[
2V_3\le(\gamma-2)_+P_2^+(G,M).
\]

Take the better of the two bounds and insert all three estimates into the exact
functional. ∎

The caps may be localized by primitive height or prefix/carry class.

## 6. Explicit corrected line-cap criterion

Define `mathcal U_n(S;O,F)` to be the right side of CMR1226.

### Corollary CMR1227 -- PROVED

For a current host with `b` unavailable allowed bank edges, if

\[
\boxed{
\kappa_n
\left[
\mathcal U_n(S;O,F)
+
\frac{(\Phi(S)+1)b}{n}
\right]
<
D_S(e),
}
\]

then a feasible response state has strictly smaller physical triple potential.

### Proof

CMR1226 bounds the exact collateral score in CMR1208. ∎

Failure gives an explicit lower bound on opposite-layer line load, genuinely new
allowed-line load, higher-rank compatible-pair energy, or unavailable inventory.

## 7. Edge-owner scores are line-local

For an allowed response edge `a`, let `mathcal L(a)` be the real lines through its
physical cell.

### Theorem CMR1228 -- PROVED

The rank-one owner score is

\[
\boxed{
V_1(a)
=
\mathbf 1_{a\notin M}
\sum_{L\in\mathcal L(a)}\binom{o_L}{2}.
}
\]

Rank-two and rank-three owner scores count, on every line through `a`, compatible
pairs or triples which are not wholly contained in `M_G` and for which `a` is the
least residual edge under the CMR1215 order.  Summing the edge-local scores
recovers CMR1222--CMR1224.

### Proof

A rank-one triple supported by an old edge `a in M` already belongs to `S`; every
rank-one triple supported by `a notin M` is new.  For higher rank, partition the
corrected candidate subsets by their least edge. ∎

Thus every genuinely created triple has one absolute edge and one real-line owner.

## 8. Corrected line-energy endpoint

### Corollary CMR1229 -- PROVED

The degree-two-bank collateral expectation has the exact geometric upper bound

\[
\mathbb E N(Q)
\le
\kappa_n
\sum_L
\left[
\frac{\binom{o_L}{2}g_L^+}{n}
+
\frac{o_L\left(c_2(G_L)-\binom{m_L}{2}\right)}{(n)_2}
+
\frac{c_3(G_L)-\binom{m_L}{3}}{(n)_3}
\right].
\]

Every term counts only triples absent from the old state.  The next quantitative
step is to average or localize this corrected energy over forbidden extensions and
to compare it with `3Phi(S)` and the unavailable-edge penalty.

No all-`n` theorem is claimed.  Corrected line decompositions, new-pair stock,
line-cap arithmetic and owner localization are checked in
[`scripts/verify_prime_power_degree_two_bank_line_energy.py`](../scripts/verify_prime_power_degree_two_bank_line_energy.py).
