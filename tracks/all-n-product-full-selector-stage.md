# All-n product track: full-selector stage

**Branch:** `research/all-n-product-construction`

This stage follows the complete arbitrary-map one-inner-layer classification
through base side eight.  It moves to the complete four-layer host and records
the first closure that genuinely requires a mixed selector.

## Current ledger

| Item | Current status |
|---|---|
| PC1 | **COMPLETE.** Arbitrary blockwise digit maps preserve the four-regular host, and every spanning degree-two state is saturated and decomposes into two permutation layers. |
| PC2 | **SUBSTANTIAL STRUCTURAL REDUCTION.** The complete side-two-outer host has the exact normal form `Q^j T H^s P^i`; factor dependence is only the relative cycle type of `H`. Projection-fibre, line, carry, and conflict-degree bounds remain available. |
| PC3 | **MIXED.** The arbitrary-map one-inner-layer family is completely classified through base side eight and fails at `3,6,7,8`. The full selector succeeds universally at base three. |
| PC4 | **THREE SPECIAL CLOSURES PROVED.** Factor-independent products `2 x 3 -> 6`, `2 x 4 -> 8`, and `2 x 5 -> 10` are exact. No infinite multiplicatively closed family is known. |
| PC5 | **OPEN.** The special closures and finite witnesses do not imply arithmetic coverage. |
| PC6 | **REFORMULATED AGAIN.** For the full selector, the next classification is per relative cycle type rather than per individual factor. Repair/resampling remains open for genuinely mixed selectors. |

## New full-host normal form

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
relative permutation.  Therefore full-selector geometry depends on the factor
only through relative cycle type.

## Universal side-three closure

Every side-three factor has a fixed-point-free relative permutation, hence a
3-cycle.  All such factors therefore transport to the same canonical crossed
host.  The fixed selected state has permutation layers

\[
(1,5,3,0,4,2),
\qquad
(3,1,5,2,0,4).
\]

PX51 proves the factor-independent closure

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

## One-outer-layer side-six obstruction

PX52 reduces one-outer-layer states to two independently relabelled saturated
factors having the same relative cycle type.  At side six there are exactly 116
ordered factors:

| Relative type | Count |
|---|---:|
| `(6)` | 84 |
| `(4,2)` | 16 |
| `(3,3)` | 16 |

PX53 exhausts all 60,544 choices of two target blocks, orientation, and outer
layer and finds no no-three state.  Hence a successful `2 x 6 -> 12` product
must mix both outer and both inner layers nontrivially.

## Exact next targets

1. **Genuinely mixed side-six selector.** For each of the three relative cycle
   types `(6)`, `(4,2)`, and `(3,3)`, determine whether some `T,P,Q` host has a
   no-three spanning degree-two state.
2. **Selector normal form.** Compress the degree-two selector inside one relative
   cycle component into a lower-dimensional matching, transfer-matrix, or code
   description.
3. **Cycle-type transport.** Prove that one successful mixed template transports
   every factor in its relative conjugacy class, then classify which cycle types
   occur at larger sides.
4. **Repair/resampling.** Develop a conflict-aware selection theorem for the
   complete host normal form, distinguishing feasible cycle types from structured
   infeasible cores.
5. **Arithmetic coverage.** Convert any infinite cycle-type closure family into
   coverage of all side lengths; no such family is currently known.

## Verification

```bash
python scripts/verify_product_full_host_normal_form.py
python scripts/verify_product_one_outer_layer_six.py
python scripts/verify_product_unrestricted_eight.py --orientation cc
python scripts/verify_product_unrestricted_eight.py --orientation cf
python scripts/verify_product_unrestricted_eight.py --orientation ff
```

The crossed `fc` base-eight case follows from `cf` by scalar transposition.  The
overall no-three-in-line conjecture remains open.
