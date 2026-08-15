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

## ERL2g — alternating-core route-budget import

Four exact alternating-core contracts were pinned by immutable theorem and verifier blob IDs:

```text
normalized builder boundary capacity
source-paid capacity recreation
physical source-capacity overload
outer-reset repetition and macro tickets.
```

Their verifiers use generic finite state systems, capacity vectors, seeded random histories or profile/ticket sweeps. They contain zero first-host records, owner tokens, capacity values or macro tickets.

Every one of the fourteen menu covers has the same coarse residual profile:

```text
3 selector-changing routes
1 selector-neutral route
2 r02 routes
2 r20 routes.
```

The restore/delete profile varies exactly as

```text
0/4: 1 cover
1/3: 4 covers
2/2: 4 covers
3/1: 4 covers
4/0: 1 cover.
```

The additive/interaction cross-table is

```text
additive:    restore counts 0,2,4 with multiplicities 1,2,1
interaction: restore counts 1,2,3 with multiplicities 4,2,4.
```

For any nonnegative cost depending only on restore versus delete direction, plus a nonnegative interaction penalty, an additive cover is optimal. Interaction can only be forced after exact directed edges or selected-target patterns receive distinct costs.

The exact conditional episode ceilings are

```text
N_cap <= C0 + H_cap
N_out <= E_first + Q,
```

where `C0` is initial exact gate capacity, `H_cap=sum rho_a*s_a(0)` is source-paid recreation budget, `E_first` counts first decorated outer-edge traversals, and `Q` is finite macro-ticket stock.

Sixteen first-host import fields are required to activate these formulae; zero are populated.

## ERL2h — exact closure-route source gate

The capacity and reset formulae do not decide whether one exact menu edge is admissible under any physical closure route. The source gate therefore classifies every directed edge against five alternating-core routes:

```text
physical exclusion
terminal or improving output
bounded strict potential
finite unrestorable capacity
decorated outer reset.
```

The resulting acceptance surface has

```text
8 directed menu edges
5 route classes
40 exact edge-route pairs.
```

All eight symbolic edges have candidate normalized menu-state addresses. Current source coverage gives

```text
physical legal edges                         0
persistent physical owner tokens             0
source-admissible edge-route pairs            0
edges with at least one admissible route       0.
```

The five route contracts use eight fields from the existing sixteen-field physical worklist and sixteen additional route-specific fields. The additional fields include exact exclusion references, terminal outcome proofs, bounded potential values and ranges, capacity addresses and nonrestoration proofs, and decorated outer-profile repetition routes. None is populated.

A capacity-only label-scalar closure requires three distinct exact gate addresses; a capacity-only menu-scalar closure requires four. Distinct directed normalized edges cannot share one capacity coordinate unless a separate shared-capacity theorem is installed.

Each selector-changing directed edge is residual in exactly three of the six label covers. Each directed menu edge is residual in exactly seven of the fourteen menu covers. Thus no exact directed edge is unavoidable under every scalar choice, but every chosen scalar exposes a complete source-backed worklist of three or four routes.

Naming a transition an outer reset closes only its first decorated traversal. Repetition still requires a macro ticket, payment theorem, bounded descent or terminal output.

## Import boundary

The exact scalar alternatives, conditional budgets and source acceptance matrix are finite:

```text
6 label-scalar route covers
14 menu-scalar route covers
4 additive bit-potential orientations
10 interaction-required orientations
2 exact conditional episode ceilings
40 exact edge-route acceptance cells.
```

No artifact chooses one of these alternatives physically. A valid alternating-core import must still attach every realized menu edge to a persistent physical owner, prove legality, assign source-backed potential values on paid edges, and populate one accepted route with exact source evidence for every residual edge.

Therefore

```text
physical_route_assignment_proved = 0
physical_potential_installed = 0
physical_capacity_or_reset_contract_installed = 0
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

scripts/check_exact_recurrent_first_host_alternating_route_budget_import.py
data/exact_recurrent_first_host_alternating_route_budget_import.json
docs/exact-recurrent-first-host-alternating-route-budget-import.md

scripts/check_exact_recurrent_first_host_closure_route_source_gate.py
data/exact_recurrent_first_host_closure_route_source_gate.json
docs/exact-recurrent-first-host-closure-route-source-gate.md

.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```
