# Mixed child-product conflicts admit finite deletion or strict child recursion

CMR664--CMR670 classify cross-child candidate conflicts as low-rank Cartesian
boxes.  This chapter gives the canonical finite execution inside one fixed
routing skeleton.  Active mixed atoms can never appear under deletions; each
nonforced atom contains a nonessential edge which can be removed while
preserving a product state.  The process therefore terminates after at most the
initial child-edge stock.

Fix a routing product

\[
\mathcal P
=
\prod_{a\in A}\operatorname{PM}(H_a)
\]

from CMR659, with nonempty child sides `d_a` summing to `d`.  The child factors
lie in pairwise distinct strict depth-`\beta+1` prefix cells.  Candidate atoms
retain their original parent-grid coordinates.

For a mixed atom `T`, write

\[
T_a=T\cap E(H_a).
\]

Call `T` **active** when it occurs in at least one product state.

## 1. Exact active-atom criterion

### Theorem CMR677 — PROVED

A mixed atom `T` is active if and only if

\[
\boxed{
\operatorname{PM}(H_a;T_a)
e\varnothing
}
\]

for every child `a`, where

\[
\operatorname{PM}(H_a;T_a)
=
\{M\in\operatorname{PM}(H_a):T_a\subseteq M\}.
\]

When active, its occurrence family is exactly the Cartesian box

\[
\boxed{
\prod_{a\in A}\operatorname{PM}(H_a;T_a).
}
\]

### Proof

This is CMR666 applied to the fixed routing product. ∎

## 2. Every active nonforced atom has a deletable edge

### Theorem CMR678 — PROVED

Let `T` be an active mixed atom.  Exactly one of the following holds.

1. **Forced mixed certificate.**  Every edge of every nonempty `T_a` is essential
   in `H_a`.  Then every product state contains `T`.
2. **Nonessential atom edge.**  Some edge `e in T_a` is nonessential in its child
   host.

### Proof

If every atom edge is essential in its child factor, every local perfect
matching contains the complete local prescription.  CMR677 then gives the full
product as the occurrence box.

Otherwise an atom edge is absent from some perfect matching of its child host,
which is exactly nonessentiality. ∎

The alternative uses edge essentiality, not merely whether the complete local
prescription is common.

## 3. Matching-preserving mixed-atom deletion

### Theorem CMR679 — PROVED

In the second branch of CMR678, delete one nonessential atom edge `e` from its
child host.  Then:

1. the reduced child host still has a perfect matching;
2. the complete product remains nonempty;
3. the selected atom is inactive in the reduced product.

### Proof

Nonessentiality means that some perfect matching avoids `e`, so deletion
preserves matchability of that child.  All other factors are unchanged, hence
the product remains nonempty.  Every occurrence of the atom requires `e`, so
its occurrence box is empty after deletion. ∎

This is a monotone host operation and requires no restored edge.

## 4. Deletions cannot activate a new atom

### Theorem CMR680 — PROVED

Let `H'_a\subseteq H_a` be obtained by deleting child edges.  If a mixed atom
`T` is inactive in the original product, it remains inactive in the reduced
product.

Consequently, repeated CMR679 steps strictly decrease the active mixed-atom set
and terminate after at most

\[
\boxed{
\sum_{a\in A}|E(H_a)|
\le
\sum_{a\in A}d_a^2
\le
d^2
}
\]

deletions.

### Proof

Every perfect matching of a reduced child host is also a perfect matching of the
old host.  Therefore an unextendable local prescription cannot become
extendable after deletions.  CMR679 removes one physical edge at every step and
never restores it.  The displayed edge-stock bound follows from
`|E(H_a)|\le d_a^2` and

\[
\sum_ad_a^2\le\left(\sum_ad_a\right)^2=d^2.
\]

∎

## 5. Terminal mixed-product dichotomy

Run the following canonical procedure: choose the lexicographically first
active mixed atom; if it is forced, stop; otherwise delete the lexicographically
first nonessential atom edge and repeat.

### Theorem CMR681 — PROVED

The procedure preserves a nonempty child product and terminates in one of two
states.

1. **Forced cross-child conflict.**  One active mixed atom consists entirely of
   child-essential edges and belongs to every product state.
2. **Mixed-clean product.**  No active mixed atom remains.

The first state is a fixed owner-labelled product certificate.  Contracting the
complete essential cores of its child factors places all three certificate edges
in the accumulated forced core.

### Proof

Preservation and finite termination are CMR679--CMR680.  If the process stops on
an active atom, CMR678 makes it forced.  Otherwise no active mixed atom remains.
Essential contraction is exact by CMR636 and CMR649. ∎

Escape from the first state is paid by the deletion, routing-skeleton, or
entering-edge alternatives CMR643--CMR648.

## 6. Exact additivity after mixed cleaning

### Theorem CMR682 — PROVED

In the mixed-clean terminal state, every candidate conflict in every product
state is pure in one child factor.  Hence

\[
\boxed{
X\left(\bigcup_aM_a\right)
=
\sum_{a\in A}X_a(M_a)
}
\]

for all local perfect matchings `M_a`.

The product contains a globally candidate-conflict-free state if and only if
every child factor contains a pure-conflict-free perfect matching.

### Proof

With no active mixed atom, no product state contains a mixed conflict.  Apply
CMR664.  If every factor has a pure-clean matching, their union is globally
clean.  Conversely, the restriction of a globally clean product state is pure-
clean in every child. ∎

Thus all remaining obstruction is genuinely internal to strict child factors.

## 7. Strict child-recursion endpoint

### Corollary CMR683 — PROVED

Assume the fixed routing skeleton comes from the canonical first split of a
nontrivial factor of side `d` and envelope depth `\beta`.  Its positive child
factors satisfy

\[
\boxed{|A|\ge2,}
\qquad
\boxed{1\le d_a\le d-1,}
\]

and every child lies in a strict depth-`\beta+1` prefix cell.

After the finite mixed-deletion procedure, at least one of the following holds.

1. A globally candidate-conflict-free product state exists.
2. A fixed cross-child essential certificate exists and has the escape payment
   of CMR643--CMR648.
3. Some strict child factor has no pure-conflict-free perfect matching.  The
   obstruction recurses in a host of side at most `d-1` inside an envelope of
   depth at least `\beta+1`.

Therefore the lexicographic geometric measure

\[
\boxed{
\left(
\text{factor-envelope side},
\text{factor side},
\text{host-edge count}
\right)
}
\]

strictly decreases under every noncertificate continuation: a mixed deletion
reduces edge count, essential contraction reduces factor side, and child
recursion reduces the envelope side by at least a factor of `p` and also reduces
factor side.

### Proof

CMR657--CMR659 give at least two positive child cells.  Their positive loads sum
to `d`, so each is at most `d-1`, and each lies in a strict child prefix cell.
Apply CMR681.  In its mixed-clean branch, CMR682 gives a global clean state or a
pure-dirty child factor.  The stated measure changes exactly as described. ∎

This closes the fixed recurrent child-product branch up to the already isolated
forced essential certificate.  Routing changes are separately paid by
CMR671--CMR676.

No all-`n` theorem is claimed.  Active-box monotonicity, essential/deletable
classification, finite edge-stock termination, additivity, and strict-child
recursion are checked in
[`scripts/verify_prime_power_mixed_child_recursion.py`](../scripts/verify_prime_power_mixed_child_recursion.py).
