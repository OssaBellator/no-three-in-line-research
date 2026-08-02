# Connected-circulation shell realization

`docs/679` clears rational mixed cycles and accounts for connector tours. This
chapter gives the exact graph-theoretic condition under which a rational mixed
edge certificate already clears to one deterministic closed walk.

Let `f_e` be a nonnegative rational weight on the directed edges of a finite macro
transition graph.

## PP3ddn — Exact rational executability criterion

The weighted support clears to one closed walk using each edge proportionally to
`f_e` exactly when

```text
sum_{e out of v} f_e = sum_{e into v} f_e
```

for every vertex `v`, and the nonzero support is weakly connected.

The balance equations say that `f` is a rational circulation. Clear denominators
to obtain a nonnegative integer circulation. A balanced directed multigraph with
weakly connected nonzero support is Eulerian on its support, so one Euler tour uses
every edge with exactly the cleared multiplicity.

Conversely, the edge-incidence vector of any closed walk is balanced and has
connected support. Thus both conditions are necessary.

## PP3ddo — Robust gain survives denominator clearing

Let `U` be a compact polyhedral burden set and let the rational circulation have
strict robust saving

```text
min_{b in U} sum_e f_e (3-b_e) > 0.
```

If `D` clears all denominators, the Eulerian realization has edge multiplicities
`D f_e` and robust gain

```text
D * min_{b in U} sum_e f_e (3-b_e) > 0.
```

Therefore a positive connected rational circulation is already an executable
fixed composite shell walk. No separate cycle-by-cycle compatibility argument or
connector overhead is needed.

In the checker example, denominator six gives multiplicities

```text
0->1:3, 1->0:3, 1->2:2, 2->1:2
```

and a robust gain of ten.

## PP3ddp — Disconnected certificates and connector cost

A balanced mixed certificate can still fail direct execution when its support is
disconnected. Two loop certificates at different bases are the minimal example.
No single closed walk can traverse both supports without additional edges.

Adding a connector tour preserves balance and joins the support. If the connected
bundle has robust gain `G_bundle>0`, connector saving `A_connector`, and fixed setup
`S`, the least number of bundle repetitions giving strict improvement is

```text
max(0, floor((S-A_connector)/G_bundle)+1).
```

This separates two exact cases:

1. **connected circulation:** denominator clearing is lossless;
2. **disconnected circulation:** connector edges are mathematically necessary and
   their worst-case loss must be charged.

## Verification

`scripts/check_shell_circulation_realization.py` exhausts all 1,086 nonzero
balanced weakly connected directed multigraphs on three labelled vertices with
edge multiplicities zero, one, or two. Hierholzer reconstruction verifies exact
edge usage in every case. The script also checks rational denominator clearing,
polyhedral robust gain, disconnected-loop failure, connector repair, and the exact
setup formula.

## Evidence boundary

No coordinate macro transition graph currently supplies a positive connected
circulation, certified edge burdens, and exposed-state legality. The theorem is an
exact execution interface, not a geometric shell construction.
