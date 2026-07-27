# Chronological realization of primitive lift-cycle relations

**Branch:** `research/alternating-core-chain`

AC3td--AC3th reduce every normalized mixed-sign SCC walk to exact simple-cycle addresses,
primitive zero-sum count-vector relations and one zero-sum-free residual.  The remaining caveat is
chronological: the cycles in one primitive relation may occur at different control vertices and at
different positions in the original walk.

This note gives every primitive relation one canonical executable root-based macro word.  The cycle
drifts cancel exactly.  The only remaining drift is the bounded cost of the canonical connector
paths.  Those connector defects form another finite translation alphabet, and because every macro
starts and ends at the same root, primitive relations among the defects are genuine chronological
exact returns rather than noncontiguous ledger identities.

## Rooted connector model

Fix one normalized strongly connected control graph with:

- `q>=1` control vertices;
- integer edge increments `alpha_e` with `|alpha_e|<=A`;
- one root vertex `r`;
- the exact canonical simple-cycle address set `C` from AC3td.

For every ordered pair of control vertices `(u,v)`, choose the lexicographically least shortest
directed path

`P_(u,v)`

from `u` to `v`.  Strong connectivity guarantees its existence, and a shortest path is simple, so

`length(P_(u,v))<=q-1`,

`|drift(P_(u,v))|<=(q-1)A`.

For a simple cycle `C`, let `b(C)` be the starting vertex of its canonical cyclic rotation.

In the mixed-sign branch, let the nonzero simple-cycle drifts have extrema

`P=max{d(C):d(C)>0}`,

`N=max{-d(C):d(C)<0}`.

AC3te gives primitive relation length

`L_rel=P+N`

and primitive relation-address stock

`K_rel=binom(P+N+s,s)-1`,

where `s` is the number of exact nonzero-drift simple-cycle addresses.

## AC3ti -- finite canonical connector dictionary -- PROVED

The rooted connector dictionary contains at most `q^2` exact path addresses.  Every connector has
length at most `q-1` and drift magnitude at most `(q-1)A`.

### Proof

There is one chosen path for each ordered pair of vertices.  A shortest directed path cannot repeat
a vertex, since deleting the intervening closed segment would shorten it.  Hence it uses at most
`q-1` edges.  Summing the edge-increment bound gives the drift bound. QED.

A change of root, graph, edge law or connector tie-breaking rule is an outer reset.

## AC3tj -- canonical chronological macro for one primitive relation -- PROVED

Let `rho` be one primitive exact-cycle relation.  Expand its count vector into the canonical
lexicographically ordered list

`C_1,...,C_k`,

where `k<=P+N`.  Define the rooted chronological word

`W_rho=P_(r,b(C_1)) C_1 P_(b(C_1),b(C_2)) C_2 ... C_k P_(b(C_k),r)`.

Then `W_rho` is one legal closed control walk based at `r`.  Its length satisfies

`length(W_rho)
 <=k*q+(k+1)(q-1)
 <=(2q-1)(P+N)+(q-1)`.

Its lift drift is exactly the connector defect

`beta_rho=sum of the connector-path drifts in W_rho`,

and

`|beta_rho|
 <=(k+1)(q-1)A
 <=(P+N+1)(q-1)A`.

### Proof

Every connector ends at the base of the next canonical cycle, and the final connector returns to
`r`, so the concatenation is a legal rooted closed walk.  Each simple cycle has length at most `q`;
AC3ti bounds the `k+1` connectors.

The cycle part of the word has total drift

`sum_i d(C_i)=0`

because `rho` is a relation.  Therefore only connector drifts remain.  The absolute-value estimate
follows by summing the connector bounds. QED.

Thus every noncontiguous primitive relation has one finite chronological representative.

## AC3tk -- finite transport-defect gate stock -- PROVED

There is at most one rooted macro address `W_rho` for each primitive relation address, so the macro
stock is at most `K_rel`.

Let `M_*` be the exact macro addresses with nonzero connector defect and put

`s_tr=|M_*|`,

`B_tr=(P+N+1)(q-1)A`.

Then every nonzero defect lies in `[-B_tr,B_tr]`.  Moreover:

1. if `beta_rho=0`, `W_rho` is an exact chronological root return;
2. if all nonzero defects have one weak sign, the root-boundary lift is monotone under every
   completed relation macro;
3. if both signs occur, define

   `P_tr=max{beta_rho:beta_rho>0}`,

   `N_tr=max{-beta_rho:beta_rho<0}`.

### Proof

The stock and magnitude bounds are AC3te and AC3tj.  A zero connector defect makes the rooted closed
word lift-neutral.  At root boundaries, completing `W_rho` changes the lift by exactly `beta_rho`,
so a common sign gives a macro-boundary monotone rank.  The final quantities are finite extrema of
the mixed-sign exact macro dictionary. QED.

The rank in item 2 is a macro-boundary rank; the lift may fluctuate inside one macro word.

## AC3tl -- primitive transport-defect relations are chronological exact returns -- PROVED

Assume both signs occur in the transport-defect alphabet.  A primitive nonnegative count vector on
the exact macro addresses `M_*` whose weighted defect sum is zero has total macro count at most

`P_tr+N_tr`.

The number of primitive exact macro-relation addresses is at most

`K_tr=binom(P_tr+N_tr+s_tr,s_tr)-1`.

Concatenate the root-based macros in the canonical lexicographic order prescribed by such a count
vector.  The result is a genuine chronological exact root return.  Its edge length is at most

`(P_tr+N_tr)*L_mac`,

where

`L_mac=(2q-1)(P+N)+(q-1)`.

### Proof

Treat the exact macro addresses as a finite mixed-sign integer alphabet whose values are their
connector defects.  The opposite-sign partial-sum proof of AC3ru gives the `P_tr+N_tr` primitive
length bound even when different macro addresses have equal defect.  Counting nonnegative vectors
of bounded total gives `K_tr`.

Every macro begins and ends at the same root.  Hence the macros may be concatenated in the canonical
order without any additional connector.  Their defect sum is zero, so the concatenation returns to
the same control vertex and lift.  AC3tj bounds the length of every constituent macro. QED.

This removes the earlier noncontiguity caveat at the second relation level.

## AC3tm -- chronological mixed-sign lift router -- PROVED UNDER THE ROOT-MACRO CONTRACT

Every fixed normalized mixed-sign SCC lift has one exact continuation:

1. one first-level primitive cycle relation has zero connector defect and yields a finite exact
   chronological root-return gate;
2. all nonzero connector defects have one sign and give a common root-boundary monotone rank;
3. mixed connector defects yield the finite second-level exact root-return stock `K_tr`, with each
   return word of length at most `(P_tr+N_tr)L_mac`;
4. a bounded lift closes after the exact return gates are erased, descended, paid by finite tickets,
   declared impossible or sent to an outer reset;
5. an unbounded zero-sum-free residual carries the complete nonzero net lift drift;
6. or the SCC, connector, legality, augmented-state, exact-return-ticket or outer-reset contract
   fails at one named field.

### Proof

Apply AC3ti--AC3tk to every primitive relation from AC3te.  Zero and sign-coherent defects give the
first two branches.  In the mixed branch apply AC3tl.  The resulting second-level words are actual
rooted chronological returns, so only their declared erasure, descent, payment, impossibility or
reset treatment remains.  AC3tf continues to isolate the unbounded zero-sum-free residual. QED.

## Corrected AC4 numerical frontier

Primitive SCC lift relations no longer remain merely noncontiguous count-vector identities.  Every
one has a canonical chronological root macro with bounded transport defect; mixed defects themselves
produce a finite stock of exact chronological root returns.

The remaining numerical work is discharge of unticketed exact root-return gates, a physical or
rank payment for those gates, unbounded zero-sum-free lift residuals, dynamic or unbounded control
graphs, nonadditive updates, omitted guards or balances, and changes of law not declared as outer
resets.

## Finite check

`scripts/verify_ac_chronological_lift_relation_gates.py` samples strongly connected normalized
control graphs, enumerates canonical simple cycles, constructs primitive mixed-sign relations and
their rooted macro words, and checks legality, closure, cycle-drift cancellation, connector-defect
identities, macro length bounds, finite defect stocks and second-level exact root returns.