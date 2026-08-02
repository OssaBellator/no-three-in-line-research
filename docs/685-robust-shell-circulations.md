# Robust shell circulations

`docs/679` realizes rational mixed-cycle certificates by clearing denominators and
paying connector losses. This chapter packages the search problem as one finite
linear program on edge circulations.

Let `G=(V,E)` be a finite directed macro graph. Let the burden uncertainty polytope
have vertices `b^u`, and write `B` for the vertex-edge incidence matrix.

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
all data are rational, a positive optimum has a rational optimal witness and its
denominators can be cleared.

## PP3ddo — From circulation to one executable closed walk

After clearing denominators, the circulation becomes an integer Eulerian
multigraph on each connected support component. Each component therefore has a
closed Euler tour carrying its certified robust gain.

If the ambient macro graph supplies a fixed connector tour visiting all support
components, let its worst-case saving be `A_connector<=0`, and let one cleared
circulation bundle have robust gain `G_bundle>0`. Repeating the bundle

```text
max(1, floor((-A_connector)/G_bundle)+1)
```

times and inserting the connector tour gives one deterministic closed walk with
strictly positive robust gain.

More generally, with setup `S`, replace `-A_connector` by `S-A_connector`.

## PP3ddp — Exact two-state circulation witness

`scripts/check_shell_robust_circulation.py` audits a two-state graph with one loop
at each state and a connector in each direction. The uncertainty vertices assign
loop burdens

```text
(1,4) and (4,1),
```

while both connectors have burden four.

The optimal normalized circulation is

```text
x=(1/2,1/2,0,0)
```

with exact robust margin `1/2`. The checker proves optimality from the average of
the two scenario gains and exhausts every rational grid of denominator at most 32.

Clearing denominators gives one copy of each loop with robust gain one. The
connector tour has worst-case saving `-2`, so two bundles only break even and
exactly three bundles give a deterministic closed walk of robust gain one.

## Evidence boundary

This converts a finite macro graph and burden polytope into an exact optimization
and execution test. No coordinate construction currently supplies the required
macro edges, rational burden vertices, or connector tour, so no shell row is
promoted.
