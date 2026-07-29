# Prime-patching parity index supplement: `docs/423--428`

This supplement continues the cumulative parity index after `docs/422`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3bzh--PP3bzj | Sequential marker-prefix trees retain the product repair degree; safety conditioning costs inverse leaf density, and failure exposes one low-branching prefix | PROVED | `docs/423-sequential-petal-marker-trees.md` |
| PP3bzk--PP3bzm | Capacity-weighted Hall target mass transfers back to a heavy source family; marginal atom bounds give a two-sided dense incidence rectangle | PROVED | `docs/424-two-sided-heavy-rectangles-from-hall-target-mass.md` |
| PP3bzn--PP3bzp | Deleting every target above a multiplicity threshold gives the optimized residual-layer envelope; failure produces a source-side tail of high-multiplicity hubs | PROVED | `docs/425-high-multiplicity-target-stripping.md` |
| PP3bzq--PP3bzs | Fixed-length codes schedule corridor banks with ambiguity `ceil(K/b^ell)`; injective logarithmic markers remove all bank-count loss, including after safety conditioning | PROVED | `docs/426-coded-corridor-bank-schedules.md` |
| PP3bzt--PP3bzv | Every failed shell rate has a simple cycle witness of length at most the state count; every successful rational threshold has a rational bounded-path potential and SCC-local audit | PROVED | `docs/427-bounded-path-certificates-for-shell-cycle-rates.md` |
| PP3bzw--PP3bzy | Nonnegative Schur elimination is associative and monotone; transient strongly connected components may be eliminated locally in reverse topological order | PROVED | `docs/428-associative-scc-elimination-for-type-loads.md` |

## Frontier update

### Boundary recleaning

Marker amplification no longer assumes simultaneous independent actions.  A
depth-`k` repair-prefix tree with branching `q_1,...,q_k` and final ambiguity
`h` has

```text
lambda_*<=h/product_i q_i.
```

After retaining safe leaves of density `p`, the bound becomes

```text
lambda_*<=h_G/(p product_i q_i).
```

If the required density fails, one explicit prefix has fewer than
`p^(1/k)q_i` safe-extending children.  The remaining geometric search can
therefore proceed prefix by prefix and return a short local obstruction.

### Localized Hall transport

A high-multiplicity target set `H` with target-law mass `eta` forces source-law
mass at least

```text
(eta-alpha)/(1-alpha)
```

on sources devoting at least an `alpha` fraction of their capacity to `H`.
When source atoms, target atoms, and row atoms are bounded, this gives many
sources, many targets, and a uniform lower target degree on every selected
source.  A diffuse Hall obstruction is therefore a concrete two-sided incidence
rectangle; a nondiffuse obstruction has already localized to one large atom.

### Fractional direct-clean layers

For target multiplicity threshold `h`, let `d_h` be the minimum number of
actions remaining after all targets of multiplicity greater than `h` are
deleted.  Then

```text
lambda_*<=min_(h:d_h>0) h/d_h.
```

If a proposed load `rho` fails, every useful threshold has `d_h<h/rho`, and
some source is adjacent to more than `d(x)-h/rho` high-multiplicity targets.
This supplies an iterative multiplicity-tail obstruction rather than only one
hub or one biclique core.

### Support-chord repair words

`K` corridor banks need only a short recoverable schedule code.  An alphabet of
size `b` and code length `ell` gives optimal ambiguity

```text
ceil(K/b^ell)
```

and hence load

```text
ceil(K/b^ell) h/q.
```

Length `ceil(log_b K)` is injective and removes all bank-count loss.  Safety
conditioning is incorporated by replacing each bank load `rho_i` with
`rho_i/p_i` before balancing code classes.

### Clean-macro shells

Arbitrary closed walks are no longer part of the finite audit.  A failed rate
`q` has a simple directed cycle of length at most the number of shell states.
If every such cycle passes, the exact rational potential is

```text
a(u)=max product_(e in P)(p_e/q),
```

over simple paths starting at `u`, all of length at most `|V|-1`.  Strongly
connected components contain every recurrent obstruction; the condensation
graph contributes only acyclic transitions.

### Integration

Transient type elimination can now be modular.  Eliminating disjoint blocks in
any order gives the same effective core, and entrywise upper envelopes remain
valid through the Schur complement.  Decomposing the transient graph into
strongly connected components reduces the global inverse to small local
resolvents plus finite acyclic propagation.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_423_428.py
```

or individually with

```bash
python scripts/check_sequential_petal_marker_trees.py
python scripts/check_hall_heavy_rectangles.py
python scripts/check_high_multiplicity_target_stripping.py
python scripts/check_coded_corridor_bank_schedules.py
python scripts/check_bounded_path_shell_potentials.py
python scripts/check_associative_type_elimination.py
```

The local audits verify all 254 proper safe subtrees of a three-level marker
cube, exact rational source-target rectangle bounds, every source subset and
multiplicity threshold of a stored action graph, sharp binary code ambiguity
for seven banks, all simple cycles and a nontrivial rational shell potential,
and exact direct, sequential, monotone, and SCC-local Schur eliminations.

The next available theorem identifier is `PP3bzz`.
