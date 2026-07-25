# Same-level rollback motion is column-polarized or has a mixed exchange cycle

CMR462--CMR466 reduce every minimum rollback or minimum marked-edge state to a
sparse cross-level skeleton and independent perfect matchings inside residual
potential levels. This chapter identifies the exact structure of one such
same-level residual host.

For a tight edge which stays in one potential level, the contraction weight is
zero. Therefore its binary marked cost equals the cost of the base matching
edge at its right endpoint. Markedness is consequently determined by the
right column, not by the chosen source. Every local matching uses the same
number of marked edges, and the only remaining freedom is which source subset
is assigned to the marked columns.

That source-subset freedom has an exact alternating-cycle certificate. It is
unique precisely when no zero-cost alternating cycle contains both marked and
unmarked right columns. Otherwise one mixed-colour cycle flip changes the
source subset while preserving the minimum marked cost.

Use the setting of CMR465. Fix one feasible cross-level skeleton and one
potential level `s`. Let

\[
H=(L,R;E)
\]

be the corresponding balanced residual same-level host, and let

\[
P=\{p_j=\ell_jr_j:j\in J\}
\]

be one perfect matching of `H`, after relabelling the residual right endpoints
by their base-matching indices. Put

\[
\beta(j)=c(p_j)\in\{0,1\}.
\]

The right vertices split as

\[
R_1=\{r_j:\beta(j)=1\},
\qquad
R_0=\{r_j:\beta(j)=0\}.
\]

## 1. Right-endpoint polarization

### Theorem CMR467 — PROVED

Every edge `\ell_ir_j\in E(H)` satisfies

\[
\boxed{c(\ell_ir_j)=\beta(j).}
\]

Consequently every perfect matching `Q` of `H` has the same marked cost

\[
\boxed{c(Q)=|R_1|.}
\]

### Proof

All vertices and edges of `H` stay in one potential level. The tight level
equation therefore has value zero:

\[
0
=
\phi(j)-\phi(i)
=
c(\ell_ir_j)-c(p_j).
\]

This proves the edge identity. Every perfect matching uses each right vertex
once, so its cost is the sum of `\beta(j)` over all right vertices. ∎

Thus the marked-edge budget is fixed columnwise throughout the residual face.

## 2. Exact source-split decomposition

For a perfect matching `Q` of `H`, define

\[
X(Q)
=
\{\ell_i\in L:Q(\ell_i)\in R_1\}.
\]

Let `\mathfrak X(H)` be the family of source sets `X\subseteq L` such that

\[
|X|=|R_1|,
\]

`H[X,R_1]` has a perfect matching, and `H[L\setminus X,R_0]` has a perfect
matching.

### Theorem CMR468 — PROVED

The local matching family factors as the disjoint union

\[
\boxed{
\operatorname{PM}(H)
\cong
\bigsqcup_{X\in\mathfrak X(H)}
\left(
\operatorname{PM}(H[X,R_1])
\times
\operatorname{PM}(H[L\setminus X,R_0])
\right).
}
\]

### Proof

Every perfect matching `Q` determines `X(Q)`. Its marked edges form a perfect
matching from `X(Q)` to `R_1`, while its unmarked edges form a perfect matching
from the complementary sources to `R_0`.

Conversely, the union of one perfect matching in each displayed factor is a
perfect matching of `H`. The source set sent to `R_1` is uniquely recoverable,
so the union is disjoint. ∎

The remaining same-level state variable is exactly the feasible marked-column
source set.

## 3. Mixed-colour cycle criterion

Relative to `P`, contract the matching edges. A nonmatching edge
`\ell_ir_j` becomes the directed arc `i\to j`. Call a directed or alternating
cycle **mixed-colour** when its matching/right vertices include both values of
`\beta`.

### Theorem CMR469 — PROVED

For another perfect matching `Q` of `H`, one has

\[
X(Q)\ne X(P)
\]

if and only if at least one alternating cycle of `P\triangle Q` is
mixed-colour.

Consequently,

\[
\boxed{\mathfrak X(H)=\{X(P)\}}
\]

if and only if the contraction digraph contains no mixed-colour directed cycle.

### Proof

The symmetric difference `P\triangle Q` is a disjoint union of alternating
cycles. On one such cycle, flipping cyclically permutes the right vertices
among its source vertices. The set of sources assigned to marked right
vertices is unchanged exactly when the cyclic colour word is invariant under a
one-step cyclic shift. That occurs exactly when all right vertices on the
cycle have the same colour.

Thus `X(Q)` differs from `X(P)` precisely when one component cycle is mixed.
Conversely, flipping any mixed-colour directed cycle produces a perfect
matching with a different source split. ∎

Every mixed-colour flip moves at least one source into the marked-column class
and at least one source out of it.

## 4. Strong-component endpoint

Let `D_P(H)` be the matching-contraction digraph relative to `P`.

### Corollary CMR470 — PROVED

Exactly one of the following holds.

1. **Colour-separated factorization.** Every strongly connected component of
   `D_P(H)` is colour-homogeneous. Then `\mathfrak X(H)=\{X(P)\}` and
   \[
   \boxed{
   \operatorname{PM}(H)
   \cong
   \operatorname{PM}(H[X(P),R_1])
   \times
   \operatorname{PM}(H[L\setminus X(P),R_0]).
   }
   \]
2. **Mixed exchange block.** Some strongly connected component contains both
   colours. Then it contains a mixed-colour directed cycle of length at most
   its number of vertices. Flipping that cycle preserves minimum cost and
   changes the source set assigned to restored columns.

### Proof

Every arc inside a strongly connected component lies on a directed cycle. If
a component contains both colours, a directed path between the two colour
classes contains an arc crossing the colour boundary; that arc lies on a
simple directed cycle in the component, which is mixed-colour. CMR469 gives
the second alternative.

If every component is colour-homogeneous, every directed cycle is
colour-homogeneous, so CMR469 makes the source split unique. Apply CMR468 to
that unique set. ∎

The first branch is strict two-colour host decomposition. The second supplies
an explicit zero-cost move rather than an arbitrary same-level state change.

## 5. Transfer to rollback and ancestor-return faces

### Corollary CMR471 — PROVED

For every residual level factor in CMR465, and more generally for every binary
marked-edge face in CMR461, the remaining zero-cost motion has the CMR470
alternative:

1. exact factorization into the sources assigned to marked and unmarked right
   endpoints; or
2. a mixed-colour zero-cost alternating cycle which changes the marked-source
   assignment without increasing marked cost.

For a repeated compatible ancestor-return slot, the marked right class records
the base endpoints whose selected edges are returned old edges. Positive-
return excursions and cross-level motion are already bounded by CMR461--CMR466;
only repeated mixed-colour cycle motion remains as an unfunded local dynamic.

### Proof

Apply CMR467--CMR470 to each residual same-level host, with the binary marked set
used in CMR461. ∎

## 6. Revised frontier

The minimum marked-edge normal form now has four exact layers.

1. SCC factorization localizes marked dependence.
2. A sparse balanced skeleton contains every cross-level edge.
3. Conditional on the skeleton, the face factors by potential level.
4. Inside one level, markedness is right-column polarized and the source split
   either factors or changes along an explicit mixed-colour zero-cost cycle.

The active geometric frontier is therefore a family of mixed-colour
alternating cycles inside one same-level block. The next theorem should either
extract many low-overlap such cycles for simultaneous resampling or show that
cycle overlap concentrates on a prefix, primitive-height, quotient, carry,
Hall, reserve, or envelope signature. If no mixed block exists, the entire
minimum face decomposes into lower-dimensional marked and unmarked matching
problems.

No all-`n` theorem is claimed here. Right-endpoint polarization, source-split
factorization, and the mixed-cycle criterion are checked in
[`scripts/verify_prime_power_same_level_colour_split.py`](../scripts/verify_prime_power_same_level_colour_split.py).
