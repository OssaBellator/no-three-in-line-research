# Two-cycle-free and near-Hamilton signed-cover audit

Run:

```bash
python scripts/check_two_cycle_free_near_hamilton_family.py \
  experiments/archived-prime-seed-codes.json \
  experiments/two-cycle-free-near-hamilton-family-audit.json
```

The thirteen public/code swapped certificates have pair-cycle partitions

```text
p=17: [8]
p=19: [5,4]
p=23: [10,1]
p=29: [13,1]
p=31: [10,4,1]
p=41: [19,1]
p=43: [17,3,1]
p=47: [22,1]
p=53: [12,8,5,1]
p=59: [28,1]
p=61: [29,1]
p=67: [32,1]
p=73: [36]
```

Every partition is pair-2-cycle-free.  The Hamilton cases are `p=17,73`, and
the one-fixed near-Hamilton cases are

```text
p=23,29,41,47,59,61,67.
```

Thus nine of the thirteen verified records lie in the Hamilton or one-fixed
near-Hamilton family.

The exact coefficient audit compares canonical edge-disjoint covers `A_m` with
canonical two-cycle-free covers `C_m`:

| `m` | `A_m` | `C_m` | `C_m/A_m` |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1.000000 |
| 1 | 1 | 1 | 1.000000 |
| 2 | 3 | 1 | 0.333333 |
| 3 | 23 | 17 | 0.739130 |
| 4 | 185 | 161 | 0.870270 |
| 5 | 1,809 | 1,409 | 0.778883 |
| 6 | 21,739 | 16,609 | 0.764019 |
| 7 | 304,807 | 237,649 | 0.779670 |
| 8 | 4,876,017 | 3,805,633 | 0.780480 |
| 9 | 87,761,825 | 68,334,209 | 0.778632 |
| 10 | 1,755,259,091 | 1,366,734,401 | 0.778651 |

The ratio approaches `exp(-1/4)=0.778800...`, as proved in PP3biy.  The values
through `m=8` are also independently recovered by exhaustive weighted
enumeration of all

```text
0!+1!+...+8! = 46,234
```

pair permutations, using the cycle weights from PP3bfo rather than the
generating functions.

The cylinder audit exhaustively enumerates directed cycles through pair size
`m=8` and checks every compatible path forest of at most three prescribed
edges.  It verifies

```text
19,846 full-Hamilton path forests,
19,534 one-fixed path forests,
39,380 total path forests.
```

For a full Hamilton cycle, every `r`-edge path forest occurs in exactly
`(m-r-1)!` cyclic orders.  In the one-fixed family, a forest using `v` vertices
occurs in exactly `(m-v)(m-r-2)!` choices of fixed vertex and cyclic order.
Independent orientation bits then give the cylinder probabilities in PP3bjc
and PP3bjd.

The complete machine-readable ledger is stored in
`experiments/two-cycle-free-near-hamilton-family-results.json`.

This diagnostic verifies a structural reduction and a probability barrier.  It
does not prove the asymptotic seed theorem.
