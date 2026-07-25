# Two-valued transition pseudoforests and Boolean cycle banks

PP3zq--PP3zv leave one exact support obstruction at a fixed captive centre. After
reserving at most `m^(1/2+o(1))` high-choice middle indices, every remaining
middle index has at most two source-valid predecessor choices, or transposed
successor choices.

A family of sets of size at most two has a complete graph-theoretic description.
Represent every two-choice set by an edge and every one-choice set by a loop. An
injective choice exists exactly when every connected component is a pseudoforest.
A minimal failure is a connected bicyclic multigraph. If an injective choice does
exist, the remaining perfect-matching state space is not an arbitrary sparse-host
space: every flexible alternating component is one directed cycle with exactly
two states.

Thus the two-valued transition branch reduces to a bicyclic Hall core or an exact
Boolean cycle bank with rank-at-most-three source clauses and a quadratic paid
objective.

## 1. Conditioning on the high-choice core

Let `V` be the endpoint-index set in one controller pool and let `c in V` be the
fixed captive centre. Suppose the predecessor alternative of PP3zv holds; the
successor alternative is transposed.

Let

```text
E={p: p has at least three source-valid predecessors}.
```

Then

```text
|E|=O(m^(1/2+o(1))).
```

First choose distinct predecessor resources for the indices in `E`. If this is
impossible, Hall's theorem already gives a deficient set contained entirely in
`E`, hence a support core of size `O(m^(1/2+o(1)))`.

Condition on any injective assignment of `E`, delete the used predecessor
resources, and let:

```text
P = remaining middle indices,
L = remaining predecessor resources.
```

Then `|P|=|L|`, and every `p in P` has a source-valid choice set

```text
A(p) subseteq L,
|A(p)|<=2.
```

An empty `A(p)` is an immediate unit obstruction. Below assume every choice set is
nonempty.

## 2. The choice multigraph

Construct a multigraph `Gamma` on vertex set `L` with one labelled edge `e_p` for
each `p in P`:

1. if `A(p)={u,v}` with `u!=v`, let `e_p` join `u` and `v`;
2. if `A(p)={u}`, let `e_p` be a loop at `u`.

Choosing one predecessor for every middle index is equivalent to orienting each
nonloop edge toward its selected endpoint, with a loop selecting its unique
vertex. Injectivity means that every vertex receives at most one selected edge.

### Proposition PP3zw -- PROVED

The residual choice family has an injective representative if and only if every
connected component `C` of `Gamma` satisfies

```text
|E(C)|<=|V(C)|.
```

Equivalently, `Gamma` is a pseudoforest: every connected component contains at
most one cycle, where a loop is a cycle of length one and two parallel edges form
a cycle of length two.

#### Proof

An injective representative orients every edge toward a selected endpoint with
indegree at most one. Summing indegrees in one component gives

```text
|E(C)|<=|V(C)|.
```

Conversely, a connected component with fewer edges than vertices is a tree after
ignoring isolated vertices. Choose a root and orient every edge away from the
root; each nonroot vertex receives exactly one edge and the root receives none.

A connected component with equally many edges and vertices is unicyclic. Orient
its unique cycle cyclically and orient every attached tree away from the cycle.
Every vertex then receives exactly one edge. Loops and parallel-edge cycles obey
the same construction. Taking the union over components gives an injective
representative. ∎

This is Hall's theorem specialized exactly to two-valued choice sets.

## 3. Minimal Hall failure is bicyclic

Let `Q subseteq P` be inclusion-minimal with

```text
|N(Q)|<|Q|,
```

where `N(Q)` is the union of the predecessor choices of indices in `Q`.

### Theorem PP3zx -- PROVED

For every such minimal deficient family:

```text
|Q|=|N(Q)|+1.
```

The multigraph formed by the edges `{e_p:p in Q}` on `N(Q)` is connected, has
minimum degree at least two, and has cyclomatic number two:

```text
|E|-|V|+1=2.
```

After suppressing degree-two vertices, its core is one of the standard connected
bicyclic types:

1. a theta graph: three internally disjoint paths between two branch vertices;
2. a figure-eight: two cycles sharing one branch vertex;
3. a barbell: two cycles joined by one path.

Loops and parallel edges are allowed as degenerate cycles.

#### Proof

Minimality gives, for every `p in Q`,

```text
|Q|-1<=|N(Q\{p})|<=|N(Q)|.
```

Together with `|N(Q)|<|Q|`, this forces `|Q|=|N(Q)|+1`.

If the induced multigraph were disconnected, one connected component would have
more edges than vertices and its edge labels would give a smaller deficient
subfamily, contrary to minimality.

If a vertex had degree one, remove its unique incident labelled edge. The vertex
would disappear from the neighbourhood at the same time, leaving a smaller
family with the same positive deficiency. This again contradicts minimality.
Thus the minimum degree is at least two.

Connectedness and `|E|=|V|+1` give cyclomatic number two. Suppress every maximal
path whose internal vertices have degree two. The remaining connected multigraph
has total degree excess

```text
sum_v (deg(v)-2)=2.
```

Hence it has either one degree-four branch vertex or two degree-three branch
vertices. These are respectively the figure-eight and the theta/barbell cases. ∎

Therefore failure of predecessor matching is an explicit bicyclic transition
support core, not a diffuse near-complete role table.

## 4. Exact Boolean factorization when a matching exists

Assume `Gamma` is a pseudoforest and fix one injective representative. This is a
perfect matching `M` between the residual predecessor resources `L` and middle
indices `P`. Relabel the two sides so that `M` is the diagonal matching.

Form the alternating digraph `D_M` as in PP3tn: put an arc `i->j` for every allowed
predecessor assignment from left index `i` to right index `j`, and ignore the
diagonal loops when computing nontrivial strong components.

### Theorem PP3zy -- PROVED

Every nontrivial strongly connected component of `D_M` is one simple directed
cycle. Its induced bipartite host has exactly two perfect matchings:

1. the diagonal reference state;
2. the cyclic-shift state using every nonloop arc of the directed cycle.

All global perfect matchings are obtained by choosing independently between these
two states in every nontrivial component and retaining every forced diagonal edge
outside them.

#### Proof

Every right vertex has degree at most two in the predecessor host. One incident
edge is its reference matching edge, so every vertex of `D_M` has at most one
incoming nonloop arc.

Inside a nontrivial strong component, every vertex has at least one incoming and
one outgoing internal arc. The incoming bound makes the internal indegree exactly
one at every vertex. The number of internal arcs therefore equals the number of
vertices. Strong connectivity then forces internal outdegree exactly one as well,
so the component is one directed cycle.

No other internal allowed edge exists, because it would create a second incoming
nonloop arc at its head. Thus the component host consists exactly of the diagonal
matching and one cyclic-shift matching. These are its only two perfect matchings.
The componentwise factorization is PP3to, or follows directly by taking the union
of independently chosen component matchings. ∎

This is stronger than a generic alternating-SCC finite-state decomposition: every
flexible residual component is Boolean.

## 5. Source and paid normalization

Introduce one Boolean variable for every nontrivial directed-cycle component,
with value zero for the diagonal state and value one for the cyclic shift.

Every selected endpoint arc is then either:

1. forced;
2. present under one literal of one cycle variable;
3. absent under that literal.

Consequently:

- every source-invalid pattern involving at most three selected arcs becomes an
  exact forbidden clause on at most three Boolean variables;
- every unary or binary `Xi` insertion weight becomes a pseudo-Boolean function
  of degree at most two;
- state-dependent removal credit is affine in the cycle variables;
- deterministic invalidity is represented by an empty clause or an infinite
  constant cost.

The existing paid first-moment, local-lemma, Ramsey, and exact finite-CSP
interfaces therefore apply without introducing a new matching distribution.

### Corollary PP3zz -- PROVED

After reserving the `O(m^(1/2+o(1)))` high-choice middle indices, a fixed-centre
two-valued transition core has one of the following exact forms.

1. **Small exceptional Hall core:** the high-choice indices themselves have no
   injective predecessor assignment.
2. **Bicyclic choice core:** the residual two-valued multigraph contains a minimal
   theta, figure-eight, or barbell Hall obstruction.
3. **Paid Boolean cycle bank:** an injective predecessor assignment exists and all
   remaining matching freedom is an exact bank of independent two-state directed
   cycles, with rank-at-most-three source clauses and a degree-at-most-two net paid
   objective.
4. **Forced deterministic obstruction:** every residual matching contains a fixed
   source-invalid pattern or has nonpositive available removal credit.

Thus a generic two-valued outer relation is no longer a frontier. The remaining
transition problem is conversion of a small Hall core, a bicyclic algebraic
support core, or concentrated source/paid weight in the explicit Boolean cycle
bank.
