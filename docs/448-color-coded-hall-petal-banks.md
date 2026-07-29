# Color-coded Hall petal banks

`docs/442` decomposes the residual Hall incidence graph into matchings. This
chapter uses the full proper edge coloring as a target marker. The color tag
turns every residual edge into a private reverse target and gives a sharp
source-degree load bound.

## 1. Proper residual colors

Let `G=(X,Y;E)` be a bipartite residual incidence multigraph and let

```text
Delta=max(max_x d(x), max_y d(y)).
```

By bipartite edge coloring, the edges admit a proper coloring with colors
`1,...,Delta`.

### Theorem PP3cce -- PROVED / TAGGED-TARGET UNIQUENESS

For a proper edge coloring, every tagged target `(y,c)` has at most one incident
source edge.

#### Proof

Two edges incident to the same target cannot receive the same color in a proper
edge coloring. ∎

## 2. Uniform private-petal kernel

### Theorem PP3ccf -- PROVED / DEGREE-RECIPROCAL LOAD

Suppose every source has residual degree at least `d`. Let a source choose one
of its incident residual edges uniformly and retain the tagged target `(y,c)`.
Then the reverse load is at most

```text
1/d.
```

More precisely, the load on the unique tagged edge from source `x` is
`1/d(x)`.

#### Proof

`PP3cce` leaves at most one predecessor for each tagged target. Its contribution
is exactly the uniform row probability `1/d(x)<=1/d`. ∎

## 3. Compressed colors

Let `kappa` map the proper colors to shorter recovered code labels, and suppose
every code fiber has size at most `g`.

### Theorem PP3ccg -- PROVED / COLOR-COMPRESSION BOUND

If the final target retains `(y,kappa(c))`, then the uniform residual-edge kernel
has reverse load at most

```text
g/d.
```

If a larger load is observed, then either some source has degree below `d`, the
edge coloring is not proper, or one recovered code label contains more than `g`
colors.

#### Proof

At a fixed target and code label, at most one edge of each color contributes.
There are at most `g` colors in the fiber, and every contribution is at most
`1/d`. The failure statement is the contrapositive. ∎

## Frontier consequence

The entire common-core residual graph is now one repair reservoir rather than a
choice of a single matching bank. Exact color recovery gives load `1/d`; a
short ambiguous color code costs only its actual fiber size.
