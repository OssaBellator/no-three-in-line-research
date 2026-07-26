# Prime-minus-one seed examples

Run:

```bash
python scripts/check_prime_minus_one_seed.py \
  experiments/prime-minus-one-seed-examples.json
```

The stored two-permutation certificates verify prime-minus-one seeds for:

```text
p=3   n=2
p=5   n=4
p=7   n=6
p=11  n=10
p=13  n=12
```

The largest case has `24` points and performs all `2024` exact determinant checks.
Every case has two edge-disjoint permutation layers, exactly two points in each row and
column, and no Euclidean collinear triple.

These examples are finite certificates only.  They do not prove existence for every
sufficiently large prime.
