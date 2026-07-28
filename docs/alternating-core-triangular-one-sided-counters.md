# Triangular one-sided additive counters

**Branch:** `research/alternating-core-chain`

AC3vq--AC3vu reduce one lower-guarded additive balance to a finite normalized word shape and one base counter.  The next obstruction is interaction among several one-sided counters.  This note closes the lexicographically triangular case: the guard of coordinate `i` may depend on the finite control state and earlier counters, but not on later counters.

The result does not cover arbitrary mutually coupled guards.  Its point is that the first nonzero drift coordinate sees an exactly periodic guard profile because every earlier coordinate has zero drift.

## Triangular macro contract

Fix a finite macro word of length `P`.  Let

\[
m=(m_1,\ldots,m_q)\in\mathbb Z^q
\]

be additive counters and let the `t`-th edge add `v_t in Z^q`.  Put

\[
s_t=\sum_{u<t}v_u,
\qquad
\Delta=\sum_{t=0}^{P-1}v_t.
\]

At occurrence `t`, every lower guard on coordinate `i` has the form

\[
m_i+s_{t,i}\ge L_{t,i}(m_1+s_{t,1},\ldots,m_{i-1}+s_{t,i-1}),
\]

where `L_{t,i}` is fixed by the finite control word and depends only on earlier counters.  Changed guard functions, changed word, changed finite control or omitted payment-sensitive fields are outer resets.

## AC3vv -- periodic guard profile at the first drift coordinate -- PROVED

Assume `Delta` is nonzero and let

\[
i_* = \min\{i:\Delta_i\ne0\}.
\]

Then every earlier counter has zero drift.  Consequently, at every repetition of the same macro word, the complete lower-guard threshold profile seen by coordinate `i_*` is identical.

### Proof

For `j<i_*`, `Delta_j=0`.  At the start of every repetition, counter `j` therefore has the same value, and its within-word trajectory is always `m_j+s_{t,j}`.  Every threshold `L_{t,i_*}` depends only on those earlier trajectories and the repeated finite control word, so it is unchanged from one repetition to the next. QED.

Define the exact base requirement

\[
B_{i_*}
=
\max_t
\left(
L_{t,i_*}(m_{<i_*}+s_{t,<i_*})-s_{t,i_*}
\right).
\]

One repetition is legal in coordinate `i_*` exactly when `m_{i_*}>=B_{i_*}`.

## AC3vw -- positive first drift is strict lexicographic escape -- PROVED

If `Delta_{i_*}>0`, every repetition increases the first changing counter while all earlier counters return exactly.  Hence the repeated macro word cannot return to the same additive resource state, and the vector `m` increases strictly in lexicographic order at every repetition.

### Proof

Earlier coordinates have zero drift by the definition of `i_*`, while coordinate `i_*` changes by the positive integer `Delta_{i_*}`.  Therefore the endpoint is lexicographically larger and cannot equal the start. QED.

This is a monotone-output route, not a finite ticket claim.  A later guard may still stop execution, but exact recurrence of the complete additive state is impossible.

## AC3vx -- negative first drift has an exact headroom budget -- PROVED

If `Delta_{i_*}<0` and the first execution is legal, the number of legal repetition starts in coordinate `i_*` is exactly

\[
\boxed{
1+\left\lfloor
\frac{m_{i_*}-B_{i_*}}{-\Delta_{i_*}}
\right\rfloor.
}
\]

After that many executions, the next repetition violates at least one lower guard on coordinate `i_*`.

### Proof

By AC3vv the base requirement is the same at every repetition.  The `r`-th repetition starts with value `m_{i_*}+rDelta_{i_*}` and is legal exactly when this value is at least `B_{i_*}`.  Solving that one-dimensional integer inequality gives the displayed count. QED.

Thus negative first drift consumes finite lower-guard headroom even when later counters interact arbitrarily with earlier ones under the triangular contract.

## AC3vy -- zero drift returns the complete additive resource vector -- PROVED

If `Delta=0`, one execution returns every additive counter exactly.  Any nonconstant recurrence is therefore entirely in the finite control, physical occurrence, owner, lineage, legality or other declared boundary fields and routes to the existing finite-state restoration/ticket interfaces.

### Proof

Additivity gives endpoint `m+Delta=m`.  No additive coordinate is omitted from this conclusion.  Any remaining state change lies outside the additive vector and must be represented in the complete boundary address or returned as a reset. QED.

## AC3vz -- triangular multi-counter router -- PROVED UNDER THE COMPLETE-TRIANGULAR-GUARD CONTRACT

For a repeated bounded macro word with finitely many triangular lower-guarded additive counters, exactly one of the following applies:

1. `Delta=0`, and the additive state returns exactly by AC3vy;
2. the first nonzero drift is positive, giving strict lexicographic escape by AC3vw;
3. the first nonzero drift is negative, giving the exact finite execution budget of AC3vx;
4. the guard dependency is not triangular, the word or finite control changes, or a payment-sensitive field is omitted, giving an explicit outer reset.

Consequently, multiple one-sided counters do not create a hidden recurrent tail whenever their dependency order is triangular.  The remaining AC4 counter frontier is genuinely cyclic guard dependence, dynamic dictionaries, nonlinear/nonadditive resources, or fresh physical replenishment.

### Proof

If `Delta=0`, use AC3vy.  Otherwise choose `i_*` and apply AC3vv, followed by AC3vw or AC3vx according to the sign of its drift.  Contract failure is returned rather than silently identified. QED.

## Finite check

`scripts/verify_ac_triangular_one_sided_counters.py` enumerates small triangular affine guard systems, verifies periodicity at the first drift coordinate, checks positive lexicographic escape and the exact negative-drift headroom count.