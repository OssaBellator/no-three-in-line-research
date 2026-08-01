# Prime-patching parity index supplement: `docs/615--620`

This supplement continues the cumulative PP3 index after `docs/614`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cvl--PP3cvn | Corrected six-block states have six minimum-four seventh candidates, one canonical six-point corrected transition, and no raw eighth extension | PROVED | `docs/615-corrector-aware-boundary-transition-census.md` |
| PP3cvo--PP3cvq | `K_4,4` minus two partial matchings survives one further edge exclusion, giving an explicit six-resource conditional Hall interface | PROVED / PROVED UNDER HOST CONDITION | `docs/616-two-matching-spare-resource-hall-lemma.md` |
| PP3cvr--PP3cvt | The eight nearest legal degree-four threshold matrices are exactly unit alternating three-cycle trades | PROVED / PROVED UNDER SOURCE ACTION | `docs/617-source-preserving-threshold-three-cycle-trades.md` |
| PP3cvu--PP3cvw | Every unary-run composition has a row-column-distinct two-anchor chord lift with eleven anchored blockers per encoding | PROVED | `docs/618-synthetic-source-anchor-support-chords.md` |
| PP3cvx--PP3cvz | Signed cancellation, fixed-column optimization, and coordinate permutation preserve the even-sum shell source lattice | PROVED | `docs/619-signed-permuted-shell-source-lattice.md` |
| PP3cwa--PP3cwc | Candidate completion remains `24/30`, no actual row is promoted, and fixture arithmetic slack remains positive | PROVED | `docs/620-composition-source-generation-evidence-gate.md` |

## Frontier update

### Boundary recleaning

The corrector-aware state graph is no longer empty.  Of 2,080 seventh-block
attempts, six have minimum conflict-transversal size four, with eighty-two
minimum transversals total.  Under the canonical lexicographic transversal rule,
one attempt admits a six-point degree-preserving correction.  The resulting
state has no raw eighth-block extension.

### Localized Hall transport

A six-resource conditional host leaves `K_4,4` after selecting the local pair.
If the restricted partner fibre and source exclusions are both partial
matchings, every one of the 43,681 ordered forbidden-family pairs has a perfect
matching and survives one additional cell exclusion.

### Fractional direct-clean layers

The nearest legal degree-four replacements no longer require a fifth slot.
Exactly eight exist, and each is one unit alternating three-cycle trade moving
three source-cell units while preserving all row and column margins.  The missing
object is now an actual geometric trade operation.

### Support-chord repair words

Adding two synthetic anchors to every unary-run line gives an exact source-pair
blocking interpretation.  All anchors and inserted points use distinct rows and
columns, cross-run triples vanish, and every encoding has eleven anchored
blockers.  The anchors remain synthetic.

### Clean-macro shells

Allowing signed cancellations and arbitrary relabelling of the cycle coordinates
does not escape the determinant-two lattice.  Every generated integer vector has
even coordinate sum.  A genuinely new source column remains necessary.

### Integration

Candidate-field completion remains `24/30`.  Every direct row remains
fixture-derived, so geometric closure remains false despite unchanged positive
arithmetic slack.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_615_620.py
```

or individually with

```bash
python scripts/check_boundary_corrector_transition_state.py
python scripts/check_hall_two_matching_exclusion_lemma.py
python scripts/check_threshold_three_cycle_replacements.py
python scripts/check_prefix_source_anchor_chords.py
python scripts/check_shell_signed_permutation_lattice.py
python scripts/check_composition_source_generation_evidence_gate.py
```

The next available theorem identifier is `PP3cwd`.
