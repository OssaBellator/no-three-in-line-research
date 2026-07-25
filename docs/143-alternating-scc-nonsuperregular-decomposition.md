# Alternating-SCC decomposition of matchable non-superregular hosts

The superregular endpoint theorem does not cover every matchable source-safe
host.  Fixing one perfect matching exposes the exact remaining freedom.  Orient
an allowed off-diagonal edge from its left matching index to its right matching
index.  Every alternative perfect matching decomposes into directed cycles, so
it may differ from the reference matching only inside nontrivial strongly
connected components.

These components are disjoint equal-margin finite-state variables.  Trivial
components are forced matching edges.  Thus matchable non-superregularity is
reduced to an exact alternating-block CSP or a forced-credit core.

## 1. Directed graph relative to a perfect matching

Let \(G=(L,R;E)\) be a balanced bipartite graph with a fixed perfect matching

\[
M=\{\ell_i r_i:i\in[n]\}.
\]

Form a directed graph \(D_M\) on \([n]\) by placing an arc

\[
i\longrightarrow j
\]

whenever

\[
\ell_i r_j\in E.
\]

The diagonal loops \(i\to i\) correspond to the reference matching and may be
ignored when computing nontrivial strong components.

### Proposition PP3tn -- PROVED

Every perfect matching \(N\) of \(G\) defines a permutation
\(\pi_N\in S_n\) satisfying

\[
i\longrightarrow\pi_N(i)
\]

in \(D_M\) for every \(i\).  Every nontrivial cycle of \(\pi_N\) lies inside one
strongly connected component of \(D_M\).

#### Proof

The edge of \(N\) incident with \(\ell_i\) has the form
\(\ell_i r_{\pi_N(i)}\), and matching uniqueness makes \(\pi_N\) a permutation.
Its cycle arcs give directed paths in both directions between every two vertices
on one permutation cycle, so the cycle lies in one strongly connected component.
∎

## 2. Edges between strong components are never selected

Let

\[
C_1,\ldots,C_s
\]

be the strongly connected components of \(D_M\).

### Theorem PP3to -- PROVED

Every perfect matching of \(G\) is the disjoint union of perfect matchings on the
induced component hosts

\[
G[C_a,C_a]
\qquad(a\in[s]).
\]

In particular, an allowed edge \(\ell_i r_j\) with \(i,j\) in different strong
components belongs to no perfect matching of \(G\).

#### Proof

By PP3tn, every nontrivial permutation cycle of a perfect matching is contained
in one strong component.  Fixed points also remain in their own component.
Hence \(\pi_N\) maps every component to itself, and the selected edges split into
componentwise perfect matchings.

Conversely, the union of one perfect matching from each induced component host
covers every global left and right vertex exactly once. ∎

Thus the condensation DAG contains allowed edges that are irrelevant to all
perfect matchings; they may be deleted without changing the matching state
space.

## 3. Forced and flexible components

Call a component **trivial** when it contains one vertex and no nontrivial
self-cycle.  Call it **flexible** otherwise.

### Proposition PP3tp -- PROVED

A matching edge \(\ell_i r_i\in M\) belongs to every perfect matching of \(G\) if
and only if \(i\) is a trivial component of \(D_M\).

Every flexible component has at least two perfect matchings of its induced host.

#### Proof

If \(i\) lies on a directed cycle of length at least two, switching the
corresponding alternating cycle produces a perfect matching omitting
\(\ell_i r_i\).  Thus a nontrivial component is not forced.

Conversely, if some perfect matching omits \(\ell_i r_i\), the permutation cycle
containing \(i\) is nontrivial and gives a directed cycle through \(i\).  Hence
\(i\) lies in a nontrivial strong component.

The reference matching and one directed-cycle switch give two states in every
flexible component. ∎

This is the exact forced-edge test; degree or regularity estimates are not
needed.

## 4. Exact finite-state component bank

For flexible component \(C_a\), let

\[
\Omega_a
\]

be the finite set of all perfect matchings of \(G[C_a,C_a]\).  Regard one state
as its set of endpoint cells.

### Theorem PP3tq -- PROVED

The flexible components form an equal-margin finite-state bank with disjoint
supports.

1. Every global perfect matching of \(G\) is obtained by choosing one state from
   each \(\Omega_a\) and retaining every trivial forced edge.
2. Every choice of component states preserves all endpoint row and column
   margins.
3. Every no-three violation gives an exact bad box involving at most three
   flexible components.
4. Every controller-shadow insertion term depends on at most two flexible
   components.

#### Proof

The first two statements are PP3to.  Distinct components use disjoint left and
right resources.  Apply the multistate exact-CSP construction PP3bh--PP3bi.
A collinear triple meets at most three component supports, and a blocker pair
meets at most two. ∎

Thus the entire matchable host has an exact rank-at-most-three CSP and an exact
unary/binary paid objective even without superregularity.

## 5. Credited endpoints and local movement

Let \(c_i\ge0\) be the designated removal credit attached to reference endpoint
\(\ell_i r_i\).  For component state \(\omega\in\Omega_a\), define

\[
C_a(\omega)
=
\sum_{i\in C_a:\,\omega(i)\ne i}c_i.
\]

### Proposition PP3tr -- PROVED

The exact removal credit of a global component-state assignment is at least

\[
\sum_aC_a(\omega_a),
\]

with equality for the designated-credit subpotential.  A credited endpoint in a
trivial component contributes zero to every possible trade inside \(G\).

#### Proof

A component state moves endpoint \(i\) exactly when its matching permutation is
not fixed at \(i\).  Moving it destroys its designated old incidence, while a
fixed endpoint retains it.  Sum the distinct designated units.  Trivial
components have only the fixed state by PP3tp. ∎

Thus forced credited edges are a genuine obstruction in the chosen host, not an
artifact of the reference matching.

## 6. Exact paid component criterion

### Corollary PP3ts -- PROVED

A source-admissible strict improvement exists whenever the component CSP has an
assignment \((\omega_a)\) satisfying

\[
\mathcal I(\omega)<\mathcal C(\omega),
\]

where the insertion cost is the exact unary/binary component-state objective and
\(\mathcal C\) includes the moved designated credits PP3tr.

The first-moment and variable-local-lemma criteria PP3bj--PP3bl and PP3oy--PP3oz
apply to arbitrary product measures on the component state sets.

#### Proof

Saturation and exact source validity are PP3tq.  Apply the paid endpoint identity
PP3id or PP3kx. ∎

## 7. Complete non-superregular endpoint

### Corollary PP3tt -- PROVED

A matchable source-safe endpoint host has one of the following exact forms.

1. **Flexible component bank:** a positive amount of credited mass lies in
   nontrivial alternating strong components.  Conversion is an explicit finite-
   state rank-three CSP with unary/binary paid cost.
2. **Forced-credit core:** a positive amount of credited mass lies on trivial
   components and cannot be moved by any perfect matching of the host.
3. **Mixed form:** delete the forced part and apply the component bank to the
   flexible credited mass.

Thus matchable but non-superregular is no longer an unstructured graph class.
Its remaining obstruction is forced credited matching edges or concentrated
component-CSP geometry/cost.