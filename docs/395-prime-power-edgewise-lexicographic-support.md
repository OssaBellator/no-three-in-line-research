# Edgewise lexicographic audit of the global support graph

CMR2302--CMR2309 prove row-level strict weight margin or critical rank descent. A stronger,
optional pathwise criterion asks whether every individual positive target edge decreases the
pair `(global weight, rank)`.

## Theorem CMR2334 — PROVED AS AN INTERFACE

For every support edge `p -> t`, reconstruct

\[
\Delta_W(p,t)=W_p-W_t,
\qquad
\Delta_\rho(p,t)=\rho(p)-\rho(t).
\]

Weights and ranks come from the same final global quotient and interface certificate used by
the support-condensation checker.

## Theorem CMR2335 — PROVED

Each support edge receives exactly one classification:

1. `strict-weight-drop` when `Delta_W>0`;
2. `equal-weight-rank-drop` when `Delta_W=0` and `Delta_rho>0`;
3. `nondecreasing-edge` otherwise.

The first two cases are precisely strict lexicographic descent of `(W,rho)`.

## Theorem CMR2336 — PROVED

All nondecreasing edges are published explicitly with their row ID, multiplicity, row-level
classification, endpoint weights, endpoint ranks and exact drops.

A valid row-level quotient is not rejected merely because this stronger edgewise criterion
fails.

## Theorem CMR2337 — PROVED

The graph containing only lexicographically descending edges is acyclic. The checker publishes
a canonical topological order, exact longest path and one canonical maximum path.

## Theorem CMR2338 — PROVED

When positive drops exist, the checker publishes the minimum positive weight drop and the
minimum positive rank drop among equal-weight edges, together with the complete edge-class
distribution.

## Theorem CMR2339 — PROVED

The `complete_edgewise_lex_termination` flag is set exactly when the global family is complete
and every support edge is lexicographically descending.

In that case the exact longest descending path is a finite pathwise termination bound.

## Theorem CMR2340 — HONEST SUFFICIENCY BOUNDARY

Edgewise lexicographic descent is sufficient but not necessary. A branching or multiset
induction may be valid even when one target has nondecreasing individual weight, because the
proved row inequality controls the complete child multiset and signed fixed term.

## Corollary CMR2341 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_edgewise_lexicographic_support.py` audits every support edge and
publishes the stronger optional pathwise termination certificate or its exact failure set.

The checker was syntax-compiled in the publication environment. No genuine global quotient is
supplied.
