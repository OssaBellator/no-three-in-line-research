# Pure-factor conflict potential admits finite essential-core contraction and anchored deletion recursion

CMR629--CMR648 remove mixed product interactions by sparse rectangle
extraction, low-rank deletion/contraction, and forced-certificate escape
payment.  The remaining obstruction may be pure inside one matching factor.
This chapter gives an exact recursion for that case.

The normalisation is canonical: contract the **complete essential core**, not an
arbitrary subset of essential edges.  The residual host then has no essential
edge at all.  Candidate conflicts split according to how many contracted core
edges they use.  A conflict using one or two core edges induces a nonempty
rank-at-most-two prescription in the residual host; because the residual host
has no essential edges, one of those prescription edges may be deleted while
preserving a perfect matching.  Deletions may create a new essential core, so
the procedure recomputes and contracts the complete core after every deletion.

The process is finite.  Contractions strictly lower matching side and deletions
remove distinct physical edges.  It ends with a fixed conflict among contracted
core edges, or with a strictly smaller residual factor in which every remaining
candidate conflict is pure.

Let `H` be any balanced bipartite factor host with at least one perfect
matching.  All edges retain their original parent-board cell coordinates for
collinearity.

## 1. Contracting the complete essential core removes all essentiality

Let

\[
E_*(H)
=
\bigcap_{M\in\operatorname{PM}(H)}M
\]

be the complete essential core.

### Theorem CMR649 — PROVED

The set `E_*(H)` is a matching.  Put

\[
K=H-V(E_*(H)).
\]

Then

\[
\boxed{
\operatorname{PM}(H)
\cong
\{E_*(H)\}
\times
\operatorname{PM}(K).
}
\]

Moreover

\[
\boxed{E_*(K)=\varnothing.}
\]

### Proof

Every perfect matching contains every edge of `E_*(H)`, so those edges are
pairwise compatible and form a matching.  The product identity is CMR636.

Suppose an edge `f` were essential in `K`.  Every perfect matching of `H` is the
union of `E_*(H)` with a perfect matching of `K`, so every perfect matching of
`H` would contain `f`.  Then `f\in E_*(H)`, but its endpoints survive in `K`, a
contradiction. ∎

Thus complete-core contraction leaves an entirely nonessential matching host.

## 2. Exact conflict decomposition around a contracted core

Let

\[
R=E_*(H),
\qquad
K=H-V(R).
\]

For `N\in\operatorname{PM}(K)`, the corresponding full factor matching is

\[
M=R\cup N.
\]

For `j=0,1,2,3`, let `X_j(N;R)` count candidate conflicts in `M` containing
exactly `j` edges of `R`.

### Theorem CMR650 — PROVED

For every residual matching `N`,

\[
\boxed{
X(M)
=
X_0(N;R)+X_1(N;R)+X_2(N;R)+X_3(R).
}
\]

Here:

- `X_0` is exactly the candidate-conflict count internal to `N`;
- `X_3(R)` is independent of `N` and counts collinear triples contained in the
  contracted core itself.

### Proof

Every three-edge subset of `R\cup N` contains a unique number `j` of core
edges.  Restrict the partition to collinear triples.  The classes are disjoint
and exhaustive.  The `j=0` class lies wholly in `N`, and the `j=3` class lies
wholly in fixed `R`. ∎

This is the pure-factor analogue of CMR629.

## 3. Core-anchored conflicts have residual rank at most two

A conflict counted by `X_j` with `j\ge1` has residual prescription

\[
A=T\cap E(K).
\]

### Theorem CMR651 — PROVED

Exactly one of the following holds for every conflict using the contracted
core.

1. **Fixed core conflict.**  `j=3`, so `A=\varnothing` and the same collinear
   triple lies in every perfect matching of `H`.
2. **Rank-one anchored prescription.**  `j=2` and `|A|=1`.
3. **Rank-two anchored prescription.**  `j=1` and `|A|=2`.

Every nonempty residual prescription is a compatible partial matching in `K`.

### Proof

The conflict has three compatible edges and exactly `j` of them lie in `R`, so
`|A|=3-j`.  For `j\in\{1,2,3\}` this gives ranks two, one, and zero.  Compatibility
is inherited from the full matching conflict. ∎

No higher-rank residual condition is produced by core contraction.

## 4. One canonical reduction step

Maintain an accumulated contracted matching `R_acc` and a current residual host
`K` such that

\[
E_*(K)=\varnothing.
\]

Call a compatible one-edge or two-edge prescription `A\subseteq E(K)`
**anchored** when `R_acc\cup A` contains a candidate conflict using at least one
edge of `R_acc`.

### Theorem CMR652 — PROVED

At one normalised stage, exactly one of the following operations is available.

1. **Fixed contracted conflict.**  Three edges of `R_acc` are collinear.  Then
   every extension of the residual host contains that conflict.
2. **Anchored deletion.**  Some anchored prescription `A` exists.  Every edge of
   `A` is nonessential in `K`; deleting any chosen edge `e\in A` preserves at
   least one perfect matching of `K` and kills that anchored prescription.
3. **Pure residual state.**  No fixed contracted conflict and no anchored
   prescription exists.  Then every candidate conflict in every full matching
   `R_acc\cup N` is wholly contained in the residual matching `N`.

### Proof

If the first branch fails and an anchored prescription exists, CMR649 gives
`E_*(K)=\varnothing`, so every edge of `K`, including every edge of `A`, is
nonessential.  Deleting one preserves a perfect matching and makes `A`
unavailable.

If neither of the first two branches holds, a conflict in `R_acc\cup N` cannot
use three contracted edges and cannot use one or two contracted edges together
with a residual prescription.  By CMR650--CMR651 it must use zero contracted
edges and therefore lies wholly in `N`. ∎

After an anchored deletion, the residual host is renormalised by contracting
its newly created complete essential core.

## 5. Finite essential-core recursion

Start from `H_0=H`, accumulated core `R_0=\varnothing`, and repeat:

1. contract the complete essential core of the current residual host and add it
   to the accumulated core;
2. if the accumulated core contains a conflict, stop;
3. if an anchored prescription exists, delete one of its residual edges and
   repeat;
4. otherwise stop with a pure residual factor.

### Theorem CMR653 — PROVED

The recursion preserves a perfect matching at every stage and terminates after
finitely many steps.

If the initial factor side is `d`, then:

1. the total number of contracted edges is at most
   \[
   \boxed{d;}
   \]
2. the number of nonempty contraction rounds is at most `d`;
3. the number of anchored-deletion rounds is at most
   \[
   \boxed{|E(H)|\le d^2;}
   \]
4. the process has at most `d+d^2+1` normalised stages.

At termination, exactly one of the following holds.

- The accumulated contracted matching contains a fixed candidate conflict.
- The remaining host has strictly smaller side and every candidate conflict in
  every extension is pure inside that residual host.
- The residual side is zero and no conflict remains outside a possible fixed
  contracted conflict.

### Proof

Complete-core contraction preserves the exact perfect-matching family by
CMR649.  Anchored deletion preserves a perfect matching by CMR652.

Every contracted edge removes one source and one target vertex permanently, so
at most `d` edges can be contracted.  Every anchored deletion removes one
physical edge which is never recreated inside the monotone recursion; hence at
most `|E(H)|` deletions occur.  Each nonterminal stage performs at least one of
these two monotone operations.

The terminal alternatives are exactly the first and third branches of CMR652,
including the empty residual host. ∎

The recursion has a lexicographically decreasing measure

\[
(\text{residual side},\ \text{residual edge count}).
\]

## 6. Private restoration code for anchored deletions

For every anchored-deletion round, record the selected deleted edge `e_A` of
the processed prescription `A`.

### Theorem CMR654 — PROVED

The selected edges are pairwise distinct.  If `s` processed anchored
prescriptions are all recreated after a rollback or ancestor reset, then at
least `s` distinct selected edges must be restored.

In a parent of side

\[
t=p^h,
\]

those restorations carry exact labelled nonroot full-token incidence

\[
\boxed{
s(p+1)(h-1).
}
\]

### Proof

A selected edge is deleted permanently inside the monotone recursion, so it
cannot be selected again.  Recreating the complete processed prescription
requires restoring its own selected edge.  Distinct prescriptions processed in
distinct deletion rounds therefore require distinct selected restorations.
CMR413 supplies the exact token incidence per physical edge. ∎

Thus recursive purification cannot be undone cheaply by recreating many paid
anchored conflicts with one common edge.

## 7. Pure-factor recursion endpoint

### Corollary CMR655 — PROVED

Every pure-factor obstruction from CMR635 and CMR648 reaches at least one of the
following endpoints.

1. **Fixed essential-core conflict.**  Three accumulated essential edges form a
   candidate conflict present in every factor matching.
2. **Strict factor-side reduction.**  Essential contraction lowers the factor
   side.
3. **Matching-preserving anchored deletion.**  A rank-one or rank-two conflict
   prescription is killed while preserving a residual perfect matching.
4. **Private restoration payment.**  Recreating `s` killed anchored
   prescriptions requires `s` distinct restored edges and the CMR654 token
   incidence.
5. **Pure residual recursion.**  Every remaining conflict lies wholly in one
   strictly reduced residual matching host.
6. **Finite normalisation.**  Before restoration, at most `d` contractions and
   `d^2` anchored deletions occur for an initial side-`d` factor.

### Proof

Apply the canonical recursion CMR653 and the restoration ledger CMR654. ∎

## 8. Revised frontier

Candidate-conflict potential now respects both product factorisation and
essential-core recursion.

- Mixed conflicts are sparse low-rank rectangles.
- Fully essential mixed prescriptions transfer or become forced product
  certificates.
- Pure conflicts contract through complete essential cores.
- Core-anchored conflicts become rank-at-most-two residual prescriptions and
  pay matching-preserving deletion.
- What survives is a strictly smaller pure residual host.

The remaining prime-power frontier is therefore an owner-labelled recursion on
strictly smaller matching hosts, together with payment for fixed essential-core
conflicts.  The next theorem should connect the residual host's source/target
subsets to prime-power prefix envelopes: either the reduced factor lies inside a
strict descendant block, or its scattered vertices force quotient/carry
separation, Hall walls, or envelope expansion.

No all-`n` theorem is claimed.  Complete-core contraction, absence of residual
essential edges, conflict-rank decomposition, and monotone recursion are checked
in
[`scripts/verify_prime_power_pure_factor_recursion.py`](../scripts/verify_prime_power_pure_factor_recursion.py).
