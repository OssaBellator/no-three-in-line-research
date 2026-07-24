# Exact census for the simplest blockwise reversals

PX25 shows that simultaneous reversal of the fine digits in the second coarse
row and second coarse column can repair one `2 x 5` product. This note exhausts
that fixed reversal pattern over every distinct saturated no-three factor at
side five and compares it with the two one-sided variants.

Layer order does not change the full four-layer host. There are 64 ordered
side-five factor pairs and 32 distinct hosts after identifying the swap of the
two fine permutation layers.

Let

\[
\rho=(4,3,2,1,0).
\]

For the side-two outer factor, test three local-map patterns:

1. **both:** `alpha=(id,rho)` and `beta=(id,rho)`;
2. **row-only:** `alpha=(id,rho)` and `beta=(id,id)`;
3. **column-only:** `alpha=(id,id)` and `beta=(id,rho)`.

For every pattern, every side-five factor host, and every orientation, search
all spanning degree-two subgraphs exactly until a no-three state is found or the
state space is exhausted.

## Theorem PX28 — PROVED FINITE

The numbers of successful layer-unordered side-five factor hosts are:

| Pattern | `cc` | `cf` | `fc` | `ff` |
|---|---:|---:|---:|---:|
| simultaneous row and column reversal | 2 / 32 | 2 / 32 | 2 / 32 | 7 / 32 |
| row reversal only | 0 / 32 | 0 / 32 | 0 / 32 | 0 / 32 |
| column reversal only | 0 / 32 | 0 / 32 | 0 / 32 | 0 / 32 |

Thus the side-ten witness is part of a larger exact positive family: the one
fixed simultaneous reversal creates thirteen successful orientation--factor
hosts. Neither one-sided reversal creates a single successful host in the
complete census.

### Proof

Generate every ordered pair of pointwise-disjoint side-five permutations whose
union is no-three, then quotient only by swapping the two layers. For each of
the resulting 32 factors, construct the locally permuted four-regular host.
Expose scalar rows in order and choose two of the four host cells in each row.
Prune whenever a column exceeds degree two, the remaining rows cannot complete
a column to degree two, or the new cells complete a collinear triple with two
previously selected cells. The search is exact and returns the displayed
counts. \(\square\)

## Interpretation

The useful geometry is genuinely two-coordinate. Merely reordering scalar rows
inside one coarse row block, or merely reordering scalar columns inside one
coarse column block, leaves all 32 side-five factors infeasible. Applying the
same reversal on both sides changes the coupling of row and column digits and
breaks the unmodified positive defect gap for several factors.

This makes blockwise digit maps a credible enlarged-host route, but not yet a
closure theorem: most side-five factors remain infeasible under this one fixed
map, and the reflection-only selector from PX26 is much narrower than the full
successful census.

## Verification

Run

```bash
python scripts/verify_product_blockwise_reversal_census.py
```
