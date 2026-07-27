# Compatible batching of neutral persistent one-swap repairs

**Branch:** `research/sparse-algebraic-spread`

SAS5es--SAS5ew classify a heavy fresh exact record with zero mixed curvature as a persistent
one-swap repair: exactly one of the two distinguished swaps creates the record, and the other swap
preserves it.  A single such record is already exact, but a large family of neutral outputs may use
intersecting creating swaps or share other geometric constraints.

This note gives a two-stage weighted extraction.  First, a line-graph colouring makes the creating
swaps endpoint-disjoint.  Second, the complete exact-record incidence ledger removes every remaining
cross-operation interaction.  The resulting swaps execute simultaneously, their selected neutral
records all survive, and the energy change is exactly additive.

## Neutral operation ledger

Let `A` be an alias-aggregated bank of exact neutral repair atoms.  An atom is a pair

`a=(sigma_a,Q_a)`

with weight `h_a>0`, where:

- `sigma_a` is the unique balanced swap creating `Q_a` from the current colouring;
- `Q_a` is an exact rank-three record absent currently and present after `sigma_a`;
- the second distinguished disjoint swap from SAS5ev preserves `Q_a` after creation.

Aggregate all atoms with the same creating swap `sigma` and write

`A_sigma=sum_(a:sigma_a=sigma) h_a`,

`W_neu=sum_sigma A_sigma`.

Assume the **neutral-operation realization contract**:

1. every declared creating swap is physically balanced and legal;
2. the exact record list is alias-aggregated before `A_sigma` is formed;
3. the complete rank-three energy ledger contains every record affected by the selected swaps;
4. every physical column belongs to at most `Lambda` exact record scopes in that complete ledger;
5. a failure returns the least exact swap, record, label, incidence or boundary field.

## SAS5ex -- exact creating-swap aggregation -- PROVED

Executing one creating swap `sigma` installs every neutral record assigned to it, before any other
swap is applied, with total exact selected-record weight `A_sigma`.

The complete neutral weight satisfies

`W_neu=sum_sigma A_sigma`.

### Proof

Each atom assigned to `sigma` has the same unique creating operation.  Exact aliases were aggregated
before the weights were summed, so executing `sigma` creates each selected physical record once and
the union weight is the sum of its exact record weights.  Summing over distinct creating swaps gives
`W_neu`. QED.

## SAS5ey -- endpoint-disjoint weighted creating swaps -- PROVED

The graph whose vertices are the distinct creating swaps and whose edges join swaps sharing a
column has maximum degree at most

`2N-4`.

Hence it has an endpoint-disjoint colour class `M` satisfying

`sum_(sigma in M) A_sigma>=W_neu/(2N-3)`.

### Proof

A swap `{x,y}` shares an endpoint with at most `N-2` other swaps through `x` and at most `N-2`
through `y`.  Thus the line graph has maximum degree at most `2N-4` and is greedily colourable with
`2N-3` colours.  The colour-class weights sum to `W_neu`; a heaviest class gives the bound. QED.

Every physical column is an endpoint of at most one swap in `M`.

## SAS5ez -- complete-record interaction extraction -- PROVED UNDER THE INCIDENCE CAP

On the endpoint-disjoint class `M`, join two swaps when some exact rank-three record scope in the
complete energy ledger meets both endpoint pairs.  This interaction graph has maximum degree at
most

`D_neu=4Lambda`.

Consequently it contains an independent subbank `J` with

`sum_(sigma in J) A_sigma
 >=W_neu/[(2N-3)(4Lambda+1)]`.

If the declared cap fails, one physical column lies in more than `Lambda` exact record scopes.

### Proof

Fix one swap in `M`.  Its two endpoint columns lie in at most `2Lambda` record scopes in total.  A
rank-three scope meets at most three endpoint-disjoint swap supports, so each incident scope can
identify at most two other swaps.  Thus the interaction degree is at most `4Lambda`.  Greedy
colouring retains at least a `1/(4Lambda+1)` fraction of the weight already retained in `M`.
Substitute the SAS5ey bound. QED.

Repeated counting of one neighbouring swap only weakens the estimate.

## SAS5fa -- simultaneous persistence and exact energy additivity -- PROVED

Execute every distinct creating swap in `J` simultaneously.  Then:

1. every selected neutral record assigned to a swap in `J` is present in the final colouring;
2. selected exact records belonging to different swaps are distinct after alias aggregation;
3. the selected repaired-record union has weight exactly

   `R_neu(J)=sum_(sigma in J) A_sigma`;
4. if

   `Delta_sigma=T(kappa^sigma)-T(kappa)=R_sigma-D_sigma`,

   then

   `T(kappa^J)-T(kappa)=sum_(sigma in J) Delta_sigma`.

### Proof

The swaps in `J` are endpoint-disjoint by SAS5ey.  A selected record `Q_a` meets the endpoints of
its own creating swap.  If another selected swap met the scope of `Q_a`, that scope would meet both
swap supports and the two operations would be adjacent in the interaction graph, contradicting
independence.  Therefore every other selected swap leaves the indicator of `Q_a` unchanged after
its creation.

The same interaction condition says that every exact rank-three scope in the complete ledger meets
at most one selected swap support.  Its indicator change is therefore exactly its one-swap change,
or zero if it meets none.  Summing record by record proves energy additivity.  If one exact record
were assigned to two different selected swaps, its scope would meet both supports, again a
contradiction.  Thus the selected repaired union is distinct and has the displayed weight. QED.

## SAS5fb -- neutral repair batch router -- PROVED UNDER THE NEUTRAL-OPERATION CONTRACT

Let

`G_neu=sum_sigma (D_sigma-R_sigma)_+`

be the total positive one-swap energy gain available in the neutral operation bank.  One of the
following holds:

1. one exact creating swap, neutral table or record address is unrealized;
2. a compatible endpoint-disjoint batch gives energy descent at least

   `G_neu/[(2N-3)(4Lambda+1)]`;
3. at a swap-local minimum, a compatible batch installs a distinct exact neutral repair union of
   weight at least

   `W_neu/[(2N-3)(4Lambda+1)]`,

   and its simultaneous energy change is the exact nonnegative sum of its one-swap barriers;
4. the incidence cap fails, yielding one physical column in more than `Lambda` exact record scopes;
5. or one complete-ledger, label, boundary or operation contract field fails.

### Proof

Apply SAS5ey and SAS5ez with vertex weights `(D_sigma-R_sigma)_+` to obtain alternative 2, then use
SAS5fa for additive descent.  If every creating swap is nonimproving, apply the same two colourings
with weights `A_sigma`.  SAS5fa gives the exact repaired union and energy sum.  The remaining
alternatives are precisely the failed hypotheses of the two extraction and additivity steps. QED.

The theorem batches the neutral records themselves; it does not claim that a nonimproving repair
batch lowers energy.

## Corrected SAS6 frontier

Curvature-zero fresh records now admit a simultaneous exact repair bank with explicit retained
weight, additive energy and a named high-incidence alternative.  The remaining sparse work is
physical comparison of that repair union with the opposite destruction ledger, resolution of the
positive barrier by negative mixed collateral, realization of positive base-row translations, and
the reflected-boundary or high-incidence branches.

## Finite check

`scripts/verify_sparse_neutral_one_swap_batching.py` samples weighted creating-swap systems, exact
neutral records and complete rank-three scope ledgers.  It checks the `2N-4` endpoint degree, the
`4Lambda` interaction degree, both weighted colour extractions, simultaneous record persistence,
distinct repaired unions, exact recordwise energy additivity and the high-incidence alternative.