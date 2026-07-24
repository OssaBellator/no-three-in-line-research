# Global slot-occurrence endpoint

The square-root macro patch is sampled from independent slot variables.  Source
and cross-macro certificates can therefore be added to the same product-space
local lemma, provided they do not exhaust the slot-occurrence slack left by the
internal pair and triple events.

## 1. General rank-three slot system

Let every slot variable take values in a domain of size at least `gamma R`.
Let `A` be a family of conflict events satisfying:

1. every event depends on two or three slots;
2. every event has probability at most

\[
 p=\frac8{\gamma^2R};
\]

3. every slot occurs in at most `Delta` events.

Events are adjacent when their slot sets intersect.

### Theorem PP3ei -- PROVED

A simultaneous avoidance assignment exists whenever

\[
 \boxed{
 3p(3\Delta-2)\le1.
 }
\]

Equivalently, it is sufficient that

\[
 \boxed{
 \Delta
 \le
 \frac{\gamma^2R+48}{72}.
 }
\]

#### Proof

An event on at most three slots shares a variable with at most
`3(Delta-1)` other events.  Thus its dependency degree satisfies
`D+1<=3Delta-2`.  Apply the rational symmetric local-lemma condition
`3p(D+1)<=1` and substitute `p=8/(gamma^2R)`. ∎

The probability assumption holds whenever, after all but one involved slot are
fixed, each geometric type has only a bounded number of completing source edges.
The constant eight covers the movement/refill type choices used in PP3dl.

## 2. Internal occurrence cost

One macro pool has `n=2W` slots.  Its internal system has one pair event for
every slot pair and one three-slot event for every slot triple.

### Proposition PP3ej -- PROVED

Every macro slot belongs to exactly

\[
 \Delta_{\rm int}
 =
 (n-1)+\binom{n-1}{2}
 =
 \frac{n(n-1)}2
\]

internal events.  If

\[
 W\le\frac{\gamma\sqrt R}{16},
\]

then

\[
 \boxed{
 \Delta_{\rm int}\le\frac{\gamma^2R}{128}.
 }
\]

Consequently the additional source-containing and cross-macro event occurrence
available to each slot is at least

\[
 \boxed{
 \frac{7\gamma^2R}{1152}+O(1).
 }
\]

#### Proof

The exact count follows by choosing the one or two other slots in an internal
event.  Since `n=2W`,

\[
 \Delta_{\rm int}\le\frac{n^2}{2}=2W^2
 \le\frac{\gamma^2R}{128}.
\]

Subtract this from the asymptotic threshold `gamma^2R/72` in PP3ei:

\[
 \frac1{72}-\frac1{128}=\frac7{1152}.
\]

The additive constant comes from the `48/72` term. ∎

This is the first direct numerical budget for all remaining certificate classes.

## 3. Global conditional spread

Assume `Delta>=2` and the PP3ei inequality.  Put

\[
 x=\frac1{3\Delta-2}.
\]

### Theorem PP3ek -- PROVED FROM THE PUBLISHED LLL-DISTRIBUTION THEOREM

Under the distribution conditioned on avoiding every event in `A`, a cylinder
fixing `q` slot values has probability at most

\[
 \boxed{
 \frac{e^q}{(\gamma R)^q}.
 }
\]

#### Proof

The PP3ei inequality gives

\[
 p\le\frac1{3(3\Delta-2)}.
\]

Since an event has at most `3Delta-3` neighbors and

\[
 \left(1-\frac1{3\Delta-2}\right)^{3\Delta-3}>\frac13,
\]

the asymmetric LLL inequalities hold with activity `x`.

A `q`-slot cylinder meets at most `qDelta` conflict events.  The
LLL-distribution theorem bounds its inflation by

\[
 (1-x)^{-q\Delta}.
\]

For `Delta>=2`,

\[
 -\log(1-x)\le\frac{x}{1-x}=\frac1{3\Delta-3},
\]

so the inflation is at most

\[
 \exp\left(\frac{q\Delta}{3\Delta-3}\right)
 \le e^q.
\]

The unconditional cylinder probability is at most `(gamma R)^(-q)`. ∎

Thus adding globally controlled source and cross events does not destroy
fixed-rank spread.

## 4. Exact remaining occurrence theorem

At the balanced prime-gap exponents, it is enough to construct macro pools and
label domains such that:

1. unary fixed-pair cell conflicts are removed by domain restriction PP3ea;
2. every remaining source-anchor or cross-macro conflict has probability at most
   `8/(gamma^2R)`;
3. each slot occurs in at most

\[
 \frac{7\gamma^2R}{1152}+O(1)
\]

additional events beyond the internal system.

PP3ei then solves internal, source-containing, and cross-macro geometry in one
assignment, and PP3ek supplies the output spread.

A failure must therefore be visible as a slot supporting `Omega(R)` distinct
external certificate patterns.  The same-edge product core PP3dv and the
boundary Hall obstruction PP3eh are two explicit mechanisms that can create
such concentration.