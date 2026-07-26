# A rolled-back target bank has a parameter-free missing-edge cover

CMR1118--CMR1125 attach a nonempty missing support to every infeasible
full-parent bank state.  A threshold argument isolates a recurrent blocker or a
large distinct inventory.  For minimum-anchor execution one can do better:
greedily select one missing edge and discard every pending candidate containing
it.  The selected edges are distinct and already absent from the current host.
After at most the complete labelled edge stock, they cover the whole rolled-back
bank.

Because the stored minimum anchor is feasible in the current host, every selected
blocker lies outside that anchor.  If some blockers later return while the anchor
survives, all returned blockers may be deleted again simultaneously.  Thus bank
rollback has a parameter-free normalization and does not require candidate-by-
candidate recurrence counting.

Fix a normalized host `H`, a feasible minimum anchor `S`, and a finite family
`B` of valid ambient labelled states, every one infeasible in `H`.  For
`Q in B`, put

\[
A_H(Q)=Q\setminus E(H).
\]

By CMR1118, every support is nonempty.

## 1. Greedy blocker-cover algorithm

Start with `B_0=B` and `C_0=emptyset`.  While `B_i` is nonempty, choose the first
candidate `Q_i in B_i`, choose the first edge `e_i in A_H(Q_i)`, and set

\[
C_{i+1}=C_i\cup\{e_i\},
\qquad
B_{i+1}=\{Q\in B_i:e_i\notin Q\}.
\]

### Theorem CMR1126 -- PROVED

Every selected edge is currently unavailable and lies outside the stored anchor:

\[
\boxed{e_i\notin E(H),\qquad e_i\notin S.}
\]

### Proof

The edge belongs to `A_H(Q_i)`, so it is absent from `H`.  Since `S` is feasible
in `H`, every edge of `S` belongs to `H`; hence `e_i` cannot belong to `S`. ∎

## 2. Selected blockers are distinct

### Theorem CMR1127 -- PROVED

The blocker edges `e_0,e_1,...` are pairwise distinct.

### Proof

After choosing `e_i`, every candidate containing it is removed.  Every later
candidate lies in `B_{i+1}` and therefore omits `e_i`; a later selected edge,
which belongs to its chosen candidate, cannot equal `e_i`. ∎

## 3. The final set covers the complete bank

Let `C` be the selected blocker set when the algorithm terminates.

### Theorem CMR1128 -- PROVED

Every original candidate contains at least one selected blocker:

\[
\boxed{
Q\cap C\ne\varnothing
\quad\text{for every }Q\in\mathcal B.
}
\]

Consequently every candidate remains infeasible in every host which omits `C`.

### Proof

A candidate leaves the pending family exactly at the first step whose selected
edge it contains.  Termination removes every candidate. ∎

Thus `C` is a transversal of the candidate-state family, chosen entirely from
currently missing edges.

## 4. Parameter-free cover size

### Theorem CMR1129 -- PROVED

\[
\boxed{|C|\le|U\setminus E(H)|\le|U|.}
\]

For a saturated side-`N` two-layer universe,

\[
\boxed{|C|\le2N^2.}
\]

### Proof

CMR1127 makes the selected blockers distinct, and CMR1126 places them in the
unavailable part of the labelled universe. ∎

The bound is independent of the number of candidate states in the bank.

## 5. Bulk redeletion after a return

Let `H'` be a later host and put

\[
R=C\cap E(H')
\]

for the blockers which have returned.

### Theorem CMR1130 -- PROVED

If the stored anchor `S` remains feasible in `H'`, then deleting every edge of
`R` simultaneously preserves `S` and restores a host omitting all of `C`.
Therefore the complete bank `B` is blocked again in one operation.

### Proof

CMR1126 gives `C cap S=emptyset`, so deleting `R subseteq C` does not remove an
anchor edge.  The resulting host omits all of `C`; apply CMR1128. ∎

No returned blocker is charged once for every candidate it blocks.

## 6. Failure of bulk redeletion has a canonical response

### Theorem CMR1131 -- PROVED

At a later attempted bank reopening, at least one of the following holds.

1. The stored anchor survives, and all returned blockers are bulk-redeleted by
   CMR1130.
2. The stored anchor is infeasible, exposing a canonical missing anchor edge and
   entering CMR1103--CMR1116.
3. The later host has a lower minimum value, giving strict improvement.
4. An added edge enters the minimum core and contracts.
5. A strict factor, wall, or envelope exit occurs.

### Proof

If the anchor survives and no lower value appears, use CMR1130 and the
minimum-preserving restriction theorem CMR902.  If it fails, use CMR1113.  Normalize
added batches by CMR952; structural changes give the final branch. ∎

## 7. Branch-wide blocker-cover stock

Define the parameter-free selected owner-stage count

\[
\mathfrak O_{\min}(N,h)
=
(h+1)(2N+1)\mathcal A(N),
\]

where `A(N)=sum_{m<=N}(2m^2+m+1)` is CMR1098.

### Theorem CMR1132 -- PROVED

Across one complete selected minimum closure branch, the total number of
owner-labelled blocker-cover edges chosen by fresh bank normalizations is at most

\[
\boxed{
2N^2\,\mathfrak O_{\min}(N,h).
}
\]

Returned cover edges are not fresh: they enter the bulk-redeletion, anchor-loss,
contraction, structural-exit, or improvement alternatives of CMR1131.

### Proof

Each selected host owner contributes at most `2N^2` fresh blocker edges by
CMR1129.  Multiply by the owner-stage stock. ∎

A side-sensitive sum can replace the coarse `2N^2` factor, but is unnecessary for
finiteness.

## 8. Blocker-cover endpoint

### Corollary CMR1133 -- PROVED

Target-bank rollback has a complete parameter-free response:

1. one missing-edge cover of size at most `2N^2` blocks the whole bank;
2. exact duplicate candidates need not be revisited;
3. returned cover edges are bulk-redeleted while the stored minimum survives;
4. anchor failure pays one permanent loss witness;
5. lower minima improve;
6. added-core edges contract; and
7. factor, wall, or envelope exits enter the finite structural scheduler.

The active frontier is now the final **selected-scheduler synthesis**: combine the
static dirty-minimum target packing, simultaneous target banks, robust-surplus
execution, parameter-free protected/loss/blocker stocks, and fixed-core
reconditioning into one global finite-response theorem without claiming that the
prime-field or arbitrary-length assembly is complete.

### Proof

Combine CMR1126--CMR1132. ∎

No all-`n` theorem is claimed.  Greedy cover construction, blocker distinctness,
cover exactness, bulk redeletion, and branch arithmetic are checked in
[`scripts/verify_prime_power_rollback_blocker_cover.py`](../scripts/verify_prime_power_rollback_blocker_cover.py).
