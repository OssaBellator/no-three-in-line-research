# Exact `(5,2)` radius-three support-twenty multiplicity-two shards eight through fifteen

PX956--PX959 close multiplicity-two cases `40` through `79`. This chapter closes
the next eighty signatures, cases `80` through `159`, in eight canonical
ten-signature proof shards.

This is a finite obstruction result, not an infinite product theorem and not a
proof of the no-three-in-line conjecture.

## 1. Exact shard census

### Theorem PX976 -- PROVED FINITE

Cases `80` through `159` contain eighty multiplicity-two signatures and
therefore

\[
80\cdot2=\boxed{160}
\]

selectors. Every selector is infeasible in all four radix orientations.

| Shard | Global cases | Signatures | Selectors | Transcript digest |
|---:|---:|---:|---:|---:|
| 8 | `80`--`89` | 10 | 20 | `5856008537745773282` |
| 9 | `90`--`99` | 10 | 20 | `3834793925943032802` |
| 10 | `100`--`109` | 10 | 20 | `9447947952084994573` |
| 11 | `110`--`119` | 10 | 20 | `17946475240143660` |
| 12 | `120`--`129` | 10 | 20 | `14137670081341765779` |
| 13 | `130`--`139` | 10 | 20 | `15736712881480794511` |
| 14 | `140`--`149` | 10 | 20 | `11228535735195360597` |
| 15 | `150`--`159` | 10 | 20 | `3048902713011650628` |
| **Total** | `80`--`159` | **80** | **160** | eight independent digests |

The exact GitHub Actions batch completed all eight searches successfully and
uploaded one ordered transcript per shard. Each transcript was promoted to a
standalone digest verifier.

## 2. Exact clean-top census

### Theorem PX977 -- PROVED FINITE

Across cases `80` through `159`, the complete clean-top enumeration is:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,438,388 | 24,187,947 |
| Interleaved | 4,895,504 | 21,259,674 |
| **Total** | **10,333,892** | **45,447,621** |

The cost remains highly nonuniform. Shard eleven is interleaved-heavy, while
shards eight and ten are concatenated-heavy. Fixed ten-signature proof boundaries
remain useful, but execution should continue to schedule shards by observed or
predicted clean-top weight.

## 3. Exact shared bottom CSP

### Theorem PX978 -- PROVED FINITE

The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 8,359,571 |
| 1 | 7,691,084 |
| 2 | 8,740,025 |
| 3 | 7,600,519 |
| **Total** | **32,391,199** |

Every one of the 160 selectors terminates with the active mask empty. Combining
with cases `0` through `79`, the first 160 multiplicity-two signatures use

\[
31{,}023{,}669+32{,}391{,}199
=\boxed{63{,}414{,}868}
\]

bottom-CSP nodes.

## 4. Revised finite cache boundary

### Corollary PX979 -- PROVED REDUCTION

The first 160 multiplicity-two signatures add 320 certified-infeasible selectors
to the higher-multiplicity cache. Therefore the exact support-twenty boundary is

\[
37{,}600+320=\boxed{37{,}920}
\]

certified-infeasible selectors and

\[
2{,}766{,}455{,}244+63{,}414{,}868
=\boxed{2{,}829{,}870{,}112}
\]

shared rejection-CSP nodes.

Together with the one constructive multiplicity-four selector, exactly

\[
71{,}860-37{,}920-1=\boxed{33{,}939}
\]

selectors remain unclassified:

- `3,680` multiplicity-two signatures containing `7,360` selectors;
- all `26,579` multiplicity-one signatures and selectors.

The next canonical multiplicity-two frontier begins at global case `160`.

## 5. Verification

```bash
for shard in $(seq 8 15); do
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
