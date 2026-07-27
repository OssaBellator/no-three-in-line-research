# Primitive relations in mixed-sign translation phase memory

**Branch:** `research/alternating-core-chain`

AC3rp--AC3rt give a common rank when all affine phase-cycle maps share one rational centre or when all nonzero translations have one sign.  The remaining translation obstruction is a finite set of positive and negative increments whose interleavings may cancel.

This note replaces arbitrary cancellation histories by a finite dictionary of primitive zero-sum count vectors.  Every primitive relation has bounded length, every zero-net word decomposes into primitive relations, and after removing those relations the remaining zero-sum-free word has a length controlled by its net drift.  Thus mixed-sign translations reduce to finite relation tickets plus one bounded residual.

## Translation alphabet

Let

`B subset Z`

be the finite set of translation increments attached to the live canonical phase-cycle addresses in one fixed epoch.  Remove the zero increment as an identity quotient stutter.  Assume both signs remain and put

`P=max{b in B:b>0}`,

`N=max{-b:b in B,b<0}`.

A finite multiset of increments is a **zero-sum relation** if its total is zero.  It is **primitive** if no proper nonempty submultiset has total zero.  Since translations commute at the memory-coordinate level, a relation is represented canonically by its count vector

`m=(m_b)_(b in B)`.

This count-vector address records a cancellation relation.  It does not by itself assert that the corresponding chronological phase segment may be erased; erasure, descent or ticket payment remains an explicit contract.

## AC3ru -- primitive relation length bound -- PROVED

Every primitive zero-sum relation has total length at most

`P+N`.

The bound is sharp, for example for the relation consisting of one increment `P` and `P` copies of `-1` when `N=1`.

### Proof

Order the terms as follows.  Start with a positive term.  While both signs remain, choose a negative term when the current partial sum is positive and choose a positive term when it is negative.

Every nonfinal partial sum lies in

`[1-N,P]`.

Indeed, after a positive partial sum, adding a term at least `-N` gives a new value at least `1-N`, while after a negative partial sum, adding a term at most `P` gives a new value at most `P-1`.  The first partial sum lies in `[1,P]`.

No nonfinal partial sum is zero, because that would give a proper zero-sum submultiset.  No two nonfinal partial sums are equal, because the intervening terms would form a proper zero-sum submultiset.  The interval `[1-N,P]` contains exactly `P+N-1` nonzero integers.  Hence a primitive relation of length `ell` has

`ell-1<=P+N-1`,

so `ell<=P+N`. QED.

## AC3rv -- finite primitive relation-address stock -- PROVED

Let

`s=|B|`,

`L_rel=P+N`.

The number of primitive count-vector addresses is at most

`binom(L_rel+s,s)-1`.

### Proof

AC3ru bounds the total count `sum_b m_b` by `L_rel`.  The number of nonnegative integer count vectors on `s` coordinates with total at most `L_rel` is

`binom(L_rel+s,s)`.

Remove the zero vector.  Primitive vectors form a subset of the remaining finite stock. QED.

Thus symbolic repetition of the same relation does not create new relation addresses.

## AC3rw -- zero-sum-free residual bound -- PROVED

Let `v_1,...,v_ell` be a nonempty word over `B` containing no nonempty zero-sum submultiset, and let

`S=sum_i v_i`.

Then

`ell<=P+N+|S|`.

### Proof

Use the same opposite-sign greedy ordering as in AC3ru until one sign is exhausted, then append the remaining same-sign terms.  Because the word is zero-sum-free, all partial sums are nonzero and pairwise distinct.

During the mixed-sign part, every partial sum lies in `[-N,P]`.  Once one sign is exhausted, the remaining tail is monotone and ends at `S`.

If `S>=0`, every partial sum lies in

`[-N,max(P,S)]`.

After excluding zero, this interval contains at most

`N+max(P,S)<=P+N+S`

possible values.  If `S<0`, the symmetric interval

`[min(-N,S),P]`

contains at most `P+N+|S|` nonzero values.  Distinctness of the partial sums gives the result. QED.

In particular, if the physical memory range has width `R`, then every zero-sum-free residual occurring inside that range has at most

`P+N+R`

nonidentity translation cycles.

## AC3rx -- canonical relation decomposition -- PROVED

Every finite translation word decomposes as a disjoint multiset union of:

1. primitive zero-sum relations; and
2. one zero-sum-free residual.

The decomposition can be made canonical by repeatedly choosing the lexicographically least nonempty zero-sum count subvector and then shrinking it to the lexicographically least primitive subrelation.

The total translation increment of the original word equals the increment of the residual.

### Proof

If the current multiset contains a nonempty zero-sum submultiset, choose the canonical one and delete a proper zero-sum submultiset from it until it is primitive.  Record that primitive count vector and repeat.  Each step removes at least one occurrence, so the process terminates.  The final residual has no nonempty zero-sum submultiset.  Every removed relation has total zero, so the total increment is preserved. QED.

The relation occurrences need not be contiguous in chronological order.  AC3rx is an exact commutative memory-ledger decomposition; a phase-history theorem must still declare how each completed relation is erased, paid or ranked.

## AC3ry -- mixed-sign translation router -- PROVED UNDER THE RELATION-TICKET CONTRACT

Suppose the memory coordinate remains in an integer interval of width `R`.  Let `T_rel` be the total available ticket stock over all primitive relation addresses from AC3rv.  Assume every completed primitive relation is one of:

1. quotient-stuttering and erasable at the phase level;
2. strictly descending in a declared common rank;
3. charged to one finite ticket of its exact primitive count-vector address;
4. impossible under the physical phase contract; or
5. an outer reset.

Then one fixed mixed-sign translation epoch contains at most

`(P+N)T_rel+(P+N+R)`

nonidentity cycle occurrences after quotient erasure and before rank-decreasing or resetting exits.

### Proof

Apply AC3rx to the multiset of cycle increments.  Every charged primitive relation has length at most `P+N` by AC3ru, and there are at most `T_rel` ticketed relation occurrences.  Quotient or descending relations are removed or terminate the current rank level.  The final zero-sum-free residual has net increment bounded in magnitude by `R`, so AC3rw bounds its length by `P+N+R`.  Add the two contributions. QED.

Without a physical interval, the same theorem still produces a finite relation stock and one residual carrying the entire nonzero net drift.  That residual is an explicit unbounded translation gate rather than hidden cancellation.

## Corrected AC4 phase-memory frontier

Mixed-sign translation memory is no longer an arbitrary affine-semigroup obstruction.  It consists of:

- finitely many primitive zero-sum count-vector relations of length at most `P+N`;
- one zero-sum-free residual controlled by its net drift;
- and the explicit question whether each primitive relation erases, descends, spends a ticket or resets.

The remaining affine frontier is therefore unticketed primitive cancellation, mixed-centre nontranslation semigroups, genuinely nonlinear path memory and law changes not recorded as outer resets.  The separate weighted-capacity, nonadditive-output, unpaid-loss and non-source-ticket interfaces remain unchanged.

## Finite check

`scripts/verify_ac_mixed_sign_translation_relations.py` exhausts small mixed-sign increment alphabets and words.  It checks the primitive `P+N` length bound, finite count-vector stock, opposite-sign partial-sum proof, zero-sum-free residual bound, canonical relation extraction and the displayed ticketed occurrence budget.