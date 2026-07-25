# All-n product track: terminal-core classification stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`tracks/all-n-product-nested-mixed-decoder-stage.md`](all-n-product-nested-mixed-decoder-stage.md).
PX256--PX269 restore the mixed-sector decoder, nested log-log depth, and exact
two-layer spread. PX270--PX293 now classify the terminal matching obstruction,
make terminal optimization exact and subpower, prove causal lexicographic
nonrecurrence, absorb every maximally deficient Hall core, and reduce genuine
immobility to trajectory-saturated rows and columns.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Missing PX256--PX269 bundle | **RESTORED** | Four theorem chapters, four verifiers, the mixed/nested stage ledger, and a theorem-index continuation are committed. |
| Terminal Hall failure | **CLASSIFIED** | PX270 localizes every failure to a complete forbidden rectangle and bounds deficiency by `2Delta-m`. |
| Sharp Hall obstruction | **ABSORBED** | PX271 and PX281--PX283 classify the saturated `K_(Delta,Delta)` core and rematch all but one common label. |
| Maximal near-threshold deficiency | **ABSORBED** | PX284--PX286 delete exactly `r=2Delta-m` common labels and rematch every other endpoint. |
| Terminal exact optimization | **SUBPOWER** | PX273--PX276 enumerate one- and two-block terminal states in `N^o(1)` time and output auditable obstruction certificates. |
| Paid-certificate recurrence | **CLOSED** | PX277--PX280 give causal lexicographic descent; historical positions and packet complements prevent paid defects from returning. |
| Principal trade below Hall threshold | **AVAILABLE** | PX287--PX290 give a directed cycle trade whenever `m>Delta` and an exact subpower cycle optimizer. |
| Cycle-free core | **CLASSIFIED** | PX291--PX293 force a completely forbidden row and column and at least `m-Delta_0` distinct historical positions. |
| Strict-sign-or-child interface | **OPEN** | Diffuse unassigned clean-star/radial and small-packet collateral still needs immediate descent or child conversion. |
| Trajectory-saturated absorber | **OPEN** | Cores with `m<=Delta` and full historical rows/columns need a reset, coupled move, or finite classification. |
| Infinite exact closure | **OPEN** | No all-side product closure follows yet. |

## 1. Terminal Hall structure

For an order-`m` allowed graph with forbidden degree `Delta`, every positive
matching deficiency `delta` produces a complete forbidden rectangle `S x B`
with

\[
|S|+|B|=m+\delta,
\qquad
|S|,|B|\le\Delta.
\]

Hence

\[
\delta\le2\Delta-m.
\]

At equality, both Hall sides have size `Delta`, are saturated, and share at
least `2Delta-m` labels. Deleting those common labels exposes two complete
allowed cross-blocks and gives a principal rematching of all remaining
endpoints.

## 2. Terminal computation

A terminal block has order

\[
m=O(\Delta_0+\log\log N).
\]

The exact one-block rank-at-most-three optimizer costs

\[
O(m!m^6),
\]

and the dependent two-block optimizer costs

\[
O((m!)^2m^6).
\]

Both are `N^o(1)`. Failure is therefore an explicit replayable obstruction,
not an asymptotic black box.

## 3. Causal nonrecurrence

Historical-position constraints form one partial matching per ancestor level.
A designated star, line, radial, coordinate-field, or mixed-shadow certificate
can recur only at its unique historical row position. Packet crosses recur only
as the complementary packet two-cycle. Consequently the designated vector is
lexicographically decreasing and cannot cycle. The remaining debt is solely
unassigned collateral.

## 4. Principal cycle escape

When the current diagonal is forbidden and `m>Delta`, every row has an allowed
off-diagonal cell. The allowed label digraph has minimum outdegree at least one
and therefore contains a directed cycle. This gives an executable principal
cyclic trade moving at least two endpoints even when a full perfect matching
fails.

If no directed cycle exists, the allowed digraph is acyclic and has a sink and
a source. Thus one row and one column are completely forbidden. When the
forbidden graph is a bounded base plus historical position matchings, the
corresponding endpoint has visited at least `m-Delta_0` distinct historical
positions.

## Immediate frontier

1. **Trajectory reset.** Use the full historical row/column to build a composite
   reset trade or coupled-block escape for `m<=Delta`.
2. **Strict-sign-or-child.** Convert every diffuse unassigned linear-sector
   residue into immediate descent or a deeper designated child.
3. **Terminal obstruction census.** Run the PX273/PX290 exact optimizers on the
   trajectory-saturated templates and identify the minimal frozen cores.
4. **Small packet range.** Apply causal lexicographic charging to
   `t<=N^(1/2+o(1))` diffuse packet defects.
5. **Closure conversion.** Assemble the nested decoder and terminal treatment
   into PX63.

## Verification

```bash
python scripts/verify_product_two_block_rainbow_decoder.py
python scripts/verify_product_mixed_rank_three_decoder.py
python scripts/verify_product_nested_recursion_depth.py
python scripts/verify_product_two_layer_regular_spread.py
python scripts/verify_product_terminal_hall_core.py
python scripts/verify_product_terminal_core_optimizer.py
python scripts/verify_product_causal_lexicographic_descent.py
python scripts/verify_product_sharp_hall_absorber.py
python scripts/verify_product_maximal_deficiency_absorber.py
python scripts/verify_product_terminal_cycle_escape.py
python scripts/verify_product_trajectory_saturated_core.py
```

The classical no-three-in-line conjecture and exact infinite product closure
remain open.
