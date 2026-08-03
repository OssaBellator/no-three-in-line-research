# Exact recurrent scalar-route progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

This track records symbolic scalar-potential and route-cover results for the first residual host. It does not assert that the four restoration menu states or their edges are physically realized.

## ERL2e — complete scalar route-cover classification

The selected-label graph is the complete bidirected triangle on

```text
3012, 2031, 3201.
```

Its six strict label orders give six distinct descent orientations. Every label scalar pays exactly three selector-changing gates and leaves exactly three external routes:

```text
2 routes flipping r02
1 route flipping r20.
```

Among the eight formal choices of one external route from each bidirected label pair, exactly six are scalar-compatible. The remaining two leave a directed label cycle.

The full four-state restoration graph is the bidirected square on

```text
00 blocked
01 restore 20
10 restore 02
11 restore both.
```

Its 24 strict state orders induce exactly 14 distinct acyclic edge orientations. Every menu scalar pays four directed edges and leaves four external routes:

```text
3 selector-changing routes
1 selector-neutral route
2 routes flipping r02
2 routes flipping r20.
```

Among the sixteen formal choices of one external route per undirected square edge, exactly fourteen are scalar-compatible. The remaining two leave a directed four-cycle.

Menu-state refinement does not increase the maximum number of selector-changing gates paid: it remains three. It does expand the attainable paid triples from the six transitive label tournaments to all eight tournaments.

Exactly two acyclic menu orientations project to directed selected-label cycles. They are possible only because selected label `2031` has two distinct menu representatives, `10` and `11`.

Only four of the fourteen menu orientations arise from an additive bit potential

```text
V=alpha*r02+beta*r20.
```

The other ten require interaction-sensitive menu state.

## ERL2f — sharp Boolean interaction coefficient

Write a general menu potential as

```text
V(r02,r20)=c+alpha*r02+beta*r20+Gamma*r02*r20.
```

Then

```text
Gamma = V11-V10-V01+V00
      = (V11-V01)-(V10-V00)
      = (V11-V10)-(V01-V00).
```

If either restoration bit reverses paid direction between its two parallel cube edges, the corresponding two nonzero integer marginal differences have opposite signs. Therefore

```text
|Gamma| >= 2.
```

If neither bit reverses direction, an additive potential with `Gamma=0` realizes the orientation. Thus `Gamma=0` is possible exactly for the four additive orientations.

The complete fourteen-orientation reversal profile is

```text
no parallel reversal  4
r02 reversal only     4
r20 reversal only     4
both reverse           2.
```

Every nonadditive orientation has a witness with values in `{0,1,2,3}` and `|Gamma|=2`, so the lower bound is sharp throughout:

```text
minimum |Gamma|=0   4 orientations
minimum |Gamma|=2  10 orientations.
```

The two cyclic selected-label lifts use opposite minimal interactions:

```text
Gamma=-2 for paid edges
  00->01, 01->11, 10->00, 10->11

Gamma=+2 for paid edges
  00->10, 01->00, 11->01, 11->10.
```

## Import boundary

The exact scalar alternatives are now finite:

```text
6 label-scalar route covers
14 menu-scalar route covers
4 additive bit-potential orientations
10 interaction-required orientations.
```

No artifact chooses one of these alternatives physically. A valid alternating-core import must still attach every realized menu edge to a persistent physical owner, prove legality, assign source-backed potential values, verify strict descent on paid edges, and populate a registered closure route or capacity for every residual edge.

Therefore

```text
physical_route_assignment_proved = 0
physical_potential_installed = 0
promotion_to_recurrent_closure_allowed = 0
all_n_proved_by_checker = 0.
```

## Executable artifacts

```text
scripts/check_exact_recurrent_first_host_scalar_route_cover.py
data/exact_recurrent_first_host_scalar_route_cover.json
docs/exact-recurrent-first-host-scalar-route-cover.md

scripts/check_exact_recurrent_first_host_menu_interaction_potential.py
data/exact_recurrent_first_host_menu_interaction_potential.json
docs/exact-recurrent-first-host-menu-interaction-potential.md

.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```
