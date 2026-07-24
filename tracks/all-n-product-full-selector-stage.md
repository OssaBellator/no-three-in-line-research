# All-n product track: full-selector stage

**Branch:** `research/all-n-product-construction`

This stage follows the complete arbitrary-map one-inner-layer classification
through base side eight. It moves to the complete four-layer host and records
closures that genuinely require mixed selectors.

## Current ledger

| Item | Current status |
|---|---|
| PC1 | **COMPLETE.** Arbitrary blockwise digit maps preserve the four-regular host, and every spanning degree-two state is saturated and decomposes into two permutation layers. |
| PC2 | **SUBSTANTIAL STRUCTURAL REDUCTION.** The complete side-two-outer host has normal form `Q^j T H^s P^i`; factor dependence is only the relative cycle type of `H`. The degree-two selector has an exact nine-state transfer matrix on every relative cycle. |
| PC3 | **MIXED.** The arbitrary-map one-inner-layer family is completely classified through base side eight and fails at `3,6,7,8`. The full selector succeeds universally at base three and for the side-six 6-cycle factor class. |
| PC4 | **THREE UNIVERSAL SPECIAL CLOSURES PLUS ONE FACTOR CLASS.** Products `2 x 3 -> 6`, `2 x 4 -> 8`, and `2 x 5 -> 10` are factor-independent. Product `2 x 6 -> 12` is proved for all side-six factors of relative 6-cycle type. No infinite multiplicatively closed family is known. |
| PC5 | **OPEN.** The special closures and finite witnesses do not imply arithmetic coverage. |
| PC6 | **REFORMULATED AGAIN.** Full-selector feasibility is classified per relative cycle type and geometric parameters `T,P,Q`; repair/resampling remains open for arbitrary mixed selectors. |

## Full-host normal form

For an inner factor `(tau_0,tau_1)` and arbitrary row/column block maps, define

\[
T=\beta_0\tau_0\alpha_0^{-1},
\qquad
P=\alpha_0\alpha_1^{-1},
\qquad
Q=\beta_1\beta_0^{-1},
\]

\[
H=\alpha_0\tau_0^{-1}\tau_1\alpha_0^{-1}.
\]

PX50 proves that the two inner-layer maps in coarse block `(i,j)` are exactly

\[
Q^j T H^s P^i,
\qquad s\in\{0,1\}.
\]

Conversely, `T,P,Q` are arbitrary and `H` may be any conjugate of the factor's
relative permutation. Therefore full-selector geometry depends on the factor
only through relative cycle type.

## Universal side-three closure

Every side-three factor has a fixed-point-free relative permutation, hence a
3-cycle. All such factors transport to one canonical crossed host with selected
permutation layers

\[
(1,5,3,0,4,2),
\qquad
(3,1,5,2,0,4).
\]

PX51 proves

\[
\boxed{2\times3\longrightarrow6}.
\]

This closure is genuinely beyond PX28: the complete one-inner-layer family is
infeasible at base three.

## Closed one-layer boundary

PX49 completes the arbitrary-map PX28 classification through base eight:

| Base side | One-inner-layer template |
|---:|---|
| 2 | yes |
| 3 | no |
| 4 | yes |
| 5 | yes |
| 6 | no |
| 7 | no |
| 8 | no |

Thus the `2 x 4 -> 8` closure cannot iterate to side sixteen inside PX28.

## Abstract mixed-selector transfer system

For one relative cycle of length `L`, PX54 gives the exact selector count

\[
A_L
=
2+2\cdot4^L
+(4+2\sqrt3)^L
+(4-2\sqrt3)^L.
\]

Counts multiply over the cycles of `H`. At side six this gives:

| Relative type | Abstract degree-two states |
|---|---:|
| `(6)` | 181,122 |
| `(4,2)` | 325,620 |
| `(3,3)` | 298,116 |

The selector count is independent of `T,P,Q`; those permutations control the
real-grid geometry and the collinearity constraints.

## Side-six restricted obstruction and mixed success

PX52 reduces one-outer-layer states to two independently relabelled saturated
factors of the same relative type. The 116 ordered side-six factors split as:

| Relative type | Count |
|---|---:|
| `(6)` | 84 |
| `(4,2)` | 16 |
| `(3,3)` | 16 |

PX53 exhausts all 60,544 one-outer-layer states and finds none no-three.

The complete affine full-selector census then tests all

\[
3\cdot4\cdot12^3=20,736
\]

hosts with `T,P,Q` affine on `Z/6Z`. PX56 finds exactly one feasible host:
relative type `(6)`, orientation `ff`, and

\[
T=(2,1,0,5,4,3),
\qquad
P=Q=(5,4,3,2,1,0).
\]

Its no-three state has permutation layers

\[
(2,7,0,6,10,8,3,1,5,11,4,9),
\]

\[
(4,6,9,3,0,10,1,11,8,2,5,7).
\]

PX57 transports this same side-twelve certificate to all 84 ordered side-six
factors of relative 6-cycle type. The selector uses both outer and both inner
layers and is therefore genuinely mixed.

## Exact next targets

1. **Remaining side-six cycle types.** Determine whether arbitrary `T,P,Q` give a
   full-selector template for `(4,2)` or `(3,3)`. The affine family is already
   proved empty for both.
2. **Structured extension of the 6-cycle template.** Identify a map group or
   recurrence containing the unique affine template and applicable at infinitely
   many cycle lengths.
3. **Geometric transfer refinement.** Enrich the nine-state selector transfer
   matrix with line or carry signatures so selector states and `T,P,Q` can be
   searched jointly.
4. **Repair/resampling.** Develop a conflict-aware theorem for the complete host
   normal form, distinguishing feasible cycle types from structured infeasible
   cores.
5. **Arithmetic coverage.** Convert an infinite cycle-type closure family into
   coverage of all side lengths; no such family is currently known.

## Verification

```bash
python scripts/verify_product_full_host_normal_form.py
python scripts/verify_product_one_outer_layer_six.py
python scripts/verify_product_selector_transfer.py
python scripts/verify_product_affine_full_selector_six.py
python scripts/verify_product_unrestricted_eight.py --orientation cc
python scripts/verify_product_unrestricted_eight.py --orientation cf
python scripts/verify_product_unrestricted_eight.py --orientation ff
```

The crossed `fc` base-eight case follows from `cf` by scalar transposition. The
overall no-three-in-line conjecture remains open.
