# Prime-minus-one seed examples

Run:

```bash
python scripts/check_prime_minus_one_seed.py \
  experiments/prime-minus-one-seed-examples.json
```

The stored two-permutation certificates verify prime-minus-one seeds for:

```text
p=3,5,7,11,13,17,19,23,29,31,37,47,61,67,73
```

The largest case has `144` points on `[72]^2` and performs all `487344`
exact determinant checks. Every case has two edge-disjoint permutation
layers, exactly two points in each row and column, and no Euclidean
collinear triple.

The cases through `p=13` were generated inside this research branch. The
`p=37` certificate was generated internally by an exact support-thirteen
repair in the swapped quarter-turn orbit CSP. The `p=47` certificate was
independently decoded and reverified from the first public RLE record in
`mvr/no-three-in-line:results/c4-46.out`; its dedicated provenance checker is
`scripts/check_p47_public_rle_certificate.py`. The
`p=17,19,23,29,31,61,67,73` cases were independently decoded and reverified
from compact public archive codes.

These examples are finite certificates only. They do not prove existence for
every sufficiently large prime.
