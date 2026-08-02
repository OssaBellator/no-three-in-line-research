# Threshold factorization, exposure, and sign-coherent drift

This chapter consolidates the concurrent threshold audits into one canonical
three-theorem account. It separates transient-buffer scheduling, exposed-cell
sharing, and endpoint displacement.

## PP3czv — Complete three-round buffer factorization

The twenty-four target-buffer incidences of the connected cubic bipartite graph
admit exactly forty-four unordered one-factorizations into three perfect
matchings. Hence there are

```text
44*3! = 264
```

ordered three-round schedules in which every target uses each of its three
available transient cells exactly once and every transient cell is used exactly
once per round. Each incidence has two native swap orders, giving

```text
264*2^24 = 4,429,185,024
```

fully ordered native three-round schedules.

## PP3czw — Matching-independent full-grid exposure

For every one of the forty-nine perfect transient assignments, the union of the
eight seven-cell native footprints is the entire `4 x 4` source grid. The cell
load histogram is independent of the matching:

```text
load 2: eight source-unit cells,
load 5: eight non-unit cells.
```

Thus no distinct-buffer assignment makes the eight target operations disjoint or
reduces the maximum shared-cell load below five. Every round requires protection
of all sixteen source cells.

## PP3czx — Endpoint drift is sign-coherent and cannot cancel

For every matrix cell, the eight nearest target-minus-source entries have one
sign: no cell is increased by one nearest target and decreased by another.
Consequently every nonempty target subset `S` satisfies

```text
|| sum_{T in S}(T-SOURCE) ||_1 = 6|S|,
```

and no nonempty subset has zero displacement. The all-eight batch has aggregate
signed matrix

```text
(-5,-1, 1, 5,
  5,-5,-1, 1,
  1, 5,-5,-1,
 -1, 1, 5,-5)
```

and `L1` norm 48. Buffer assignment and swap order alter exposed scheduling but
cannot alter this endpoint drift.

## Verification

- `scripts/check_threshold_factorized_exposure_collision.py` reconstructs the
  legal catalogue, all forty-nine matchings, all forty-four factorizations, and
  the invariant footprint loads.
- `scripts/check_threshold_incidence_factorizations.py` independently checks the
  one-factorization counts and matching participation histogram.
- `scripts/check_threshold_sign_coherent_drift.py` exhausts all 255 nonempty target
  subsets and verifies exact additive endpoint drift.

## Evidence boundary

Balanced transient scheduling does not yield independent geometric operations,
and the nearest-target family cannot neutralize itself. A realization must
protect a coupled full-grid batch and also supply an inverse or compensating
source operation with legal exposed states.
