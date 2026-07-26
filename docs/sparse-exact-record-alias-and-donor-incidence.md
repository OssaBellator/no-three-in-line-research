# Exact-record alias quotient and donor-bank mixed-curvature incidence

**Branch:** `research/sparse-algebraic-spread`

SAS5cc--SAS5cg localize the negative mixed-curvature branch to one exact geometric-label
record.  The remaining multiplicity question is whether repeated symbolic occurrences of
that record create additional independent obstruction.  They do not: identical records
have the same indicator under every colouring and may be merged into one weighted physical
record without changing any energy or mixed-curvature calculation.

For several donor swaps there is also an exact compatibility bound.  Relative to one fixed
original swap, a rank-three record has at most two columns outside the original endpoint
pair.  Hence it can interact with at most two members of a pairwise endpoint-disjoint donor
bank.

## Exact physical record signatures

An exact geometric-label record signature is

`Q=(ordered rows, ordered columns, required labels)`.

Every symbolic occurrence `xi` with signature `Q` has a nonnegative weight `w_xi` and the
same conjunction indicator `I_Q(kappa)` under every colouring `kappa`.  Put

`Omega_Q=sum_(xi:sigma(xi)=Q)w_xi`.

Fix one original transposition `omega={x,y}`.  Let `T` be a finite family of donor
transpositions, pairwise disjoint in their endpoint columns and disjoint from `{x,y}`.

## SAS5ch -- exact-record aliases aggregate without loss -- PROVED

Replacing all symbolic occurrences of one exact signature `Q` by one physical weighted
record of weight `Omega_Q` preserves:

1. the energy `T(kappa)` for every colouring;
2. every single-swap increment;
3. every composed-swap increment;
4. every mixed curvature contribution.

### Proof

Every alias has the identical indicator value in every colouring.  Its total contribution is

`sum_xi w_xi*I_Q(kappa)=Omega_Q*I_Q(kappa)`.

All listed increments and curvatures are linear combinations of four such energy values, so
they are preserved as well. QED.

Thus symbolic duplication creates no new compatibility object.  It changes only the one
aggregate physical weight `Omega_Q`.

## SAS5ci -- exact negative fibres have one aggregate curvature atom -- PROVED

Fix disjoint swaps `omega,tau` and an exact record signature `Q` with

`partial_(omega,tau)I_Q=-1`.

All aliases of `Q` contribute total negative mixed curvature exactly `Omega_Q`.  They may be
charged, localized or capacity-capped only through this shared aggregate; alias names do not
supply separate physical records.

If the energy model declares a physical occurrence capacity `c_Q`, then exactly one of

`Omega_Q<=c_Q`

or

`Omega_Q-c_Q>0`

holds, the second being an exact multiplicity-overload amount at `Q`.

### Proof

SAS5ch merges the aliases.  The merged curvature contribution is

`Omega_Q*(-partial I_Q)=Omega_Q`.

The capacity split is tautological and is attached to the physical signature rather than to
its aliases. QED.

## SAS5cj -- rank-three records meet at most two disjoint donor swaps -- PROVED

Let `Q` be a rank-three record whose scope meets `{x,y}`.  Then the number of donor swaps
`tau in T` for which

`partial_(omega,tau)I_Q != 0`

is at most

`3-|scope(Q) intersect {x,y}|`,

and hence at most two.

If `Q` contains both original endpoints, the bound improves to one.

### Proof

Nonzero mixed curvature requires the scope to meet both endpoint sets.  The scope has three
columns and already uses `|scope(Q) intersect {x,y}|` of them on the original swap.  Every
donor swap producing nonzero curvature must contain at least one of the remaining scope
columns.  Because donor endpoint sets are pairwise disjoint, distinct donors require
distinct remaining columns. QED.

This is an exact incidence cap, not a probabilistic spread estimate.

## SAS5ck -- total negative mixed curvature has reuse at most two -- PROVED

For each donor `tau in T`, let

`C_minus(tau)=sum_Q Omega_Q*(-partial_(omega,tau)I_Q)_+`,

where exact aliases have already been aggregated.  Put

`Omega_cross=sum_(Q:scope(Q) meets {x,y})Omega_Q`.

Then

`sum_(tau in T) C_minus(tau) <= 2*Omega_cross`.

More sharply,

`sum_tau C_minus(tau)
 <= sum_Q (3-|scope(Q) intersect {x,y}|)*Omega_Q`.

### Proof

For conjunction records the negative curvature magnitude is at most one.  By SAS5cj, a
fixed physical record contributes to at most `3-|scope intersect {x,y}|` donor sums.  Sum
first over donors and then over exact records. QED.

No exact negative record can be reused across arbitrarily many pairwise disjoint donor
moves.

## SAS5cl -- donor-bank barrier and improving-move budget -- PROVED

For each donor `tau in T`, suppose a selected repaired divisor scale has weight `L_tau>0`.
Fix `eta in (0,1)` and define the heavy-collateral donor set

`H_eta={tau:C_minus(tau)>=eta*L_tau}`.

Then

`sum_(tau in H_eta)L_tau <= 2*Omega_cross/eta`.

Every donor outside `H_eta` satisfies the SAS5bp energy barrier

`Delta_comb(tau)>(1-eta)*L_tau`.

In particular, every energy-improving composed move belongs to `H_eta` for every `eta<1`,
and the improving donors satisfy

`sum_(tau improving)L_tau < 2*Omega_cross`.

If every selected scale has `L_tau>=lambda>0`, the number of improving donors is strictly
less than

`2*Omega_cross/lambda`.

### Proof

Sum `eta*L_tau<=C_minus(tau)` over `H_eta` and apply SAS5ck.  For donors outside the set,
SAS5bp gives the displayed barrier.  An improving move has `C_minus(tau)>L_tau`, so summing
over improving donors and applying SAS5ck gives the strict bound.  The cardinality estimate
follows from the common lower bound `lambda`. QED.

## Corrected SAS6 frontier

Occurrence multiplicity inside one exact negative record is now a harmless weighted alias
quotient.  Across an endpoint-disjoint donor bank, every physical rank-three record has
mixed-curvature reuse at most two, giving a finite aggregate budget for heavy-collateral and
improving composed moves.

The remaining sparse frontier is now:

- exploit the exact heavy record or multiplicity overload when it occurs;
- construct a donor bank whose selected scale mass beats the two-reuse collateral budget;
- use the coprime donor-saturated progression in the alternate scale branch;
- handle high-incidence and board-boundary profiles.

## Finite check

`scripts/verify_sparse_exact_record_alias_and_donor_incidence.py` exhausts small conjunction
records and colourings, aggregates symbolic aliases, and samples endpoint-disjoint donor
banks.  It checks energy/curvature preservation, the exact two-donor incidence cap, the
weighted reuse inequality and the donor-bank barrier bounds.