# Label-weighted nested assignments form one finite Lyapunov LP

CMR1822--CMR1829 combine return, bounded-selector and geometric collateral into
one outer edge score after the rank-two and rank-three terms are peeled through
contracted assignments.  The remaining final quotient is labelled: a child keeps
its owner, collision, local-line, root, thin, interface and CRT provenance.

This chapter shows that proposed Lyapunov weights may be inserted before every
peeling step.  For fixed finite labelled state data, all local conditions

\[
Ax<x
\]

become one finite system of rational linear assignment-dual inequalities.  The
construction is sufficient for the exact or componentwise upper offspring table
being certified; it does not claim that the peeled upper table is always sharp.

Let `I` be a finite parent/child state set.  For parent `i`, let `G_i` be its
nonempty bipartite response host and let `T_i` be its proved selector restoration
cap.  For child label `j`, let

- `r_{ij}(e)` and `s_{ij}(e)` be return and selector edge coefficients;
- `c^{(1)}_{ij}(e)` be the rank-one geometric coefficient;
- `c^{(2)}_{ij}(P)` be the rank-two coefficient on compatible pairs; and
- `c^{(3)}_{ij}(P)` be the rank-three coefficient on compatible triples.

All coefficients are nonnegative rational numbers and retain every provenance
label needed by future rows.

## 1. Label linearization

Let `x_j>0` be proposed child Lyapunov weights.  Define the weighted primitive
scores

\[
q_i(e;x)
=
\sum_{j\in I}x_j
\left[
 r_{ij}(e)+T_i s_{ij}(e)+c^{(1)}_{ij}(e)
\right],
\]

\[
b_i(P;x)=\sum_{j\in I}x_jc^{(2)}_{ij}(P),
\]

and

\[
t_i(P;x)=\sum_{j\in I}x_jc^{(3)}_{ij}(P).
\]

### Theorem CMR1838 -- PROVED

For every response matching `Q`, its total child Lyapunov weight is exactly the
sum of the three aggregated primitive ranks:

\[
\boxed{
\sum_{j\in I}x_jN_{ij}(Q)
=
\sum_{e\in Q}q_i(e;x)
+
\sum_{\substack{P\subseteq Q\\|P|=2}}b_i(P;x)
+
\sum_{\substack{P\subseteq Q\\|P|=3}}t_i(P;x),
}
\]

whenever the displayed coefficients are the exact labelled offspring counts.  If
they are componentwise upper coefficients, the equality becomes `<=`.

### Proof

Expand the left side by child label and interchange the finite sum over labels
with the finite sums over edge, pair and triple prescriptions.  Componentwise
upper rows remain upper after multiplication by positive weights and summation. ∎

Thus provenance labels are not discarded; they are evaluated against the current
candidate Lyapunov vector.

## 2. Weighted nested peeling

For every allowed outer edge `e`, define

\[
J_{2,i}(e;x)
=
\mathcal A_{G_i/e}
\bigl(f\mapsto b_i(\{e,f\};x)\bigr).
\]

For compatible ordered pairs `(e,f)`, define

\[
J_{3,i}(e,f;x)
=
\mathcal A_{G_i/\{e,f\}}
\bigl(g\mapsto t_i(\{e,f,g\};x)\bigr),
\]

and then

\[
H_{3,i}(e;x)
=
\mathcal A_{G_i/e}
\bigl(f\mapsto J_{3,i}(e,f;x)\bigr).
\]

Only extendable prescriptions are retained; nonextendable prescriptions have
zero response contribution.

### Theorem CMR1839 -- PROVED

Every response matching satisfies

\[
\boxed{
\sum_{j\in I}x_jN_{ij}(Q)
\le
\sum_{e\in Q}
\left[
 q_i(e;x)
 +\frac12J_{2,i}(e;x)
 +\frac16H_{3,i}(e;x)
\right].
}
\]

### Proof

Apply CMR1838, then the rank-two and rank-three peeling bounds CMR1791--CMR1792
to the weighted nonnegative scores `b_i(.;x)` and `t_i(.;x)`. ∎

The same child weights are used at every contraction level.

## 3. One weighted outer score

Define

\[
\gamma_i(e;x)
=
q_i(e;x)
+\frac12J_{2,i}(e;x)
+\frac16H_{3,i}(e;x).
\]

### Theorem CMR1840 -- PROVED

For any probability law on the response matchings of `G_i`,

\[
\boxed{
\sum_{j\in I}A_{ij}x_j
\le
\mathcal A_{G_i}(\gamma_i(.;x)),
}
\]

where `A_{ij}` is the exact expected labelled offspring row or any row dominated
by the primitive coefficients.

### Proof

CMR1839 holds responsewise.  Maximize its right side over response matchings and
then take expectation. ∎

Return, selector and all three geometric ranks remain coupled to the same outer
response matching.

## 4. Row Lyapunov criterion

### Theorem CMR1841 -- PROVED

Suppose there is a positive vector `x` and positive rational slacks `epsilon_i`
such that for every recurrent parent `i`,

\[
\boxed{
\mathcal A_{G_i}(\gamma_i(.;x))
\le
x_i-\epsilon_i.
}
\]

Then

\[
\boxed{Ax<x}
\]

componentwise on those recurrent rows.  In particular the certified nonnegative
upper matrix has spectral radius below one.

### Proof

CMR1840 gives

\[
(Ax)_i\le\mathcal A_{G_i}(\gamma_i(.;x))<x_i.
\]

A positive strict supersolution for a finite nonnegative matrix implies spectral
radius below one. ∎

This is the labelled version of the scalar recurrent test `L_T<1`.

## 5. Simultaneous rational dual LP

Every assignment maximum in CMR1839 has an ordinary bipartite dual.  Introduce
the following rational variables for every parent row.

1. For each outer edge `e`, inner rank-two dual potentials on `G_i/e` and an
   objective upper variable `j_{2,i}(e)`.
2. For each extendable ordered pair `(e,f)`, inner rank-three dual potentials on
   `G_i/{e,f}` and an objective upper variable `j_{3,i}(e,f)`.
3. For each outer edge `e`, middle rank-three dual potentials on `G_i/e` and an
   objective upper variable `h_{3,i}(e)`.
4. Outer dual potentials `U_{i,u},V_{i,v}` on `G_i`.
5. Positive state weights `x_i` and slacks `epsilon_i`.

The inner dual constraints require their vertex-potential sums to dominate the
weighted pair or triple scores.  Their objective sums dominate `j_2`, `j_3` and
`h_3`.  At the outer level use the sixfold score

\[
\Theta_i(e;x)
=
6q_i(e;x)+3j_{2,i}(e)+h_{3,i}(e).
\]

### Theorem CMR1842 -- PROVED

The following conditions form a finite rational linear feasibility problem:

\[
U_{i,u}+V_{i,v}\ge\Theta_i((u,v);x)
\]

on every allowed outer cell, together with

\[
\boxed{
\sum_uU_{i,u}+\sum_vV_{i,v}
\le
6x_i-6\epsilon_i
}
\]

for every recurrent parent, all inner dual constraints, and one normalization
such as

\[
\sum_{i\in I}x_i=1.
\]

Every feasible solution certifies `Ax<x`.

### Proof

All weighted primitive scores are linear in `x`.  Assignment-dual feasibility and
objective inequalities are linear in their potential variables.  The inner dual
objectives dominate `J_2` and `H_3`; the outer dual therefore dominates six times
the outer score in CMR1840.  The strict slack inequality gives CMR1841.  There are
only finitely many states, hosts, contractions and allowed cells. ∎

No eigenvalue, product of unknowns or floating-point approximation appears in the
certificate system.

## 6. Rational and integer certificates

### Theorem CMR1843 -- PROVED

Assume all primitive coefficients and selector caps are rational.

1. If the strict dual system of CMR1842 has a real feasible point, it has a
   rational feasible point with positive slacks.
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

The feasible set with fixed positive slack margins is a rational polyhedron.
Rational points are dense in its relative interior.  Clear all coefficient,
weight and dual denominators.  Strict positive rational slacks become positive
integers; scale once more if necessary. ∎

Assignment dual potentials may be signed integers.  Their displayed edge and
objective inequalities are independently checkable by exact arithmetic.

## 7. SCC and auxiliary assembly

### Theorem CMR1844 -- PROVED

Apply the LP only to genuinely recurrent labelled states after the following
exact reductions.

1. Contract structural strongly connected components while preserving every
   owner, collision, local-line, interface and CRT label.
2. Eliminate already-certified auxiliary modules through the rational resolvent
   of CMR1694--CMR1701.
3. Solve the weighted assignment LP on each surviving recurrent block.
4. Use the reverse-topological scaling of CMR1625 to absorb all finite
   off-diagonal transfers.

If every surviving recurrent block has a strict LP certificate, the complete
labelled offspring matrix has one global strict integer Lyapunov certificate.

### Proof

CMR1842--CMR1843 certify each recurrent diagonal block.  The resolvent reduction
preserves subcriticality and supplies exact effective core rows.  CMR1625 glues
strict block certificates across the finite condensation DAG. ∎

The LP does not authorize premature label merging or elimination of an
uncertified auxiliary block.

## 8. Label-weighted LP endpoint

### Corollary CMR1845 -- PROVED

The final numerical search has a finite exact formulation.

1. Choose positive weights for every surviving labelled recurrent state.
2. Aggregate all child labels against those weights before peeling.
3. Certify contracted rank-two and rank-three objectives by assignment duals.
4. Add return, bounded selector and rank-one scores to the same outer edge score.
5. Require one strict outer dual objective below the parent weight in every row.
6. Clear denominators and publish the integer weights, every inner and outer dual,
   and every row slack.

Failure of this LP is not a proof that the original row is supercritical, because
the peeled or componentwise upper coefficients may be coarse.  It identifies the
specific parent, outer edge class or contracted inner class requiring a sharper
geometric row.

No all-`n` conclusion is claimed.  The remaining work is to populate the finite
LP with the actual background, owner and provenance coefficients on the 740 raw
side-four/five hosts and on the surviving reused-support and collision/local-line
states.

Label aggregation, responsewise nested bounds, feasible rational duals and exact
denominator clearing are checked in
[`scripts/verify_prime_power_label_weighted_unified_assignment_lp.py`](../scripts/verify_prime_power_label_weighted_unified_assignment_lp.py).
