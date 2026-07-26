# Restricted fixed-target banks have an explicit availability-penalized improvement criterion

CMR1198--CMR1205 control collateral in the complete degree-two response bank.  A
current matching host may omit some allowed response edges, so a low-collateral
ambient completion need not be feasible.  This chapter adds an exact feasibility
penalty.

Retain the fixed-target setup of CMR1198.  Let `H subseteq G` be the currently
available rematched-layer host and put

\[
B=E(G)\setminus E(H),
\qquad
b=|B|.
\]

For `R in mathcal B=PM(G)`, let

\[
r_H(R)=|R\cap B|.
\]

Thus `R` is feasible in the current host exactly when `r_H(R)=0`.

Write

\[
m=\Phi(S),
\qquad
W=m+1.
\]

## 1. Expected unavailable-edge use

### Theorem CMR1206 -- PROVED

Under the uniform complete-bank law,

\[
\boxed{
\mathbb E r_H(R)
\le
\frac{\kappa_n b}{n}
\le
\frac{16b}{n}.
}
\]

### Proof

Sum the indicators of the unavailable allowed edges.  Each rank-one edge has
bank probability at most `kappa_n/n` by CMR1200. ∎

The estimate deliberately uses the complete ambient bank and does not condition on
the feasible subbank.

## 2. A negative weighted response is feasible and improving

Put

\[
\Delta(R)=\Phi(Q_R)-\Phi(S).
\]

### Theorem CMR1207 -- PROVED

If

\[
\boxed{
\Delta(R)+W r_H(R)<0,
}
\]

then

\[
\boxed{r_H(R)=0,
\qquad
\Delta(R)<0.}
\]

### Proof

The physical potential is nonnegative, so `Delta(R)>=-m`.  If `r_H(R)>=1`, then

\[
\Delta(R)+Wr_H(R)
\ge
-m+(m+1)=1,
\]

contrary to the hypothesis.  Hence `r_H(R)=0`, and the displayed inequality then
says `Delta(R)<0`. ∎

The coefficient `m+1` is a safe integrality barrier.  Smaller local coefficients
may be substituted whenever a sharper lower bound on `Delta` is available.

## 3. Restricted-host one-bank criterion

Let `mathcal C(S;O,F)` and `D_S(e)` be the CMR1202 and CMR1203 quantities.

### Theorem CMR1208 -- PROVED

If

\[
\boxed{
\kappa_n
\left(
\mathcal C(S;O,F)
+
\frac{(m+1)b}{n}
\right)
<
D_S(e),
}
\]

then the current host contains a feasible response state `Q_R` satisfying

\[
\boxed{\Phi(Q_R)<\Phi(S).}
\]

### Proof

CMR1202--CMR1203 give

\[
\mathbb E\Delta(R)
\le
\kappa_n\mathcal C(S;O,F)-D_S(e).
\]

CMR1206 gives

\[
\mathbb E[Wr_H(R)]
\le
(m+1)\kappa_n b/n.
\]

The hypothesis makes the expectation of `Delta(R)+Wr_H(R)` negative.  Some
response has negative weighted value, and CMR1207 makes it feasible and improving.
∎

Thus host unavailability enters the target-versus-collateral inequality through one
explicit linear term.

## 4. Positive minima satisfy an availability-collateral barrier

### Corollary CMR1209 -- PROVED

If `S` is minimum among the currently feasible saturated states, then every
selected target cell `e` and every disjoint forbidden extension `F` containing it
satisfy

\[
\boxed{
D_S(e)
\le
\kappa_n
\left(
\mathcal C(S;O,F)
+
\frac{(m+1)b}{n}
\right).
}
\]

### Proof

Otherwise CMR1208 supplies a feasible state below the current minimum. ∎

The two terms distinguish genuine geometric collateral from unavailable-bank
obstruction.

## 5. Exact target-incidence identity

Let `E(S)` be the `2n` distinct physical selected cells of the two-layer saturated
state.

### Theorem CMR1210 -- PROVED

\[
\boxed{
\sum_{e\in E(S)}D_S(e)=3\Phi(S).
}
\]

### Proof

Every physical collinear triple of `S` contains exactly three distinct selected
cells and contributes one incidence to each of them. ∎

Hence one selected cell has target load at least `3m/(2n)`, but the summed form is
more useful for bank weighting.

## 6. Edge-averaged response-bank criterion

For each selected physical cell `e`, choose the layer containing it, keep the
opposite matching fixed, choose a disjoint forbidden extension `F_e`, and let
`b_e` and `mathcal C_e` be the corresponding unavailable count and normalized
collateral score.

### Theorem CMR1211 -- PROVED

If

\[
\boxed{
\sum_{e\in E(S)}
\kappa_n
\left(
\mathcal C_e
+
\frac{(m+1)b_e}{n}
\right)
<
3m,
}
\]

then at least one selected-cell response bank contains a feasible state of
potential below `m`.

### Proof

If every bank failed the CMR1208 criterion, CMR1209 would hold for every selected
cell.  Summing those inequalities and applying CMR1210 would give the reverse weak
inequality. ∎

This is a finite weighted instance of the open CMR1196 target-versus-collateral
inequality.

## 7. Optimize the forbidden extension

Let `mathcal E(e;O)` be the finite family of perfect matchings disjoint from `O`
and containing `e`.  Define

\[
\boxed{
A_H(e)
=
\min_{F\in\mathcal E(e;O)}
\kappa_n
\left(
\mathcal C(S;O,F)
+
\frac{(m+1)b(S;O,F,H)}{n}
\right).
}
\]

### Theorem CMR1212 -- PROVED

If

\[
\boxed{
\sum_{e\in E(S)}A_H(e)<3m,
}
\]

then a feasible strict improvement exists.  Conversely, every positive minimum
satisfies

\[
\boxed{
\sum_{e\in E(S)}A_H(e)\ge3m.
}
\]

### Proof

Choose a minimizing extension for every finite family `mathcal E(e;O)` and apply
CMR1211.  The converse is its contrapositive. ∎

The minimization can be performed exactly in finite base cases and estimated by
averaging over extensions in larger recursive owners.

## 8. Restricted-bank barrier endpoint

### Corollary CMR1213 -- PROVED

Every dirty selected minimum of side `n>=4` reaches one of the following exact
numerical conclusions.

1. One fixed-target degree-two bank satisfies CMR1208 and gives a feasible strict
   improvement.
2. Every target edge satisfies the availability-collateral barrier CMR1209.
3. The optimized global barrier
   \[
   \sum_eA_H(e)\ge3\Phi(S)
   \]
   holds.
4. A fully blocked bank enters the minimal unit-wall descent CMR1150--CMR1157.
5. A structural factor, fixed-core lift, or small-side transition changes the bank
   owner.

This advances the CMR1196 frontier from an unspecified bank weighting to a concrete
finite score.  The remaining task is to upper-bound the optimized scores using
line, prefix, carry, product and fixed-interface structure.

No all-`n` theorem is claimed.  Availability expectations, feasibility forcing,
target-incidence arithmetic, extension optimization and the edge-averaged criterion
are checked in
[`scripts/verify_prime_power_restricted_bank_selection.py`](../scripts/verify_prime_power_restricted_bank_selection.py).
