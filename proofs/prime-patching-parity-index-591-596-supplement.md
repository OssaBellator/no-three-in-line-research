# Prime-patching parity index supplement: `docs/591--596`

This supplement continues the cumulative parity index after `docs/590`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3csr--PP3cst | The four sharp boundary repairs have exactly twelve degree-preserving local refills, all obstructed, so wider replacement is necessary | PROVED | `docs/591-saturation-preserving-boundary-refill-obstruction.md` |
| PP3csu--PP3csw | Every complete bijection onto the twelve grid-pair geometries contains six singleton-blocker choices and cannot be uniformly single-exclusion robust | PROVED | `docs/592-complete-grid-hall-robustness-upper-bound.md` |
| PP3csx--PP3csz | The eight nearest legal threshold matrices have exact loss branches `(2,1)` and `(3,0)`, with price frontier `min(2 alpha+beta,3 alpha)` | PROVED | `docs/593-threshold-replacement-price-frontier.md` |
| PP3cta--PP3ctc | Canonical subtree intervals admit a convex laminar chord embedding with zero support-point collinear triples despite positive span risk | PROVED / DECODER MISMATCH | `docs/594-convex-support-chord-embedding-mismatch.md` |
| PP3ctd--PP3ctf | A unit odd-coset shell action completes the lattice, but exact target service requires two uses, one extra active slot, and unchanged minimum buffer | PROVED CONDITIONALLY | `docs/595-minimal-coset-crossing-shell-action.md` |
| PP3ctg--PP3cti | Completion attempts leave candidate coverage at `23/30`, preserve the fixture fixed point, and promote zero global rows | PROVED | `docs/596-completion-attempt-evidence-gate.md` |

## Frontier update

### Boundary recleaning

The sharp three-deletion repairs leave three deficient columns and a row multiset of type `2+1`. There are exactly three degree-preserving refills per repair and twelve overall. Every refill recreates a collinear triple. A successful seam corrector must alter a wider resource neighbourhood.

### Localized Hall transport

The twelve ordered distinct grid-pair geometries intrinsically split into six one-extension and six two-extension cases. Any complete bijection preserves that split. One forbidden residual cell leaves either ten or eleven quotient choices, so relabelling the same grid cannot provide uniform robustness.

### Fractional direct-clean layers

The eight nearest legal matrices split evenly between quotient losses `(2,1)` and `(3,0)`. With nonnegative prices `alpha,beta`, the exact replacement cost is `min(2 alpha+beta,3 alpha)`. No source inequality currently supplies those prices.

### Support-chord repair words

Preorder subtree intervals are laminar. Embedding encoded nodes at `(k,k^2)` gives an explicit convex support-point model with no collinear triple, while the exact aggregate interval span remains `4963626417750`. Span is therefore not itself the required geometric risk.

### Clean-macro shells

Any unit cycle vector crosses the index-two lattice and completes `Z^3`. Exact service of `(12,10,8)` uses the added odd action twice, raises active controls from fifteen to sixteen, and leaves the minimum cycle buffer at `2/5`.

### Integration

Candidate completion remains `23/30`. All direct rows remain fixture-derived, the exact fixed-point total remains

```text
705466760524005697 / 3623878655999606784,
```

and geometric closure remains false.

## Exact diagnostics

Run

```bash
python scripts/check_frontier_591_596.py
```

or the six new audits individually:

```bash
python scripts/check_boundary_saturation_refill_obstruction.py
python scripts/check_hall_bijection_robustness_bound.py
python scripts/check_threshold_replacement_price_frontier.py
python scripts/check_prefix_convex_chord_embedding.py
python scripts/check_shell_coset_crossing_action.py
python scripts/check_completion_attempt_evidence_gate.py
```

The next available theorem identifier is `PP3ctj`.
