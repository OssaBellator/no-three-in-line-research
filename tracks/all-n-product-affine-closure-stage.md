# All-n product track: template and affine closure stage

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
| PC3 | **PARTIAL POSITIVE / RESTRICTED ROUTES REFUTED.** Non-global digit maps remove the unmodified `2 x 5` defect gap and supply normalized templates at base sides 2, 4, and 5. Global radix phases, unmodified full hosts, and several affine families still have exact obstructions. |
| PC4 | **TWO SPECIAL CLOSURES PROVED.** Every saturated side-four factor composes with side two to side eight using arbitrary block permutations. Every saturated side-five factor composes with side two to side ten using blockwise affine maps. No infinite multiplicative closure class is known. |
| PC5 | **OPEN / FINITE COVERAGE.** Exact product-derived configurations include sides 6, 8, 9, and 10. The two special doubling theorems do not yield arithmetic coverage by themselves. |
| PC6 | **SUBSTANTIAL PARTIAL.** Full repair-state connectivity, exact collateral, bounded projection fibres, finite bounded-support batches, and unsatisfiable-core certificates are available. A general resampling-or-infeasibility theorem remains open. |

## 1. Gauge normalization and template universality

PX39 proves a full permutation-level gauge identity. Any one-inner-layer state
with arbitrary block maps is literally equal to a normalized state with first
row and column block maps equal to the identity.

PX40 exhausts the normalized family through base side five:

| Base side | Successful parameters | Scalar configurations |
|---:|---:|---:|
| 2 | 16 | 9 |
| 3 | 0 | 0 |
| 4 | 4 | 4 |
| 5 | 8 | 5 |

PX41 applies PX38 with the full symmetric group. Since

\[
\operatorname{Sym}([n])\,t\,\operatorname{Sym}([n])
=
\operatorname{Sym}([n]),
\]

one successful normalized template transports every fine permutation and hence
every permutation layer of every saturated factor at that side.

Using the side-four template

\[
t=(1,3,0,2),
\qquad
r=s=\operatorname{id},
\qquad
\theta=ff,
\]

PX42 proves

\[
\boxed{2\times4\longrightarrow8.}
\]

The exact side-eight output layers are

\[
(2,3,6,7,0,1,4,5)
\]

and

\[
(3,2,7,6,1,0,5,4).
\]

## 2. From non-affine escape to structured side-five closure

PX33 exhausts normalized arbitrary second-block permutations at `2 x 5`. It
finds seven successful parameter states, five scalar configurations, and an
explicit non-affine escape for the canonical factor that remains impossible in
the normalized affine full-selector family.

The factor-independent structured theorem uses nontrivial affine maps in all
four blocks. Let

\[
H=\operatorname{AGL}(1,5)
\]

and

\[
t=(2,4,0,3,1).
\]

PX34 proves

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
PX35 proves

\[
\boxed{2\times5\longrightarrow10.}
\]

The exact output is the side-ten witness already recorded in the finite
certificate ledger.

PX38 abstracts both mechanisms: successful normalized templates transport to
map-group double cosets. Template existence and double-coset coverage are the
two exact inputs for a general special closure theorem.

## 3. Exact affine boundary

The side-five affine mechanism is not a generic doubling theorem. PX36
normalizes the complete four-block affine one-inner-layer family to identity
first blocks. PX37 then exhausts

\[
414{,}720
\]

states at base side six and

\[
35{,}562{,}240
\]

states at base side seven, finding no no-three state.

The unrestricted template family is larger: PX40 proves a template obstruction
at base side three but does not settle base sides six, seven, or eight. The
reflection and affine subfamilies are insufficient at those sizes.

## Exact next targets

1. **Template existence at new bases.** Determine whether arbitrary block
   permutations give a normalized template at base side six, seven, or eight.
2. **Iterability at eight.** A successful base-eight template would combine with
   PX42 to continue the doubling route from side eight to side sixteen.
3. **Structured map groups.** Replace full symmetric maps by smaller groups whose
   successful template double cosets still cover every admissible factor layer.
4. **Two-layer selection.** Determine whether both inner layers and the full
   exact selector overcome one-layer template obstructions.
5. **Core-directed map choice.** Convert the canonical 35-line core into a
   symbolic projection pattern and prove which block maps necessarily break it.

## Verification

```bash
python scripts/verify_product_gauge_census.py
python scripts/verify_product_universal_side_four_closure.py
python scripts/verify_product_nonaffine_one_layer.py
python scripts/verify_product_affine_side_five_closure.py
python scripts/verify_product_affine_one_layer_obstruction.py --side 6
python scripts/verify_product_affine_one_layer_obstruction.py --side 7 --workers 8
python scripts/verify_product_2x5_unsat_core.py
```

The completion criterion for the overall track remains unmet: no infinite
closure class or arithmetic coverage theorem has been proved.
