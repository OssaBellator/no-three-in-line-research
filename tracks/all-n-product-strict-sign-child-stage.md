# All-n product track: strict-sign-or-child stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`tracks/all-n-product-terminal-core-stage.md`](all-n-product-terminal-core-stage.md).
PX294--PX313 close the realized-collateral and diffuse selected-packet
strict-sign-or-child interfaces.  The only remaining unresolved objects are
finite weighted trajectory-saturated terminal templates and the final global
assembly.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Weighted trajectory reset | **CONTROLLED** | PX294--PX298 permit a historical return when cycle destruction exceeds recurrence load; failure forces a heavy historical star field or a small exact basin. |
| Bounded-overlap collateral | **CLOSED** | PX299--PX302 color every excess family into finitely many endpoint-disjoint typed child batches. |
| High-overlap collateral | **CLOSED** | PX303--PX306 convert one high-overlap endpoint into a loaded line or quantitative clean-star child. |
| Realized rank-at-most-three strict-sign-or-child | **PROVED** | PX306 handles every realized collateral family. |
| Packet release dependence | **SHARPENED** | PX307--PX309 replace packet count by row/column incidence and total packet-event energy. |
| Diffuse selected packet defects | **CLOSED** | PX310--PX313 release only active packet arcs; bounded overlap gives one joint release and high overlap gives loaded-line/star geometry. |
| Terminal weighted census | **OPEN FINITE** | Small trajectory-saturated basins still require exact weighted reset/absorber classification. |
| Constant assembly | **OPEN** | Fixed thresholds `K,m_0,B,Q` and residual spread constants must be placed into one global statement. |
| PX63 insertion | **OPEN** | The terminating decoder has not yet been written into the product-closure theorem. |
| Infinite exact closure | **OPEN** | No unconditional all-side product theorem is claimed. |

## 1. Hybrid reset potential

The terminal reset potential is ordered by

\[
\left(
\sum_j(U_j+d_j),
(U_0,d_0,U_1,d_1,\ldots)
\right).
\]

Ordinary causal child transitions preserve or lower the total and decrease the
lexicographic coordinate.  A historical cycle reset may revive a shallower
certificate, but is allowed whenever it destroys more total current obligation
weight than it recreates.

For a sink `v`, a historical return edge `v->c` closing an allowed path `P`
strictly improves when

\[
h_{v,c}<\sum_{x\in P}a_x.
\]

Failure produces heavy historical return cells in row `v`; long paths force one
large return star, while large reverse basins force a coordinate field.

## 2. Complete realized-collateral conversion

A rank-at-most-three certificate uses at most six endpoint labels.  If maximum
endpoint overlap is `Lambda`, all excess certificates split into at most

\[
6\Lambda-5
\]

support-disjoint batches and at most

\[
2Q(6\Lambda-5)
\]

single-type child blocks.

If overlap is larger than `B=4Km_0`, one endpoint label forces one selected cell
into more than `B/2` triples.  Either a line through that cell is loaded or a
line-by-line matching extracts a clean star of order greater than `m_0`.

Thus every realized collateral family gives immediate sign, bounded-overlap
children, loaded-line improvement, or a clean-star child.

## 3. Active packet normalization

For one packet level of old selected defect load `d_alpha`, retain only packet
arcs appearing in selected crosses.  PX310 gives active size

\[
|A_\alpha|=2d_\alpha.
\]

The maximum active packet incidence is at most actual old-defect endpoint
overlap.  If it is bounded by `B`, all active packet cores release jointly with
cylinder factor at most

\[
e^{4\Delta+4B}.
\]

If it exceeds `B`, PX305 gives loaded-line or clean-star geometry.  Blocks below
`32max(1,Delta,B)` are terminal exact instances.

This removes the candidate-energy packet-count barrier from the actual decoder:
inactive packet arcs are never paid.

## 4. Immediate frontier

1. **Weighted terminal census.**  Enumerate trajectory-saturated small basins
   with recurrence loads and test every allowed historical reset, principal
   cycle, Hall absorber, and coupled two-block move.
2. **Census-to-theorem conversion.**  Identify a finite family of minimal frozen
   weighted templates or prove none survive the exact optimizer.
3. **Constant assembly.**  Choose fixed `K,m_0,B,Q` and state one quantitative
   recursion theorem with all spread thresholds.
4. **PX63 insertion.**  Replace the former open decoder hypothesis by the
   assembled strict-sign-or-child and terminal statements.

## 5. Verification

```bash
python scripts/verify_product_weighted_historical_reset.py
python scripts/verify_product_bounded_overlap_batching.py
python scripts/verify_product_high_overlap_cell_star.py
python scripts/verify_product_incidence_weighted_packet_release.py
python scripts/verify_product_active_packet_core.py
```

All five verifiers pass locally.  The classical no-three-in-line conjecture and
exact infinite product closure remain open.