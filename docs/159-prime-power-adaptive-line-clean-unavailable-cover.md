# Adaptive line-clean forbidden matchings absorb unavailable edges or expose a small row-column cover

CMR502--CMR506 show that failure of cheap clean selection forces frozen
collateral, factorization, or a large unavailable-edge inventory.  The forbidden
matching used to define a line-clean derangement cylinder is not canonical,
however: it only has to contain the residual trace of the paid line.  This
freedom can absorb a maximum compatible matching of unavailable cells at zero
restoration cost.

After that absorption, König's theorem gives a small row-column cover for every
unavailable edge which remains allowed in the cylinder.  Thus the repeated-cell
branch is sharpened to a large freely absorbed unavailable matching or a heavy
unavailable row/column star.

Fix one compatible paid pair `Z` on a nonaxis line `L`.  Delete its two rows and
two columns and let

\[
K=K_{n,n},
\qquad n=m-2.
\]

Let `Q_L` be the partial matching consisting of all remaining cells of `L` in
`K`, and put

\[
\ell_L=|Q_L|.
\]

Before choosing an extension of `Q_L`, let

\[
B_L^0=E(K)\setminus E(G)
\]

be the currently unavailable residual edges.  Delete from `K` all source and
target vertices incident with `Q_L`, and let `J_L` be the bipartite graph formed
by the edges of `B_L^0` on the surviving vertices.  Define

\[
\nu_L=\nu(J_L),
\]

its maximum matching number.

## 1. Maximum unavailable-edge absorption

### Theorem CMR507 — PROVED

Choose a maximum matching

\[
S_L\subseteq E(J_L),
\qquad |S_L|=\nu_L.
\]

Then the partial matching

\[
Q_L\cup S_L
\]

extends to a perfect matching `F_L` of `K`.  Every such extension satisfies

\[
\boxed{
F_L\cap B_L^0
=
(Q_L\cap B_L^0)\cup S_L.
}
\]

Consequently the line-clean derangement cylinder avoiding `F_L`

1. avoids every residual cell of the paid line;
2. also avoids all edges of `S_L` without restoring them;
3. retains the exact cylinder size `D_n` and the exact derangement marginals of
   CMR330 and CMR502.

### Proof

The two partial matchings are vertex-disjoint by the definition of `J_L`, so
their union extends to a perfect matching of the complete residual bipartite
graph.

Suppose an extension edge outside `Q_L\cup S_L` were unavailable.  It is
disjoint from `Q_L` and from `S_L`, because all edges of one perfect matching
are pairwise vertex-disjoint.  It would therefore enlarge `S_L` inside `J_L`,
contradicting maximality.  The displayed identity follows.  Relabelling the
perfect matching `F_L` as the identity again gives exactly `D_n` derangements
and the same uniform allowed-edge marginal. ∎

Thus `\nu_L` unavailable edges are removed from the restoration inventory for
free, in addition to any unavailable cells already lying on the paid line.

## 2. A small cover for the remaining unavailable inventory

Let

\[
U_L=E(K)\setminus F_L
\]

and define the unavailable edges which remain allowed by

\[
B_L=U_L\cap B_L^0.
\]

### Theorem CMR508 — PROVED

There is a set `W_L` of residual source and target vertices such that

\[
\boxed{|W_L|\le2\ell_L+\nu_L}
\]

and every edge of `B_L` is incident with `W_L`.

More precisely, one may take

\[
W_L=V(Q_L)\cup C_L,
\]

where `C_L` is a minimum vertex cover of `J_L` and

\[
|C_L|=\nu_L.
\]

### Proof

By König's theorem, `J_L` has a vertex cover `C_L` of size equal to its maximum
matching number `\nu_L`.  Let `e\in B_L`.  If `e` meets a vertex of `Q_L`, it is
covered by `V(Q_L)`.  Otherwise `e` belongs to `J_L`, so it is covered by
`C_L`.  Since `Q_L` is a matching, `|V(Q_L)|=2\ell_L`. ∎

This is a structural statement about the remaining restoration inventory, not
only a cardinality estimate.

## 3. Absorption or a heavy unavailable row/column

For a residual vertex `v`, let

\[
d_{B_L}(v)
=
|\{e\in B_L:v\in e\}|.
\]

### Corollary CMR509 — PROVED

If `B_L` is nonempty, some residual row or column vertex satisfies

\[
\boxed{
d_{B_L}(v)
\ge
\left\lceil
\frac{|B_L|}{2\ell_L+\nu_L}
\right\rceil.
}
\]

Fix an integer threshold `s\ge1`.  At least one of the following holds.

1. **Free unavailable matching absorption.**
   \[
   \boxed{\nu_L\ge s.}
   \]
   The forbidden matching absorbs at least `s` pairwise compatible unavailable
   edges.
2. **Small-cover concentration.**
   \[
   \boxed{
   |W_L|
   \le
   2\ell_L+s-1.
   }
   \]
   If `B_L` is nonempty, one row or column contains at least
   \[
   \boxed{
   \left\lceil
   \frac{|B_L|}{2\ell_L+s-1}
   \right\rceil
   }
   \]
   remaining unavailable edges.

When `2\ell_L+s-1=0`, the second branch forces `B_L=\varnothing`.

### Proof

CMR508 covers `B_L` by at most `2\ell_L+\nu_L` vertices.  Some cover vertex
meets at least the average number of covered edges.  If `\nu_L<s`, substitute
`\nu_L\le s-1`.  The zero-denominator case has an empty cover, so it cannot
cover a nonempty edge set. ∎

A heavy vertex gives an unavailable-cell star in one source row or one target
column.  The edges of that star are distinct and carry exact full-token
incidence.

## 4. Adaptive weighted selection endpoint

Choose the line-clean cylinder using the adaptive `F_L` from CMR507, and define
`S_L`, `A_L`, and the restoration count exactly as in CMR502--CMR504 but with the
new allowed unavailable set `B_L`.

### Theorem CMR510 — PROVED

Fix integers `q,s\ge1` and a real `0<\alpha<1`.  If there is no anchored outside
continuation and no line-clean completion with

\[
X_L=0,
\qquad
r_L<q,
\]

then at least one of the following holds.

1. **Frozen collateral.**
   \[
   \boxed{
   S_L
   \ge
   \frac{11}{30}(1-\alpha).
   }
   \]
2. **Free absorption.**
   \[
   \boxed{\nu_L\ge s.}
   \]
3. **Heavy unavailable row/column.** Some residual vertex `v` satisfies
   \[
   \boxed{
   d_{B_L}(v)
   \ge
   \left\lceil
   \frac{\alpha q(n-1)}{2\ell_L+s-1}
   \right\rceil.
   }
   \]

The third branch is required only when the denominator is positive.  Its
distinct unavailable edges have exact labelled full-token incidence at least

\[
\boxed{
(p+1)(h-1)
\left\lceil
\frac{\alpha q(n-1)}{2\ell_L+s-1}
\right\rceil
}
\]

when the parent side is `t=p^h`.

### Proof

Apply the one-line form of CMR504 to the adaptive cylinder.  If the frozen term
is below its threshold, then

\[
|B_L|\ge\alpha q(n-1).
\]

Apply CMR509.  In the nonabsorption branch, divide this lower bound by the cover
size `2\ell_L+s-1`.  The token identity is CMR413 applied to the distinct star
edges. ∎

The unavailable inventory can therefore be made geometrically one-dimensional
unless the forbidden matching absorbs a large compatible portion of it.

## 5. Rooted-arm and bottleneck endpoint

### Corollary CMR511 — PROVED

For every rooted secant-star arm of CMR494 and every bottleneck paid pair of
CMR496, choose the residual forbidden matching adaptively as in CMR507.  For any
`q,s\ge1` and `0<\alpha<1`, at least one of the following endpoints is
available.

1. an anchored outside continuation;
2. a line-clean completion destroying the designated target conflict, creating
   no candidate-only replacement triple, and restoring fewer than `q` edges;
3. a minimum restoration footprint of size at least `q`, giving the forced-core
   factorization of CMR499;
4. frozen CMR334 rank-zero/rank-one collateral mass;
5. a matching of at least `s` unavailable residual cells absorbed for free into
   the forbidden matching;
6. a heavy unavailable-cell star in one residual row or column, with the degree
   and token mass supplied by CMR510.

### Proof

CMR507 preserves the universal line-clean cylinder and its equal size, so the
weighted selection theorem CMR503 applies unchanged.  Use CMR499 for expensive
minimum restoration and CMR510 for the remaining cheap but nonimproving branch.
CMR494 and CMR496 provide the paid pairs. ∎

The generic repeated-unavailable-edge branch of CMR505 is therefore replaceable
by an adaptive endpoint: unavailable cells are absorbed as a compatible
matching, or the remaining inventory is concentrated in a source-row or
target-column star.  The latter is suitable for Hall-wall, prefix, quotient,
carry, protected-reserve, and envelope analysis.

The immediate frontier is to classify a large unavailable-cell star by its
first-separation depth and direction, or show that repeated free absorption
consumes a finite reserve of forbidden-matching slots across parent epochs.

No all-`n` theorem is claimed.  Maximum absorption, König covers, heavy-star
arithmetic, and adaptive selection are checked in
[`scripts/verify_prime_power_adaptive_line_clean_cover.py`](../scripts/verify_prime_power_adaptive_line_clean_cover.py).
