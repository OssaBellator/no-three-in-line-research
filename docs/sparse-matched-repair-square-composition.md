# Physical square composition for matched repair banks

**Branch:** `research/sparse-algebraic-spread`

SAS5fc--SAS5fg compare every realized repair union with an opposite destruction ledger.  The matched
branch is exact and alias-safe, but it is still only a signed-ledger cancellation: the repair
operation and the opposite destruction operation need not yet form one legal chronological move.

This note isolates the missing physical contract and proves the corresponding batching theorem.
Once every matched record is assigned to a legal repair-then-destroy operation square, bounded
support and complete-scope incidence give a compatible subbank.  Under an explicit joint two-stage
legality clause, all selected matched records are physically created in the first stage and destroyed
in the second, with exact energy additivity across the selected squares.

## Matched operation-square model

Let the exact matched repaired/opposite-destruction bank have total weight

`M=sum_Q m_Q`.

Aggregate it into a finite family `A` of **operation-square vertices**.  A vertex `a in A` consists
of:

- one legal repairing operation `sigma_a` in a common base colouring `kappa`;
- one opposite destruction operation `tau_a` legal after `sigma_a`;
- a nonempty alias-aggregated set `R_a` of exact matched records;
- vertex weight

  `H_a=sum_(Q in R_a) m_Q`;
- combined movable support

  `S_a=supp(sigma_a) union supp(tau_a)`.

Every exact matched record is assigned to exactly one vertex, so

`M=sum_(a in A) H_a`.

Assume the **matched-square realization contract**:

1. every `Q in R_a` is absent in `kappa`, present after `sigma_a`, and absent after
   `sigma_a tau_a`;
2. the complete exact rank-three ledger contains every record affected by either operation;
3. each local two-stage operation is legal in its declared state;
4. every interaction-independent square family has a legal simultaneous repair stage, followed by a
   legal simultaneous destruction stage after those repairs;
5. distinct exact aliases were aggregated before assignment;
6. every combined support has size at most `r`;
7. every physical column belongs to at most `mu` combined supports;
8. every physical column belongs to at most `Lambda_sq` exact record scopes in the complete ledger;
9. failure returns the least square, operation, joint-legality, record, alias, support, scope, label
   or boundary field.

For two balanced swaps one may take the safe support bound `r<=4`.

## SAS5fh -- exact matched-square aggregation -- PROVED UNDER THE REALIZATION CONTRACT

The square weights satisfy

`M=sum_a H_a`.

For one vertex `a`, executing `sigma_a` creates every exact record in `R_a` with total transient
matched weight `H_a`, and executing `tau_a` afterwards destroys every one of those same records.

### Proof

Every matched exact record is assigned once after alias aggregation, giving the weight identity.
Items 1 and 3 of the realization contract give the exact absent--present--absent indicator table for
each assigned record.  Summing the assigned record weights gives `H_a`. QED.

This is the physical condition missing from signed-ledger cancellation.  If it fails, the matched
record remains an accounting witness rather than an executable square.

## SAS5fi -- bounded matched-square interaction degree -- PROVED UNDER THE INCIDENCE CAPS

Join two square vertices when either:

1. their combined supports intersect; or
2. one exact rank-three scope in the complete ledger meets both combined supports.

The resulting interaction graph has maximum degree at most

`D_sq=r*(mu-1)+r*Lambda_sq*(3mu-1)`.

Consequently it has an independent square bank `J` with

`sum_(a in J) H_a>=M/(D_sq+1)`.

If an incidence cap fails, one physical column belongs to more than `mu` square supports or more than
`Lambda_sq` complete-ledger scopes.

### Proof

Fix one square vertex `a`.  Through each of at most `r` support columns, at most `mu-1` other square
supports meet `S_a`, giving at most `r(mu-1)` support-overlap neighbours.

Each support column lies in at most `Lambda_sq` exact scopes.  A rank-three scope contains three
columns, and each column belongs to at most `mu` square supports.  Thus one such scope meets at most
`3mu` square supports and identifies at most `3mu-1` other vertices.  Summing over the at most
`r Lambda_sq` incident scopes gives the second term.  Repeatedly counting one neighbour only weakens
the bound.

Greedy colouring uses at most `D_sq+1` colours.  A heaviest colour class retains the displayed
weight. QED.

## SAS5fj -- simultaneous two-stage cancellation and energy additivity -- PROVED

Execute every repair operation `sigma_a`, `a in J`, simultaneously, and then every destruction
operation `tau_a`, `a in J`, simultaneously.  Under the matched-square contract:

1. both simultaneous stages are legal in their stated order;
2. after the repair stage, every selected matched record is present;
3. after the destruction stage, every selected matched record is absent;
4. selected exact record sets from distinct vertices are disjoint;
5. the transient physically created-and-destroyed matched weight is exactly

   `H_J=sum_(a in J) H_a`;
6. if

   `Delta_a=T(kappa^(sigma_a tau_a))-T(kappa)`,

   then the complete two-stage batch satisfies

   `T(kappa^(J))-T(kappa)=sum_(a in J) Delta_a`.

### Proof

Independence makes the combined supports pairwise disjoint.  Item 4 of the realization contract gives
joint legality of the two simultaneous stages.  If an exact scope met two selected supports, the
corresponding vertices would be adjacent by the second interaction rule.  Hence every complete-ledger
record indicator is affected by at most one selected square.

For a selected matched record, its own square gives the absent--present--absent table from SAS5fh,
and every other selected square leaves its scope unchanged.  This proves the two-stage cancellation.
Every matched exact record was assigned to exactly one square vertex, and alias aggregation forbids
duplicate physical addresses, so the selected record sets are disjoint.

Finally sum the complete exact energy ledger record by record.  Every scope has either one local
square change or zero change, so the simultaneous energy difference is the sum of the local square
differences. QED.

The final absence of the selected records is physical.  No claim is made that all other collateral
cancels.

## SAS5fk -- improving-square or barrier batch router -- PROVED

Define the local composed gain

`g_a=T(kappa)-T(kappa^(sigma_a tau_a))=-Delta_a`

and total positive square gain

`G_sq=sum_a (g_a)_+`.

One of the following holds:

1. one matched-square realization or joint-legality field fails;
2. one support or complete-scope incidence cap fails;
3. a compatible square batch gives energy descent at least

   `G_sq/(D_sq+1)`;
4. at a square-local minimum, a compatible batch physically creates and destroys matched exact
   weight at least

   `M/(D_sq+1)`,

   and its final energy change is the exact nonnegative sum of its local square barriers.

### Proof

For alternative 3, restrict to vertices with `g_a>0`, give them weight `g_a`, and apply SAS5fi to the
induced graph.  SAS5fj makes their gains additive.

At a square-local minimum every `g_a<=0`.  Apply SAS5fi with weights `H_a`.  SAS5fj gives the physical
transient cancellation bank and exact energy sum

`sum_a Delta_a=sum_a (-g_a)>=0`.

The remaining alternatives are precisely failed realization, joint-legality or incidence
hypotheses. QED.

The theorem does not claim that a nonimproving square batch lowers energy; it exposes the exact
barrier attached to a physically cancelled matched bank.

## SAS5fl -- integrated matched-bank composition bounds -- PROVED UNDER THE MATCHED-SQUARE CONTRACT

For the neutral persistent repair branch, SAS5fg gives matched weight

`M>=W_neu/[2(2N-3)(4Lambda_rep+1)]`

whenever its overlap branch occurs.  Therefore SAS5fk yields either an improving square batch, an
incidence/realization failure, or a physically created-and-destroyed matched bank of weight at least

`W_neu/[2(2N-3)(4Lambda_rep+1)(D_sq+1)]`.

For a common-step pair bank, SAS5el gives

`M>=B_pair/[2(D_pair+1)]`,

so the corresponding physically composed matched bank has weight at least

`B_pair/[2(D_pair+1)(D_sq+1)]`.

### Proof

Substitute the two existing matched-weight lower bounds into alternative 4 of SAS5fk.  The improving
and failed-contract alternatives are unchanged. QED.

## Corrected SAS6 frontier

Matched repair/opposite-destruction mass no longer stops at signed-ledger cancellation once the
local and joint repair-then-destroy square contracts are realized.  Bounded support and complete-scope
incidence retain an explicit compatible fraction whose matched records are physically created and
then destroyed with exact additive energy.

The remaining sparse work is realization of the local and joint matched-square contracts for every
word family, payment or descent through the resulting nonnegative square barriers, resolution of
composed-only positive curvature by negative collateral, positive base-row realization, and the
reflected-boundary or high-incidence branches.

## Finite check

`scripts/verify_sparse_matched_repair_square_composition.py` samples weighted square vertices,
combined supports and complete rank-three scope ledgers.  It checks the `D_sq` degree bound, weighted
independent extraction, absent--present--absent matched tables, distinct transient unions, exact
two-stage energy additivity, positive-gain restriction and the integrated neutral/common-step
constants.  Joint operation legality remains the explicit physical contract audited by the theorem.