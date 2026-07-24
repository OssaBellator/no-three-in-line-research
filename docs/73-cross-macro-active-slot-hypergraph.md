# Cross-macro active slot hypergraph

Once macro slots have dense domains, cross-macro patch events automatically have
small probability.  The remaining support-compression requirement is exactly a
maximum-degree bound in the hypergraph of slot pairs and triples that can realize
a collinear patch pattern.

## 1. Active cross-slot events

Consider distinct macro pools with disjoint new-coordinate labels and slot
domains of size at least `gamma R`.

A pair of slots `s,t` is **cross-active** if some choices of their source edges
create a triple using both movement/refill points from one slot and one point
from the other.  Make one event `P_{s,t}^{cross}` for the union of both
orientations.

A triple of slots `s,t,u` from at least two macro pools is **cross-active** if
some pairwise-distinct source-edge choices create a collinear triple using one
movement/refill point from each slot.  Make one event
`T_{s,t,u}^{cross}`.

Inactive slot sets create no geometric restriction and are omitted.

## 2. Universal probability bounds

### Proposition PP3eo -- PROVED

For dense domains as above,

\[
 \Pr(P_{s,t}^{\rm cross})
 \le
 \frac4{\gamma R}
 \le
 \frac4{\gamma^2R},
\]

and

\[
 \Pr(T_{s,t,u}^{\rm cross})
 \le
 \frac8{\gamma R}
 \le
 \frac8{\gamma^2R}.
\]

#### Proof

For one orientation of a pair event, condition on the source edge controlling
the movement/refill pair.  Its joining line meets the other slot's movement
support in at most one old column and its refill support in at most one old row.
At most two values in the other domain complete the event, giving
`2/(gamma R)`.  Sum the two orientations.

For a three-slot event, condition on the first two source-edge values.  For each
of the eight movement/refill type choices, their two points determine a line,
and the required third support line prescribes at most one old column or row.
Thus at most eight values in the third domain complete the event. ∎

No global count of candidate triples is needed for these probability estimates.

## 3. Active-degree endpoint

For a slot `s`, let

\[
 d_{\rm cross}(s)
\]

be the number of active cross-slot pair and triple events containing `s`.
Include ordinary fixed-anchor pair events from PP3em in a separate count
`d_anchor(s)` after verifying their completion codegree.

### Theorem PP3ep -- PROVED

Assume:

1. unary source conflicts have been removed by fully safe domains PP3el;
2. ordinary anchor events satisfy the probability bound
   `8/(gamma^2R)`;
3. every slot satisfies

\[
 \boxed{
 d_{\rm cross}(s)+d_{\rm anchor}(s)
 \le
 \frac{7\gamma^2R}{1152}+O(1).
 }
\]

Then one simultaneous assignment of every macro slot is:

- injective inside each source pool;
- internally no-three in every macro;
- clean against the fixed source sets;
- free of every cross-macro patch triple.

#### Proof

The internal event occurrence is at most `gamma^2R/128` by PP3ej.  The added
occurrence bound keeps the total below the PP3ei threshold
`(gamma^2R+48)/72`.  Proposition PP3eo and the anchor hypothesis give the
required event probability.  Apply PP3ei. ∎

The conditional output distribution retains the cylinder spread PP3ek.

## 4. Exact support-compression target

The complete unpruned slot system has about `MW` slots, so one slot could belong
to `Theta((MW)^2)` active triples.  PP3ep requires only `O(R)`.
At the balanced exponents

\[
 M=m^{23/80},
 \qquad
 W=m^{19/80},
 \qquad
 R=m^{38/80},
\]

one has

\[
 (MW)^2=m^{84/80},
 \qquad
 R=m^{38/80}.
\]

Therefore genuine geometry must remove almost all formal slot triples; merely
correlating their edge choices cannot suffice.

The remaining cross-macro theorem is now precise:

> arrange new-coordinate labels, pool endpoint sets, or protected trades so that
> the active slot pair/triple hypergraph has maximum degree `O(R)` with a constant
> smaller than the PP3ep budget.

Failure produces a slot with `Omega(R)` distinct geometrically realizable cross
patterns.  Such a slot is an explicit secant-star or pair-shadow core rather
than a diffuse global triple population.