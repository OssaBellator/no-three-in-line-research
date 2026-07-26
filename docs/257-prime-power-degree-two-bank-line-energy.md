# Degree-two bank collateral is an exact three-rank line energy

CMR1198--CMR1221 reduce one fixed-target response to a normalized collateral score
and assign every created triple to one entering edge.  The score can be written
exactly in the line language used by the prefix, primitive-height and carry
chapters.

Retain the complete degree-two bank

\[
G=K_{n,n}\setminus(O\cup F),
\qquad n\ge4,
\]

where `O,F` are disjoint perfect matchings.  For every real line `L` meeting the
`n x n` board, put

\[
o_L=|O\cap L|,
\qquad
g_L=|E(G)\cap L|.
\]

Let `c_r(G_L)` be the number of rank-`r` compatible edge subsets of `E(G) cap L`.
Thus `c_1(G_L)=g_L`; `c_2` counts matching-compatible pairs on the line; and `c_3`
counts matching-compatible triples.

Only finitely many lines contribute.

## 1. Exact rank-one line energy

### Theorem CMR1222 -- PROVED

The rank-one candidate count of CMR1201 is

\[
\boxed{
V_1
=
\sum_L\binom{o_L}{2}g_L.
}
\]

### Proof

A rank-one new triple contains exactly two fixed opposite-layer cells and one
allowed response edge.  Its three physical cells determine one real line.  On a
fixed line, choose the two `O` cells and the one `G` edge.  Conversely every such
choice is a physical collinear triple with residual prescription equal to that
single response edge. ∎

No ordering or multiplicity factor is present.

## 2. Exact rank-two line energy

### Theorem CMR1223 -- PROVED

\[
\boxed{
V_2
=
\sum_L o_L\,c_2(G_L).
}
\]

### Proof

A rank-two new triple has one fixed opposite-layer cell and a compatible pair of
response edges.  The triple determines its unique line, its unique fixed cell and
its unique unordered residual pair.  Conversely every fixed cell and compatible
pair on one line gives one candidate triple. ∎

## 3. Exact rank-three line energy

### Theorem CMR1224 -- PROVED

\[
\boxed{
V_3
=
\sum_L c_3(G_L).
}
\]

### Proof

A rank-three candidate is precisely a compatible three-edge subset of `G` lying on
one real line.  Three distinct physical cells determine one line, so it is counted
once. ∎

Combining CMR1222--CMR1224 gives

\[
\boxed{
\mathcal C(S;O,F)
=
\sum_L
\left[
\frac{\binom{o_L}{2}g_L}{n}
+
\frac{o_Lc_2(G_L)}{(n)_2}
+
\frac{c_3(G_L)}{(n)_3}
\right].
}
\]

This is the exact degree-two-bank collateral functional.

## 4. Exact compatible-pair stock of the response graph

Let

\[
P_2(G)
=
\sum_Lc_2(G_L).
\]

Every compatible pair determines one real line, so this is also the total number
of rank-two partial matchings in `G`.

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

### Proof

The `(n-2)`-regular graph has `n(n-2)` edges.  From all unordered edge pairs,
subtract pairs sharing a source and pairs sharing a target.  Each of the `n`
source and `n` target vertices contributes `binom(n-2,2)` incompatible pairs.
Distinct edges cannot share both endpoints, so the two subtracted classes are
disjoint.  Algebra gives the factorized form. ∎

## 5. A line-cap upper bound for the normalized score

Put

\[
\rho=\max_Lo_L,
\qquad
\gamma=\max_Lg_L.
\]

### Theorem CMR1226 -- PROVED

\[
\boxed{
\mathcal C(S;O,F)
\le
\frac{\gamma\binom n2}{n}
+
\frac{\rho P_2(G)}{(n)_2}
+
\frac{(\gamma-2)_+P_2(G)}{3(n)_3}.
}
\]

### Proof

Every unordered pair of cells of `O` determines one line, hence

\[
\sum_L\binom{o_L}{2}=\binom n2.
\]

Use `g_L<=gamma` in CMR1222.

For rank two, use `o_L<=rho` and

\[
\sum_Lc_2(G_L)=P_2(G).
\]

For rank three, count a compatible triple by one of its three compatible pairs.
A pair on `L` has at most `(gamma-2)_+` possible third `G` cells on that line.
Thus

\[
3V_3\le(\gamma-2)_+P_2(G).
\]

Insert the three bounds into the exact score. ∎

The line caps may be replaced by height-localized caps on any subfamily of lines.

## 6. Explicit line-cap improvement criterion

Define

\[
\mathcal U_n(\rho,\gamma)
=
\frac{\gamma\binom n2}{n}
+
\frac{\rho P_2(G)}{(n)_2}
+
\frac{(\gamma-2)_+P_2(G)}{3(n)_3}.
\]

### Corollary CMR1227 -- PROVED

For a current host with `b` unavailable allowed bank edges, if

\[
\boxed{
\kappa_n
\left[
\mathcal U_n(\rho,\gamma)
+
\frac{(\Phi(S)+1)b}{n}
\right]
<
D_S(e),
}
\]

then a feasible response state has strictly smaller physical triple potential.

### Proof

CMR1226 bounds the collateral term in CMR1208. ∎

Failure gives an explicit lower bound on one of target-line load, allowed-graph line
load or unavailable-edge inventory.

## 7. Edge-owner scores are line-local

For an allowed response edge `a`, let `mathcal L(a)` be the real lines through its
physical cell.

### Theorem CMR1228 -- PROVED

The rank-one owner score of `a` is exactly

\[
\boxed{
V_1(a)
=
\sum_{L\in\mathcal L(a)}\binom{o_L}{2}.
}
\]

Rank-two and rank-three owner scores are obtained by counting, on every line
through `a`, compatible pairs or triples for which `a` is the least residual edge
under the CMR1215 order.  Summing the edge-local line scores recovers the exact
functional of CMR1222--CMR1224.

### Proof

A rank-one atom has one residual edge, so that edge is automatically its owner.
For higher rank, partition every compatible line subset by its least edge.  This is
CMR1220 applied line by line. ∎

Thus collateral can be charged simultaneously to one absolute edge and one real
line.

## 8. Line-energy endpoint

### Corollary CMR1229 -- PROVED

The CMR1196 target-versus-collateral frontier now has an exact degree-two-bank
geometric form:

\[
\mathbb E N(Q)
\le
\kappa_n
\sum_L
\left[
\frac{\binom{o_L}{2}g_L}{n}
+
\frac{o_Lc_2(G_L)}{(n)_2}
+
\frac{c_3(G_L)}{(n)_3}
\right].
\]

Every summand has one line and one entering-edge owner.  The next quantitative
step is to average or localize this line energy over forbidden extensions `F`, and
to compare its height/carry decomposition with the exact target incidence
`3Phi(S)` and the unavailable-edge term of CMR1208.

No all-`n` theorem is claimed.  Exact line decompositions, compatible-pair stock,
line-cap arithmetic and owner localization are checked in
[`scripts/verify_prime_power_degree_two_bank_line_energy.py`](../scripts/verify_prime_power_degree_two_bank_line_energy.py).
