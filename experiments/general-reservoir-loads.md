# General reservoir and one-strip load experiments

These computations use exact integer determinants and rational probabilities.
They test the sufficient criteria in
[`docs/29-general-reservoir-patching.md`](../docs/29-general-reservoir-patching.md);
they are not asymptotic proofs.

## 1. One-strip averaging loads on the certificate corpus

Running

```bash
python scripts/analyze_one_strip_seed_loads.py \
  certificates/prime-patching-small.json
```

gives the following data. `U` is the number of noncorner boundary cells lying
on an old secant. `Q_occ` and `Q_empty` are the two mixed-pair counts from
PP3b.

| `n` | `|U|` | `|Q_occ|` | `|Q_empty|` | PP3b bound |
|---:|---:|---:|---:|---:|
| 2 | 4 | 1 | 0 | `9/2` |
| 3 | 6 | 1 | 1 | `41/9` |
| 4 | 8 | 1 | 1 | `17/4` |
| 5 | 10 | 1 | 2 | `149/35` |
| 6 | 12 | 3 | 4 | `235/54` |
| 7 | 14 | 1 | 7 | `337/77` |
| 8 | 16 | 1 | 7 | `445/104` |
| 9 | 18 | 2 | 9 | `578/135` |
| 10 | 20 | 4 | 12 | `366/85` |

Every stored seed has all `2n` noncorner boundary cells on at least one old
secant. Consequently the deliberately strong PP3b criterion fails before the
mixed-pair term is even considered. This is compatible with the exact
one-strip obstruction results: PP3b is a seed-preparation target, not a claim
about arbitrary certificates.

## 2. Regression check for an unrestricted patch

The stored `3 -> 4` unrestricted patch deletes

```text
(1,1), (2,3)
```

from the stored `n=3` certificate. Running

```bash
python scripts/analyze_reservoir_patch_loads.py \
  certificates/prime-patching-small.json \
  --n 3 --t 1 --delete 1,1 --delete 2,3
```

produces:

| Quantity | Value |
|---|---:|
| Active clone size `N` | 4 |
| Active rectangle cells | 9 |
| Allowed cells | 7 |
| Unavailable cells | 2 |
| Retained-anchor forbidden pairs | 4 |
| Internal candidate triples | 1 |
| Exact maximum clone load | `5/4` |
| Coarse PP2g load | `25/6` |

The patch itself exists and is independently verified, but both load criteria
fail. This is expected: PP2f and PP2g are sufficient local-lemma endpoints,
not necessary conditions.

## 3. Corner-only sanity checks

For the stored `n=2` certificate with `t=2` and no deletion, the new corner has
four cells, two of which are old-secant blocked. The exact maximum clone load is
`2/3` and the coarse load is `5/6`.

For the stored `n=4` certificate with `t=2` and no deletion, all four corner
cells are old-secant blocked. The exact maximum clone load is `1` and the
coarse load is `4/3`.

These examples reinforce the PP3 requirement: an arbitrary saturated seed can
have a completely shadowed future corner. A successful all-`n` route must
prepare the seed or delete a structured reservoir before invoking the exact
selection endpoint.
