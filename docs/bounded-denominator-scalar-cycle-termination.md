# Scalar-edge forests and denominator-cycle termination

**Branch:** `research/bounded-denominator-absorbers`

The remaining BDA6 transition problem contains several different kinds of
profile changes.  This note closes the part generated only by genuine adjacent
physical scales and strict effective-denominator descent.  For one exact
profile and anchor, the physical scale graph is a subgraph of an integer path.
Capacity-one unordered adjacent-support tickets therefore eliminate every
same-denominator closed walk.  Strict divisor descent is bounded by the
prime-factor height of the initial denominator.

## Exact scale graph

Fix an exact ordinary or separately occurrence-faithful reflected profile with
physical denominator `q`, one anchor `P`, and represented positive scales
`H_P`.  Form the undirected graph

\[
G(P,q)
\]

with vertex set `H_P` and one edge

\[
\{h,h+q\}
\]

whenever both scales are represented and the corresponding adjacent-support
address is eligible for a transition.

The address retains the anchor, unordered scale pair, denominator, primitive
directions, role scalars and every finite decoder decoration.

## BDA5as -- the physical adjacent-scale graph is a forest -- PROVED

Every connected component of `G(P,q)` is a path.  In particular, `G(P,q)` is a
forest.

The same statement holds for an interlaced scalar-slot profile.  Although the
slot-index gap may be `g=gcd(delta,q)` or `g_A=gcd(2A,q)`, the corresponding
physical scales still differ by exactly `q`.

### Proof

All represented scales in one exact profile lie in one residue class modulo
the relevant primitive slot spacing.  A physical adjacent-pair edge joins the
two integers `h` and `h+q`.  Order the vertices by their integer value.  Each
vertex has at most one neighbour below it and at most one neighbour above it.
A finite graph with this order and only consecutive fixed-gap edges is a
disjoint union of paths. QED.

## BDA5at -- capacity-one adjacent tickets forbid scalar cycles -- PROVED

Give every unordered edge address of every graph `G(P,q)` capacity one.

Any nonempty closed walk using only physical adjacent-scale transitions
traverses some unordered edge at least twice.  Therefore no such walk is
admissible when every traversal consumes the corresponding capacity-one
ticket.

### Proof

A forest contains no nonempty closed trail.  Hence a closed walk in a forest
must repeat an edge.  The first traversal consumes its unique ticket, so the
second traversal is unavailable. QED.

This rules out not only the immediate backtrack `h -> h+q -> h`, but every
longer scalar walk such as

\[
h\to h+q\to h+2q\to h+q\to h.
\]

## Strict denominator descent

Let `q_0` be the denominator at the beginning of one BDA descent epoch.
Every effective denominator encountered is a positive divisor of `q_0`.
Write

\[
\Omega_{\rm pf}(q)
\]

for the number of prime factors of `q`, counted with multiplicity.

A strict effective-denominator descent `q' proper-divides q` satisfies

\[
\Omega_{\rm pf}(q')\le \Omega_{\rm pf}(q)-1.
\]

Let `R` be the total number of capacity-one adjacent-support tickets in the
finite epoch universe, over every represented anchor, divisor profile and
physical scale edge.  Let `c` be the number already consumed.

## BDA5au -- combined denominator/ticket potential -- PROVED

For a trajectory whose nonterminal steps are only:

1. a strict effective-denominator descent; or
2. a physical adjacent-scale transition consuming a previously unused edge
   ticket,

the integer potential

\[
\boxed{
\Xi_{\rm scal}
=
(R+1)\bigl(\Omega_{\rm pf}(q_0)-\Omega_{\rm pf}(q)\bigr)+c
}
\]

strictly increases at every step and satisfies

\[
0\le \Xi_{\rm scal}
\le
(R+1)\Omega_{\rm pf}(q_0)+R.
\]

Consequently such a trajectory terminates after at most

\[
\boxed{
(R+1)\Omega_{\rm pf}(q_0)+R
}
\]

nonterminal steps and contains no directed cycle.

### Proof

A new adjacent-scale traversal increases `c` by one.  A strict divisor descent
increases the prime-factor deficit by at least one, hence raises the first
term by at least `R+1`; the ticket count never decreases.  The denominator
deficit is at most `Omega_pf(q_0)` and at most `R` tickets can be consumed.
QED.

## Consequence for BDA6

Every directed BDA transition cycle must contain an edge outside the two
classes closed here.  In particular, a surviving cycle must change at least
one of:

- the primitive direction or projective slope;
- the scalar residue or reduced unit without strict denominator descent;
- the current/new rank or channel word;
- the anchor/context role;
- the realized bank type or external carry/RI label.

Pure scale wandering and pure denominator descent are no longer BDA6
obstructions.

The theorem applies to raw reflected `CD` arithmetic only for its strict
effective-denominator descents.  A raw reflected `CD` scalar pair is not a
radial support edge unless a separate physical radial occurrence has been
proved.

## Finite check

`scripts/verify_bda_scalar_cycle_termination.py` exhausts finite scale subsets,
their fixed-gap edge graphs, every walk through the bounded model, strict
divisor chains, prime-factor heights and all transition inequalities for
`Xi_scal`.
