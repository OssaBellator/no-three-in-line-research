# Two-valued transition pseudoforest states

PP3zq--PP3zv leave one exact support object at a fixed captive centre: outside a
high-choice exceptional set of size `m^(1/2+o(1))`, every possible middle index
has at most two safe predecessors, or symmetrically at most two safe successors.

The local paths

```text
r -> p -> c
```

are alternative states sharing the centre `c`; they are not arcs to install
simultaneously. The correct use of the two-valued relation is therefore to choose
one safe predecessor for every possible middle so as to build a large, low-overlap
bank of alternative local path states. A family of one- and two-element choice
sets admits such an injective selection exactly when its labelled choice
multigraph is a pseudoforest. Minimal failure is one bicyclic Hall core.

When the pseudoforest criterion holds, its component orientations parameterize
possible designs of the alternative-state bank: unicyclic components have two
design states and tree components are indexed by an unused root. One injective
design has overlap degree at most two away from `c`, so a linear subbank has
pairwise disjoint noncentral resources. One local path from that subbank may then
be fixed and completed by a residual single-cycle permutation.

## 1. The labelled predecessor multigraph

Fix the predecessor version; the successor version is transposed. Let `P` be a
set of possible middle indices outside the high-choice core, and for each `p in P`
let

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

An injective predecessor design is a map

```text
f:P->U
```

such that `f(p) in A(p)` for every `p` and the values `f(p)` are pairwise
distinct. It produces the alternative path bank

```text
H_f={f(p)->p->c : p in P}.
```

Only one member of `H_f` is selected in the final endpoint permutation.

## 2. Exact pseudoforest criterion

### Theorem PP3zw -- PROVED

The family `{A(p):p in P}` has an injective predecessor design if and only if
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
count, which is the pseudoforest condition. ∎

## 3. Minimal failure is bicyclic

### Proposition PP3zx -- PROVED

Suppose the injective predecessor design fails, and choose an inclusion-minimal
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

Thus failure is one explicit bicyclic Hall support core, not a diffuse transition
table.

## 4. Exact designs of a pseudoforest component

Orient each labelled choice edge toward the predecessor selected for its label.
An injective design is exactly an orientation in which every ground vertex has
indegree at most one; a loop contributes indegree one at its vertex.

### Proposition PP3zy -- PROVED

Let `C` be a connected pseudoforest component.

1. If `C` is a tree with `v` vertices, then it has exactly `v` injective designs.
   They are indexed by the unique unused root `r`; every edge is oriented away
   from `r`.
2. If `C` is unicyclic and its unique cycle has length at least two, then it has
   exactly two injective designs. Every tree attached to the cycle is oriented
   away from the cycle, and the cycle is oriented in either cyclic direction.
3. If the unique cycle is a loop, the component has exactly one injective design;
   the loop selects its vertex and every attached tree edge is oriented away from
   that vertex.

#### Proof

In a tree, `|E|=|V|-1`, so every valid orientation has exactly one indegree-zero
vertex and all other vertices have indegree one. Once that root is specified,
induction from the leaves forces every edge away from the root.

In a unicyclic component, `|E|=|V|`, so every vertex has indegree one.
Leaf-stripping forces every attached tree edge away from the cycle. On a cycle of
length at least two, the two cyclic orientations are the only possibilities. A
loop is forced. ∎

These are design choices for the alternative-state bank; they are not simultaneous
endpoint-permutation variables.

## 5. Boolean bulk of the bank-design space

Let `t(K_A)` be the number of tree components containing at least one labelled
edge. Put

```text
delta_A=|U|-|P|.
```

### Corollary PP3zz -- PROVED

After discarding isolated ground vertices,

```text
t(K_A)=|U|-|P|.
```

Hence when

```text
|P|=N-o(N),   |U|<=N,
```

there are only `o(N)` tree components. Every remaining nontrivial design component
is a two-state unicyclic component, apart from forced loop components.

#### Proof

For each tree component, `|V|-|E|=1`; for each unicyclic component the difference
is zero. Sum over all edge-containing components. ∎

Thus optimization over injective bank designs has a Boolean bulk plus a sublinear
root surplus.

## 6. Linear bounded-overlap path bank

Fix one injective design `f`. Associate to each `p in P` the unordered pair of
noncentral indices

```text
E_p={f(p),p}.
```

Because the middles `p` are distinct and the selected predecessors `f(p)` are
distinct, every endpoint index belongs to at most two of the pairs `E_p`: at most
once as a selected predecessor and at most once as a middle.

### Theorem PP3aaa -- PROVED

The alternative path bank `H_f` contains a subbank `H'_f` of size at least

```text
|P|/3
```

such that distinct paths in `H'_f` are vertex-disjoint outside the common centre
`c`.

#### Proof

The graph with edge set `{E_p:p in P}` has maximum degree at most two, so it is a
disjoint union of paths, cycles, and possible doubled edges. Greedily choose one
edge and delete it together with all incident edges. Each choice deletes at most
three edges. The selected matching has size at least `|P|/3`. The corresponding
two-arc paths share only `c`. ∎

When `|P|=N-o(N)`, this gives `Omega(N)` alternative clean local path states with
pairwise disjoint auxiliary resources.

## 7. Joint local-state and single-cycle completion

For `h=(r,p,c) in H'_f`, fix the two arcs

```text
r->p,   p->c.
```

Contract this directed path to one ordered object. On the full `N`-index pool,
there are exactly

```text
(N-3)!
```

single-cycle permutations containing `h`.

For every source-invalid or paid pattern remaining after `h` is fixed, let `u` be
the number of additional random arcs it requires. Let `S_h,u` be its count or
nonnegative weight, `0<=u<=3`. Let `J_h` be the expected remaining insertion cost
and let `R_h>=R_*>0` be the exact removal credit.

### Theorem PP3aab -- PROVED

Conditional on `h`, every compatible set of `u` additional arcs has probability
at most

```text
1/(N-3)_u,
```

unless it creates a proper directed cycle with the fixed path, in which case its
probability is zero.

If

```text
(1/|H'_f|) sum_{h in H'_f} [
  sum_{u=0}^3 K^u S_h,u/(N-2)^u
  + J_h/R_*
] < 1,
```

then one local path state and one conditional single-cycle completion are
source-admissible and have insertion cost below removal credit.

#### Proof

Contract the two-arc path. There are `N-2` cyclic objects and `(N-3)!` directed
cyclic orders. Each additional compatible arc that does not create a proper cycle
contracts two current objects, giving the displayed cylinder probability.

Choose `h` uniformly from `H'_f`, then choose a uniform conditional single cycle.
The displayed expression bounds the expected number of source violations plus
normalized paid cost. An outcome below one has no source-invalid event and cost
below `R_*<=R_h`. ∎

The denominator `(N-2)^u` is a harmless weaker normalization of the exact falling
factorial for fixed `u` after adjusting the absolute constant `K`.

## 8. Revised transition endpoint

### Corollary PP3aac -- PROVED

The bounded-choice alternatives of PP3zv reduce to one of:

1. **Bicyclic Hall core:** one theta or handcuff obstruction in the safe
   predecessor or successor relation.
2. **Linear alternative-state bank:** a pseudoforest design yields `Omega(N)` clean
   two-arc paths sharing only the captive centre.
3. **Paid path-state completion:** the joint source and cost average PP3aab lies
   below the path's removal credit.
4. **Path-bank concentration:** the support-ranked source or insertion cost is at
   the credit scale on the linear alternative-state bank.
5. **Bank-design concentration:** optimization over the injective design is trapped
   in its Boolean unicyclic bulk or sublinear tree-root surplus.
6. **Clean five-index chain branch:** PP3zu applies before the bounded-choice
   reduction whenever both outer roles retain at least three choices.

A generic two-valued relation and a diffuse near-complete transition star are no
longer independent frontiers. The remaining support objects are a minimal
bicyclic Hall core or paid concentration on a linear, auxiliary-resource-disjoint
path-state bank.
