# First-host alternating-core route-budget import

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact conditional import of alternating-core capacity and reset contracts for the symbolic four-state first-host restoration square. It does not populate physical capacities, owner tokens, legal transitions, outer profiles or macro tickets.

## Immutable upstream contracts

The audit pins four alternating-core theorem and verifier pairs by Git blob ID:

```text
normalized builder boundary capacity
source-paid capacity recreation
physical source-capacity overload
outer-reset repetition and macro tickets
```

The theorems are exact under their stated hypotheses. Their verifiers are generic finite-state enumerations, exhaustive capacity vectors, seeded random histories or profile/ticket parameter sweeps. None contains:

```text
host s4-75b04c45c1c8eac2
one first-host owner token
one first-host capacity value
one first-host capacity-source counter
one first-host decorated outer edge
one first-host macro ticket.
```

They are therefore import contracts, not first-host source data.

## Constant coarse burden of every menu scalar

Every scalar-compatible orientation of the restoration square leaves four residual directed edges. For all fourteen covers the residual stock is exactly

```text
3 selector-changing edges
1 selector-neutral edge
2 edges flipping r02
2 edges flipping r20.
```

Consequently no cost or capacity theorem depending only on

```text
restoration-bit family
selector-changing versus neutral status
```

can distinguish the fourteen covers.

In particular, every menu-scalar proof must route one selector-neutral edge. Refining from selected labels to menu states never removes that obligation.

## Exact operation-direction frontier

The number of residual restore-direction edges has distribution

```text
0 restores, 4 deletes: 1 cover
1 restore,  3 deletes: 4 covers
2 restores, 2 deletes: 4 covers
3 restores, 1 delete:  4 covers
4 restores, 0 deletes: 1 cover.
```

Crossing with the interaction classification gives

```text
additive covers:
  restore count 0: 1
  restore count 2: 2
  restore count 4: 1

interaction-required covers:
  restore count 1: 4
  restore count 2: 2
  restore count 3: 4.
```

Thus the two one-direction extremes are additive. The odd `1/3` and `3/1` direction splits always require the Boolean interaction term.

## Aggregate direction costs never require interaction

Give every residual restore edge cost `c_R>=0`, every residual delete edge cost `c_D>=0`, and every interaction-required potential an additional penalty `c_I>=0`.

A cover with `r` residual restores has cost

```text
r*c_R + (4-r)*c_D + c_I*1[interaction].
```

The linear direction term is minimized at `r=0` or `r=4`, unless `c_R=c_D`, and both extremes have additive representatives. When the direction costs tie, additive covers also exist.

Therefore every nonnegative aggregate direction-cost problem has an additive optimum. Interaction is never forced merely by a preference for restore versus delete routes.

By contrast, each exact edge-sensitive cover can be made uniquely optimal by assigning cost zero to its four residual directions and cost one to their reverses. Interaction is therefore relevant only after the source distinguishes exact menu edges or selected-target patterns.

## Finite gate-capacity budget

Suppose a residual edge is charged through exact normalized gate capacity. Put

```text
C0    = sum of initial capacities at the charged residual gate addresses
H_cap = sum_a rho_a*s_a(0)
```

where `H_cap` is the source-faithful budget for every later positive capacity increment.

If every charged episode consumes one capacity unit and every recreation is occurrence-faithfully assigned to the fixed capacity sources, then

```text
N_cap <= C0 + H_cap.
```

This combines the normalized builder-gate capacity theorem with the source-capacity recreation ledger. It does not permit free restoration of a spent gate ticket.

A valid record must supply at least:

```text
persistent owner token
exact normalized source and target states
legal transition witness
initial gate capacities
fixed capacity atom universe
capacity-source addresses
conversion rates
initial source counters
assignment of every positive capacity increment.
```

None is populated for the first host.

## Outer-reset ticket budget

A residual transition may instead leave the reconstructed family as a decorated outer edge. First traversal of one exact decorated edge is finite progress, but its repetition is not.

Let

```text
E_first = number of distinct decorated residual edges actually traversed
Q       = finite capacity-one macro-ticket stock for repeated traversals.
```

If every repeat consumes a new ticket or closes by another registered route, then

```text
N_out <= E_first + Q.
```

A symbolic menu edge is not automatically one decorated outer edge. The source must supply the complete source and target profiles, reset decoration, internal epoch bound and ticket address.

No such first-host data exists.

## Exact missing import fields

The checker records sixteen still-empty fields:

```text
persistent_owner_token
legal_normalized_transition_edges
direct_gate_capacities
capacity_atom_universe
capacity_source_addresses
capacity_conversion_rates
capacity_source_initial_counters
capacity_increment_assignments
physical_occurrence_capacities
overload_crossing_tickets
outer_profile_dictionary
outer_edge_decorations
internal_epoch_bound
macro_ticket_stock
source_backed_menu_potential_values
registered_residual_route_assignment
```

Thus

```text
required fields              16
populated fields               0
complete route contracts       0
promotion to recurrence        0.
```

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_alternating_route_budget_import.py \
  --check data/exact_recurrent_first_host_alternating_route_budget_import.json
```

The checker reconstructs all fourteen scalar-compatible menu covers, proves the constant coarse burden, compiles the operation-direction and interaction cross-table, verifies aggregate direction-cost optimality and exact-edge unique-optimum witnesses, installs both conditional budget formulae, and rejects sixteen deliberate corruptions.

Physical chart confinement, occurrence coverage, transition legality, owner identity, capacities, macro tickets, recurrent child rows, strict Lyapunov slack, global termination and `all_n_proved_by_checker` remain zero.
