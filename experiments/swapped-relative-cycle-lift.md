# Swapped relative-cycle lift diagnostic

Run:

```bash
python scripts/check_swapped_relative_cycle_lift.py \
  experiments/swapped-relative-cycle-lift-example.json
```

The checker exhausts every signed pair permutation through seven pair vertices,
for a total of `695,483` ordered signed permutations.  It constructs the full
swapped-quarter-turn layer pair, computes the relative permutation directly,
and checks the cycle-by-cycle lift formula.

The exact counts are:

```text
 m   all ordered   ordered disjoint   canonical covers   canonical disjoint
 0             1                  1                  1                    1
 1             2                  2                  1                    1
 2             8                  6                  5                    3
 3            48                 36                 29                   23
 4           384                300                233                  185
 5         3,840              3,000              2,329                1,809
 6        46,080             35,880             27,949               21,739
 7       645,120            502,320            391,285              304,807
```

For every edge-disjoint state, every odd relative-cycle length occurs with
multiplicity divisible by four.  The checker also evaluates the three exact
exponential-generating-function coefficients using rational arithmetic.

Both the ordered edge-disjoint fraction and the canonical edge-disjoint
fraction tend to

```text
exp(-1/4) = 0.778800783...
```

This diagnostic concerns collision removal and relative-cycle structure.  It
does not test maximal-line feasibility and does not prove the asymptotic seed
theorem.
