# Random matching-block preparation diagnostics

This experiment accompanies
[`docs/56-random-matching-block-preparation.md`](../docs/56-random-matching-block-preparation.md)
and
[`docs/57-deletion-aware-random-block-profiles.md`](../docs/57-deletion-aware-random-block-profiles.md).
It constructs the global labelled signature counts used by PP3cl, PP3cm, and
PP3cq before choosing the matching-layer equipartition.

Run the deletion-blind baseline with

```bash
python scripts/analyze_random_matching_block_preparation.py \
  certificates/prime-patching-small.json \
  --block-size 4 --delta 1/72
```

and the exact matching-layer anchor correction with

```bash
python scripts/analyze_deletion_aware_random_block_profiles.py \
  certificates/prime-patching-small.json \
  --block-size 4 --delta 1/72
```

The first analyzer uses the complete four-cell support of every source edge in
every reserved width-two interval and counts all source anchors deletion-blindly.
The second removes controller-anchor collisions and multiplies selected-layer
anchor ranks by the exact PP3cp hypergeometric survival factors.

## Exact local-signature expectations

For `r=4`, the PP3cl value `L_*` on the stored matching layers is:

| Side | Layer 0 | Layer 1 |
|---:|---:|---:|
| 4 | `11` | `8` |
| 5 | `58/5` | `37/5` |
| 6 | `8` | `4` |
| 7 | `186/35` | `158/35` |
| 8 | `71/14` | `13/2` |
| 9 | `137/21` | `33/7` |
| 10 | `137/30` | `151/30` |

These values exceed one because the calculation exposes every possible local
candidate cell before pair-partition feasibility, retained-point deletion, or
clean-domain pruning is used.  PP3cl is an exact expectation for that signature
superset.

## Global deletion-blind profile counts

For the first cases with two labelled blocks, the counts are:

| Side/layer | `M1` | `Mh` | `M2` | `M11` | `Mh1` | `M21` | `M111` |
|---|---:|---:|---:|---:|---:|---:|---:|
| 8/0 | 163 | 70 | 93 | 177 | 57 | 462 | 0 |
| 8/1 | 163 | 72 | 91 | 173 | 30 | 483 | 0 |
| 9/0 | 208 | 77 | 138 | 209 | 33 | 627 | 0 |
| 9/1 | 208 | 82 | 133 | 214 | 39 | 651 | 0 |
| 10/0 | 224 | 89 | 167 | 290 | 48 | 776 | 0 |
| 10/1 | 224 | 91 | 165 | 288 | 45 | 770 | 0 |

`M111=0` here because `K=floor(n/4)=2`; there are no three distinct block
labels.

At `delta=1/72`, the resulting deletion-blind `G_delta` values range from roughly
`1.4e5` to `1.7e5` on sides eight through ten.  PP3cn therefore does not certify
these small examples.

## Deletion-aware anchor stratification

The PP3cq analyzer records `M1` by selected-layer anchor rank `0,1,2`, and
`Mh,M2,M11` by rank `0,1`.  It removes every signature in which a proposed
retained anchor is one of the candidate controller edges.

For example, the side-eight counts are:

| Layer | `M1^(0,1,2)` | `Mh^(0,1)` | `M2^(0,1)` | `M11^(0,1)` |
|---:|---|---|---|---|
| 0 | `(27,50,22)` | `(35,3)` | `(53,40)` | `(94,83)` |
| 1 | `(22,50,27)` | `(36,4)` | `(39,52)` | `(83,90)` |

Here `r=4` and `K=2`, so all eight edges of the selected matching layer are
deleted.  Consequently every positive-rank selected-layer anchor factor is zero:
only the rank-zero entries survive in `G_delta^del`.

The deletion-aware values on sides eight through ten are:

| Side/layer | `G_delta` baseline | `G_delta^del` |
|---|---:|---:|
| 8/0 | `1161378/7` | `924741/7` |
| 8/1 | `1143252/7` | `887130/7` |
| 9/0 | `1029740/7` | `800452/7` |
| 9/1 | `152382` | `889320/7` |
| 10/0 | `144060` | `582162/5` |
| 10/1 | `142740` | `113758` |

For the one-block sides four through seven the reduction is larger because the
same-layer anchor cancellation removes most source-anchor profiles.  For
example:

| Side/layer | baseline | deletion-aware |
|---|---:|---:|
| 4/0 | `1710` | `432` |
| 4/1 | `1692` | `504` |
| 6/0 | `10536/5` | `3948/5` |
| 6/1 | `2112` | `5088/5` |

The correction is exact for the unconditioned full block banks and remains a
valid upper bound after clean-domain conditioning through the displayed powers
of `1/delta`.

## Interpretation

The experiment now separates three tasks.

1. **Partition algebra is closed.**  PP3ck--PP3cn convert global labelled
   signature counts into block-scale expectations, and the powers of `r` cancel.
2. **Deletion correlation is closed.**  PP3co--PP3cr remove every
   controller-anchor collision and give exact hypergeometric survival factors for
   selected-layer source anchors.
3. **Geometric signature compression remains open.**  Even after deletion-aware
   correction, the finite `G_delta^del` values are large because other-layer
   source anchors and all-patch cross-block profiles survive, and the calculation
   still counts all support cells before the clean 36-state domain is used
   exactly.

At the asymptotic prime-gap scale, only `4K/m=m^-0.475+o(1)` of one matching layer
is deleted, so fixed-rank survival factors tend to one.  The remaining theorem
must therefore reduce the number or occurrence of controlled secant signatures,
not rely solely on anchor deletion.