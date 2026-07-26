# The full side-six grid has twelve physical one-layer target-response traps

CMR1302--CMR1309 replace extension enumeration by the exact family of response
matchings avoiding the fixed opposite layer and one target cell.  On the complete
standard `6 x 6` grid, this policy almost always finds an immediate lower state.
The exceptions have a precise finite form.

This chapter is restricted to the full standard coordinate grid, its translations
and common affine scalings.  It does not classify scattered residual side-six
factors.

## 1. Complete standard-grid state stock

### Theorem CMR1310 -- PROVED BY COMPLETE FINITE ENUMERATION

There are

\[
\boxed{190800}
\]

ordered disjoint permutation pairs and

\[
\boxed{67950}
\]

physical saturated states on the standard `6 x 6` grid.  Exactly 116 ordered states
and 50 physical states are clean.  The remaining 190684 ordered states are dirty.

The maximum physical triple potential is forty.

### Proof

Enumerate the `6!=720` perfect matchings and the `!6=265` derangements relative to
each fixed matching.  Deduplicate physical unions and test the 372 collinear
three-cell subsets of the standard board. ∎

The complete potential distributions are stored and checked by the companion
script.

## 2. Extension-free target response table

For a fixed opposite matching `O` and cell `e notin O`, define

\[
\mu_6(O,e)
=
\min_{R\in\operatorname{PM}(K_{6,6}\setminus(O\cup\{e\}))}
\Phi(O\cup R).
\]

### Theorem CMR1311 -- PROVED

The table is defined for all

\[
\boxed{720\cdot30=21600}
\]

fixed-opposite/nonopposite-cell pairs.  Every minimizing response has a compatible
forbidden extension through `e` by CMR1303--CMR1304.

### Proof

There are thirty cells outside each perfect matching.  CMR1303 identifies the
response union and CMR1302 makes every cell in the complement available to some
forbidden extension. ∎

## 3. Immediate lower-response classification

### Theorem CMR1312 -- PROVED BY COMPLETE FINITE ENUMERATION

Of the 190684 dirty ordered states:

1. exactly
   \[
   \boxed{189476}
   \]
   have a target cell whose extension-free response has strictly smaller potential;
2. exactly
   \[
   \boxed{1208}
   \]
   have no immediate lower target response, but do have an equal-potential target
   response.

Among the 1208 immediate traps, 1128 have potential one and 80 have potential two.

### Proof

For every dirty ordered state, enumerate the cells belonging to its current
physical targets.  For a cell in one layer, query `mu_6` with the other layer fixed.
The displayed counts exhaust all ordered states. ∎

Thus side six is the first full-grid side where one target-bank step is not always
strictly improving.

## 4. Equal-response escape graph

Make a directed graph on the 1208 immediate traps.  Draw an edge from `S` to `Q`
when `Q` is an equal-potential extension-free response through a current target
cell.  A target state outside the 1208-set is called an **exit** when it has an
immediate lower response.

### Theorem CMR1313 -- PROVED BY COMPLETE FINITE ENUMERATION

1. 1120 immediate traps have an equal-response edge directly to an exit.
2. 64 further traps reach an exit after two equal-response steps.
3. The remaining 24 ordered traps have no equal-response path to an exit.

The first two classes therefore admit a target-response path with at most two
equal moves followed by one strict decrease.

### Proof

Enumerate all equal-potential response matchings, build the directed graph and run
reverse breadth-first search from vertices with an exit edge.  The distance
histogram is `1120` at distance one and `64` at distance two. ∎

Exact state cycles are cycle-erasable, but the final class requires a different
response family.

## 5. The closed trap core

### Theorem CMR1314 -- PROVED BY COMPLETE FINITE ENUMERATION

The closed class consists of

\[
\boxed{24\text{ ordered states}=12\text{ physical states}.}
\]

Every one has potential one and a unique physical target.  Inside the closed class,
every ordered state has exactly one equal-response successor.  The functional
graph consists of

\[
\boxed{12\text{ fixed points and }6\text{ directed two-cycles}.}
\]

### Proof

Restrict the equal-response graph of CMR1313 to the unreachable vertices and
compute its strongly connected components.  Every vertex has one internal
successor; the component-size distribution is twelve singletons and six pairs. ∎

These are exact one-layer target-response traps on the full standard grid.  They
are not positive minima of the complete saturated state space.

## 6. A clean two-layer escape exists

Let the recorded CMF1 side-six clean state be

\[
p=(4,3,5,0,2,1),
\qquad
q=(3,1,0,5,4,2).
\]

### Theorem CMR1315 -- PROVED

The union `G(p) union G(q)` is saturated and has potential zero.  Hence every one of
the 24 one-layer trap states has an ambient two-layer response of strictly smaller
potential.

### Proof

The cleanliness and saturation of the displayed state are CMF1.  Every trap has
potential one by CMR1314, so the fixed clean state is lower. ∎

The clean response need not preserve either old layer and is not a single-target
degree-two bank response.

## 7. Restricted-host two-layer lowering expansion

### Theorem CMR1316 -- PROVED UNDER THE FULL-GRID COORDINATE HYPOTHESIS

Let a restricted host on the same full side-six coordinate sets have one of the 24
trap states as selected minimum.  Add all missing labelled edges of the recorded
clean two-layer state.  The resulting joint-host expansion has minimum zero and is
therefore lowering.  Canonical expansion normalization accepts a clean state or
contracts an added minimum-core edge.

### Proof

The expansion retains the old feasible trap and makes the clean CMF1 state
feasible.  Apply the complete lowering-expansion normalization CMR942--CMR952 to
the joint labelled state family. ∎

This argument is a finite full-grid escape, not a construction on arbitrary
scattered six-vertex factors.

## 8. Side-six scoped endpoint

### Corollary CMR1317 -- PROVED

On the full standard/affine side-six grid:

1. almost every dirty state has an immediate lower target response;
2. 1184 immediate traps escape after at most two equal target responses;
3. twelve physical one-layer response traps remain;
4. a recorded clean two-layer state gives a lowering expansion from every trap.

The finite root grid is therefore closed, while the trap core demonstrates why the
uniform proof cannot rely only on repeated one-layer fixed-target banks.  For
scattered residual factors the open work remains the local-envelope/spectral
collateral inequality in inherited coordinates.

No all-`n` theorem is claimed.  The 190800 ordered states, 21600 target-response
table entries, equal-response graph, trap components and CMF1 escape are checked in
[`scripts/verify_prime_power_side_six_target_response_traps.py`](../scripts/verify_prime_power_side_six_target_response_traps.py).
