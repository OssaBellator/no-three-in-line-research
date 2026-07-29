# Frontier pass: labeled sparse cycle defects

## Added

- SAS5ig: exact physical-label partition of fundamental defect mass.
- SAS5ih: one label carries at least `D/K`, and one sign at least `D/(2K)`.
- SAS5ii: one non-tree edge realizes the corresponding edge-level bound.
- SAS5ij: complete labeled history router.

## Corrected frontier

Sparse history dependence is now finite, physically labeled and sign-resolved. Remaining work is to construct the actual legal-state graphs and show the returned arithmetic, line, boundary, owner, occurrence or lineage classes cancel or are otherwise resolved.

## Verification

`scripts/verify_sparse_labeled_fundamental_defects.py` checks the label, sign and edge-level concentration bounds.