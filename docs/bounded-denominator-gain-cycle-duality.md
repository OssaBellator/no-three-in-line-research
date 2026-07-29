# Bounded-denominator gain-cycle duality

This note records BDA5de--BDA5di. It turns the retained physical gain graph into an exact potential-or-cycle alternative.

## Contract

Let `G=(V,E)` be a finite directed source graph. Every edge `u -> v` carries a positive rational gain `g_uv`. An occurrence-faithful transfer obeys

`m_v' <= g_uv m_u`

for the exact nonnegative numerator mass attached to that occurrence. No splitting, source-less creation or omitted lineage is allowed.

## Theorem block BDA5de--BDA5di

The following are equivalent:

1. every directed cycle `C` satisfies `prod_{e in C} g_e <= 1`;
2. there is a positive rational vertex potential `q` satisfying
   `q_u >= g_uv q_v` on every edge;
3. the weighted mass `q_state * m` is nonincreasing along every legal transfer.

When the cycle condition holds, one canonical potential is

`q_u = max { product of gains along P : P is a simple directed path starting at u }`.

Removing a repeated cycle cannot decrease the path product because every cycle product is at most one, so the maximum is attained by a simple path.

If no such potential exists, the complete finite graph contains a directed cycle with gain product greater than one. The least such cycle is the exact amplification obstruction.

## Consequence

Individual physical source transitions may increase raw numerator mass. What is required is the weaker and exact condition that no closed source route amplifies the retained weighted mass. Under that condition the earlier weighted SCC source bank applies to `q_v m_v`.

## Finite audit

Run:

`python scripts/verify_bda_gain_cycle_duality.py`

The audit enumerates simple cycles in random finite rational-gain graphs, constructs the maximum-path potential when possible and verifies weighted nonincrease on sampled transfers.

## Scope

The theorem requires a complete finite gain graph and exact occurrence lineage. It does not prove that the concrete BDA source graph has no amplifying cycle, nor does it prove BDA6 or the global conjecture.
