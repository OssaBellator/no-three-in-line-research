# All-n product track: affine closure stage

**Branch:** `research/all-n-product-construction`

This update supersedes the earlier statement that PC4 had no factor-independent
positive case. It should be read with
[`tracks/all-n-product-construction.md`](all-n-product-construction.md) and the
product theorem index.

## Updated ledger

| Item | Current status |
|---|---|
| PC1 | **COMPLETE / EXTENDED.** Arbitrary blockwise fine-digit permutations preserve the four-regular product host; every spanning degree-two state is saturated and decomposes into two permutation layers. |
| PC2 | **SUBSTANTIAL PARTIAL.** Exact determinant, projection-fibre, direction, line, and pair-codegree bounds are proved. Global resonance elimination remains open. |
| PC3 | **PARTIAL POSITIVE / RESTRICTED ROUTES REFUTED.** Non-global digit maps remove the unmodified `2 x 5` defect gap. Global radix phases, unmodified full hosts, and the normalized affine canonical full-selector family still have exact obstructions. |
| PC4 | **SPECIAL CLOSURE PROVED.** Every saturated side-five factor composes with the saturated side-two factor to a saturated no-three side-ten configuration using blockwise affine maps and one chosen inner layer. No infinite multiplicative closure class is known. |
| PC5 | **OPEN / FINITE COVERAGE.** Exact product-derived configurations now include sides 6, 8, 9, and 10. The special `2 x 5` theorem does not yield arithmetic coverage by itself. |
| PC6 | **SUBSTANTIAL PARTIAL.** Full repair-state connectivity, exact collateral, bounded projection fibres, finite bounded-support batches, and unsatisfiable-core certificates are available. A general resampling-or-infeasibility theorem remains open. |

## From non-affine escape to universal closure

PX33 exhausts normalized arbitrary second-block permutations at `2 x 5`. It
finds seven successful parameter states, five scalar configurations, and an
explicit non-affine escape for the canonical factor that remains impossible in
the normalized affine full-selector family.

The factor-independent theorem uses a different normalization in which all four
block maps may be nontrivial. Let

\[
H=\operatorname{AGL}(1,5)
\]

and

\[
t=(2,4,0,3,1).
\]

Theorem PX34 proves

\[
S_5=H\sqcup HtH,
\]

where the 100-element double coset is exactly the non-affine permutations.
Every affine permutation graph in `[5]^2` already contains a collinear triple,
so every permutation layer occurring in a saturated side-five factor belongs
to `HtH`.

For either layer `tau` of an arbitrary saturated side-five factor, choose
`alpha_0,beta_0 in H` with

\[
\beta_0\tau\alpha_0^{-1}=t.
\]

Set

\[
\alpha_1=\rho\alpha_0,
\qquad
\beta_1=\rho\beta_0,
\qquad
\rho(u)=4-u,
\]

then use orientation `ff` and the explicit one-inner-layer construction PX28.
PX35 proves that the resulting configuration is the exact saturated no-three
side-ten witness.

This gives the factor-independent operation

\[
\boxed{2\times5\longrightarrow10.}
\]

PX38 abstracts the argument: any successful normalized template transports to
its complete map-group double coset. Covering all admissible factor layers by a
bounded set of successful double cosets is therefore a sufficient closure
criterion.

## Exact affine boundary

The mechanism is not a generic doubling theorem. PX36 normalizes the complete
four-block affine one-inner-layer family to identity first blocks. PX37 then
exhausts:

\[
414{,}720
\]

states at base side six and

\[
35{,}562{,}240
\]

states at base side seven, finding no no-three state.

Thus the next target is not “repeat the side-five affine proof.” A useful
extension must instead identify another digit-map group and target double coset,
use non-affine maps, exploit both inner layers, or combine blockwise maps with
full-selector resampling.

## Exact next targets

1. **Group-orbit coverage.** Find infinitely many side lengths `n` for which a
   manageable map group has successful target double cosets covering every
   permutation layer that may occur in a saturated factor.
2. **Two-layer affine selection.** Determine whether both inner layers and the
   full exact selector can overcome the affine one-layer obstruction at base
   six or seven.
3. **Core-directed map choice.** Convert the 35-line canonical `2 x 5` core into
   a symbolic projection pattern and prove which block maps necessarily break
   it.
4. **Iterability.** Construct a product operation that accepts the side-ten
   output as a new factor, rather than proving only the isolated multiplication
   `2 x 5`.

## Verification

```bash
python scripts/verify_product_nonaffine_one_layer.py
python scripts/verify_product_affine_side_five_closure.py
python scripts/verify_product_affine_one_layer_obstruction.py --side 6
python scripts/verify_product_affine_one_layer_obstruction.py --side 7 --workers 8
python scripts/verify_product_blockwise_reversal.py
python scripts/verify_product_2x5_unsat_core.py
```

The completion criterion for the overall track remains unmet: no infinite
closure class or arithmetic coverage theorem has been proved.
