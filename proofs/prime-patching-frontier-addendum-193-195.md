# Prime-patching frontier addendum: credited-bank and domain-support closure

This addendum extends `proofs/prime-patching-recent-index.md` after PP3afm.
It records the paid resource-bank, fixed-cell, and direct allocation-domain
reductions in `docs/193` through `docs/199` without replacing the larger
historical ledger.  The filename is retained for continuity with earlier
references.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3afn--PP3aft | Ambient random thinning makes all selected credit-line self-recapture identically zero while preserving a source-regular paid subbank | PROVED / CONDITIONAL PAID INTERFACE | `docs/193-credited-line-self-recapture-thinning.md` |
| PP3afu--PP3afz | A recapture-free credited resource bank either has a zero-insertion paid permutation or a purely foreign quadratic unary/cubic binary support core | PROVED | `docs/194-recapture-free-resource-bank-endpoint.md` |
| PP3aga--PP3agg | Adaptive ambient thinning absorbs every vanishing foreign support density; persistent failure is a positive-density ambient unary/rank-three/rank-four resource star | PROVED | `docs/195-adaptive-ambient-foreign-support-thinning.md` |
| PP3agh--PP3agn | A marked source-star centre recreates only an `O(q/Q)` fraction of its own credit; failure is foreign support, marked source structure, or endpoint-host failure | PROVED / CONDITIONAL MARKED PAID INTERFACE | `docs/196-marked-source-star-credit-amortization.md` |
| PP3ago--PP3agt | Thresholding a fixed-cell candidate fan pays all light partners; failure yields a uniform heavy partner pencil, conditional Hall structure, or foreign paid/source concentration | PROVED / CONDITIONAL PAID INTERFACE | `docs/197-thresholded-fixed-cell-fan-payment.md` |
| PP3agu--PP3agz | A fixed-cell fan removes at most `n` controller entries per label and at most `2n` values from one paired macro domain; robust allocation margin bypasses arbitrary fan multiplicity | PROVED / CONDITIONAL DIRECT-COMPLETION INTERFACE | `docs/198-fixed-cell-fan-allocation-domain-bypass.md` |
| PP3aha--PP3ahg | Every binary shadow of an `s`-cell source-valid endpoint state is supported on `binom(s,2)` line matchings and costs at most `s(s-1)` values from one macro domain | PROVED / CONDITIONAL DIRECT-COMPLETION INTERFACE | `docs/199-small-endpoint-binary-shadow-allocation-bypass.md` |

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

Adaptive thinning absorbs every vanishing ambient support degree.  Persistent
failure of the monotone paid route therefore gives an ambient unary,
rank-three, or rank-four fixed-resource star.

## Fixed-cell paid and allocation endpoints

For a fixed centre cell with residual size `n=q-1`, credit `C_a`, and reserved
slack `tau`, put

```text
theta=tau C_a/(2n).
```

Deleting partners above `theta` pays every remaining light fan inside half the
reserved credit.  If heavy deletion kills matching in a superregular host,
robust Hall forces a linear uniformly heavy partner pencil and a credit-scale
bank of distinct candidate incidences.

There is now a separate direct-completion route.  Every centre--partner secant
line is a matching between controller edges and movement labels, and another
matching between controller edges and refill labels.  A residual matching of
size `n` therefore removes at most `n` entries at one controller or label and
at most `2n` values from one refined domain.  If the nonfan domains have margin
`xi R` and

```text
2n<=xi R,
```

the global controller-aware allocation graphs survive regardless of candidate
multiplicity.

## Complete binary-shadow domain bypass

A source-valid endpoint state with `s` inserted cells has exactly

```text
binom(s,2)
```

nonaxis inserted-pair secants.  All rank-two through rank-four binary `Xi`
entries are supported on the corresponding line matchings.  Hence

```text
Delta(binary candidate support) <= binom(s,2)
```

on the controller-edge and label sides, and one macro domain loses at most

```text
2 binom(s,2)=s(s-1)
```

values.

At the active scales,

```text
R=m^(19/20+o(1)),
s=m^(kappa+o(1)),
kappa<19/40,
```

so `s^2=o(R)`.  Any fixed positive nonbinary domain margin absorbs the complete
binary insertion shadow.  This is a direct final-allocation theorem, not a
claim that the trade decreases the integer `Xi` potential.

## Revised open objects

The frontier now separates the monotone paid route from the robust direct
allocation route.

In the robust-domain direct-completion branch, positive-density rank-three and
rank-four binary stars, fixed-cell heavy pencils, weighted choice grids,
candidate-rich projective covers, and arbitrary binary `Xi` multiplicity of one
active endpoint state are no longer independent obstructions.

The remaining concentrated problems are:

1. positive-density ambient unary insertion shadow whose witness structure gives
   a resource bank rather than one marked source centre;
2. fixed-centre unary arc/path-petal cost and other unary insertion shadow using
   retained source points;
3. failure of the nonbinary `Omega(R)` domain margin or of the global allocation
   criterion;
4. marked source, transition, anchor, or endpoint-host failure;
5. conditional-Hall or alternating-host structure before a source-valid trade is
   selected;
6. branches that still require a monotone `Xi` decrease because no direct final
   allocation is available;
7. endpoint states too large for `s^2=o(R)`.

Rich designated recapture fibres, selected-credit self-recreation, diffuse
foreign support cores, source-star self-recapture, unstructured fixed-cell
candidate multiplicity, and binary multiplicity on small source-valid endpoint
states are no longer separate frontiers.

The no-three-in-line conjecture remains unproved.
