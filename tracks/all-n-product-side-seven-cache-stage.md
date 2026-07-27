# All-n product track: side-seven radius-three cache stage

**Branch:** `research/all-n-product-construction`

This stage continues the exact full-selector classification at base side seven.
It studies the `(5,2)` relative-cycle class inside the radius-three,
support-twenty selector layer of the canonical `[14]^2` host. The task is a
finite obstruction-and-witness census, not an infinite closure theorem.

## Current ledger

The exact support-twenty layer contains `71,860` selectors. Shared-top searches
have classified every top-signature tier of multiplicity at least `4` and the
first seven hundred signatures of multiplicity `3`:

| Multiplicity | Signatures | Selectors | Status |
|---:|---:|---:|---|
| 46 | 4 | 184 | certified infeasible |
| 40 | 3 | 120 | certified infeasible |
| 38 | 3 | 114 | certified infeasible |
| 35 | 2 | 70 | certified infeasible |
| 32 | 3 | 96 | certified infeasible |
| 27 | 6 | 162 | certified infeasible |
| 26 | 6 | 156 | certified infeasible |
| 24 | 8 | 192 | certified infeasible |
| 23 | 10 | 230 | certified infeasible |
| 20 | 1 | 20 | certified infeasible |
| 19 | 42 | 798 | certified infeasible |
| 16 | 38 | 608 | certified infeasible |
| 15 | 2 | 30 | certified infeasible |
| 14 | 40 | 560 | certified infeasible |
| 13 | 48 | 624 | certified infeasible |
| 12 | 128 | 1,536 | certified infeasible |
| 10 | 164 | 1,640 | certified infeasible |
| 9 | 64 | 576 | certified infeasible |
| 8 | 277 | 2,216 | certified infeasible |
| 7 | 100 | 700 | certified infeasible |
| 6 | 524 | 3,144 | certified infeasible |
| 5 | 725 | 3,625 | certified infeasible |
| 4 | 2,392 | 9,568 | 9,567 infeasible; 1 witnessed |
| 3, shards 0--6 | 700 of 3,544 | 2,100 | certified infeasible |
| **Total** | **5,290 completed classes** | **29,068 rejected; 1 witnessed** | **1,788,607,134 rejection-CSP nodes** |

Thus `42,791` support-twenty selectors remain unclassified and active in this
cache layer.

The latest exact results are PX830--PX833 in
[`docs/257-side-seven-cycle52-radius-three-support-twenty-multiplicity-three-shard-six.md`](../docs/257-side-seven-cycle52-radius-three-support-twenty-multiplicity-three-shard-six.md).

## Constructive witness

Global multiplicity-four case `1392`, selector zero, has a verified no-three
embedding in orientation `1`. The mixed verifier checks the selector state,
clean top assignment, bottom permutation, 28 distinct points, and all 3,276
nonzero integer determinants. The other three selectors in that signature are
jointly certified infeasible in all four orientations.

## Solver and proof-object improvements

The common radius-layer generation, clean-top enumeration, hoisted incidence
masks, scalar point tables, active-selector propagation, and exact count checks
live in `scripts/product_side_seven_cache_engine.hpp`.

The common transcript verifiers print every per-signature count while one
asserted 64-bit digest commits each complete ordered tier or shard transcript.
`scripts/product_side_seven_tier_shard_digest.hpp` adds independently
reproducible lexicographic shard intervals without checking in large case data
tables. Witness-preserving scan workers retain constructive data and continue
rather than terminating a range.

PX743--PX744 add the first explicit proof-object pilot. For case `1180`,
orientation `0`, and the first clean concatenated top order, a `60,536`-byte
certificate supplies one concrete collinear triple for each of `20,160`
selector-permutation obligations. Its checker validates exact geometry without
calling `BottomGroupSolver`.

PX749--PX750 extend the format to two clean top orders. A shared dictionary of
`84` triples represents `40,320` obligations in `40,648` bytes.

PX764--PX765 measure dictionary saturation across eight clean top orders. The
cumulative dictionary sizes are `66, 84, 107, 120, 122, 124, 142, 152`; only
`152` triples cover `161,280` obligations. The projected shared proof payload is
`161,896` bytes rather than `484,288` bytes for eight raw certificates.

PX804--PX805 extend the same exact experiment through thirty-two clean top
orders. A dictionary of `363` triples covers `645,120` obligations in a projected
`646,705`-byte proof payload, rather than `1,937,152` bytes for thirty-two raw
certificates.

PX810--PX811 double the prefix to sixty-four top orders. Only `404` triples cover
`1,290,240` obligations in a projected `1,292,396`-byte payload, rather than
`3,874,304` bytes for sixty-four raw certificates. The second block of thirty-two
orders introduces only 41 new triples, and order 64 introduces none.

PX816--PX817 transfer the dictionary format to multiplicity-three case `0`,
orientation `0`. Only `241` triples cover `483,840` obligations across the first
thirty-two clean top orders in a projected `485,059`-byte payload. This removes
about `66.6%` of the raw triple payload and confirms that the proof compression
is not confined to multiplicity four.

PX834--PX835 double the multiplicity-three prefix to sixty-four clean top orders.
Only `283` triples cover `967,680` obligations in a projected `969,473`-byte
payload, rather than `2,903,984` bytes for raw triples. The second block of
thirty-two orders introduces only 42 new triples.

PX774--PX775 give the first exact top-assumption core. For case `1180`,
orientation `0`, every one of the fourteen top literals can be deleted: the
signature alone refutes all `70,376` clean concatenated top orders after
`95,298` shared bottom-CSP nodes. This is an empty top-assumption core and a
signature-level master nogood.

PX641--PX642 remain the stronger full selector-choice CSP and proof-logged SAT
route. No external SAT solver or DRAT/FRAT checker is available in the current
execution environment, so independently checked native certificates remain the
active proof-producing route.

## Immediate task

The remaining multiplicity-three frontier begins at global case index `700` and
contains `2,844` top signatures and `8,532` selectors. Continue in independently
reproducible, witness-preserving intervals. In parallel:

1. test whether empty or small top-assumption cores recur across signatures;
2. generalize signature-level master nogoods across mechanically checked incidence features;
3. continue measuring dictionary saturation over wider top-order batches;
4. export one selector-choice shard to CNF when an independent proof checker is available;
5. add only mechanically verified host/reflection symmetry constraints.

## Stage completion criterion

This cache stage is complete when every selector in the radius-three,
support-twenty `(5,2)` layer is either certified infeasible in all four
orientations or accompanied by an independently checked no-three witness.
Afterward the side-seven classification must still address the remaining
support layers and relative-cycle classes.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard6.cpp \
  -o /tmp/m3s6
/tmp/m3s6

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case0_orientation0_dictionary_saturation64.cpp \
  -o /tmp/m3-case0-dict64
/tmp/m3-case0-dict64

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard14_mixed.cpp \
  -o /tmp/m4s14
/tmp/m4s14 1392
```

The classical no-three-in-line conjecture and infinite product closure remain
open.
