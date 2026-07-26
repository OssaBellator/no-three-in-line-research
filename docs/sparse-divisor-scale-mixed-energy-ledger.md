# Mixed energy curvature on one repaired divisor scale

**Branch:** `research/sparse-algebraic-spread`

SAS5bi--SAS5bm isolate one exact singleton divisor scale `F_(z,g)`.  In the safe-donor
branch, the original swap `omega={x,y}` composed with one donor transposition
`tau={z,r}` repairs every record in that scale.  The missing energy comparison is not
an ordinary sum of the two single-swap increments: records meeting both endpoint
pairs contribute a mixed second difference.

This note gives the exact four-colouring ledger.  Every selected scale record has
mixed contribution `+1`.  At a swap-local minimum, either that positive scale weight
survives as a quantified energy barrier or a comparable amount of negative mixed
collateral is forced into one of four exact endpoint-pair fibres.

## Weighted indicator energy

Let `Q` be the complete finite multiset of geometric constraint records.  Equivalent
multiplicities may be grouped into nonnegative weights `w_Q`.  For a colouring
`kappa`, write

`I_Q(kappa) in {0,1}`

and

`T(kappa)=sum_Q w_Q*I_Q(kappa)`.

Fix disjoint transpositions `omega={x,y}` and `tau={z,r}`.  For one record define its
mixed swap curvature

`partial_(omega,tau) I_Q
 = I_Q(kappa^(omega union tau))-I_Q(kappa^omega)
   -I_Q(kappa^tau)+I_Q(kappa)`.

It belongs to `{-2,-1,0,1,2}`.

Write

`Delta_omega=T(kappa^omega)-T(kappa)`,

`Delta_tau=T(kappa^tau)-T(kappa)`,

and

`Delta_comb=T(kappa^(omega union tau))-T(kappa)`.

## SAS5bn -- exact mixed-second-difference identity -- PROVED

One has

`Delta_comb=Delta_omega+Delta_tau+sum_Q w_Q*partial_(omega,tau)I_Q`.

Moreover `partial_(omega,tau)I_Q=0` whenever the scope of `Q` misses all endpoints of
`omega` or misses all endpoints of `tau`.

### Proof

Add and subtract `I_Q(kappa^omega)` and `I_Q(kappa^tau)` in the four-state indicator
difference, then sum with weights.  If a scope misses one transposition, applying that
transposition leaves the indicator unchanged in both relevant states, so the mixed
difference is zero. QED.

Thus every nonzero mixed term is supported on a constraint meeting both endpoint
pairs.

## SAS5bo -- every repaired scale record has mixed curvature `+1` -- PROVED WITH ORIGINAL-SWAP COMPOSITION

Let `F_(z,g)` be a safe-donor divisor scale from SAS5bk and let

`L_g=sum_(Q in F_(z,g))w_Q`.

For every selected record `Q` the four indicators are

`I_Q(kappa)=0`,

`I_Q(kappa^omega)=0`,

`I_Q(kappa^tau)=0`,

`I_Q(kappa^(omega union tau))=1`.

Hence

`partial_(omega,tau)I_Q=1`,

and the selected scale contributes exactly `L_g` to the mixed-curvature sum.

### Proof

Originally the mirror record has the unswapped original-column defect and the wrong
label at `z`.  The original swap alone fixes the original-column literal but leaves
`z` wrong.  The donor alone fixes `z` but leaves the original columns unswapped.  The
composed move fixes both, by SAS5bk.  Substitute the four zero-one values. QED.

This is the precise energy meaning of original-swap composition.

## Negative mixed collateral

Remove the selected scale records from the remaining constraint multiset and define

`C_minus=sum_(Q notin F_(z,g)) w_Q*(-partial I_Q)_+`,

`C_plus=sum_(Q notin F_(z,g)) w_Q*(partial I_Q)_+`.

Then `C_minus,C_plus>=0` and SAS5bn--SAS5bo give the exact identity

`Delta_comb=Delta_omega+Delta_tau+L_g+C_plus-C_minus`.

## SAS5bp -- local-minimum scale barrier or negative mixed collateral -- PROVED

Assume the original colouring is swap-local-minimal, so

`Delta_omega>=0` and `Delta_tau>=0`.

For every real `eta` with `0<eta<1`, one of the following holds:

1. `C_minus>=eta*L_g`;
2. `Delta_comb>(1-eta)*L_g`.

In particular, with `eta=1/2`, either negative mixed collateral has total weight at
least `L_g/2`, or the composed move increases the energy by more than `L_g/2`.

Any energy-improving composed move necessarily satisfies the stronger inequality

`C_minus>L_g+Delta_omega+Delta_tau+C_plus>=L_g`.

### Proof

Use the exact identity.  If `C_minus<eta L_g`, discard the nonnegative single-swap
increments and `C_plus` to obtain

`Delta_comb>L_g-eta L_g`.

If `Delta_comb<0`, rearrangement of the same identity gives the final strict bound.
QED.

Thus an improving composed move is possible only through a mixed interaction large
enough to cancel the entire designated scale contribution.

## SAS5bq -- four endpoint-pair fibres localize negative curvature -- PROVED

Every record with negative mixed curvature meets at least one endpoint of `omega` and
at least one endpoint of `tau`.  Assign it canonically to the least endpoint pair

`(a,b) in {x,y} x {z,r}`

contained in its scope.  There are four such fibres.  One fibre carries negative
mixed-curvature weight at least

`C_minus/4`.

Consequently, in the first branch of SAS5bp, one exact endpoint-pair fibre carries at
least

`eta*L_g/4`

negative mixed curvature.  If the composed move improves, one endpoint-pair fibre
carries more than `L_g/4`.

### Proof

SAS5bn gives the support condition.  The fixed endpoint order assigns every negative
record to one of four pairs, and the assigned negative-curvature weights sum to
`C_minus`.  Weighted pigeonhole proves the bounds. QED.

The output is an exact cross-interaction certificate, not a claim that its records are
currently paid or mutually compatible.

## SAS5br -- divisor-scale energy continuation -- PROVED

For the heavy divisor scale supplied by SAS5bm, the safe-donor branch has one exact
continuation at every `eta in (0,1)`:

1. the composed original-plus-donor move increases energy by more than
   `(1-eta)L_g`;
2. or one exact original-endpoint/donor-endpoint pair supports negative mixed
   curvature at least `eta L_g/4`.

In particular, any improving composed move returns the second alternative with more
than `L_g/4` negative mixed curvature in one exact endpoint-pair fibre.

The saturated branch of SAS5bm remains the coprime congruence progression.  Thus the
complete exact-scale router is now:

- whole-scale repair with a quantified energy barrier;
- one concentrated mixed-curvature cross fibre;
- or donor saturation in one coprime progression.

## Corrected SAS6 frontier

The composed-move energy comparison is no longer an unexpanded black box.  The
remaining work is to classify the exact negative mixed-curvature endpoint-pair fibre,
use the coprime progression in the saturated branch, and handle high-incidence and
board-boundary profiles.  A scale repair by itself is not asserted to improve the
energy.

## Finite check

`scripts/verify_sparse_divisor_scale_mixed_energy.py` exhausts all four-state indicator
patterns for two disjoint swaps and random weighted record systems.  It checks the
mixed-difference identity, the selected-record `+1` pattern, the local-minimum
barrier/cancellation inequalities, the four-fibre localization and the necessary
condition for a composed improvement.