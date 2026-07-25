# Tight rollback faces factor into strongly connected exchange blocks

CMR448--CMR452 identify minimum rollback with a binary-cost assignment face and
construct a tight host whose perfect matchings are exactly the minimum rollback
states. This chapter removes the remaining combinatorial ambiguity. Tight edges
which can actually occur in an optimum are precisely the edges lying on tight
alternating cycles, so the optimum family factors over the strongly connected
components of the tight contraction digraph.

The binary cost gives a second sharpening. If an optimum uses `k` deleted edges,
its shortest-path potential occupies only `k+1` levels, not merely `t` levels.
Cheap rollback therefore yields either exact host factorization or a large
same-level exchange cluster.

Use the notation of CMR448--CMR452. Thus

\[
M=\{m_j=\ell_jr_j:1\le j\le t\}
\]

is a minimum-cost perfect matching of `G_0-e`,

\[
k=c(M)=\kappa(e),
\]

and `D^=` is the contraction digraph formed by the zero-reduced-cost arcs of the
tight host `T_e(M)`. Let

\[
\mathcal S=\{C_1,\ldots,C_s\}
\]

be its strongly connected components.

## 1. Rollback-sensitive potential range

### Theorem CMR453 — PROVED

The shortest-path potential may be chosen integral with

\[
\boxed{-k\le \phi(j)\le0}
\]

for every contraction vertex. Hence at most `k+1` levels are occupied, and some
level contains at least

\[
\boxed{\left\lceil\frac{t}{k+1}\right\rceil}
\]

vertices.

### Proof

The auxiliary source has a zero arc to every vertex, so `\phi(j)\le0`. With no
negative directed cycle, a shortest path may be chosen simple. An arc has weight
`-1` only when its nonmatching edge has cost zero and its replaced matching edge
has cost one. Along a simple path the target vertices are distinct. Exactly `k`
base matching edges have cost one, so the path contains at most `k` negative
arcs and has weight at least `-k`.

Integrality follows from CMR452. There are at most `k+1` integer levels in
`[-k,0]`; apply the pigeonhole principle. ∎

## 2. Optimal-allowed edges

Call an edge **optimal-allowed** if it belongs to at least one minimum-cost
perfect matching.

### Theorem CMR454 — PROVED

Let `a=\ell_jr_k` be a nonmatching edge of the tight host. The following are
equivalent.

1. `a` is optimal-allowed.
2. The contraction arc `j\to k` lies on a directed cycle of `D^=`.
3. The vertices `j` and `k` lie in the same strongly connected component.

Moreover, `m_j` belongs to every minimum rollback matching if and only if `j`
lies on no directed cycle of `D^=`, equivalently its component is a singleton.

### Proof

If an optimum `N` contains `a`, the component of `M\triangle N` containing `a`
is an alternating cycle. CMR450 makes that cycle weight zero and CMR451 makes
all its arcs tight, so `j\to k` lies on a directed cycle.

Conversely, flipping a directed cycle of `D^=` is a zero-cost alternating-cycle
flip and produces an optimum containing every nonmatching edge of the cycle.
The matching-edge statement follows by applying the same argument to an optimum
which omits `m_j`. The contraction has no nonmatching loops, so a vertex lies on
no directed cycle exactly when its strongly connected component is a singleton.
∎

## 3. The optimal-allowed core

Define

\[
A_e(M)=
\bigcup\{N:N\in\operatorname{PM}(G_0-e),\ c(N)=k\}.
\]

### Theorem CMR455 — PROVED

The union of all minimum rollback states is exactly

\[
\boxed{
A_e(M)
=
M\cup
\{\ell_jr_k:j\to k\in D^=,\ C(j)=C(k)\}.
}
\]

Furthermore,

\[
\boxed{
\operatorname{PM}(A_e(M))
=
\{N\in\operatorname{PM}(G_0-e):c(N)=k\}.
}
\]

### Proof

The edge description is CMR454. Every optimum is contained in the union by
definition. Conversely, `A_e(M)` is a subgraph of `T_e(M)`, and CMR451 says
every perfect matching of the tight host is minimum. ∎

Cross-component tight arcs are dual-tight but unusable by every minimum
rollback state.

## 4. Exact strongly connected product

For `C\in\mathcal S`, put

\[
L_C=\{\ell_j:j\in C\},\qquad R_C=\{r_j:j\in C\},
\]

and let `A_C` be the block induced by `L_C\cup R_C`.

### Theorem CMR456 — PROVED

The optimal matching family factors exactly:

\[
\boxed{
\operatorname{PM}(A_e(M))
\cong
\prod_{C\in\mathcal S}\operatorname{PM}(A_C).
}
\]

A singleton component contributes only its base matching edge. A nontrivial
component is a flexible optimum block: every base matching edge in it can be
omitted by some minimum state.

### Proof

CMR455 leaves no optimal-allowed edge between distinct components. Every block
is balanced because it contains the corresponding base matching edges. A
perfect matching of the disjoint union is therefore exactly an independent
choice of a perfect matching in every block. The final statements are CMR454.
∎

## 5. Rollback cost is additive across components

Define the local rollback cost

\[
k_C=\sum_{j\in C}c(m_j).
\]

### Theorem CMR457 — PROVED

Every local perfect matching `N_C\in\operatorname{PM}(A_C)` satisfies

\[
\boxed{c(N_C)=k_C},
\]

and

\[
\boxed{\sum_{C\in\mathcal S}k_C=k.}
\]

### Proof

Combine `N_C` with the base matching on every other component. CMR456 gives a
global perfect matching of `A_e(M)`, hence a global optimum by CMR455. Its cost
is

\[
c(N_C)+\sum_{C'\ne C}k_{C'}=k,
\]

which forces `c(N_C)=k_C`. The sum identity is the definition of `k`. ∎

## 6. Rollback-free and rollback-active blocks

Call `C` **rollback-active** when `k_C>0`.

### Corollary CMR458 — PROVED

1. If `k_C=0`, every edge of `A_C` has cost zero. Thus the whole block lies in
   the final host and all of its optimum variation is rollback-free.
2. There are at most `k` rollback-active components.
3. Singleton rollback-active components are forced restored-edge factors of the
   entire optimum face.

### Proof

If a cost-one edge belonged to a block with `k_C=0`, it would occur in some
local perfect matching because `A_C` is the union of the local optimum edges.
That local matching would have positive cost, contradicting CMR457. Every
active component contributes at least one to `\sum_Ck_C=k`. The singleton
statement follows from CMR454 and CMR456. ∎

Thus restored-edge dependence is localized to at most `k` independent blocks.

## 7. Active same-level concentration

Let `\mathcal S_+` be the active components and put

\[
a=\sum_{C\in\mathcal S_+}|C|.
\]

For each active block, apply the shortest-path construction to the local binary
cost problem on `A_C`.

### Theorem CMR459 — PROVED

The local potential of block `C` occupies at most `k_C+1` levels. Consequently,

\[
\boxed{
\sum_{C\in\mathcal S_+}(k_C+1)
=
k+|\mathcal S_+|
\le2k.
}
\]

If `a>0`, some active component-level cell contains at least

\[
\boxed{
\left\lceil\frac{a}{k+|\mathcal S_+|}\right\rceil
\ge
\left\lceil\frac{a}{2k}\right\rceil
}
\]

vertices.

### Proof

CMR453 applied to the local block gives levels in `[-k_C,0]`. Sum the level
counts and use CMR457--CMR458. The active vertices are partitioned among at most
`k+|\mathcal S_+|` component-level cells, so one cell has the displayed size.
∎

## 8. Three-way threshold endpoint

### Corollary CMR460 — PROVED

Fix `2\le q\le t`. At least one of the following holds.

1. **Large rollback-free block.** Some component of side at least `q` lies
   entirely in the final host.
2. **Strict small-block factorization.** Every component has side less than `q`,
   so the entire minimum rollback family factors into matching problems of side
   below `q`.
3. **Rollback-active level concentration.** The active region has `a\ge q`, and
   one active component-level cell has size at least
   \[
   \boxed{\left\lceil\frac{q}{2k}\right\rceil}.
   \]

### Proof

If a rollback-free component has size at least `q`, use the first alternative.
Otherwise, if `a<q`, every active component also has size below `q`; hence all
components have size below `q` and CMR456 gives the second alternative. If
`a\ge q`, apply CMR459. ∎

The first branch gives executable flexibility without restored edges. The second
is exact host decomposition. Only the third branch requires new geometric
analysis.

## 9. Transfer to repeated ancestor-return edges

### Corollary CMR461 — PROVED

Let `H` be any matchable balanced bipartite host and let `B\subseteq E(H)` be a
marked edge set. Define

\[
k_B=\min_{N\in\operatorname{PM}(H)}|N\cap B|.
\]

The minimum-`B` perfect matchings admit all conclusions of CMR453--CMR460 with
`B` in place of the deleted-edge set and `k_B` in place of `k`.

For one compatible recursive ancestor-reset slot, take `B` to be the old edges
which that slot can return after all current hard constraints have been encoded
as edge deletions. Choosing a minimum-`B` feasible state eliminates every
positive-return alternating excursion and confines repeated use of the slot to
a canonical SCC-factorized tight face.

### Proof

Repeat CMR448--CMR460 with the binary cost `c=1_B`. The arguments use only
minimum-cost matching, alternating-cycle weights, shortest-path potentials, and
strong connectivity. ∎

CMR461 does not yet prove termination of repeated ancestor resets. The remaining
task is a monotone payment for zero-cost movement inside the rollback-active
same-level cells.

## 10. Revised frontier

Cheap rollback now has an exact structural endpoint:

- potentials use only `k+1` levels;
- all minimum states factor over strongly connected exchange blocks;
- rollback cost splits additively across those blocks;
- at most `k` blocks are rollback-active;
- all active vertices occupy at most `2k` component-level cells.

For every threshold, the proof therefore reaches rollback-free flexibility,
strict small-block factorization, or a large rollback-active same-level cluster.
The immediate geometric theorem should attach a p-adic, primitive-height,
quotient, carry, Hall, prefix, or line-clean certificate to that cluster.

The same normalization now applies to each repeated compatible ancestor slot.
What remains there is payment for zero-cost motion in the marked tight face.

No all-`n` theorem is claimed here. The claims are checked in
[`scripts/verify_prime_power_tight_rollback_scc.py`](../scripts/verify_prime_power_tight_rollback_scc.py).
