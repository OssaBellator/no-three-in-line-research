# Random matching-block sparsification diagnostics

This experiment accompanies
[`docs/56-random-matching-block-sparsification.md`](../docs/56-random-matching-block-sparsification.md).

The command

```bash
python scripts/analyze_random_matching_block_sparsification.py \
  certificates/prime-patching-small.json --r 5
```

enumerates every five-edge subset of both perfect-matching layers.  For each
pool it computes the exact PP3ca signature load and exact canonical clean-state
fraction.  It also verifies that the average load does not exceed the universal
PP3cl bound.

## Exact five-edge results

| Side | Layer | Average PP3ca load | Average exact clean fraction | Pools with load `<1` / total |
|---:|---:|---:|---:|---:|
| 5 | 0 | `16/5` | `2/5` | `0/1` |
| 5 | 1 | `6/5` | `3/5` | `0/1` |
| 6 | 0 | `5/3` | `8/15` | `2/6` |
| 6 | 1 | `1` | `2/3` | `3/6` |
| 7 | 0 | `41/35` | `71/105` | `7/21` |
| 7 | 1 | `41/35` | `2/3` | `7/21` |
| 8 | 0 | `281/280` | `197/280` | `26/56` |
| 8 | 1 | `57/70` | `211/280` | `33/56` |
| 9 | 0 | `20/21` | `461/630` | `73/126` |
| 9 | 1 | `613/630` | `461/630` | `71/126` |
| 10 | 0 | `827/1260` | `254/315` | `180/252` |
| 10 | 1 | `857/1260` | `73/90` | `179/252` |

The exact clean fraction improves with the side in this small corpus.  The
universal PP3cl bound is much larger than the exact average at these sizes—for
example it is `968/9` at `(m,r)=(10,5)`—because PP3ck counts every possible
candidate cell and pair rather than the sparse realized signatures of one
certificate.

The asymptotic use is different.  PP3cl gives

\[
\lambda(m,r)=O(r^2/m+r/m),
\]

so the bound tends to zero for `r=m^0.475` even without any certificate-specific
savings.  The finite table is a regression check for the exact enumeration and
not evidence for the asymptotic rate.