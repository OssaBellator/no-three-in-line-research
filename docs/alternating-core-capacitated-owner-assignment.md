# Canonical capacitated owner assignment

**Branch:** `research/alternating-core-chain`

AC3nh leaves capacities that have not been expanded into named capacity-one units as
live owner-assignment data.  Named cloning is unnecessary when the owner theorem
supplies an exact integer capacity: the assignment problem is a bipartite
`b`-matching with unit demand capacities and integral owner capacities.  A fixed
lexicographic rule reconstructs one maximum assignment, capacitated Hall failure
returns one canonical deficient core, and persistent unit consumption has a bounded
integer potential.

This note concerns **private additive capacity**.  Assigning two demands to an owner
of residual capacity two means that two units of that owner's declared resource are
available and, on an accepted consuming transition, are charged separately.  A
shared owner whose one payment is counted once for several alternatives remains an
AC3w common-owner object and is not converted into additive capacity by this note.
Eligibility still does not imply payment: every selected edge must separately pass
the AC3ke--AC3kf current, physical, coherent, payable and faithful-destruction
checks.

## Capacitated demand--owner graph

Fix finite totally ordered sets

\[
D=\{d_1,\ldots,d_s\},
\qquad
T=\{t_1,\ldots,t_m\},
\]

an eligibility graph

\[
E\subseteq D\times T,
\]

and integer owner capacities

\[
b:T\to\mathbb Z_{\ge0}.
\]

Let `f(t)` be the persistent number of already spent units, with
`0<=f(t)<=b(t)`, and put

\[
c(t)=b(t)-f(t).
\]

A partial capacitated assignment is a set `M subseteq E` satisfying

\[
\deg_M(d)\le1\quad(d\in D),
\qquad
\deg_M(t)\le c(t)\quad(t\in T).
\]

Encode it by the owner index assigned to each ordered demand, with the sentinel
`m+1` for an unmatched demand.  First maximize the number of matched demands and
then choose the lexicographically least encoding.

## AC3ni -- canonical maximum capacitated assignment -- PROVED

There is one unique canonical assignment

\[
\boxed{M_b^*(D,T,E,b,f)}
\]

obtained as the lexicographically least maximum capacitated assignment.  Its
selected private subbank is the set of owners of positive degree in `M_b^*`.
Consequently:

1. the exact demand set, owner set, eligibility graph, capacity vector, spent vector
   and fixed orders determine one selected private subbank and assignment;
2. if any capacitated assignment saturates every demand, `M_b^*` saturates every
   demand;
3. otherwise `M_b^*` has maximum possible demand coverage;
4. unnamed capacity units need not be introduced merely to select an assignment.

### Proof

The empty assignment is feasible, so the finite feasible family is nonempty.
Maximum cardinality is defined, and the finite maximum family has one
lexicographically least encoding.  A maximum assignment saturates `D` exactly when
some feasible assignment does.  Its positive-degree owner set is determined by the
assignment. QED.

The theorem is a reconstruction statement, not a claim that all capacity vectors
have polynomially many possible values.  Any outer-profile bound must separately
bound the declared capacities or the total capacity.

## AC3nj -- unit-atom rank sensitivity -- PROVED

Write

\[
\nu_b(E,c)=|M_b^*(D,T,E,b,f)|.
\]

Each of the following atomic updates changes `nu_b` by at most one:

1. adding or deleting one eligibility edge;
2. increasing or decreasing one residual owner capacity `c(t)` by one;
3. adding or deleting one demand.

The exact canonical assignment can nevertheless rotate on many edges after one
atomic update.  Thus the safe statement is

\[
\boxed{|\nu_b-\nu_b'|\le1,}
\]

not a constant symmetric-difference bound for the canonical assignments.

For fixed demand and owner universes, every strict atomic input change has a least
decoration of one of the forms

\[
(d,t,+),\ (d,t,-),\ (t,+),\ (t,-),\ (d,+),\ (d,-).
\]

Hence the assignment-reset alphabet satisfies

\[
\boxed{R_{b\text{-assign}}\le2(sm+m+s).}
\]

A weighted family of atomic assignment resets of total weight `W` contains one
exact decoration class of weight at least

\[
\boxed{W/R_{b\text{-assign}}.}
\]

### Proof

Adding one eligibility edge can enlarge a feasible assignment by at most the one
new edge.  Deleting one edge removes at most one edge from an old optimum, leaving
a feasible assignment of size at least `nu_b-1`.  Increasing one owner capacity by
one permits at most one additional matched demand; decreasing it by one requires
deleting at most one incident assignment edge from an old optimum.  Adding or
deleting one unit-capacity demand has the same bound.  Lexicographic tie-breaking
may choose a different augmenting path or alternating cycle and therefore may
rotate many edges without changing rank by more than one.  The finite decoration
count and weighted pigeonhole conclusion are immediate. QED.

A capacity jump of size greater than one is either recorded with its exact amount or
decomposed into unit atoms before AC3nj is invoked.

## AC3nk -- canonical capacitated Hall core -- PROVED

A capacitated assignment saturating every demand exists if and only if

\[
\boxed{
|X|\le \sum_{t\in N_E(X)}c(t)
\quad\text{for every }X\subseteq D.
}
\]

If `M_b^*` does not saturate every demand, choose first an inclusion-minimal set
`X subseteq D` violating the displayed inequality, then the lexicographically least
one among those of minimum cardinality.  This gives one canonical capacitated Hall
core

\[
\boxed{X_b^*(D,T,E,b,f)}
\]

with positive integer deficiency

\[
\boxed{
\delta_b(X_b^*)
=
|X_b^*|-\sum_{t\in N_E(X_b^*)}c(t)
\ge1.
}
\]

### Proof

Replace each owner `t` by `c(t)` formal copies having the same demand
neighbourhood.  A matching saturating all original demands in the copied graph is
exactly a capacitated assignment saturating all demands.  Hall's theorem in the
copied graph says that every demand set `X` must see at least `|X|` owner copies.
The number of copies in its neighbourhood is exactly
`sum_{t in N_E(X)} c(t)`, proving the criterion.  On failure, the finite family of
deficient demand sets has an inclusion-minimal member and the fixed orders select
one canonically. QED.

The copied graph is used only in the proof.  The theorem does not create physical
capacity-one tickets or duplicate a shared payment owner.

## AC3nl -- persistent capacitated consumption has a linear potential -- PROVED

Fix `D,T,E,b` inside one owner epoch.  Suppose the spent vectors form a coordinatewise
monotone history

\[
f_0\le f_1\le\cdots\le b,
\]

and every accepted consuming transition charges at least one unit assigned by the
current canonical assignment:

\[
\sum_{t:\deg_{M_i^*}(t)>0}
\bigl(f_{i+1}(t)-f_i(t)\bigr)
\ge1.
\]

Then the number of accepted consuming transitions is at most

\[
\boxed{
\sum_{t\in T}(b(t)-f_0(t)).
}
\]

The potential is

\[
\boxed{\Xi_{b\text{-cap}}=\sum_{t\in T}f(t).}
\]

It strictly increases on every accepted transition even when recomputation rotates
the canonical assignment among many owners.

### Proof

Every accepted transition increases the integer potential by at least one.  It is
bounded above by `sum_t b(t)`, so there are at most
`sum_t(b(t)-f_0(t))` strict increases.  Assignment rotation cannot restore spent
capacity or lower the potential. QED.

If a selected owner is only a fixed witness and no capacity is consumed, the step
must obtain payment or descent elsewhere.  If a spent coordinate decreases, the
history has left the persistent-capacity epoch and the decrease is an outer reset.

## AC3nm -- non-unit private-owner profile reduction -- PROVED UNDER THE ADDITIVE-CAPACITY CONTRACT

Assume an installed transition family declares:

- its exact ordered demand and owner sets;
- its complete demand--owner eligibility graph;
- exact nonnegative integer owner capacities and a persistent spent vector;
- the canonical policy AC3ni;
- additive private capacity, meaning one assigned demand consumes one declared
  capacity unit on an accepted consuming transition;
- the AC3ke status and faithful destruction or consumption contract for every
  selected edge.

Then:

1. the selected capacitated private subbank and assignment are reconstructed from
   `(D,T,E,b,f)` and are not independent AC3ka profile fields;
2. a complete canonical assignment supplies eligibility coverage, while payment is
   credited only on owner routes declared `PAID`;
3. assignment failure returns the canonical capacitated Hall core AC3nk;
4. one eligibility, demand or unit-capacity change receives the AC3nj reset
   decoration;
5. inside a persistent consuming epoch, accepted transitions terminate after
   AC3nl's total residual-capacity budget;
6. an assignment change with no changed input is impossible.

The following remain live:

- common owners whose one payment covers several alternatives;
- nonadditive or state-dependent capacities;
- arbitrary noncanonical selected subbanks;
- generators of the demand, eligibility or capacity data;
- owner-status and faithful-destruction changes;
- nonpersistent spent vectors;
- recurrent exact input resets outside a consuming epoch.

### Proof

AC3ni gives deterministic reconstruction and preserves complete-assignment
existence.  AC3nk gives the exact failure certificate.  AC3nj localizes every
atomic input change without asserting a false matching-distance bound.  AC3nl gives
the monotone consumption potential.  Payment remains restricted by
AC3ke--AC3kf, and the excluded objects are not determined by the additive
capacitated inputs. QED.

## Consequence

The non-unit **private additive** owner-assignment frontier is reduced to exact
finite input data, a canonical capacitated Hall core, atomic reset labels and a
bounded total-capacity ticket stock.  Recurrent owner edges that survive this note
must therefore expose a common/nonadditive owner, a generator or status reset, a
nonpersistent capacity reset, or a repeated exact macro edge requiring separate
payment, descent or impossibility.

## Finite check

`scripts/verify_ac_capacitated_owner_assignment.py` exhausts every bipartite graph
with at most three demands and three owners, every residual capacity vector with
entries at most two, all canonical maximum assignments, all capacitated Hall
inequalities, and every one-edge or one-unit-capacity rank update.  It also records
examples where one atomic input change rotates several canonical assignment edges
while the maximum rank changes by at most one.
