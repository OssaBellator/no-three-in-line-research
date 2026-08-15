# First-host closure-route source gate

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact source-acceptance audit for the symbolic restoration square. It does not prove that any restoration or deletion edge is physically legal.

## Directed edge domain

The four symbolic menu states are

```text
00  blocked       selected 3012
01  restore 20    selected 3201
10  restore 02    selected 2031
11  restore both  selected 2031.
```

The restoration square has eight directed single-bit edges:

```text
00->01  restore 20  selector changing
01->00  delete 20   selector changing
00->10  restore 02  selector changing
10->00  delete 02   selector changing
01->11  restore 02  selector changing
11->01  delete 02   selector changing
10->11  restore 20  selector neutral
11->10  delete 20   selector neutral.
```

Every edge has a finite **candidate normalized gate address** at the symbolic menu level. No source currently proves any edge is a legal physical transition or identifies one persistent physical owner token across its endpoints.

## Five admissible closure routes

The alternating-core boundary contracts permit five route classes.

### Physical exclusion

The exact directed edge is source-proved impossible for the physical occurrence.

Required base fields include

```text
physical_source_ref
legal_operations
realization_status
```

and the route must supply an exact edge reference and exclusion proof.

### Terminal or improving output

The exact legal transition produces a source-backed terminal or improving outcome.

This route requires the physical source, owner identity, operation trace, intermediate states, child row, positive weights, parent budget and realization status, plus an outcome kind and proof reference.

### Bounded strict potential

A source-backed bounded potential satisfies

```text
V(source) > V(target)
```

on the exact legal transition. The source and target values, potential definition and bounded-range proof must be installed. The symbolic scalar witnesses already compiled in this branch do not satisfy this physical-source requirement.

### Finite unrestorable capacity

Every traversal debits one unit from one exact finite gate address and that capacity cannot be restored during the closure epoch.

The route must provide

```text
capacity_address
initial_capacity
debit_rule_ref
nonrestoration_ref.
```

Different directed normalized edges have different exact addresses. One capacity coordinate cannot pay multiple edges unless a separate shared-capacity theorem is supplied.

### Decorated outer reset

The transition changes one reconstructed outer profile to another and carries an exact decoration. First traversal of a decorated edge is finite progress, but repetition is not automatically closed.

A repeated edge requires its own macro ticket, payment theorem, bounded descent or terminal output. Merely naming an edge an outer reset is insufficient.

## Exact source audit

Four alternating-core interfaces were pinned:

```text
builder-state boundary gates
physical source-capacity overload
source-paid capacity recreation
outer-reset quotient.
```

Their theorems provide acceptance rules. Their checkers enumerate synthetic predicates, capacities, source stocks, profiles and ticket budgets. None contains the first-host ID, a first-host owner token, legal transition, capacity value, source stock or outer-profile mapping.

The exact audit is therefore

```text
directed menu edges                         8
route classes                               5
edge-route pairs                           40
candidate normalized symbolic gates         8
physical legal edges                        0
persistent owner tokens                     0
source-admissible edge-route pairs           0
edges with at least one admissible route     0
```

The route interfaces use eight distinct fields from the existing sixteen-field physical worklist and sixteen additional route-specific fields. None is source-populated.

## Scalar-cover consequences

For a selected-label scalar:

```text
compatible scalar covers                    6
residual selector edges per cover            3
capacity-only exact addresses required       3.
```

Each of the six selector-changing directed edges is residual in exactly three of the six covers. No directed selector edge is forced to be residual under every scalar choice.

For an arbitrary menu scalar:

```text
compatible scalar covers                   14
residual menu edges per cover                4
residual selector-changing edges             3
residual selector-neutral edges              1
capacity-only exact addresses required       4.
```

Each of the eight directed menu edges is residual in exactly seven of the fourteen covers.

Thus choosing a scalar orientation does not choose a free closure. It chooses the exact set of three or four directed edges for which physical exclusion, output, bounded descent, capacity or reset evidence must be supplied.

## Conditional finite budgets

If every residual edge uses a separate finite capacity, the total residual traversal budget is

```text
sum_{e in residual cover} initial_capacity(e).
```

If capacity can be recreated, the alternating-core source ledger permits only source-faithful recreation bounded by

```text
sum_a rho_a * source_stock_a(0).
```

For decorated outer resets, first traversals are bounded by the number of distinct decorated edges. Repetitions require the finite macro-ticket stock plus separately bounded payment or descent events.

No numerical first-host value is currently available for any of these expressions.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_closure_route_source_gate.py \
  --check data/exact_recurrent_first_host_closure_route_source_gate.json
```

The checker reconstructs all eight edges, all forty route pairs, all six label-scalar covers, all fourteen menu-scalar covers, the exact residual-edge frequencies and the source-coverage gate. It rejects twelve deliberate corruptions.

Physical occurrence coverage, transition legality, persistent owner identity, capacities, outer profiles, child rows, strict Lyapunov slack, global termination and `all_n_proved_by_checker` remain zero.
