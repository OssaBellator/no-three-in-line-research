# Canonical collateral profiles decompose into heavy lines, disjoint banks, or secant stars

CMR552--CMR557 attach one time-independent rank-zero/rank-one collateral
profile to every canonical compatible-pair selector.  A static selector has

\[
S_\Sigma
=
\frac{V_0(\Sigma)}{(n)_3}
+
\frac{V_1(\Sigma)}{(n)_2}
\ge
c_q,
\qquad
c_q=
\frac{11}{30}\left(1-\frac2q\right),
\]

for `q>=4`.  The remaining question is geometric: what does this fixed mass
look like?

This chapter gives an exact answer.  Rank-one atoms group into secant lines
through the two paid endpoints.  Distinct such lines through one endpoint have
pairwise disjoint residual supports.  Rank-zero atoms group into residual
supporting lines.  Many distinct rank-zero lines yield either a cell-disjoint
triple bank or a repeated-cell secant star by a maximal-matching argument.

Thus a static canonical profile is never an unstructured collection of
collisions.  It reaches the same heavy-line, secant-star, matching-vertex-wall,
and disjoint-bank objects already used by the line-energy and carry programme.

Fix one canonical selector signature

\[
\Sigma=(E,Z,L),
\qquad
Z=\{z_1,z_2\},
\]

with residual side

\[
n=m-2\ge5.
\]

Let `U_\Sigma` be its canonical allowed residual host from CMR552.  All
candidate triples below are atoms of the fixed CMR553 profile.

## 1. Rank polarization

For `z\in Z`, let `V_1(z)` be the number of rank-one profile atoms using the
paid endpoint `z`.  Then

\[
V_1=V_1(z_1)+V_1(z_2).
\]

### Theorem CMR558 — PROVED

Assume `q>=4` and that `\Sigma` is a static collateral signature.  At least one
of the following holds.

1. **Rank-zero mass.**
   \[
   \boxed{
   V_0
   \ge
   \frac{c_q}{2}(n)_3.
   }
   \]
2. **One-endpoint rank-one mass.**  Some `z\in Z` satisfies
   \[
   \boxed{
   V_1(z)
   \ge
   \frac{c_q}{4}(n)_2.
   }
   \]

Since `q>=4`, one always has

\[
\boxed{c_q\ge\frac{11}{60}.}
\]

### Proof

The static condition gives

\[
\frac{V_0}{(n)_3}+
\frac{V_1}{(n)_2}
\ge c_q.
\]

Hence one normalized summand is at least `c_q/2`.  This gives the first
alternative or

\[
V_1\ge\frac{c_q}{2}(n)_2.
\]

In the latter case one of the two paid endpoints supports at least half of
`V_1`, giving the second conclusion.  Finally,
`1-2/q>=1/2` for `q>=4`. ∎

## 2. Exact decomposition by supporting line

For a nonaxis residual grid line `K`, let

\[
r_K=|K\cap U_\Sigma|
\]

be its number of canonical allowed residual cells.  Let `T_0(K)` be the number
of rank-zero profile atoms supported on `K`.

For `z\in Z` and a nonaxis line `K` through `z` with `K\ne L`, let `T_1(z,K)`
be the number of rank-one profile atoms using `z` and supported on `K`.

### Theorem CMR559 — PROVED

One has the exact identities

\[
\boxed{
V_0=
\sum_K T_0(K)
}
\]

and

\[
\boxed{
V_1(z)=
\sum_{\substack{K\ni z\\K\ne L}}T_1(z,K).
}
\]

Moreover,

\[
\boxed{
T_0(K)\le\binom{r_K}{3},
\qquad
T_1(z,K)\le\binom{r_K}{2},
\qquad
r_K\le n.
}
\]

### Proof

Every candidate-only collinear triple has one unique real supporting line.
A rank-zero atom contains three residual matching cells, so its line is
nonaxis and it is counted by exactly one `T_0(K)`.

A rank-one atom contains one fixed paid endpoint and two residual matching
cells.  Its supporting line is nonaxis.  CMR550 shows that it is distinct from
the paid line `L`, so it is counted by exactly one `T_1(z,K)`.

A nonaxis line meets each residual source row and target column in at most one
cell.  Hence it contains at most `n` residual cells.  Rank-zero atoms on it are
among the three-subsets of those cells, and rank-one atoms through a fixed paid
endpoint are among the two-subsets. ∎

For integers `H>=1`, define

\[
\rho_2(H)=
\min\left\{r\ge2:\binom r2\ge H\right\},
\]

and

\[
\rho_3(H)=
\min\left\{r\ge3:\binom r3\ge H\right\}.
\]

Thus `H` atoms on one line force at least `\rho_2(H)` or `\rho_3(H)` profile
cells on that line.

## 3. Rank-one mass gives a heavy secant or a disjoint secant star

Fix a paid endpoint `z` and put

\[
W_1=V_1(z).
\]

### Theorem CMR560 — PROVED

For every integer `H>=2`, at least one of the following holds.

1. **Heavy rank-one secant.**  Some line `K\ni z`, `K\ne L`, satisfies
   \[
   \boxed{T_1(z,K)\ge H.}
   \]
   Consequently
   \[
   \boxed{r_K\ge\rho_2(H).}
   \]
2. **Many disjoint secant arms.**  At least
   \[
   \boxed{
   M_1
   \ge
   \left\lceil\frac{W_1}{H-1}\right\rceil
   }
   \]
   distinct lines through `z` support rank-one atoms.  Choosing one atom from
   each such line gives `M_1` triples sharing exactly the paid endpoint `z`,
   whose two-cell residual arms are pairwise disjoint.

### Proof

If no line contains `H` atoms, every occupied line contains at most `H-1`.
The line decomposition in CMR559 then requires at least
`ceil(W_1/(H-1))` occupied lines.

Two distinct real lines through `z` intersect only at `z`.  Their chosen
rank-one atoms therefore have disjoint residual two-cell arms.  The occupancy
conclusion in the heavy branch follows from CMR559. ∎

The second branch is exactly a repeated-cell secant star with cell-disjoint
outside pairs.

## 4. Rank-zero mass gives a heavy line, a disjoint bank, or a residual secant star

Put

\[
W_0=V_0.
\]

### Theorem CMR561 — PROVED

Fix integers `H,s>=2`.  At least one of the following holds.

1. **Heavy rank-zero line.**  Some residual line `K` satisfies
   \[
   \boxed{T_0(K)\ge H,}
   \]
   hence
   \[
   \boxed{r_K\ge\rho_3(H).}
   \]
2. **Cell-disjoint residual bank.**  There are `s` pairwise cell-disjoint
   rank-zero profile triples on distinct supporting lines.
3. **Residual repeated-cell star.**  Some residual cell belongs to at least
   \[
   \boxed{
   \left\lceil
   \frac{M_0}{3(s-1)}
   \right\rceil
   }
   \]
   selected profile triples on distinct supporting lines, where
   \[
   \boxed{
   M_0
   \ge
   \left\lceil\frac{W_0}{H-1}\right\rceil.
   }
   \]
   Their two-cell outside arms are pairwise disjoint.

### Proof

If the first branch fails, CMR559 implies that at least

\[
M_0\ge\left\lceil\frac{W_0}{H-1}\right\rceil
\]

distinct residual lines support atoms.  Choose one profile triple from each
line, obtaining a three-uniform hypergraph with `M_0` edges.

Take a maximal cell-disjoint subfamily.  If it has at least `s` members, the
second conclusion holds.  Otherwise its union contains at most `3(s-1)` cells
and meets every chosen triple by maximality.  One of those cells therefore
belongs to at least

\[
\left\lceil\frac{M_0}{3(s-1)}\right\rceil
\]

chosen triples.

Those triples lie on distinct real lines through the common cell.  Distinct
such lines share no other cell, so their outside pairs are pairwise disjoint.
The heavy-line occupancy conclusion is CMR559. ∎

Thus the concentration branch is again an exact secant star, now centred at a
residual matching cell.

## 5. Square-root line extraction

### Theorem CMR562 — PROVED

Let `W>=1` be either `W_1` in CMR560 or `W_0` in CMR561, and put

\[
H_W=\lceil\sqrt W\rceil.
\]

If `W=1`, one supporting line exists.  If `W>=2`, then the corresponding line
decomposition gives either

\[
\boxed{
\text{one line supporting at least }H_W\text{ atoms}
}
\]

or

\[
\boxed{
\text{at least }H_W\text{ distinct occupied supporting lines}.
}
\]

In the rank-one case the latter lines give `H_W` disjoint secant arms.  In the
rank-zero case those lines enter the disjoint-bank versus repeated-cell-star
alternative of CMR561.

### Proof

Use `H=H_W` in CMR560 or CMR561.  Since

\[
W>(H_W-1)^2,
\]

one has

\[
\left\lceil\frac{W}{H_W-1}\right\rceil\ge H_W
\]

when `H_W>=2`. ∎

## 6. Canonical static-profile endpoint

### Corollary CMR563 — PROVED

Fix `q>=4`.  Every static canonical selector profile reaches at least one of
the following exact geometric structures.

1. **Heavy paid-endpoint secant.**  One line through a paid endpoint and
   distinct from the paid line supports many rank-one atoms.
2. **Paid-endpoint secant-star bank.**  Many rank-one atoms share one paid
   endpoint and have pairwise disjoint residual arms.
3. **Heavy residual collision line.**  One residual line supports many
   rank-zero atoms.
4. **Cell-disjoint residual triple bank.**  Many fixed target-load atoms have
   pairwise disjoint cell support.
5. **Residual repeated-cell secant star.**  Many rank-zero atoms share one
   residual cell and have pairwise disjoint outside arms.

Quantitatively, the rank-one branch of CMR558 has

\[
W_1\ge\frac{c_q}{4}(n)_2,
\]

and the rank-zero branch has

\[
W_0\ge\frac{c_q}{2}(n)_3.
\]

CMR560--CMR562 then give tunable or square-root lower bounds for the selected
line/star/bank structure.

### Proof

Apply CMR558.  In the rank-one branch use CMR560 or CMR562.  In the rank-zero
branch use CMR561 or CMR562. ∎

## 7. Revised frontier

The static side of the canonical selector ledger is now geometrically
classified.

- Rank-one collateral is a heavy secant or an exact cell-disjoint secant star
  through a paid endpoint.
- Rank-zero collateral is a heavy residual line, a cell-disjoint target bank,
  or an exact residual secant star.
- The selector signature, paid line, supporting lines, and atom sets are all
  fixed; no temporal double counting remains.

These objects coincide with existing endpoints:

- heavy lines feed line-energy, primitive-height, quotient, and carry analysis;
- repeated-cell stars feed CMR390-style wall/secant-star alternatives;
- cell-disjoint banks feed simultaneous repair and target-load averaging.

The remaining prime-power task is payment for these already-canonical geometric
structures and for the persistent canonical-edge branch of CMR557.  One must
show strict potential decrease, protected-reserve depletion, full-token return,
deletion ancestry, or envelope expansion without reusing the same fixed
line/star/bank certificate.

No all-`n` theorem is claimed.  Rank polarization, exact line decomposition,
line occupancy bounds, secant-arm disjointness, and the maximal-matching
packing/concentration step are checked in
[`scripts/verify_prime_power_canonical_collateral_lines.py`](../scripts/verify_prime_power_canonical_collateral_lines.py).
