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

physical saturated states.  Exactly 116 ordered states and 50 physical states are
clean.  The remaining 190684 ordered states are dirty, and the maximum physical
potential is forty.

### Proof

Enumerate the `6!=720` perfect matchings, the `!6=265` derangements relative to each
fixed matching, and the 372 collinear three-cell subsets of the standard board. ∎

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

There are thirty cells outside each perfect matching, and CMR1303 identifies the
response union. ∎

## 3. Immediate lower-response classification

### Theorem CMR1312 -- PROVED BY COMPLETE FINITE ENUMERATION

Of the 190684 dirty ordered states:

1. exactly 189476 have a target cell with a strictly lower extension-free response;
2. exactly 1208 have no immediate lower target response but have an equal-potential
   response.

Among the 1208 immediate traps, 1128 have potential one and 80 have potential two.

### Proof

Enumerate the cells of every current target and query `mu_6` with the other layer
fixed. ∎

## 4. Equal-response escape graph

Draw an edge between immediate traps when an equal-potential extension-free target
response connects them.  A state outside the trap set is an exit if it has an
immediate lower response.

### Theorem CMR1313 -- PROVED BY COMPLETE FINITE ENUMERATION

1. 1120 immediate traps have an equal-response edge directly to an exit.
2. 64 further traps reach an exit after two equal-response steps.
3. The remaining 24 ordered traps have no equal-response path to an exit.

### Proof

Build the complete equal-response graph and run reverse breadth-first search from
vertices with an exit edge.  The distance histogram is 1120 at distance one and 64
at distance two. ∎

## 5. The closed trap core

### Theorem CMR1314 -- PROVED BY COMPLETE FINITE ENUMERATION

The closed class consists of

\[
\boxed{24\text{ ordered states}=12\text{ physical states}.}
\]

Every state has potential one and one physical target.  Each ordered state has
exactly one equal-response successor inside the closed class.  The functional
graph consists of

\[
\boxed{6\text{ directed two-cycles and }12\text{ one-step feeder states}.}
\]

Every feeder enters one of the two-cycles after one equal response.  There are no
fixed points.

### Proof

Restrict the equal-response graph to the 24 unreachable vertices.  Every vertex has
one internal successor.  Exactly twelve vertices lie on six directed two-cycles;
the other twelve have distance one to those cycles. ∎

Thus the recurrent core itself has twelve ordered states, while twelve additional
ordered states feed it.  Together they represent twelve physical configurations.

## 6. A clean two-layer escape exists

Let the recorded CMF1 side-six clean state be

\[
p=(4,3,5,0,2,1),
\qquad
q=(3,1,0,5,4,2).
\]

### Theorem CMR1315 -- PROVED

The union `G(p) union G(q)` is saturated and has potential zero.  Hence every one of
the 24 closed-class ordered states has an ambient two-layer response of strictly
smaller potential.

### Proof

Use CMF1 and CMR1314. ∎

The clean response need not preserve either old layer and is not a one-layer
fixed-target bank response.

## 7. Restricted-host two-layer lowering expansion

### Theorem CMR1316 -- PROVED UNDER THE FULL-GRID COORDINATE HYPOTHESIS

At a restricted host on the same full side-six coordinate sets, adding the missing
labelled edges of the recorded clean state creates a lowering joint-host expansion.
Canonical normalization accepts a clean state or contracts an added minimum-core
edge.

### Proof

The expansion retains the old trap and makes a potential-zero state feasible.
Apply CMR942--CMR952. ∎

## 8. Side-six scoped endpoint

### Corollary CMR1317 -- PROVED

On the full standard/affine side-six grid:

1. 189476 dirty ordered states improve immediately;
2. 1184 immediate traps escape after at most two equal target responses;
3. 24 ordered states form a feeder-plus-two-cycle one-layer trap class;
4. the CMF1 clean state gives a two-layer lowering expansion from every trap.

The root grid is therefore closed, while the trap class demonstrates why a uniform
proof cannot rely only on repeated one-layer fixed-target banks.  Scattered
residual factors still require inherited-coordinate local-envelope or spectral
control.

No all-`n` theorem is claimed.  The complete state stock, response table,
equal-response graph and clean escape are checked in
[`scripts/verify_prime_power_side_six_target_response_traps.py`](../scripts/verify_prime_power_side_six_target_response_traps.py).
