# Exact `(5,2)` radius-three support-twenty multiplicity-two shards forty-eight through fifty-five

PX1022--PX1025 close multiplicity-two cases `400` through `479`. This chapter
closes the next eighty signatures, cases `480` through `559`, in eight canonical
ten-signature proof shards.

This is a finite obstruction result, not an infinite product theorem and not a
proof of the no-three-in-line conjecture.

## 1. Exact shard census

### Theorem PX1026 -- PROVED FINITE

Cases `480` through `559` contain eighty multiplicity-two signatures and
therefore 160 selectors. Every selector is infeasible in all four radix
orientations.

| Shard | Global cases | Selectors | Transcript digest |
|---:|---:|---:|---:|
| 48 | `480`--`489` | 20 | `7369468559469468632` |
| 49 | `490`--`499` | 20 | `5474747236930159619` |
| 50 | `500`--`509` | 20 | `2680446809043638559` |
| 51 | `510`--`519` | 20 | `6799617504066900155` |
| 52 | `520`--`529` | 20 | `12482974293267331403` |
| 53 | `530`--`539` | 20 | `11100554868985595416` |
| 54 | `540`--`549` | 20 | `5234405795839717689` |
| 55 | `550`--`559` | 20 | `12678841959537449495` |
| **Total** | `480`--`559` | **160** | eight independent digests |

GitHub Actions run `30268514286` completed all eight exact jobs and uploaded the
ordered transcripts used by the replay wrappers.

## 2. Exact clean-top census

### Theorem PX1027 -- PROVED FINITE

Across cases `480` through `559`, the complete clean-top enumeration is:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,948,864 | 25,139,783 |
| Interleaved | 5,113,054 | 23,250,448 |
| **Total** | **10,061,918** | **48,390,231** |

## 3. Exact shared bottom CSP

### Theorem PX1028 -- PROVED FINITE

The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 7,727,144 |
| 1 | 7,905,092 |
| 2 | 7,541,614 |
| 3 | 8,078,659 |
| **Total** | **31,252,509** |

Every one of the 160 selectors terminates with the active mask empty. Combining
with cases `0` through `479`, the first 560 multiplicity-two signatures use

\[
208{,}563{,}563+31{,}252{,}509
=\boxed{239{,}816{,}072}
\]

bottom-CSP nodes.

## 4. Revised finite cache boundary

### Corollary PX1029 -- PROVED REDUCTION

The first 560 multiplicity-two signatures add 1,120 certified-infeasible
selectors to the higher-multiplicity cache. Therefore the exact support-twenty
boundary is

\[
37{,}600+1{,}120=\boxed{38{,}720}
\]

certified-infeasible selectors and

\[
2{,}766{,}455{,}244+239{,}816{,}072
=\boxed{3{,}006{,}271{,}316}
\]

shared rejection-CSP nodes.

Together with the one constructive selector, exactly

\[
71{,}860-38{,}720-1=\boxed{33{,}139}
\]

selectors remain unclassified:

- `3,280` multiplicity-two signatures containing `6,560` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two frontier begins at global case `560`.

## 5. Verification

```bash
for shard in $(seq 48 55); do
  source="scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard${shard}.cpp"
  binary="/tmp/m2s${shard}"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```

Every verifier regenerates the complete radius-three layer, asserts the tier size
`3,840`, checks its exact ten-signature interval, replays all four orientation
searches, and asserts all aggregate counts and the ordered digest.
