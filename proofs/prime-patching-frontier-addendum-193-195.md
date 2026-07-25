# Prime-patching frontier addendum: credited-bank and domain-support closure

This addendum extends `proofs/prime-patching-recent-index.md` after PP3afm.
It records the paid resource-bank, fixed-cell, direct allocation-domain,
composite source-star, final-state path, and adaptive cascade reductions in
`docs/193` through `docs/205` without replacing the larger historical ledger.
The filename is retained for continuity with earlier references.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3afn--PP3aft | Ambient random thinning makes all selected credit-line self-recapture identically zero while preserving a source-regular paid subbank | PROVED / CONDITIONAL PAID INTERFACE | `docs/193-credited-line-self-recapture-thinning.md` |
| PP3afu--PP3afz | A recapture-free credited resource bank either has a zero-insertion paid permutation or a purely foreign quadratic unary/cubic binary support core | PROVED | `docs/194-recapture-free-resource-bank-endpoint.md` |
| PP3aga--PP3agg | Adaptive ambient thinning absorbs every vanishing foreign support density; persistent failure is a positive-density ambient unary/rank-three/rank-four resource star | PROVED | `docs/195-adaptive-ambient-foreign-support-thinning.md` |
| PP3agh--PP3agn | A marked source-star centre recreates only an `O(q/Q)` fraction of its own credit; failure is foreign support, marked source structure, or endpoint-host failure | PROVED / CONDITIONAL MARKED PAID INTERFACE | `docs/196-marked-source-star-credit-amortization.md` |
| PP3ago--PP3agt | Thresholding a fixed-cell candidate fan pays all light partners; failure yields a uniform heavy partner pencil, conditional Hall structure, or foreign paid/source concentration | PROVED / CONDITIONAL PAID INTERFACE | `docs/197-thresholded-fixed-cell-fan-payment.md` |
| PP3agu--PP3agz | A fixed-cell fan removes at most `n` controller entries per label and at most `2n` values from one paired macro domain; robust allocation margin bypasses arbitrary fan multiplicity | PROVED / CONDITIONAL DIRECT-COMPLETION INTERFACE | `docs/198-fixed-cell-fan-allocation-domain-bypass.md` |
| PP3aha--PP3ahg | Every binary shadow of an `s`-cell source-valid endpoint state is supported on `binom(s,2)` line matchings and costs at most `s(s-1)` values from one macro domain | PROVED / CONDITIONAL DIRECT-COMPLETION INTERFACE | `docs/199-small-endpoint-binary-shadow-allocation-bypass.md` |
| PP3ahh--PP3ahn | Unary witness multiplicity is one for a fixed inserted cell and candidate; `o(R)` unary weight is domain-absorbed, while failed arc-petal completion forces `A_2=Omega(RW)` | PROVED / CONDITIONAL DIRECT-COMPLETION INTERFACE | `docs/200-unary-shadow-domain-margin-threshold.md` |
| PP3aho--PP3ahu | Unary domain failure creates a post-trade source star of degree `Omega(R/s)`; a second marked trade cancels the created incidences exactly in a composite potential identity | PROVED / CONDITIONAL COMPOSITE PAID INTERFACE | `docs/201-unary-domain-failure-composite-source-star.md` |
| PP3ahv--PP3aia | In a two-step source-valid path, final controller domains depend only on surviving final new points; transient shadow disappears and direct allocation uses only final unary support plus `s_f(s_f-1)` | PROVED / CONDITIONAL DIRECT-COMPLETION INTERFACE | `docs/202-two-step-final-state-shadow-path-independence.md` |
| PP3aib--PP3aig | Along any bounded-depth source-valid path, only the final new set matters; binary loss is controlled by cumulative surviving size squared and unary failure yields the next final source star | PROVED / CONDITIONAL CASCADE INTERFACE | `docs/203-bounded-depth-final-shadow-cascade.md` |
| PP3aih--PP3ain | Every planned cascade of depth `d=o(W)` admits marked subbank sizes with cumulative final size `o(W)`; failed final unary margin still yields an `omega(W)` source star | PROVED / CONDITIONAL DIRECT-CASCADE INTERFACE | `docs/204-adaptive-sub-square-root-cascade-sizing.md` |
| PP3aio--PP3air | The explicit choice `q=floor(sqrt(W/d))` gives both `dq=o(W)` and the exact joint trace budget `dq^3/R=o(1)`; all planned selected-credit traces can be cleaned sequentially | PROVED / CONDITIONAL UNIFORM MARKED-HOST INTERFACE | `docs/205-exact-joint-cascade-trace-budget.md` |

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

Adaptive thinning absorbs every vanishing ambient support degree. Persistent
failure of the monotone paid route therefore gives an ambient unary,
rank-three, or rank-four fixed-resource star.

## Fixed-cell paid and allocation endpoints

For a fixed centre cell with residual size `n=q-1`, credit `C_a`, and reserved
slack `tau`, put

```text
theta=tau C_a/(2n).
```

Deleting partners above `theta` pays every remaining light fan inside half the
reserved credit. If heavy deletion kills matching in a superregular host,
robust Hall forces a linear uniformly heavy partner pencil and a credit-scale
bank of distinct candidate incidences.

There is now a separate direct-completion route. Every centre--partner secant
line is a matching between controller edges and movement labels, and another
matching between controller edges and refill labels. A residual matching of
size `n` therefore removes at most `n` entries at one controller or label and
at most `2n` values from one refined domain. If the nonfan domains have margin
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

nonaxis inserted-pair secants. All rank-two through rank-four binary `Xi`
entries are supported on the corresponding line matchings. Hence

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

so `s^2=o(R)`. Any fixed positive nonbinary domain margin absorbs the complete
binary insertion shadow. This is a direct final-allocation theorem, not a
claim that the trade decreases the integer `Xi` potential.

## Unary domain threshold and petal consequence

For one fixed inserted cell and one controller candidate entry, source validity
permits at most one retained-source witness. Thus the unary `Xi` contribution
of a forced arc cell is simple candidate-entry support.

For a source-valid state `P` of size `s`, a sufficient direct-allocation
criterion is

```text
U_Xi(P)+s(s-1) <= xi R,
```

or the sharper per-label degree form in PP3ahj. Therefore every unary state cost
`o(R)` is absorbed together with all binary shadow.

For a comparable fixed-axis arc-petal bank `B`, assume the nonarc unary cost and
the binary line-support term each use at most `xi R/4`. Then either one petal has

```text
a(e)<=xi R/2
```

and completes directly, or every petal is domain-heavy and

```text
A_2 >= sum_{e in B}a(e) > (xi/2)R|B|.
```

At target size `|B|=W`, failed direct completion therefore forces

```text
A_2=Omega(RW).
```

Rank-three path-petal, rank-four partner, and choice-grid local costs are binary
and are already absorbed by the complete binary-shadow bypass in the robust
margin branch.

## Composite cancellation of unary domain failure

Suppose an `s`-cell source-valid trade starts from domains of size at least
`(gamma+xi)R` and unary insertion shadow pushes one paired macro domain below
`gamma R`. Assign each removed value to a causing inserted cell and to movement
or refill type. One class has size

```text
C > xi R/(2s).
```

In the post-trade source, the causing inserted cell is a common blocker endpoint
in those `C` distinct entries, with distinct retained partners. It is therefore
a genuine source-star centre carrying `C` units of dynamic credit.

Let the first trade have removal credit `R_1` and other insertion cost `J_1`.
Let a second marked trade move the new centre, with selected-line self-recapture
`I_self` and foreign cost `J_2`. The exact two-step identity is

```text
Xi(S_2)-Xi(S_0)
<=
J_1+I_self+J_2-R_1.
```

The `C` incidences created in the first state and destroyed in the second cancel
exactly. If `R_1->infinity`, `C<=R`, and the post-trade marked layer has size
`Omega(R)`, the second subbank may be chosen slowly enough that

```text
E I_self=o(R_1).
```

Thus diffuse first-step and second-step foreign cost gives a strict composite
improvement. Domain-scale unary failure is a second-generation marked
source-star, not a new terminal weight table.

## Final-state path independence

For robust direct allocation there is a stronger alternative to paying the
uncancelled intermediate terms. After a source-valid trade path, write

```text
S_t=O_t dot-union N_t,
S=|N_t|,
```

where `O_t` is the final retained original source and `N_t` is the set of points
that survive as genuinely new final points. Every final blocker pair not already
contained in `O_t` is either `N_t--O_t` or `N_t--N_t`. Points inserted and later
removed belong to neither class.

Consequently every transient candidate entry disappears from the final domains,
regardless of its intermediate `Xi` multiplicity. The complete final shadow
removes at most

```text
d_M^t(i,A)+d_F^t(i,B)+S(S-1)
```

values from one macro domain. A sufficient label-free bound is

```text
U_t+S(S-1).
```

If this fits a fixed margin `xi R`, direct allocation completes without any
potential decrease or growing removal credit along the path. If final unary
support destroys one margin, some point in `N_t` is a final source-star centre
of degree greater than

```text
xi R/(2S).
```

For a depth-`t` path with at most `s_j` points inserted at step `j`, all final
binary shadow is negligible whenever

```text
(sum_j s_j)^2=o(R).
```

At the slab scale this permits total surviving size
`m^(kappa_*+o(1))` for every `kappa_*<19/40`, including polynomially growing
cascade depth when the individual trades are sufficiently small.

## Adaptive sub-square-root cascade budget

Put

```text
W=sqrt(R)=m^(19/40+o(1)).
```

For every planned depth `d=o(W)`, choose

```text
q=floor(sqrt(W/d)).
```

Then the exact estimates are

```text
dq/W <= sqrt(d/W)=o(1)
```

and

```text
dq^3/R <= 1/sqrt(Wd)=o(1).
```

Thus a `d`-generation marked cascade has cumulative surviving size at most
`dq=o(W)`, final binary domain loss `o(R)`, and a summable selected-credit trace
failure budget. If final unary shadow still destroys one margin, the resulting
source-star degree is

```text
Omega(R/(dq))=omega(W).
```

Therefore every failed final unary endpoint still supplies more than target
width. Under uniform marked-host preparation, the trace and support-cleaning
events may be imposed sequentially along the entire planned cascade without
independence.

## Revised open objects

The frontier now separates the monotone paid route, robust direct allocation,
two-step composite conversion, bounded-depth final-state cascades, and adaptive
sub-square-root cascade sizing.

In the robust-domain direct-completion branch, positive-density rank-three and
rank-four binary stars, fixed-cell heavy pencils, weighted choice grids,
candidate-rich projective covers, arbitrary binary `Xi` multiplicity,
intermediate foreign shadow, intermediate lack of credit, cumulative binary
support below depth `o(W)`, and `o(R)` final unary weight are no longer
independent obstructions.

Unary shadow that destroys a final robust margin is localized to a final
source-star centre of degree `omega(W)` throughout every planned `o(W)`-depth
cascade.

The remaining concentrated problems are:

1. failure to select a uniformly prepared controller-preserving source-valid
   path because of marked source, transition, anchor, conditional-Hall,
   alternating-host, or distinguished endpoint-host structure;
2. failure of the nonshadow `Omega(R)` base-domain margin or of the global
   allocation criterion;
3. proving termination, or otherwise bounding the number of source-star
   generations by `o(W)`;
4. branches that still require a one-step monotone `Xi` decrease because no
   robust final allocation is available;
5. genuinely final unary support whose star centre cannot be moved through the
   prepared marked infrastructure;
6. cascade depth at or beyond the target-width scale, where the explicit
   cumulative-size argument no longer gives `S=o(W)`.

Rich designated recapture fibres, selected-credit self-recreation, diffuse
foreign support cores, source-star self-recapture, unstructured fixed-cell
candidate multiplicity, binary multiplicity on small source-valid endpoint
states, credit-scale path-petal binary cost, raw unary domain failure,
intermediate foreign multiplicity, intermediate lack of credit, and
sub-target-depth cumulative binary growth are no longer separate frontiers.

The no-three-in-line conjecture remains unproved.
