# Prime-patching frontier addendum: credited-bank support closure

This addendum extends `proofs/prime-patching-recent-index.md` after PP3afm.
It records the paid resource-bank and fixed-cell reductions in `docs/193`
through `docs/197` without replacing the larger historical ledger.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3afn--PP3aft | Ambient random thinning makes all selected credit-line self-recapture identically zero while preserving a source-regular paid subbank | PROVED / CONDITIONAL PAID INTERFACE | `docs/193-credited-line-self-recapture-thinning.md` |
| PP3afu--PP3afz | A recapture-free credited resource bank either has a zero-insertion paid permutation or a purely foreign quadratic unary/cubic binary support core | PROVED | `docs/194-recapture-free-resource-bank-endpoint.md` |
| PP3aga--PP3agg | Adaptive ambient thinning absorbs every vanishing foreign support density; persistent failure is a positive-density ambient unary/rank-three/rank-four resource star | PROVED | `docs/195-adaptive-ambient-foreign-support-thinning.md` |
| PP3agh--PP3agn | A marked source-star centre recreates only an `O(q/Q)` fraction of its own credit; failure is foreign support, marked source structure, or endpoint-host failure | PROVED / CONDITIONAL MARKED PAID INTERFACE | `docs/196-marked-source-star-credit-amortization.md` |
| PP3ago--PP3agt | Thresholding a fixed-cell candidate fan pays all light partners; failure yields a uniform heavy partner pencil, conditional Hall structure, or foreign paid/source concentration | PROVED / CONDITIONAL PAID INTERFACE | `docs/197-thresholded-fixed-cell-fan-payment.md` |

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
endpoint indices, so a source-regular resource subbank can be chosen with no
self-recapture at all. Every derangement destroys all selected witness
incidences and recreates none of them.

For a source-star centre owning `C` credit lines, zero trace support is not
needed. Under the exact marked subset-and-derangement law,

```text
E I_self <= C(q-2)/(Q-2).
```

Thus a marked source-star spends only an `O(q/Q)` fraction of its credit on its
own lines. Under a near-uniform marked source-valid law, heavy free and captive
centres are paid unless foreign insertion shadow, marked source structure, or
the distinguished endpoint host fails.

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

Rank-two binary support is automatically lower order under adaptive thinning.

## Updated fixed-cell fan endpoint

For a fixed centre cell with residual size `n=q-1`, credit `C_a`, and reserved
slack `tau`, put

```text
theta=tau C_a/(2n).
```

Delete only partner cells of multiplicity above `theta`. Every residual perfect
matching then spends at most `tau C_a/2` on all remaining fan incidences. If the
heavy deletion kills matching in a superregular host, robust Hall forces one
secondary resource incident with `Omega(n)` heavy partners.

Candidate sets are disjoint across partners in one complete-grid row or
column. The heavy pencil therefore carries a credit-scale bank of distinct
candidate incidences, and dyadic pigeonholing gives a factor-two comparable
subbank after only a logarithmic loss.

## Revised open paid objects

The selected witness incidences of source-star, hard-unary, transition, and
binary resource banks are no longer part of their own insertion collateral.
Diffuse foreign insertion support is also absorbed, and self-recapture of one
heavy source-star centre is amortized. Unstructured fixed-cell multiplicity is
replaced by a uniform heavy pencil.

The remaining paid objects are:

1. positive-density ambient unary insertion-shadow stars whose witness graph
   gives a resource-bank rather than a single heavy centre;
2. positive-density ambient rank-three or rank-four binary stars;
3. uniform heavy fixed-cell partner pencils and their candidate banks;
4. fixed-centre arc/path-petal cost;
5. conditional-Hall and alternating-host residual structure;
6. marked source preparation or endpoint-host failure;
7. foreign insertion multiplicity already comparable with removal credit.

Rich designated recapture fibres, selected-credit self-recreation, diffuse
foreign support cores, source-star self-recapture, and unstructured fixed-cell
candidate multiplicity are no longer independent frontiers.

The no-three-in-line conjecture remains unproved.
