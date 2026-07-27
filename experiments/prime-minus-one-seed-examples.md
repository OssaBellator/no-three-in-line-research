# Prime-minus-one seed examples

Run:

```bash
python scripts/check_prime_minus_one_seed.py \
  experiments/prime-minus-one-seed-examples.json
```

The stored two-permutation certificates verify prime-minus-one seeds for every
odd prime through `73`:

```text
p=3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,73
```

The largest case has `144` points on `[72]^2` and performs all `487344`
exact determinant checks. Every case has two edge-disjoint permutation
layers, exactly two points in each row and column, and no Euclidean
collinear triple.

The cases through `p=13` were generated inside this research branch. The
`p=37` certificate was generated internally by an exact support-thirteen
repair in the swapped quarter-turn orbit CSP. The `p=41,43,53` certificates
were independently decoded from the first records of the public
`n40_rot4`, `n42_rot4`, and `n52_rot4` archive files. The `p=47` certificate
was independently decoded from the first public RLE record in
`mvr/no-three-in-line:results/c4-46.out`. The `p=59` certificate was
independently reconstructed from the attributed Wikimedia Commons coordinate
record for `N=58`, licensed CC BY-SA 4.0. The
`p=17,19,23,29,31,61,67,73` cases were independently decoded and reverified
from compact public archive codes.

These examples are finite certificates only. They do not prove existence for
every sufficiently large prime.
