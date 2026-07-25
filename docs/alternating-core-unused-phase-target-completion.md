# Unused hard phases complete centred target fans

**Branch:** `research/alternating-core-chain`

AC3kr--AC3ku reduce two-block target correction to centre-only witnesses,
residual-block-only witnesses and joint kernels.  The canonical active-literal
chart gives a stronger conclusion whenever the residual block has a phase not
mentioned by any active hard check.

A hard check containing block `x` can be violated at phase `b` only when its
forbidden literal at `x` is exactly `b`.  Thus an unused hard phase eliminates
all residual-only and joint witnesses at once.  Only a blocker which avoids `x`
can remain.

## Hard literal support

For a phase block `x`, define

\[
L_x^{\rm hard}
=
\{f_C(x):C\in\mathcal H,\ x\in S_C\}.
\]

Write `q_x=omega_x` for the current phase and

\[
B_x=\mathcal A_x\setminus\{q_x\}.
\]

A phase

\[
b\in B_x\setminus L_x^{\rm hard}
\]

is an **unused hard phase** at `x`.

Retain the AC3kr setup: `v` has target `a`, a selected blocker contains both
`v` and `x`, and changing `x` away from its current phase kills that blocker.

## AC3kv -- unused residual phase eliminates two witness classes -- PROVED

Let `b` be an unused hard phase at `x`.  Then no hard check violated by

\[
\omega^{v\leftarrow a,\ x\leftarrow b}
\]

contains `x`.

Consequently the pair assignment is hard-safe if and only if no centre-only
witness for `a` exists.

### Proof

Suppose a violated hard check contains `x`.  Its forbidden literal at `x` must
equal the installed phase `b`, which would put `b` in `L_x^hard`, contradicting
the choice of `b`.  AC3kr says every newly violated check must contain `v` or
`x`.  Since the `x` case is impossible, every failure is centre-only.  Absence
of such a witness is therefore equivalent to hard safety. QED.

The statement uses the complete hard literal support, not merely the selected
blocker family.  Soft checks do not affect feasibility and remain in the exact
created-collateral ledger.

## AC3kw -- one unused common phase completes a target subfan -- PROVED

Suppose one current residual block `x` occurs in the chosen blockers of a target
set `A` at centre `v`.  Let `A_0` be the targets for which every activated hard
blocker contains `x`; equivalently, no centre-only witness exists.

If `x` has one unused hard phase `b`, then for every `a in A_0`,

\[
\boxed{
\omega^{v\leftarrow a,\ x\leftarrow b}
\text{ is hard-safe}.
}
\]

Under the declared physical phase realization and AC3ki completion contract,
these states form one legal alternative-state menu.  The common change at `x`
does not turn the alternatives into a product; common and private payment is
still counted by AC3kj.

### Proof

Apply AC3kv to every target.  The same phase `b` is unused globally at `x`, and
by definition every target in `A_0` has no centre-only witness.  Each pair
assignment is therefore hard-safe.  AC3ki converts the individually completed
physical states into a menu without requiring compatibility between different
target values. QED.

## Literal saturation

Call `x` **hard-literal saturated** when

\[
\boxed{
B_x\subseteq L_x^{\rm hard}.
}
\]

Equivalently, every noncurrent phase is named by at least one active hard check.
This is the sharp compression boundary already identified by AC3aa: the hard
chart has no generic `other` phase at `x`.

## AC3kx -- unresolved support-disjoint arms force literal saturation or a new blocker -- PROVED

Suppose AC3jk returns targets with pairwise-disjoint residual arms.  For each
target `a`, choose the least mutable block `x_a` in its arm.  Then the `x_a` are
distinct.

Every target for which:

1. `x_a` is not hard-literal saturated; and
2. no centre-only witness exists,

has an AC3ki-complete state after choosing any unused hard phase at `x_a` and
attaching the declared physical completion data.

Therefore every target which remains uncompleted returns at least one of:

- an exact replacement blocker avoiding its selected residual block;
- a distinct hard-literal-saturated residual block;
- physical occurrence failure, coherence mismatch, owner reset, protected
  contract reset or envelope reset.

If `m` support-disjoint targets remain and fewer than `c` have replacement
blockers or outer resets, at least

\[
\boxed{m-c}
\]

distinct residual blocks are hard-literal saturated.

### Proof

Disjoint arms give distinct selected blocks.  Apply AC3kv to every target whose
selected block has an unused phase.  Failure despite an unused phase is exactly
a centre-only witness.  The only other way to avoid completion inside the fixed
contract is a change or failure of one of its declared physical/accounting
fields.  Counting the remaining targets proves the final bound. QED.

## AC3ky -- exact residual completion frontier -- PROVED

After AC3kr--AC3kx, neither a common residual literal nor support-disjoint arms
remain as an unqualified local obstruction.

A centred target family returns only:

1. AC3ki-complete alternative states and their exact menu comparison;
2. centre-only replacement blockers with finite target/check exposure tickets;
3. ordinary one-block hard phase fans on a residual block;
4. joint centre/residual kernels of residual rank at most one;
5. hard-literal-saturated residual blocks, where every noncurrent phase is an
   explicit active hard literal;
6. exact physical, owner, protected-contract or envelope macro resets.

In particular, large raw phase alphabets help rather than hurt unless their
entire noncurrent part is explicitly occupied by active hard literals.  The
remaining arithmetic task is classification or discharge of those saturated
literal blocks and recurrent replacement-blocker/macro-edge records.

### Proof

AC3ku gives the lower-depth witness list.  AC3kv--AC3kx complete every target
with an unused residual phase and no replacement blocker.  The complement is
exactly literal saturation or one of the already named witness/reset outputs.
QED.

## Finite check

`scripts/verify_ac_unused_phase_target_completion.py` exhausts small hard-check
systems, confirms that an unused phase cannot occur in a violated check through
its block, checks common-residual batch completion, and verifies the
support-disjoint saturation count.