# Finite signature quotient for tagged-only lineage recycling

**Branch:** `research/geometric-cleaning`

GC2ch--GC2cl show that the tagged-energy potential has zero drift exactly when every destroyed
factor unit was already an active tagged lineage.  GC2cm--GC2cr then import every surviving
created-star cohort into the paid GC4 machinery.  The remaining temporal branch is tagged-only
recycling: old tagged lineages are destroyed and new tagged lineages are created without
consuming any previously uncharged current factor.

This note removes arbitrary lineage names from that branch.  Under fixed physical capacities
and signature-Markov continuation, only the current tagged multiplicity of each exact physical
signature matters.  The quotient is finite, exact first-destruction accounting is preserved at
the named level, and every recurrent tagged-only history reduces to one finite recycling-cycle
address.

## Fixed tagged-signature model

Let `P` be a finite set of exact physical factor signatures.  Signature `p` has fixed integer
capacity

`c_p>=0`

and fixed positive weight `w_p`.  At one time, let `L` be the finite set of active named tagged
lineages.  Every lineage `ell in L` has one signature `sigma(ell) in P`.  Put

`u_p=|{ell in L:sigma(ell)=p}|`,

so

`0<=u_p<=c_p`.

The untagged current background, hard context, correction rule and any other finite data are
included in one context value `chi` from a finite set `X`.

A **tagged-only event** destroys named active lineages and creates new named tagged lineages.
If it destroys `d_p` and creates `n_p` units of signature `p`, then

`u_p'=u_p-d_p+n_p`,

with `0<=d_p<=u_p` and `0<=u_p'<=c_p`.

A recreated copy of a previously destroyed signature receives a new lineage name.  Retired
lineage names never become active again.

The **signature-Markov contract** says that event legality, terminal status, future correction
menus and payment semantics depend on the active tagged family only through `(u,chi)`, not
through lineage names, birth times or the order in which equal-signature lineages were created.

## GC2cs -- exact active-lineage alias quotient -- PROVED

Two named active-lineage states with the same multiplicity vector `u` and context `chi` have the
same legal tagged-only quotient transitions and the same terminal classification.

For a quotient event with destruction vector `d` and creation vector `n`, both named states
produce the same successor vector

`u'=u-d+n`.

Renaming active lineages therefore changes neither the current weighted tagged mass nor any
future quotient behavior.

### Proof

The weighted tagged mass is

`U=sum_p w_p*u_p`,

which depends only on multiplicities.  The signature-Markov contract makes every legal action
and terminal test a function of `(u,chi)`.  Destroying any `d_p` of the equal-signature named
lineages and creating `n_p` fresh names produces the displayed vector independently of the
chosen names. QED.

First-destruction injectivity is not discarded.  At the named level every old lineage still has
one unique first destroying event.  The quotient removes only inactive historical names after
their payment has already been recorded.

## GC2ct -- exact finite quotient-state stock -- PROVED

The number of tagged multiplicity vectors is exactly

`N_mult=prod_(p in P)(c_p+1)`.

The full tagged quotient has at most

`N_tag=|X|*prod_(p in P)(c_p+1)`

states `(u,chi)`.

If a fixed total tagged unit count `B` is also imposed, the multiplicity stock is the coefficient
of `z^B` in

`prod_p(1+z+...+z^(c_p))`,

and is at most `binom(B+|P|-1,|P|-1)`.

### Proof

Coordinate `u_p` has exactly `c_p+1` choices.  Multiply the independent coordinate counts and
then the finite context count.  The fixed-total refinement is the standard bounded-composition
generating function, dominated by unrestricted weak compositions. QED.

No symbolic lineage-name factor appears.

## GC2cu -- tagged-only quotient preserves zero tagged-energy drift -- PROVED

Let a tagged-only event destroy weighted tagged mass

`D=sum_p w_p*d_p`

and create weighted tagged mass

`N=sum_p w_p*n_p`.

If `T` is total current factor weight, `U` is active tagged weight and

`Phi_tag=T-U`,

then

`T'=T-D+N`,

`U'=U-D+N`,

and therefore

`Phi_tag'=Phi_tag`.

This identity is determined entirely by the quotient transition `(u,chi)->(u',chi')`.

### Proof

Every destroyed factor in a tagged-only event is an active tagged lineage, so the same weighted
amount `D` leaves both `T` and `U`.  Every newly created factor receives an active tag, so the
same weighted amount `N` enters both quantities.  Subtraction gives zero drift. QED.

Thus the quotient does not manufacture descent; it identifies the exact finite state space on
which zero-drift recycling occurs.

## GC2cv -- exact cycle erasure and canonical recycling address -- PROVED

In one fixed signature-Markov epoch, if

`(u_i,chi_i)=(u_j,chi_j)`

for `i<j`, then the intervening tagged-only segment is quotient-erasable: start directly from
the repeated quotient state at time `i` and replay the suffix beginning after time `j`.

Consequently:

1. a shortest tagged-only history to a prescribed terminal output has fewer than `N_tag`
   nonterminal quotient states;
2. every history with at least `N_tag` transitions contains a repeated quotient state;
3. choosing the earliest-ending repeat and latest preceding copy gives a simple recycling word
   of length at most `N_tag`;
4. after canonical rotation, all recycling words lie in a finite safe address stock, for example

   `C_tag=sum_(ell=1)^N_tag N_tag^ell`.

### Proof

At the two equal quotient states, the signature-Markov contract supplies exactly the same
future legal actions and terminal tests.  The suffix therefore replays verbatim.  The remaining
claims are finite-state pigeonhole, shortest-path simplicity and canonical rotation of a finite
closed word. QED.

Named lineages inside the erased segment may differ, but every destroyed old lineage has already
been retired and paid.  Future behavior sees only the active successor multiplicities.

## GC2cw -- tagged-only recycling closure -- PROVED UNDER THE SIGNATURE-RECYCLING CONTRACT

Assume inside one fixed tagged-only epoch:

1. the physical signature universe, capacities, weights and finite context alphabet are fixed;
2. every active-lineage continuation is signature-Markov;
3. each canonical recycling address from GC2cv is quotient-stuttering, strictly descending in a
   declared well-founded rank, or consumes one ticket from a finite exact address stock;
4. any change of capacities, weights, signature semantics, untagged background or identity-
   sensitive future rule is an outer reset.

Then no tagged-only recycling branch can sustain an infinite nonterminal internal history.  After
quotient erasure and removal of descending or ticketed cycles, every remaining acyclic segment
has at most `N_tag-1` transitions.

### Proof

Apply GC2cv whenever a quotient state repeats.  A repeated cycle erases, descends or spends a
finite ticket.  Infinite continuation would require infinitely many well-founded descents or
ticket expenditures.  If no state repeats, the path has length at most `N_tag-1`.  Forbidden
data changes leave the epoch. QED.

## Corrected GC frontier

Tagged-only lineage recycling is no longer a free temporal obstruction when active lineage
names quotient to fixed physical signature capacities.  The live exceptions are now:

- identity-sensitive or age-sensitive future rules;
- unbounded physical multiplicities or a changing signature universe;
- changing weights or capacities not recorded as outer resets;
- or unticketed recurrence in the finite quotient.

The other geometric-cleaning interfaces remain final execution of compatible paid current-star
banks, labelled paid-overload recursion, high created-pair multiplicity, isolated-cell
prospective stars, pool depletion, global context causes and local superregular resampling.

## Finite check

`scripts/verify_geometric_tagged_lineage_signature_quotient.py` exhausts small capacity vectors,
checks the exact product state stock and samples named lineage histories.  It verifies rename
invariance, fresh names on signature recreation, unique lineage retirement, quotient updates,
zero tagged-energy drift and repeated-state cycle erasure.