# Absolute-threshold periodic one-counter tails

**Branch:** `research/alternating-core-chain`

AC3wa--AC3we handle cyclic counter dependence when the complete transition law is finite residue-controlled.  This note allows genuinely absolute behaviour in one additive balance, provided that all exceptional absolute dependence is confined below one declared threshold.  Above that threshold, the transition and lower requirement are periodic in the balance residue.

The conclusion is an exact finite-strip-or-phase-cycle router.  It does not assume that the low strip behaves periodically.

## Tail model

Fix a finite control set `Q`, a modulus `M>=1`, and an additive balance `b in Z_{>=0}`.  Fix a threshold `H>=1`.

For every state with `b>=H`, the complete transition is determined by

\[
(q,r),\qquad r=b\pmod M,
\]

and consists of:

- a next control `q'=f(q,r)`;
- an integer increment `delta(q,r)`;
- a lower requirement `b>=h(q,r)`.

The residue update is therefore

\[
(q,r)\longmapsto
\bigl(f(q,r),\ r+\delta(q,r)\pmod M\bigr).
\]

Below `H`, the transition law may be arbitrary, but the full low state `(q,b)` is retained.

A change of `Q`, `M`, `H`, the tail transition table, the lower-requirement table, or the meaning of `b` is an outer reset.

## AC3wf -- finite exceptional strip -- PROVED

The absolute-dependent region

\[
\{(q,b):q\in Q,\ 0\le b<H\}
\]

has exactly `|Q|H` complete states.

Consequently every visit below `H` is either a repeated finite-strip state, a capacity-one strip ticket, a paid/reset transition, or an explicit finite-state recurrence requiring the existing finite-state router.

### Proof

There are `|Q|` controls and `H` possible balance values. QED.

## AC3wg -- eventual periodic tail phase -- PROVED

Every trajectory segment which remains in the tail `b>=H` has a residue-control orbit in the finite set `Q x Z/MZ`.  Within at most `|Q|M` steps it enters a directed phase cycle of length at most `|Q|M`.

### Proof

The tail phase update is deterministic on `|Q|M` states.  The first repeated phase gives a preperiod followed by a directed cycle. QED.

## AC3wh -- exact phase-block drift and threshold -- PROVED

Let

\[
C=(s_0,s_1,\ldots,s_{ell-1},s_0)
\]

be one tail phase cycle and put

\[
D=\sum_{i=0}^{ell-1}\delta(s_i).
\]

Because the residue returns,

\[
\boxed{D\equiv0\pmod M.}
\]

Let `p_0=0` and

\[
p_i=\sum_{j<i}\delta(s_j).
\]

All visits of one traversal remain in the tail and satisfy their lower guards exactly when the block-entry balance obeys

\[
\boxed{
 b\ge T(C):=
 \max_i\{H-p_i,\ h(s_i)-p_i\}.
}
\]

### Proof

At phase `s_i` the balance is `b+p_i`; the two required inequalities are `b+p_i>=H` and `b+p_i>=h(s_i)`.  Maximizing their rearrangements gives the threshold.  Residue return gives `D=0 mod M`. QED.

## AC3wi -- exact repeated-block trichotomy -- PROVED

Fix a legal block-entry value `b_0>=T(C)`.

1. If `D>0`, every repeated block is legal and the block-entry balance is `b_0+nD`; exact complete-state recurrence is impossible.
2. If `D=0`, one traversal returns the exact balance and phase.
3. If `D<0`, the number of legal traversals is exactly

\[
\boxed{
1+\left\lfloor\frac{b_0-T(C)}{|D|}\right\rfloor.
}
\]

### Proof

At the start of traversal `n` the balance is `b_0+nD`.  AC3wh says that traversal is legal exactly when this value is at least `T(C)`.  The three cases follow immediately. QED.

## AC3wj -- absolute-threshold tail router -- PROVED UNDER THE COMPLETE-TAIL CONTRACT

Every deterministic one-counter history satisfying the model has one continuation:

1. it enters the finite exceptional strip of AC3wf;
2. a tail phase has not yet repeated, so at most `|Q|M` transient steps remain;
3. it reaches a phase cycle with positive drift and escapes monotonically at block boundaries;
4. it reaches a zero-drift exact return;
5. it reaches a negative-drift cycle with the explicit finite budget of AC3wi;
6. or a control, modulus, threshold, transition, lower requirement, balance interpretation or omitted payment field changes, giving an outer reset.

Thus unbounded absolute dependence confined to a finite lower strip does not create a new recurrent tail obstruction.

### Proof

Use AC3wf on every low visit and AC3wg--AC3wi on every maximal tail segment. QED.

## Updated AC4 frontier

The unresolved absolute-value cases are now those in which exceptional thresholds move without a finite dictionary, the transition depends on the unbounded magnitude even arbitrarily far into the tail, or nonlinear/nonadditive legality cannot be represented by a complete finite control and lower requirement.

## Finite check

`scripts/verify_ac_absolute_threshold_periodic_tail.py` audits finite tail tables, phase extraction, the residue divisibility of drift, the exact block threshold and the repeated-block trichotomy.