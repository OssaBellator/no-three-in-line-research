# Physical installation of aggregate negative mixed collateral

**Branch:** `research/sparse-algebraic-spread`

SAS5fw--SAS5ga remove the final-output stock loss and return an aggregate exact negative
mixed-curvature bank when the high matched-square barrier is not paid by neutral repairs or by the
square barrier itself. The bank is still an energy-ledger object. This note makes it physical.

Every negative conjunction record has exactly one single-swap-only orientation. For each independent
square, choose the constituent swap which creates the heavier orientation. Under a mixed-orientation
creator-stage contract, all chosen creators execute simultaneously, installing at least half of the
aggregate negative bank as genuinely current exact records. A second density split gives a large
low-cost installation or a quantified aggregate first-stage barrier.

## Negative square-bank model

Fix the interaction-independent high square bank `J_high` from SAS5fw--SAS5ga. For square `a`, with
base-admissible disjoint swaps `sigma_a,tau_a`, partition its exact negative mixed-curvature weight as

- `C_(a,sigma)^-`: records with table `(0,1,0,0)`;
- `C_(a,tau)^-`: records with table `(0,0,1,0)`.

Put

`C_a^-=C_(a,sigma)^-+C_(a,tau)^-`

and

`C_J^-=sum_(a in J_high)C_a^-`.

Assume the **mixed-orientation creator-stage contract**:

1. both constituent swaps of every square are individually legal from the common base colouring;
2. for every interaction-independent square family and every choice of one constituent swap per
   square, the chosen swaps are jointly legal when executed simultaneously from the base state;
3. after the chosen creator of one square, its unchosen constituent is legal and destroys every
   selected record in that creator orientation;
4. no complete exact record scope meets two selected square supports;
5. exact aliases are aggregated before orientation and square assignment;
6. every selected negative record retains its square, creating-swap and opposite-destroyer address;
7. failure returns the least base-legality, mixed-stage-legality, opposite-destroyer legality, support,
   scope, alias, record, orientation or boundary field.

## SAS5gb -- exact negative-orientation partition -- PROVED

For every square,

`C_a^-=C_(a,sigma)^-+C_(a,tau)^-`.

Every record in the first bank is absent in the base state, present after `sigma_a` alone and absent
after `sigma_a tau_a`. The symmetric statement holds for the second bank with `tau_a` as creator.

### Proof

SAS5bu classifies negative conjunction tables exactly as `(0,1,0,0)` and `(0,0,1,0)`. Alias
aggregation and the unique square assignment make the two orientation banks disjoint and complete.
The indicator statements are the definitions of the two tables. QED.

## SAS5gc -- heavier creator orientation retains one half -- PROVED

For each square choose

`gamma_a=sigma_a`

when `C_(a,sigma)^->=C_(a,tau)^-`, and choose `gamma_a=tau_a` otherwise. Let `R_a^-` be the selected
orientation weight and put

`R_J^-=sum_a R_a^-`.

Then

`R_a^->=C_a^-/2`

for every square and

`R_J^->=C_J^-/2`.

### Proof

The larger of two nonnegative numbers is at least half their sum. Sum over the high square bank.
QED.

## SAS5gd -- simultaneous physical negative-bank installation -- PROVED UNDER THE CREATOR-STAGE CONTRACT

Execute all chosen creator swaps `gamma_a` simultaneously. Then:

1. the simultaneous operation is legal;
2. every selected negative record is present afterwards;
3. selected exact record banks from distinct squares are disjoint;
4. the physically installed current exact-record weight is exactly `R_J^-`;
5. if `Delta_(gamma_a)` is the base single-swap energy increment, then

   `T(kappa^Gamma)-T(kappa)=sum_a Delta_(gamma_a)`.

At a swap-local minimum this total first-stage cost is nonnegative. Every installed record retains the
opposite constituent swap as an exact legal destruction address after its creator.

### Proof

Item 2 of the creator-stage contract gives simultaneous legality. SAS5gb says that the chosen
constituent creates every record in its selected orientation. Complete-scope independence prevents
any other selected square from changing that record, and alias aggregation gives disjoint exact
banks. Record-by-record summation of the complete ledger gives energy additivity. Swap-local
minimality makes every individually base-admissible increment nonnegative. Item 3 makes the unchosen
constituent a legal opposite destroyer after the creator, and the negative table shows that it removes
the selected records. QED.

This is a physical installation statement, not a claim that the installed conflicts are free.

## SAS5ge -- creator barrier-density router -- PROVED

Fix `kappa_0>0`. Split the selected creator squares into

`J_low^-={a:Delta_(gamma_a)<=kappa_0 R_a^-}`

and its complement `J_high^-`.

Exactly one of the following weighted alternatives holds:

1. the low-cost subbank carries selected negative-record weight at least `R_J^-/2`; its simultaneous
   creator batch installs that exact weight at energy cost at most `kappa_0` times the installed
   weight;
2. the high-cost subbank carries more than `R_J^-/2`, and its aggregate base single-swap barrier is
   greater than

   `kappa_0 R_J^-/2>=kappa_0 C_J^-/4`.

### Proof

The two subbanks partition `R_J^-`. If the low subbank has at least half, sum
`Delta_(gamma_a)<=kappa_0R_a^-` and use SAS5gd on the induced independent family. Otherwise the high
subbank has more than half and every one of its terms satisfies the strict reverse inequality. Sum
and apply SAS5gc. QED.

## SAS5gf -- integrated physical negative-collateral router -- PROVED UNDER THE DECLARED CONTRACTS

Let an original matched bank have weight `M` and square interaction degree `D_sq`. Suppose SAS5ga
returns

`C_J^->(1-theta)lambda M/[4(D_sq+1)]`

for `lambda>0` and `theta in (0,1)`. For every `kappa_0>0`, one has:

1. a jointly legal creator batch physically installs exact current negative-record weight greater than

   `(1-theta)lambda M/[16(D_sq+1)]`

   at energy cost at most `kappa_0` times that installed weight;

2. or an aggregate base single-swap barrier greater than

   `kappa_0(1-theta)lambda M/[16(D_sq+1)]`;

3. or one mixed-orientation creator-stage, opposite-destroyer legality, base-admissibility,
   interaction-independence, complete-ledger, record, alias or boundary field fails.

The installed bank enters the exact current-record and realized repair/opposite-destruction ledgers
with its full selected mass and known legal opposite destroyers.

### Proof

SAS5gc gives

`R_J^->(1-theta)lambda M/[8(D_sq+1)]`.

Apply SAS5ge. Its low branch retains at least half of `R_J^-`, giving alternative 1. Its high branch
has barrier greater than `kappa_0R_J^-/2`, giving alternative 2. Failed hypotheses are alternative 3.
QED.

## Corrected SAS6 frontier

The aggregate negative mixed-curvature branch is no longer only a signed energy term. At every
creator-density scale it gives either a large physically installed current record bank with known
opposite destroyers or a comparably quantified aggregate base single-swap barrier.

The remaining sparse work is paying or recycling the installed negative-record bank, choosing global
`lambda,theta,kappa_0` scales whose barrier alternatives are globally bounded, proving mixed-orientation
creator and opposite-destroyer legality in every arithmetic word family, batching neutral outputs
under failed incidence caps, and the positive-base-row, reflected-boundary and high-incidence branches.

## Finite check

`scripts/verify_sparse_negative_collateral_physical_installation.py` enumerates both negative
conjunction tables and samples interaction-independent weighted square banks. It checks the
squarewise heavier-orientation half bound, simultaneous exact installed mass, creator energy
additivity, the second barrier-density split and the integrated matched-bank constants.
