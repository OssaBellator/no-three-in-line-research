# Repeated macro edges as simple decorated profile cycles

**Branch:** `research/alternating-core-chain`

AC3ka--AC3kd reduce global outer-profile churn to repeated exact decorated
macro edges.  Equality of one edge does not identify the intervening matching
history.  It does, however, force a return path in the finite outer-profile
graph.  Removing loops from that return path produces a simple decorated cycle
through the repeated edge.

This note records that exact reduction and the remaining cycle-level contract.
It does not declare a profile cycle progressive merely because its word is
finite.

## Decorated outer graph

Let `P_out` be the exact outer-profile set, with

\[
P=|\mathcal P_{\rm out}|.
\]

Let every directed reset edge carry one decoration from an alphabet of size at
most `R`.  Fix one repeated decorated edge

\[
e=(\alpha,\beta,\delta).
\]

Suppose it occurs `t>=2` times in chronological order.  Between two consecutive
occurrences, the projected outer-profile walk starts at `beta` immediately after
the first traversal and reaches `alpha` immediately before the next traversal.

## AC3kz -- repeated edge contains a simple decorated cycle -- PROVED

Between every consecutive pair of traversals of `e`, delete closed subwalks from
the projected `beta`-to-`alpha` walk until no vertex repeats.  The resulting
simple directed path, together with `e`, is a simple directed profile cycle
containing `e`.

Its length is between two and `P` directed edges.

### Proof

Chronology gives a directed walk from `beta` to `alpha`.  Whenever a vertex
repeats, delete the segment between its first and next occurrence.  The
remaining sequence is still a directed walk with the same endpoints.  Repeating
this operation terminates with a simple path.  Its internal vertices avoid both
endpoints and are distinct, so adjoining `alpha -> beta` gives a simple directed
cycle.  A simple cycle in a `P`-vertex graph has at most `P` edges. QED.

The deleted subwalks are not claimed to be irrelevant to payment.  The theorem
extracts one recurrence witness from each return episode; it does not erase the
physical history.

## Finite cycle-word stock

For `l` internal vertices on the simple return path, there are at most

\[
(P-2)_l
\]

ordered choices, where `(m)_l=m(m-1)...(m-l+1)`.  The return path has `l+1`
edges, each with at most `R` decorations.  Define

\[
\boxed{
N_{\rm cyc}(P,R)
=
\sum_{l=0}^{P-2}(P-2)_lR^{l+1}.
}
\]

The decoration of the fixed repeated edge `e` is already specified and is not
counted again.

## AC3la -- cycle-word concentration -- PROVED

The `t-1` consecutive return episodes of a repeated edge produce at most
`N_cyc(P,R)` simple decorated cycle words through `e`.  Hence one cycle word
occurs at least

\[
\boxed{
\left\lceil\frac{t-1}{N_{\rm cyc}(P,R)}\right\rceil
}
\]

times.

For weighted return episodes of total weight `W`, one exact cycle word carries
weight at least

\[
\boxed{
W/N_{\rm cyc}(P,R).
}
\]

### Proof

AC3kz associates each return episode with one simple decorated return path.
The displayed count bounds the possible path words.  Apply ordinary or weighted
pigeonhole. QED.

This stock is finite.  It is polynomial only under an additional bound on the
simple cycle length or on the relevant profile subgraph; the theorem does not
hide the factorial ordered-vertex term.

## Field-return localization

Write an outer profile as a tuple of exact fields

\[
\alpha=(\alpha_1,\ldots,\alpha_s).
\]

For the fixed edge `e`, let `i` be the least field changed by the edge.  Thus

\[
\alpha_i\ne\beta_i.
\]

On every return path from `beta` to `alpha`, let `f` be the first return edge
after which field `i` again equals `alpha_i`.  Retain:

- the field index `i`;
- the value word of field `i` from `beta_i` through its first return to
  `alpha_i`;
- the decorated macro edges on that prefix;
- the exact ticket, owner or arithmetic witnesses required by those edges.

## AC3lb -- every macro cycle has an exact first field return -- PROVED

Every simple decorated cycle through `e` contains the canonical first return of
its least changed field.  Its prefix has at most `P-1` return edges.

Consequently a recurrent macro cycle cannot consist solely of strict movement
in one bounded acyclic order on that field.  It must contain at least one of:

1. a reverse or sideways field transition;
2. an edge which leaves the field fixed while another outer field changes;
3. a terminal/payment edge;
4. a ticketed edge;
5. failure of the declared field order or occurrence chart.

### Proof

The return path ends at `alpha`, so field `i` eventually equals `alpha_i`.
Choose its first such occurrence.  The path is simple and has at most `P-1`
edges.  A strictly monotone walk in a bounded acyclic order cannot return to its
starting value, so some listed nonmonotone or external event must occur. QED.

For the current alternating-core dictionary, pure adjacent-scale and strict
denominator movement has already been removed by AC3hu--AC3hw.  A surviving
cycle must therefore use a same-denominator non-scalar arithmetic edge, owner
route change, base-host construction change, protected-contract change,
envelope change or another explicitly decorated outer field.

## Capacity-one cycle tickets

A simple decorated cycle word `gamma` is **cycle-progressive** when every
nonterminal realization of that complete cycle consumes one previously unused
ticket from a finite universe `T_cyc`, and no later alternating transition can
restore the ticket during the same closure attempt.

The ticket may name an exact arithmetic support, owner token, replacement
blocker, protected contract, envelope witness, parent/payment record or another
proved capacity-one object.  Equality of the profile cycle word alone is not a
ticket.

## AC3lc -- conditional cycle-level closure -- PROVED UNDER THE CYCLE-TICKET CONTRACT

Assume every recurrent simple decorated macro cycle satisfies at least one of:

1. some edge returns an improving state, accepted arithmetic chamber, paid menu
   or terminal literal/resource profile;
2. completing the cycle strictly increases a separately bounded integer
   potential;
3. completing the cycle consumes a previously unused capacity-one cycle ticket;
4. the cycle cannot be physically realized under its retained occurrence and
   coherence decorations.

Then repeated decorated macro edges cannot support an infinite nonterminal
history.

If the cycle-ticket universe has size `Q_cyc`, at most `Q_cyc` cycle
realizations can use alternative 3.  Combining this with AC3kb and the bounded
potentials in alternative 2 gives a finite global AC4 counter.

### Proof

AC3kz turns every repeated edge return into a simple decorated cycle.  Outcomes
1 and 4 terminate that recurrence.  Outcome 2 strictly advances a bounded
potential.  Outcome 3 consumes an unrestorable ticket and can occur at most
`Q_cyc` times.  Therefore no cycle word recurs indefinitely.  AC3kb already
bounds histories before a repeated edge appears, so the complete history is
finite. QED.

## Consequence

The global recurrence frontier is now cycle-local rather than edge-local.  For
each recurrent cycle word it is enough to prove one current payment, bounded
field descent, capacity-one cycle ticket or physical impossibility.  The least
changed field and its first-return prefix identify the exact theorem which must
supply that progress.

## Finite check

`scripts/verify_ac_macro_cycle_router.py` exhausts directed profile walks on
small finite graphs, extracts simple return paths through repeated edges,
checks the cycle-word count, verifies first field returns, and checks the
cycle-ticket potential.