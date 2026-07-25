# Minimum rollback states form a layered tight matching face

CMR439--CMR447 bound and pay sparse rollback, but the cheap branch can still
contain many avoiding perfect matchings.  This chapter gives that branch a
canonical structure.  Give every deleted edge unit cost and every final-host
edge zero cost.  The rollback number is exactly the minimum assignment cost of
a perfect matching avoiding the terminal essential edge.

Relative to one minimum-cost matching, alternating cycles become directed cycles
with weights in `{-1,0,1}`.  Optimality excludes negative directed cycles.
Shortest-path potentials therefore produce a tight-edge subgraph whose perfect
matchings are **exactly** the minimum rollback states.  All tight exchange arcs
stay within one potential level or move by one level according to whether they
replace a final edge by a deleted edge or conversely.

Use the deletion-pass notation of CMR439.  Thus

\[
G\subseteq G_0,
\qquad
\Delta=E(G_0)\setminus E(G),
\]

and `e` is essential in `G` but nonessential in `G_0`.  On `E(G_0-e)` define

\[
c(a)=
\begin{cases}
0,&a\in E(G),\\
1,&a\in\Delta.
\end{cases}
\]

For a perfect matching `M`, put

\[
c(M)=\sum_{a\in M}c(a)=|M\cap\Delta|.
\]

## 1. Rollback number is minimum assignment cost

### Theorem CMR448 — PROVED

The rollback number satisfies

\[
\boxed{
\kappa(e)
=
\min\{c(M):M\in\operatorname{PM}(G_0-e)\}.
}
\]

If `M` is a minimum-cost matching, then

\[
R_M=M\cap\Delta
\]

is a minimum rollback set.  Conversely, every minimum rollback set is the
restored-edge set of at least one minimum-cost matching.

### Proof

For every perfect matching `M` of `G_0-e`, restoring `M\cap\Delta` makes `M`
available in the final host, so

\[
\kappa(e)\le c(M).
\]

Conversely, if `R\subseteq\Delta` and `G+R-e` has a perfect matching `N`, then

\[
N\cap\Delta\subseteq R
\]

and therefore

\[
c(N)\le |R|.
\]

Minimize first over matchings and then over rollback sets.  Equality follows.
If `R` is minimum and `N` witnesses it, then `N` must use every edge of `R` by
CMR440, so `N\cap\Delta=R`. ∎

Thus cheap rollback is an ordinary minimum-cost assignment face with binary
edge costs.

## 2. Alternating-cycle optimality

Fix one minimum-cost perfect matching

\[
M=\{m_j=\ell_jr_j:1\le j\le t\}
\]

of `G_0-e`.  Form the matching-contraction digraph on `[t]`: every nonmatching
edge `a=\ell_jr_k` gives an arc `j\to k`.  Give that arc weight

\[
\boxed{
w(j,k)=c(\ell_jr_k)-c(m_k).
}
\]

The weights lie in `{-1,0,1}`.

### Theorem CMR449 — PROVED

Every directed cycle in the weighted contraction digraph has nonnegative total
weight.

Equivalently, flipping any `M`-alternating cycle in `G_0-e` cannot reduce the
number of deleted edges used by the matching.

### Proof

A directed cycle

\[
j_1\to j_2\to\cdots\to j_s\to j_1
\]

replaces the matching edges

\[
m_{j_2},m_{j_3},\ldots,m_{j_1}
\]

by the corresponding nonmatching edges.  Its total directed weight is exactly
the change in matching cost under that alternating-cycle flip.  A negative
cycle would therefore produce a perfect matching of `G_0-e` with cost below
`c(M)=\kappa(e)`, contradicting CMR448. ∎

This is a genuine no-negative-cycle invariant for minimum rollback.

## 3. Zero cycles connect all minimum rollback states

### Theorem CMR450 — PROVED

Let `M'` be another perfect matching of `G_0-e`.  Then `M'` has minimum rollback
cost if and only if every alternating cycle of

\[
M\triangle M'
\]

has total weight zero in the contraction digraph.

Consequently every minimum rollback state is obtained from `M` by flipping a
family of vertex-disjoint zero-weight alternating cycles.

### Proof

The symmetric difference is a disjoint union of alternating cycles.  By CMR449,
flipping any one of those cycles from `M` has nonnegative cost change.  The total
cost change from `M` to `M'` is the sum of the cycle changes.

If `M'` is minimum, the total change is zero, so every nonnegative summand is
zero.  Conversely, if every cycle has zero change, flipping all of them preserves
cost and produces `M'`. ∎

Thus positive-cost excursions are unnecessary inside the canonical cheap
rollback class.

## 4. Shortest-path potentials and the tight host

Add an auxiliary source with a zero-weight arc to every contraction vertex.  Let

\[
\phi(j)
\]

be the shortest-path distance from that source to `j`.  CMR449 guarantees that
these distances are finite.  For every contraction arc define the reduced
weight

\[
\overline w(j,k)
=
w(j,k)+\phi(j)-\phi(k).
\]

Let `T_e(M)` be the bipartite subgraph consisting of all matching edges of `M`
and every nonmatching edge whose contraction arc has reduced weight zero.

### Theorem CMR451 — PROVED

One has

\[
\boxed{
\overline w(j,k)\ge0
}
\]

for every contraction arc, and

\[
\boxed{
\operatorname{PM}(T_e(M))
=
\{N\in\operatorname{PM}(G_0-e):c(N)=\kappa(e)\}.
}
\]

Thus the perfect matchings of the tight host are exactly the minimum rollback
states.

### Proof

Shortest-path optimality gives

\[
\phi(k)\le\phi(j)+w(j,k),
\]

which is the reduced-weight inequality.

Let `N` be minimum cost.  By CMR450, every cycle of `M\triangle N` has original
weight zero.  Potentials telescope around a cycle, so its total reduced weight
is also zero.  Since every reduced arc weight is nonnegative, every arc on the
cycle is tight.  Hence `N\subseteq T_e(M)`.

Conversely, let `N` be a perfect matching of `T_e(M)`.  Every cycle of
`M\triangle N` uses only tight arcs.  Its reduced-weight sum is zero, and
potential telescoping shows that its original-weight sum is zero.  Flipping all
cycles therefore preserves `c(M)`, so `N` is minimum cost. ∎

This canonical tight host is independent of arbitrary positive-cost rollback
states.  Different choices of the base optimum `M` describe the same optimal
matching family.

## 5. Integer rollback levels

### Corollary CMR452 — PROVED

The shortest-path potentials may be chosen integral with

\[
\boxed{
-(t-1)\le\phi(j)\le0.
}
\]

For every tight arc `j\to k`,

\[
\boxed{
\phi(k)-\phi(j)
=
w(j,k)
\in\{-1,0,1\}.
}
\]

In particular:

1. if the nonmatching edge and the replaced matching edge have the same rollback
   cost, the tight arc stays in one potential level;
2. replacing a final-host matching edge by a deleted edge moves up one level;
3. replacing a deleted matching edge by a final-host edge moves down one level.

### Proof

All arc weights are integral, so shortest-path distances are integral.  The
auxiliary zero arcs give `\phi(j)\le0`.  With no negative cycle, a shortest path
can be chosen simple; it has at most `t-1` contraction arcs, each of weight at
least `-1`, giving `\phi(j)\ge-(t-1)`.

For a tight arc, the equality `\overline w(j,k)=0` rearranges to the displayed
level equation.  The three cases are the definitions of the binary edge costs.
∎

The optimal rollback face is therefore layered by at most `t` consecutive
integer levels.  Zero-cost exchange cycles lie entirely in the tight host and
have net level change zero.

## 6. Revised frontier

CMR448--CMR452 turn cheap rollback into a canonical weighted matching object.

1. `\kappa(e)` is a minimum assignment cost, not merely an existential rollback
   size.
2. Minimum rollback matchings have no negative alternating cycle.
3. All minimum states differ by zero-weight cycle flips.
4. The tight host `T_e(M)` contains exactly those minimum states.
5. Tight arcs are layered by an integral potential of range at most `t-1`.

The immediate geometric task is now sharper: analyze the p-adic, primitive-
height, quotient, and carry distribution of the tight rollback host and its
level sets.  A large level or a dense zero-level component should feed the Hall,
prefix, or line-clean alternatives; many level changes should consume restored
edges and rollback budget.

The same minimum-cost construction is a candidate canonical class for repeated
compatible local ancestor resets: restrict each reset to the tight optimal face
rather than permitting arbitrary positive-cost state excursions.

No all-`n` theorem is claimed here.  Minimum-cost characterization,
no-negative-cycle optimality, zero-cycle connectivity, tight-host equality, and
integer potential layering are checked in
[`scripts/verify_prime_power_rollback_optimal_face.py`](../scripts/verify_prime_power_rollback_optimal_face.py).
