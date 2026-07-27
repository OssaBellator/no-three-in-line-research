# Public quarter-turn archive certificates for p=41, p=43, and p=53

The first records of the public `n40_rot4`, `n42_rot4`, and `n52_rot4`
archive files were retrieved on 2026-07-27 and independently decoded. The
complete bulk files are not stored in this repository. Their byte lengths,
record counts, and SHA-256 digests are retained in the JSON certificate.

The verifier starts from each stored standard row-pair code and checks:

- exactly `2n` distinct selected cells;
- exactly two cells in every row and column;
- quarter-turn invariance;
- deterministic swapped-equivariant decomposition into two disjoint permutations;
- the forced swapped identity and reversal commutation;
- signed pair-cover and relative-cycle data; and
- every exact integer determinant.

With the original archive directory available, it additionally checks each
complete file digest, byte count, record count, and that the stored code is its
first record.

## Exact results

| p | n | archive records | pair cycles | relative cycles | determinant checks |
|---:|---:|---:|---|---|---:|
| 41 | 40 | 541 | `[19,1]` | `[38,2]` | 82,160 |
| 43 | 42 | 746 | `[17,3,1]` | `[34,6,2]` | 95,284 |
| 53 | 52 | 5,062 | `[12,8,5,1]` | `[10,8,8,6,6,6,6,2]` | 182,104 |

Every determinant is nonzero and the minimum absolute determinant is one in all
three cases.

## Reproduction

```bash
python scripts/check_public_rot4_prime_certificates.py \
  experiments/public-rot4-prime-certificates-p41-p43-p53.json

python scripts/check_public_rot4_prime_certificates.py \
  experiments/public-rot4-prime-certificates-p41-p43-p53.json \
  --archive-dir /path/to/archive-files
```

The finite certificates do not constitute a uniform construction and do not
prove the asymptotic prime-minus-one seed theorem.
