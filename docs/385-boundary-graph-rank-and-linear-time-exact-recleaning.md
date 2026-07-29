# Boundary-graph rank and linear-time exact recleaning

`docs/343` reduces target recleaning after a covered three-owner rotation to an
affine XOR system on owner variables and boundary-component variables.  Its
sparse-core algorithm enumerates at most `2^(3+q)` assignments.  The special
form of those equations is much stronger: they are precisely labelled-edge
constraints on a graph, so rank, solution count, and minimum Hamming cost are
all available in linear time.

The statements below do not prove that a useful covering rotation exists, and
they do not prove a uniform bound on the minimum recleaning cost.

## 1. The boundary constraint graph

Use the notation of `PP3bpr`.  The variables are

```text
y_t  for t in T,
x_j  for boundary components C_j of H-T.
```

Construct a labelled multigraph `Gamma=Gamma(H,T,e)` whose vertices are these
variables.  Every equation

```text
y_t xor x_j = c
```

becomes an edge between `y_t` and `x_j` labelled `c`, and every equation

```text
y_t xor y_t' = c
```

becomes an edge between the two owner vertices.  Parallel edges are retained;
they merely repeat or test the same relative parity.

Let

```text
n = |T| + b,
r = number of connected components of Gamma,
```

where isolated owner variables count as components.

### Theorem PP3bur -- PROVED / EXACT BOUNDARY-GRAPH RANK

Assume the hypotheses of `PP3bpr`, so the boundary system is feasible.  Then its
coefficient matrix over `GF(2)` has rank

```text
n-r.
```

Its solution set is an affine space of dimension `r`, and therefore contains
exactly

```text
2^r
```

solutions.  Moreover every connected component of `Gamma` contains at least one
owner vertex, so

```text
r <= |T| <= 3.
```

Consequently the complete component-local recleaning system has at most eight
solutions, independently of the number or sizes of the boundary components.

#### Proof

On one connected component, choose a root variable.  Every labelled edge fixes
the XOR difference between its endpoints.  Feasibility means that the XOR of
labels around every closed walk is zero, so propagation from the root is
well-defined.  All variables in that connected component are then determined by
one free root bit.  Thus a component with `n_i` vertices contributes rank
`n_i-1` and one affine degree of freedom.  Summing over the `r` components gives
rank `n-r` and dimension `r`.

Every component variable `x_j` is adjacent to an owner by definition of a
boundary component.  Hence every connected component contains an owner vertex,
and there are at most `|T|` connected components. ∎

## 2. Exact minimum-cost recleaning

Give each variable its owner-Hamming weight:

```text
weight(y_t) = 1,
weight(x_j) = |C_j|.
```

A feasible assignment `z` has cost

```text
cost(z)
 = sum_(t in T) z(y_t)
   + sum_j |C_j| z(x_j),
```

which is exactly the number of owner signs changed by the corresponding clean
orientation.

### Theorem PP3bus -- PROVED / LINEAR-TIME EXACT MINIMUM RECLEANING

A minimum-owner-Hamming clean target permitted by `PP3bpr` can be found in

```text
O(|V(Gamma)| + |E(Gamma)|)
```

time and linear memory.

More explicitly, propagate one feasible reference assignment `z_0`.  For a
connected component `R` of `Gamma`, let

```text
W_R = total variable weight in R,
A_R = weight of vertices assigned 1 by z_0 in R.
```

The exact minimum recleaning cost is

```text
sum_R min(A_R, W_R-A_R).
```

#### Proof

By `PP3bur`, every solution on `R` is either the propagated reference assignment
or its global complement.  Their costs are `A_R` and `W_R-A_R`.  Distinct graph
components have independent root bits, so the global minimum is the sum of the
componentwise minima.  One breadth-first or depth-first traversal both checks
consistency and accumulates `A_R,W_R`. ∎

This strictly sharpens the enumeration bound in `PP3bpu`; that exponential
algorithm remains correct but is unnecessary for this graph-structured system.
The possible obstruction is now structural cost, not computational search:
flipping one variable `x_j` may still change a large component `C_j`.

## 3. Linear-time test for changing only the rotated owners

Fix a propagated reference solution `z_0`.  Every solution on a graph component
`R` has the form

```text
z(v) = z_0(v) xor alpha_R,
```

for one component bit `alpha_R`.

### Corollary PP3but -- PROVED / EXACT `T`-ONLY PROPAGATION TEST

The reduced system with

```text
x_1=...=x_b=0
```

is feasible if and only if, inside every connected component `R` of `Gamma`, all
boundary vertices `x_j in R` receive the same reference value under `z_0`.

When boundary vertices occur in `R`, their common reference value uniquely
forces `alpha_R`.  When `R` contains only owner vertices, `alpha_R` remains free
and is chosen to minimise the number of changed owners.  Thus feasibility and
the exact minimum number of changed signs inside `T` are both computable in the
same linear traversal.

#### Proof

The condition `z(x_j)=0` is equivalent to

```text
alpha_R = z_0(x_j)
```

for every boundary vertex in `R`.  A common component bit exists exactly when
those reference values agree.  If no boundary vertex occurs, either component
bit is allowed.  The owner cost is then evaluated directly for the forced or
better of the two choices. ∎

## 4. Revised local-sign frontier

The recleaning coordinate is now completely explicit.

1. A covering successor determines a labelled boundary graph.
2. That graph has at most three affine degrees of freedom and at most eight
   feasible clean targets under component-local coupling.
3. Exact minimum owner-Hamming cost and the stricter `T`-only feasibility test
   are linear-time graph propagation problems.

The remaining asymptotic difficulty is therefore entirely structural: prove the
existence of a pair-safe or clean covering successor whose boundary graph admits
a low-cost choice, ideally with every boundary-component variable fixed to zero.
Neither global orientation optimization nor exponential boundary enumeration is
needed.

The next theorem identifier after this chapter is `PP3buu`.
