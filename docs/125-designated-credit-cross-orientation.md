# Designated-credit cross orientation

The signed Ramsey theorem PP3pj treats the two rectangle states symmetrically.
In the recapture branch they are not symmetric.  State zero is the diagonal on
the designated obstruction line, while state one is the opposite rectangle
diagonal.  The cross diagonal lies off that line and therefore cannot directly
recreate the designated unary blocker incidence.

This chapter isolates that preferred orientation and reduces its failure to a
signed cross-conflict core or residual paid collateral.

## 1. Owner credit carried by a rectangle

Use the designated resource data of PP3jo:

\[
 (z_i,e_i,\{r_i,s_i\}),
\]

where \(r_i=(x_i,y_i)\) is the removed endpoint and the designated recapture
line is

\[
 L_i=\overline{z_is_i}.
\]

A common-line rectangle associated with owner \(i\) has state-zero diagonal

\[
 D_s^0=\{p_s,t_s\}\subseteq L_i
\]

and cross diagonal

\[
 D_s^1=\{p_s^*,t_s^*\}.
\]

### Proposition PP3pm -- PROVED

Neither cell of \(D_s^1\) lies on the designated line \(L_i\).  Consequently,
selecting state one does not directly reinsert the designated incidence through
the unchanged blocker endpoint \(s_i\).

#### Proof

This is PP3oh: the opposite rectangle diagonal lies off the nonaxis line
containing \(p_s,t_s\).  Proposition PP3jp says that direct recreation through
\(s_i\) occurs exactly when the replacement cell in the old column of \(r_i\)
lies on \(L_i\).  The state-one cell in that column does not. ∎

Other inserted pairs may still block \(z_i\); those contributions remain in the
residual unary or binary insertion-shadow cost.

### Proposition PP3pn -- PROVED

Let \(H\) be a resource-disjoint rectangle subbank whose owner indices are
distinct.  Assume every selected rectangle state is supported on off-diagonal
endpoint cells, so every owner endpoint \(r_i\) is moved.  Then the old source
pairs associated with the owners in \(H\) supply at least

\[
 R_H\ge |H|
\]

units of removal credit.

If every rectangle in \(H\) is put in state one, none of these \(|H|\)
designated units is directly recaptured through its unchanged endpoint \(s_i\).

#### Proof

Distinct owner indices come from the resource-disjoint extraction PP3ok.  For
each owner, the selected bad controller entry contributes one unit to the old
pair \(\{r_i,s_i\}\).  Since \(r_i\) is moved, that unit occurs in the removal
credit, exactly as in PP3ic.  Proposition PP3pm gives the final assertion. ∎

The inequality is a lower bound; moving the same endpoints may destroy further
shadow incidences.

## 2. Cross-conflict graph

After PP3pc unit preprocessing, let \(H\) be a ternary-free flexible rectangle
bank.  Form the **cross-conflict graph** \(G_\times\) on its variables by joining
\(s,t\) when the binary signature contains

\[
 (1,1).
\]

Thus an edge means that selecting the cross diagonal in both rectangles creates
at least one geometric bad box.

### Proposition PP3po -- PROVED FROM THE TWO-COLOUR RAMSEY THEOREM

Every growing ternary-free rectangle bank contains a growing subset \(J\) of
one of the following two forms.

1. **Cross-compatible set:** \(J\) is independent in \(G_\times\).
2. **Cross-conflict clique:** every pair of variables in \(J\) is adjacent in
   \(G_\times\).

#### Proof

Colour each variable pair by adjacency or nonadjacency in \(G_\times\).  The
fixed-colour Ramsey bound gives a monochromatic clique of size
\(\Omega(\log |H|)\), which tends to infinity with \(|H|\). ∎

This is the preferred-orientation version of PP3pi.  It does not claim that the
cross-conflict clique is unsatisfiable under mixed orientations.

## 3. Source-valid all-cross completion

### Theorem PP3pp -- PROVED

Let \(J\) be a cross-compatible set supplied by PP3po.  Suppose unit clauses
and ternary clauses have been removed as above.  Then assigning

\[
 X_s=1
 \qquad(s\in J)
\]

avoids every geometric clause on the rectangle subbank.

#### Proof

There are no unit or ternary bad boxes.  A binary bad box selected by the
all-cross assignment would have state pair \((1,1)\), which would make its two
variables adjacent in \(G_\times\).  Independence excludes this. ∎

Together with a source-valid residual matching from PP3ov, the resulting
complete endpoint state is source-admissible.

## 4. Paid cross-orientation criterion

Let \(C_\times(J)\) denote the exact insertion-shadow cost of the all-cross
state on \(J\), including the fixed residual contribution allocated to the
constant and unary state tables.  Let \(R_H\) be the exact removal credit of the
endpoints moved by the installed trade.

### Corollary PP3pq -- PROVED

If \(J\) is cross-compatible and

\[
 C_\times(J)<R_H,
\]

then the installed rectangle trade is source-admissible and strictly decreases
the paid potential.

It is sufficient to verify

\[
 C_\times(J)<|J|
\]

when the only credited endpoints being used are the distinct designated owners
of PP3pn.

#### Proof

Geometric validity is PP3pp.  Apply the exact potential identity PP3oo and the
credit lower bound PP3pn. ∎

The all-cross state has zero direct designated-recapture cost for its own owner
units.  Its remaining cost consists of residual-source blockers, interactions
with the fixed residual matching, and cross-rectangle binary shadow.

## 5. Revised preferred-orientation endpoint

### Corollary PP3pr -- PROVED

The common-line rectangle conversion has the following preferred-orientation
alternatives after adaptive source preparation.

1. A growing cross-compatible subbank has all-cross insertion cost below its
   removal credit, giving a strict improvement.
2. Every growing Ramsey subbank contains a growing cross-conflict clique.
3. Cross-compatible subbanks exist, but their residual all-cross insertion cost
   is at least their removal credit.
4. Unit preprocessing forbids or forces the cross state on a linear number of
   rectangle blocks.

Thus direct designated recapture is no longer part of the paid all-cross cost.
The remaining cross-state obstruction is either pairwise geometric conflict or
residual unary/binary collateral.