# Sign-coherent threshold drift

`docs/647` shows that the eight nearest legal targets admit 49 assignments of
distinct transient buffer cells. Distinctness removes buffer reuse, but it does
not address the displacement accumulated at the batch endpoint.

## PP3czv — The nearest-target family is cellwise sign-coherent

For every matrix cell, all eight target-minus-source entries have one sign: no
cell is increased by one nearest target and decreased by another.

### Proof

`scripts/check_threshold_sign_coherent_drift.py` reconstructs all 4,475 legal
four-layer matrices and the eight distance-six targets. It checks the eight
signed differences in each of the sixteen cells and finds no cell containing
both `+1` and `-1`. ∎

## PP3czw — Every nonempty target subset has additive drift

For any nonempty subset `S` of the eight nearest targets,

```text
|| sum_{T in S} (T-SOURCE) ||_1 = 6 |S|.
```

In particular, no nonempty subset has zero aggregate displacement.

### Proof

Each individual target has `L1` displacement six. By `PP3czv`, absolute values
commute with summation cell by cell, so no cancellation is possible. The checker
exhausts all 255 nonempty subsets. ∎

## PP3czx — Distinct buffers do not change endpoint drift

Every one of the 49 perfect transient assignments and all 12,544 ordered
factorization batches have the same target endpoint displacement. For the batch
containing all eight targets, the aggregate signed matrix is

```text
(-5,-1, 1, 5,
  5,-5,-1, 1,
  1, 5,-5,-1,
 -1, 1, 5,-5).
```

Its `L1` norm is 48.

### Proof

The transient cell cancels between the two swaps of each factorization, so it is
absent from the endpoint. Assignment and swap order can change exposed states,
but not the sum of target-minus-source matrices. ∎

## Evidence boundary

The distinct-buffer construction solves a scheduling collision, not the endpoint
balance problem. A geometric threshold batch must supply an inverse or other
compensating source operation; batching only nearest targets can never neutralize
its own displacement.
