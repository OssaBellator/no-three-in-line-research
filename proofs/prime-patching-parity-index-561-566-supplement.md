# Prime-patching parity index supplement: `docs/561--566`

This supplement continues the cumulative parity index after `docs/560`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cpf--PP3cph | Explicit four- and seven-side saturated blocks admit a finite port/seam census, and every naive diagonal dihedral seam is obstructed | PROVED | `docs/561-coordinate-level-four-seven-boundary-seam-attempt.md` |
| PP3cpi--PP3cpk | An independently defined six-state cylinder gadget has a complete transition census, a unique common pair-lumping, and exact switched quotient commutation | PROVED | `docs/562-independent-cylinder-microcensus-for-hall-gadgets.md` |
| PP3cpl--PP3cpn | Threshold layer sums are reorder-invariant, the stored source and transient alphabets differ, and bounded physical normals admit an exact quotient-coverage census | PROVED / ONE LINEAGE IDENTITY REFUTED | `docs/563-source-layer-alignment-for-threshold-schedules.md` |
| PP3cpo--PP3cpq | Original leaf grading and encoded node grading are reconciled by a size-preserving unary-binary encoding, which admits an exact unary-run risk DP | PROVED AFTER DUAL-GRADING CORRECTION | `docs/564-corrected-node-grading-and-risk-marked-prefix-dp.md` |
| PP3cpr--PP3cpt | A full-rank nonprecancelled shell benchmark has an exact physical trajectory, order optimum, and identifiable reserve certificate | PROVED FOR THE BENCHMARK | `docs/565-nonprecancelled-shell-incidence-benchmark.md` |
| PP3cpu--PP3cpw | Independent extraction completes 22 of 30 candidate fields, preserves positive arithmetic slack, and keeps the geometric evidence gate closed | PROVED | `docs/566-fieldwise-evidence-gate-after-independent-extraction.md` |

## Frontier update

### Boundary recleaning

Two coordinate-level saturated blocks were independently enumerated:

```text
P: side 4, eight points,
Q: side 7, fourteen points.
```

Both have two points per row and column and no collinear triple.  Each has four
distinct dihedral variants.  All sixty-four ordered diagonal seams fail; the
most common first-witness slope is one, occurring twenty-nine times.  Thus the
simplest diagonal realization of the four/seven semigroup is ruled out.

### Localized Hall transport

Microscopic states are defined before the quotient as `(syndrome mod 3,
orientation mod 2)`, with four explicit local choices.  The complete pair of
`6 x 6` transition matrices has thirty-six positive entries with choice
witnesses.  Of all fifteen pair partitions, only the syndrome fibres are
strongly lumpable for both gadgets, and they recover the stored quotient
matrices exactly.

### Fractional direct-clean layers

The stored `docs/521` decomposition sums to its conservative matrix `M`, while
the four distinct cyclic layers in `docs/527` sum to the all-ones matrix.  No
reordering can identify the fixtures.  In the later four-layer coordinates,
only six of 1120 canonical primitive normals with coefficients in `[-3,3]`
factor through the two-observable quotient.

### Support-chord repair words

The original automaton series remains leaf-graded.  Its eliminated equation also
has a size-preserving unary-binary encoding in which the same exponent is encoded
total-node count.  At original leaf count and encoded size thirty with nine
encoded binary nodes, the family size is `168212023980`; the encoding has eleven
unary nodes and ten encoded leaves.  An exact DP marks encoded unary-to-unary
edges, gives mean risk `110/29`, certifies `153857776072` objects with risk at
most five, and reconstructs a risk-zero encoding.

### Clean-macro shells

The multiset `A,A,B,B,C` is mapped through the full-rank incidence matrix

```text
((1,0,1),(0,1,1),(1,1,0)).
```

The physical word is not precancelled.  Among all thirty orders, ten attain
minimum physical `l_1` reserve `6/5`; the lexicographic optimum `ABABC` has
buffer `(2/5,4/5,0)`.

### Integration

The exact fixture fixed point still totals

```text
705466760524005697 / 3623878655999606784
```

and remains below `1/4`.  Independent extraction covers 22 of 30 candidate
source fields, with internally complete encoded-prefix and benchmark-shell
models.  No actual global row is promoted, so geometric closure remains false.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_561_566.py
```

or individually with

```bash
python scripts/check_boundary_coordinate_seam_attempt.py
python scripts/check_independent_hall_microcensus.py
python scripts/check_threshold_source_layer_alignment.py
python scripts/check_node_graded_prefix_risk_dp.py
python scripts/check_nonprecancelled_shell_incidence.py
python scripts/check_independent_extraction_evidence_gate.py
```

The local audits cover sixty-four boundary seams, all fifteen Hall pair
partitions and 511 switch words, 1120 bounded primitive threshold normals, the
full thirty-size encoded prefix risk distribution, all thirty shell orders with
five hundred repeated prefixes, and the exact six-row fixed point.

The next available theorem identifier is `PP3cpx`.
