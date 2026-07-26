# Candidate transversals expose the exact Hall-wall obstruction

CMR1382--CMR1389 rewrite same-owner collateral as an edge-assignment problem.
That normal form is exact, but the selector which attains equality is constructed
from an already optimal response.  The next useful step is to expose what a
low-collateral response means before the response is known.

The answer is a deletion-transversal problem.  Exempt a low-weight family of
candidate triples, choose one residual edge from every other candidate, delete
the chosen edges, and ask whether a perfect matching survives.  This is exactly
equivalent to the original weighted minimum-collateral problem.  Failure is not
an uncontrolled optimization endpoint: every failed transversal contains an
inclusion-minimal perfect-matching blocker, hence an exact deficiency-one Hall
wall by the existing unit-wall theory.

The statements apply to any finite bipartite response host `G` with at least one
perfect matching.  Let `C` be a finite family of possible new physical credits.
Each `T in C` has a nonempty compatible residual prescription

\[
P_T\subseteq E(G),
\qquad
1\le |P_T|\le3,
\]

and a nonnegative weight `v_T`.  For a response matching `R`, put

\[
N_v(R)=\sum_{T\in\mathcal C}v_T\mathbf1_{P_T\subseteq R}.
\]

For `B subseteq C`, a **`B`-transversal selector** is a map

\[
\sigma:\mathcal C\setminus B\to E(G),
\qquad
\sigma(T)\in P_T.
\]

Its deletion set is

\[
F_\sigma=\{\sigma(T):T\in\mathcal C\setminus B\}.
\]

Repeated choices collapse to one physical deleted edge.

## 1. Every response produces a surviving transversal

### Theorem CMR1390 -- PROVED

For every response `R in PM(G)`, let

\[
B(R)=\{T\in\mathcal C:P_T\subseteq R\}.
\]

There is a `B(R)`-transversal selector `sigma_R` such that

\[
R\in\operatorname{PM}(G\setminus F_{\sigma_R})
\]

and

\[
\sum_{T\in B(R)}v_T=N_v(R).
\]

### Proof

If `T notin B(R)`, then `P_T` is not contained in `R`, so choose

\[
\sigma_R(T)\in P_T\setminus R.
\]

Every chosen edge lies outside `R`.  Therefore deleting their union preserves
`R`.  The weight identity is the definition of `B(R)`. ∎

## 2. Every surviving transversal bounds collateral

### Theorem CMR1391 -- PROVED

Let `B subseteq C` and let `sigma` be a `B`-transversal selector.  If

\[
R\in\operatorname{PM}(G\setminus F_\sigma),
\]

then

\[
\boxed{
N_v(R)\le\sum_{T\in B}v_T.
}
\]

### Proof

For every `T notin B`, the selected edge `sigma(T)` belongs to `P_T` and is
absent from `R`.  Hence `P_T` is not contained in `R`.  Only exempt candidates
can occur. ∎

## 3. Exact weighted transversal identity

### Theorem CMR1392 -- PROVED

\[
\boxed{
\min_{R\in\operatorname{PM}(G)}N_v(R)
=
\min_{B\subseteq\mathcal C}
\left\{
\sum_{T\in B}v_T:
\begin{array}{l}
\text{there is a `B`-transversal selector `sigma`}\\
\text{with }\operatorname{PM}(G\setminus F_\sigma)\ne\varnothing
\end{array}
\right\}.
}
\]

### Proof

CMR1390 sends every response to a feasible transversal of exactly the same
weight, so the right side is at most the left side.  CMR1391 sends every feasible
transversal to a response whose collateral is at most the exempt weight, so the
left side is at most the right side. ∎

Unlike the selector identity of CMR1384, this form isolates the obstruction to a
small value: one must preserve a perfect matching after hitting every
nonexempt prescription.

## 4. Clean and strict-response criteria

### Theorem CMR1393 -- PROVED

The host contains a clean response,

\[
\min_RN_v(R)=0,
\]

if and only if there is a full candidate transversal

\[
\sigma:\mathcal C\to E(G),
\qquad
\sigma(T)\in P_T,
\]

such that

\[
\operatorname{PM}(G\setminus F_\sigma)\ne\varnothing.
\]

### Proof

Set `B=emptyset` in CMR1392. ∎

### Theorem CMR1394 -- PROVED

For every real threshold `L`, the following are equivalent.

1. There is a response `R` with `N_v(R)<L`.
2. There is a family `B subseteq C` with

   \[
   \sum_{T\in B}v_T<L
   \]

   and a `B`-transversal selector whose deletion leaves a perfect matching.

Thus a guaranteed old-credit loss `L_v` gives a strict improving response
exactly when a transversal with exempt weight below `L_v` survives.

### Proof

This is the strict sublevel form of CMR1392. ∎

## 5. Failed transversals are Hall walls

### Theorem CMR1395 -- PROVED

Fix `B` and a `B`-transversal selector `sigma`.  Exactly one of the following
holds.

1. `G setminus F_sigma` has a perfect matching, and CMR1391 gives a response of
   collateral at most `sum_{T in B}v_T`.
2. `G setminus F_sigma` has no perfect matching.  Then there is a row set `U`
   with

   \[
   |N_{G\setminus F_\sigma}(U)|<|U|.
   \]

   Moreover `F_sigma` contains an inclusion-minimal blocker `Q`.  Deleting `Q`
   gives exact matching deficiency one, and restoring any edge of `Q` restores a
   perfect matching.  Hence `Q` is the deficiency-one unit-wall object of
   CMR1150--CMR1157.

### Proof

The first branch is CMR1391.  In the second branch, Hall's theorem supplies `U`.
Because `F_sigma` is finite, delete redundant edges until an inclusion-minimal
subset `Q` still blocks every perfect matching.  The existing minimal-blocker
unit-wall theorem gives exact deficiency one and edgewise restoration. ∎

Consequently, failure of a proposed cross-line policy has a finite geometric
certificate: its chosen candidate edges cover a unit Hall wall.  The remaining
research task is to show that low-weight exemptions, primitive-height classes,
prefix/carry classes, or owner credits prevent all such transversal walls from
persisting.

## 6. Equal fractional ownership is not sufficient

A tempting computable policy splits each candidate weight equally among its
residual edges:

\[
\ell(a)=
\sum_{T:a\in P_T}\frac{v_T}{|P_T|}.
\]

For every response,

\[
N_v(R)\le\sum_{a\in R}\ell(a),
\]

so a minimum-cost perfect matching for `ell` is a valid explicit upper bound.
It does exploit cross-line edge sharing, but it is still too coarse.

### Theorem CMR1396 -- PROVED BY COMPLETE FINITE CHECK

On the standard side-four grid, take the disjoint layers

\[
O=(0,1,3,2),
\qquad
M=(1,3,2,0).
\]

The state has the single old target

\[
\{(0,0),(1,1),(2,2)\}.
\]

For each of its three target-cell extension-free banks, the destroyed load is
one and a clean response exists, but the minimum equal-share assignment costs
are respectively

\[
1,
\qquad
\frac{11}{6},
\qquad
2.
\]

Thus equal splitting never proves the required strict inequality on this state,
even though the exact transversal optimum is zero in every relevant bank.

### Proof

Direct determinant enumeration gives the unique old target.  Complete
enumeration of each extension-free response bank gives true minimum collateral
zero.  The equal-share loads have the displayed exact rational minimum matching
costs. ∎

This rules out equal ownership as a universal all-`n` closure policy.  Useful
fractional ownership must depend on geometry, height, prefix/carry type, or the
Hall wall exposed by the proposed deletion.

## 7. The side-five witness is a clean transversal

### Theorem CMR1397 -- PROVED BY COMPLETE FINITE CHECK

For the CMR1389 side-five state

\[
M=(0,1,2,4,3),
\qquad
O=(1,3,4,0,2),
\qquad
e=(0,0),
\]

and clean response

\[
R=(4,1,0,2,3),
\]

the extension-free bank has `43` candidate prescriptions.  Choosing, from each
prescription, one edge outside `R` produces a deletion set of `13` physical
edges, and `R` remains a perfect matching after all thirteen deletions.

### Proof

CMR1389 proves that no candidate prescription is contained in `R`.  Therefore
every prescription has an edge outside `R`; select one.  Duplicate selected
edges collapse to a set of size thirteen.  Direct enumeration verifies that `R`
is disjoint from this set and remains in the extension-free host. ∎

## 8. Transversal/Hall endpoint

The same-owner frontier now has two exact normal forms.

1. CMR1382--CMR1389 assign candidate weight to response edges and minimize the
   resulting matching cost.
2. CMR1390--CMR1397 exempt a low-weight candidate family, hit every remaining
   prescription, and require a perfect matching to survive the deletions.

The second form makes the next obstruction explicit.  At a positive minimum,
every candidate transversal below the destroyed-load threshold must contain a
perfect-matching blocker, and every inclusion-minimal such blocker is a
unit Hall wall.  A closing theorem must charge these transversal walls to
primitive height, prefix/carry ancestry, protected reserve, or a subcritical
same-owner credit class.  No all-`n` theorem is claimed.

The weighted identity, clean and threshold criteria, Hall witnesses, minimal
blockers, side-four equal-share obstruction, and side-five clean transversal are
checked in
[`scripts/verify_prime_power_candidate_transversal_hall.py`](../scripts/verify_prime_power_candidate_transversal_hall.py).
