# General reservoir and one-strip load experiments

These computations use exact integer determinants and rational probabilities.
They test the sufficient criteria in:

- [`docs/29-general-reservoir-patching.md`](../docs/29-general-reservoir-patching.md);
- [`docs/30-deletion-aware-row-lift-banks.md`](../docs/30-deletion-aware-row-lift-banks.md).

They are finite checks, not asymptotic proofs.

## 1. The unconditioned one-strip average is universally vacuous

Running

```bash
python scripts/analyze_one_strip_seed_loads.py \
  certificates/prime-patching-small.json
```

gives the following data. `U` is the number of noncorner boundary cells lying
on an old secant. `Q_occ` and `Q_empty` are the mixed-pair counts from PP3b.

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

This is not a peculiarity of the stored certificates. Every saturated seed has
`|U|=2n`: each top boundary cell lies on the vertical secant through its old
column pair, and each right boundary cell lies on the horizontal secant through
its old row pair. Proposition PP3c records this exact obstruction.

The forced type-two deletion automatically clears those axis blocker edges, so
a meaningful average must be deletion-aware.

## 2. Deletion-aware type-two certificate masses

Running

```bash
python scripts/analyze_deletion_aware_one_strip.py \
  certificates/prime-patching-small.json
```

gives:

| `n` | Nonaxis blocker incidences `B` | `A_occ` | `A_empty` | PP3f bound | Exact average defects | Minimum | Clean states |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 0 | 1 | 0 | `1/2` | `1/2` | 0 | 1 |
| 3 | 4 | 2 | 1 | `10/3` | `8/3` | 1 | 0 |
| 4 | 8 | 1 | 2 | `89/20` | `67/20` | 2 | 0 |
| 5 | 9 | 1 | 3 | `139/35` | `114/35` | 1 | 0 |
| 6 | 13 | 3 | 5 | `257/54` | `118/27` | 1 | 0 |
| 7 | 20 | 2 | 8 | `474/77` | `417/77` | 2 | 0 |
| 8 | 27 | 1 | 10 | `743/104` | `82/13` | 4 | 0 |
| 9 | 35 | 3 | 13 | `221/27` | `1013/135` | 3 | 0 |
| 10 | 40 | 4 | 14 | `142/17` | `668/85` | 3 | 0 |

The deletion-aware theorem detects the valid `2 -> 3` type-two extension. It
also shows exactly where the later stored seeds fail: their nonaxis blocker and
mixed-anchor certificate mass remains too large even after the automatic axis
blockers are removed.

The coarse PP3f value is an upper bound on the exact average. The gap records
certificates cleared by the chosen deletion beyond the guaranteed axis
clearance.

## 3. Regression check for an unrestricted patch

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

## 4. Row-lift reservoir bank sanity check

For the stored side-three certificate, delete all three old rows and add three
new rows and columns:

```bash
python scripts/analyze_row_lift_bank.py \
  certificates/prime-patching-small.json \
  --n 3 --rows 1,2,3
```

The exact bank has:

| Quantity | Value |
|---|---:|
| Movement states | 12 |
| Refill states | 12 |
| Total states | 144 |
| Support cells | 18 |
| Maximum cell probability | `2/3` |
| Maximum pair probability | `1/2` |
| Maximum triple probability | `1/3` |
| Blocked support cells | 0 |
| Retained-anchor support pairs | 0 |
| Compatible internal support triples | 34 |
| Exact expected certificates | `34/3` |
| Minimum certificates in one state | 3 |
| Clean states | 0 |

Deleting the entire old configuration removes every external certificate in
this example. The obstruction is purely internal: the cross-shaped support has
34 compatible nonaxis collinear triples, and every one of the 144 exact degree
states selects at least three triple certificates.

This confirms both halves of the new result:

- the row-lift bank supplies the promised interchangeable states and spread;
- spread alone does not solve the internal direction problem.

The next finite experiment is to search over reservoir-row choices and
direction-pruned subbanks rather than use the full cross support.

## 5. Corner-only sanity checks

For the stored `n=2` certificate with `t=2` and no deletion, the new corner has
four cells, two of which are old-secant blocked. The exact maximum clone load is
`2/3` and the coarse load is `5/6`.

For the stored `n=4` certificate with `t=2` and no deletion, all four corner
cells are old-secant blocked. The exact maximum clone load is `1` and the
coarse load is `4/3`.

These examples reinforce the PP3 requirement: an arbitrary saturated seed can
have a completely shadowed future corner. A successful all-`n` route must
prepare the seed, delete a structured reservoir, and control the internal
directions of the resulting completion bank.

## 6. Exhaustive reservoir-row search on the stored corpus

Running

```bash
python scripts/search_row_lift_reservoirs.py \
  certificates/prime-patching-small.json
```

enumerates every two- and three-row reservoir in every stored certificate.
Across the 17 `(n,t)` cases with `2<=n<=10` and `t in {2,3}`, no unrestricted
full row-lift bank contains a clean state. The best minimum certificate counts
are:

| `n` | `t=2` | `t=3` |
|---:|---:|---:|
| 2 | 4 | -- |
| 3 | 2 | 3 |
| 4 | 2 | 3 |
| 5 | 4 | 3 |
| 6 | 4 | 3 |
| 7 | 5 | 5 |
| 8 | 5 | 7 |
| 9 | 5 | 6 |
| 10 | 6 | 7 |

This is a finite statement about the stored seeds, not an asymptotic
refutation. It does show that choosing reservoir rows while retaining the full
four-permutation state space is insufficient on the current corpus. Direction
constraints or state pruning must be part of the PP3 preparation mechanism.
