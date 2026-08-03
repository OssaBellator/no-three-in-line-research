# First-host state-exclusion route leverage

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact conditional classification of the closure leverage supplied by source-backed impossible restoration-menu states. It does not prove any state impossible.

## Conditional exclusion rule

If a physical source proves that one menu state cannot occur for the first-host occurrence, then every directed transition incident to that state is physically impossible. Those incident edges may therefore use the `physical_exclusion` route from the closure-route source gate.

The four symbolic states are

```text
00  blocked
01  restore 20
10  restore 02
11  restore both.
```

The audit enumerates all `2^4=16` possible sets of impossible states and asks how many label-scalar and menu-scalar residual covers are already contained in the incident excluded-edge set.

This is conditional on an exact physical state-impossibility proof. Omitting a state from a fixture, failing to populate it, or not yet proving it realizable does not count as proving it impossible.

## No single-state shortcut

Every single state is incident to four directed edges, but no single-state exclusion contains a complete scalar residual cover:

```text
impossible state  label covers  menu covers  extra label routes  extra menu routes
00                0             0            1                   2
01                0             0            1                   2
10                0             0            2                   2
11                0             0            2                   2
```

In particular, proving restore-both state `11` impossible closes

```text
01->11
10->11
11->01
11->10
```

but still leaves a minimum deficit of two route-closed edges for both the selected-label and full-menu scalar problems.

Therefore

```text
exclude state 11 alone does not close recurrence.
```

It removes the simultaneous-restoration node and its four incident directions, but does not resolve the remaining bidirected transitions around states `00`, `01`, and `10`.

## Exact two-state shortcuts

Among the six two-state exclusion patterns, exactly three contain a complete label-scalar cover:

```text
{00,01}
{00,11}
{01,10}.
```

Their effects differ.

### Adjacent pair `{00,01}`

This closes six directed edges and contains all six label-scalar residual covers, but no menu-scalar cover. One additional menu edge route is still required.

### Opposite pairs `{00,11}` and `{01,10}`

Each opposite pair touches every undirected square edge and therefore physically excludes all eight directed edges. Each contains

```text
6 label-scalar covers
14 menu-scalar covers.
```

These are the only two-state patterns that complete a menu cover without any separately routed edge.

The remaining adjacent pairs do not complete either cover type:

```text
{00,10}
{01,11}
{10,11}.
```

Each still requires one additional route at both levels, except `{00,10}`, whose label deficit is also one.

## Complete census

```text
state-exclusion patterns                         16
single-state patterns                             4
single-state patterns completing label cover      0
single-state patterns completing menu cover       0

two-state patterns                                6
two-state patterns completing label cover         3
two-state patterns completing menu cover          2

minimum state exclusions for label-only closure   2
minimum state exclusions for menu closure         2
patterns excluding all eight directed edges       7.
```

The seven all-edge patterns are the two opposite pairs, all four three-state exclusions, and the four-state exclusion.

## Physical ingestion consequence

A future source may combine state impossibility and edge-specific routes. For an impossible-state set `S`, the manifest reports

```text
incident physically excluded edges
complete covers already contained
minimum additional label routes
minimum additional menu routes.
```

The remaining routes must still pass the exact closure-route source gate. State-level exclusion does not populate owner identity, child rows, capacities, outer profiles or Lyapunov values for surviving states and edges.

The current source provides no state-impossibility proof, so the current incident excluded-edge set remains empty.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_state_exclusion_route_leverage.py \
  --check data/exact_recurrent_first_host_state_exclusion_route_leverage.json
```

The checker joins the transition-domain source audit and route-cover admission theorem, enumerates all sixteen state subsets, proves the exact shortcut lists and rejects fourteen deliberate corruptions.

Physical occurrence coverage, transition legality, owner identity, capacities, recurrent child rows, strict Lyapunov slack, global termination and `all_n_proved_by_checker` remain zero.
