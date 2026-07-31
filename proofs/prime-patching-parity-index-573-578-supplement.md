# Prime-patching parity index supplement: `docs/573--578`

This supplement continues the cumulative parity index after `docs/572`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cqp--PP3cqr | Exact inherited line signatures decide boundary extension; the bounded-offset path tree has counts `8,282,74,4,0`, so no five-block word exists | PROVED / CATALOGUE OBSTRUCTION | `docs/573-inherited-line-state-obstruction-for-boundary-words.md` |
| PP3cqs--PP3cqu | Cylinder quotient choices biject onto the twelve compatible pairs of `K_4,4`; every pair has two perfect-matching extensions and two orientation witnesses | PROVED FOR THE COMPLETE-GRID HOST | `docs/574-complete-grid-extension-decoder-for-hall-choices.md` |
| PP3cqv--PP3cqx | The twelve positive source-cell occupancy normals admit a complete census: four are quotient-controlled and eight are hidden | PROVED FOR THE ALIGNED SOURCE MATRIX | `docs/575-source-cell-normal-census-for-threshold-layers.md` |
| PP3cqy--PP3cra | The Motzkin constructors decode to state-0/1/2 support terminals, and unary-run risk is exact consecutive state-1 support nesting | PROVED FOR THE AUTOMATON DECODER | `docs/576-automaton-support-leaf-risk-decoder.md` |
| PP3crb--PP3crd | The source unit service actions force identity incidence and transfer both the `ABC` phase buffers and `AABBC` optimum into one coordinate system | PROVED FOR THE SOURCE SERVICE MODEL | `docs/577-source-action-bridge-for-shell-service.md` |
| PP3cre--PP3crg | Candidate completion rises to `23/30`, arithmetic slack remains positive, and the geometric evidence gate still promotes zero actual rows | PROVED | `docs/578-geometric-decoder-evidence-gate.md` |

## Frontier update

### Boundary recleaning

The exact globally legal path counts inside offset radius twenty-four are

```text
8, 282, 74, 4, 0
```

for one through five blocks.  The four length-four survivors have 496 distinct
inherited pair lines, and all 306 adjacent-legal fifth steps fail.

### Localized Hall transport

The map

```text
(s,c) -> ((0,c),(1,c+s+1 mod 4))
```

is a bijection onto the twelve compatible pairs incident with two fixed left
resources of `K_4,4`.  Every pair leaves `K_2,2` and therefore has exactly two
perfect-matching extensions.  Both cylinder orientations witness every pair.

### Fractional direct-clean layers

Cell occupancy in the aligned conservative source matrix gives twelve positive
normals.  Four factor through constant/fixed/forward observables; eight are
hidden.  The cell `(0,0)` gives the explicit hidden normal `(1,1,0,0)`.

### Support-chord repair words

At original leaf count thirty and encoded binary profile nine, the eliminated
encoding has terminal inventory

```text
state 0: 10, state 1: 11, state 2: 9.
```

Unary-to-unary edges are consecutive nested state-1 support terminals.  Their
exact aggregate remains `638045608200`, with mean `110/29`.

### Clean-macro shells

The unit source services `A,B,C` force identity incidence.  This transfers the
three `ABC` phase buffers and the `AABBC` optimum without an extra incidence
fixture.  The least `l_1` buffer remains `6/5`.

### Integration

Candidate completion is now `23/30`, with internally complete repository-typed
models for Hall, prefix, and shell.  All six actual global rows remain
`fixture_derived`, so zero rows are promoted and geometric closure remains
false.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_573_578.py
```

or individually with

```bash
python scripts/check_boundary_inherited_line_states.py
python scripts/check_hall_complete_grid_extensions.py
python scripts/check_threshold_source_cell_normals.py
python scripts/check_prefix_support_leaf_risk_decoder.py
python scripts/check_shell_source_action_bridge.py
python scripts/check_geometric_decoder_evidence_gate.py
```

The next available theorem identifier is `PP3crh`.
