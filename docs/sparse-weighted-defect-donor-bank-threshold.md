# Weighted construction of scale-mass donor banks

**Branch:** `research/sparse-algebraic-spread`

SAS5cm--SAS5cq give an aggregate energy theorem for any endpoint-disjoint donor bank once
the selected `+1` repair mass `L_bank` is known.  The remaining construction issue is
weighted: a diffuse reflected-label defect family may have many defect columns, but one must
retain enough exact record weight after choosing one record per column and matching distinct
donors.

This note gives that construction under one explicit exact-record stock bound.  It produces
an endpoint-disjoint bank with a quantitative `L_bank`, and under the existing global
column-incidence hypothesis it also produces a simultaneously compatible subbank.  The
result feeds directly into the aggregate two-reuse threshold.

## Weighted defect-column data

Fix one original swap `omega={x,y}`, one reflected mirror word, one failing non-swapped role
and one required label `ell`.  Let `Z` be a finite nonempty set of distinct defect columns.
Column `z` carries total aggregated exact-record weight `L(z)>0`, and put

`W_Z=sum_(z in Z)L(z)`,

`k=|Z|`.

Assume that for every `z`, after exact aliases are merged, the fibre at `z` contains at most
`K_rec` exact geometric-label record signatures.  Let `D_ell` be the donor-label class,
`d=|D_ell|`, and assume every chosen exact record excludes at most three donor columns as in
SAS5ag.

For one exact record `Q_z` and one locally safe donor `q`, the transposition
`tau_z={z,q}` has the four-state pattern

`I_Q(kappa)=I_Q(kappa^omega)=I_Q(kappa^tau)=0`,

`I_Q(kappa^(omega union tau))=1`.

Thus its selected exact record weight is a valid `+1` mass for the donor-bank energy ledger.

## SAS5cr -- one exact designated record per defect column -- PROVED

For every `z in Z`, choose a heaviest exact record signature `Q_z` in its fibre and let its
weight be `a_z`.  Then

`a_z>=L(z)/K_rec`

and

`sum_z a_z>=W_Z/K_rec`.

### Proof

At most `K_rec` nonnegative exact-signature weights sum to `L(z)`, so their maximum is at
least the average.  Sum over `z`. QED.

The chosen records are distinct because their fixed failing role contains distinct defect
columns.

## SAS5cs -- weighted endpoint-disjoint donor matching -- PROVED

Put

`m=min(k,(d-3)_+)`.

If `m>0`, there is a family of `m` endpoint-disjoint locally safe donor transpositions,
using `m` distinct defect columns and `m` distinct donor columns, whose selected exact-record
weight satisfies

`L_match>= (m/k)*W_Z/K_rec`.

### Proof

Order the defect columns by nonincreasing `a_z` and retain the first `m`.  Their total weight
is at least `m/k` times `sum_z a_z`, hence at least the displayed amount by SAS5cr.

Match the retained records greedily to unused donor columns.  Before the `j`-th choice,
`j<m<=d-3` donors have been used and the current record excludes at most three donors.
Therefore at least `d-j-3>=1` donors remain.  Defect columns lie outside `D_ell`, so all
transposition endpoints are distinct. QED.

This is the weighted strengthening of the cardinality matching in SAS5ag.

## SAS5ct -- compatible weighted subbank under bounded column incidence -- PROVED

Assume every board column belongs to at most `Lambda` exact constraint scopes.  The matched
donor interaction graph has maximum degree at most `4Lambda`.  It therefore contains an
independent donor subbank with selected record weight

`L_comp>=L_match/(4Lambda+1)`

and hence

`L_comp>= m*W_Z/[k*K_rec*(4Lambda+1)]`.

Applying `omega` together with this independent subbank repairs all of its selected exact
records simultaneously.

### Proof

SAS5aj gives the degree bound and a proper colouring with at most `4Lambda+1` colours.
The colour-class weights sum to `L_match`, so one independent class has at least the average
weight.  SAS5aq preserves every designated repair in that independent class. QED.

The endpoint-disjoint matched bank is sufficient for the family of individual two-swap
experiments in SAS5cm.  The smaller compatible subbank is available when simultaneous
installation is required.

## SAS5cu -- designated records feed the aggregate mixed-energy identity -- PROVED

For every matched donor `tau_z`, set

`L_tau=a_z`.

Then the exact one-donor identity and the summed donor-bank identity SAS5cm remain valid with
these designated masses, and

`L_bank=sum_tau L_tau=L_match`.

### Proof

The proofs of SAS5bo and SAS5cm use only that each selected record has the four-state
indicator pattern `(0,0,0,1)` and that selected records assigned to different donors are
exact physical records with their aggregate weights.  The designated `Q_z` records have
that pattern by the reflected-label composition contract, and distinct defect columns make
them distinct.  Therefore each contributes exactly `+a_z` to its donor's mixed-curvature
ledger and summing gives `L_match`. QED.

No divisor-scale hypothesis is needed for this designated-record version.

## SAS5cv -- explicit scale-dominance/collateral threshold -- PROVED

Let `Omega_cross` be the aggregate physical weight of exact records meeting the original
swap and at least one donor endpoint, as in SAS5ck.  For the matched bank define the lower
bound

`L_0=m*W_Z/(k*K_rec)`.

Then one of the following holds:

1. **constructed scale-dominant bank:** `L_0>2Omega_cross`; one matched donor has a positive
   composed-move barrier at least

   `(L_0-2Omega_cross)/m`;
2. **constructed collateral-dominant bank:** `L_0<=2Omega_cross`; hence

   `Omega_cross>=L_0/2`;
3. for the improving donors in the matched bank,

   `sum_(tau improving)(L_tau+|Delta_comb(tau)|)<=2Omega_cross`.

If the relevant cross family contains at most `K_cross` exact physical signatures, the
collateral-dominant branch has one exact signature of weight at least

`L_0/(2K_cross)`.

Under the column-incidence cap, the same statements apply to the compatible subbank after
replacing `L_0` by

`L_0/(4Lambda+1)`.

### Proof

SAS5cs and SAS5cu give an actual endpoint-disjoint bank with
`L_bank>=L_0`.  If `L_0>2Omega_cross`, then `L_bank>2Omega_cross`, so SAS5cp gives a donor
with positive barrier at least `(L_bank-2Omega_cross)/m`, which is at least the displayed
quantity.  Otherwise the second inequality is immediate.  The improving-move budget is
SAS5co.  Weighted pigeonhole gives the exact-signature localization.  Apply SAS5ct for the
compatible version. QED.

## Corrected SAS6 frontier

Diffuse reflected-label weight now supplies an explicit donor-bank mass after only two
declared losses: the exact-record stock `K_rec` and, when simultaneous installation is
needed, the interaction-colouring factor `4Lambda+1`.  The aggregate energy router can
therefore be triggered by the concrete inequality

`m*W_Z/(k*K_rec)>2Omega_cross`.

The remaining sparse work is to prove useful exact-record stock bounds in the heaviest
geometric regimes, exploit the heavy cross signature in the complementary branch, and
continue the coprime donor-saturated progression, high-incidence and board-boundary
analyses.

## Finite check

`scripts/verify_sparse_weighted_defect_donor_bank.py` exhausts small weighted defect fibres,
donor exclusions and interaction graphs and samples larger systems.  It checks heaviest
record extraction, top-weight donor matching, weighted compatibility colouring, the
`+1` designated pattern and the final scale/collateral threshold.