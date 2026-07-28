# Capacity-one matching and tickets for bounded donor reservoirs

**Branch:** `research/geometric-cleaning`

GC2fp--GC2fy isolate a bounded-budget branch `p<=D_phys` in which a heavy
lineage has only a small donor reservoir.  GC2fz--GC2gd handle one shared
removable blocker across a full donor fan.  This note prevents the remaining
small reservoir from being discarded: it is either fully assigned, returns a
canonical Hall core, or spends a finite donor ticket.

## Small-reservoir system

Fix a weighted target family `T` and a physical donor reservoir `P` with

\[
|P|=p\le D_{\rm phys}.
\]

Let `G subseteq T x P` contain exactly the donor assignments satisfying every
current rectangle, collision, line, layer and protected-height test.  Each edge
retains its least blocker/cause decoration.

Assume the **capacity-one donor contract**:

1. one physical donor occurrence serves at most one selected target at a time;
2. a consuming donor assignment spends the ticket `(t,p,lambda)`;
3. restoration of a spent donor has an occurrence-faithful source or blocker
   removal lineage;
4. changed legality, target, donor, role or context is a reset.

## GC2ge -- canonical maximum donor assignment -- PROVED

The lexicographically least maximum matching `M(G)` is a canonical selected
donor assignment.  Exactly one of the following holds:

1. every target is matched;
2. there is a canonical nonempty Hall core `X subseteq T` with

   \[
   |N_G(X)|<|X|.
   \]

### Proof

Finite bipartite matching gives a maximum matching.  Fixing the branch orders
makes the least maximum matching canonical.  It saturates `T` exactly when
Hall's inequalities hold.  Otherwise choose the least deficient target set,
first by size and then lexicographically. QED.

## GC2gf -- bounded reservoirs have an exact ticket stock -- PROVED

The complete donor-assignment ticket stock is at most

\[
\boxed{|E(G)|\le |T|p\le |T|D_{\rm phys}.}
\]

If only one target lineage is active, the stock is at most `p`.

### Proof

A ticket is addressed by one legal target--donor edge and its already fixed
least-cause decoration.  The complete bipartite ambient graph has `|T|p` edges.
QED.

## GC2gg -- persistent consuming epochs terminate or reopen a Hall edge --
PROVED UNDER THE CAPACITY-ONE CONTRACT

Inside one fixed legality epoch, repeated fully matched donor executions either

1. consume a previously unused donor-assignment ticket;
2. strictly reduce the unresolved target set;
3. restore a donor through a named physical source/removal lineage; or
4. change the graph and reset the epoch.

Thus source-free, reset-free executions are bounded by `|E(G)|`.

### Proof

Use the canonical matching from GC2ge.  Every nonempty execution consumes at
least one selected edge ticket or removes its matched target from the unresolved
set.  A previously spent edge can reappear only by restoring its physical donor
and legality, which is route 3 or a reset.  Capacity one and GC2gf give the
bound. QED.

## GC2gh -- Hall failure retains the concentrated witness -- PROVED

If the bounded reservoir cannot saturate `T`, the canonical Hall core `X`
retains all of the following exact data:

1. its target weight and cardinality;
2. the donor set `N_G(X)` of size below `|X|`;
3. every least blocker/cause on the missing cut edges;
4. the deficiency

   \[
   d(X)=|X|-|N_G(X)|\ge1.
   \]

Consequently the small-reservoir branch returns an atomic donor shortage,
same-blocker overload, target-common/global cause, or one of the existing
least-blocker concentration outputs; it does not return an unlabelled failure.

### Proof

The graph was defined after all legality tests and every absent edge retained
its least cause.  Hall deficiency supplies the exact target and available-donor
sets.  Pigeonholing the missing cut edges over their retained causes gives one
of the named cause fibres. QED.

## GC2gi -- bounded donor-reservoir router -- PROVED UNDER THE DECLARED
CONTRACTS

Every `p<=D_phys` donor reservoir now has one continuation:

1. a canonical full donor assignment;
2. finite capacity-one donor tickets and target-count descent;
3. an occurrence-faithful donor restoration/removal gate;
4. a canonical Hall-deficient target/cause core;
5. or an explicit legality/context reset.

This closes the bounded-budget branch as a finite matching problem.  GC5 remains
open for target-common/global blockers without executable removal, unbounded or
replenishable donor sources, non-tagged feedback, and preservation of the
dyadic clean-height invariant through the chosen transitions.

## Finite check

`scripts/verify_gc_small_reservoir_matching.py` exhausts all bipartite graphs up
to `3 x 3` and a structured sample through `4 x 4`.  It verifies the canonical
maximum-matching/full-Hall dichotomy and records the finite target--donor ticket
stock.
