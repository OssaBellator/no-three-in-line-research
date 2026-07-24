# Product-LLL square-root macro patch

A direct product-space local lemma removes the mixed triples left by PP3di.
This closes the internal geometry of a square-root macro patch on every matching
pool.

## 1. Independent slot model

Let `E` be an `R`-edge matching pool and let `S` contain `n=2W` labelled slots.
Fix balanced maps `alpha,beta:S->[W]`, each with fibre size two.  Independently
choose a uniform edge

\[
 X_s=(x_s,y_s)\in E
\]

for every slot.  Slot `s` produces

\[
 M_s=(x_s,m+\alpha(s)),
 \qquad
 F_s=(m+\beta(s),y_s).
\]

For each pair of slots, make one conflict event containing:

- equality of their selected source edges;
- a collinear triple using both points from one slot and one point from the other.

For each triple of slots, make one conflict event when one point from each slot
is collinear.  Avoiding every event makes the edge choices injective and the
entire inserted patch no-three-in-line.

## 2. Event bounds

### Proposition PP3dl -- PROVED

For distinct slots,

\[
 \Pr(P_{s,t})\le\frac5R,
 \qquad
 \Pr(T_{s,t,u})\le\frac8R.
\]

#### Proof

The equality probability is `1/R`.

Condition on the edge selected by slot `s`.  Its movement/refill pair determines
one line.  That line meets the movement support of slot `t` in at most one old
column and its refill support in at most one old row.  Since `E` is a matching,
at most two choices for `X_t` complete such a triple.  This contributes `2/R`;
interchanging the two slots contributes another `2/R`.

For three slots, choose one of the movement/refill points from each slot.  There
are eight type choices.  After two source edges are fixed, the required line
prescribes at most one old column or row for the third slot, and hence at most
one matching edge.  Each type has probability at most `1/R`. ∎

## 3. Dependency bound

Events are adjacent when their slot sets intersect.

### Proposition PP3dm -- PROVED

The maximum dependency degree is at most

\[
 D\le2n^2.
\]

#### Proof

A pair event meets exactly the pair and triple events containing at least one of
its two slots, at most `n^2` other events.  A triple event meets at most

\[
 \frac{3n^2-9n+6}{2}
\]

other events.  Both are at most `2n^2`. ∎

## 4. Universal internal macro patch

### Theorem PP3dn -- PROVED FROM THE STANDARD LOCAL LEMMA

If

\[
 \boxed{48n^2\le R,}
\]

then some slot assignment avoids all conflicts.  Deleting the `2W` selected
source edges and inserting the `4W` slot points gives a saturated internally
no-three patch of width `W` and net point gain `2W`.

#### Proof

Every event has probability at most `p=8/R`.  By PP3dm,

\[
 3p(D+1)
 \le
 3\frac8R\,2n^2
 =
 \frac{48n^2}{R}
 \le1.
\]

The symmetric local lemma yields an avoiding assignment.  Pair-event avoidance
makes the selected source edges distinct.  Any triple among the inserted points
uses either two slots or three slots, so it is excluded by the corresponding
event.

Every selected old column and row is restored once.  Balance of `alpha,beta`
gives two points on every new row and column, proving saturation. ∎

### Corollary PP3do -- PROVED

For sufficiently large `R`, one may take

\[
 \boxed{W=\left\lfloor\sqrt R/16\right\rfloor.}
\]

Thus every matching pool supports endpoint-adapted internally no-three geometry
of width `Theta(sqrt(R))`; monotone endpoint order is unnecessary.

## 5. Remaining distribution problem

PP3dn proves existence in the raw product space.  It does not yet prove that the
avoiding assignments have constant density or inherit `O(1/R)` fixed-rank
marginals.  The remaining local input is therefore a distribution theorem:
retain slot-edge spread while also excluding opposite-layer and cross-macro
certificates, either through a resampling/switching measure or through one
enlarged product-space local lemma.

At the PP3dh exponents,

\[
 M=m^{23/80+o(1)},\quad
 R=m^{19/40+o(1)},\quad
 W=m^{19/80+o(1)},
\]

and `MW=m^(21/40+o(1))`.  Matching availability, degree restoration, and all
internal patch geometry are now closed at the required prime-gap width.