# Constraint-compatible donor batches and exact energy additivity

**Branch:** `research/sparse-algebraic-spread`

SAS5ae--SAS5ai produce a large endpoint-disjoint bank of balanced donor
transpositions for diffuse reflected-label defects.  Local safety for the
selected mirror records does not by itself control all geometric constraints.
This note adds the global constraint interaction graph.

A bounded column-incidence hypothesis gives a large subbank on which no
constraint sees two donor swaps.  On that subbank the balanced-colour energy
change is exactly the sum of the individual changes, and all newly satisfied
collateral is charged to donor endpoints.

## Constraint and donor notation

Let `Q` be the complete multiset of geometric constraint records used by the
balanced-colour energy.  Every record has three distinct scope columns and one
required label at each column.

For a balanced colouring `kappa`, write

`I_Q(kappa) in {0,1}`

for the satisfaction indicator and

`T(kappa)=sum_Q I_Q(kappa)`.

Let `B` be a bank of pairwise endpoint-disjoint transpositions

`tau={z,q}`.

For one transposition define

`Delta_tau=T(kappa^tau)-T(kappa)=R_tau-D_tau`,

where `D_tau` and `R_tau` are the numbers of currently satisfied records
destroyed and currently unsatisfied records repaired by `tau`.

Assume each column occurs in the scopes of at most `Lambda` records of `Q`.

## Global donor interaction graph

Join distinct transpositions `tau,sigma in B` when some constraint scope meets
an endpoint of both transpositions.

## SAS5aj -- global donor interaction degree -- PROVED

The donor interaction graph has maximum degree at most

`4*Lambda`.

Consequently it contains an independent set of size at least

`|B|/(4*Lambda+1)`.

### Proof

Fix `tau`, with two endpoint columns.  Each endpoint belongs to at most
`Lambda` constraint scopes, so at most `2*Lambda` constraint incidences touch
`tau`.  A rank-three scope containing one endpoint of `tau` has at most two
other columns.  Since bank endpoints are disjoint, each such other column is an
endpoint of at most one other bank transposition.  Thus each incident record
creates at most two neighbours, giving degree at most `4*Lambda`.  Greedy
colouring with one more colour gives the independent-set bound. QED.

## SAS5ak -- independent donor banks have exact energy additivity -- PROVED

Let `I` be an independent set in the global donor interaction graph and apply
all its endpoint-disjoint transpositions simultaneously.  Then

`T(kappa^I)-T(kappa)=sum_(tau in I) Delta_tau`.

Equivalently, the total numbers of destroyed and repaired records are the sums
of the individual `D_tau` and `R_tau` values.

### Proof

Independence means every constraint scope meets endpoints of at most one
selected transposition.  A record meeting no endpoint is unchanged.  A record
meeting one selected transposition changes exactly as it does under that
transposition alone.  Sum the indicator changes over all records. QED.

Thus any independent subbank with

`sum D_tau > sum R_tau`

is an executable balanced batch lowering the energy by the difference.

## SAS5al -- positive individual gain survives compatibility extraction -- PROVED

Give transposition `tau` positive gain

`g_tau=(D_tau-R_tau)_+`.

There is an independent donor subbank `I` satisfying

`sum_(tau in I) g_tau >= (sum_(tau in B) g_tau)/(4*Lambda+1)`.

Every transposition in `I` with positive gain may be retained, and the resulting
simultaneous batch lowers `T` by at least the displayed amount.

### Proof

Colour the global interaction graph with at most `4*Lambda+1` colours.  One
colour class carries at least the average positive gain.  It is independent,
and SAS5ak makes the simultaneous energy change the sum of its individual
negative changes. QED.

At a balanced swap-local minimum every `g_tau` is zero, so the useful output is
instead a quantified collateral bank.

## SAS5am -- endpoint collateral and repair multiplicity bounds -- PROVED

For every donor transposition,

`D_tau+R_tau <= 2*Lambda`.

Moreover, because the bank is endpoint-disjoint, one exact constraint record is
repaired by at most three transpositions in `B`.

Consequently, at a swap-local minimum,

`sum_(tau in B) R_tau >= sum_(tau in B) D_tau`,

and the union of distinct repaired records has size at least

`(sum_(tau in B) D_tau)/3`.

### Proof

Only records containing one of the two changed endpoint columns can change.
Each endpoint lies in at most `Lambda` records, giving the first bound.

If a transposition repairs one fixed rank-three record, at least one of its
endpoints lies in that record's three-column scope.  Endpoint disjointness
assigns at most one bank transposition to each scope column, so at most three
bank transpositions repair the record.

At a swap-local minimum `Delta_tau=R_tau-D_tau>=0` for every balanced
transposition.  Sum this inequality and divide the repair-incidence count by
the multiplicity bound three. QED.

## SAS5an -- donor-batch energy router -- PROVED

A donor bank from SAS5ag now has one of two exact continuations.

1. Positive individual donor gain exists.  Under the column-incidence cap, an
   executable constraint-compatible batch retains at least a
   `1/(4*Lambda+1)` fraction of the total positive gain.
2. The colouring is donor-local-minimal on the bank.  Then the donor endpoints
   expose at least `sum D_tau/3` distinct repaired geometric records, while each
   swap has total changed-record collateral at most `2*Lambda`.

The second branch is a new near-conflict bank, not a proof of improvement.  It
must be compared with the reflected destruction records or passed back through
the finite word and parameter classifiers.

## Corrected SAS6 frontier

The first global collateral extraction for reflected-label donor swaps is now
complete under a column-incidence cap:

- a large constraint-compatible subbank exists;
- its energy change is exactly additive;
- positive donor gain survives with explicit loss `4*Lambda+1`;
- donor-local failure returns many distinct repaired constraints with
  multiplicity at most three.

The remaining work is to relate `sum D_tau` to the original reflected-defect
weight, classify the returned repaired records arithmetically, and handle
boundary profiles or hosts where `Lambda` is too large.

## Finite check

`scripts/verify_sparse_donor_batch_energy.py` exhausts small endpoint-disjoint
donor banks and rank-three constraint scopes.  It checks the `4*Lambda` degree
bound, per-record and total energy additivity, the `2*Lambda` changed-record cap
and the repair multiplicity bound three.
