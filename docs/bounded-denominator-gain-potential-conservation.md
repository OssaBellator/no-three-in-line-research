# Bounded-denominator gain-potential source conservation

This note records BDA5cz--BDA5dd.  It extends exact nonamplifying source conservation to physical transitions that may enlarge raw numerator mass on one edge but have no amplifying directed cycle.

## Contract

Let `G=(V,E)` be a finite decorated source graph.  Every edge `e:u->v` has a positive rational gain `g_e`.  A transition carrying input mass `m` may create output mass `m'` only when

`m' <= g_e m`.

Physical predecessor lineage is one-for-one: an output occurrence has one retained input occurrence, and splitting or source-less creation is not allowed.

Assume every directed cycle `C` satisfies

`product_{e in C} g_e <= 1`.

## Results

### BDA5cz — gain-potential certificate

There are positive rational vertex weights `q_v` such that for every edge `u->v`,

`q_v g_e <= q_u`.

One canonical choice is the maximum gain product over simple directed paths starting at `v`, with the empty path contributing `1`.

### BDA5da — weighted transition monotonicity

Every legal transition obeys

`q_v m' <= q_u m`.

Thus raw mass may increase while the certified potential mass cannot.

### BDA5db — epoch conservation

During an epoch with initial live potential `P_0`, exact deposited potential `D`, terminally consumed potential `T` and remaining live potential `P_live`,

`T+P_live <= P_0+D`.

Repeated circulation inside a gain-one SCC cannot enlarge the restoration account.

### BDA5dc — restoration threshold bound

If every selected restoration consumes at least potential `J_0`, then the number of selected restorations is at most

`floor((P_0+D)/J_0)`.

### BDA5dd — exact failure return

An edge with `q_v g_e>q_u`, a directed cycle with product greater than one, splitting, source-less creation, missing mass, or changed decorations is returned as an amplification/reset obstruction rather than being treated as paid source mass.

## Proof

If a path repeats a directed cycle, deleting that cycle does not reduce its gain product because the cycle product is at most one.  Therefore a maximum is attained by a simple path, so the path-product definition of `q` is finite.  Prepending an edge `u->v` to a maximizing path from `v`, and deleting any repeated nonamplifying cycle, proves `q_u>=g_e q_v`.  Summing the edgewise inequality over occurrence-faithful transitions gives the epoch conservation law and its threshold corollary.

## Finite audit

Run:

`python scripts/verify_bda_gain_potential_conservation.py`

The deterministic audit checks:

- 10,000 finite source systems;
- 39,131 certified gain edges;
- 46,426 occurrence-faithful transfers;
- 126,799 terminal source units;
- 1,745 sampled gain-certificate violations;
- at most seven source nodes per system.

## Scope

The theorem does not establish the cycle-product inequality for the concrete bounded-denominator source graph.  It supplies an exact target: prove a rational gain potential or return an amplifying cycle.  Unbounded source dictionaries and incomplete predecessor lineage remain outside the contract.  BDA6 and the no-three-in-line conjecture remain open.
