# Quantitative obstruction for every unmodified `2 x 5` product host

The earlier full-selector census proved that no unmodified `2 x 5` or `5 x 2`
global product host contains a no-three degree-two state. This chapter sharpens
that statement by computing the exact minimum possible number of bad triples in
every `2 x 5` host.

Layer swaps do not change the full four-layer product host. Up to swapping the
two fine permutation layers, there are `32` saturated no-three factor
configurations at side five. The side-two factor has one underlying
configuration. Thus each radix orientation has `32` distinct hosts, covering
all `128` ordered factor-pair instances after restoring layer order.

## Theorem PX23 — PROVED FINITE

Every degree-two state in every unmodified global `2 x 5` factor-product host
contains at least two collinear triples.

More precisely, among the `32` layer-unordered hosts in each orientation, the
minimum triple-potential distributions are:

| Orientation | Number of hosts by exact minimum potential |
|---|---|
| `cc` | `12` hosts with minimum `7`; `12` with minimum `8`; `8` with minimum `9` |
| `cf` | `4` hosts with minimum `2`; `12` with minimum `3`; `8` with minimum `4`; `4` with minimum `5`; `4` with minimum `6` |
| `fc` | `4` hosts with minimum `2`; `12` with minimum `3`; `8` with minimum `4`; `4` with minimum `5`; `4` with minimum `6` |
| `ff` | `8` hosts with minimum `2`; `4` with minimum `3`; `12` with minimum `4`; `8` with minimum `5` |

Consequently, the earlier zero-model result has a uniform quantitative gap:

\[
\boxed{
\min_Q T(Q)\ge2
}
\]

for every ordered `2 x 5` factor pair and every global radix orientation.

## Proof

For one host, expose the scalar rows in order. Each row has four host cells and
a degree-two state chooses one of its six two-element subsets. Track the current
column degrees and prune whenever the remaining rows cannot complete every
column to degree two.

When the next row inserts two cells, every newly completed collinear triple
contains exactly one of those cells and two previously exposed cells. Precompute
all such prior-pair certificates. The search therefore accumulates the exact
triple potential monotonically and prunes any branch already exceeding the best
complete state found.

Run this exact branch-and-bound search for all `32` layer-unordered side-five
factors and all four orientations. The displayed distributions result.
Swapping either factor's two permutation layers leaves the full host unchanged,
so the census covers all ordered decompositions. \(\square\)

## Interpretation

The `2 x 5` obstruction is not caused by a single unlucky factor pair or by one
radix orientation. Even the best unmodified host states retain at least two
bad triples, and ordinary `cc` products retain at least seven.

This gives a sharper target for any enlarged construction. An offset, digit-map,
or absorber extension must remove a genuine positive defect gap, not merely
unlock a state missed by the original SAT search.

The theorem remains computational and finite. It does not identify a concise
human-readable unsatisfiable core common to all hosts. Extracting such a core
is a useful next task because it may reveal which additional host cells or
offsets are sufficient.

## Verification

Run

```bash
python scripts/verify_product_2x5_minimum_defects.py
```

The script uses only the standard library and checks the complete distribution,
not just the lower bound two.
