# Degree-two centre-conflict components

The first Hall stage in `docs/670` selects resource-disjoint motifs. The second
stage must retain enough of their three good centres after cross-copy conflicts.
This chapter gives the exact component law when that centre-conflict graph is
bipartite and has maximum degree two.

## PP3dcm — Path and even-cycle classification

Let `H` be a finite bipartite centre-conflict graph with maximum degree at most
two. Every connected component of `H` is one of:

```text
an isolated vertex,
a finite path,
an even cycle.
```

Indeed, every finite connected graph of maximum degree two is a path or cycle,
with isolated vertices included as paths of length zero; bipartiteness forces every
cycle to have even length.

Thus the second-stage geometry can be audited componentwise once the two degree
conditions and bipartiteness are certified from coordinates.

## PP3dcn — Exact retained-centre formula

The maximum independent set of a path on `s` vertices has size `ceil(s/2)`, while
an even cycle on `s` vertices has size `s/2`. Therefore the exact number of
simultaneously retainable centres is

```text
alpha(H)
 = sum_{path components C} ceil(|C|/2)
 + sum_{even-cycle components C} |C|/2.
```

Equivalently, the exact matching or vertex-cover loss is

```text
nu(H)=tau(H)=sum_{nontrivial components C} floor(|C|/2).
```

This replaces a global matching oracle by a finite component census of vertex
counts and path/cycle types.

## PP3dco — Sharp motif-count loss budgets

If the first stage selects `q` motifs, there are `3q` candidate centres. The exact
28-centre condition is

```text
3q - nu(H) >= 28.
```

Consequently the allowed matching losses are sharp:

```text
q=10: nu(H) <= 2,
q=11: nu(H) <= 5,
q=12: nu(H) <= 8.
```

For example, with ten selected motifs, three vertex-disjoint centre-conflict edges
already obstruct the 28-centre target. With the component formula, this obstruction
is visible directly from the path and cycle census.

## Verification

`scripts/check_hall_degree_two_centre_components.py` exhausts all 74,954 labelled
bipartite graphs with partition sizes at most four. Among them, 10,172 have maximum
degree at most two. For every such graph it verifies the component classification,
the exact independent-set formula, and equality with total vertices minus matching
loss.

## Evidence boundary

This closes the second-stage calculation only after the geometric host proves that
the centre-conflict graph is bipartite and maximum-degree two. No asymptotic
coordinate motif family currently provides that graph together with enough
first-stage motifs and both restricted degree-two theorems.
