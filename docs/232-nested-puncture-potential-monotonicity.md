# Nested puncture potentials eliminate paid reserve histories

PP3akk--PP3akp treated successive controller punctures by fixed-universe epochs and
left reserve exhaustion as a possible endpoint.  The active candidate universes
are, however, nested.  Puncturing a controller value removes candidate entries; it
does not alter whether a blocker pair is noncontroller for any surviving entry.
The controller-shadow potentials for successive universes are therefore directly
comparable.

This gives a global monotonicity theorem.  Enlarge the puncture set, then perform a
strict paid trade for the smaller candidate universe.  The puncture itself cannot
increase the potential, and the paid trade decreases it by at least one.  Thus the
whole puncture-plus-trade operation decreases a single chronological sequence of
nonnegative integers.

Consequently a `Theta(R)` puncture history is impossible when every puncture is
followed by the paid conversion PP3akh, or by any other strict paid conversion for
the new active universe.  The history signatures of PP3apf--PP3apl remain relevant
only for branches that repeatedly leave the monotone interface.

## 1. Nested candidate universes

Fix the original disjoint controller pools

```text
E_1,...,E_M.
```

For a puncture set

```text
X subseteq E_1 union ... union E_M,
```

let

```text
V_X
```

be the typed movement/refill candidate-entry universe whose controller belongs to
`E\X`.  For a saturated source `S` containing every active controller in `E\X`,
define

```text
Psi_X(S)
```

by the controller-shadow formula PP3ij, restricted to entries in `V_X`.

### Proposition PP3apm -- PROVED

If

```text
X subseteq Y,
```

then

```text
V_Y subseteq V_X
```

and, for every source `S` containing all controllers in `E\Y`,

```text
Psi_Y(S) <= Psi_X(S).
```

The right-hand potential is interpreted using the same source `S`; it is well
defined even when some controllers in `Y\X` have already been removed from the
source, because `Psi_X` is simply the sum of the fixed entry weights

```text
w_(V_X)(p,q)
```

over source pairs.

#### Proof

Puncturing more controller values deletes every candidate entry controlled by one
of those values and changes no surviving candidate cell or controlling edge.
Hence `V_Y subseteq V_X`.

For one source pair `{p,q}`, its contribution is the number of entries in the
chosen universe whose candidate cell is collinear with `p,q` and whose controller
is neither endpoint.  Restricting the entry universe can only decrease that
number.  Sum over source pairs. ∎

The phrase **noncontroller blocker pair** is entry-relative: it means that the
entry's controlling edge is not the blocker pair.  It does not mean that neither
blocker endpoint belongs to some controller pool.  Thus puncturing a point does
not create a blocker reclassification term for surviving entries.

## 2. One puncture followed by one paid trade

Let `X` be the current puncture set and let

```text
p in E\X.
```

Put

```text
Y=X union {p}.
```

Let `S` be the current source.  After puncturing `p`, perform a source-admissible
trade in the fixed universe `V_Y`, producing `S'`, preserving every controller in
`E\Y`, and satisfying

```text
Psi_Y(S') <= Psi_Y(S)-1.
```

### Theorem PP3apn -- PROVED

The complete puncture-plus-paid-trade operation satisfies

```text
Psi_Y(S') < Psi_X(S).
```

More quantitatively, if the paid trade decreases `Psi_Y` by at least `c>=1`, then

```text
Psi_Y(S') <= Psi_X(S)-c.
```

#### Proof

By PP3apm,

```text
Psi_Y(S) <= Psi_X(S).
```

The strict paid hypothesis gives

```text
Psi_Y(S') <= Psi_Y(S)-c.
```

Combine the two inequalities. ∎

No comparison of insertion and removal terms across different universes is
needed.  The dynamic identity is used only after the puncture, in the fixed
smaller universe where PP3akh applies.

## 3. Arbitrary nested paid histories

Consider source states and puncture sets

```text
(X_0,S_0),(X_1,S_1),...,(X_t,S_t)
```

such that

```text
X_0 subseteq X_1 subseteq ... subseteq X_t.
```

At stage `j`, first enlarge `X_j` to `X_(j+1)` without changing the source, and
then perform one or more source-admissible trades preserving every controller in
`E\X_(j+1)`.  Assume their combined change in the fixed new universe is strict:

```text
Psi_(X_(j+1))(S_(j+1))
<=
Psi_(X_(j+1))(S_j)-1.
```

### Theorem PP3apo -- PROVED

The chronological values

```text
P_j=Psi_(X_j)(S_j)
```

form a strictly decreasing sequence of nonnegative integers.  Hence

```text
t <= P_0.
```

In particular no infinite sequence of successful paid puncture stages exists,
and no positive puncture reserve can be exhausted by such stages without first
reaching a nonpaid endpoint.

#### Proof

For every `j`, Proposition PP3apm gives

```text
Psi_(X_(j+1))(S_j) <= Psi_(X_j)(S_j)=P_j.
```

The strict paid stage then gives

```text
P_(j+1)
=
Psi_(X_(j+1))(S_(j+1))
<
P_j.
```

Each `P_j` is a nonnegative integer by PP3ij. ∎

The same proof permits several controller values to be punctured at one stage and
permits any finite package of endpoint, rectangle, cycle, or tomographic trades,
provided the package strictly decreases the potential for the final active
universe.

## 4. Application to captive source stars

Suppose `p` is a captive source-star centre.  PP3akg shows that all designated star
entries survive deletion of entries controlled by `p`.  PP3akh then supplies a
strict paid trade for the punctured universe whenever the marked host and foreign
cost inequalities hold.

### Corollary PP3app -- PROVED / CONDITIONAL MARKED-HOST INTERFACE

Every successful paid captive-star conversion strictly decreases the nested
chronological potential.  Repeating successful conversions cannot produce the
reserve-exhaustion alternative of PP3akm.

The process instead reaches, after finitely many paid stages, one of:

1. a ready state and final allocation;
2. a robust direct-completion branch;
3. a free post-trade source star entering an established paid or composite
   interface;
4. marked source, transition, anchor, Hall, alternating, distinguished-endpoint,
   or controller-pool host failure;
5. foreign insertion cost at the star-credit scale;
6. a branch in which the proposed puncture conversion is not a strict paid trade
   for the new active universe.

#### Proof

Apply PP3apn at every successful use of PP3akh and PP3apo to the resulting nested
history.  The other outcomes are exactly the failure and direct alternatives in
PP3akh--PP3aki. ∎

Thus controller puncturing itself does not break monotone termination.

## 5. Relation to the chronological history signatures

PP3apf--PP3apl localize a reserve-exhausting history to repeated candidates,
partner/controller/label stacks, or a full chronological resource matching.
The nested-potential theorem identifies when that localization is actually
needed.

### Corollary PP3apq -- PROVED

A `Theta(R)` puncture history can occur only if at least one puncture stage fails
to belong to the strict nested-paid sequence of PP3apo.  More precisely, along
any history with more than `Psi_(X_0)(S_0)` puncture stages, some stage must be:

1. nonpaid for its post-puncture universe;
2. robust/direct rather than monotone;
3. unsupported because a marked or external host fails;
4. part of a multi-step conversion whose net decrease has not been proved in the
   final nested universe.

The temporal-stability problem in PP3apk is therefore confined to these
nonmonotone stages.  It is not a generic consequence of changing controller
universes.

#### Proof

Otherwise every stage satisfies PP3apo, which bounds the number of stages by the
initial potential. ∎

## 6. Revised puncture frontier

### Corollary PP3apr -- PROVED

The moving-controller frontier now splits exactly.

1. **Strict paid punctures:** globally terminating by nested-potential
   monotonicity; no reserve-history core occurs.
2. **Robust punctures:** direct completion, a free super-target star, or explicit
   host/allocation failure.
3. **Nonmonotone punctures:** only here can the five chronological signatures of
   PP3api and their temporal-stability problem remain relevant.

Hence `Theta(R)` puncture reserve exhaustion is no longer an independent endpoint
of the paid prime-patching architecture.  The live history problem is narrower:
prove a net decrease for the currently nonmonotone multi-step puncture packages,
or convert their explicit chronological signatures.

The no-three-in-line conjecture remains unproved.
