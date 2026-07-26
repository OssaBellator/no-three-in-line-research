# Same-value host expansions are exactly rollbackable

CMR926--CMR933 show that new minimum states under host expansion use added
physical edges.  For a minimum-anchor proof, this yields a stronger scheduler
rule.  If an expansion lowers the minimum potential, it is the desired strict
improvement.  If it does not lower the minimum, the old minimum states remain
feasible and the entire added-edge batch can be deleted again.  The expansion is
therefore structurally unnecessary.

For an arbitrary same-vertex-set transition, factor through the intersection
host.  If an old minimum survives the restriction part, every subsequent
same-value addition can be rolled back to the intersection.  If no old minimum
survives, the transition has a concrete lost edge from the old canonical minimum.
Thus every nonimproving transition is canonically reduced to monotone restriction,
minimum-loss ancestry, or structural exit.  Restoration-only cycles cannot create
unpaid progress.

Use the notation of CMR926--CMR933.  All state potentials are evaluated by one
fixed function `\Phi` on the ambient labelled state universe.

## 1. Pure expansion is improvement or rollback

Let `H\subseteq H'` and assume both feasible families are nonempty.

### Theorem CMR934 -- PROVED

Exactly one of the following potential relations holds.

1. **Strict improvement.** `m(H')<m(H)`.
2. **Same-value expansion.** `m(H')=m(H)`, every old minimum state remains a
   minimum in `H'`, and deleting the complete added batch
   \[
   A=H'\setminus H
   \]
   restores the original host and preserves the minimum value.

In the second branch,

\[
\boxed{
\mathcal F(H'-A)=\mathcal F(H),
\qquad
m(H'-A)=m(H').
}
\]

### Proof

CMR927 gives `m(H')\le m(H)`.  Under equality, the old minimum face embeds in
the new one.  Removing exactly `H'\setminus H` returns the edge set to `H`, so
the feasible family and minimum value return exactly. ∎

No estimate on the number of newly enabled states is needed.

## 2. Canonical expansion scheduler

### Theorem CMR935 -- PROVED

A minimum-anchor scheduler may use the following complete rule for a pure
same-vertex-set expansion.

1. Accept the expansion only when it gives `m(H')<m(H)`.
2. Otherwise delete all added edges and retain the old canonical minimum state.

The rejected expansion changes neither the normalized host nor the retained
minimum value.

### Proof

Apply CMR934.  In the same-value branch the old canonical minimum survives and
the host returns exactly to `H`. ∎

Thus a new equal-potential minimum state enabled by restored edges need not be
adopted.

## 3. Pure restoration cycles are erasable

Suppose a batch `A` of absent edges is restored, no other edge changes, and the
minimum value does not decrease.  After CMR935 the same batch is deleted again.

### Theorem CMR936 -- PROVED

The selected minimum state, minimum value, and normalized host after rollback are
exactly those before restoration.  The restoration/rollback segment is
cycle-erasable.

The physical restorations still carry their exact CMR413 token incidence, but
they cannot be credited as new structural progress.

### Proof

The expansion host is `H\cup A`; CMR935 returns it to `H` while retaining the old
minimum state.  Hence the complete normalized state is identical before and
after the segment. ∎

This is the minimum-face analogue of private-batch normalization CMR807--CMR813.

## 4. Arbitrary transitions reduce through the intersection

Let `H_0,H_1` be two same-vertex-set hosts and put

\[
K=H_0\cap H_1.
\]

Write

\[
D=H_0\setminus H_1,
\qquad
A=H_1\setminus H_0.
\]

### Theorem CMR937 -- PROVED

Assume

\[
m(H_1)\ge m(H_0).
\]

Then exactly one of the following structural cases occurs.

1. Some old minimum survives in `K`.  Then
   \[
   m(K)=m(H_0)=m(H_1),
   \]
   and deleting the complete added batch `A` from `H_1` returns to `K` while
   preserving minimum value.
2. No old minimum survives in `K`.  Then the canonical old minimum contains at
   least one lost edge in `D`.

### Proof

Restriction gives `m(K)\ge m(H_0)` and expansion gives `m(H_1)\le m(K)`.  In the
first case CMR926 gives `m(K)=m(H_0)`, so the assumed lower bound on `m(H_1)`
forces equality throughout.  Apply CMR934 to `K\subseteq H_1`.  In the second
case the old canonical state is infeasible in `K` and therefore contains an edge
of `H_0\setminus K=D`. ∎

The cases are disjoint according to survival of the old minimum face.

## 5. Canonical no-improvement transition

### Theorem CMR938 -- PROVED

Every same-vertex-set transition with no strict minimum decrease can be replaced
by one of the following canonical responses.

1. A monotone restriction from `H_0` to `K=H_0\cap H_1` which preserves an old
   minimum; all added edges are rolled back.
2. A minimum-loss event with one canonical lost edge of the old minimum state.
3. A contraction or owner/vertex-set exit.

No pure added-edge batch remains in the normalized no-improvement history.

### Proof

Use CMR937.  The first case rolls back `A`; the second records the first lost edge
of the canonical old minimum.  Vertex-set changes are outside the same-host
factorisation. ∎

## 6. Monotone same-value restrictions have finite edge depth

Consider a normalized segment using branch 1 of CMR938 repeatedly at one labelled
owner.

### Theorem CMR939 -- PROVED

The hosts form a nested decreasing chain.  Every strict transition deletes at
least one previously available labelled edge.  Therefore the number of strict
same-value restriction transitions is at most

\[
\boxed{|U|-k,}
\]

where `k` is the cardinality of one surviving minimum state.  For saturated
two-layer side `n`, this is at most

\[
\boxed{2n^2-2n.}
\]

### Proof

Added edges are removed by normalization.  A strict host change is therefore a
new deletion.  One minimum state survives every transition and contributes `k`
edges which cannot be deleted. ∎

The common minimum core grows monotonically along this segment by CMR930.

## 7. Nonerasable transitions pay minimum-loss ancestry

At every branch-2 transition of CMR938, store the old canonical minimum and its
first lost edge.

### Theorem CMR940 -- PROVED

For `J` nonerasable minimum-loss transitions on one labelled edge universe and
every integer `\lambda\ge2`, at least one of the following holds.

1. One exact labelled physical edge is the canonical lost-edge witness in at
   least `\lambda` transitions.
2. 
   \[
   \boxed{
   J\le(\lambda-1)|U|.
   }
   \]

Repeated use of one witness edge is covered by one continuous absence run or
requires genuine restoration between loss generations, entering CMR777--CMR925.

### Proof

There is one witness in the finite edge universe for every nonerasable
transition.  Apply pigeonhole, then the physical absence-run identity. ∎

## 8. Expansion-rollback endpoint

### Corollary CMR941 -- PROVED

Every minimum-anchor same-vertex-set history reaches at least one of:

1. strict potential improvement under expansion;
2. exact rollback of a same-value added-edge batch;
3. a finite monotone same-value restriction pass;
4. a lost edge of the old canonical minimum and forward ancestry;
5. recurrent physical loss/restoration with exact full-token payment;
6. minimum-core contraction;
7. factor, wall, owner, or envelope exit.

Consequently restoration-only activity does not require an independent capacity
bound: if it fails to improve the minimum, it is exactly rollbackable.  The
remaining dynamic obstruction is mixed loss/restoration ancestry across owner or
vertex-set changes, together with the geometric conversion of those losses into
target-load, reserve, quotient/carry, or envelope progress.

### Proof

Combine CMR934--CMR940 with CMR910--CMR933 and the global restoration forest.
∎

No all-`n` theorem is claimed.  Expansion rollback, intersection factorisation,
minimum survival, monotone restriction depth, lost-edge witnesses, and recurrence
arithmetic are checked in
[`scripts/verify_prime_power_minimum_expansion_rollback.py`](../scripts/verify_prime_power_minimum_expansion_rollback.py).
