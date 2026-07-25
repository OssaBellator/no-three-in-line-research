# Prime-patching frontier addendum: credited-bank support closure

This addendum extends `proofs/prime-patching-recent-index.md` after PP3afm.
It records the paid resource-bank reductions in `docs/193` through `docs/195`
without replacing the larger historical ledger.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3afn--PP3aft | Ambient random thinning makes all selected credit-line self-recapture identically zero while preserving a source-regular paid subbank | PROVED / CONDITIONAL PAID INTERFACE | `docs/193-credited-line-self-recapture-thinning.md` |
| PP3afu--PP3afz | A recapture-free credited resource bank either has a zero-insertion paid permutation or a purely foreign quadratic unary/cubic binary support core | PROVED | `docs/194-recapture-free-resource-bank-endpoint.md` |
| PP3aga--PP3agg | Adaptive ambient thinning absorbs every vanishing foreign support density; persistent failure is a positive-density ambient unary/rank-three/rank-four resource star | PROVED | `docs/195-adaptive-ambient-foreign-support-thinning.md` |

## Updated resource-bank endpoint

Let the ambient credited endpoint bank have size

```text
Q=m^(21/40+o(1))
```

and thin adaptively to `q->infinity` with

```text
q^3/Q=o(1).
```

Each chosen credit line has a matching trace on the tied endpoint rectangle.
An off-diagonal recreation of one selected credit requires three prescribed
endpoint indices, so a source-regular subbank can be chosen with no
self-recapture at all. Every derangement destroys all selected witness
incidences and recreates none of them.

Split foreign binary support by endpoint-index rank. Conditional on retaining
one incident resource, a rank-`h` support survives with exact factor

```text
(q-1)_(h-1)/(Q-1)_(h-1).
```

Choose `q` slowly enough that the rank-four normalized ambient degree times
`q` tends to zero. After deleting `o(q)` exceptional indices, the foreign
unary degree is `o(q)` and the total foreign binary degree is `o(q^2)`. The
zero-cost permutation local lemma then gives a strict `Xi` decrease.

Consequently failure requires at least one ambient fixed-resource degree
threshold:

```text
Delta_1=Omega(Q),
Delta_3=Omega(Q^2),
Delta_4=Omega(Q^3).
```

Rank-two binary support is automatically lower order under the adaptive
thinning.

## Revised open paid objects

The selected witness incidences of source-star, hard-unary, transition, and
binary resource banks are no longer part of their own insertion collateral.
Diffuse foreign insertion support is also absorbed. The remaining paid objects
are:

1. positive-density ambient unary insertion-shadow stars;
2. positive-density ambient rank-three or rank-four binary stars;
3. fixed-centre arc/path-petal cost;
4. fixed-cell fan multiplicity after conditioning;
5. conditional-Hall and alternating-host residual structure;
6. source preparation or endpoint-host failure;
7. local insertion multiplicity already comparable with removal credit.

Rich designated recapture fibres, selected-credit self-recreation, and diffuse
foreign support cores are no longer independent frontiers.

The no-three-in-line conjecture remains unproved.
