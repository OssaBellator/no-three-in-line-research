# Prime-patching parity index supplement: `docs/609--614`

This supplement continues the cumulative parity index after `docs/608`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cut--PP3cuv | The sharp radius-32 boundary seam has exact degree-preserving six-point correctors, and the corrected states have no raw seventh-block extension in the audited radius | PROVED | `docs/609-sharp-six-point-boundary-seam-corrector.md` |
| PP3cuw--PP3cuy | A five-resource conditional Hall host with matching-shaped residual partner fibre survives one further exclusion, including all twelve lifted source-fixture choices | PROVED | `docs/610-spare-resource-conditional-hall-lemma.md` |
| PP3cuz--PP3cvb | An integer cell dual proves the legal threshold augmentation cannot be amortized below one layer per source period | PROVED | `docs/611-threshold-augmentation-nonamortization-dual.md` |
| PP3cvc--PP3cve | Unary-run incidences admit row-column-distinct integer embeddings with zero cross-run triples and exact aggregate collinearity | PROVED | `docs/612-row-column-distinct-unary-run-geometry.md` |
| PP3cvf--PP3cvh | Parametric, quantized, and chamber-stable shell operations retain the fixed even-sum source-action lattice | PROVED | `docs/613-fixed-column-shell-source-type-obstruction.md` |
| PP3cvi--PP3cvk | Candidate completion rises to 24/30, fixture arithmetic is unchanged, and zero actual rows are promoted | PROVED | `docs/614-source-resource-realization-evidence-gate.md` |

## Frontier update

### Boundary recleaning

The four sharp radius-32 sixth-block repairs now have exact row- and
column-degree-preserving correctors.  Six deleted points and six refill points
are necessary and sufficient in the audited degree-support class.  The corrected
forty-eight-point states remain terminal under all 2,080 raw seventh-block
attempts in the same radius.

### Localized Hall transport

A source-typed spare-resource condition is now isolated.  After the local pair
uses two resources, a residual `K_3,3` minus any partial matching has between two
and six perfect matchings and survives one further cell exclusion.  All twelve
choices of the best lifted binary-resource-star fixture satisfy this condition.

### Fractional direct-clean layers

The fifth legal threshold layer cannot be shared among source periods.  The
integer dual matrix

```text
(( 3, 1, 2, 0),
 ( 0, 0, 0,-1),
 (-1,-3,-1,-3),
 ( 1, 0, 0, 0))
```

scores the source matrix by three, every legal layer by at most zero, and every
augmentation by at least minus three.  Thus `k` source periods require at least
`k` augmentation layers.

### Support-chord repair words

All 1,024 ordered compositions of the eleven unary nodes now have canonical
integer embeddings with distinct rows and columns.  Runs are collinear, cross-run
triples are absent, and the exact thirty-node profile aggregate remains
`396499770810`, with mean `33/14`.

### Clean-macro shells

The shell source-type obstruction now covers the wider chain through `docs/499`,
`505`, `511`, and `517`.  Parametric targets, coefficient quantization, and
chamber stability keep the same three action columns, whose integer image is
exactly the even-coordinate-sum lattice.

### Integration

Candidate field completion rises from `23/30` to `24/30` because the stored
boundary fixture now has a complete degree-preserving seam corrector.  All six
actual rows remain fixture-derived.  The fixed-point total and positive slack are
unchanged, and geometric closure remains false.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_609_614.py
```

or individually with

```bash
python scripts/check_boundary_six_point_corrector.py
python scripts/check_hall_spare_resource_lemma.py
python scripts/check_threshold_nonamortization_dual.py
python scripts/check_prefix_row_column_run_embedding.py
python scripts/check_shell_fixed_column_lattice.py
python scripts/check_source_resource_realization_evidence_gate.py
```

The standalone audits verify four exact boundary correctors and 2,080 seventh
extensions, all thirty-four residual partial matchings, every permutation score,
all 1,024 unary-run compositions, one thousand bounded shell lattice vectors,
and the exact evidence ledger.  The next available theorem identifier is
`PP3cvl`.
