# Cause-capacity bank for Hall-core missing rectangles

**Branch:** `research/geometric-cleaning`

GC2gt--GC2gx retain the complete blocked rectangle produced by a failed donor assignment and partition its weighted incidence by exact physical cause.  This note gives the direct payment interface when those causes have finite blocking capacities.

## Exact cause loads

Let `R=X x (A\Y)` be the missing rectangle of one canonical Hall core.  Give each target `x` weight `w_x>=0`.  Every missing pair `(x,a)` has one canonical exact cause `c(x,a)` from a finite dictionary `C`.

Define

\[
L_c=\sum_{(x,a)\in R:\ c(x,a)=c}w_x,
\qquad
W_R=\sum_c L_c.
\]

For every cause `c`, fix a nonnegative capacity `B_c`.  A paid incidence consumes its weight from that capacity, and capacity is not replenished inside the epoch.

## GC2gy -- exact cause partition -- PROVED

The cause loads form a disjoint partition:

\[
\boxed{W_R=\sum_{c\in C}L_c.}
\]

### Proof

Every missing pair receives exactly one canonical cause. QED.

## GC2gz -- paid rectangle or exact overload -- PROVED

Exactly one of the following holds:

1. `L_c<=B_c` for every cause, so the complete missing rectangle is paid by the cause bank;
2. some exact cause satisfies

\[
\boxed{L_c>B_c,}
\]

and is returned as a physical capacity overload.

In particular, if

\[
W_R>\sum_c B_c,
\]

then an overload cause must exist.

### Proof

The first alternative is the coordinatewise capacity condition.  If it fails, choose the least overloaded cause.  The final implication follows by summing the coordinatewise inequalities. QED.

## GC2ha -- finite repeated-failure mass -- PROVED UNDER THE NONREPLENISHING-BANK CONTRACT

Across any sequence of Hall-core failures in one epoch for which every cause load is paid, the cumulative missing-rectangle mass is at most

\[
\boxed{\sum_c B_c.}
\]

### Proof

Cause `c` can pay cumulative load at most `B_c`.  Sum over causes. QED.

## GC2hb -- capacity-one cause tickets -- PROVED

When all weights and capacities are integral, expand cause `c` into tickets

\[
(c,u),\qquad1\le u\le B_c.
\]

Canonical ordered allocation of the `L_c` units gives an occurrence-faithful ticket realization.  No ticket is reused inside the epoch.

### Proof

This is the unit expansion of the integer capacity bank. QED.

## GC2hc -- Hall-cause payment router -- PROVED UNDER THE COMPLETE-CAUSE-BANK CONTRACT

Every bounded-reservoir Hall failure has one continuation:

1. `Y=A`, giving the existing pure global donor-count shortage;
2. the missing rectangle is paid by finite cause capacities;
3. one exact target-common, global, column, line, owner, clean-height or context cause exceeds its capacity;
4. a paid cause yields current-factor payment, strict descent or a capacity-one ticket;
5. or the cause dictionary, canonical labelling, weight interpretation or capacity bank changes, giving an outer reset.

Thus the many-distinct-cause branch is finite whenever exact causes have nonreplenishing capacities.

### Proof

Use GC2gy--GC2hb on the missing rectangle supplied by GC2gt--GC2gx. QED.

## Finite check

`scripts/verify_gc_cause_capacity_bank.py` generates weighted cause partitions and repeated failure sequences, verifying exact mass conservation, the paid/overload dichotomy and the cumulative bank bound.