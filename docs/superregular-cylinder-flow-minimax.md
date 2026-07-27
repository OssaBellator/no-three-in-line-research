# Minimax design of cylinder-balanced stationary switching flows

**Branch:** `research/superregular-resampling`

SRR2c--SRR2e identify the exact source of remote-cylinder bias: the reverse column load of a feasible Hall flow. This note gives an exact finite optimization and dual certificate for choosing that flow. It does not prove the required superregular expansion; it converts the remaining probabilistic design problem into min-cost transportation against an adversarial cylinder mixture.

## Switching-flow polytope

Let `Gamma subseteq A x B` be a flaw-removing switching graph satisfying Hall's condition. Write `P(Gamma)` for the nonempty polytope of nonnegative edge weights satisfying

\[
\sum_b w_{ab}=1\quad(a\in A),
\qquad
\sum_a w_{ab}\le1\quad(b\in B).
\]

Put

\[
q_w(b)=\sum_a w_{ab}.
\]

For a nonempty cylinder `C subseteq B`, define its normalized reverse load

\[
g_C(w)=
\frac{|B|}{|A||C|}\sum_{b\in C}q_w(b).
\]

By SRR2c, `g_C(w)` is exactly the ratio between the resampled probability of `C` and the uniform probability of `C` inside `B`.

Let `F` be a finite nonempty family of relevant cylinders and define

\[
\rho^*(\Gamma,F)=
\min_{w\in P(\Gamma)}\max_{C\in F}g_C(w).
\]

## SRR2f -- optimal cylinder-balanced flow exists -- PROVED

The minimum defining `rho*` is attained. If the switching graph and cylinders are finite, an optimal flow may be chosen rational.

### Proof

`P(Gamma)` is a nonempty compact polytope. The maximum of finitely many linear functions `g_C` is continuous, so it attains its minimum. Introducing a variable `rho` and inequalities `g_C(w)<=rho` gives a linear program with rational coefficients; a rational optimal basic feasible solution exists. QED.

## Adversarial cylinder mixtures

For a probability vector `lambda` on `F`, put

\[
c_\lambda(b)=
\frac{|B|}{|A|}
\sum_{C\in F:\,b\in C}
\frac{\lambda_C}{|C|}.
\]

Then

\[
\sum_{C\in F}\lambda_Cg_C(w)
=
\sum_{ab\in\Gamma}c_\lambda(b)w_{ab}.
\]

The right side is a min-cost fractional matching problem with costs depending only on the unflawed endpoint `b`.

## SRR2g -- exact minimax cylinder criterion -- PROVED

\[
\boxed{
\rho^*(\Gamma,F)
=
\max_{\lambda\in\Delta(F)}
\min_{w\in P(\Gamma)}
\sum_{ab\in\Gamma}c_\lambda(b)w_{ab}.
}
\]

Equivalently, `rho*<=rho` if and only if for every probability distribution `lambda` on the relevant cylinders there is a feasible Hall flow whose `c_lambda` transportation cost is at most `rho`.

### Proof

The flow polytope and the cylinder simplex are compact convex sets, and

\[
L(w,\lambda)=\sum_C\lambda_Cg_C(w)
\]

is bilinear. Finite-dimensional minimax gives

\[
\min_w\max_\lambda L(w,\lambda)
=
\max_\lambda\min_w L(w,\lambda).
\]

For fixed `w`, maximizing over the simplex selects a cylinder of maximum load, so the left side is `rho*`. The displayed cost identity gives the right side. The final equivalence is the same equality compared with `rho`. QED.

## SRR2h -- partition lower bound and exact balance -- PROVED

If `F` contains a partition `C_1,...,C_k` of `B`, then every feasible flow obeys

\[
\max_i g_{C_i}(w)\ge1.
\]

Therefore `rho*>=1` for that family. Equality holds whenever a feasible flow has constant reverse load `q_w(b)=|A|/|B|` on `B`.

### Proof

The weighted average of the partition loads is

\[
\sum_i\frac{|C_i|}{|B|}g_{C_i}(w)
=
\frac1{|A|}\sum_{b\in B}q_w(b)=1,
\]

because every flawed row sends total flow one. The maximum is at least the average. Constant reverse load makes every cylinder ratio one. QED.

## Aggregate event families

Let `E` be a multiset of cylinders, allowing repeated geometric events with the same state set. Define the state multiplicity

\[
m_E(b)=|\{C\in E:b\in C\}|.
\]

## SRR2i -- exact aggregate event-load law -- PROVED

For the stationary resampling output `Y` associated with a feasible symmetric flow,

\[
\boxed{
\sum_{C\in E}\Pr(Y\in C)
=
\frac1{|A|}\sum_{b\in B}m_E(b)q_w(b).
}
\]

Consequently the feasible flow minimizing the expected number of events in `E` is exactly a min-cost Hall flow with endpoint cost `m_E(b)`.

### Proof

SRR2c gives

\[
\Pr(Y\in C)=\frac1{|A|}\sum_{b\in C}q_w(b).
\]

Sum over the event multiset and interchange the two finite sums. QED.

## Consequence for SRR2

The remaining construction problem has two exact formulations.

1. For worst-cylinder control, solve the minimax transportation problem of SRR2g.
2. For one declared geometric event inventory, solve the single min-cost Hall flow of SRR2i.

Thus forward-switch counting should be organized to prove either low transportation cost for every adversarial cylinder mixture or low endpoint cost for the actual event multiset. Hall feasibility alone remains insufficient.

## Finite check

`scripts/verify_superregular_cylinder_flow_minimax.py` enumerates all tiny switching graphs with up to two flawed and three unflawed states that admit a saturating matching. It represents the Hall-flow polytope as the convex hull of saturating matchings, solves the finite zero-sum cylinder game exactly with rational support enumeration, checks the partition lower bound and verifies the aggregate event-load identity.
