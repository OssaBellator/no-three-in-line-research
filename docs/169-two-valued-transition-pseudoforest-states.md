# Two-valued transition pseudoforest states

PP3zq--PP3zv leave one exact support object at a fixed captive centre: outside a
high-choice exceptional set of size `m^(1/2+o(1))`, every middle index has at most
two safe predecessors, or symmetrically at most two safe successors.

A family of one- and two-element choice sets is not an arbitrary matching
problem. Regard every two-element set as an edge and every singleton as a loop on
the predecessor ground set. An injective choice exists exactly when this labelled
multigraph is a pseudoforest. Minimal failure is therefore one bicyclic component.
When the pseudoforest criterion holds, every unicyclic component has exactly two
states, while every tree component has one state for each possible unused root.
Since the transition branch has `N-o(N)` middle indices in a ground set of size at
most `N`, only `o(N)` tree components occur; the bulk state space is Boolean.

The injective choice is a large partial endpoint matching, not automatically a
complete endpoint permutation. Its unused left and right resource sets both have
size `o(N)`. The final completion problem is therefore an explicit residual host
of sublinear order.

## 1. The labelled predecessor multigraph

Fix the predecessor version; the successor version is transposed. Let `P` be a
set of middle indices outside the high-choice core, and for each `p in P` let

```text
1 <= |A(p)| <= 2
```

be its safe predecessor set. Every member of `A(p)` is distinct from `p` and the
fixed centre `c`.

Let

```text
U=union_{p in P} A(p).
```

Build a labelled multigraph `K_A` on vertex set `U`:

- if `A(p)={u,v}` with `u!=v`, add one edge `uv` labelled by `p`;
- if `A(p)={u}`, add one loop at `u` labelled by `p`.

Parallel edges and loops are retained because distinct middle indices are
distinct choice obligations.

An injective predecessor assignment is a map

```text
f:P->U
```

such that `f(p) in A(p)` for every `p` and the values `f(p)` are pairwise
distinct.

## 2. Exact pseudoforest criterion

### Theorem PP3zw -- PROVED

The family `{A(p):p in P}` has an injective predecessor assignment if and only if
every connected subgraph of `K_A` has at most as many labelled edges as vertices.
Equivalently, every connected component of `K_A` is a pseudoforest component: a
tree or a unicyclic multigraph.

#### Proof

Hall's theorem says that an injective choice exists exactly when

```text
|J| <= |union_{p in J} A(p)|
```

for every subfamily `J subseteq P`.

The edges labelled by `J` form a submultigraph whose nonisolated vertex set is
exactly `union_{p in J} A(p)`. Thus Hall is exactly the assertion that every
edge-induced submultigraph has at most as many edges as nonisolated vertices.
This holds if and only if every connected subgraph has edge count at most vertex
count, which is the standard pseudoforest condition. ∎

Thus failure of the two-valued transition relation is already an exact Hall core
with cyclomatic excess.

## 3. Minimal failure is bicyclic

### Proposition PP3zx -- PROVED

Suppose the injective predecessor assignment fails, and choose an inclusion-minimal
label set `J subseteq P` with

```text
|J| > |union_{p in J} A(p)|.
```

Then its labelled multigraph is connected and satisfies

```text
|E|=|V|+1.
```

Every proper labelled subgraph is a pseudoforest. Consequently the underlying
minimal obstruction is a circuit of the bicircular matroid: one of

1. a theta graph, consisting of three internally disjoint paths with the same two
   ends;
2. a tight handcuff, consisting of two cycles meeting in one vertex;
3. a loose handcuff, consisting of two vertex-disjoint cycles joined by one path;

with the usual loop and parallel-edge degeneracies allowed.

#### Proof

If the minimal violating subgraph had two edge-containing connected components,
one component would already have more edges than vertices, contradicting
minimality. Hence it is connected.

Minimality gives `|E|-1 <= |V|` after deleting any labelled edge, while violation
gives `|E|>|V|`; therefore `|E|=|V|+1`. Every proper labelled subgraph satisfies
the pseudoforest inequalities by minimality. The connected minimal graphs of
cyclomatic number two are exactly the theta and the two handcuff types, including
multigraph degeneracies. ∎

So the failed bounded-choice branch is not a diffuse near-complete table. It is
one explicit bicyclic Hall support core.

## 4. Exact states of a pseudoforest component

Orient each labelled edge toward the predecessor selected for its label. An
injective assignment is exactly an orientation in which every ground vertex has
indegree at most one; a loop contributes indegree one at its vertex.

### Proposition PP3zy -- PROVED

Let `C` be a connected pseudoforest component.

1. If `C` is a tree with `v` vertices, then it has exactly `v` injective states.
   They are indexed by the unique unused root `r`; every edge is oriented away
   from `r`.
2. If `C` is unicyclic and its unique cycle has length at least two, then it has
   exactly two injective states. Every tree attached to the cycle is oriented away
   from the cycle, and the cycle is oriented in either cyclic direction.
3. If the unique cycle is a loop, the component has exactly one injective state;
   the loop selects its vertex and every attached tree edge is oriented away from
   that vertex.

#### Proof

In a tree, `|E|=|V|-1`, so every valid orientation has exactly one indegree-zero
vertex and all other vertices have indegree one. Once that root is specified,
induction from the leaves forces every edge away from the root, and that
orientation is valid.

In a unicyclic component, `|E|=|V|`, so every vertex must have indegree one.
Leaf-stripping forces every attached tree edge away from the cycle. On a cycle of
length at least two, indegree one at each cycle vertex leaves exactly the two
cyclic orientations. For a loop, the loop is forced and the attached trees are
again forced outward. ∎

The nontrivial flexible states are therefore exact alternating-cycle variables.

## 5. Boolean bulk and small root surplus

Let `t(K_A)` be the number of tree components containing at least one labelled
edge. Put

```text
delta_A=|U|-|P|.
```

### Corollary PP3zz -- PROVED

If the pseudoforest criterion holds, then

```text
t(K_A) <= delta_A.
```

More precisely, after discarding isolated ground vertices,

```text
t(K_A)=|U|-|P|.
```

Hence when

```text
|P|=N-o(N),   |U|<=N,
```

there are only `o(N)` tree components. Every remaining nontrivial component is a
Boolean unicyclic variable, apart from forced loop components.

#### Proof

For each tree component, `|V|-|E|=1`; for each unicyclic component the difference
is zero. Summing over all edge-containing components gives

```text
|U|-|P|=t(K_A).
```

If isolated vertices were retained in `U`, they only increase the left side and
give the displayed inequality. The asymptotic conclusion follows immediately. ∎

Thus the two-valued transition branch consists of a Boolean cycle bank plus only
a sublinear collection of root variables.

## 6. Exact residual completion interface

Let `V` be the full endpoint-index set of size `N`. For one injective assignment
`f`, prescribe the endpoint arcs

```text
F_f={f(p)->p : p in P}.
```

These arcs have distinct tails and distinct heads, so they form a bipartite partial
matching. Put

```text
L_f=V\f(P),
R_f=V\P,
d=N-|P|.
```

Then `|L_f|=|R_f|=d`.

### Theorem PP3aaa -- PROVED AS A RESIDUAL-HOST INTERFACE

For every pseudoforest state `f`:

1. in the complete coordinate host, every bijection `L_f->R_f` completes `F_f` to
   a full endpoint permutation, giving exactly `d!` residual completions;
2. in an allowed endpoint host `G`, the completions are exactly the perfect
   matchings of the residual bipartite host `G[L_f,R_f]`;
3. when `|P|=N-o(N)`, this residual host has order `d=o(N)`;
4. after one residual matching is fixed, every source-invalid pattern touches at
   most three pseudoforest component variables, and every insertion-shadow or
   dynamic-`Xi` term touches at most two;
5. if the residual matching is selected jointly, every remaining pattern is
   ranked by the number of additional residual arcs it requires, exactly as in
   PP3ze and PP3zu.

The nonloop unicyclic bulk is Boolean. The only non-Boolean predecessor variables
are the `o(N)` tree roots from PP3zz, together with the explicit residual matching
on `o(N)` resources.

#### Proof

The unused tail and head sets have equal size because `F_f` contains `|P|`
compatible arcs. A full completion is therefore exactly a bijection between the
unused sets; imposing an allowed host restricts this bijection to a residual
perfect matching.

A source obstruction contains at most three newly selected endpoint cells, so
after the residual cells are fixed it depends on at most three pseudoforest
component states. Unary and binary paid incidences depend on at most one or two
selected cells. When residual cells are random or selected jointly, condition on
`f` and classify each pattern by its number of additional residual arcs. ∎

Thus the pseudoforest theorem reduces the large transition table to a Boolean
component bank plus a residual matching problem of sublinear order. It does not
by itself assert that this residual host is matchable or source-valid.

## 7. Revised transition endpoint

### Corollary PP3aab -- PROVED

The bounded-choice alternatives of PP3zv reduce to one of:

1. **Bicyclic Hall core:** one theta or handcuff support obstruction in the safe
   predecessor or successor relation.
2. **Boolean alternating-cycle bank:** the safe relation is a pseudoforest and its
   unicyclic bulk gives exact two-state variables.
3. **Sublinear root surplus:** at most `o(N)` tree components retain a choice of
   unused predecessor or successor root.
4. **Sublinear residual host:** the selected safe arcs leave an exact endpoint
   matching problem on `o(N)` unused resources.
5. **Paid finite-state concentration:** after residual completion, the resulting
   rank-at-most-three source term or unary/binary cost reaches the cycle-credit
   scale.
6. **Clean-chain branch:** the support-ranked paid criterion PP3zu applies before
   the bounded-choice reduction.

A generic two-valued relation and a diffuse near-complete transition star are no
longer independent frontiers. The exact unresolved support objects are a minimal
bicyclic Hall core, a paid Boolean cycle bank, the sublinear tree-root surplus, or
the sublinear residual host.
