# Two-block completion of centred target alternatives

**Branch:** `research/alternating-core-chain`

AC3ji--AC3jm reduce every failed blocker completion to alternative values of one
phase block `v`.  AC3jk returns either an unconditional target exclusion, one
current residual literal shared by many targets, or target blockers with
support-disjoint residual arms.  AC3ki--AC3km explain how completed alternatives
must be counted, but deliberately leave the construction of those complete
states open.

This note gives the exact next reduction for the latter two cases.  Changing the
centre block and one current-aligned residual block kills the selected hard
check.  Any new hard failure has one of only three incidence types, with strictly
smaller residual rank.  Thus a raw common-residual or support-disjoint arm is not
left as an unclassified completion problem.

The result is stated for the canonical O1 phase system.  Every phase assignment
preserves the active row and column sets.  The declared hard family must include
all opposite-layer, protected-bank and other feasibility conditions needed for
the proposed local phase state.  A hard-safe assignment becomes an AC3ki
complete state only after its physical phase realization, AC3v envelope,
opposite-layer record, owner chart and reverse ticket are attached.

## Setup

Let

\[
\omega\in\prod_{z\in V}\mathcal A_z
\]

be the current hard-feasible phase assignment.  Every canonical hard check
`C=(S_C,f_C)` has rank at most three and is violated exactly when the phase
assignment restricts to `f_C` on `S_C`.

Fix distinct mutable blocks `v,x`.  Write

\[
q_v=\omega_v,
\qquad
q_x=\omega_x.
\]

Fix a centre target `a != q_v` and suppose its chosen hard blocker `C_0`
contains both `v` and `x` with

\[
f_{C_0}(v)=a,
\qquad
f_{C_0}(x)=q_x,
\]

and every other literal of `C_0` current-aligned.  For every residual phase
`b != q_x`, let

\[
\omega^{a,b}
=
\omega^{v\leftarrow a,\ x\leftarrow b}.
\]

The assignment `omega^{a,b}` does not violate `C_0`, because its value at `x`
differs from `f_{C_0}(x)`.

## AC3kr -- exact two-block hard-witness trichotomy -- PROVED

Let `C` be any hard check violated by `omega^{a,b}`.  Since `omega` is
hard-feasible, `C` meets `{v,x}`.  Exactly one of the following applies.

1. **Centre-only witness.**  The scope contains `v` and not `x`.  Every other
   literal of `C` is current-aligned, so its effective residual rank is at most
   two.
2. **Residual-block-only witness.**  The scope contains `x` and not `v`.  Every
   other literal is current-aligned, again with effective residual rank at most
   two.
3. **Joint two-block kernel.**  The scope contains both `v` and `x`.  Every
   remaining literal is current-aligned, and the effective residual rank is at
   most one.

No violated check can avoid both changed blocks.

### Proof

Only `v` and `x` differ between `omega` and `omega^{a,b}`.  A check avoiding
both has the same restriction in the two assignments and therefore cannot be
newly violated.  If a violated check contains exactly one changed block, every
other scope variable retains its current phase, and rank at most three leaves at
most two such variables.  If it contains both changed blocks, at most one scope
variable remains, and that variable is current-aligned.  These three incidence
patterns are disjoint and exhaustive. QED.

The centre-only witness is a new blocker for the target `a` which does not use
the attempted residual correction.  The residual-only witness is an ordinary
current-context hard target at block `x`.  The joint witness is already a
depth-one kernel after fixing the pair `(v=a,x=b)`.

## Phase-cover notation

Let

\[
B_x=\mathcal A_x\setminus\{q_x\},
\qquad
h_x=|B_x|.
\]

For the fixed target `a`, define:

- `V(a)=1` when some centre-only witness is violated for every attempted
  residual phase because it does not involve `x`;
- `X` as the set of phases `b in B_x` for which at least one residual-only
  witness is violated;
- `J(a)` as the set of phases `b in B_x` for which at least one joint witness is
  violated.

A phase may belong to both `X` and `J(a)`.  The sets record blocked phase values,
not hard-check multiplicity.

## AC3ks -- exact completion-or-cover bound -- PROVED

If `V(a)=0`, then

\[
\boxed{
\omega^{a,b}\text{ is hard-safe}
\iff
b\notin X\cup J(a).
}
\]

Consequently, if no two-block correction is hard-safe and `V(a)=0`, then

\[
\boxed{B_x=X\cup J(a)}
\]

and hence

\[
\boxed{|X|+|J(a)|\ge h_x.}
\]

In particular, at least one of

\[
\boxed{|X|\ge\lceil h_x/2\rceil}
\qquad\text{or}\qquad
\boxed{|J(a)|\ge\lceil h_x/2\rceil}
\]

holds.

Under the declared scope-complete phase realization contract, every hard-safe
`omega^{a,b}` yields one AC3ki complete target state after attaching its physical
state, full AC3v envelope, owner chart and reverse ticket.

### Proof

AC3kr classifies every possible hard failure.  When `V(a)=0`, a phase `b` fails
exactly when a residual-only or joint witness is present, which is exactly
membership in `X union J(a)`.  If every phase fails, that union covers `B_x`.
The cardinality and half-cover alternatives follow from the union bound.  The
last statement is the completion contract: hard safety supplies feasibility,
while the additional records supply the remaining AC3ki fields. QED.

## AC3kt -- common-residual target router -- PROVED

Suppose one current residual literal `(x,q_x)` occurs in the selected blockers
of a target set `A` at centre `v`.  For each `a in A`, scan all phases
`b in B_x` and retain the least hard witness when the pair assignment fails.
Then every target belongs to exactly one of the following classes.

1. **Completed target:** some `b` is hard-safe and gives a complete target state
   under the phase realization contract.
2. **Centre-only obstruction:** `V(a)=1`; the target has a canonical blocker not
   using `x`.
3. **Residual-block phase obstruction:**
   \[
   |X|\ge\lceil h_x/2\rceil.
   \]
   This conclusion is independent of `a` and enters the ordinary cross-centre
   hard-target router at block `x` in the original current context.
4. **Joint lower-depth fan:**
   \[
   |J(a)|\ge\lceil h_x/2\rceil.
   \]
   Every retained witness contains the pair `(v=a,x=b)` and has current-aligned
   residual rank at most one.

If `A_open` is a target subfamily with no completed target and no centre-only
obstruction, while the residual-block phase obstruction fails, then the number
of distinct target-phase incidences in joint kernels is at least

\[
\boxed{
|A_{\rm open}|\lceil h_x/2\rceil.
}
\]

After splitting by any finite joint-witness role alphabet of size `R_joint`, one
role carries at least

\[
\boxed{
\frac{|A_{\rm open}|\lceil h_x/2\rceil}{R_{\rm joint}}
}
\]

incidences.

### Proof

Apply AC3ks target by target.  The residual-only set `X` depends only on changing
`x` from the original current assignment and not on `a`, because its witnesses
do not contain `v`.  If `X` is smaller than half the residual alphabet, every
uncompleted target with no centre-only witness has a joint set of size at least
half the alphabet.  Sum these sizes and pigeonhole over the finite role words.
QED.

Centre-only obstructions are assigned exact target/check exposure tickets.  A
recurrent return with the same exact ticket is a decorated macro edge unless a
separate literal, owner or arithmetic theorem discharges it.  It is not counted
as successful completion.

## Support-disjoint residual arms

Suppose AC3jk supplies target blockers with pairwise-disjoint nonempty residual
scopes.  For every target `a`, choose the least mutable block `x_a` in its
selected residual scope.  The blocks `x_a` are distinct across the retained
family.  Scanning the noncurrent phases of `x_a` kills the selected blocker and
puts each target into the AC3kt four-way classification, with `x` replaced by
`x_a`.

## AC3ku -- support-disjoint arms reduce to lower-depth objects -- PROVED

A support-disjoint residual-arm family returns one of:

1. AC3ki-complete target states, forming an alternative-state menu under
   AC3ki--AC3kk;
2. exact centre-only replacement blockers, each carrying a finite exposure
   ticket;
3. distinct residual blocks with at least half of their alternative phases
   hard-unsafe in the original current context;
4. joint centre/residual phase kernels with current-aligned residual rank at most
   one;
5. a physical realization, owner interpretation, protected-contract or envelope
   change, recorded as an AC3ka macro edge.

Thus neither a common residual literal nor support-disjoint residual arms remain
as raw AC4 terminal labels.  The remaining local objects are complete target
states, ordinary one-block hard phase fans, depth-one joint kernels, finite
replacement-blocker tickets or exact outer resets.

### Proof

Disjoint residual scopes give distinct selected blocks `x_a`.  Apply AC3kr--AC3kt
to every target.  A hard-safe phase assignment gives conclusion 1 under the
completion contract.  The three witness types give conclusions 2--4.  Failure
of any fixed physical or accounting field is conclusion 5 by AC3jt and AC3kh.
The list is exhaustive. QED.

## Finite check

`scripts/verify_ac_two_block_target_completion.py` exhausts canonical hard checks
of rank at most three in small phase alphabets, verifies the three incidence
classes and current alignment, checks every finite phase-cover system, and
checks the common-residual/support-disjoint routing identities.