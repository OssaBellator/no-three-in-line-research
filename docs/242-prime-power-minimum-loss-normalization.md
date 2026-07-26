# Canonical minimum losses are permanent inside each normalized host segment

CMR950--CMR957 normalize arbitrary same-vertex-set host transitions to rollback,
minimum-core contraction, strict improvement, or a nested decreasing restriction
segment.  CMR1094--CMR1101 remove routing changes from the selected minimum path.
The remaining lost-minimum witnesses can therefore be counted directly: inside one
normalized segment a lost edge never returns, and two canonical loss events cannot
use the same labelled edge.

This chapter records a parameter-free branch-wide loss stock.  It does not claim
that a contracted dirty interface can never be reopened under a later structural
escape; that fixed-core reopening remains part of the target-ancestry frontier.

Fix one selected minimum execution on labelled vertex sets of current side `m`.
Let `H_0,H_1,...` be the canonically normalized same-vertex-set hosts between two
successive contractions or structural exits.

## 1. Normalized hosts are nested

### Theorem CMR1102 -- PROVED

Between contractions, strict improvement, or structural owner exit,

\[
\boxed{
H_0\supsetneq H_1\supsetneq H_2\supsetneq\cdots.
}
\]

Every attempted added batch is rolled back completely, contracts one added
minimum-core edge, or yields strict improvement.

### Proof

This is CMR952--CMR956.  After canonical normalization no added batch remains in a
same-value, noncontracting continuation, so only strict restrictions survive. ∎

Consequently there is no restoration-only recurrence inside a normalized segment.

## 2. Lost-minimum witnesses are permanent in one segment

At a strict transition choose an old canonical minimum `S_i`.  If it does not
survive in `H_{i+1}`, choose the first edge

\[
f_i\in S_i\setminus H_{i+1}.
\]

### Theorem CMR1103 -- PROVED

The edge `f_i` is absent from every later host in the same normalized segment.
Moreover the canonical witnesses `f_i` are pairwise distinct.

### Proof

Nestedness gives `H_j subseteq H_{i+1}` for every later `j`, so `f_i` remains
absent.  Every later canonical minimum is feasible in its current host and
therefore cannot contain `f_i`; hence a later loss witness, which belongs to that
later minimum, cannot equal `f_i`. ∎

Thus a minimum loss spends one previously unspent labelled host edge.

## 3. One-segment loss bound

Suppose the segment has state cardinality `k` and edge-universe size `u`.

### Theorem CMR1104 -- PROVED

The number of canonical lost-minimum events in the segment is at most

\[
\boxed{u-k.}
\]

For a saturated two-layer side-`m` system,

\[
\boxed{u-k\le2m^2-2m.}
\]

### Proof

Every loss event accompanies a strict host transition and has a distinct witness
by CMR1103.  The final nonempty host contains a size-`k` state whose edges survive
the segment, leaving at most `u-k` other labelled edges available for strict loss.
The two-layer bounds are `u<=2m^2` and `k=2m`. ∎

This sharpens the coarse transition count when only loss witnesses are charged.

## 4. Fixed-vertex execution bound

A side-`m` normalized execution has at most `2m` contractions and hence at most
`2m+1` restriction segments.

### Theorem CMR1105 -- PROVED

Before strict improvement or structural exit, the total number of canonical
lost-minimum witnesses on fixed side-`m` labelled universes is at most

\[
\boxed{
L_m
=
(2m+1)(2m^2-2m).
}
\]

### Proof

Apply CMR1104 to each of at most `2m+1` segments supplied by CMR955.  The displayed
bound deliberately uses the initial side for every segment. ∎

## 5. Branch-wide parameter-free loss stock

Recall

\[
H_m=2m^2+m+1.
\]

Define

\[
\mathcal L(d)
=
\sum_{m=1}^{d}H_mL_m
\]

and

\[
\boxed{
\mathfrak L(N,h)
=
(h+1)(2N+1)\mathcal L(N).
}
\]

### Theorem CMR1106 -- PROVED

Across one complete selected minimum closure branch, before fixed-core reopening
of an already contracted interface, strict improvement, or finite structural exit,
the total number of owner-labelled lost-minimum witnesses is at most

\[
\boxed{
\mathfrak L(N,h)
=
(h+1)(2N+1)
\sum_{m=1}^{N}
(2m^2+m+1)(2m+1)(2m^2-2m).
}
\]

### Proof

At side `m`, CMR1098 gives at most `H_m` selected-routing host stages along one
strict descent path.  Apply CMR1105 to each.  Multiply by the `2N+1` nodes of the
complete unit-wall tree and the `h+1` closure-envelope epochs. ∎

The bound is intentionally coarse but polynomial and has no routing recurrence
parameter.

## 6. Same-value target-cell handoffs are loss events

### Theorem CMR1107 -- PROVED

A same-value physical target handoff from CMR983 deletes both layer copies of one
target cell omitted by a surviving minimum.  After canonical host normalization,
at least one of those labelled copies is a strict restriction edge and the handoff
is charged to the finite loss stock of CMR1106 unless contraction, structural
exit, or strict improvement occurs.

Repeated use of the same physical target cell in one segment requires a genuine
added batch, which is rolled back, contracts an added minimum-core edge, or
improves.

### Proof

The two-label cut preserves the new minimum and removes at least the selected old
copy.  CMR1102 makes the resulting restriction permanent inside the segment.
Any later availability is an expansion and receives the complete CMR952 response.
∎

Thus zero-growth target-cell recurrence is not independent of the normalized loss
ledger.

## 7. Routing-support recurrence disappears

### Theorem CMR1108 -- PROVED

On the selected minimum path there is no routing-support recurrence branch.  At
every host stage the execution restricts once to the routing skeleton of its chosen
minimum and never changes routing before host restriction, contraction, strict
child descent, wall/product descent, envelope exit, or improvement.

### Proof

This is CMR1097. ∎

Routing-support edges may still appear as witnesses in a complete state-space
search, but not in this canonical minimum-anchor lineage.

## 8. Normalized loss endpoint

### Corollary CMR1109 -- PROVED

After CMR1094--CMR1108, the selected minimum prime-power scheduler has finite,
parameter-free stocks for:

1. routing-normalized owner stages;
2. owner-labelled protected growth;
3. fresh structural deletion roots;
4. same-vertex-set lost-minimum witnesses;
5. same-value physical target-cell handoffs.

Every continuation beyond those stocks reaches minimum-core contraction, strict
factor or unit-wall descent, fixed-core reopening, envelope expansion, finite base
handling, or strict objective improvement.

The remaining dynamic frontier is therefore **fixed-core reopening ancestry**:
when a target or interface already contracted into the induced objective is later
escaped in a larger structural owner, prove that repeated reopening of its physical
edges has finite owner-independent stock or forces strict minimum decrease.

### Proof

Combine CMR1094--CMR1108 with CMR950--CMR957 and CMR982--CMR989. ∎

No all-`n` theorem is claimed.  Nestedness, witness distinctness, segment bounds,
branch-wide arithmetic, and target-cell charging are checked in
[`scripts/verify_prime_power_minimum_loss_normalization.py`](../scripts/verify_prime_power_minimum_loss_normalization.py).
