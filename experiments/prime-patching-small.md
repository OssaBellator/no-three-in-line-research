# Small exact prime-patching experiments

These are finite computations, not asymptotic theorems. Every positive output
is rechecked with exact integer determinants.

## Certificate set

[`certificates/prime-patching-small.json`](../certificates/prime-patching-small.json)
contains saturated no-three-in-line configurations for every side length

\[
2\le n\le 10.
\]

```bash
python scripts/verify_no_three_certificate.py \
  certificates/prime-patching-small.json
```

The verifier checks exactly `2n` distinct in-range points, exactly two points in
every row and column, and all `binom(2n,3)` determinants.

## Exact boundary-only one-strip classification

Proposition PP1d shows that a boundary-only `n -> n+1` patch can delete only
one or two old points. Therefore `scripts/analyze_one_strip_extensions.py`
checks every possible state, with no deletion cutoff.

```bash
python scripts/analyze_one_strip_extensions.py \
  certificates/prime-patching-small.json
```

For the stored certificates the results are:

| Source `n` | Type-one candidates | Type-two candidates | Valid extensions |
|---:|---:|---:|---:|
| 2 | 4 | 2 | 2 |
| 3 | 6 | 9 | 0 |
| 4 | 8 | 20 | 0 |
| 5 | 10 | 35 | 0 |
| 6 | 12 | 54 | 0 |
| 7 | 14 | 77 | 0 |
| 8 | 16 | 104 | 0 |
| 9 | 18 | 135 | 0 |
| 10 | 20 | 170 | 0 |

Thus the displayed seeds for every `3<=n<=10` have no boundary-only one-strip
extension at all. Earlier bounded deletion searches are superseded by this
complete classification for the `t=1`, outer-strip-only model.

The `n=2` seed has two valid extensions, producing the two labeled saturated
no-three configurations on the `3 x 3` grid.

## Exhaustive small seed graph

The script

```bash
python scripts/enumerate_one_strip_seeds.py --max-n 5
```

enumerates all unions of two edge-disjoint permutations, deduplicates them,
filters by exact no-three tests, and applies every PP1d move. The exact labeled
counts are:

| `n` | Saturated states | No-three states | Extendable states | Directed extensions |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 | 2 |
| 3 | 6 | 2 | 1 | 1 |
| 4 | 90 | 11 | 4 | 9 |
| 5 | 2040 | 32 | 9 | 9 |

Starting from the unique `n=2` state and branching over every possible
boundary-only one-strip move, the numbers of reachable states at
`n=2,3,4,5` are

\[
1,2,1,0.
\]

Hence no recursive boundary-only one-strip chain reaches side five. This is a
finite refutation of that specific recursive gadget, not of wider strips,
interior replacements, or prepared absorber reservoirs.

## Unrestricted replacement chain

The general CSP search still finds an unrestricted chain through the current
certificate corpus:

| Transition | Search model | Deletions | Result |
|---|---:|---:|---|
| `2 -> 3` | boundary-only | 1 or 2 | found |
| `3 -> 4` | unrestricted | 2 | found |
| `4 -> 5` | unrestricted | 2 | found |
| `5 -> 6` | unrestricted | 3 | found |
| `6 -> 7` | unrestricted | 3 | found |
| `7 -> 8` | unrestricted | 3 | found |
| `8 -> 9` | unrestricted | 7 | found |
| `9 -> 10` | unrestricted | 6 | found |

For the displayed `n=3` certificate, one unrestricted `3 -> 4` patch deletes

\[
(1,1),(2,3)
\]

and inserts

\[
(1,3),(2,4),(4,1),(4,4).
\]

The point `(1,3)` is an old-old replacement cell. This demonstrates exactly why
a PP3 reservoir may need interior trades rather than a pure outer-strip rule.

## Wider-corner load profiling

For `t>=2`, `scripts/analyze_corner_patch_loads.py` deletes every corner cell
blocked by an old-pair secant, counts old-anchor forbidden pairs and internal
candidate triples, and evaluates the exact PP2c local-load inequality.

```bash
python scripts/analyze_corner_patch_loads.py \
  certificates/prime-patching-small.json --n 3 --t 10
```

The profiler is exhaustive and intended for modest `t`. Passing the inequality
certifies a patch; failing it is not a nonexistence proof, because the theorem
is only a sufficient endpoint.

## Interpretation

The finite data give two complementary messages:

1. arbitrary saturated seeds are not robust enough for naive one-strip
   recursion;
2. interior replacement can recover extensions that the boundary-only model
   forbids.

The open PP3 task is therefore genuine seed and reservoir preparation, not
merely choosing a larger deletion cutoff for the same outer-strip gadget.
