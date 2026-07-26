# Active exact cross records and two-donor peeling

**Branch:** `research/sparse-algebraic-spread`

SAS5cm--SAS5da construct an endpoint-disjoint donor bank with explicit selected repair mass
and show that negative mixed curvature has physical-record reuse at most two.  In the
collateral-dominant branch, a heavy exact cross record was previously only localized.  This
note makes it active.

Only records which actually have negative curvature with at least one donor can pay the
negative bank.  Their incidence ledger is exact, not merely bounded.  A heavy active record
meets one or two donors, contributes its full aggregate weight to each of them, and admits a
five-way local energy router.  Removing those at most two donors deletes the record entirely
from the residual negative ledger, allowing iterative peeling.

## Active negative-record notation

Fix one original swap `omega` and one endpoint-disjoint donor bank `T`.  Exact record aliases
are already aggregated.  For every exact record `Q` meeting the original swap, put

`I_Q={tau in T: partial_(omega,tau)I_Q=-1}`,

`nu_Q=|I_Q|`.

Call `Q` **active negative** when `nu_Q>0`, and write

`A={Q:nu_Q>0}`,

`Omega_act=sum_(Q in A)Omega_Q`.

By SAS5cj,

`1<=nu_Q<=2`

for every `Q in A`, with `nu_Q<=1` when `Q` contains both original endpoints.

For each donor `tau`, retain the notation `C_minus(tau)`, `C_plus(tau)`, `L_tau`,
`Delta_tau`, `Delta_omega` and `Delta_comb(tau)` from SAS5cm.

## SAS5db -- exact active-incidence identity -- PROVED

The total negative mixed-curvature mass across the bank is exactly

`C_minus_bank=sum_(tau in T)C_minus(tau)=sum_(Q in A)nu_Q*Omega_Q`.

Consequently

`Omega_act<=C_minus_bank<=2*Omega_act`.

### Proof

For conjunction records, negative mixed curvature is either zero or exactly `-1`.  An active
record `Q` contributes `Omega_Q` to precisely the donors in `I_Q`, hence contributes
`nu_Q Omega_Q` after summing over donors.  Summing first over records gives the identity.
The inequalities use `1<=nu_Q<=2`. QED.

This replaces the larger passive stock `Omega_cross` by the exact stock which actually pays
negative curvature.

## SAS5dc -- active-stock aggregate refinement -- PROVED

Under swap-local minimality,

`sum_(tau in T)Delta_comb(tau)>=L_bank-2*Omega_act`.

If every composed move in the bank is nonpositive, then

`Omega_act>=L_bank/2`.

If the active family contains at most `K_act` exact signatures, one active exact record has
weight at least

`L_bank/(2*K_act)`.

### Proof

Repeat SAS5cn with the exact estimate
`C_minus_bank<=2Omega_act` from SAS5db.  If all composed increments are nonpositive, their sum
is nonpositive and the lower bound forces `L_bank<=2Omega_act`.  Weighted pigeonhole over at
most `K_act` active signatures gives the last statement. QED.

A collateral-dominant bank therefore contains a heavy record that really interacts
negatively with the donor bank; inert cross records are excluded.

## SAS5dd -- a heavy active record localizes to at most two donors -- PROVED

Fix an active record `Q_*` of weight `Omega_*`.  Its donor incidence set `I_*` is nonempty and
has size at most two.  For every `tau in I_*`,

`C_minus(tau)>=Omega_*`.

Choose the least donor in `I_*` as the canonical incident donor.

### Proof

The size bound is SAS5cj.  For every incident donor, the exact record has curvature `-1`, so
its aggregate aliases contribute exactly `Omega_*` to that donor's negative-curvature sum.
All other contributions are nonnegative. QED.

Thus a heavy active record cannot diffuse over a long endpoint-disjoint bank.

## SAS5de -- five-way local energy router at a heavy active record -- PROVED

Let `tau_*` be the canonical donor incident with `Q_*`.  Put

`A_*=Delta_omega+Delta_(tau_*)+L_(tau_*)+C_plus(tau_*)`.

The exact one-donor identity gives

`C_minus(tau_*)=A_*-Delta_comb(tau_*)`.

At least one of the following holds:

1. **deep composed improvement:**

   `Delta_comb(tau_*)<=-Omega_*/2`;

2. **large original-swap barrier:** `Delta_omega>Omega_*/8`;
3. **large donor-swap barrier:** `Delta_(tau_*)>Omega_*/8`;
4. **large designated repair mass:** `L_(tau_*)>Omega_*/8`;
5. **large positive mixed curvature:** `C_plus(tau_*)>Omega_*/8`.

If the composed move is nonimproving, the stronger conclusion

`A_*>=Omega_*`

holds.

### Proof

SAS5dd gives `C_minus(tau_*)>=Omega_*`.  If alternative 1 fails, then
`-Delta_comb(tau_*)<Omega_*/2`, and therefore

`A_*=C_minus(tau_*)+Delta_comb(tau_*)>Omega_*/2`.

The four summands of `A_*` are nonnegative under swap-local minimality, so one exceeds
`Omega_*/8`.  If `Delta_comb(tau_*)>=0`, then
`A_*=C_minus+Delta_comb>=Omega_*`. QED.

The heavy record therefore returns an executable deep improvement or one explicit positive
energy component of comparable scale.

## SAS5df -- deleting the incident donors removes the heavy record -- PROVED

Remove the at most two donors in `I_*` and put

`T'=T\I_*`,

`L_res=sum_(tau in T')L_tau`,

`Omega_res=Omega_act-Omega_*`.

Then the residual negative-curvature sum satisfies

`sum_(tau in T')C_minus(tau)<=2*Omega_res`.

Consequently, if

`L_res>2*Omega_res`,

some residual donor has positive composed-move barrier at least

`[L_res-2*Omega_res]/|T'|`.

If `T'` is nonempty and every residual composed move is nonpositive, then

`Omega_res>=L_res/2`.

### Proof

The record `Q_*` has zero mixed curvature with every donor outside `I_*`, so it contributes
nothing to the residual bank.  Every other active record still has residual incidence at most
two.  Sum their weights exactly as in SAS5db to obtain the first inequality, then apply the
aggregate argument of SAS5cp to `T'`. QED.

This is a genuine peeling step: one heavy physical record is removed at the cost of at most
two donors.

## SAS5dg -- heavy-active-record peeling router -- PROVED

Suppose an endpoint-disjoint donor bank is collateral-dominant in the active sense

`L_bank<=2*Omega_act`,

and the active exact-record family has size at most `K_act`.  Then one exact record `Q_*` has

`Omega_*>=L_bank/(2*K_act)`

and yields one of:

1. the five-way local energy output of SAS5de on one of at most two donors;
2. a residual scale-dominant bank after deleting those donors;
3. a residual active-collateral-dominant bank with one fewer active record.

Iterating the third alternative removes at least one active exact signature per step and at
most two donors per step.  Hence after at most `K_act` peel steps the process terminates in a
local energy output, a scale-dominant residual bank, or an empty donor bank.

### Proof

Use SAS5dc to choose `Q_*`, SAS5de for the local router and SAS5df for the residual bank.  In
the residual collateral-dominant branch, `Q_*` is absent and the number of active signatures
strictly decreases.  Finite iteration proves termination. QED.

## Corrected SAS6 frontier

The collateral-dominant branch no longer ends at a passive heavy exact record.  Its active
negative stock has an exact incidence identity, every heavy record acts on at most two donors,
and iterative peeling terminates after at most the active-signature stock.

The remaining sparse work is to convert the five local energy outputs into the desired global
arithmetic continuation, bound `K_act` sharply in the concentrated geometric regimes,
continue the coprime donor-saturated progression, and handle high-incidence and reflected-
board boundary profiles.

## Finite check

`scripts/verify_sparse_active_cross_record_peeling.py` exhausts small active-record incidence
systems and samples larger donor banks.  It checks the exact incidence identity, active-stock
aggregate bound, one-or-two-donor localization, five-way energy router, residual peeling
inequality and finite signature-removal process.