# Block collateral energy and block-shadow closure

## 1. Geometry of an order-\(h\) block

Write \(n=qh\). A coset absorber block is an \(h\times h\) subgrid

\[
\mathcal B=C\times R,
\]

where coordinates in \(C\) and \(R\) differ by multiples of \(q\).

### Lemma B1 — PROVED

Every line containing two distinct cells of \(\mathcal B\) has primitive height at most \(h-1\).

Hence if \(h\le H\), every line of height at least \(H\) meets \(\mathcal B\) in at most one cell.

## 2. Exact one-block collateral

Remove the current block state \(A_0\) and put \(E=S\setminus A_0\). Let \(\mathcal Q_H(E,\mathcal B)\) be the high lines that meet \(\mathcal B\) and contain at least two points of \(E\). Let

\[
\sigma_H(E,\mathcal B)=|\mathcal Q_H(E,\mathcal B)|.
\]

For state \(t\), let \(c_t\) count the lines in \(\mathcal Q_H\) whose unique block intersection belongs to state \(t\).

### Theorem B2 — PROVED

\[
\Psi_H(E\cup A_t)=\Psi_H(E)+c_t,
\qquad
\sum_tc_t=\sigma_H(E,\mathcal B).
\]

If the current state is zero, then

\[
\Psi_H(E\cup A_t)-\Psi_H(S)=c_t-c_0.
\]

Thus a negative-drift state exists whenever

\[
\sigma_H<hc_0.
\]

No unanchored internal high-line error term exists.

## 3. Blocker graph cleaning

For a removed block \(B\) and outside set \(X\), create a graph on \(X\): two outside points are adjacent when their high secant intersects \(B\).

A vertex cover removes all external secants through \(B\). Endpoints of a maximal matching give such a cover.

## 4. Whole-block closure

Instead of removing individual endpoint points, add every absorber block containing an endpoint to the reservoir and remove its entire current state.

### Theorem B3 — PROVED

Iterating maximal-matching cleaning terminates with a reservoir \(\mathcal R_*\) such that every reservoir block is shadow-clean relative to the remaining outside set.

If the matching sizes are \(|F_i|\), then

\[
|\mathcal R_*|\le|\mathcal R_0|+2\sum_i|F_i|.
\]

All selected-point endpoints recorded in different rounds are disjoint.

## 5. Independent completion energy

For a shadow-clean reservoir, let \(k_L\) be the number of reservoir blocks met by a high line. Define

\[
J_2=
\sum_{|X\cap L|=1}\binom{k_L}{2},
\qquad
J_3=
\sum_{|X\cap L|=0}\binom{k_L}{3}.
\]

Choosing independent uniform states gives

\[
\mathbb E[\text{new excess}]
\le
\frac{J_2}{h^2}+
\frac{J_3}{h^3}.
\]

This is correct but can be too large.

## 6. Product-state local lemma

For each block \(B\), let \(d_2(B)\) count anchored bad pair events involving \(B\), and \(d_3(B)\) candidate-only bad triple events. If

\[
\rho(B)=\frac{d_2(B)}{h^2}+\frac{d_3(B)}{h^3}
\le\frac1{20}
\]

for every block and \(h\ge4\), the variable Lovász local lemma gives a simultaneous completion with no new high defect.

The remaining obstruction is candidate-only concentration \(d_3(B)\), which cannot be removed by adding outside anchor blocks.
