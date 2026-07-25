# Exact edge incidence pays full-token state expansion

CMR410--CMR412 erase exact selected-state cycles, but leave a factorial bound on
histories of distinct states.  The full-token ledger has a much sharper aggregate
interpretation.  A returned cell belongs to exactly one full prefix cell at each
depth, while the projective direction is only a certificate label.  Therefore
summing token reintroduction over all prefix coordinates counts actual returned
edges with an exact, depth-independent multiplicity.

This removes an unnecessary factor of `t` from the aggregate bounds in CMR402
and CMR409.  It also gives a direct polynomial payment for state-space expansion:
two distinct perfect matchings differ on at least two old edges.

Let

\[
t=p^h,
\qquad h\ge2,
\]

and for

\[
1\le b<h,
\qquad
(a,c)\in(\mathbb Z/p^b\mathbb Z)^2,
\qquad
\theta\in\mathbb P^1(\mathbb F_p),
\]

write

\[
U_{b,a,c,\theta}^{(2)}
=
\{(x,y)\in[t]^2:
 x\equiv a\pmod{p^b},
 y\equiv c\pmod{p^b}\}.
\]

The set does not depend on `theta`; the label is retained because the dynamic
certificate inventories do.

## 1. Exact labelled incidence identity

Let `R_1,\ldots,R_m` be arbitrary finite returned-edge sets in the same parent
board.  Repetitions between different `R_j` are counted with multiplicity.  Put

\[
\mathcal I(R_1,\ldots,R_m)
=
\sum_{j=1}^m
\sum_{\theta\in\mathbb P^1(\mathbb F_p)}
\sum_{b=1}^{h-1}
\sum_{a,c\bmod p^b}
|R_j\cap U_{b,a,c,\theta}^{(2)}|.
\]

### Theorem CMR413 — PROVED

The labelled full-token incidence mass is exactly

\[
\boxed{
\mathcal I(R_1,\ldots,R_m)
=
(p+1)(h-1)
\sum_{j=1}^m|R_j|.
}
\]

### Proof

Fix one returned edge `(x,y)` and one depth `b`.  There is exactly one prefix
pair

\[
(a,c)=(x\bmod p^b,y\bmod p^b)
\]

whose full-token universe contains the edge.  The same cell universe is recorded
under each of the `p+1` projective direction labels.  Hence the edge contributes
exactly `p+1` at each of the `h-1` nonroot depths.  Sum over all edge occurrences.
∎

This identity is purely combinatorial and applies to prefix, packet,
joint-parent, or arbitrary selected-matching resets.

## 2. Scale-filtered prefix incidence

For a reset performed at prefix depth `r`, only token depths `b>r` can regard the
move as a later coarse reset.  Define

\[
\mathcal I_{>r}(R)
=
\sum_{\theta}
\sum_{b=r+1}^{h-1}
\sum_{a,c\bmod p^b}
|R\cap U_{b,a,c,\theta}^{(2)}|.
\]

### Theorem CMR414 — PROVED

For every returned set `R`,

\[
\boxed{
\mathcal I_{>r}(R)
=
(p+1)(h-1-r)|R|.
}
\]

Consequently, a two-layer one-pass prefix sweep in which the selected blocks at
each depth are pairwise disjoint has total direction-labelled full-token coarse
return mass at most

\[
\boxed{
(p+1)t h(h-1).
}
\]

For one layer, the bound is halved.

### Proof

The first identity repeats the proof of CMR413 over the `h-1-r` finer depths.
At one fixed depth `r`, pairwise disjoint rematched blocks contain disjoint old
matching edges.  Their total returned-edge count is at most `t` in one layer and
at most `2t` in two layers.  Therefore the depth-`r` contribution is at most

\[
2t(p+1)(h-1-r).
\]

Sum over `r=0,\ldots,h-2` and use

\[
2\sum_{r=0}^{h-2}(h-1-r)=h(h-1).
\]

∎

Thus the full-token aggregate for one prefix pass is

\[
O_p(t\log^2t),
\]

not merely the valid but nonsharp `O_p(t^2\log t)` bound of CMR402.

## 3. Harmonic-packet sweep

Let `P_\eta(t)` be the packet count from CMR406.  A packet sweep performs one
one-layer whole-parent reset for every packet.

### Corollary CMR415 — PROVED

One harmonic-packet sweep has total direction-labelled full-token return mass at
most

\[
\boxed{
(p+1)(h-1)P_\eta(t)t.
}
\]

One descending two-layer prefix pass followed by one packet sweep therefore has
mass at most

\[
\boxed{
(p+1)t(h-1)\bigl(h+P_\eta(t)\bigr).
}
\]

For fixed `p`, this is

\[
\boxed{O_p(t\log^2t).}
\]

### Proof

By CMR403, one whole-parent one-layer reset returns at most `t` edges.  Apply
CMR413 to each of the `P_\eta(t)` packet installations.  Add CMR414 for the prefix
pass.  Finally CMR406 gives `P_\eta(t)=O(\log t)` and `h=\log_p t`. ∎

This improves CMR409 by one factor of `t`.  The earlier theorem remains correct
as a tokenwise union bound, but it does not use the fact that a matching has only
`t` old edges.

## 4. Every genuinely new selected state returns two edges

Let `K` be one parent matching board, let `F` be a fixed forbidden set, and let
`M,M'` be perfect matchings of `K\setminus F`.  Put

\[
H=K\setminus(M\cup F),
\qquad
H'=K\setminus(M'\cup F).
\]

### Theorem CMR416 — PROVED

The returned set is exactly

\[
\boxed{H'\setminus H=M\setminus M'.}
\]

If `M\ne M'`, then

\[
\boxed{|H'\setminus H|\ge2.}
\]

### Proof

Because `M\cap F=\varnothing`,

\[
H'\setminus H
=(M\cup F)\setminus(M'\cup F)
=M\setminus M'.
\]

The symmetric difference of two perfect matchings is a disjoint union of even
alternating cycles.  If the matchings are distinct, one such cycle has length at
least four and contributes at least two edges of `M\setminus M'`. ∎

The lower bound is specific to a feasible **selected-state** reset.  For an
arbitrary forbidden matching which overlaps other fixed forbidden edges, only
the upper inclusion of CMR403 is available.

## 5. Quantitative state-space expansion

Consider a monotone-mask deletion history in which selected-state changes are
performed at fixed current mask, so CMR416 applies to every reset.  Let `N` be
the number of nontrivial whole-parent selected-state resets, let

\[
C=\sum_j|H_j'\setminus H_j|
\]

be their unlabelled returned-edge churn, and let `\mathcal I` be the corresponding
all-depth, all-direction full-token mass.

### Corollary CMR417 — PROVED

One has

\[
\boxed{C\ge2N}
\]

and

\[
\boxed{
\mathcal I
=(p+1)(h-1)C
\ge
2(p+1)(h-1)N.
}
\]

Hence a cycle-erased history containing `L` whole-parent selected states satisfies

\[
\boxed{
L
\le
1+rac{\mathcal I}{2(p+1)(h-1)}.
}
\]

For a changed local matching in a depth-`r` prefix block, the scale-filtered
payment is at least

\[
\boxed{2(p+1)(h-1-r)}
\]

whenever `r\le h-2`.

### Proof

CMR416 gives at least two returned edges for every nontrivial reset.  CMR413
converts total churn to labelled mass.  CMR410--CMR411 allow a shortest history
to be taken without repeated complete selected states, so `L-1` transitions are
nontrivial.  The local statement uses CMR414 instead of CMR413. ∎

This is the first polynomial state-expansion payment independent of the
factorial number of parent permutations.  Exact recurrence is cycle-erasable;
a long sequence of distinct states now necessarily creates proportionally large
returned-edge and full-token mass.

It does not yet prove termination: repeated sweeps may keep paying new edge
churn, and fully forced exchange ancestry may transport the payment elsewhere.
The revised frontier is to couple this exact churn payment to target-load
destruction, packet protection, reserve depletion, or bounded ancestry width.

No all-`n` theorem is claimed here.  The incidence identities, prefix and packet
sums, matching-difference lower bound, and state-history inequalities are checked
in
[`scripts/verify_prime_power_edge_incidence_state_expansion.py`](../scripts/verify_prime_power_edge_incidence_state_expansion.py).
