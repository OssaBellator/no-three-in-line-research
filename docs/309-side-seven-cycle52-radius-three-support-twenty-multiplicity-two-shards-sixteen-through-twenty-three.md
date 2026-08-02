# Exact `(5,2)` radius-three support-twenty multiplicity-two shards sixteen through twenty-three

PX976--PX979 close multiplicity-two cases `80` through `159`. This chapter
closes the next eighty signatures, cases `160` through `239`, in eight canonical
ten-signature proof shards.

This is a finite obstruction result, not an infinite product theorem and not a
proof of the no-three-in-line conjecture.

## 1. Exact shard census

### Theorem PX986 -- PROVED FINITE

Cases `160` through `239` contain eighty multiplicity-two signatures and
therefore

\[
80\cdot2=\boxed{160}
\]

selectors. Every selector is infeasible in all four radix orientations.

| Shard | Global cases | Signatures | Selectors | Transcript digest |
|---:|---:|---:|---:|---:|
| 16 | `160`--`169` | 10 | 20 | `18351291531595309837` |
| 17 | `170`--`179` | 10 | 20 | `576955961683063087` |
| 18 | `180`--`189` | 10 | 20 | `16784769552087234267` |
| 19 | `190`--`199` | 10 | 20 | `12273077452420250578` |
| 20 | `200`--`209` | 10 | 20 | `14184090767390867316` |
| 21 | `210`--`219` | 10 | 20 | `18208381549471948796` |
| 22 | `220`--`229` | 10 | 20 | `7321435250783849553` |
| 23 | `230`--`239` | 10 | 20 | `10637276132094415816` |
| **Total** | `160`--`239` | **80** | **160** | eight independent digests |

The exact GitHub Actions batch completed all eight jobs successfully and
uploaded one ordered transcript per shard. Every transcript is promoted to a
standalone digest verifier.

## 2. Exact clean-top census

### Theorem PX987 -- PROVED FINITE

Across cases `160` through `239`, the complete clean-top enumeration is:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,870,242 | 31,314,637 |
| Interleaved | 5,052,110 | 26,440,232 |
| **Total** | **10,922,352** | **57,754,869** |

Shard twenty-three is strongly interleaved-heavy, while shards twenty and
twenty-one are concatenated-heavy. The fixed ten-signature proof partition
remains stable despite this load variation.

## 3. Exact shared bottom CSP

### Theorem PX988 -- PROVED FINITE

The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 9,238,542 |
| 1 | 7,921,952 |
| 2 | 8,946,788 |
| 3 | 8,028,585 |
| **Total** | **34,135,867** |

Every one of the 160 selectors terminates with the active mask empty. Combining
with cases `0` through `159`, the first 240 multiplicity-two signatures use

\[
63{,}414{,}868+34{,}135{,}867
=\boxed{97{,}550{,}735}
\]

bottom-CSP nodes.

## 4. Revised finite cache boundary

### Corollary PX989 -- PROVED REDUCTION

The first 240 multiplicity-two signatures add 480 certified-infeasible selectors
to the higher-multiplicity cache. Therefore the exact support-twenty boundary is

\[
37{,}600+480=\boxed{38{,}080}
\]

certified-infeasible selectors and

\[
2{,}766{,}455{,}244+97{,}550{,}735
=\boxed{2{,}864{,}005{,}979}
\]

shared rejection-CSP nodes.

Together with the one constructive multiplicity-four selector, exactly

\[
71{,}860-38{,}080-1=\boxed{33{,}779}
\]

selectors remain unclassified:

- `3,600` multiplicity-two signatures containing `7,200` selectors;
- all `26,579` multiplicity-one signatures and selectors.

The next canonical multiplicity-two frontier begins at global case `240`.

## 5. Verification

```bash
for shard in $(seq 16 23); do
  source="scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard${shard}.cpp"
  binary="/tmp/m2s${shard}"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```

Every verifier regenerates the complete radius-three layer, asserts the
multiplicity-two tier size `3,840`, checks its exact ten-signature interval,
replays all four orientation searches, and asserts its aggregate clean-top
counts, top-search nodes, bottom-CSP totals, and ordered transcript digest.
