# CRT assembly must retain collision and local-line labels

The current prime-power frontier has exact recurrent modules:

- one scalarized return-selector assignment row;
- strong, singleton and endpoint-overlap line-clean rows with integer slacks;
- finitely concentrated critical selector classes;
- prime-field reused-support and fixed-interface atoms; and
- finite exact thin-side tables.

Strict product, owner, depth, token, edge and first-signature transfers are already
acyclic.  The remaining balanced/CRT task is algebraic only if collision and
local-line interface labels are retained.  Dropping those labels can merge
different transfer paths and create an artificial diagonal cycle.

This chapter gives a label-preserving assembly theorem and an explicit rational
scaling recursion.  Once every genuinely recurrent labelled block has a strict
certificate, all finite CRT interface collateral glues without a new spectral
estimate.

Let `I` be the finite exact state set of one chosen finite quotient.  Every state
retains

\[
\iota=(\omega,\mathbf p,\lambda),
\]

where

- `omega` is the structural/last-entering owner stage;
- `mathbf p` records the active prime-power factor and inherited local state;
- `lambda` records all collision, local-line, fixed-interface and CRT provenance
  needed to determine the next exact row.

Let `A` be the resulting finite nonnegative rational offspring matrix.

## 1. Exact label refinement

Let

\[
\pi:I\to\bar I
\]

forget some interface labels.  For an exact parent state `i`, its offspring row
is a measure on `I`.

### Theorem CMR1622 -- PROVED

Retaining the full label `lambda` preserves exact offspring identities and their
canonical owners.  Projection by `pi` satisfies

\[
\boxed{
\bar c_{i,\bar j}
=
\sum_{j:\pi(j)=\bar j}c_{ij}
}
\]

for every exact row `i` and projected class `bar j`.

A projected matrix is an honest upper quotient only after taking a componentwise
maximum or another proved domination over all exact rows in each projected
parent fibre.  Simply identifying parent rows is not exact in general.

### Proof

The child fibres partition the exact offspring set, giving the displayed sum.
Different exact parent labels may have different response laws and child rows,
so identifying them requires an explicit upper domination. ∎

This is the required bookkeeping rule for CRT collision and local-line labels.

## 2. Labelled transfer graph and recurrent cores

Form a directed graph on `I` with arc `i to j` whenever `A_ij>0`.  Mark as
**strict transfer arcs** all transitions already proved acyclic, including

- later structural owner or wall exits;
- strict child-factor descent;
- earlier-depth handoff;
- first absolute-token, private-edge, restoration-label or support-label use;
- first fixed-interface signature use; and
- strict CRT factor or interface descent supplied by the selected assembly
  policy.

All remaining arcs are retained exactly.

### Theorem CMR1623 -- PROVED

Contract the strongly connected components of the full labelled graph.  Its
condensation graph is a finite DAG.  Every strict transfer arc lies between
components whenever the exact policy executes the corresponding monotone or
structural transition.

After a topological ordering of the components, `A` is block upper triangular.

### Proof

The condensation of every finite directed graph is acyclic.  The listed strict
transitions change one coordinate of the established lexicographic transfer
rank while preserving earlier coordinates, so they cannot lie on a directed
cycle.  Topologically order the components. ∎

The statement does not classify a transition as strict merely because a
structural alternative exists; the chosen row must execute it.

## 3. Spectral reduction with interface labels

Let the diagonal SCC blocks be

\[
D_1,\ldots,D_s.
\]

### Theorem CMR1624 -- PROVED

\[
\boxed{
\rho(A)=\max_{1\le i\le s}\rho(D_i).
}
\]

Thus collision and local-line interface arcs between labelled SCCs do not need
independent contraction estimates.  Only recurrent labelled cores do.

### Proof

A block upper triangular matrix has characteristic polynomial equal to the
product of the characteristic polynomials of its diagonal blocks. ∎

This is the label-preserving CRT specialization of the owner/resource
triangularity established earlier.

## 4. Constructive rational gluing recursion

Assume every recurrent block has a positive rational vector `v_i` and positive
rational slack vector `s_i` satisfying

\[
\boxed{D_i v_i\le v_i-s_i.}
\]

Write `B_ij` for the off-diagonal block from component `i` to later component
`j`.

Process components in reverse topological order.  Suppose positive rational
scales `c_j` have already been chosen for all `j>i`.  Put

\[
w_i=
\sum_{j>i}B_{ij}c_jv_j.
\]

Define

\[
\boxed{
 c_i
>
\max_k\frac{(w_i)_k}{(s_i)_k},
}
\]

with the maximum interpreted as zero when `w_i=0`.

### Theorem CMR1625 -- PROVED

Every reverse-topological choice satisfying the displayed strict inequality
gives a positive rational global vector

\[
\boxed{
v=(c_1v_1,\ldots,c_sv_s)}
\]

with

\[
\boxed{Av<v.}
\]

### Proof

For block row `i`,

\[
(Av)_i
=
D_ic_iv_i+w_i
\le
c_i(v_i-s_i)+w_i
<
c_iv_i
\]

coordinatewise by the choice of `c_i`.  Reverse induction covers all rows. ∎

Arbitrarily large but finite off-diagonal CRT collateral changes only the
rational scales.

## 5. Explicit integer scaling

Suppose all block matrices, local vectors and slacks are rational.  At step `i`,
choose

\[
 c_i=1+
\max_k\frac{(w_i)_k}{(s_i)_k}
\]

or any larger rational number, then clear all denominators at the end.

### Theorem CMR1626 -- PROVED

There is a positive integer vector `V` and positive integer slack vector `S`
such that, after multiplying `A` by one common positive denominator `D`,

\[
\boxed{
(DA)V\le DV-S.
}
\]

Conversely every such integer certificate gives `Av<v` after division by `D`.

### Proof

CMR1625 constructs a rational strict vector.  Multiply by a common denominator
large enough to make the vector and every strict slack integral.  The converse
is immediate. ∎

This is an independently checkable certificate artifact for the final finite
quotient.

## 6. Why labels may not be discarded prematurely

### Theorem CMR1627 -- PROVED

There exist finite labelled DAG quotients whose naive unlabeled identification
creates a self-loop or a directed cycle.  Therefore an unlabeled CRT quotient
may have a larger spectral radius than the exact labelled system unless its rows
are constructed by a proved honest upper-quotient rule.

### Proof

Take two labelled states `a_0,a_1` with one transfer `a_0 to a_1` and no return
arc.  The labelled graph is acyclic.  If both states are identified as one
unlabeled class `a`, the transfer becomes a self-loop.  Larger examples turn two
oppositely oriented transfers between different label fibres into an apparent
two-cycle. ∎

Hence collision and local-line provenance must remain in the state until the
honest domination step.

## 7. Current recurrent block schema

Define the labelled recurrent core to contain only the following exact modules.

1. **Return-selector assignment blocks.**  One combined edge score
   `g_ret+T g_sel` and its rational assignment dual.
2. **Line-clean blocks.**  Strong, singleton or endpoint-overlap rows with exact
   component probabilities or the CMR1590--CMR1597 integer slack.
3. **Critical selector blocks.**  One concentrated rank/profile/geometric class
   from CMR1598--CMR1605.
4. **Reused-support blocks.**  Exact support labels not paid by first use, with
   response reintroduction routed through the return kernel.
5. **Fixed-interface blocks.**  Repeated exact rank-one/rank-two prescriptions
   with rational rook rows.
6. **Thin blocks.**  Exact finite rows from the chosen side cap.
7. **Residual CRT collision/local-line blocks.**  Only states which preserve all
   structural and monotone coordinates and genuinely recur with the same
   interface label.

### Theorem CMR1628 -- PROVED

If every block in this labelled schema has a positive rational strict
certificate, then all strict prime-power transfers, first-use resources, root
channel reductions, balanced-factor transfers and finite CRT interface
collateral glue into one positive rational certificate for the complete finite
quotient.

### Proof

All omitted states and arcs are strict transfer nodes in the labelled
condensation DAG.  Apply CMR1623--CMR1625. ∎

No coefficient may be omitted from a recurrent block unless an earlier theorem
places its chosen transition on a strict arc.

## 8. Label-preserving assembly endpoint

### Corollary CMR1629 -- PROVED

Balanced/CRT assembly now has an exact certificate protocol.

1. retain collision, local-line and factor provenance in every exact state;
2. construct exact rational rows for the recurrent modules listed in CMR1628;
3. contract labelled SCCs and topologically order the condensation DAG;
4. certify every recurrent diagonal block;
5. glue the certificates by the explicit reverse-topological scaling recursion;
6. clear denominators and publish one strict integer certificate.

The remaining mathematical work is numerical rather than structural: obtain
strict certificates for the surviving labelled recurrent blocks.  In
particular, the return assignment dual, line-clean integer slacks, concentrated
critical selector classes and finite fixed-interface/thin tables must be filled
with host-uniform geometric bounds.  No all-`n` theorem is claimed.

Exact label projection, SCC reduction, rational scaling, integer clearing,
artificial-cycle examples and multi-block certificate gluing are checked in
[`scripts/verify_prime_power_label_preserving_crt_assembly.py`](../scripts/verify_prime_power_label_preserving_crt_assembly.py).
