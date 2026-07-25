# Canonical collateral profiles decompose into heavy lines, disjoint banks, or secant stars

CMR552--CMR557 attach one time-independent rank-zero/rank-one collateral
profile to every canonical compatible-pair selector. A static selector has

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

for `q>=4`. This chapter gives an exact geometric classification. Rank-one
atoms group into secant lines through the paid endpoints. Distinct such lines
through one endpoint have pairwise disjoint residual supports. Rank-zero atoms
group into residual supporting lines. Many distinct rank-zero lines yield
either a cell-disjoint triple bank or a repeated-cell secant star.

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

Let `U_\Sigma` be its canonical allowed residual host from CMR552.

## 1. Rank polarization

For `z\in Z`, let `V_1(z)` be the number of rank-one profile atoms using `z`.

### Theorem CMR558 — PROVED

Assume `q>=4` and `\Sigma` is static. At least one of the following holds.

1. **Rank-zero mass.**
   \[
   \boxed{V_0\ge\frac{c_q}{2}(n)_3.}
   \]
2. **One-endpoint rank-one mass.** Some `z\in Z` satisfies
   \[
   \boxed{V_1(z)\ge\frac{c_q}{4}(n)_2.}
   \]

Also

\[
\boxed{c_q\ge\frac{11}{60}.}
\]

### Proof

The static inequality forces one normalized rank term to be at least `c_q/2`.
In the rank-one case, one of the two paid endpoints supports at least half of
`V_1`. The last bound follows from `q>=4`. ∎

## 2. Exact supporting-line decomposition

For a nonaxis residual line `K`, let

\[
r_K=|K\cap U_\Sigma|
\]

and let `T_0(K)` count rank-zero profile atoms on `K`. For `z\in Z` and a line
`K` through `z`, `K\ne L`, let `T_1(z,K)` count rank-one profile atoms using
`z` and supported on `K`.

### Theorem CMR559 — PROVED

One has

\[
\boxed{V_0=\sum_KT_0(K)}
\]

and

\[
\boxed{V_1(z)=\sum_{\substack{K\ni z\\K\ne L}}T_1(z,K).}
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

Every collinear candidate triple has one unique supporting real line. Rank-zero
atoms contain three residual matching cells. Rank-one atoms contain one paid
endpoint and two residual matching cells; CMR550 excludes the paid line. A
nonaxis line meets each residual source row and target column at most once, so
it contains at most `n` residual cells. The binomial capacities follow. ∎

For `H>=1`, define

\[
\rho_2(H)=\min\{r\ge2:\binom r2\ge H\},
\qquad
\rho_3(H)=\min\{r\ge3:\binom r3\ge H\}.
\]

## 3. Rank-one heavy line or disjoint secant star

Fix a paid endpoint `z` and put `W_1=V_1(z)`.

### Theorem CMR560 — PROVED

For every integer `H>=2`, at least one of the following holds.

1. Some line `K\ni z`, `K\ne L`, satisfies
   \[
   \boxed{T_1(z,K)\ge H,\qquad r_K\ge\rho_2(H).}
   \]
2. At least
   \[
   \boxed{M_1\ge\left\lceil\frac{W_1}{H-1}\right\rceil}
   \]
   distinct lines through `z` support atoms. Choosing one atom per line gives
   triples sharing exactly `z`, with pairwise disjoint residual two-cell arms.

### Proof

If no line contains `H` atoms, every occupied line contributes at most `H-1`,
so CMR559 gives the line count. Two distinct real lines through `z` intersect
only at `z`, so their residual arms are disjoint. ∎

## 4. Rank-zero heavy line, disjoint bank, or residual star

Put `W_0=V_0`.

### Theorem CMR561 — PROVED

Fix integers `H,s>=2`. At least one of the following holds.

1. Some residual line `K` satisfies
   \[
   \boxed{T_0(K)\ge H,\qquad r_K\ge\rho_3(H).}
   \]
2. There are `s` pairwise cell-disjoint rank-zero profile triples on distinct
   supporting lines.
3. Some residual cell belongs to at least
   \[
   \boxed{
   \left\lceil\frac{M_0}{3(s-1)}\right\rceil
   }
   \]
   selected profile triples on distinct lines, where
   \[
   \boxed{M_0\ge\left\lceil\frac{W_0}{H-1}\right\rceil.}
   \]
   Their outside two-cell arms are pairwise disjoint.

### Proof

If the first branch fails, choose one atom on each of at least `M_0` occupied
lines. Take a maximal cell-disjoint subfamily. If it has size at least `s`, use
branch 2. Otherwise its union has at most `3(s-1)` cells and meets every chosen
triple. One cell therefore lies in at least the displayed number. The relevant
triples lie on distinct lines through that cell, so their outside pairs are
disjoint. ∎

## 5. Square-root extraction

### Theorem CMR562 — PROVED

Let `W>=1` be either `W_1` or `W_0`, and put

\[
H_W=\lceil\sqrt W\rceil.
\]

If `W=1`, one supporting line exists. If `W>=2`, the corresponding line
decomposition gives either one line supporting at least `H_W` atoms or at
least `H_W` distinct occupied lines.

### Proof

Use `H=H_W`. Since `W>(H_W-1)^2`,

\[
\left\lceil\frac{W}{H_W-1}\right\rceil\ge H_W.
\]

Apply CMR560 or CMR561. ∎

## 6. Canonical static-profile endpoint

### Corollary CMR563 — PROVED

Every static canonical selector profile reaches at least one of:

1. a heavy paid-endpoint secant;
2. a paid-endpoint secant-star bank with disjoint residual arms;
3. a heavy residual collision line;
4. a cell-disjoint residual triple bank;
5. a residual repeated-cell secant star.

Quantitatively, the rank-one branch has

\[
W_1\ge\frac{c_q}{4}(n)_2,
\]

and the rank-zero branch has

\[
W_0\ge\frac{c_q}{2}(n)_3.
\]

### Proof

Apply CMR558, followed by CMR560--CMR562. ∎

## 7. Revised frontier

The static canonical profile is no longer unstructured. Heavy lines feed line
energy, primitive-height, quotient, and carry analysis. Repeated-cell stars
feed the existing wall/secant-star alternatives. Cell-disjoint banks feed
simultaneous repair, deletion, and target-load averaging.

No all-`n` theorem is claimed. Rank polarization, exact line decomposition,
line occupancy, secant-arm disjointness, and packing/concentration are checked
in the subsequent static-line and deletion verifiers.
