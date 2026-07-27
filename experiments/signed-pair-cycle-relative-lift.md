# Signed pair-cycle relative lift diagnostic

Run:

```bash
python scripts/check_signed_pair_cycle_relative_lift.py \
  experiments/archived-prime-seed-codes.json \
  experiments/p37-swapped-quarter-turn-near-example.json
```

The checker obtains a swapped quarter-turn layer decomposition, extracts the
signed pair permutation `(rho,e)`, and decomposes `rho` into cycles.  For each
pair cycle it records:

```text
cycle length ell,
orientation xor s,
and the relative cycles predicted by PP3bfn.
```

It then constructs the full relative permutation `sigma^(-1) o tau` and checks
that the direct cycle partition is identical to the compiled partition.

The nine checked records give:

```text
p=17: (8,1)                       -> [8,8]
p=19: (5,0),(4,0)                 -> [10,2,2,2,2]
p=23: (10,1),(1,0)                -> [5,5,5,5,2]
p=29: (13,0),(1,0)                -> [26,2]
p=31: (10,1),(4,0),(1,0)          -> [5,5,5,5,2,2,2,2,2]
p=61: (29,1),(1,0)                -> [58,2]
p=67: (32,0),(1,0)                -> [16,16,16,16,2]
p=73: (36,1)                      -> [36,36]
p=37 near-state: (11,1),(6,0),(1,1) -> [22,6,6,2]
```

Here each ordered pair is `(pair-cycle length, orientation parity)`.

The diagnostic proves only the algebraic lift for the supplied records.  It
does not assert that the `p=37` near-state is valid and does not prove the
asymptotic seed theorem.