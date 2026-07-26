# Aggregate mixed-energy accounting across an endpoint-disjoint donor bank

**Branch:** `research/sparse-algebraic-spread`

SAS5ch--SAS5cl quotient symbolic aliases to exact physical records and prove that one
rank-three record has negative mixed-curvature incidence at most two across a bank of
pairwise endpoint-disjoint donor swaps.  This note sums the exact mixed-energy identity
over the complete bank.

The result controls not only the selected scale mass of improving donors, but the sum of
that mass and the actual improvement depth.  It also gives the precise threshold at which
a donor bank must contain a positive composed-move barrier.

## Donor-bank setup

Fix one original transposition `omega={x,y}` and a finite donor family `T` whose endpoint
sets are pairwise disjoint and disjoint from `{x,y}`.  Exact record aliases have already
been aggregated as in SAS5ch.

For each donor `tau in T`, let:

- `L_tau>0` be the selected repaired divisor-scale weight;
- `Delta_tau` be the single-donor energy increment;
- `Delta_comb(tau)` be the energy increment of `omega union tau`;
- `C_minus(tau),C_plus(tau)>=0` be the external negative and positive mixed-curvature
  masses.

Write

`Delta_omega=T(kappa^omega)-T(kappa)`,

`L_bank=sum_(tau in T)L_tau`,

`C_minus_bank=sum_tau C_minus(tau)`,

`C_plus_bank=sum_tau C_plus(tau)`.

Assume the original colouring is swap-local-minimal, so

`Delta_omega>=0`

and `Delta_tau>=0` for every donor.  Let

`Omega_cross=sum_(Q:scope(Q) meets {x,y})Omega_Q`.

By SAS5ck,

`C_minus_bank<=2*Omega_cross`.

## SAS5cm -- exact summed donor-bank identity -- PROVED

If `m=|T|`, then

`sum_(tau in T)Delta_comb(tau)`

`=m*Delta_omega+sum_tau Delta_tau+L_bank+C_plus_bank-C_minus_bank`.

### Proof

For each donor, SAS5bn--SAS5bo give

`Delta_comb(tau)=Delta_omega+Delta_tau+L_tau+C_plus(tau)-C_minus(tau)`.

Sum over `tau`. QED.

The original-swap increment appears once for each separately tested composed move.  This
is an identity for a family of individual two-swap experiments, not for one simultaneous
multi-donor move.

## SAS5cn -- two-reuse aggregate lower bound -- PROVED

Under swap-local minimality,

`sum_tau Delta_comb(tau) >= L_bank-2*Omega_cross`.

More sharply,

`sum_tau Delta_comb(tau)`

`>=m*Delta_omega+sum_tau Delta_tau+L_bank-2*Omega_cross`.

### Proof

Discard the nonnegative `C_plus_bank` in SAS5cm and apply
`C_minus_bank<=2*Omega_cross`.  The single-swap increments are nonnegative. QED.

Thus the complete bank cannot hide more than two units of negative mixed-curvature reuse
per unit of physical cross-record weight.

## SAS5co -- total improvement-depth budget -- PROVED

Let

`I={tau in T:Delta_comb(tau)<0}`.

Then

`sum_(tau in I)(L_tau-Delta_comb(tau)) <= 2*Omega_cross`.

Equivalently,

`sum_(tau in I)(L_tau+|Delta_comb(tau)|) <= 2*Omega_cross`.

Consequently:

1. `sum_(tau in I)L_tau<2*Omega_cross` unless `I` is empty;
2. `sum_(tau in I)|Delta_comb(tau)|<2*Omega_cross`;
3. if every improving donor has `L_tau>=lambda>0` and improvement depth
   `|Delta_comb(tau)|>=gamma>0`, then

   `|I| <= floor(2*Omega_cross/(lambda+gamma))`.

### Proof

For an improving donor, the exact one-donor identity rearranges to

`C_minus(tau)`

`=Delta_omega+Delta_tau+L_tau+C_plus(tau)-Delta_comb(tau)`

`>=L_tau-Delta_comb(tau)`.

Sum over `I` and use

`sum_(tau in I)C_minus(tau)<=C_minus_bank<=2*Omega_cross`.

The separate mass and depth bounds follow by dropping positive summands.  The cardinality
bound follows from the common lower bounds. QED.

This strengthens SAS5cl: collateral pays both for the repaired scale and for how far the
composed move actually descends.

## SAS5cp -- bank-scale threshold forces a positive barrier -- PROVED

If

`L_bank>2*Omega_cross`,

then at least one donor satisfies

`Delta_comb(tau)>0`.

More quantitatively, with `m=|T|>0`, one donor has

`Delta_comb(tau) >= (L_bank-2*Omega_cross)/m`.

Conversely, if every composed move in the bank is nonpositive, then

`L_bank<=2*Omega_cross`.

### Proof

SAS5cn gives

`sum_tau Delta_comb(tau)>=L_bank-2*Omega_cross`.

If the right side is positive, the average composed increment is at least the displayed
quantity, so one donor attains at least the average.  If every increment is nonpositive,
the sum is nonpositive and the same inequality forces `L_bank<=2*Omega_cross`. QED.

This is an energy barrier, not an improving-move conclusion.  It records exactly what a
large donor bank proves when the physical cross-collateral stock is too small.

## SAS5cq -- aggregate donor-bank router -- PROVED

Every endpoint-disjoint donor bank has one exact continuation:

1. **scale-dominant bank:** `L_bank>2*Omega_cross`; then one donor has a positive composed
   barrier at least `(L_bank-2*Omega_cross)/|T|`;
2. **cross-collateral-dominant bank:** `L_bank<=2*Omega_cross`; then the physical exact-record
   stock satisfies `Omega_cross>=L_bank/2`;
3. **improving subbank:** regardless of the first two alternatives, the total selected
   scale mass plus total improvement depth of all improving donors is at most
   `2*Omega_cross`.

If the cross-record family under consideration has at most `K_cross` exact physical
signatures, the second alternative contains one signature of aggregate weight at least

`L_bank/(2*K_cross)`.

### Proof

The first two alternatives are complementary and use SAS5cp.  The improving-subbank
statement is SAS5co.  The final localization is weighted pigeonhole over the exact alias
quotient. QED.

## Corrected SAS6 frontier

The negative mixed-curvature branch now has:

- one exact physical-record quotient;
- mixed-curvature reuse at most two across endpoint-disjoint donors;
- an aggregate bank lower bound;
- and a joint budget for repaired scale mass plus actual improvement depth.

The remaining sparse obligations are to construct geometric donor banks with enough
selected scale mass for the desired side of SAS5cq, exploit the resulting heavy exact
record when cross collateral dominates, and continue the coprime donor-saturated
progression, high-incidence and boundary analyses.

## Finite check

`scripts/verify_sparse_donor_bank_aggregate_energy.py` exhausts small exact mixed-energy
systems and samples larger endpoint-disjoint donor banks.  It checks the summed identity,
the two-reuse lower bound, the improvement-depth budget, the average positive-barrier
bound and exact-record localization in the collateral-dominant branch.
