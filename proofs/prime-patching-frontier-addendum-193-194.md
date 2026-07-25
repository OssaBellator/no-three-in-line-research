# Prime-patching frontier addendum: credited-bank recapture closure

This addendum extends `proofs/prime-patching-recent-index.md` after PP3afm.
It records the paid resource-bank reductions in `docs/193` and `docs/194`
without replacing the larger historical ledger.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3afn--PP3aft | Ambient random thinning makes all selected credit-line self-recapture identically zero while preserving a source-regular paid subbank | PROVED / CONDITIONAL PAID INTERFACE | `docs/193-credited-line-self-recapture-thinning.md` |
| PP3afu--PP3afz | A recapture-free credited resource bank either has a zero-insertion paid permutation or a purely foreign quadratic unary/cubic binary support core | PROVED | `docs/194-recapture-free-resource-bank-endpoint.md` |

## Updated resource-bank endpoint

Let the ambient credited endpoint bank have size

```text
Q=m^(21/40+o(1))
```

and thin to

```text
q=m^(kappa+o(1)),
0<kappa<1/40.
```

Each chosen credit line has a matching trace on the tied endpoint rectangle.
An off-diagonal recreation of one selected credit requires three prescribed
endpoint indices, so the expected number surviving the thinning is

```text
O(q^3/Q)=o(1).
```

A source-regular subbank can therefore be chosen with no off-diagonal cell on
any selected credit line. Every derangement destroys all selected witness
incidences and recreates none of them.

After this recapture-free thinning, the zero-cost permutation local lemma has
no designated-recapture term. It gives a strict `Xi` decrease unless a linear
set of endpoint indices carries:

```text
Omega(q)
```

foreign unary support degree, or

```text
Omega(q^2)
```

foreign binary support degree.

These yield respectively a quadratic foreign unary core or a cubic foreign
binary core. They return to the existing source-star/resource-bank,
fixed-cell-fan, conditional-Hall, or alternating-host chains.

## Revised open paid objects

The selected witness incidences of source-star, hard-unary, transition, and
binary resource banks are no longer part of their own insertion collateral.
The remaining paid objects are:

1. foreign unary insertion-shadow cores;
2. foreign binary insertion-shadow cores;
3. fixed-centre arc/path-petal cost;
4. conditional-Hall and alternating-host residual structure;
5. source preparation or endpoint-host failure;
6. local insertion multiplicity already comparable with removal credit.

Rich designated recapture fibres are no longer an independent frontier.

The no-three-in-line conjecture remains unproved.
