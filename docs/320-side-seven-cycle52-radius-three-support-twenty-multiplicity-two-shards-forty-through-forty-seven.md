# Exact `(5,2)` radius-three support-twenty multiplicity-two shards forty through forty-seven

PX1003--PX1006 close multiplicity-two cases `320` through `399`. This chapter
closes the next eighty signatures, cases `400` through `479`, in eight canonical
ten-signature proof shards.

This is a finite obstruction result, not an infinite product theorem and not a
proof of the no-three-in-line conjecture.

## 1. Exact shard census

### Theorem PX1022 -- PROVED FINITE

Cases `400` through `479` contain eighty multiplicity-two signatures and
therefore 160 selectors. Every selector is infeasible in all four radix
orientations.

| Shard | Global cases | Selectors | Transcript digest |
|---:|---:|---:|---:|
| 40 | `400`--`409` | 20 | `16705625326510863433` |
| 41 | `410`--`419` | 20 | `5749020248150475417` |
| 42 | `420`--`429` | 20 | `3162344281037951680` |
| 43 | `430`--`439` | 20 | `10652007544342656566` |
| 44 | `440`--`449` | 20 | `1665996365935274379` |
| 45 | `450`--`459` | 20 | `14092422409558173123` |
| 46 | `460`--`469` | 20 | `5944945430537609933` |
| 47 | `470`--`479` | 20 | `13602949510585451809` |
| **Total** | `400`--`479` | **160** | eight independent digests |

The first attempted matrix was cancelled before any job started and produced no
artifact. GitHub Actions run `30266889212` is the successful durable replay; all
eight jobs completed and uploaded exact transcripts.

## 2. Exact clean-top census

### Theorem PX1023 -- PROVED FINITE

Across cases `400` through `479`, the complete clean-top enumeration is:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 11,042,194 | 41,872,061 |
| Interleaved | 5,713,946 | 23,507,208 |
| **Total** | **16,756,140** | **65,379,269** |

This block is substantially heavier than the preceding eighty cases. Shard 45
alone has more than three million clean top orders and over ten million bottom
nodes.

## 3. Exact shared bottom CSP

### Theorem PX1024 -- PROVED FINITE

The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 17,503,484 |
| 1 | 8,841,306 |
| 2 | 17,011,145 |
| 3 | 9,241,612 |
| **Total** | **52,597,547** |

Every one of the 160 selectors terminates with the active mask empty. Combining
with cases `0` through `399`, the first 480 multiplicity-two signatures use

\[
155{,}966{,}016+52{,}597{,}547
=\boxed{208{,}563{,}563}
\]

bottom-CSP nodes.

## 4. Revised finite cache boundary

### Corollary PX1025 -- PROVED REDUCTION

The first 480 multiplicity-two signatures add 960 certified-infeasible selectors
to the higher-multiplicity cache. Therefore the exact support-twenty boundary is

\[
37{,}600+960=\boxed{38{,}560}
\]

certified-infeasible selectors and

\[
2{,}766{,}455{,}244+208{,}563{,}563
=\boxed{2{,}975{,}018{,}807}
\]

shared rejection-CSP nodes.

Together with the one constructive selector, exactly

\[
71{,}860-38{,}560-1=\boxed{33{,}299}
\]

selectors remain unclassified:

- `3,360` multiplicity-two signatures containing `6,720` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two frontier begins at global case `480`.

## 5. Verification

```bash
for shard in $(seq 40 47); do
  source="scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard${shard}.cpp"
  binary="/tmp/m2s${shard}"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```

Every verifier regenerates the complete radius-three layer, asserts the tier size
`3,840`, checks its exact ten-signature interval, replays all four orientation
searches, and asserts all aggregate counts and the ordered digest.
