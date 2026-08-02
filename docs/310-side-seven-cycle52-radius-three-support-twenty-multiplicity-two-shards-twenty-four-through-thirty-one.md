# Exact `(5,2)` radius-three support-twenty multiplicity-two shards twenty-four through thirty-one

PX986--PX989 close multiplicity-two cases `160` through `239`. This chapter
closes the next eighty signatures, cases `240` through `319`, in eight canonical
ten-signature proof shards.

This is a finite obstruction result, not an infinite product theorem and not a
proof of the no-three-in-line conjecture.

## 1. Exact shard census

### Theorem PX990 -- PROVED FINITE

Cases `240` through `319` contain eighty multiplicity-two signatures and
therefore

\[
80\cdot2=\boxed{160}
\]

selectors. Every selector is infeasible in all four radix orientations.

| Shard | Global cases | Signatures | Selectors | Transcript digest |
|---:|---:|---:|---:|---:|
| 24 | `240`--`249` | 10 | 20 | `9055214726262274039` |
| 25 | `250`--`259` | 10 | 20 | `1131586997605564077` |
| 26 | `260`--`269` | 10 | 20 | `11692544106972541554` |
| 27 | `270`--`279` | 10 | 20 | `13591523195064408722` |
| 28 | `280`--`289` | 10 | 20 | `1683636985435897178` |
| 29 | `290`--`299` | 10 | 20 | `6776011627925700319` |
| 30 | `300`--`309` | 10 | 20 | `11051023198654571322` |
| 31 | `310`--`319` | 10 | 20 | `18126001820985620447` |
| **Total** | `240`--`319` | **80** | **160** | eight independent digests |

GitHub Actions run `30261206602` completed all eight jobs successfully and
uploaded one ordered transcript per shard. Every transcript is promoted to a
standalone digest verifier.

## 2. Exact clean-top census

### Theorem PX991 -- PROVED FINITE

Across cases `240` through `319`, the complete clean-top enumeration is:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,606,132 | 23,571,617 |
| Interleaved | 5,562,202 | 21,950,922 |
| **Total** | **11,168,334** | **45,522,539** |

Shard thirty is the dominant cost unit, while shard twenty-nine is unusually
small. The fixed ten-signature partition remains replayable despite this load
variation.

## 3. Exact shared bottom CSP

### Theorem PX992 -- PROVED FINITE

The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 8,895,985 |
| 1 | 9,076,552 |
| 2 | 9,204,942 |
| 3 | 8,380,772 |
| **Total** | **35,558,251** |

Every one of the 160 selectors terminates with the active mask empty. Combining
with cases `0` through `239`, the first 320 multiplicity-two signatures use

\[
97{,}550{,}735+35{,}558{,}251
=\boxed{133{,}108{,}986}
\]

bottom-CSP nodes.

## 4. Revised finite cache boundary

### Corollary PX993 -- PROVED REDUCTION

The first 320 multiplicity-two signatures add 640 certified-infeasible selectors
to the higher-multiplicity cache. Therefore the exact support-twenty boundary is

\[
37{,}600+640=\boxed{38{,}240}
\]

certified-infeasible selectors and

\[
2{,}766{,}455{,}244+133{,}108{,}986
=\boxed{2{,}899{,}564{,}230}
\]

shared rejection-CSP nodes.

Together with the one constructive multiplicity-four selector, exactly

\[
71{,}860-38{,}240-1=\boxed{33{,}619}
\]

selectors remain unclassified:

- `3,520` multiplicity-two signatures containing `7,040` selectors;
- all `26,579` multiplicity-one signatures and selectors.

The next canonical multiplicity-two frontier begins at global case `320`.

## 5. Verification

```bash
for shard in $(seq 24 31); do
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
