# Maximum-mobility alternating-cycle banks

PP3ul leaves unbounded flexible alternating components as one endpoint of the
matchable non-superregular branch.  In the resource-bank application every
selected reference endpoint carries one designated credit unit.  In that
full-credit setting, maximize the number of reference edges moved by a perfect
matching.

The symmetric difference with the reference matching is already a collection of
vertex-disjoint alternating cycles.  If the maximum moved set is small, that set
meets every alternating cycle.  Thus a large component is not an arbitrary large
state variable: it gives either a large binary cycle bank or a small mobility hub
through which every change must pass.

## 1. Moved vertices and directed cycle packings

Let \(C\) be one alternating strong component of the normalized host, with
reference matching

\[
M_C=\{\ell_i r_i:i\in C\}.
\]

Assume every index \(i\in C\) carries one designated credit unit.  Let \(D_C\)
be the directed graph from PP3tn, and ignore its diagonal loops when speaking of
cycles.

For a component perfect matching \(N\), let

\[
\operatorname{mov}(N)
=
\{i\in C:N(i)\ne i\}.
\]

### Proposition PP3um -- PROVED

The nontrivial cycles of the permutation associated with \(N\) are pairwise
vertex-disjoint directed cycles of \(D_C\), and their vertex union is exactly
\(\operatorname{mov}(N)\).

Conversely, switching any family of pairwise vertex-disjoint directed cycles of
\(D_C\) and retaining every other reference edge gives a perfect matching of the
component host.

#### Proof

The first statement is the permutation-cycle decomposition in PP3tn.  A vertex
is moved exactly when it belongs to a nontrivial permutation cycle.

For the converse, one directed cycle

\[
i_1\to i_2\to\cdots\to i_s\to i_1
\]

replaces the reference edges \(\ell_{i_j}r_{i_j}\) by
\(\ell_{i_j}r_{i_{j+1}}\).  This preserves every used left and right resource.
Pairwise vertex-disjoint cycles use disjoint resources, so their switches may be
united. ∎

## 2. Exact maximum mobility

Define

\[
\nu(C)
=
\max_N|\operatorname{mov}(N)|,
\]

where the maximum is over component perfect matchings.

### Theorem PP3un -- PROVED

The quantity \(
u(C)\) is exactly the maximum number of vertices covered by a
family of pairwise vertex-disjoint nontrivial directed cycles of \(D_C\).

It is also the optimum of the ordinary assignment problem on the component host
with edge weight

\[
w_{ij}=\mathbf 1_{i\ne j}.
\]

Hence maximum mobility is polynomial-time computable and has the standard
integral assignment dual certificate.

#### Proof

The cycle-packing equality is PP3um in both directions.  A perfect matching has
assignment weight equal to the number of off-diagonal selected edges, which is
exactly the number of moved indices.  Integrality is the bipartite perfect-
matching polytope theorem. ∎

The same optimization accepts arbitrary nonnegative designated credits by using
\(w_{ij}=c_i\mathbf1_{i\ne j}\).  The feedback-set conclusion below uses the
full-support unit-credit case.

## 3. Binary alternating-cycle bank

Choose a maximum-mobility matching \(N_*\).  Write its nontrivial permutation
cycles as

\[
\Gamma_1,\ldots,\Gamma_s.
\]

### Proposition PP3uo -- PROVED

The cycles \(\Gamma_a\) form a resource-disjoint binary equal-margin state bank.
For each \(a\), state zero keeps the reference edges on \(\Gamma_a\), and state
one switches the directed cycle.

1. Every choice of the \(s\) binary states is a component perfect matching.
2. The all-one state is \(N_*\).
3. Cycle \(a\) supplies exactly \(|V(\Gamma_a)|\) designated credit units in
   state one.
4. The total all-one credit is
   
   \[
   \sum_a|V(\Gamma_a)|=\nu(C).
   \]
5. Relative to the fixed source outside the cycles, no-three conditions are exact
   bad boxes of rank at most three and insertion shadow is an exact unary/binary
   cost on the cycle variables.

#### Proof

The first four statements follow from PP3um and disjointness of permutation
cycles.  Distinct cycles use disjoint left and right resources.  The final
statement is the exact finite-state construction PP3tq applied to the binary
cycle supports. ∎

Thus a large unbounded component with linear mobility has already been converted
to the same paid binary-bank interface as the rectangle and bounded-component
branches.

## 4. A maximum moved set is a feedback set

Put

\[
U=\operatorname{mov}(N_*).
\]

### Theorem PP3up -- PROVED

The nonloop digraph \(D_C-U\) is acyclic.  Equivalently, every nontrivial
alternating cycle of the component meets \(U\).

#### Proof

If \(D_C-U\) contained a directed cycle \(\Gamma\), then \(\Gamma\) would be
vertex-disjoint from every cycle of \(N_*\).  Switching \(\Gamma\) together with
all cycles of \(N_*\) would produce a perfect matching moving

\[
|U|+|V(\Gamma)|>|U|,
\]

contrary to maximality of \(N_*\). ∎

Hence

\[
\tau_{\rm fvs}(D_C)\le\nu(C),
\]

where loops are ignored and \(	au_{m fvs}\) is directed feedback-vertex-set
size.  No equality is asserted.

## 5. Hub-path normal form

### Proposition PP3uq -- PROVED

Every component perfect matching differs from the reference matching along at
most \(|U|\) nontrivial cycles, and every such cycle meets \(U\).

After deleting the vertices of \(U\) from those permutation cycles, what remains
is a collection of pairwise vertex-disjoint directed paths in the acyclic graph
\(D_C-U\), whose endpoints attach to vertices of \(U\).

Thus every matching state is an exact path system routed through the mobility
hub \(U\).

#### Proof

Theorem PP3up forces every nontrivial permutation cycle to meet \(U\).  The
cycles are vertex-disjoint, so there are at most \(|U|\) of them.  Removing their
hub vertices breaks each directed cycle into directed path segments contained
in \(D_C-U\).  Distinct permutation cycles and segments remain vertex-disjoint.
∎

The statement is combinatorial, not asymptotic: it gives an exact state-space
normal form for every low-mobility component.

## 6. Quantitative component dichotomy

### Corollary PP3ur -- PROVED

For every \(0<\delta<1\), a fully credited alternating component of size \(n\)
has one of the following forms.

1. **Large cycle-bank form:**
   
   \[
   \nu(C)\ge\delta n.
   \]
   
   Then PP3uo gives a resource-disjoint binary alternating-cycle bank with total
   designated credit at least \(\delta n\).
2. **Small mobility-hub form:**
   
   \[
   |U|=\nu(C)<\delta n,
   \]
   
   and every alternating cycle, hence every nontrivial matching change, is routed
   through the hub \(U\) as in PP3uq.

#### Proof

Choose \(N_*\) and \(U\) as above and split according to the displayed
inequality.  Apply PP3uo in the first case and PP3up--PP3uq in the second. ∎

Therefore unbounded alternating SCC size is no longer itself an obstruction.  A
large component supplies either linear paid cycle credit or a sublinear
alternating-cycle transversal.  The remaining low-mobility object is a
hub-routed path-system geometry/cost concentration, analogous to the earlier
source-star and witness-pencil endpoints.