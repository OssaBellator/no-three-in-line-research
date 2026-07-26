# Owner transitions change the minimum face only through physical edge support

CMR910--CMR925 close every edge inside one unchanged minimum face and amortise
that response along the finite structural owner lineage.  The remaining dynamic
question is how the minimum face itself changes when the available host changes.

On fixed labelled vertex sets the answer is exact.  Restricting the feasible
family can only raise the minimum value.  If one old minimum survives, the new
minimum face is exactly the surviving portion of the old face.  Expanding the
family can only lower the minimum value.  If it does not lower it, the old
minimum face embeds into the new one, and every genuinely new minimum state uses
an added physical edge.

An arbitrary same-vertex-set transition factors through the intersection host.
Consequently a change of canonical minimum without strict potential improvement
has an explicit lost-edge or added-edge witness.  Equal-value restrictions grow
the common minimum core; equal-value expansions shrink it.  Strict core loss is
supported by a newly feasible minimum state and therefore by an added edge.

Let `U` be one finite labelled edge universe.  A state is feasible in a host
`H\subseteq U` when all of its labelled edges belong to `H`.  Let
`\mathcal F(H)` be any fixed equal-cardinality state system with this edgewise
feasibility rule, and let `\Phi` be fixed on the ambient state universe.  Write

\[
m(H)=\min_{R\in\mathcal F(H)}\Phi(R)
\]

and

\[
\mathcal M(H)=\{R\in\mathcal F(H):\Phi(R)=m(H)\}.
\]

Only nonempty feasible families are considered.

## 1. Exact minimum face under restriction

Let `H'\subseteq H`.

### Theorem CMR926 -- PROVED

One has

\[
\boxed{m(H')\ge m(H).}
\]

Moreover:

1. if `\mathcal M(H)\cap\mathcal F(H')` is nonempty, then
   \[
   \boxed{
   m(H')=m(H),
   \qquad
   \mathcal M(H')
   =
   \mathcal M(H)\cap\mathcal F(H');
   }
   \]
2. if no old minimum survives, then
   \[
   \boxed{m(H')>m(H).}
   \]

### Proof

Every state feasible in `H'` is feasible in `H`, so the minimum cannot decrease.
If an old minimum survives, it witnesses equality, and the states of the new
face are exactly the surviving states of old minimum value.  If none survives,
no state of value `m(H)` remains, so the finite new minimum is strictly larger.
∎

## 2. Exact minimum face under expansion

Let `H\subseteq H'`.

### Theorem CMR927 -- PROVED

One has

\[
\boxed{m(H')\le m(H).}
\]

Moreover:

1. if `m(H')=m(H)`, then
   \[
   \boxed{
   \mathcal M(H)\subseteq\mathcal M(H');
   }
   \]
2. if `m(H')<m(H)`, a strict potential improvement is feasible in the expanded
   host.

Every state in

\[
\mathcal M(H')\setminus\mathcal M(H)
\]

uses at least one added edge from `H'\setminus H`.

### Proof

Every old feasible state remains feasible, so the minimum cannot increase.  Under
value equality every old minimum remains a minimum.  A state newly entering the
minimum face but using no added edge would already have been feasible in `H` and
would already have belonged to `\mathcal M(H)`. ∎

## 3. Arbitrary transitions factor through the intersection host

For two hosts `H_0,H_1`, put

\[
K=H_0\cap H_1.
\]

### Theorem CMR928 -- PROVED

The transition `H_0\to H_1` factors canonically as

\[
H_0\supseteq K\subseteq H_1.
\]

Every disappearance of an old feasible state is witnessed by an edge in
`H_0\setminus H_1`, and every newly feasible state is witnessed by an edge in
`H_1\setminus H_0`.

If `m(H_1)<m(H_0)`, strict improvement occurs.  Otherwise every change of the
minimum face is supported by loss of an old minimum edge, addition of an edge
used by a new minimum state, or both.

### Proof

Edgewise feasibility gives the restriction/expansion factorisation.  A state
which ceases to be feasible contains a lost edge; a state which becomes feasible
contains an added edge.  Apply CMR926--CMR927 to the two factors. ∎

## 4. Canonical minimum change has one physical witness

Fix a total order on labelled states and let `S(H)` be the first state in
`\mathcal M(H)`.

### Theorem CMR929 -- PROVED

Suppose

\[
m(H_1)\ge m(H_0)
\]

and `S(H_1)\ne S(H_0)`.  Then at least one of the following holds.

1. `S(H_0)` is infeasible in `H_1` and contains an edge of
   `H_0\setminus H_1`.
2. `m(H_1)=m(H_0)`, the new canonical minimum `S(H_1)` was infeasible in `H_0`,
   and it contains an edge of `H_1\setminus H_0`.

### Proof

If the old canonical state does not survive, branch 1 holds.  If it survives and
the value has not decreased, it is still a minimum in `H_1`.  A different first
minimum can precede it only if that state was not previously feasible; CMR927
supplies an added edge. ∎

Thus a same-value canonical-minimum change is never caused by owner relabelling
alone.

## 5. Equal-value restriction grows the minimum core

Define

\[
E_{\min}(H)
=
\bigcap_{R\in\mathcal M(H)}R.
\]

### Theorem CMR930 -- PROVED

If `H'\subseteq H` and `m(H')=m(H)`, then

\[
\boxed{
E_{\min}(H)
\subseteq
E_{\min}(H').
}
\]

If the inclusion is strict, every newly common edge was previously omitted by at
least one old minimum state which became infeasible under the restriction.

### Proof

CMR926 says the new minimum face is a nonempty subfamily of the old face.
Intersecting fewer states can only enlarge the common intersection.  A newly
common edge had an old minimum counterexample, and that counterexample did not
survive. ∎

The loss of that counterexample has a physical lost-edge witness by CMR928.

## 6. Equal-value expansion shrinks the minimum core

### Theorem CMR931 -- PROVED

If `H\subseteq H'` and `m(H')=m(H)`, then

\[
\boxed{
E_{\min}(H')
\subseteq
E_{\min}(H).
}
\]

If an edge `e` leaves the minimum core, there is a newly feasible minimum state
`R\in\mathcal M(H')\setminus\mathcal M(H)` with `e\notin R`.  Every such state
uses at least one edge of `H'\setminus H`.

### Proof

CMR927 embeds the old minimum face into the new one, so intersecting the larger
face can only shrink the core.  If `e` leaves the core, some new minimum omits it;
an old minimum cannot do so because `e` belonged to the old core.  CMR927 gives
added-edge support. ∎

Thus minimum-core escape is paid by physical host expansion.

## 7. Finite witness stock or recurrence

Consider `J` same-vertex-set owner transitions with no strict potential decrease.
For every transition which changes the canonical minimum or the minimum core,
choose the first lost or added physical edge supplied by CMR929--CMR931.

### Theorem CMR932 -- PROVED

For every integer `\lambda\ge2`, at least one of the following holds.

1. One exact labelled physical edge is selected as a transition witness at least
   `\lambda` times.
2. The number of minimum-face-changing transitions satisfies
   \[
   \boxed{
   J\le(\lambda-1)|U|.
   }
   \]

For a two-layer side-`N` board, `|U|\le2N^2`.

### Proof

Every counted transition has one witness from the finite labelled edge universe.
Apply the pigeonhole principle. ∎

Repeated added/lost use of one edge enters the owner-independent absence-run and
restoration ledgers CMR777--CMR925.

## 8. Owner-transition minimum-face endpoint

### Corollary CMR933 -- PROVED

Every same-vertex-set transition of a minimum face reaches at least one of:

1. strict potential improvement under expansion;
2. survival of an old minimum and exact face intersection under restriction;
3. loss of an old minimum supported by a removed physical edge;
4. entry of a new minimum supported by an added physical edge;
5. monotone minimum-core growth under equal-value restriction;
6. minimum-core shrinkage supported by an added edge under equal-value expansion;
7. finite physical witness stock or one recurrent witness edge;
8. contraction, factor/wall descent, or envelope change when the vertex sets
   change.

Hence owner transitions do not create a new anonymous minimum-face recurrence.
The remaining task is to combine recurrent transition witnesses and their exact
full-token payment with target-load, protected-reserve, quotient/carry, and
envelope budgets.

### Proof

Combine CMR926--CMR932 with the fixed-owner minimum-face and edge-lineage
endpoints CMR910--CMR925. ∎

No all-`n` theorem is claimed.  Restriction and expansion faces, canonical
minimum witnesses, core monotonicity, added-edge support, and recurrence
arithmetic are checked in
[`scripts/verify_prime_power_minimum_face_owner_transition.py`](../scripts/verify_prime_power_minimum_face_owner_transition.py).
