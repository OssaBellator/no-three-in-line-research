# Integer manifests make the labelled assignment LP independently checkable

CMR1838--CMR1845 formulate the final recurrent numerical search as a finite
rational assignment-dual LP.  This chapter specifies a denominator-cleared
certificate manifest and an exact checker for a completed solution.

The manifest checks arithmetic relative to a declared exact or componentwise
upper coefficient table.  It does not independently reconstruct geometric
ownership, provenance or correction rules; those coefficient tables must be
produced and verified by the corresponding geometric compilers.

Consider one closed recurrent labelled block with state set `I`.  Every state
`i` has positive integer weight `X_i`.  Row `i` has:

- a nonempty response host `G_i` of side `d_i`;
- a positive coefficient denominator `D_i`;
- nonnegative integer edge, pair and triple coefficient numerators for every
  labelled child;
- contracted rank-two and rank-three assignment duals;
- one unified outer assignment dual; and
- a positive integer row slack.

## 1. Exact weighted coefficient aggregation

For child label `j`, let the declared integer coefficient numerators be

\[
c^{(1)}_{ij}(e),
\qquad
c^{(2)}_{ij}(P),
\qquad
c^{(3)}_{ij}(P).
\]

The edge term may already include return, the proved selector cap and rank-one
geometry.  Define the denominator-cleared weighted scores

\[
q_i(e)=\sum_jX_jc^{(1)}_{ij}(e),
\]

\[
b_i(P)=\sum_jX_jc^{(2)}_{ij}(P),
\qquad
t_i(P)=\sum_jX_jc^{(3)}_{ij}(P).
\]

### Theorem CMR1862 -- PROVED

If the declared coefficient table is exact, then for every response matching `Q`,
the denominator-cleared total child Lyapunov weight is

\[
\boxed{
\sum_{e\in Q}q_i(e)
+
\sum_{\substack{P\subseteq Q\\|P|=2}}b_i(P)
+
\sum_{\substack{P\subseteq Q\\|P|=3}}t_i(P).
}
\]

If the table is componentwise upper, the displayed expression is an upper bound.

### Proof

Multiply each labelled coefficient by its fixed integer child weight, sum over
labels, and interchange the finite label and prescription sums.  Positive weights
preserve componentwise domination. ∎

The checker rejects unknown child labels, nonpositive state weights, negative
coefficients, repeated coefficient entries and incompatible prescriptions.

## 2. Extendability-complete manifest surface

Call an edge or ordered pair **extendable** when it occurs in at least one perfect
matching of the declared host.

### Theorem CMR1863 -- PROVED

A self-contained nested-assignment manifest needs:

1. one rank-two contracted dual for every extendable outer edge;
2. one rank-three inner dual for every extendable ordered edge pair;
3. one rank-three middle dual for every extendable outer edge; and
4. one outer dual on the original host.

Nonextendable prescriptions need no nested record because they occur in no
response.  Requiring exact equality with the computed extendable sets prevents
both omitted and extraneous dual records.

### Proof

The peeling identities distinguish one outer edge and, at rank three, one ordered
second edge.  Every such distinguished prescription occurring in a response must
have its contracted assignment bounded.  Conversely a nonextendable prescription
has zero response contribution. ∎

The checker recomputes all perfect matchings of each declared finite host and
verifies this coverage exactly.

## 3. Rank-two inner certificate

For every extendable outer edge `e`, a manifest supplies integer potentials
`alpha^{i,e}`, `beta^{i,e}` on `G_i/e` and an integer upper variable `j_{2,i}(e)`.
It must satisfy

\[
\alpha^{i,e}_u+\beta^{i,e}_v
\ge
b_i(\{e,(u,v)\})
\]

on every residual allowed cell, and

\[
\boxed{
j_{2,i}(e)
\ge
\sum_u\alpha^{i,e}_u+
\sum_v\beta^{i,e}_v.
}
\]

### Theorem CMR1864 -- PROVED

Every accepted rank-two record satisfies

\[
j_{2,i}(e)\ge J_{2,i}(e),
\]

where `J_{2,i}(e)` is the exact contracted assignment maximum for weighted pair
score `b_i`.

### Proof

The displayed vertex inequalities are a feasible assignment dual on `G_i/e`.
Its objective dominates the assignment maximum, and the manifest upper variable
dominates that objective. ∎

Signed dual potentials are allowed; only the inequalities and objective matter.

## 4. Rank-three inner and middle certificates

For every extendable ordered pair `(e,f)`, the inner record supplies a dual on
`G_i/{e,f}` whose cell scores are `t_i({e,f,g})` and whose objective is bounded
above by `j_{3,i}(e,f)`.

For every extendable outer edge `e`, the middle record supplies a dual on `G_i/e`
with residual-edge score `j_{3,i}(e,f)` and objective upper variable `h_{3,i}(e)`.

### Theorem CMR1865 -- PROVED

Every accepted rank-three inner and middle family satisfies

\[
\boxed{h_{3,i}(e)\ge H_{3,i}(e),}
\]

where `H_{3,i}(e)` is the exact two-level contracted objective used by the
rank-three peeling theorem.

### Proof

Each inner dual objective dominates the corresponding final-edge assignment.
The middle dual then dominates the assignment of those inner upper objectives on
`G_i/e`.  Transitivity gives the claim. ∎

## 5. Unified outer row certificate

Define the denominator-cleared sixfold edge score

\[
\Theta_i(e)
=
6q_i(e)+3j_{2,i}(e)+h_{3,i}(e).
\]

The manifest outer potentials satisfy

\[
U_{i,u}+V_{i,v}\ge\Theta_i((u,v))
\]

on every allowed host cell.  With positive integer slack `delta_i`, the required
row objective is

\[
\boxed{
\sum_uU_{i,u}+\sum_vV_{i,v}
\le
6D_iX_i-\delta_i.
}
\]

### Theorem CMR1866 -- PROVED

Every accepted row satisfies

\[
\sum_jA_{ij}X_j<X_i
\]

for the exact expected row `A`, or for every row dominated by the declared
coefficient table.

### Proof

CMR1864--CMR1865 and the rank-two/rank-three peeling factors give a responsewise
upper score of `Theta_i/6`.  The outer potentials form a feasible dual for its
maximum over response matchings.  Divide the strict integer objective by
`6D_i`; the positive slack makes the result strictly below `X_i`. ∎

## 6. Global manifest theorem

### Theorem CMR1867 -- PROVED

Suppose a manifest contains exactly one accepted recurrent row for every declared
state.  Then its positive integer state vector `X` satisfies

\[
\boxed{AX<X.}
\]

Consequently the declared nonnegative recurrent upper matrix has spectral radius
below one.

### Proof

Apply CMR1866 to every row.  A finite nonnegative matrix with a positive strict
supersolution has spectral radius below one. ∎

A block certificate may then enter the already-proved auxiliary resolvent and
reverse-topological CRT assembly.  The manifest does not authorize omission of an
uncertified recurrent row.

## 7. Gauge freedom and portable integer form

Assignment dual potentials have the gauge transformation

\[
U_u\mapsto U_u+c,
\qquad
V_v\mapsto V_v-c.
\]

### Theorem CMR1868 -- PROVED

On every connected assignment host, this transformation preserves all edge
inequalities and the complete dual objective.  On a disconnected host it may be
applied independently on each connected component.

Therefore a publisher may normalize one chosen potential per component to zero
without changing certificate validity.  No such normalization is required by the
checker; arbitrary signed integer potentials are accepted.

### Proof

Every edge sum gains `c-c=0`.  In a balanced bipartite component supporting a
perfect matching, the left and right vertex counts agree, so the complete objective
also gains zero. ∎

## 8. Executable checker endpoint

### Corollary CMR1869 -- PROVED

The final labelled LP now has a publication and verification protocol.

1. Store positive integer state weights and one denominator per row.
2. Store every labelled nonnegative integer edge, pair and triple coefficient.
3. Store complete rank-two, rank-three inner and rank-three middle dual families.
4. Store one unified outer dual and a positive integer row slack.
5. Recompute host perfect matchings and extendability from the manifest itself.
6. Check every prescription, dual-feasibility, objective-upper and strict-row
   inequality using exact integer arithmetic.
7. Accept the manifest only when every declared recurrent state has exactly one
   accepted row.

The standalone checker is
[`scripts/check_label_weighted_assignment_certificate.py`](../scripts/check_label_weighted_assignment_certificate.py).
With no argument it validates a complete built-in example and rejects twelve
independently corrupted variants.  With a JSON path it checks an external
certificate and reports its state, row, coefficient and dual counts.

This closes the format/checker frontier, not the mathematical coefficient frontier.
The remaining task is to populate such a manifest with the true 740-host
background/provenance rows and the surviving reused-support and collision/local-line
states.
