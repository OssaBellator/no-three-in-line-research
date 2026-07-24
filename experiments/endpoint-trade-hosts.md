# Endpoint-trade host diagnostics

This experiment accompanies
[`docs/90-superregular-paid-endpoint-trades.md`](../docs/90-superregular-paid-endpoint-trades.md),
[`docs/91-endpoint-host-regularization.md`](../docs/91-endpoint-host-regularization.md),
[`docs/92-low-support-permutation-local-lemma.md`](../docs/92-low-support-permutation-local-lemma.md),
and
[`scripts/analyze_endpoint_trade_hosts.py`](../scripts/analyze_endpoint_trade_hosts.py).

Run

```bash
python scripts/analyze_endpoint_trade_hosts.py \
  certificates/prime-patching-small.json
```

For each deterministic perfect-matching layer, the whole layer is removed and
its columns and rows form the tied endpoint rectangle. The opposite layer is the
fixed source. The program:

- removes the diagonal, occupied cells, and cells on secants through two fixed
  points;
- computes the exact maximum matching of this unary-safe host;
- counts anchored-pair and inserted-triple patterns by endpoint-index support
  rank;
- applies the PP3is high-degree pruning;
- computes the exact PP3ix low-event resource mass and the PP3ja high-support
  source term;
- searches exactly for a perfect matching whose insertion restores a saturated
  no-three configuration.

The full-layer trade is only a diagnostic. An asymptotic controller repair must
also preserve the fixed controller pools, as required by PP3ik.

## Full unary-safe hosts

| Side/layer | Safe host edges | Unary forbidden density | Maximum matching | Source-admissible perfect matching |
|---|---:|---:|---:|:---:|
| 4/0 | 6 | 0.625 | 4 | yes |
| 4/1 | 6 | 0.625 | 4 | yes |
| 5/0 | 10 | 0.600 | 5 | no |
| 5/1 | 13 | 0.480 | 5 | no |
| 6/0 | 14 | 0.611 | 6 | no |
| 6/1 | 19 | 0.472 | 6 | no |
| 7/0 | 19 | 0.612 | 7 | no |
| 7/1 | 25 | 0.490 | 7 | no |
| 8/0 | 33 | 0.484 | 8 | no |
| 8/1 | 27 | 0.578 | 8 | no |
| 9/0 | 28 | 0.654 | 8 | no |
| 9/1 | 32 | 0.605 | 9 | no |
| 10/0 | 48 | 0.520 | 10 | no |
| 10/1 | 38 | 0.620 | 10 | no |

Except for side `9`, layer `0`, the unary-safe graph itself has a perfect
matching. Nevertheless, from side five onward no full-layer perfect matching is
source-admissible. Unary cell safety therefore does not solve the endpoint trade
by itself; the pair and triple terms in PP3io are genuine.

The stored densities are far outside the asymptotic `theta=o(1)` regime of
PP3is. They are finite stress tests rather than counterexamples to the
regularization theorem.

## Support-rank profiles

The full-host anchored-pair counts are:

| Side/layer | Rank 2 | Rank 3 | Rank 4 |
|---|---:|---:|---:|
| 5/0 | 1 | 3 | 5 |
| 5/1 | 0 | 5 | 7 |
| 6/0 | 1 | 5 | 7 |
| 6/1 | 1 | 11 | 12 |
| 7/0 | 0 | 9 | 11 |
| 7/1 | 0 | 14 | 36 |
| 8/0 | 0 | 20 | 34 |
| 8/1 | 1 | 18 | 44 |
| 9/0 | 0 | 10 | 21 |
| 9/1 | 0 | 17 | 51 |
| 10/0 | 4 | 34 | 130 |
| 10/1 | 1 | 17 | 55 |

The inserted-triple profiles contain support ranks three through six. At side
`10`, they are:

| Layer | Rank 3 | Rank 4 | Rank 5 | Rank 6 |
|---:|---:|---:|---:|---:|
| 0 | 1 | 26 | 87 | 80 |
| 1 | 1 | 4 | 31 | 33 |

Most finite patterns have support rank above their event rank and are eligible
for additional dilution under PP3iv. PP3iz identifies the low-support patterns
exactly: rank-two pairs are transpositions, rank-three pairs are directed
transitions, and rank-three triples are directed 3-cycles.

## Low-support permutation mass

The exact maximum PP3ix resource masses on the full hosts are:

| Side/layer | Maximum low-event mass | PP3ix threshold `1/24` |
|---|---:|:---:|
| 4/0 | `5/6` | fail |
| 4/1 | `5/6` | fail |
| 5/0 | `17/20` | fail |
| 5/1 | `4/5` | fail |
| 6/0 | `5/6` | fail |
| 6/1 | `5/6` | fail |
| 7/0 | `19/21` | fail |
| 7/1 | `17/21` | fail |
| 8/0 | `45/56` | fail |
| 8/1 | `11/14` | fail |
| 9/0 | `1` | fail |
| 9/1 | `65/72` | fail |
| 10/0 | `34/45` | fail |
| 10/1 | `203/240` | fail |

These values are dominated by unary forbidden arcs, not by transpositions or
directed triangles. This is consistent with PP3jb: the finite hosts have
forbidden degrees comparable to their side length, whereas the asymptotic
criterion requires a small fixed fraction with total transition mass below the
remaining `1/24` budget.

The high-support PP3ja source term also exceeds one on almost every full host;
for example it is `16911/1000` on side `10`, layer `0`, and `3393/500` on side
`10`, layer `1`. Thus the exact finite failures are not artefacts of the coarse
constant in PP3ix.

## High-degree pruning

Although PP3is is not quantitatively applicable at these large finite forbidden
densities, applying its deterministic deletion rule remains informative.
Several pruned subbanks admit an exact source-admissible matching:

| Side/layer | Retained endpoints | Pruned maximum matching | Pruned source-admissible matching |
|---|---:|---:|:---:|
| 7/1 | 6 | 6 | yes |
| 8/0 | 7 | 7 | yes |
| 10/1 | 7 | 7 | yes |

Other layers remain obstructed after pruning. Endpoint regularization can
therefore recover clean subbanks even when neither the asymptotic LLL constant
nor the full-host first moment certifies them.

## Interpretation

The exact finite data support the revised conversion programme.

1. Put unary-invalid cells outside a superregular host, or include them as
   canonical unary events when their per-resource mass is small.
2. Prune high endpoint rows and columns when the forbidden density is sparse.
3. Remove transposition, transition, and directed-triangle cores with the
   permutation local lemma PP3ix.
4. Thin by endpoint-index support rank to dilute diffuse high-support patterns.
5. Apply the paid PP3ja endpoint to the remaining rank-four pair, high-support
   triple, and controller-shadow collateral terms.

The experiment does not prove an asymptotic endpoint trade. It verifies that the
new theorem tests the intended quantities and that the stored failures are
structurally genuine.