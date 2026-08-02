# Robust shell circulations

`docs/679` realizes rational mixed-cycle certificates by clearing denominators and
paying connector losses. This chapter packages robust search as a finite linear
program and gives the exact condition for lossless execution as one closed walk.

Let `G=(V,E)` be a finite directed macro graph. Let the burden uncertainty polytope
have rational vertices `b^u`, and write `B` for the vertex-edge incidence matrix.

## PP3ddn — Exact robust-circulation linear program

Normalize a nonnegative edge circulation by

```text
Bx=0,  x>=0,  sum_e x_e=1.
```

Its robust saving margin is

```text
min_u sum_e x_e(3-b^u_e).
```

Therefore the best normalized robust circulation is the rational linear program

```text
maximize gamma
subject to
  Bx=0,
  x>=0,
  sum_e x_e=1,
  gamma <= sum_e x_e(3-b^u_e)  for every uncertainty vertex u.
```

A positive optimum is equivalent to a positive rational robust circulation. Since
all data are rational, a positive optimum has a rational witness.

## PP3ddo — Exact single-walk realization criterion

A nonnegative rational edge vector clears to one closed walk using every edge in
its prescribed proportion exactly when it is balanced and its nonzero support is
weakly connected.

After clearing denominators, balance gives an integer circulation. A balanced
directed multigraph with weakly connected nonzero support is Eulerian, so one
Euler tour uses every edge with exactly the cleared multiplicity. Conversely, the
edge-incidence vector of any closed walk is balanced and has connected support.

Thus a positive robust circulation with connected support is directly executable,
and denominator clearing multiplies its robust gain by the clearing denominator
without connector loss.

If the support has several connected components, each component clears to a closed
walk but no single walk traverses all components. A connector tour is then
mathematically necessary. If its worst-case saving is `A_connector<=0`, one cleared
bundle has gain `G_bundle>0`, and setup is `S`, the exact repetition count is

```text
max(1, floor((S-A_connector)/G_bundle)+1).
```

## PP3ddp — Exact finite witnesses and audits

The two-state circulation example has one loop at each state and connectors in
both directions. Its uncertainty vertices assign loop burdens `(1,4)` and `(4,1)`
while both connectors have burden four. The optimal normalized circulation is

```text
x=(1/2,1/2,0,0)
```

with robust margin `1/2`. Clearing denominators gives one copy of each loop with
robust gain one. The connector tour has worst-case saving `-2`, so two bundles only
break even and exactly three give positive gain.

A separate connected example with rational edge weights `1/2,1/2,1/3,1/3`
clears at denominator six to multiplicities `3,3,2,2` and has robust gain ten.

## Verification

- `scripts/check_shell_robust_circulation.py` proves the two-state LP optimum and
  exhausts rational grids of denominator at most 32.
- `scripts/check_shell_circulation_realization.py` exhausts all 1,086 nonzero
  balanced weakly connected directed multigraphs on three labelled vertices with
  edge multiplicities zero, one, or two, reconstructing an exact Euler tour in
  every case. It also checks denominator clearing, disconnected-support failure,
  connector repair, and setup repayment.

## Evidence boundary

This converts a finite macro graph and rational burden polytope into an exact
optimization and execution test. No coordinate construction currently supplies a
positive connected circulation, the certified macro edges and burdens, or a
connector tour for disconnected support, so no shell row is promoted.
