# Exact `(5,2)` radius-three support-twenty multiplicity-two shards thirty-two through thirty-nine

PX990--PX993 close multiplicity-two cases `240` through `319`. This chapter
closes the next eighty signatures, cases `320` through `399`, in eight canonical
ten-signature proof shards.

This is a finite obstruction result, not an infinite product theorem and not a
proof of the no-three-in-line conjecture.

## 1. Exact shard census

### Theorem PX1003 -- PROVED FINITE

Cases `320` through `399` contain eighty multiplicity-two signatures and
therefore

\[
80\cdot2=\boxed{160}
\]

selectors. Every selector is infeasible in all four radix orientations.

| Shard | Global cases | Signatures | Selectors | Transcript digest |
|---:|---:|---:|---:|---:|
| 32 | `320`--`329` | 10 | 20 | `7141580424024650355` |
| 33 | `330`--`339` | 10 | 20 | `3155208086192315161` |
| 34 | `340`--`349` | 10 | 20 | `16622973091455341356` |
| 35 | `350`--`359` | 10 | 20 | `7917794102842155404` |
| 36 | `360`--`369` | 10 | 20 | `1284622885101910788` |
| 37 | `370`--`379` | 10 | 20 | `16735768237502152273` |
| 38 | `380`--`389` | 10 | 20 | `16236183647005793889` |
| 39 | `390`--`399` | 10 | 20 | `13987574131200629039` |
| **Total** | `320`--`399` | **80** | **160** | eight independent digests |

GitHub Actions run `30263068006` completed all eight exact jobs successfully.
Every transcript is promoted to a standalone digest verifier.

## 2. Exact clean-top census

### Theorem PX1004 -- PROVED FINITE

Across cases `320` through `399`, the complete clean-top enumeration is:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,170,484 | 13,806,167 |
| Interleaved | 3,354,656 | 11,250,684 |
| **Total** | **7,525,140** | **25,056,851** |

Shard 37 is the dominant unit, with more than two million bottom nodes in each
of orientations zero and two. The ten-signature partition remains exact and
replayable despite this cost variation.

## 3. Exact shared bottom CSP

### Theorem PX1005 -- PROVED FINITE

The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 6,352,729 |
| 1 | 5,293,491 |
| 2 | 6,430,508 |
| 3 | 4,780,302 |
| **Total** | **22,857,030** |

Every one of the 160 selectors terminates with the active mask empty. Combining
with cases `0` through `319`, the first 400 multiplicity-two signatures use

\[
133{,}108{,}986+22{,}857{,}030
=\boxed{155{,}966{,}016}
\]

bottom-CSP nodes.

## 4. Revised finite cache boundary

### Corollary PX1006 -- PROVED REDUCTION

The first 400 multiplicity-two signatures add 800 certified-infeasible selectors
to the higher-multiplicity cache. Therefore the exact support-twenty boundary is

\[
37{,}600+800=\boxed{38{,}400}
\]

certified-infeasible selectors and

\[
2{,}766{,}455{,}244+155{,}966{,}016
=\boxed{2{,}922{,}421{,}260}
\]

shared rejection-CSP nodes.

Together with the one constructive multiplicity-four selector, exactly

\[
71{,}860-38{,}400-1=\boxed{33{,}459}
\]

selectors remain unclassified:

- `3,440` multiplicity-two signatures containing `6,880` selectors;
- all `26,579` multiplicity-one signatures and selectors.

The next canonical multiplicity-two frontier begins at global case `400`.

## 5. Verification

```bash
for shard in $(seq 32 39); do
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
