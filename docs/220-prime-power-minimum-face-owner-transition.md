# Owner transitions change the minimum face only through physical edge support

CMR910--CMR925 close every edge inside one unchanged minimum face.  The remaining
dynamic question is how the face changes when the available host changes.  On
fixed labelled vertex sets, restriction and expansion give exact formulas.

Restricting the feasible family can only raise its minimum.  If one old minimum
survives, the new minimum face is exactly the surviving part of the old face.
Expanding can only lower the minimum.  If the value stays equal, the old face
embeds into the new one and every genuinely new minimum state uses an added edge.

An arbitrary transition factors through the intersection host.  The intersection
may have no feasible state; in that case no minimum value is assigned to it and
the old canonical minimum already has a lost-edge witness.  This convention is
used throughout.

Let `U` be a finite labelled edge universe.  A state is feasible in
`H\subseteq U` when all its labelled edges belong to `H`.  Let `\mathcal F(H)`
be a fixed equal-cardinality state system with this edgewise feasibility rule and
let `\Phi` be fixed on the ambient state universe.  For nonempty
`\mathcal F(H)`, write

\[
m(H)=\min_{R\in\mathcal F(H)}\Phi(R),
\qquad
\mathcal M(H)=\{R\in\mathcal F(H):\Phi(R)=m(H)\}.
\]

## 1. Exact minimum face under restriction

Let `H'\subseteq H` and assume both feasible families are nonempty.

### Theorem CMR926 -- PROVED

One has

\[
\boxed{m(H')\ge m(H).}
\]

If `\mathcal M(H)\cap\mathcal F(H')` is nonempty, then

\[
\boxed{
m(H')=m(H),
\qquad
\mathcal M(H')=\mathcal M(H)\cap\mathcal F(H').
}
\]

If no old minimum survives, then `m(H')>m(H)`.

### Proof

Every state feasible in `H'` is feasible in `H`.  A surviving old minimum
witnesses equality, and the equal-value states are exactly the surviving old
minima.  Without one, no state of value `m(H)` remains. ∎

## 2. Exact minimum face under expansion

Let `H\subseteq H'` and assume both feasible families are nonempty.

### Theorem CMR927 -- PROVED

One has

\[
\boxed{m(H')\le m(H).}
\]

If equality holds, then

\[
\boxed{
\mathcal M(H)\subseteq\mathcal M(H').
}
\]

If the inequality is strict, the expanded host contains a strict potential
improvement.  Every state in

\[
\mathcal M(H')\setminus\mathcal M(H)
\]

uses at least one edge of `H'\setminus H`.

### Proof

Every old state remains feasible.  Under equality every old minimum remains a
minimum.  A new minimum using no added edge would already have been feasible and
minimum in `H`. ∎

## 3. Arbitrary transitions factor through the intersection host

For hosts `H_0,H_1`, put `K=H_0\cap H_1`.

### Theorem CMR928 -- PROVED

The transition factors canonically as

\[
H_0\supseteq K\subseteq H_1.
\]

Every old state which disappears contains an edge of `H_0\setminus H_1`, and
every newly feasible state contains an edge of `H_1\setminus H_0`.

If `m(H_1)<m(H_0)`, strict improvement occurs.  Otherwise every change of the
minimum face is supported by loss of an old minimum edge, addition of an edge
used by a new minimum state, or both.  If `\mathcal F(K)` is empty, the lost-edge
branch holds immediately.

### Proof

Edgewise feasibility gives the factorisation and the state witnesses.  When
`\mathcal F(K)` is nonempty, apply CMR926--CMR927 to the two factors.  When it is
empty, every old feasible state, in particular the canonical old minimum, loses
an edge before reaching `K`. ∎

## 4. Canonical minimum change has one physical witness

Fix a total order on states and let `S(H)` be the first state in `\mathcal M(H)`.

### Theorem CMR929 -- PROVED

Suppose `m(H_1)\ge m(H_0)` and `S(H_1)\ne S(H_0)`.  Then at least one of:

1. `S(H_0)` is infeasible in `H_1` and contains an edge of
   `H_0\setminus H_1`;
2. `m(H_1)=m(H_0)`, the new canonical minimum was infeasible in `H_0`, and it
   contains an edge of `H_1\setminus H_0`.

### Proof

If the old canonical state fails, use branch 1.  If it survives, the assumed
inequality and feasibility force value equality.  A different earlier canonical
minimum must be newly feasible, so CMR927 supplies an added edge. ∎

## 5. Equal-value restriction grows the minimum core

Define

\[
E_{\min}(H)=\bigcap_{R\in\mathcal M(H)}R.
\]

### Theorem CMR930 -- PROVED

If `H'\subseteq H` and `m(H')=m(H)`, then

\[
\boxed{E_{\min}(H)\subseteq E_{\min}(H').}
\]

Every newly common edge was omitted by an old minimum state which became
infeasible under the restriction.

### Proof

CMR926 makes the new face a nonempty subfamily of the old face.  Intersecting
fewer states enlarges the intersection. ∎

The lost old minimum has a physical removed-edge witness by CMR928.

## 6. Equal-value expansion shrinks the minimum core

### Theorem CMR931 -- PROVED

If `H\subseteq H'` and `m(H')=m(H)`, then

\[
\boxed{E_{\min}(H')\subseteq E_{\min}(H).}
\]

If `e` leaves the core, some new minimum state omits `e`, and that state uses an
edge of `H'\setminus H`.

### Proof

CMR927 embeds the old face into the new one.  If an old core edge is omitted in
the larger face, the omitting minimum is new and therefore uses an added edge.
∎

## 7. Finite witness stock or recurrence

For every same-vertex-set transition which changes the canonical minimum or the
minimum core without strict potential decrease, choose the first lost or added
edge supplied above.

### Theorem CMR932 -- PROVED

For every `\lambda\ge2`, either one exact labelled edge is selected at least
`\lambda` times or the number `J` of such transitions satisfies

\[
\boxed{J\le(\lambda-1)|U|.}
\]

For a two-layer side-`N` board, `|U|\le2N^2`.

### Proof

Every counted transition has one witness in the finite edge universe. ∎

Repeated use of one edge enters the owner-independent absence-run and restoration
ledgers CMR777--CMR925.

## 8. Owner-transition minimum-face endpoint

### Corollary CMR933 -- PROVED

Every same-vertex-set minimum-face transition reaches at least one of:

1. strict potential improvement;
2. exact surviving-face intersection under restriction;
3. loss of an old minimum supported by a removed edge;
4. entry of a new minimum supported by an added edge;
5. monotone core growth under equal-value restriction;
6. core shrinkage supported by an added edge under equal-value expansion;
7. finite witness stock or one recurrent witness edge;
8. contraction, factor/wall descent, or envelope change when vertex sets change.

Thus owner transitions do not create an anonymous minimum-face recurrence.  The
remaining task is to combine recurrent witnesses and token payment with target-
load, reserve, quotient/carry, and envelope budgets.

No all-`n` theorem is claimed.  Restriction and expansion faces, empty
intersections, canonical witnesses, core monotonicity, and recurrence arithmetic
are checked in
[`scripts/verify_prime_power_minimum_face_owner_transition.py`](../scripts/verify_prime_power_minimum_face_owner_transition.py).
