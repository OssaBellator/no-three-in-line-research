# Exact symmetry quotient for two-permutation switch graphs

## Status

This note keeps AC as the sole active research track and proves AC5ob--AC5oe. It gives an exact quotient for finite two-permutation switch searches under the eight square symmetries and interchange of the two layers.

The quotient changes only finite-state enumeration. It does not identify geometrically different states outside the declared symmetry group and does not by itself prove that any particular sublevel component is exhausted.

## Setup

A state is an ordered pair

\[
v=(R,B)
\]

of disjoint permutation graphs on `[1,n]^2`. A legal switch swaps two row images in one layer and is admitted only when both inserted cells avoid the opposite layer.

Let `D_4` be the order-eight symmetry group of the square. Let `C_2` interchange the red and blue layers, and put

\[
G=D_4\times C_2.
\]

The real triple potential is

\[
\Phi(v)=\sum_L\binom{|(R\cup B)\cap L|}{3}.
\]

## AC5ob -- switch-graph automorphism group -- PROVED

Every element of `G` maps a pair of disjoint permutation graphs to another such pair. It preserves:

1. the number of selected cells;
2. the row and column multiplicities;
3. disjointness of the layers;
4. real collinearity and therefore `Phi`;
5. legal two-row-switch adjacency.

Consequently `G` acts by automorphisms on the complete physical switch graph and on every potential sublevel graph.

### Proof

A square symmetry is an affine isometry of the integer board, so it preserves collinearity. A permutation graph remains a permutation graph under reflections, rotations and coordinate interchange; coordinate interchange replaces a permutation by its inverse. A two-row image swap becomes another two-row image swap after every square symmetry. Layer interchange simply exchanges the two identical operation types. Disjointness and legality are point-set properties and are therefore preserved. QED.

## AC5oc -- canonical orbit representative -- PROVED

Order the complete two-layer permutation words lexicographically. Define

\[
\operatorname{can}(v)=\min_{g\in G}g(v).
\]

Then:

1. `can(v)` belongs to the orbit of `v`;
2. `can(can(v))=can(v)`;
3. `can(v)=can(w)` exactly when `v,w` lie in the same `G`-orbit;
4. `Phi(can(v))=Phi(v)`.

Thus one finite string is a complete fail-closed orbit key.

### Proof

The group is finite and every orbit has a unique least word. Idempotence and orbit equivalence follow immediately. Potential invariance is AC5ob. QED.

## AC5od -- quotient reachability and path lifting -- PROVED

Let `X` be any `G`-invariant state set, for example a potential sublevel

\[
X_B=\{v:\Phi(v)\le B\}.
\]

Construct the quotient graph whose vertices are canonical orbit representatives and whose edges are induced by physical legal switches.

For any initial state `v` and any `G`-invariant target set `T`,

\[
\boxed{
v\leadsto T\text{ inside }X
\iff
\operatorname{can}(v)\leadsto\operatorname{can}(T)
\text{ inside }X/G.
}
\]

Every quotient path lifts to a physical path after choosing one representative of its first vertex.

### Proof

Projection of a physical path gives a quotient path. Conversely, a quotient edge has a physical representative `x->y`. If the currently lifted state is `g(x)`, automorphism invariance gives the physical edge `g(x)->g(y)`. Induct along the quotient path. Invariance of `X` and `T` keeps the lift inside the declared sets and ends in the target orbit. QED.

## AC5oe -- exact quotient exhaustion certificate -- PROVED

For a potential-defined lower target, breadth-first search may canonicalize every accepted successor before insertion. The search returns exactly one of:

1. a lower-potential orbit, which lifts to a physical route;
2. complete exhaustion of the quotient component, proving that the raw component contains no lower-potential state;
3. a typed implementation failure such as a malformed permutation, layer collision, non-idempotent key or transformed-edge mismatch.

No raw orbit multiplicity is needed for the reachability conclusion.

### Proof

Breadth-first search exhausts the finite quotient component. AC5od identifies quotient and physical reachability. The listed failures are precisely the checks required before orbit keys or quotient edges may be trusted. QED.

## Deterministic audit

Run:

```text
python scripts/verify_ac_switch_symmetry_quotient.py
```

The audit exhausts the ordered disjoint two-permutation state space at `n=5` and checks:

- ordered disjoint states: `5,280`;
- canonical representatives checked: `5,280`;
- orbit images checked: `79,936`;
- transformed physical edges checked: `36,000`;
- raw-versus-quotient reachability comparisons: `16`;
- summed raw component states: `76,224`;
- summed quotient component states: `5,234`.

Every comparison gives exactly the same orbit set and the same answer for every tested lower-potential target.

## Current p=31 use

The explicit three-triple `p=31` frontier of AC5nz is being enumerated inside `Phi<=9` with this quotient. The search remains fail-closed until it either returns a lower-potential orbit or exhausts its complete quotient component. Intermediate queue sizes are computational progress records, not theorems.

## Remaining frontier

1. Complete the `p=31` barrier-nine quotient component.
2. If exhausted, search the quotient at barrier ten and lift the first lower path.
3. Store group elements on predecessor edges when a shortest lifted path, rather than only a reachability certificate, is required.
4. Apply the quotient to subsequent two-, one- and zero-triple checkpoints.
5. Combine orbit keys with the physical AC rank and exceptional-event ledgers without merging non-symmetric owner or source records.

AC6 and the general no-three-in-line conjecture remain open.
