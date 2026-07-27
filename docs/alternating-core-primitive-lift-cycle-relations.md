# Primitive cycle relations in a mixed-sign SCC lift

**Branch:** `research/alternating-core-chain`

AC3sy--AC3tc remove arbitrary chronological memory from a strongly connected finite-control counter component.  After fixing the invariant residue, the live numerical state is one primitive integer lift

`ell' = ell + alpha_e`

on a finite directed control graph.  The remaining obstruction is a component containing positive and negative closed-walk drifts.

This note reduces that obstruction to a finite dictionary of exact simple-cycle addresses, finitely many primitive zero-sum relations among those addresses, and one zero-sum-free residual.  The relation occurrences need not be contiguous in the original walk, so erasure or payment remains an explicit contract.

## Normalized SCC model

Fix a strongly connected directed graph with:

- `q>=1` control vertices;
- `m>=1` directed edge addresses;
- normalized integer increments `alpha_e`;
- `A=max_e |alpha_e|`.

A directed simple cycle may be a loop of length one.  Give every simple cycle its canonical address: the lexicographically least cyclic rotation of its edge-ID word.  Let `C` be the finite set of exact canonical simple-cycle addresses and write

`d(C)=sum_(e in C) alpha_e`

for the lift drift of `C`.

Zero-drift cycles are retained as exact recurrence addresses.  In the mixed-sign branch, let `C_*` be the nonzero-drift addresses and put

`P=max{d(C):d(C)>0}`,

`N=max{-d(C):d(C)<0}`,

`s=|C_*|`.

## AC3td -- finite simple-cycle address decomposition -- PROVED

Every finite directed walk decomposes into:

1. one directed simple residual path of length at most `q-1`; and
2. a multiset of directed simple-cycle addresses, each of length at most `q`.

The exact lift displacement is the residual-path displacement plus the sum of the cycle drifts.

Moreover,

`|C| <= sum_(j=1)^q m^j`.

### Proof

Repeatedly find the first repeated control vertex in the current walk, delete the intervening closed segment, and record it.  Apply the same deletion recursively inside every recorded closed segment until each recorded component has no repeated internal vertex.  The remaining path and every recorded cycle are simple.  Additivity of the edge increments preserves the exact displacement identity.

A simple path has at most `q-1` edges and a simple cycle at most `q`.  Every canonical cycle address has an edge word of some length `1<=j<=q`, and there are at most `m^j` such words before imposing incidence or simplicity, giving the safe stock bound. QED.

## AC3te -- primitive exact-cycle relation stock -- PROVED

A **cycle relation** is a nonzero count vector

`u=(u_C)_(C in C_*)`

satisfying

`sum_C u_C d(C)=0`.

It is primitive when no proper nonzero count subvector is a relation.  Every primitive cycle relation has total cycle count at most

`L_rel=P+N`.

Consequently the number of primitive exact-cycle relation addresses is at most

`K_rel=binom(P+N+s,s)-1`.

### Proof

Treat the exact cycle addresses as a finite mixed-sign integer alphabet whose values are their drifts.  The opposite-sign partial-sum proof of AC3ru applies without identifying two different cycle addresses that happen to have the same drift: a primitive zero-sum multiset has at most `P+N` terms.

A relation address is a nonnegative integer vector on `s` coordinates with total at most `P+N`.  There are `binom(P+N+s,s)` such vectors including zero.  Primitive relations form a subset after removing zero. QED.

Thus repetition of one relation does not create a new symbolic address.

## AC3tf -- canonical walk relation decomposition -- PROVED

Let a finite normalized-lift walk have total lift displacement `Delta`.  Apply AC3td and remove every zero-drift simple cycle as a separate exact zero-cycle address.  The remaining nonzero cycle multiset decomposes canonically into:

1. primitive cycle relations; and
2. one cycle multiset containing no nonempty zero-sum submultiset.

If `S` is the drift of that residual cycle multiset, then

`S=Delta-d_path`,

where `d_path` is the residual-path drift, and its number of cycle occurrences is at most

`P+N+|Delta|+(q-1)A`.

### Proof

Repeatedly choose the lexicographically least nonzero zero-sum count subvector of the current cycle multiset and shrink it to the lexicographically least primitive subrelation.  Each step deletes at least one cycle occurrence, so the procedure terminates and leaves a zero-sum-free residual.  Removed relations have drift zero, hence the residual cycle drift is `S=Delta-d_path`.

AC3rw applied to the exact cycle-address alphabet bounds the residual cycle count by `P+N+|S|`.  The residual path has at most `q-1` edges, so `|d_path|<=(q-1)A`.  Therefore

`|S|<=|Delta|+(q-1)A`,

which gives the displayed bound. QED.

The extracted relations may combine cycles based at different control vertices and appearing at different chronological positions.  AC3tf is an exact lift-ledger decomposition, not an automatic phase-history erasure.

## AC3tg -- bounded-lift ticketed transition bound -- PROVED UNDER THE CYCLE-RELATION CONTRACT

Suppose the normalized lift remains in an integer interval of width `R`.  Let:

- `T_0` be the total available ticket stock for exact zero-drift simple-cycle occurrences;
- `T_rel` be the total available ticket stock for primitive exact-cycle relation occurrences.

Assume every completed zero cycle and every completed primitive relation is quotient-stuttering, strictly descending, charged to one finite exact ticket, impossible, or an outer reset.

Then before a descending or resetting exit, the number of simple-cycle occurrences is at most

`C_occ=T_0+(P+N)T_rel+P+N+R+(q-1)A`.

The number of internal edge transitions is therefore at most

`q*C_occ+(q-1)`.

### Proof

Every ticketed zero cycle contributes one cycle occurrence, giving at most `T_0`.  Every ticketed primitive relation contains at most `P+N` cycle occurrences by AC3te, giving at most `(P+N)T_rel`.  Quotient-stuttering relations are erased, while descending or resetting relations end the current level or epoch.

For the final zero-sum-free residual, both endpoints lie in the same width-`R` lift interval, so `|Delta|<=R`.  AC3tf bounds its nonzero cycle count by `P+N+R+(q-1)A`.  Add the three contributions.  Each simple cycle contains at most `q` edges and the residual path at most `q-1`, proving the transition bound. QED.

## AC3th -- primitive mixed-sign lift router -- PROVED UNDER THE SIMPLE-CYCLE TICKET CONTRACT

Every fixed finite-control normalized SCC lift has one exact continuation:

1. all simple-cycle drifts have one weak sign, so AC3sx supplies a common monotone rank;
2. one zero-drift simple cycle gives a finite exact quotient or ticket address;
3. positive and negative simple-cycle drifts occur, giving the finite primitive relation stock of AC3te and the canonical relation/residual decomposition of AC3tf;
4. in a bounded lift interval, the cycle-relation contract gives the explicit AC3tg transition bound;
5. in an unbounded lift, one zero-sum-free residual carries the complete nonzero net drift;
6. or the fixed SCC, edge-law, augmented-state, relation-ticket or outer-reset contract fails at one named field.

### Proof

Use AC3td to inspect the finite simple-cycle drift dictionary.  The sign-coherent branch is AC3sx.  In the mixed-sign branch apply AC3te--AC3tf, and use AC3tg when the lift is bounded.  All excluded cases are exactly the hypotheses used to define the finite normalized lift and its relation ledger. QED.

## Corrected AC4 numerical frontier

A mixed-sign primitive SCC lift is no longer an arbitrary cancellation history.  It consists of finitely many exact zero cycles, finitely many primitive zero-sum relations of at most `P+N` simple cycles, and one zero-sum-free residual carrying the full net drift.

The remaining numerical work is discharge of unticketed primitive lift relations, a secondary rank or physical payment for those relations, unbounded net-lift residuals, dynamic or unbounded control graphs, nonadditive updates, omitted guards or balances, and changes of law not declared as outer resets.

## Finite check

`scripts/verify_ac_primitive_lift_cycle_relations.py` exhausts small mixed-sign cycle-drift alphabets and samples normalized strongly connected walks.  It checks simple-path/cycle decomposition, exact displacement, primitive `P+N` relation bounds, canonical relation extraction, zero-sum-free residual bounds and the bounded-lift ticket formula.