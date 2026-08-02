# Threshold factorization and exposure collisions

`docs/647` proves that the eight nearest threshold targets and eight unit source
cells form a connected cubic bipartite graph with forty-nine perfect matchings.
This chapter classifies complete three-round buffer schedules and then audits the
cell-sharing burden that remains after buffer reuse is eliminated.

## PP3czv — Complete three-round buffer factorization

The twenty-four target-buffer incidences admit exactly forty-four unordered
one-factorizations into three perfect matchings. Equivalently, there are

```text
44 * 3! = 264
```

ordered three-round schedules in which every target uses each of its three
available transient cells exactly once and every transient cell is used exactly
once in each round.

Each incidence has two native swap orders, so these factorizations lift to

```text
264 * 2^24 = 4,429,185,024
```

fully ordered native three-round schedules.

## PP3czw — Matching-independent full-grid footprint

For each target, combine its six-cell alternating support with the transient cell
selected by a perfect matching. For every one of the forty-nine perfect
matchings, the union of the eight resulting seven-cell footprints is the entire
`4 x 4` source grid.

Moreover, the cell-load histogram is independent of the matching:

```text
load 2: eight cells,
load 5: eight cells.
```

The eight load-five cells are exactly the source cells whose multiplicity is not
one. The eight unit source cells occur once in target supports and once as the
distinct transient buffers, hence load two.

## PP3czx — Sharp shared-core obstruction

No distinct-buffer matching makes the eight target footprints disjoint, and no
matching reduces the maximum shared-cell load below five. A three-round
one-factorization balances transient-buffer use perfectly, but every round still
requires protection of all sixteen source cells and eight fivefold-shared heavy
cells.

Thus buffer assignment alone cannot produce a collection of independent atomic
`C6` operations. Any geometric realization must support a coupled full-grid batch
or introduce a new primitive whose exposed footprint is smaller than the native
two-swap catalogue.

## Verification

`scripts/check_threshold_factorized_exposure_collision.py` reconstructs the legal
layer catalogue, all eight targets, the cubic incidence graph, all forty-nine
perfect matchings, all forty-four factorizations, and every matching's exact cell
load profile.

## Remaining threshold obligation

No geometric source operation currently protects the full `4 x 4` batch with its
fivefold shared cells, and no primitive six-cell atomic edit has been constructed.
