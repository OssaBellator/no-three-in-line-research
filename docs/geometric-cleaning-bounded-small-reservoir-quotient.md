# Bounded small-reservoir quotient and donor restoration gates

**Branch:** `research/geometric-cleaning`

GC2fp--GC2fy leave the case `p<=D_phys` as a bounded-budget small donor reservoir. The reservoir is small, but its exact contents may still churn. This note gives the correct finite quotient. A reservoir of size at most `D` over a finite physical donor dictionary has a polynomial exact-state stock for fixed `D`, and every recurrent change exposes one canonical donor-membership restoration gate.

The result applies only when donor identities are occurrence-faithful physical addresses. An untagged donor alias, changing context interpretation or newly created donor dictionary is returned explicitly rather than silently identified.

## Small-reservoir model

Fix one donor epoch. Let `A` be a finite dictionary of exact physical donor addresses, with

\[
|A|=K.
\]

An address includes every payment-sensitive field used by the donor operation: physical cell/column roles, target, selected blocker, source factor, exact lineage and finite operation word.

Let the live reservoir be a subset

\[
R\subseteq A,
\qquad |R|\le D.
\]

Let `X` be the finite non-reservoir boundary state: target role, clean-height band, blocker class, current owner status, local context and legality word. Put `Q=|X|`.

## GC2ge -- exact bounded-reservoir state stock -- PROVED

The number of complete states `(x,R)` is at most

\[
\boxed{
Q\sum_{i=0}^{D}\binom Ki.
}
\]

For `K>=1`, this is bounded by

\[
\boxed{Q(D+1)K^D.}
\]

Thus the bounded-budget branch has polynomial state stock whenever `D` is fixed or already polynomially bounded with an acceptable exponent.

### Proof

Choose the finite boundary state and then choose a reservoir subset of size at most `D`. For the second display, use `binom(K,i)<=K^i<=K^D` for `0<=i<=D`. QED.

The theorem deliberately counts exact subsets; it does not replace them by cardinality alone.

## GC2gf -- long small-reservoir histories contain exact cycles -- PROVED

Inside one fixed donor dictionary and boundary-state family, any history longer than

\[
Q\sum_{i=0}^{D}\binom Ki
\]

repeats a complete state. The first repeated-state segment contains a simple exact cycle of no greater length.

### Proof

Pigeonhole gives a repeated complete state. Delete internal closed subwalks until the repeated segment has no internal repeated state. QED.

## GC2gg -- canonical donor-membership restoration gate -- PROVED

Fix a total order on `A`. Every nonconstant exact reservoir cycle has a least donor atom `a` whose membership changes. Rotate the cycle at the first change of the bit

\[
1_{a\in R}.
\]

The first later edge restoring the initial bit is the canonical **donor restoration gate**. Its address consists of:

- the donor atom `a`;
- the restored membership bit;
- the finite boundary state immediately before restoration;
- the exact operation/lineage edge performing the restoration.

### Proof

A nonconstant cycle changes the membership of at least one donor atom or changes the finite boundary state. In the donor-changing case choose the least atom. Its Boolean membership leaves one value and must later return because the complete reservoir returns. First-change and first-return conventions make the gate canonical. If only the boundary state changes, use the existing finite boundary-cycle router. QED.

## GC2gh -- monotone depletion or capacity-one restoration closes recurrence -- PROVED UNDER THE RESTORATION CONTRACT

Suppose donor membership can reappear only by one of the following exact routes:

1. current-factor payment or created-collateral descent;
2. occurrence-faithful debit from a finite nonreplenishing source;
3. one capacity-one ticket indexed by the donor restoration address;
4. a declared reset of target, blocker, clean-height, context, dictionary or lineage interpretation;
5. or physical impossibility.

Then every nonimproving exact small-reservoir cycle is paid, descending, impossible, reset, or consumes a new ticket. If the finite boundary state has stock `Q`, the coarse membership-direction ticket stock is at most

\[
\boxed{2QK}
\]

before retaining the finer operation-edge address; the exact reachable stock can only be smaller.

If reservoir membership is monotone decreasing, no nonconstant reservoir cycle exists.

### Proof

Apply GC2gg. A monotone Boolean membership cannot leave and restore its initial value. Otherwise the canonical restoration edge enters one declared route. There are two restored bit values, `Q` boundary states and `K` donor atoms, giving the coarse stock. Capacity-one use forbids recurrence of one address. QED.

## GC2gi -- bounded small-reservoir router -- PROVED UNDER THE COMPLETE-LINEAGE CONTRACT

The branch `p<=D_phys` from GC2ft is no longer an unstructured exception. It has one of the following continuations:

1. a finite exact state repetition and canonical donor restoration gate;
2. monotone reservoir depletion;
3. direct current payment or created-collateral descent;
4. finite source debit or a capacity-one restoration ticket;
5. a target-common/global blocker or clean-height failure retained as its exact witness;
6. or a missing physical donor/lineage/context field returned as an outer reset.

Thus bounded donor reservoirs are closed conditionally without discarding the concentrated blocker or column witnesses that produced the shortage.

### Proof

Use GC2ge--GC2gf for the finite quotient and GC2gg--GC2gh for recurrence. The blocker/column witness remains a field of the finite boundary state and is therefore preserved across the reduction. QED.

## Updated GC frontier

The bounded-budget small-reservoir branch now reduces to exact finite restoration gates. Remaining GC5 work is concentrated on:

- payment of target-common/global blockers lacking a physical removal;
- genuinely fresh or unbounded donor dictionaries;
- non-tagged feedback for which no occurrence-faithful lineage exists;
- block-tuple and global-context recursion;
- clean-height preservation and local superregular resampling.

## Finite check

`scripts/verify_gc_small_reservoir_quotient.py` enumerates bounded donor subsets, checks the exact stock, extracts repeated-state cycles and verifies the least donor-membership restoration gate.
