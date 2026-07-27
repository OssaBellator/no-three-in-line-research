# Label-weighted nested assignments form one finite Lyapunov LP

CMR1822--CMR1829 combine return, bounded-selector and geometric collateral into
one outer edge score after the rank-two and rank-three terms are peeled through
contracted assignments.  The remaining quotient is labelled: every child keeps
its owner, collision, local-line, root, thin, interface and CRT provenance.

This chapter inserts proposed Lyapunov weights before every peeling step.  For
fixed finite labelled state data, all local conditions

\[
Ax<x
\]

become one finite system of rational linear assignment-dual inequalities.  The
system certifies the exact or componentwise upper offspring table supplied to it;
it does not claim that a peeled upper table is always sharp.

Let `I` be a finite parent/child state set.  For parent `i`, let `G_i` be its
nonempty bipartite response host and let `T_i` be its proved selector restoration
cap.  For child label `j`, let

- `r_{ij}(e)` and `s_{ij}(e)` be return and selector edge coefficients;
- `c^{(1)}_{ij}(e)` be the rank-one coefficient;
- `c^{(2)}_{ij}(P)` be the rank-two coefficient on compatible pairs; and
- `c^{(3)}_{ij}(P)` be the rank-three coefficient on compatible triples.

All coefficients are nonnegative rational numbers and retain every provenance
label needed by future rows.

## 1. Label linearization

For proposed child weights `x_j>0`, define

\[
q_i(e;x)
=
\sum_{j\in I}x_j
\left[r_{ij}(e)+T_i s_{ij}(e)+c^{(1)}_{ij}(e)\right],
\]

\[
b_i(P;x)=\sum_{j\in I}x_jc^{(2)}_{ij}(P),
\qquad
 t_i(P;x)=\sum_{j\in I}x_jc^{(3)}_{ij}(P).
\]

### Theorem CMR1838 -- PROVED

For every response matching `Q`,

\[
\boxed{
\sum_{j\in I}x_jN_{ij}(Q)
=
\sum_{e\in Q}q_i(e;x)
+
\sum_{\substack{P\subseteq Q\\|P|=2}}b_i(P;x)
+
\sum_{\substack{P\subseteq Q\\|P|=3}}t_i(P;x)
}
\]

when the primitive coefficients are exact.  For componentwise upper coefficients,
the equality becomes `<=`.

### Proof

Expand by child label and interchange the finite label sum with the edge, pair and
triple prescription sums.  Positive weighting preserves componentwise domination.
∎

No provenance label is merged; it is evaluated against the candidate Lyapunov
vector.

## 2. Weighted nested peeling

For an extendable outer edge `e`, define

\[
J_{2,i}(e;x)
=
\mathcal A_{G_i/e}
\bigl(f\mapsto b_i(\{e,f\};x)\bigr).
\]

For an extendable ordered pair `(e,f)`, define

\[
J_{3,i}(e,f;x)
=
\mathcal A_{G_i/\{e,f\}}
\bigl(g\mapsto t_i(\{e,f,g\};x)\bigr),
\]

and

\[
H_{3,i}(e;x)
=
\mathcal A_{G_i/e}
\bigl(f\mapsto J_{3,i}(e,f;x)\bigr).
\]

Nonextendable prescriptions have zero response contribution.

### Theorem CMR1839 -- PROVED

Every response matching satisfies

\[
\boxed{
\sum_{j\in I}x_jN_{ij}(Q)
\le
\sum_{e\in Q}
\left[q_i(e;x)+\frac12J_{2,i}(e;x)+\frac16H_{3,i}(e;x)\right].
}
\]

### Proof

Apply CMR1838 and then CMR1791--CMR1792 to the weighted nonnegative pair and
triple scores. ∎

The same child weights are used at every contraction level.

## 3. One weighted outer score

Define

\[
\gamma_i(e;x)
=
q_i(e;x)+\frac12J_{2,i}(e;x)+\frac16H_{3,i}(e;x).
\]

### Theorem CMR1840 -- PROVED

For every response law on `G_i`,

\[
\boxed{
\sum_{j\in I}A_{ij}x_j
\le
\mathcal A_{G_i}(\gamma_i(.;x)).
}
\]

### Proof

CMR1839 holds responsewise.  Maximize its right side over response matchings and
then take expectation. ∎

Return, selector and all three geometric ranks remain coupled to the same outer
matching.

## 4. Row Lyapunov criterion

### Theorem CMR1841 -- PROVED

Suppose there is a positive vector `x` and positive rational slacks `epsilon_i`
such that every recurrent parent satisfies

\[
\boxed{
\mathcal A_{G_i}(\gamma_i(.;x))
\le x_i-\epsilon_i.
}
\]

Then

\[
\boxed{Ax<x}
\]

on those recurrent rows, and the certified nonnegative upper matrix has spectral
radius below one.

### Proof

CMR1840 gives `(Ax)_i<=A_{G_i}(gamma_i)<x_i`.  A finite nonnegative matrix with a
positive strict supersolution has spectral radius below one. ∎

## 5. Explicit simultaneous rational dual LP

Every assignment maximum above has an ordinary bipartite dual.  All dual
potentials below may be unrestricted rational variables.

### Rank-two inner constraints

For every parent `i` and extendable outer edge `e`, introduce dual potentials
`alpha^{i,e}_u,beta^{i,e}_v` on `G_i/e` and an objective upper variable
`j_{2,i}(e)`.  Require

\[
\alpha^{i,e}_u+\beta^{i,e}_v
\ge
b_i(\{e,(u,v)\};x)
\]

on every residual cell, and

\[
\boxed{
j_{2,i}(e)
\ge
\sum_u\alpha^{i,e}_u+
\sum_v\beta^{i,e}_v.
}
\]

The feasible dual objective dominates `J_{2,i}(e;x)`, so `j_{2,i}(e)` does also.

### Rank-three inner and middle constraints

For every extendable ordered pair `(e,f)`, introduce dual potentials on
`G_i/{e,f}` and an upper variable `j_{3,i}(e,f)` satisfying

\[
\text{inner potentials dominate }t_i(\{e,f,g\};x)
\]

on every remaining cell, and

\[
\boxed{
j_{3,i}(e,f)
\ge
\text{their complete dual objective sum}.
}
\]

For each outer edge `e`, introduce middle dual potentials
`mu^{i,e}_u,nu^{i,e}_v` on `G_i/e` satisfying

\[
\mu^{i,e}_u+\nu^{i,e}_v
\ge
j_{3,i}(e,(u,v))
\]

on every extendable residual cell, and an upper variable `h_{3,i}(e)` with

\[
\boxed{
h_{3,i}(e)
\ge
\sum_u\mu^{i,e}_u+
\sum_v\nu^{i,e}_v.
}
\]

Thus `h_{3,i}(e)` dominates `H_{3,i}(e;x)`.

### Outer constraints

Define the sixfold edge score

\[
\Theta_i(e;x)
=
6q_i(e;x)+3j_{2,i}(e)+h_{3,i}(e).
\]

Introduce outer potentials `U_{i,u},V_{i,v}` with

\[
U_{i,u}+V_{i,v}
\ge
\Theta_i((u,v);x)
\]

on every allowed cell and require

\[
\boxed{
\sum_uU_{i,u}+\sum_vV_{i,v}
\le
6x_i-6\epsilon_i.
}
\]

Use one normalization such as

\[
\sum_{i\in I}x_i=1,
\qquad x_i>0,
\qquad\epsilon_i>0.
\]

### Theorem CMR1842 -- PROVED

All displayed inner, middle and outer constraints form a finite rational linear
feasibility problem.  Every feasible solution certifies `Ax<x`.

### Proof

The primitive weighted scores are linear in `x`.  Every dual feasibility and
objective-upper constraint is linear.  The rank-two variables dominate `J_2`, the
rank-three variables dominate `H_3`, and the outer dual dominates six times the
score in CMR1840.  Its strict objective inequality gives CMR1841.  The state,
host and contraction sets are finite. ∎

No eigenvalue, unknown product or floating-point approximation appears in the
certificate system.

## 6. Rational and integer certificates

### Theorem CMR1843 -- PROVED

Assume all primitive coefficients and selector caps are rational.

1. If the strict system of CMR1842 has a real feasible point, it has a rational
   feasible point with positive slacks.
2. Every rational feasible point can be multiplied by one common denominator to
   produce a finite signed-integer assignment-dual certificate.
3. After one further positive integer scaling, every strict row slack may be made
   at least one:
   
   \[
   \boxed{
   \sum_u\mathsf U_{i,u}+\sum_v\mathsf V_{i,v}
   \le
   6\mathsf X_i-1.
   }
   \]

### Proof

With a normalization, the system is a rational polyhedron and the positive slack
conditions place a feasible point in a relative open face.  Rational points are
dense there.  Clear every coefficient, weight and dual denominator.  Positive
rational slacks become positive integers after scaling. ∎

Every edge constraint and objective inequality is independently checkable by
exact integer arithmetic.

## 7. SCC and auxiliary assembly

### Theorem CMR1844 -- PROVED

Apply the LP only after exact structural reductions:

1. retain every owner, collision, local-line, interface and CRT label;
2. contract exact structural SCCs;
3. eliminate already-certified auxiliary modules through CMR1694--CMR1701;
4. solve the weighted assignment LP on every surviving recurrent block;
5. use CMR1625 reverse-topological scaling to absorb finite off-diagonal
   transfers.

If every surviving recurrent block has a strict LP certificate, the complete
labelled offspring matrix has one global strict integer Lyapunov certificate.

### Proof

CMR1842--CMR1843 certify the recurrent diagonal blocks.  Exact resolvents preserve
subcriticality and provide effective core rows.  CMR1625 glues the strict block
certificates across the finite condensation DAG. ∎

The LP does not authorize premature label merging or elimination of an
uncertified auxiliary block.

## 8. Label-weighted LP endpoint

### Corollary CMR1845 -- PROVED

The final numerical search now has a finite exact formulation.

1. Choose positive weights for every surviving labelled recurrent state.
2. Aggregate all child labels before peeling.
3. Certify every contracted pair and triple objective by explicit dual
   potentials and objective upper variables.
4. Add return, bounded selector and rank-one scores to the same outer edge score.
5. Require one strict outer objective below the parent weight in every row.
6. Clear denominators and publish the integer state weights, all inner/middle/
   outer duals and every row slack.

Failure of this LP is not proof that the original row is supercritical: peeled or
componentwise upper coefficients may be coarse.  Failure identifies the exact
parent, outer edge class or contracted inner class requiring sharper geometry.

No all-`n` conclusion is claimed.  The remaining work is to populate the finite
LP with the actual background, owner and provenance coefficients on the 740 raw
side-four/five hosts and on the surviving reused-support and collision/local-line
states.

Label aggregation, responsewise nested bounds, feasible rational duals and exact
denominator clearing are checked in
[`scripts/verify_prime_power_label_weighted_unified_assignment_lp.py`](../scripts/verify_prime_power_label_weighted_unified_assignment_lp.py).
