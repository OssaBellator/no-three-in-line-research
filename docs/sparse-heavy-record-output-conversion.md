# Explicit active-record stock and heavy-record output conversion

**Branch:** `research/sparse-algebraic-spread`

SAS5db--SAS5dg replace passive cross collateral by the exact active negative-record stock and
peel every heavy active record through at most two donor swaps.  The local peel previously ended
with five energy quantities: a composed improvement, the original-swap increment, the donor-
swap increment, designated repair mass, or positive mixed curvature.

This note makes those outputs geometric.  First, the complete active-record family has an
explicit polynomial stock.  Second, a positive single-swap increment contains a heavy repair
word.  Third, positive mixed curvature has exactly two conjunction patterns and localizes to a
finite endpoint-pair/scope-type fibre.  Thus every nonimproving heavy-record peel returns an
explicit repair or curvature certificate at a quantified fraction of the record weight.

## Fixed bank notation

Fix a balanced colouring on `N` columns, one original cross-label swap

`omega={x,y}`,

and an endpoint-disjoint donor bank `T`, disjoint from `{x,y}`.  Exact rank-three record aliases
are aggregated.  For one active negative record `Q_*`, write

`Omega_*=Omega_(Q_*)`

and choose its canonical incident donor `tau_*` as in SAS5dd.

Use the one-donor identity

`Delta_comb(tau_*)`

`=Delta_omega+Delta_(tau_*)+L_(tau_*)+C_plus(tau_*)-C_minus(tau_*)`,

with

`C_minus(tau_*)>=Omega_*`.

All single-swap increments are nonnegative at the swap-local minimum.

## SAS5dh -- explicit global active-record signature stock -- PROVED

For fixed `omega`, current colouring and endpoint-disjoint donor bank, the number `K_act` of
exact active negative rank-three record signatures satisfies

`K_act<=24*binom(N,3)*(N-2)^2`.

### Proof

Choose the increasing ordered row positions in `binom(N,3)` ways.  The scope columns are an
ordered triple of distinct columns.  The number of ordered column triples meeting `{x,y}` is

`(N)_3-(N-2)_3=6*(N-2)^2`.

For one fixed ordered scope, at most two donor swaps meet it because donor endpoint sets are
pairwise disjoint and the rank-three scope has at most two columns outside the original swap.
For each incident donor, negative curvature has exactly the two single-swap-only orientations
of SAS5bu.  Once the current colouring, two swaps, scope and orientation are fixed, the unique
satisfying single-swap state forces every required label.  Hence each ordered scope supports at
most four active exact signatures.  Multiply the three factors. QED.

No `b^3` label factor is required.

Consequently a collateral-dominant active bank with

`Omega_act>=L_bank/2`

contains one exact active record of weight at least

`Omega_*>=L_bank/[48*binom(N,3)*(N-2)^2]`.

## SAS5di -- the two exact positive-curvature patterns -- PROVED

For two disjoint swaps, a conjunction record has positive mixed curvature if and only if its
four-state indicator table is exactly one of

`(1,0,0,0)`

or

`(0,0,0,1)`.

Equivalently:

1. **current-only orientation:** the record is satisfied only in the original colouring and is
   destroyed by either single swap and by the composed move;
2. **composed-only orientation:** the record is satisfied only after both swaps and by neither
   single swap.

Every positive record has curvature exactly `+1`.

If a family carries total positive-curvature weight `C_plus`, then one exact orientation,
canonical endpoint pair and third-column scope type carries at least

`C_plus/24`.

### Proof

Use the product factorization

`partial_(omega,tau)I=C*(A_1-A_0)*(B_1-B_0)`

from SAS5bs.  Positivity requires the two one-variable differences to have the same nonzero
sign.  Two increasing differences give `(0,0,0,1)`; two decreasing differences give
`(1,0,0,0)`.

For localization, partition into two orientations.  Every nonzero-curvature scope meets both
swap endpoint sets.  Choose canonically one of four endpoint pairs and then one of the three
third-column types: outside all endpoints, mate of the chosen original endpoint, or mate of the
chosen donor endpoint.  Weighted pigeonhole over `2*4*3=24` classes proves the bound. QED.

## SAS5dj -- a positive single-swap barrier contains a repair word -- PROVED

For any cross-label swap `sigma`, let `D(sigma)` and `R(sigma)` be its weighted destroyed-current
and repaired-near-conflict masses.  Then

`Delta_sigma=R(sigma)-D(sigma)`.

If

`Delta_sigma>=a>0`,

then

`R(sigma)>=a`,

and one of the twelve repair words from SAS5j carries weight at least

`a/12`.

### Proof

The exact energy increment is repaired weight minus destroyed weight, so

`R=D+Delta>=a`.

The twelve repair words partition `R`; a heaviest word carries at least one twelfth. QED.

This applies to either the original swap or the canonical donor swap.

## SAS5dk -- converted local router at one heavy active record -- PROVED

At the canonical incident donor `tau_*`, at least one of the following holds:

1. **composed descent:**

   `Delta_comb(tau_*)<0`;

2. **original repair word:** one repair word for `omega` carries weight at least

   `Omega_*/48`;

3. **donor repair word:** one repair word for `tau_*` carries weight at least

   `Omega_*/48`;

4. **designated divisor-scale repair:**

   `L_(tau_*)>=Omega_*/4`;

5. **positive-curvature fibre:** one current-only or composed-only endpoint-pair/scope-type fibre
   carries weight at least

   `Omega_*/96`.

### Proof

If the composed increment is negative, use alternative 1.  Otherwise rearrange the exact
one-donor identity:

`Delta_omega+Delta_(tau_*)+L_(tau_*)+C_plus(tau_*)`

`=C_minus(tau_*)+Delta_comb(tau_*)>=Omega_*`.

One of the four nonnegative summands is at least `Omega_*/4`.  If it is a single-swap increment,
apply SAS5dj and lose a factor twelve.  If it is `L_(tau_*)`, use alternative 4.  If it is
positive curvature, apply SAS5di and lose a factor twenty-four. QED.

Thus none of the four nonnegative energy terms remains an uninterpreted scalar.

## SAS5dl -- explicit collateral-dominant peel router -- PROVED

Suppose an active donor bank is collateral-dominant:

`L_bank<=2*Omega_act`,

and let

`K_0=24*binom(N,3)*(N-2)^2`.

Then one active record and one of at most two incident donors give at least one of:

1. an improving composed move;
2. an original or donor repair word of weight at least

   `L_bank/(96*K_0)`;

3. designated repaired divisor-scale mass at least

   `L_bank/(8*K_0)`;

4. a positive current-only or composed-only curvature fibre of weight at least

   `L_bank/(192*K_0)`.

Deleting the at-most-two incident donors removes that active record from the residual negative
ledger as in SAS5df.  If one elects to continue peeling rather than use the local certificate,
the active-signature count drops by at least one.  Hence after at most `K_0` peel steps the bank
is empty, becomes scale-dominant, or has produced one of the four displayed outputs at the
current residual scale.

### Proof

Collateral dominance and SAS5dh give

`Omega_*>=Omega_act/K_0>=L_bank/(2K_0)`.

Substitute this bound into the four quantitative alternatives of SAS5dk.  SAS5df gives the
residual deletion statement, and each continuation removes one active exact signature. QED.

The per-step lower bounds use the current residual `L_bank` if the peel is iterated.

## Corrected SAS6 frontier

The collateral-dominant branch now has:

- the explicit stock `K_act<=24 binom(N,3)(N-2)^2`;
- an improving composed move or a quantified original/donor repair word;
- a quantified designated divisor-scale repair;
- or a positive current-only/composed-only cross fibre;
- together with terminating one-or-two-donor peeling.

The remaining work is to batch or arithmetically classify these repair-word and positive-fibre
outputs, continue the coprime donor-saturated progression, and handle high-incidence and
reflected-board boundary profiles.  Improving the active stock below the safe degree-six bound
requires additional row or column concentration.

## Finite check

`scripts/verify_sparse_heavy_record_output_conversion.py` exhausts the conjunction factor tables,
checks the two positive-curvature patterns and enumerates small active cross scopes.  It verifies
the `24 binom(N,3)(N-2)^2` stock, barrier-to-repair-word conversion, positive-fibre localization,
the five-way converted router and the explicit collateral-dominant constants.