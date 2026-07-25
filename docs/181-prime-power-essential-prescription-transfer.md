# Essential low-rank prescriptions contract exactly and transfer conflict triggers to the other factor

CMR629--CMR635 attach every dirty protected/free product to a pure factor
obstruction, a small free/interface atom, or one rank-one/rank-two protected
prescription with large support.  The deletion pass CMR634 kills every
nonessential protected prescription.  The only surviving prescriptions are
contained in the protected factor's essential matching core.

An essential prescription is not merely frequent: every factor matching
contains it.  It may therefore be contracted exactly.  After contraction, the
mixed atom no longer constrains the protected factor.  Its remaining trigger is
one free edge, one compatible free pair, or only fixed skeleton edges.  The last
case is a forced candidate conflict in every state of the skeleton class.  The
first two cases are matching-preserving deletion/essentiality problems in the
small free factor.

This gives a finite alternating reduction.  Every nonessential trigger pays one
monotone deletion.  Every essential trigger contracts at least one matching
edge and strictly lowers total factor side.  A skeleton-only trigger is terminal
for that product class.

Fix one skeleton `S` and the factors

\[
H_I=H_I(S),
\qquad
H_J=H_J(S),
\]

of sides

\[
a=k-c,
\qquad
b=u-c.
\]

Let

\[
\mathcal P=\operatorname{PM}(H_I),
\qquad
\mathcal Q=\operatorname{PM}(H_J).
\]

## 1. Exact contraction of an essential matching

Let `H` be any balanced bipartite host with a perfect matching.  An edge is
**essential** when it belongs to every perfect matching of `H`.

### Theorem CMR636 — PROVED

Let `R` be a matching consisting of essential edges of `H`.  Then every perfect
matching contains `R`, and deletion of the endpoints of `R` gives the exact
factorisation

\[
\boxed{
\operatorname{PM}(H)
\cong
\{R\}
\times
\operatorname{PM}(H-V(R)).
}
\]

In particular, if `|R|=r`, the residual host has side reduced by exactly `r`.

### Proof

Every edge of `R` belongs to every perfect matching by essentiality.  Since `R`
is a matching, removing its source and target endpoints from a perfect matching
leaves a perfect matching of `H-V(R)`.

Conversely, adjoining `R` to any perfect matching of `H-V(R)` gives a perfect
matching of `H`, because the endpoint sets are disjoint and all selected edges
belong to `H`.  The two operations are inverse. ∎

Essential contraction is therefore exact, not a relaxation or a counting
bound.

## 2. An essential mixed atom transfers completely

Let `T\in\mathfrak A_\times(S)` be a mixed atom with decomposition

\[
T=T_I\sqcup T_J\sqcup T_S
\]

from CMR631.  Assume

\[
\varnothing\ne T_I
\subseteq
E_{\mathrm{ess}}(H_I),
\]

where `E_{\mathrm{ess}}(H_I)` is the protected essential core.

### Theorem CMR637 — PROVED

One has

\[
\boxed{
\mathcal P_T=\mathcal P.
}
\]

Hence the states containing `T` are exactly

\[
\boxed{
\mathcal P\times\mathcal Q_T.
}
\]

After contracting `T_I` by CMR636, occurrence of the global conflict `T`
depends only on whether the free matching contains `T_J`; the skeleton part
`T_S` is fixed.

### Proof

Every edge of `T_I` is essential, so every protected matching contains all of
`T_I`.  Thus `\mathcal P_T=\mathcal P`.  Substitute this into the rectangle
identity CMR631.  CMR636 removes the forced protected edges without changing
the remaining matching choices. ∎

The protected factor has disappeared from the trigger condition.

## 3. Exact transferred-trigger ranks

### Theorem CMR638 — PROVED

The transferred free prescription has rank at most two:

\[
\boxed{|T_J|\le2.}
\]

More precisely:

1. if `|T_I|=2`, then either
   - `|T_J|=1` and `T_S=\varnothing`, giving one free-edge trigger; or
   - `T_J=\varnothing` and `|T_S|=1`, giving a skeleton-only trigger;
2. if `|T_I|=1`, then exactly one of
   - `|T_J|=2`, `T_S=\varnothing`;
   - `|T_J|=1`, `|T_S|=1`;
   - `T_J=\varnothing`, `|T_S|=2`
   occurs.

Every nonempty `T_J` is a compatible one-edge or two-edge partial matching in
`H_J`.

### Proof

The atom has three edges and the three edge classes are disjoint, so

\[
|T_I|+|T_J|+|T_S|=3.
\]

CMR630 gives `1\le|T_I|\le2`.  Enumerating the nonnegative solutions gives the
listed cases.  Compatibility is inherited from the global atom. ∎

Thus no high-rank obstruction is created by essential transfer.

## 4. Skeleton-only atoms are forced product certificates

### Theorem CMR639 — PROVED

If the transferred trigger satisfies

\[
T_J=\varnothing,
\]

then

\[
\boxed{
T\subseteq S\cup P\cup Q
}
\]

for every

\[
(P,Q)\in\mathcal P\times\mathcal Q.
\]

Consequently every state in the skeleton class contains the same fixed
candidate conflict `T`; the class has no candidate-conflict-free state.

### Proof

Every protected matching contains `T_I` by essentiality, and every state
contains the fixed skeleton edges `T_S`.  There is no free requirement.  Hence
CMR637 gives the complete product as the occurrence rectangle. ∎

This is a terminal forced certificate for the fixed product class.  Escaping it
requires changing the skeleton, deleting/restoring one of its fixed edges, or
leaving the current envelope/selector owner.

## 5. Free-factor deletion or essential transfer

Suppose `T_J` is nonempty.  Process a finite list of distinct transferred free
prescriptions of rank one or two in the current free host `H_J`.  Process a
prescription only while all its edges remain present.  If one edge is
nonessential, delete one such edge.  Otherwise record the prescription as fully
essential.

### Theorem CMR640 — PROVED

The free host retains a perfect matching throughout the pass.  Deleted edges
are pairwise distinct.

Every fully essential transferred prescription lies in the final free essential
core, a matching of size at most `b`.  Therefore the number of distinct fully
essential rank-one/rank-two free prescriptions is at most

\[
\boxed{
b+\binom b2.
}
\]

Every processed nonessential prescription has a private selected deleted edge.
Recreating `s` such killed prescriptions later requires restoration of at least
`s` distinct selected free-factor edges.

### Proof

This is the CMR634 argument in `H_J`.  Deleting a nonessential edge preserves a
perfect matching.  Essentiality persists under later matching-preserving
deletions, and the final essential edges form one matching of size at most `b`.
The one-edge and two-edge subset count is therefore `b+\binom b2`.

Each killed prescription loses one selected edge which is never selected again,
so the selected deletion code is injective.  Complete recreation of each
prescription requires restoration of its own selected edge. ∎

Since `b\le u`, this is a genuinely lower-dimensional deletion/essentiality
problem when the protected core is large.

## 6. Finite alternating deletion-contraction depth

Consider a monotone reduction branch inside one fixed skeleton class.  At each
stage, a nonempty rank-one/rank-two prescription in one factor is treated as
follows:

- delete one nonessential prescription edge; or
- if the prescription is fully essential, contract all its edges and transfer
  the remaining atom trigger to the other factor.

### Theorem CMR641 — PROVED

Along such a branch:

1. the number of essential-contraction steps is at most
   \[
   \boxed{a+b\le n;}
   \]
2. the total number of contracted edges is at most `a+b`;
3. the number of nonessential deletion steps is at most
   \[
   \boxed{|E(H_I)|+|E(H_J)|\le a^2+b^2;}
   \]
4. every transfer either reaches a skeleton-only forced certificate or strictly
   decreases the sum of the two factor sides.

### Proof

A rank-`r` essential contraction removes `r\ge1` source vertices and `r` target
vertices from one factor, reducing the sum of factor sides by exactly `r`.
That sum begins at `a+b`, so there are at most `a+b` contraction steps and at
most `a+b` contracted edges.

Every nonessential deletion removes one physical edge from one of the two
current factor hosts.  Contraction only removes further vertices and edges; it
never recreates a deleted edge.  Hence each edge from the initial factor-edge
union can be deleted at most once.  The complete bipartite bounds give
`|E(H_I)|\le a^2` and `|E(H_J)|\le b^2`.

CMR638 shows that after contraction the residual trigger is in the other factor
or only in the skeleton. ∎

The reduction cannot cycle inside a fixed skeleton without paying restoration.

## 7. Essential-prescription transfer endpoint

### Corollary CMR642 — PROVED

Every low-rank protected concentration from CMR633--CMR635 reaches at least one
of the following endpoints.

1. **Protected deletion payment.**  A nonessential protected edge is deleted
   while preserving a protected-factor perfect matching.
2. **Strict protected contraction.**  One or two essential protected edges are
   contracted exactly.
3. **Bounded-side free trigger.**  The conflict transfers to one free edge or one
   compatible free pair in a factor of side `b\le u`.
4. **Free deletion/restoration payment.**  CMR640 kills nonessential transferred
   triggers with private free-factor edges.
5. **Strict free contraction.**  A fully essential free trigger contracts one or
   two free-factor edges.
6. **Forced skeleton certificate.**  One fixed atom consisting only of essential
   contracted edges and fixed skeleton edges occurs in every state of the
   product class.
7. **Finite branch.**  Before restoration, the complete alternating process has
   at most `a+b` contraction steps and at most `a^2+b^2` deletion steps.

When `u\le q`, every transferred free trigger lives in side at most `q` and the
skeleton has at most `2q` edges.

### Proof

Apply CMR634 to the protected prescription.  In the nonessential branch use
endpoint 1.  In the essential branch apply CMR636--CMR639.  Process a nonempty
free trigger by CMR640, and iterate.  CMR641 gives the global finite-depth
bounds.  The threshold form uses CMR621. ∎

## 8. Revised frontier

Low-rank prescriptions inside the protected essential core are no longer a
static obstruction.

- Essential protected edges contract exactly.
- Their mixed conflicts transfer to rank-at-most-two triggers in the small free
  factor.
- Essential triggers on both sides end as one fixed skeleton-only conflict.
- Nonessential triggers pay monotone deletion and private restoration.
- The alternating reduction has strict finite depth.

The remaining prime-power frontier now has two explicit exits from a recurrent
product class:

1. a forced skeleton certificate, which must be paid by skeleton change,
   cross-edge deletion/restoration, full-token return, or envelope expansion;
2. a pure-factor obstruction surviving after all mixed low-rank triggers are
   removed, to be handled recursively in the reduced host.

The next target is an ancestry ledger for forced skeleton certificates and an
exact recursion rule for pure protected/free conflicts under essential
contraction.

No all-`n` theorem is claimed.  Essential contraction, trigger-rank transfer,
forced-product occurrence, and factor-side reduction are checked in
[`scripts/verify_prime_power_essential_prescription_transfer.py`](../scripts/verify_prime_power_essential_prescription_transfer.py).
