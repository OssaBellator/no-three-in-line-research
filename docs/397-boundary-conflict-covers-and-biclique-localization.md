# Boundary conflict covers and biclique localization

`docs/396` shows that the exact recleaning cost is, up to the three owner bits,
the minority weight of the two propagated boundary phases.  This chapter gives
that minority weight an exact covering interpretation and extracts a complete
bipartite obstruction whenever it is large.

The statements do not prove that the resulting conflict bank is geometrically
rare in the prime-patching rotation family.

## 1. The boundary conflict graph

Fix one connected boundary-graph component `R` and a propagated reference
assignment.  Define a bipartite graph `K_R` with vertex classes

```text
X_R^0={x_j:z_0(x_j)=0},
X_R^1={x_j:z_0(x_j)=1}.
```

Join every vertex of `X_R^0` to every vertex of `X_R^1`, and give `x_j` weight
`|C_j|`.  Thus `K_R` is the complete bipartite graph on the two boundary phase
classes.  Its edges are exactly the opposite-phase boundary pairs counted by
`E_R` in `PP3bvz`.

### Theorem PP3bwc -- PROVED / EXACT BOUNDARY-CONFLICT COVER

The minimum vertex-cover weight of `K_R` is

```text
q_R=min(B_R^0,B_R^1).
```

Equivalently, `q_R` is the minimum total size of boundary components that must be
removed so that all remaining boundary vertices in `R` have one propagated
phase.

For the whole boundary graph, the minimum such deletion weight is exactly

```text
Q=sum_R q_R.
```

#### Proof

The complement of a vertex cover is an independent set.  In a complete bipartite
graph, every independent set lies wholly in one side, unless one side is empty.
Hence every vertex cover contains all vertices of `X_R^0` or all vertices of
`X_R^1`.  Since all weights are positive, a minimum cover is exactly the lighter
side, of weight `q_R`.

Deleting a vertex cover removes every opposite-phase pair, so the surviving
boundary vertices have at most one phase.  Conversely, if both phases survive,
the surviving pair between them is an uncovered conflict edge.  Distinct graph
components are independent, so the global optimum is the sum. ∎

Combined with `PP3bvy`, the exact recleaning cost is within an additive three of
this boundary-conflict cover number.

## 2. A low-cost-or-large-biclique dichotomy

Assume every boundary component represented in `R` has size at most `L`, where
`L>0`.  Let

```text
n_R^a=|X_R^a|.
```

### Theorem PP3bwd -- PROVED / BOUNDED-WEIGHT BICLIQUE EXTRACTION

If

```text
q_R >= Q_0,
```

then

```text
n_R^0 >= ceil(Q_0/L),
n_R^1 >= ceil(Q_0/L).
```

Consequently `K_R` contains a complete bipartite subgraph

```text
K_(h,h),
```

where

```text
h=ceil(Q_0/L).
```

Every one of its `h^2` conflict pairs has a parity-odd labelled path witness of
length at most six.

#### Proof

Both phase masses are at least `q_R`, hence at least `Q_0`.  A phase class with
fewer than `ceil(Q_0/L)` vertices has total weight strictly below `Q_0`, because
each vertex has weight at most `L`.  Therefore both classes have at least `h`
vertices.  Since the conflict graph is complete between the classes, arbitrary
`h`-subsets form `K_(h,h)`.  Apply `PP3bwb` to every cross pair. ∎

This is a structural alternative with no probabilistic loss: either the boundary
minority is small, or there is a large two-sided bank of bounded parity witnesses.
The paths need not be edge-disjoint; overlap of their owner vertices is the next
localization question.

## 3. Weighted conflict packing dual

Let `F_R` be the set of conflict edges of `K_R`.  A fractional conflict packing is
a family of nonnegative numbers `lambda_e` satisfying

```text
sum_(e incident to x_j) lambda_e <= |C_j|
```

for every boundary vertex.

### Theorem PP3bwe -- PROVED / EXACT FRACTIONAL CONFLICT PACKING

The maximum total fractional conflict-packing weight is exactly

```text
q_R.
```

In particular, large boundary impurity supplies a dual certificate of the same
weight, supported entirely on opposite-phase pairs and therefore on six-edge
parity witnesses.

#### Proof

Weak duality between fractional matching and weighted vertex cover gives an upper
bound `q_R` by `PP3bwc`.  For the matching lower bound, assume without loss of
generality that

```text
B_R^0 <= B_R^1.
```

Regard each vertex weight as divisible supply.  Send the full supply `|C_x|` of
each `x in X_R^0` to vertices of `X_R^1`, splitting arbitrarily, until all left
supply is exhausted.  This is possible because the total right capacity is at
least the total left supply and every cross edge exists.  The resulting edge
loads satisfy all vertex capacities and have total weight `B_R^0=q_R`. ∎

This dual form may be more convenient for averaging: rather than select a
minority side canonically, one may transport its full weight across a complete
pair-conflict bank.

## 4. Consequence for asymptotic recleaning

For every covering rotation, exactly one of the following holds at any chosen
threshold `Q_0`:

1. the total boundary conflict-cover weight is below `Q_0`, and the complete
   recleaning cost is below `Q_0+3`;
2. some boundary-graph component carries a weighted conflict packing whose total
   is at least its share of `Q_0`;
3. under a boundary-component cap `L`, that component contains a two-sided
   complete bank of bounded parity witnesses at scale `Q_0/L`.

The remaining geometric task is therefore sharpened: prove that pair-safe
covering rotations avoid large complete banks of parity-odd boundary paths, or
show that such a bank yields a different improving rotation.

The next theorem identifier after this chapter is `PP3bwf`.
