# Sparse frontier pass: fundamental cycle defects

**Branch:** `research/sparse-algebraic-spread`

## New theorem block

- **SAS5ib:** canonical tree potential on a spanning forest.
- **SAS5ic:** every non-tree edge carries its exact fundamental-cycle defect.
- **SAS5id:** vanishing fundamental defects are equivalent to a state coboundary.
- **SAS5ie:** the defect dictionary has size `|E|-|V|+kappa`, with one concentrated nonzero defect when total defect mass is positive.
- **SAS5if:** complete finite history router.

## Executable check

`scripts/verify_sparse_fundamental_cycle_defects.py`

Equivalent local execution verified **4,420** finite state-graph charge systems.

## Updated frontier

History dependence is represented by a finite cycle basis rather than arbitrary path comparisons. Remaining work is to build the actual legal-state graphs for arithmetic, line, boundary, owner and payment profiles, prove their charges are coboundaries, or pay the returned fundamental defects and lineage failures.