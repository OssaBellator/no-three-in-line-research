# Swapped quarter-turn orbit cycle-cover diagnostic

Run:

```bash
python scripts/check_swapped_quarter_turn_orbit_csp.py \
  experiments/archived-prime-seed-codes.json
```

For every stored quarter-turn certificate, the checker:

1. independently verifies saturation and every exact determinant;
2. solves the swapped-layer parity colouring;
3. derives the signed pair permutation `(rho,e)`;
4. reconstructs the selected set as `m=(p-1)/2` four-point quarter-turn
   orbits;
5. rejects duplicate reverse orbits and oppositely oriented two-cycles; and
6. verifies every occupied nonaxis line by the linear orbit coefficients.

The finite pair-cycle partitions are:

```text
p=17: [8]
p=19: [5,4]
p=23: [10,1]
p=29: [13,1]
p=31: [10,4,1]
p=61: [29,1]
p=67: [32,1]
p=73: [36]
```

The checker repeats `1,230,128` exact determinant tests.  Lines containing zero
or one selected cell satisfy the capacity inequality automatically, so the
implementation generates only nonaxis lines containing at least two selected
cells.

The diagnostic verifies the exact signed cycle-cover reformulation for these
finite seeds.  It does not prove that the orbit CSP is feasible for every
sufficiently large prime.