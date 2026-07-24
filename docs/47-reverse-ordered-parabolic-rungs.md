# Reverse-ordered parabolic rung separation

The multistate endpoint PP3bi reduces compatibility to a rank-at-most-three
CSP.  This chapter removes every cross-rung triple that repeats one geometric
component.  Only triples using three distinct movement/refill components
remain, and rank-three clauses can arise only from three distinct rungs.

## 1. Ordered component rectangles

For `i=1,...,K`, let

\[
 M_i\subseteq C_i\times N_i,
 \qquad
 F_i\subseteq N_i\times Y_i,
\]

where `C_i,Y_i` are old-coordinate blocks and `N_i` is a new-coordinate
interval.  Assume:

1. the old blocks are increasingly ordered:

\[
 \max C_i<\min C_j,
 \qquad
 \max Y_i<\min Y_j
 \quad(i<j);
\]

2. the new intervals are reverse ordered:

\[
 \min N_i>\max N_j
 \quad(i<j);
\]

3. every nonaxis secant internal to one `M_i` or one `F_i` has positive slope;
4. each `M_i` and `F_i` is no-three-in-line.

The sheared parabolic components from PP3aq satisfy conditions 3 and 4.

### Proposition PP3bm -- PROVED

Under these hypotheses:

1. every secant joining distinct movement components `M_i,M_j` has negative
   slope;
2. every secant joining distinct refill components `F_i,F_j` has negative
   slope;
3. every secant joining a movement component to a refill component has negative
   slope;
4. no collinear triple in

\[
 Q=\bigcup_i(M_i\cup F_i)
\]

contains two points from one component `M_i` or `F_i` and a third point outside
that component.

#### Proof

Take `i<j`.  A point of `M_i` has smaller first coordinate and larger second
coordinate than a point of `M_j`, so their joining line has negative slope.
For `F_i,F_j`, the first coordinate lies in the reverse-ordered new intervals
while the second lies in the increasingly ordered old row blocks; again the
slope is negative.

A movement point lies in an old column and a new row, while a refill point lies
in a new column and an old row.  Moving from the former to the latter increases
the first coordinate and decreases the second, so every movement--refill
secant has negative slope.

Two points inside one component determine either a positive-slope line or an
axis-parallel line.  A line from either point to any point outside the component
has negative slope by the preceding cases.  Hence the three points cannot be
collinear. ∎

The conclusion is stronger than pairwise no-three of the rungs.  It rules out
all `2+1` component patterns simultaneously.

## 2. Clause-rank consequence

Suppose each rung `i` is represented by one finite-state variable controlling
both `M_i` and `F_i`.  Assume every complete state of one rung is internally
no-three, as in PP3ae.

### Corollary PP3bn -- PROVED

Every collinear triple contained in the union of all rung supports and selected
by some assignment uses three distinct movement/refill components.
Consequently:

- a triple involving one rung is impossible;
- a triple involving two rungs gives a bad box of rank at most two;
- a bad box of rank three must use three distinct rungs.

#### Proof

PP3bm excludes a triple containing two points from one component.  Thus all
three points lie in distinct components.  A complete single-rung state is
internally no-three, so the three components cannot all belong to one rung.
The number of distinct rung variables met by the triple is therefore two or
three, with rank three possible only in the latter case. ∎

In particular, any reverse-ordered bank of at most two rungs has no internal
rank-three clause.  Its remaining internal compatibility is exactly a rank-two
CSP, before retained-core and auxiliary-trade certificates are added.

## 3. Deterministic three-component triple cap

### Proposition PP3bo -- PROVED

Let `A,B,C` be no-three-in-line point sets.  The number of collinear triples
with one point in each set is at most

\[
 \boxed{
 2\min\{|A||B|,|A||C|,|B||C|\}.
 }
\]

#### Proof

Fix a pair `(a,b) in A x B`.  Its line contains at most two points of `C`,
because three points of `C` on that line would contradict the no-three property
of `C`.  Hence there are at most `2|A||B|` triples.  The other two bounds follow
by symmetry. ∎

If every movement/refill component has `2t` points, then one triple of distinct
components contributes at most `8t^2` collinear triples.  Across `K` equal-width
rungs there are `2K` components, so the complete internal cross-component
triple population is at most

\[
 8t^2\binom{2K}{3}=O(K^3t^2).
\]

Writing total extension width as `T=Kt`, this is `O(KT^2)`, rather than the
naive `O(T^3)` point-triple count.

For the published prime-gap target `K=m^{0.05}` and `T=m^{0.525}`, this cap is
`O(m^{1.10})`.  It is not by itself small enough for completion, but it
identifies the exact population on which the multistate probabilities from
PP3bj--PP3bl must act.

## 4. Revised geometric target

The reverse ordering removes all repeated-component clauses without consuming
extra state entropy.  The remaining preparation problem is now:

1. install matching-admissible multistate rungs in reverse old/new order;
2. control the rank-two retained-core and two-rung bad boxes;
3. prove that the `O(KT^2)` three-rung boxes have sufficiently small product
   probability or bounded occurrence for PP3bj, PP3bk, or PP3bl;
4. add protected rectangle or tomographic variables without creating a large
   new rank-three population.