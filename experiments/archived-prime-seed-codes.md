# Archived and public prime-seed code diagnostic

Run:

```bash
python scripts/check_archived_prime_seed_codes.py \
  experiments/archived-prime-seed-codes.json
```

Each JSON record contains:

- the prime `p`;
- the source archive, repository, or coordinate-record path;
- the exact standard row-pair code; and
- the expected relative cycle partition.

The checker independently:

1. decodes two column symbols per row;
2. verifies two points in every row and column;
3. checks every exact integer determinant;
4. alternately colours the 2-regular incidence graph into two permutation
   layers;
5. reconstructs the original selected set; and
6. computes the relative derangement and cycle partition.

The stored suite verifies:

```text
p=17,19,23,29,31,41,43,47,53,59,61,67,73
```

and performs `1,968,716` exact determinant checks in total. The largest case
has `144` selected points on `[72]^2`.

The `p=41,43,53` compact codes are the first records of the public
`n40_rot4`, `n42_rot4`, and `n52_rot4` files; their complete archive digests
are retained in `experiments/public-rot4-prime-certificates-p41-p43-p53.json`.
The `p=47` compact code is independently generated from the first public RLE
record in `mvr/no-three-in-line:results/c4-46.out`. The `p=59` compact code is
independently generated from Prellberg's attributed Wikimedia Commons
coordinate record for `N=58`, licensed CC BY-SA 4.0. The other records are
transcribed from the Flammenkamp configuration archive.

The source code, RLE, or coordinate list is used only as compact input. No
geometric validity is trusted without the independent determinant check. These
finite certificates do not prove the asymptotic seed theorem.
