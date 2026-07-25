# Candidate-conflict potential factors into pure blocks and sparse mixed rectangles

CMR617--CMR628 give an exact product decomposition of every canonical
line-clean cylinder after fixing one protected/free cross skeleton.  The
remaining issue is geometric: collinearity is measured in the original parent
board, so a global candidate conflict need not lie inside one matching factor.

This chapter attaches the candidate-conflict potential to the exact product.
Every conflict is either pure protected, pure free, or a mixed atom.  For a
fixed skeleton, occurrence of one mixed atom is a Cartesian rectangle in the
protected- and free-factor matching spaces.  Moreover every mixed atom contains
at most two protected-factor edges.  The complete mixed-atom stock is
polynomial in the ambient side when the free side is bounded.

Consequently, if every pair of individually clean factor matchings is globally
dirty, one exact mixed atom covers a positive fraction of the product.  That
atom is either confined to the small free factor together with the fixed
skeleton, or it gives one fixed rank-one/rank-two protected prescription which
occurs in many protected-factor matchings.  Repeated protected prescriptions
then admit a matching-preserving deletion/essential-core pass with private
restoration edges.

Fix the notation of CMR618.  Let `S` be one protected/free cross skeleton of
flow size `c`.  Put

\[
a=k-c,
\qquad
b=u-c.
\]

Let

\[
H_I=H_I(S),
\qquad
H_J=H_J(S),
\]

and write

\[
\mathcal P=\operatorname{PM}(H_I),
\qquad
\mathcal Q=\operatorname{PM}(H_J).
\]

All edges below are interpreted as their original parent-board cells.  The
matching relabelling used to define `H_I,H_J` is only combinatorial and is not
assumed to preserve real collinearity.

For `P\in\mathcal P` and `Q\in\mathcal Q`, the corresponding full state is

\[
M(P,Q)=S\cup P\cup Q.
\]

A **candidate conflict** is a collinear three-edge subset of `M(P,Q)`.  Since
`M(P,Q)` is a matching, compatibility is automatic.

## 1. Exact pure/mixed conflict decomposition

For a full state `M(P,Q)`, let

- `X_I(P)` be the number of candidate conflicts contained entirely in `P`;
- `X_J(Q)` be the number contained entirely in `Q`;
- `X_\times(P,Q;S)` be the number of all remaining candidate conflicts.

### Theorem CMR629 — PROVED

For every product state,

\[
\boxed{
X(M(P,Q))
=
X_I(P)+X_J(Q)+X_\times(P,Q;S).
}
\]

The three classes are pairwise disjoint and exhaustive.

### Proof

Every three-edge subset of `M(P,Q)` is either contained in `P`, contained in
`Q`, or is contained in neither.  The edge classes `S,P,Q` are pairwise
disjoint, so the first two alternatives cannot occur simultaneously.  Restrict
to collinear triples. ∎

Thus the two factor potentials are exact summands; all failure of additivity is
isolated in `X_\times`.

## 2. Sparse mixed-atom universe

Let

\[
E_I=E(H_I),
\qquad
E_J=E(H_J),
\qquad
R=E_J\cup S.
\]

Define `\mathfrak A_\times(S)` to be the set of compatible collinear triples in

\[
E_I\cup E_J\cup S
\]

which are contained in neither `E_I` nor `E_J`.

### Theorem CMR630 — PROVED

Every mixed conflict in every state with skeleton `S` belongs to
`\mathfrak A_\times(S)`.  Every atom `T\in\mathfrak A_\times(S)` satisfies

\[
\boxed{|T\cap E_I|\le2.}
\]

Moreover

\[
\boxed{
|R|
\le
b^2+2c
\le
u^2+2u
}
\]

and

\[
\boxed{
N_\times(S)
:=
|\mathfrak A_\times(S)|
\le
|R|\binom{n^2-1}{2}
\le
(u^2+2u)\binom{n^2-1}{2}.
}
\]

When `u=0`, the mixed-atom universe is empty.

### Proof

A mixed conflict is a collinear compatible triple drawn from the fixed edge
universe and is pure in neither factor, so it belongs to
`\mathfrak A_\times(S)`.

An atom with three protected edges would be contained in `E_I`, contrary to the
definition.  Hence it has at most two protected edges and at least one edge in
`R`.

The free host has at most `b^2` edges and the skeleton has exactly `2c` edges.
Since `b=u-c` and `c\le u`,

\[
b^2+2c\le u^2+2u.
\]

The full residual board has `n^2` physical edges.  To overcount a mixed atom,
choose one distinguished edge from `R` and then two further edges from the
remaining board universe.  This gives the displayed bound.  If `u=0`, then
`b=c=0`, so `R` and hence the mixed-atom universe are empty. ∎

For fixed free codimension `u`, the coupling stock is polynomial in `n`.

## 3. Every mixed atom is one product rectangle

For `T\in\mathfrak A_\times(S)`, put

\[
T_I=T\cap E_I,
\qquad
T_J=T\cap E_J,
\qquad
T_S=T\cap S.
\]

Define

\[
\mathcal P_T
=
\{P\in\mathcal P:T_I\subseteq P\},
\qquad
\mathcal Q_T
=
\{Q\in\mathcal Q:T_J\subseteq Q\}.
\]

### Theorem CMR631 — PROVED

The product states containing `T` are exactly

\[
\boxed{
\mathcal P_T\times\mathcal Q_T.
}
\]

Equivalently,

\[
T\subseteq M(P,Q)
\quad\Longleftrightarrow\quad
P\in\mathcal P_T
\text{ and }
Q\in\mathcal Q_T.
\]

The protected prescription `T_I` has rank zero, one, or two.

If `T_I=\varnothing`, then

\[
\boxed{T_S\ne\varnothing.}
\]

Thus a rank-zero protected atom is confined to the free factor together with at
least one fixed skeleton edge; it is not a pure free-factor conflict.

### Proof

The skeleton part `T_S` is already present in every state of the skeleton
class.  The remaining edges of `T` occur exactly when the protected matching
contains `T_I` and the free matching contains `T_J`.  This proves the rectangle
identity.

CMR630 gives `|T_I|\le2`.  If both `T_I` and `T_S` were empty, then `T` would be
contained in `E_J`, excluded by the definition of a mixed atom. ∎

This is an exact rectangle, not a probabilistic approximation.

## 4. Dirty products force one large mixed rectangle

Let

\[
\mathcal P_0
=
\{P\in\mathcal P:X_I(P)=0\},
\qquad
\mathcal Q_0
=
\{Q\in\mathcal Q:X_J(Q)=0\}
\]

be the pure-clean factor families.

### Theorem CMR632 — PROVED

Assume `\mathcal P_0` and `\mathcal Q_0` are nonempty and every product pair

\[
(P,Q)\in\mathcal P_0\times\mathcal Q_0
\]

is globally dirty.  Then `N_\times(S)>0` and some mixed atom
`T\in\mathfrak A_\times(S)` satisfies

\[
\boxed{
|\mathcal P_T\cap\mathcal P_0|
\,|
\mathcal Q_T\cap\mathcal Q_0|
\ge
\frac{|\mathcal P_0|\,|\mathcal Q_0|}{N_\times(S)}.
}
\]

Consequently

\[
\boxed{
|\mathcal P_T\cap\mathcal P_0|
\ge
\frac{|\mathcal P_0|}{N_\times(S)}.
}
\]

and symmetrically

\[
\boxed{
|\mathcal Q_T\cap\mathcal Q_0|
\ge
\frac{|\mathcal Q_0|}{N_\times(S)}.
}
\]

At least one factor support has size at least

\[
\boxed{
\sqrt{
\frac{|\mathcal P_0|\,|\mathcal Q_0|}{N_\times(S)}
}.
}
\]

### Proof

Because both factors are pure-clean, every global conflict in their product is
mixed.  The rectangles from CMR631 therefore cover
`\mathcal P_0\times\mathcal Q_0`.  Hence

\[
|\mathcal P_0|\,|\mathcal Q_0|
\le
\sum_{T\in\mathfrak A_\times(S)}
|\mathcal P_T\cap\mathcal P_0|
|\mathcal Q_T\cap\mathcal Q_0|.
\]

One summand is at least the average.  Since
`|\mathcal Q_T\cap\mathcal Q_0|\le|\mathcal Q_0|`, division gives the protected
support bound; the free support bound is symmetric.  The square-root conclusion
follows from the product lower bound. ∎

Thus a completely dirty factor product cannot be covered only by microscopic,
unrelated coupling events.

## 5. Free/interface obstruction or low-rank protected concentration

### Corollary CMR633 — PROVED

Under the hypotheses of CMR632, at least one of the following holds.

1. **Small free/interface obstruction.**  One extracted atom has
   `T_I=\varnothing`.  It consists only of free-factor edges and fixed skeleton
   edges, contains at least one skeleton edge, and uses at most three edges from
   the carrier universe
   \[
   E_J\cup S,
   \qquad
   |E_J\cup S|\le u^2+2u.
   \]
2. **Rank-one protected concentration.**  One fixed protected edge occurs in at
   least
   \[
   \boxed{
   |\mathcal P_0|/N_\times(S)
   }
   \]
   pure-clean protected-factor matchings.
3. **Rank-two protected concentration.**  One fixed compatible protected
   two-edge prescription occurs in at least
   \[
   \boxed{
   |\mathcal P_0|/N_\times(S)
   }
   \]
   pure-clean protected-factor matchings.

If `u\le q`, then

\[
\boxed{
N_\times(S)
\le
(q^2+2q)\binom{n^2-1}{2},
}
\]

and the first branch is a bounded-dimensional free/interface certificate.

### Proof

Apply CMR632 and split according to the rank `|T_I|\in\{0,1,2\}` from CMR631.
The rank-zero description follows from `T_S\ne\varnothing`.  The quantitative
bound is CMR630 with `u\le q`. ∎

The protected concentration is in one exact partial matching, not merely in one
line or one endpoint class.

## 6. Matching-preserving deletion or essential-core concentration

Fix a free matching `Q` and skeleton `S`.  Consider a finite list of distinct
mixed atoms whose protected prescriptions

\[
R_1,R_2,\ldots,R_m
\]

have rank one or two.  Process a prescription only while all its edges are
present in the current protected host.  At that step:

- if some edge of `R_i` is nonessential, delete one such edge;
- otherwise record `R_i` as fully essential.

### Theorem CMR634 — PROVED

Throughout this pass the protected host retains a perfect matching.

The deleted edges are pairwise distinct.  Every fully essential prescription is
contained in the final essential core `E_*`, which is a matching of size at most
`a`.  Consequently the number of distinct fully essential rank-one/rank-two
prescriptions is at most

\[
\boxed{
a+\binom a2.
}
\]

Every processed nonessential prescription receives one private deleted edge.
If `s` such killed prescriptions are later all recreated, at least `s` distinct
selected edges must be restored.

### Proof

Deleting a nonessential edge preserves a perfect matching by definition.
Deleted edges are distinct because an edge, once deleted, is absent at every
later step.

Essentiality persists under later matching-preserving deletions by CMR426, so
every fully essential prescription lies in the final essential core.  CMR429
says that core is a matching of size at most `a`.  It has at most `a` one-edge
subsets and `\binom a2` two-edge subsets.

For each killed prescription, the selected deleted edge belonged to that
prescription and is distinct from the selected edges of all other processed
killed prescriptions.  Recreating the complete prescription therefore requires
restoring its own selected edge. ∎

This is the product-factor analogue of the private deletion code in
CMR577--CMR581.

## 7. Product-potential endpoint

### Corollary CMR635 — PROVED

Fix one cross skeleton `S`.  The candidate-conflict potential on its exact
product class reaches at least one of the following endpoints.

1. **Clean product state.**  Some pure-clean pair `(P,Q)` has
   `X_\times(P,Q;S)=0`, hence the full state is candidate-conflict-free.
2. **Pure protected obstruction.**  No protected-factor matching is pure-clean.
3. **Pure free obstruction.**  No free-factor matching is pure-clean; this is a
   matching problem of side `b=u-c\le u`.
4. **Small free/interface atom.**  One fixed mixed atom is confined to the free
   factor plus the fixed skeleton.
5. **Rank-one/rank-two protected concentration.**  One exact protected
   prescription occurs in at least a `1/N_\times(S)` fraction of the pure-clean
   protected factor.
6. **Deletion/restoration payment.**  Repeated nonessential prescriptions are
   killed by distinct matching-preserving deletions and require distinct
   restoration to return.
7. **Essential protected core.**  The surviving distinct low-rank prescriptions
   lie among at most
   \[
   a+\binom a2
   \]
   subsets of one fixed essential matching core.

When `u\le q`, the free factor has side at most `q`, every interface has at most
`2q` state edges, and the mixed-atom stock is at most

\[
(q^2+2q)\binom{n^2-1}{2}.
\]

### Proof

If either pure-clean factor family is empty, use branches 2 or 3.  Otherwise, if
some pair has no mixed conflict, CMR629 gives branch 1.  If every pair is dirty,
apply CMR632--CMR633.  Process recurring nonempty protected prescriptions by
CMR634.  The threshold form uses CMR621 and CMR630. ∎

## 8. Revised frontier

The candidate-conflict potential is now attached to the exact product
factorisation.

- Pure conflicts belong to one factor.
- Every mixed conflict is one sparse rectangle.
- A dirty clean-factor product yields a bounded-dimensional free/interface atom
  or a rank-at-most-two protected prescription with quantitative support.
- Repeated protected prescriptions pay monotone deletion/restoration or collapse
  into one essential matching core.

The remaining prime-power step is no longer an arbitrary product interaction.
It is payment for one of three explicit objects:

1. a pure protected-factor obstruction;
2. a bounded-side pure free or free/interface obstruction;
3. a low-rank prescription inside one protected essential core.

The next target is to recurse the bounded free object through the existing
prime-power quotient/carry machinery and convert essential-core low-rank
prescriptions into exchange-corridor motion, forced-certificate terminality,
protected-reserve depletion, full-token return, or strict envelope expansion.

No all-`n` theorem is claimed.  Product factorisation, conflict decomposition,
rectangle occurrence, atom-stock bounds, and the dirty-product concentration
are checked in
[`scripts/verify_prime_power_product_conflict_rectangle.py`](../scripts/verify_prime_power_product_conflict_rectangle.py).
