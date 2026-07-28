# Geometric-cleaning integrated remedy-height flow

This note records GC2iw--GC2ja. It replaces a remedy choice followed by a separate height check with one integral three-layer flow.

## Contract

Let `C` be finite cause classes with integral demands, `R` remedy classes with capacities, and `H` height-source classes with capacities. A complete cause/remedy graph and remedy/height-source graph are retained. One paid cause unit must traverse
`cause -> remedy -> height source`.
Remedy and height-source capacities are shared across all paths.

## Theorem block GC2iw--GC2ja

### GC2iw — integrated network

Split each remedy vertex into an input and output vertex joined by its capacity edge. Add source-to-cause demand edges and height-source-to-sink capacity edges. Legal paid units are exactly integral flows in this network.

### GC2ix — simultaneous capacity control

Every integral flow debits each remedy unit and each height-source unit at most once. No preliminary remedy selection can reserve height credit invisibly.

### GC2iy — exact full-payment criterion

All cause demand is paid iff the maximum flow equals total demand, equivalently iff every source/sink cut has capacity at least total demand.

### GC2iz — canonical mixed cut

Failure returns the canonical minimum residual cut, retaining its cause side, remedy-capacity boundary and height-source boundary.

### GC2ja — sequential-selection obstruction

Separate cause/remedy feasibility and adequate total height capacity do not imply integrated feasibility. A failed integrated cut is the exact witness to an incompatible remedy/height bottleneck.

## Proof

The split-remedy construction is a finite integral network. Integral max-flow/min-cut gives the result and preserves both capacity families simultaneously.

## Finite audit

Run `python scripts/verify_gc_integrated_remedy_height_flow.py`.

## Scope

The theorem does not construct the physical graphs or prove their capacities and height costs. It does not prove GC5 or the no-three-in-line conjecture.
