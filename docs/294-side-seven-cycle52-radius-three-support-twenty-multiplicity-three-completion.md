# Exact `(5,2)` radius-three support-twenty multiplicity-three completion

PX932--PX935 closed global multiplicity-three cases `2100` through `2199`. This chapter closes every remaining case, from `2200` through `3543`.

This is a finite obstruction result, not an infinite product theorem and not a proof of the no-three-in-line conjecture.

## 1. Exact remaining-frontier census

### Theorem PX936 -- PROVED FINITE

The remaining frontier contains `1,344` multiplicity-three signatures and therefore

\[
1{,}344\cdot3=\boxed{4{,}032}
\]

selectors.

The exact verifier family regenerates the radius-three layer, asserts the full multiplicity-three tier size of `3,544` signatures, sorts the signatures canonically, and checks global cases `2200` through `3543` without omission or overlap.

| Shard | Global cases | Signatures | Selectors | Transcript digest |
|---:|---:|---:|---:|---:|
| 22 | `2200`--`2299` | 100 | 300 | `18285130004508838207` |
| 23 | `2300`--`2399` | 100 | 300 | `9882995509441515575` |
| 24 | `2400`--`2499` | 100 | 300 | `1893542477527105416` |
| 25 | `2500`--`2599` | 100 | 300 | `11824482046511188436` |
| 26 | `2600`--`2699` | 100 | 300 | `17903848441077875937` |
| 27 | `2700`--`2799` | 100 | 300 | `12950518957910341982` |
| 28 | `2800`--`2899` | 100 | 300 | `4917294112956063211` |
| 29 | `2900`--`2999` | 100 | 300 | `2066368581572695674` |
| 30 | `3000`--`3099` | 100 | 300 | `13070021860948705188` |
| 31 | `3100`--`3199` | 100 | 300 | `9218704767626605724` |
| 32 | `3200`--`3299` | 100 | 300 | `14519279701100109802` |
| 33 | `3300`--`3399` | 100 | 300 | `9297774443006448587` |
| 34 | `3400`--`3499` | 100 | 300 | `3142633351817514366` |
| 35 | `3500`--`3543` | 44 | 132 | `3731072057743112162` |
| **Total** | `2200`--`3543` | **1,344** | **4,032** | 14 independent shard digests |

## 2. Exact clean-top census

### Theorem PX937 -- PROVED FINITE

Across the remaining frontier, the complete clean-top enumeration is:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 84,660,151 | 658,381,548 |
| Interleaved | 60,953,717 | 488,960,957 |
| **Total** | **145,613,868** | **1,147,342,505** |

Every shard stores both aggregate counts and an ordered FNV-style transcript digest. The measurement executable aborts immediately if any selector is feasible, so a successful transcript certifies that every enumerated top assignment was rejected by the shared bottom solver.

## 3. Exact shared bottom CSP

### Theorem PX938 -- PROVED FINITE

Every one of the `4,032` remaining selectors fails in every radix orientation.

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 149,343,956 |
| 1 | 107,047,667 |
| 2 | 144,660,460 |
| 3 | 103,720,697 |
| **Total** | **504,772,780** |

Combining this result with the previously certified cases `0` through `2199` closes the entire multiplicity-three tier:

\[
3{,}544\text{ signatures}\times3
=\boxed{10{,}632\text{ selectors}},
\]

all infeasible.

## 4. Revised finite cache boundary

### Corollary PX939 -- PROVED REDUCTION

Adding the completed frontier gives

\[
33{,}568+4{,}032=\boxed{37{,}600}
\]

certified-infeasible support-twenty selectors and

\[
2{,}261{,}682{,}464+504{,}772{,}780
=\boxed{2{,}766{,}455{,}244}
\]

shared rejection-CSP nodes.

Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-37{,}600-1=\boxed{34{,}259}
\]

unclassified support-twenty selectors. None of the remaining selectors has multiplicity three.

The next finite target is therefore the next nonempty multiplicity tier, not another multiplicity-three shard. This sharpens the finite side-seven census but does not supply recursive product closure for arbitrary side length.

## 5. Verification

Compile and run any shard directly:

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard22.cpp \
  -o /tmp/m3s22

/tmp/m3s22
/tmp/m3s22 2200 0
/tmp/m3s22 2299 3
```

To replay the full completion frontier:

```bash
for shard in $(seq 22 35); do
  source="scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard${shard}.cpp"
  binary="/tmp/m3s${shard}"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```

The generic measurement executable can independently regenerate any interval and print the exact constants required by a digest verifier:

```bash
g++ -O3 -std=c++17 \
  scripts/measure_product_side_seven_tier_shard.cpp \
  -o /tmp/measure-m3

/tmp/measure-m3 2200 100 3
/tmp/measure-m3 3500 44 3
```

Every full verifier asserts the tier histogram, shard interval, coordinate searches, aggregate counts, absence of every embedding, and ordered transcript digest.
