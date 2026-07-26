# Minimal weighted Hall cores and shared-resource fans

**Branch:** `research/geometric-cleaning`

GC2ag--GC2ak show that every declared weighted reopening system either pays
fractionally or returns an exact Hall-deficient event set.  This note extracts the
canonical internal structure of such a deficient set.

An inclusion-minimal weighted Hall core has no diffuse slack.  Every event demand
exceeds the capacity private to that event by at least the full core deficiency, and
all remaining uncovered demand is forced onto resources shared inside the core.
Splitting that uncovered demand among shared incidences produces one exact
resource--role fibre carrying a quantified fraction of the deficiency scale.

## Weighted event system

Let `J` be a finite totally ordered event family.  Event `j` has demand `a_j>0` and
eligible exact current resources `A_j`.  Resource `p` has capacity `c_p>=0`.

For `X subseteq J`, write

`a(X)=sum_(j in X)a_j`,

`N(X)=union_(j in X)A_j`,

and

`delta(X)=a(X)-sum_(p in N(X))c_p`.

A set is deficient when `delta(X)>0`.

## GC2al -- canonical inclusion-minimal weighted Hall core -- PROVED

If the weighted Hall inequalities fail, there is a unique canonical deficient core
`X*`: choose first an inclusion-minimal deficient event set, then the
lexicographically least one among those of minimum cardinality.

Its deficiency

`delta=delta(X*)`

is positive, while every proper subset of `X*` satisfies its weighted Hall
inequality.

### Proof

The deficient family is finite and nonempty.  It therefore has inclusion-minimal
members; minimum cardinality and the fixed order choose one uniquely.  Inclusion
minimality says every proper subset is nondeficient. QED.

## Private and shared resources

Fix the canonical core `X=X*`.  For `j in X`, define its core-private resources

`P_j=N(X)\N(X\{j})`.

Let

`P_priv=union_(j in X)P_j`

and

`P_sh=N(X)\P_priv`.

The sets `P_j` are pairwise disjoint.  Define the uncovered event demand

`u_j=a_j-sum_(p in P_j)c_p`.

## GC2am -- every core event carries the full deficiency after private capacity -- PROVED

For every `j in X`,

`u_j>=delta`.

Moreover

`U=sum_(j in X)u_j=sum_(p in P_sh)c_p+delta`

and hence

`sum_(p in P_sh)c_p>= (|X|-1)*delta`,

`U>=|X|*delta`.

If `|X|>=2`, every event has at least one shared eligible resource in `P_sh`.

### Proof

Minimality gives

`a(X\{j})<=sum_(p in N(X\{j}))c_p`.

Subtract this from

`a(X)=sum_(p in N(X))c_p+delta`.

The resources lost from the neighbourhood are exactly `P_j`, so

`a_j>=sum_(p in P_j)c_p+delta`,

which is `u_j>=delta`.

The private sets are disjoint, and `N(X)` is their union with `P_sh`.  Therefore

`U=a(X)-sum_(p in P_priv)c_p=sum_(p in P_sh)c_p+delta`.

Summing `u_j>=delta` gives `U>=|X|delta`, which yields the shared-capacity bound.
If `|X|>=2` and one event had no shared neighbour, its full neighbourhood would be
private, contradicting `u_j>=delta>0` together with the nondeficiency of the singleton
proper subset `{j}`. QED.

For `|X|=1`, the core is already one exact atomic demand/capacity overload.

## GC2an -- canonical shared-incidence weighting -- PROVED

Assume `|X|>=2`.  For each event let

`S_j=A_j intersect P_sh`,

which is nonempty by GC2am.  Split its uncovered demand equally across its shared
eligible resources:

`w_(j,p)=u_j/|S_j|` for `p in S_j`.

Then

`sum_(p in S_j)w_(j,p)=u_j`

for every event and

`sum_(j in X)sum_(p in S_j)w_(j,p)=U`.

Writing `M=|P_sh|`, one exact shared resource `p*` receives incidence weight at
least

`U/M >= |X|*delta/M`.

### Proof

The first two identities follow from equal splitting.  Pigeonhole the total incidence
weight `U` among the `M` shared resources and use GC2am. QED.

This incidence weight is a deficiency witness, not a claim that `p*` can pay all of
it.

## GC2ao -- shared-resource labelled-fan dichotomy -- PROVED

Label every incidence `(j,p)` by one of at most `T` geometric roles.  Fix an integer
`Gamma>=0` and put the full installation-conflict graph on the events using one
resource--role fibre.

There is an exact shared resource `p*` and one role `lambda` whose incidence fibre has
weight at least

`U/(M*T) >= |X|*delta/(M*T)`.

Inside that fibre one of the following holds:

1. one event conflicts with more than `Gamma` other events in the same
   resource--role fibre;
2. an installably compatible event family carries incidence weight at least

   `U/[M*T*(Gamma+1)] >= |X|*delta/[M*T*(Gamma+1)]`.

### Proof

Apply GC2an and pigeonhole the selected resource's incidence weight among at most `T`
roles.  If the induced conflict graph has maximum degree greater than `Gamma`, use
outcome 1.  Otherwise greedy colouring uses at most `Gamma+1` colours, and one colour
class carries at least the average weight. QED.

All events in the selected fibre request the same exact current resource in the same
geometric role.  The compatible family is therefore a concentrated Hall-deficiency
fan, not independently paid mass.

## GC2ap -- complete weighted-deficiency continuation -- PROVED

Whenever the normalized branch of GC2ak returns a weighted Hall failure, there is one
exact continuation:

1. a singleton core, hence one exact event whose demand exceeds the capacity of its
   complete eligible neighbourhood;
2. a same-resource, same-role installation-conflict overload;
3. or a compatible same-resource, same-role deficiency fan retaining at least

   `|X*|*delta/[M*T*(Gamma+1)]`

   of the canonical uncovered-incidence weight scale.

### Proof

Choose the canonical core by GC2al.  If it has one event, use outcome 1.  Otherwise
apply GC2ao. QED.

## Corrected GC frontier

Weighted Hall failure is now localized rather than merely certified.  A minimal core
forces:

- at least `delta` uncovered demand at every event after private capacity;
- shared capacity at least `(|X|-1)delta`;
- one exact shared-resource and role fibre carrying a quantified deficiency fan.

The remaining geometric work is to classify the same-resource compatible fan or its
second-order conflict overload, and to exploit high excess/capacity ratio families
from the other branch of GC2ak.

## Finite check

`scripts/verify_geometric_minimal_weighted_hall_core.py` exhausts small weighted event
systems and random rational/integer instances.  It checks canonical minimal cores,
private/shared decomposition, the `u_j>=delta` inequalities, exact total identities,
shared-incidence pigeonholing and the weighted labelled-fan bound.