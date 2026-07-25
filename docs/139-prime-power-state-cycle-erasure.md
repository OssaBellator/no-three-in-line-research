# Exact cycle erasure for repeated matching states

The live frontier after CMR409 is dynamic: harmonic packets and ancestor blocks
may be revisited.  Static token monotonicity is false, but one elementary
no-return principle remains exact.  During a monotone deletion pass, revisiting
the same selected matching state is redundant even when the forbidden-edge mask
has grown.  The intervening segment can be erased and the larger mask imposed
directly, because the repeated selected state itself certifies feasibility.

## 1. Monotone-mask cycle erasure

Let `K` be a finite matching host.  Consider a history

\[
(S_0,F_0),(S_1,F_1),\ldots,(S_m,F_m),
\]

where

1. every `S_i` is a perfect matching of `K\setminus F_i`;
2. the masks are monotone:
   \[
   F_0\subseteq F_1\subseteq\cdots\subseteq F_m;
   \]
3. every later operation depends only on the current selected state and current
   available host.

The same statement applies to a labeled pair of layer matchings by taking `S_i`
to be the ordered pair and `F_i` to contain all fixed forbidden cells.

### Theorem CMR410 — PROVED

If

\[
S_i=S_j
\qquad (i<j),
\]

then the segment from `i` to `j` is cycle-erasable.  More precisely, one may
replace the state `(S_i,F_i)` directly by

\[
(S_i,F_j)
\]

and replay every operation after time `j` without changing any later selected
state.

### Proof

Because `S_i=S_j` and `S_j` is a perfect matching of `K\setminus F_j`, the
matching `S_i` avoids every edge of `F_j`.  Therefore `(S_i,F_j)` is a feasible
state.  The available host `K\setminus F_j` is exactly the host present at time
`j`, and the selected state is also identical.  Every subsequent operation can
therefore be replayed verbatim. ∎

The theorem does not require that the erased segment be potential-decreasing or
that individual deletions commute.

## 2. Simple histories in one deletion pass

### Corollary CMR411 — PROVED

A shortest deletion-pass history reaching a specified terminal selected state,
a specified improvement, or a specified fully forced certificate contains no
repeated selected configuration.

Consequently:

1. for one parent layer of size `t`, its length is below `t!`;
2. for two labeled parent layers, its length is below `(t!)^2`;
3. for a fixed block row fibre of size `q`, the corresponding one-layer local
   state can occur at most `q!` times before either the outside context changes
   or the history becomes cycle-erasable.

### Proof

Any repetition contradicts minimality by CMR410.  The state counts are the
numbers of permutations of the relevant fixed row fibres. ∎

These factorial bounds are deliberately only qualitative.  Their role is to
remove exact state cycles from the live obstruction; the prime-power token
ledger is still needed for polynomial control.

## 3. Ancestor and packet recurrence must change context

Fix one block or whole-parent slot `B`.  Write a selected configuration as

\[
S=(S|_B,S|_{B^c}).
\]

### Corollary CMR412 — PROVED

Within one monotone-mask envelope epoch, suppose the same local state `S|_B`
occurs at two times.  At least one of the following holds.

1. The outside context `S|_{B^c}` is different at the two times.
2. The intervening segment is cycle-erasable.

For a whole-parent harmonic-packet state, the complement is empty.  Hence exact
repetition of the same parent permutation inside one monotone deletion pass is
always cycle-erasable.  A nonerasable packet recurrence must therefore install a
new parent permutation or begin a new mask/reset epoch.

### Proof

If the outside context is also equal, the complete selected configuration is
equal.  Apply CMR410.  The whole-parent statement is the special case
`B^c=\varnothing`. ∎

Thus the remaining packet no-return problem is not recurrence of an identical
state.  It is quantitative state-space expansion: show that a long sequence of
distinct packet or ancestor states consumes full-token return mass, target load,
reserve capacity, or width in the acyclic exchange-ancestry graph before the
factorial state space becomes relevant.

No all-`n` theorem is claimed here.  Cycle erasure and finite-state bounds are
checked in
[`scripts/verify_prime_power_state_cycle_erasure.py`](../scripts/verify_prime_power_state_cycle_erasure.py).
