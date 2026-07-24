# Small exact prime-patching experiments

These experiments use `scripts/search_boundary_extension.py` and are finite
computations, not asymptotic theorems. Every reported positive output was
rechecked by `scripts/verify_no_three_certificate.py`.

## Certificate set

[`certificates/prime-patching-small.json`](../certificates/prime-patching-small.json)
contains saturated no-three-in-line configurations for every side length

\[
2\le n\le 10.
\]

The verifier checks exactly `2n` distinct in-range points, exactly two points in
every row and column, and all `binom(2n,3)` integer determinants.

```bash
python scripts/verify_no_three_certificate.py \
  certificates/prime-patching-small.json
```

## One-step extension chain

The search found the following `t=1` transitions. The deletion count is the
number of old points removed before the prescribed-degree completion.

| Transition | Search model | Deletions | Result |
|---|---:|---:|---|
| `2 -> 3` | boundary-only | 1 | found |
| `3 -> 4` | boundary-only | at most 4 | exhausted |
| `3 -> 4` | unrestricted | 2 | found |
| `4 -> 5` | unrestricted | 2 | found |
| `5 -> 6` | unrestricted | 3 | found |
| `6 -> 7` | unrestricted | 3 | found |
| `7 -> 8` | unrestricted | 3 | found |
| `8 -> 9` | unrestricted | at most 5 | exhausted |
| `8 -> 9` | unrestricted | 7 | found |
| `9 -> 10` | unrestricted | 6 | found |

Here `boundary-only` means every inserted point lies in a new row or new
column. `Unrestricted` permits replacement points in old-old cells.

For the displayed `n=3` certificate, the exact boundary-only search exhausts
all deletion sets of size at most four, but an unrestricted two-deletion patch
exists. One such patch deletes

\[
(1,1),(2,3)
\]

and inserts

\[
(1,3),(2,4),(4,1),(4,4).
\]

The point `(1,3)` is an interior replacement cell. Thus this particular seed
cannot be extended by the tested outer-strip-only model within four deletions,
while allowing one interior replacement succeeds.

## Interpretation

This is a concrete warning against a PP2 theorem that only searches the new
row/column strips. It does **not** show that every `n=3` seed requires an
interior change, and it does not rule out boundary gadgets with a larger or
different reservoir model.

Likewise, the `8 -> 9` exhaustion at deletion budget five is only a statement
about the displayed `n=8` seed and the exact CSP implemented by the script. The
seven-deletion success shows that the obstruction is a budget obstruction, not
an absolute nonextendability result.
