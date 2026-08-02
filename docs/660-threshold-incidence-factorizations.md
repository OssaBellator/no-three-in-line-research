# Threshold incidence factorizations and shared exposure

`docs/658` chooses the unique perfectly balanced swap-order profile for each of
the forty-nine distinct-buffer assignments. This chapter instead organizes all
twenty-four target-buffer incidences into complete three-round cycles and records
the shared-cell obstruction that survives that balancing.

## PP3daq — Complete three-round factorization count

The cubic bipartite incidence graph on eight targets and eight transient cells
has exactly forty-four unordered one-factorizations into three perfect matchings.
Equivalently, it has 132 edge-disjoint pairs of perfect matchings, each with a
unique complementary third matching.

Ordering the three rounds gives

```text
44 * 3! = 264
```

round schedules. Choosing either native swap order on each of the twenty-four
incidences gives

```text
264 * 2^24 = 4,429,185,024
```

fully ordered native three-round schedules.

## PP3dar — Exact incidence balance and matching multiplicities

Within every one-factorization:

- every target appears once in each round;
- every transient cell is used once in each round;
- every target uses each of its three available transient cells exactly once;
- all twenty-four target-buffer incidences occur exactly once.

The forty-nine perfect matchings participate in respectively one, two, four, or
eight factorizations, with multiplicity histogram

```text
1:10, 2:21, 4:16, 8:2.
```

Thus transient use is completely balanced over three rounds, not merely made
distinct inside one round.

## PP3das — Matching-independent full-grid sharing obstruction

For a target in one round, combine its six-cell alternating support with its
selected transient cell. For every one of the forty-nine perfect matchings, the
union of the eight seven-cell footprints is the entire `4 x 4` source grid.
The cell-load histogram is invariant:

```text
load 2: eight unit source cells,
load 5: eight source cells of multiplicity zero or two.
```

Hence no distinct-buffer round makes target footprints disjoint and no matching
reduces maximum shared-cell load below five. Every three-round factorization
repeats this full-grid sharing pattern in each round.

The one-factorization removes buffer reuse, while `docs/658` removes exposure
imbalance, but neither makes an exposed intermediate legal. A source realization
must protect a coupled full-grid operation or replace the native two-swap path.

## Verification

- `scripts/check_threshold_incidence_factorizations.py` checks the forty-four
  factorizations, matching participation histogram, and ordered schedule count.
- `scripts/check_threshold_factorized_exposure_collision.py` checks the invariant
  sixteen-cell footprint and load histogram for every perfect matching.

## Remaining threshold obligation

No primitive or protected batch currently realizes these schedules with legal
geometric exposed states, and no compensating endpoint cycle has been certified.
