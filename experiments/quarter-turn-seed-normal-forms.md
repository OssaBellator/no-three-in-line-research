# Quarter-turn seed normal-form diagnostic

Run:

```bash
python scripts/check_quarter_turn_seed_normal_forms.py \
  experiments/archived-prime-seed-codes.json
```

The checker independently repeats the saturation and exact determinant tests for
the eight stored quarter-turn archive codes.  It then solves both binary parity
systems for an alternating incidence colouring:

```text
fixed:   c(R(e))=c(e)
swapped: c(R(e))=c(e)+1 mod 2.
```

The verified action modes are:

```text
p=17: fixed, swapped
p=19: swapped
p=23: swapped
p=29: swapped
p=31: swapped
p=61: swapped
p=67: swapped
p=73: fixed, swapped
```

For fixed action the checker verifies that both layer permutations square to
coordinate reversal.  For swapped action it verifies that the first layer
commutes with reversal and that the second layer is forced as
`sigma^(-1) o J`.  In every mode the relative permutation commutes with `J`,
and every odd cycle length has even multiplicity.

The diagnostic performs `1,230,128` exact determinant tests.  These are finite
structural certificates for the stored quarter-turn cases, not an asymptotic
seed construction.