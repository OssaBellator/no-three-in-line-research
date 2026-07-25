# Persistent canonical selector edges admit a finite absorption chase or hit the protected trace core

CMR552--CMR557 reduce the dynamic side of a canonical selector to one exact
allowed edge which is repeatedly unavailable.  The canonical forbidden
matching itself is only an accounting choice.  It may be enlarged by a partial
matching of recurrent unavailable edges while preserving the paid-line trace.

This chapter records the exact extension criterion and the resulting finite
chase.  A recurrent edge is absorbable precisely when it is vertex-disjoint
from the already protected partial matching.  Every successful absorption
increases that matching by one edge, so at most `n-|Q_L|` such steps are
possible.  A nonabsorbable recurrent edge shares a source or target vertex with
the paid-line trace or with an earlier absorbed edge, exposing a fixed
row/column contact signature.

At every chase stage the forbidden matching is chosen deterministically, so
its collateral profile is fixed and CMR554--CMR570 apply.  Thus the dynamic
branch reaches finite history, reintroduction payment, static line/carry
geometry, or one protected-core contact after only linearly many selector
changes.

Fix one envelope-labelled compatible paid pair and paid line, with residual
complete bipartite graph

\[
K=K_{n,n}.
\]

Let `Q=Q_L` be the residual paid-line trace.  It is a partial matching.  Let

\[
\ell=|Q|.
\]

A protected absorption set `R` is any partial matching vertex-disjoint from
`Q`.  Put

\[
P=Q\cup R.
\]

## 1. Canonical extension with an absorbed partial matching

Order the residual source and target vertices by inherited coordinates.

### Theorem CMR571 — PROVED

Every protected partial matching `P=Q\cup R` has a canonical perfect-matching
extension

\[
\boxed{F_P}
\]

obtained by retaining `P` and matching the unused source and target lists in
increasing order.

The associated cylinder

\[
\mathcal D_P
=
\{\delta\in\operatorname{PM}(K):\delta\cap F_P=\varnothing\}
\]

has exact size

\[
\boxed{|\mathcal D_P|=D_n.}
\]

Every state in the cylinder avoids every residual cell of the paid line and
every absorbed edge of `R`.

### Proof

The two sides have the same number of unused vertices because `P` is a partial
matching.  Pairing their ordered lists extends `P` to a perfect matching.
Relabel `F_P` as the identity; avoiding perfect matchings are exactly the
`D_n` derangements.  Since `Q\cup R\subseteq F_P`, every cylinder state avoids
all its edges. ∎

The signature `(E,Z,L,R)` therefore owns one fixed cylinder and one fixed
rank-zero/rank-one collateral profile.

## 2. Exact criterion for one more absorption

Let

\[
f=uv
\]

be a residual edge not already in `F_P`.

### Theorem CMR572 — PROVED

There exists a perfect matching extending

\[
P\cup\{f\}
\]

if and only if

\[
\boxed{
\{u,v\}\cap V(P)=\varnothing.
}
\]

In the affirmative case, the order-preserving extension defines a canonical
new cylinder `\mathcal D_{P\cup\{f\}}` of size `D_n` which avoids `f` at zero
residual restoration cost.

In the negative case, `f` shares at least one source or target vertex with a
unique edge of the protected matching `P` at that endpoint.

### Proof

If `f` meets `V(P)`, then `P\cup\{f\}` is not a partial matching and cannot be
contained in a perfect matching.

If it is vertex-disjoint from `P`, then `P\cup\{f\}` is a partial matching in
the complete bipartite graph.  Its unused source and target sets have equal
size, so the order-preserving completion gives a perfect matching.  Apply
CMR571 to its cylinder.  Uniqueness of the protected edge at a shared endpoint
follows because `P` is a matching. ∎

Thus persistent unavailability of an absorbable edge can be removed by a
single deterministic change of accounting cylinder.

## 3. Protected-core contact signatures

Call `f` **blocked by `P`** when it fails the criterion of CMR572.  Since
`f\notin F_P`, it is not itself a protected edge.

### Theorem CMR573 — PROVED

Every blocked edge has one or two exact contact signatures of the form

\[
\boxed{(f,r,\varepsilon),}
\]

where `r\in P` is the unique protected edge sharing the relevant endpoint and

\[
\varepsilon\in\{\mathrm{source},\mathrm{target}\}.
\]

For a fixed protected matching of size

\[
k=|P|=\ell+|R|,
\]

the complete blocked-edge set is covered by the `2k` source/target vertices of
`P`.  Hence any set `B` of distinct blocked edges contains one protected
source or target vertex incident with at least

\[
\boxed{
\left\lceil\frac{|B|}{2k}\right\rceil
}
\]

members.

### Proof

CMR572 gives at least one shared endpoint.  At each shared endpoint there is
one protected edge because `P` is a matching.  This gives the exact contact
label.

Every blocked edge is incident with `V(P)`, a set of `2k` vertices.  Count one
incidence for every blocked edge and pigeonhole over those vertices. ∎

When `r\in Q`, this is a paid-line trace contact.  When `r\in R`, it is a
row/column contact with an earlier absorbed persistent edge.

## 4. One-stage dynamic selector endpoint

At a fixed protected state `P`, let the canonical profile have slack
`\Delta_P` and dynamic threshold `H_P` as in CMR554.  Suppose it is dynamic,
so `H_P>=1`.

### Theorem CMR574 — PROVED

Fix a recurrence threshold `\lambda>=2`.  For any collection of failed
occurrences of the selector owned by `P`, at least one of the following holds.

1. **Finite stage history.**  The number of failures is at most
   \[
   \boxed{
   \frac{(\lambda-1)n(n-1)}{H_P}
   \le
   (\lambda-1)n(n-1).
   }
   \]
2. **Reintroduction payment.**  One canonical allowed edge recurs in at least
   `\lambda` unavailable inventories and has many absent-to-present returns.
3. **Persistent absorbable edge.**  One recurrent edge remains continuously
   unavailable on a long interval and is vertex-disjoint from `P`; it may be
   added to `R` by CMR572.
4. **Persistent protected-core contact.**  One recurrent edge remains
   continuously unavailable on a long interval and is blocked by `P`, giving
   the fixed contact signature of CMR573.

### Proof

Apply CMR555 to the canonical selector owned by `P`.  This gives the finite
bound or one recurrent allowed edge.  Apply the absence-run theorem CMR519 to
that edge.  Its reintroduction branch is conclusion 2.  In one long
continuous-absence run, apply the exact absorbability criterion CMR572, giving
conclusion 3 or 4. ∎

## 5. Finite-depth absorption chase

Start with

\[
R_0=\varnothing,
\qquad
P_0=Q.
\]

Whenever CMR574 reaches a persistent absorbable edge `f_i`, put

\[
R_{i+1}=R_i\cup\{f_i\},
\qquad
P_{i+1}=Q\cup R_{i+1},
\]

and continue with the canonical cylinder owned by `P_{i+1}`.

### Theorem CMR575 — PROVED

The absorption chase has at most

\[
\boxed{n-\ell}
\]

successful growth steps.

Before it reaches static collateral, reintroduction payment, or a protected-
core contact, the total number of nonrecurrent failed occurrences across all
stages is at most

\[
\boxed{
(\lambda-1)n(n-1)(n-\ell+1).
}
\]

### Proof

Every successful step adds one edge to `R` while preserving that `Q\cup R` is
a partial matching.  A perfect matching of side `n` contains only `n` edges,
so

\[
|R|\le n-|Q|=n-\ell.
\]

There are therefore at most `n-\ell+1` visited protected states, including the
initial state.  At every dynamic state with no recurrence endpoint, CMR574
bounds its failed history by `(\lambda-1)n(n-1)`.  Sum over the visited states.
∎

The chase is monotone in the protected matching even though the surrounding
available host need not be monotone.

## 6. Unified canonical-selector endpoint

### Corollary CMR576 — PROVED

Fix one base canonical compatible-pair selector and a recurrence threshold
`\lambda>=2`.  Its complete repeated-failure history reaches at least one of
the following endpoints.

1. **Finite dynamic history.**  The CMR575 polynomial bound holds.
2. **Static collateral geometry.**  Some protected selector state is static
   and reaches the heavy-line, secant-star, matching-wall, heavy-prefix, or
   dispersed-carry alternatives of CMR570.
3. **Reintroduction payment.**  One fixed protected-selector edge pays the
   CMR519/full-token return ledger.
4. **Protected trace/core contact.**  One continuously unavailable edge shares
   a fixed source or target vertex with the paid-line trace or an earlier
   absorbed edge.
5. **Full absorption.**  The protected matching reaches size `n`; its cylinder
   is still an exact derangement cylinder, and no further edge is absorbable
   without meeting the protected core.

### Proof

Iterate CMR574.  A persistent absorbable edge advances the chase.  CMR575
bounds the number of advances and all intervening finite histories.  A static
state invokes CMR570.  The other recurrence branches give conclusions 3 and
4.  If the matching fills the residual side, conclusion 5 holds. ∎

## 7. Revised frontier

Both canonical-selector branches now have finite structural normal forms.

- Static collateral is converted to fixed low-height lines, secant stars,
  matching walls, heavy prefix cells, or dispersed carry cells.
- Dynamic unavailability admits at most `n-|Q_L|` monotone absorption steps.
- Nonrecurrent dynamic history is polynomially bounded.
- Every irreducible recurrent edge is owned by one selector state and contacts
  one fixed protected source or target vertex.

The remaining prime-power frontier is payment for repeated protected-core
contacts and reuse of the fixed wall/prefix/carry certificates from CMR570.
The contact branch should be converted into a Hall wall, protected-reserve
loss, deletion ancestry, or strict envelope expansion.  No selector or edge
charge is now anonymous.

No all-`n` theorem is claimed.  Canonical extension, the exact absorption
criterion, blocked-edge covers, chase length, and accumulated history bounds
are checked in
[`scripts/verify_prime_power_canonical_selector_absorption.py`](../scripts/verify_prime_power_canonical_selector_absorption.py).
