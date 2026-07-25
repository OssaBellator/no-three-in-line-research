# Mixed-colour zero-cost cycles pack, concentrate, or leave a colour-separated residual

CMR467--CMR471 reduce the remaining zero-cost motion in one same-level marked
face to mixed-colour directed cycles in the matching-contraction digraph. This
chapter gives that cycle family a finite combinatorial endpoint. Cyclic colour-
boundary arcs admit canonical short witness cycles. Those witnesses either pack
vertex-disjointly, concentrate through one exchange vertex, or are sparse enough
that deleting their tails leaves a colour-separated residual matching problem.

Use the notation of CMR467--CMR471. Thus

\[
H=(L,R;E)
\]

is a balanced same-level host of side `m`,

\[
P=\{p_j=\ell_jr_j:1\le j\le m\}
\]

is a perfect matching, and

\[
\beta(j)=c(p_j)\in\{0,1\}.
\]

Let `D=D_P(H)` be the matching-contraction digraph: every nonmatching edge
`\ell_ir_j` is represented by the arc `i\to j`.

## 1. Cyclic colour-boundary arcs

Call an arc `i\to j` a **colour-boundary arc** when

\[
\beta(i)\ne\beta(j).
\]

Call it **cyclic** when it lies on a directed cycle of `D`. Let

\[
\mathcal B
=
\{i\to j:\beta(i)\ne\beta(j),\ j\leadsto i\},
\qquad
B=|\mathcal B|.
\]

### Theorem CMR472 — PROVED

The digraph `D` contains a mixed-colour directed cycle if and only if

\[
\boxed{B>0.}
\]

Every mixed-colour directed cycle contains at least two arcs of `\mathcal B`.
Conversely, every arc of `\mathcal B` lies on a mixed-colour directed cycle.

### Proof

A directed cycle whose vertex colours are not constant must cross from colour
zero to colour one and later cross back, so it contains at least two colour-
boundary arcs. Every arc on that cycle is cyclic.

Conversely, if `a=i\to j` belongs to `\mathcal B`, there is a directed path
from `j` back to `i`. The arc followed by a simple such path is a directed
cycle. Since the arc crosses the colour classes, that cycle is mixed. ∎

Thus mixed motion is indexed by concrete boundary arcs rather than by arbitrary
pairs of optimal states.

## 2. Canonical short witness cycles

For every

\[
a=i\to j\in\mathcal B,
\]

choose a shortest directed path

\[
Q_a:j\leadsto i
\]

and let

\[
\Gamma_a=a\cup Q_a.
\]

### Theorem CMR473 — PROVED

Each `\Gamma_a` is a simple mixed-colour directed cycle containing at most `m`
vertices. The indexed witness family

\[
\mathfrak G=\{\Gamma_a:a\in\mathcal B\}
\]

has exactly `B` members when counted with its boundary-arc labels, even when one
underlying cycle witnesses several boundary arcs.

### Proof

A shortest directed path may be chosen simple. It cannot contain its terminal
vertex `i` before the last step, so adjoining `i\to j` gives a simple directed
cycle. It is mixed because `\beta(i)\ne\beta(j)`, and a simple cycle in an
`m`-vertex digraph uses at most `m` vertices. The indexing statement is the
definition of `\mathfrak G`. ∎

The labels matter: concentration of many witnesses may come from many distinct
colour-boundary arcs even when some of their return geometry coincides.

## 3. Vertex packing versus witness concentration

For a contraction vertex `v`, define its witness multiplicity

\[
\mu(v)
=
|\{a\in\mathcal B:v\in V(\Gamma_a)\}|.
\]

### Theorem CMR474 — PROVED

Fix an integer

\[
\Delta\ge2.
\]

At least one of the following holds.

1. **Witness concentration.** Some contraction vertex satisfies
   \[
   \boxed{\mu(v)\ge\Delta.}
   \]
2. **Vertex-disjoint mixed-cycle packing.** The canonical family contains at
   least
   \[
   \boxed{
   r
   \ge
   \left\lceil
   \frac{B}{m(\Delta-1)}
   \right\rceil
   }
   \]
   pairwise vertex-disjoint mixed cycles.

### Proof

Assume the first alternative fails. Greedily select one remaining witness cycle
and discard every witness meeting it. A selected cycle has at most `m` vertices,
and each of its vertices belongs to at most `\Delta-1` witnesses. Therefore one
greedy selection discards at most

\[
m(\Delta-1)
\]

labelled witnesses, including itself. Starting from `B` witnesses gives the
displayed packing bound. ∎

This is a genuine low-overlap versus concentration theorem. No geometric
assumption is used.

## 4. Simultaneous zero-cost resampling

### Corollary CMR475 — PROVED

Let

\[
\Gamma_1,\ldots,\Gamma_r
\]

be pairwise vertex-disjoint mixed cycles in `D`. Their corresponding alternating
cycles in `H` may be flipped independently. The `2^r` subsets of the cycle
family produce `2^r` distinct perfect matchings of `H` and `2^r` distinct
marked-column source sets.

If two such states differ on exactly `s` of the chosen cycles, their source sets
differ in at least

\[
\boxed{2s}
\]

sources.

### Proof

Vertex-disjoint contraction cycles use disjoint matching edges and disjoint
nonmatching edges, so their alternating flips commute. Different subsets give
different perfect matchings.

On one mixed cycle, the cyclic shift of right endpoints changes the set of
sources assigned to marked right columns by CMR469. A nonconstant cyclic binary
word has at least two colour transitions, so the source-set symmetric difference
on that cycle has size at least two. Disjoint cycles act on disjoint source sets;
the differences therefore add. ∎

Thus the packing branch supplies an executable simultaneous move, not merely a
large abstract family of cycles.

## 5. Sparse boundary deletion and the three-way endpoint

Let

\[
Z
=
\{i:\text{some }i\to j\in\mathcal B\}
\]

be the set of tails of cyclic colour-boundary arcs.

### Theorem CMR476 — PROVED

One has

\[
\boxed{|Z|\le B,}
\]

and the residual host obtained by deleting the matching pairs indexed by `Z`
contains no mixed-colour directed cycle. Consequently its perfect matching
family has the colour-separated factorization of CMR470.

More quantitatively, fix integers

\[
q\ge1,
\qquad
\Delta\ge2.
\]

At least one of the following holds.

1. **Sparse mixed interface.** `B<q`. Deleting fewer than `q` matching pairs
   leaves a colour-separated residual host.
2. **Exchange-vertex concentration.** Some vertex lies in at least `\Delta`
   canonical mixed-cycle witnesses.
3. **Simultaneous mixed-cycle batch.** There are at least
   \[
   \boxed{
   \left\lceil
   \frac{q}{m(\Delta-1)}
   \right\rceil
   }
   \]
   pairwise vertex-disjoint mixed cycles, and hence that many independently
   flippable zero-cost exchanges.

### Proof

Certainly `|Z|\le B`. Suppose a mixed cycle survived after deleting `Z`. By
CMR472 it would contain a cyclic colour-boundary arc `i\to j`. Its tail `i`
belongs to `Z`, a contradiction. CMR470 then gives the residual colour
factorization.

For the quantitative statement, use the first alternative when `B<q`. If
`B\ge q`, apply CMR474. Its packing bound is at least the displayed expression
with `q` in place of `B`. ∎

The sparse branch localizes every source-split interaction to fewer than `q`
matching positions. The packing branch supplies simultaneous resampling. The
concentration branch identifies one matching position through which many
distinct boundary-arc witnesses pass.

## 6. Revised frontier

The zero-cost marked-face obstruction now has an exact finite form.

- Positive-cost excursions have already been removed.
- Cross-level motion uses at most `2k` edges.
- Inside one level, absence of mixed cycles gives colour factorization.
- Mixed cycles now either pack into a simultaneous batch, concentrate through
  one exchange vertex, or disappear after deleting a sparse matching-pair
  interface.

The immediate geometric task is to interpret the exchange-vertex concentration
branch. Many canonical cycles through one matching position should force a
prefix fan, primitive-height cluster, quotient/carry concentration, Hall wall,
reserve bottleneck, or envelope expansion. The sparse-interface branch may also
be integrated into recursive host decomposition.

No all-`n` theorem is claimed here. The boundary criterion, canonical witnesses,
packing bound, simultaneous flips, and sparse-deletion endpoint are checked in
[`scripts/verify_prime_power_mixed_cycle_packing.py`](../scripts/verify_prime_power_mixed_cycle_packing.py).
