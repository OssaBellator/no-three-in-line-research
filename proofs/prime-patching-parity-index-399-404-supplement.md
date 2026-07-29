# Prime-patching parity index supplement: `docs/399--404`

This supplement extends the cumulative parity index and the `docs/391--398`
supplements without replacing their history.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3bwi--PP3bwk | A fixed-signature boundary-conflict packing has exact role mass and yields either a heavy fixed boundary role or a large bank of witness paths disjoint outside the common owner skeleton | PROVED | `docs/399-fixed-signature-boundary-witness-hub-or-disjoint-bank.md` |
| PP3bwl--PP3bwo | Canonical overlap-walk potentials give monotonically improving finite-depth Hall congestion certificates converging to the exact Perron constant; failure has a bounded-depth rooted overlap-walk witness | PROVED | `docs/400-finite-depth-overlap-walk-potentials-for-hall-congestion.md` |
| PP3bwp--PP3bwr | Direct-clean fractional reverse load is bounded by degree and total codegree load; strict expansion failure forces one source with quadratic-scale common-target reuse | PROVED | `docs/401-codegree-expansion-for-fractional-direct-clean-layers.md` |
| PP3bws--PP3bwu | General support-chord geometry compresses to at most `L(L+1)=O(log^2 m)` dihedral and support-swap invariant dyadic types; one type carries the corresponding weighted fraction | PROVED | `docs/402-dyadic-support-chord-scale-localization.md` |
| PP3bwv--PP3bwy | Shell products have an exact exceedance-tail layer cake, a rational multiscale count envelope, a strong-count/mild-excess hybrid, and an invariant-drop conversion to bad-shell counts | PROVED | `docs/403-multiscale-shell-exceedance-profiles.md` |
| PP3bwz--PP3bxc | Reverse loads multiply under kernel composition, average under mixtures, lose at most inverse retained mass under conditioning, and pay only actual target-support overlap across structural types | PROVED | `docs/404-typed-kernel-load-composition-for-frontier-integration.md` |

## Frontier update

### Boundary recleaning

The constant-loss fixed-signature core from `docs/398` is no longer merely a
dense relation.  If its packing weight is `Lambda` and boundary-component size
is at most `L`, then either one fixed endpoint/bridge role has load at square-root
scale or there is a bank of size

```text
Omega(sqrt(Lambda/L))
```

whose paths are boundary-disjoint outside their common owner skeleton.  The next
geometric conversion can split into a hub branch and a disjoint-petal branch.

### Localized Hall transport

The Perron congestion constant now has canonical finite-depth certificates

```text
c_0>=c_1>=c_2>=...->lambda.
```

Depth zero is average target multiplicity.  Each additional depth incorporates
one more normalized overlap step.  A failed depth bound returns one rooted
bounded-depth overlap-walk tree, giving a local mesoscopic obstruction.

### Fractional direct-clean layers

If every source has degree at least `d` and total codegree load at most `L`, then

```text
lambda_* <= (d+L)/d^2.
```

This supplies a finite fractional layer bank whenever the right side is below
one.  Failure localizes to one source with large total common-target mass, merging
the layer-bank and Hall-congestion frontiers.

### Support-chord words

The exact chord distances have `Theta(m^2)` possible pairs, but only
`O(log^2 m)` dyadic types.  After this loss one has a fixed alternation pattern
and two factor-two-comparable chord scales.  Word templates and collision bounds
may now be developed scale by scale.

### Clean-macro shells

One no longer needs a single per-shell ceiling or one total excess number.  The
complete exceedance-count profile controls the product, while contractive shells
retain exact credit.  A decreasing invariant may bound only the number of gates
above each expansion threshold and still close the trajectory.

### Integration

Finite structural decompositions do not automatically cost their number of
types.  If type-specific repair target reservoirs have overlap multiplicity `h`,
the combined reverse load pays only `h`; target-disjoint reservoirs pay no type
loss.  Conditioning, type combination, and multistage composition now have one
explicit product criterion.

## Exact diagnostics

```bash
python scripts/check_fixed_signature_boundary_witness_bank.py \
  experiments/fixed-signature-boundary-witness-example.json
python scripts/check_overlap_walk_potentials.py
python scripts/check_direct_clean_codegree_expansion.py \
  experiments/direct-clean-codegree-example.json
python scripts/check_support_chord_dyadic_localization.py
python scripts/check_multiscale_shell_exceedance.py
```

The next available theorem identifier is `PP3bxd`.
