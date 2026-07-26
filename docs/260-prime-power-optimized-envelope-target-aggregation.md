# Optimized local envelopes aggregate against exact target incidence

CMR1238--CMR1245 give a pointwise collateral envelope for one fixed-target bank.
This chapter minimizes that envelope over disjoint forbidden extensions and sums it
across the `2n` selected target cells.  The exact incidence identity

\[
\sum_{e\in E(S)}D_S(e)=3\Phi(S)
\]

then forces one quantitative local line or star certificate whenever no response
improves and no bank is completely blocked.

Fix a selected minimum state `S` of side `n>=4` in a current restricted host.  For
each selected physical cell `e`, let `O_e` be the opposite-layer matching and let

\[
\mathcal E(e;O_e)
=
\{F:F\text{ is a perfect matching},\ e\in F,\ F\cap O_e=\varnothing\}.
\]

For `F in mathcal E(e;O_e)`, write `G_{e,F}` for the degree-two response graph and
`mathcal R_Lambda(e,F)` for the CMR1241 full-collateral envelope bound.

Call `F` **host-feasible** when the current rematched-layer host contains at least
one perfect matching of `G_{e,F}`.

## 1. Every target edge has a finite extension decision

### Theorem CMR1246 -- PROVED

For each selected physical cell `e`, exactly one of the following holds.

1. At least one extension in `mathcal E(e;O_e)` is host-feasible.
2. Every extension bank is completely blocked; choosing any extension gives a
   missing-edge cover and the minimal deficiency-one unit-wall descent.

### Proof

The extension family is finite and nonempty by CMR1198.  Either one member has a
feasible response matching or none does.  In the latter case apply CMR1160 and
CMR1150--CMR1157 to any complete degree-two bank. ∎

Thus failure of extension feasibility is already strict structural descent.

## 2. Best feasible collateral envelope

In the first branch of CMR1246 define

\[
\boxed{
\beta_H(e)
=
\min_{F\in\mathcal E(e;O_e)\,\text{host-feasible}}
\mathcal R_\Lambda(e,F).
}
\]

### Theorem CMR1247 -- PROVED

If

\[
\boxed{\beta_H(e)<D_S(e),}
\]

then the current host contains a strict-improvement response destroying every old
target through `e`.

### Proof

Choose a minimizing host-feasible extension.  CMR1242 says every response in its
complete bank has new collateral at most `beta_H(e)` and destroys at least
`D_S(e)`.  At least one response is feasible, so that response improves. ∎

At a positive minimum with no wall descent, every selected cell satisfies the
reverse weak inequality.

## 3. Global optimized-envelope barrier

### Theorem CMR1248 -- PROVED

Suppose no selected-cell extension bank is completely blocked and no feasible
fixed-target response improves the current minimum.  Then

\[
\boxed{
\sum_{e\in E(S)}\beta_H(e)
\ge
3\Phi(S).
}
\]

### Proof

CMR1247 gives `beta_H(e)>=D_S(e)` for every selected cell.  Sum and apply the exact
target-incidence identity CMR1210. ∎

This is a concrete instance of the weighted bank barrier CMR1196 with unit weights
on selected cells and optimized internal extension choices.

## 4. One target edge has a large optimized envelope

### Theorem CMR1249 -- PROVED

Under the hypotheses of CMR1248, some selected physical target cell `e_*` satisfies

\[
\boxed{
\beta_H(e_*)
\ge
\frac{3\Phi(S)}{2n}.
}
\]

For a minimizing feasible extension `F_*`, some allowed response edge `a_*` then
satisfies

\[
\boxed{
\Lambda_S(a_*)
\ge
\frac{3\Phi(S)}{2n^2}.
}
\]

### Proof

There are `2n` selected physical cells, so the first bound is averaging in CMR1248.
The row/column definition of `mathcal R_Lambda` has `n` maxima, each at most the
global maximum `Lambda` value.  Hence

\[
\max_a\Lambda_S(a)
\ge
\mathcal R_\Lambda(e_*,F_*)/n
=
\beta_H(e_*)/n.
\]

Combine the bounds. ∎

The edge `a_*` is an absolute last-entering collateral owner in the sense of
CMR1214--CMR1221.

## 5. One collateral rank is quantitatively large

### Theorem CMR1250 -- PROVED

For the edge `a_*` of CMR1249, at least one of the following holds.

1. **Rank one:**
   \[
   \boxed{
   w_S(a_*)
   \ge
   \frac{\Phi(S)}{2n^2}.
   }
   \]
2. **Rank two:**
   \[
   \boxed{
   \Delta_2(a_*)
   \ge
   \frac{\Phi(S)}{n^2}.
   }
   \]
3. **Rank three:**
   \[
   \boxed{
   \Delta_3(a_*)
   \ge
   \frac{3\Phi(S)}{2n^2}.
   }
   \]

### Proof

The three nonnegative terms

\[
w_S(a_*),
\qquad
\Delta_2(a_*)/2,
\qquad
\Delta_3(a_*)/3
\]

sum to `Lambda_S(a_*)`.  One is at least one third of the CMR1249 lower bound.
Rearrange in the three cases. ∎

Thus a persistent positive minimum produces a quantitative local geometric
certificate rather than diffuse collateral.

## 6. Explicit line and star consequences

Fix an integer threshold `s>=2`.

### Corollary CMR1251 -- PROVED

The alternatives of CMR1250 yield at least one of:

1. a loaded opposite-layer line through `a_*` or at least
   \[
   \left\lceil
   \frac{\Phi(S)}{2n^2\binom s2}
   \right\rceil
   \]
   distinct opposite-layer secant lines through `a_*`;
2. an opposite-layer line through `a_*` containing at least
   \[
   \left\lceil
   \frac{\Phi(S)}{n^2(n-1)}
   \right\rceil
   \]
   selected cells;
3. in a response matching attaining `Delta_3(a_*)`, one line through `a_*` with
   at least `s+1` other response cells, or at least
   \[
   \left\lceil
   \frac{3\Phi(S)}{2n^2\binom s2}
   \right\rceil
   \]
   distinct rooted response secant lines.

### Proof

Apply CMR1236 to branch one and CMR1244 to branches two and three, substituting the
CMR1250 lower bounds. ∎

Ceilings below one are interpreted as the qualitative existence already supplied
by positive local load.

## 7. Averaging over extension laws

For every selected cell `e`, let `nu_e` be any probability distribution supported
on its host-feasible extension family.

### Theorem CMR1252 -- PROVED

If

\[
\boxed{
\sum_{e\in E(S)}
\mathbb E_{F\sim\nu_e}
\mathcal R_\Lambda(e,F)
<
3\Phi(S),
}
\]

then some feasible extension bank contains a strict-improvement response.

### Proof

If every feasible extension satisfied
`mathcal R_Lambda(e,F)>=D_S(e)`, then averaging over `nu_e`, summing over `e`, and
using CMR1210 would give the reverse weak inequality.  Hence one extension has
`mathcal R_Lambda<D_S(e)`, and CMR1242 applies. ∎

This form permits random forbidden extensions, height classes or product-weighted
extension laws without first identifying the minimizing extension.

## 8. Optimized aggregation endpoint

### Corollary CMR1253 -- PROVED

Every dirty selected minimum of side `n>=4` reaches at least one of:

1. a feasible fixed-target response of strictly smaller potential;
2. a completely blocked degree-two bank and exact unit-wall descent;
3. the global optimized barrier `sum_e beta_H(e)>=3Phi(S)`;
4. one absolute entering edge with local envelope at least
   `3Phi(S)/(2n^2)`;
5. a quantitative rank-one, rank-two or rank-three loaded-line/secant-star
   certificate from CMR1250--CMR1251.

The remaining CMR1196 work is now sharply quantitative: show that the line, height,
carry, product or CRT budgets make the averaged envelope in CMR1252 smaller than
`3Phi(S)`, or absorb the concentrated certificates of CMR1251.

No all-`n` theorem is claimed.  Optimized extension arithmetic, target-incidence
aggregation, local-envelope concentration, rank splitting and extension-law
averaging are checked in
[`scripts/verify_prime_power_optimized_envelope_aggregation.py`](../scripts/verify_prime_power_optimized_envelope_aggregation.py).
