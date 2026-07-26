# Prime-seed relative-cycle and maximal-line diagnostic

Run:

```bash
python scripts/check_prime_seed_relative_cycles.py \
  experiments/prime-seed-relative-cycle-example.json
```

For the stored certificates the checker reports:

```text
p=3:  relative cycles [2],    maximal lines checked 0
p=5:  relative cycles [2,2],  maximal lines checked 14
p=7:  relative cycles [6],    maximal lines checked 58
p=11: relative cycles [10],   maximal lines checked 406
```

Every relative permutation is fixed-point-free, every `tau` layer is exactly
reconstructed as `sigma o pi`, and every maximal grid line contains at most two
selected cells.

The checker validates exact finite certificates and the compressed constraint
bookkeeping.  It does not establish asymptotic feasibility for prime-minus-one
boards.
