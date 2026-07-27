# SCC residue quotient for mixed-sign one-counter memory

**Branch:** `research/alternating-core-chain`

AC3st--AC3sx give a common shortest-path rank when every simple-cycle drift has one sign.  The
remaining finite-control additive obstruction is a strongly connected component containing both
positive and negative cycle drifts.  This note removes the arbitrary path history from that case.
Every such component has one exact closed-walk gcd, one control-state residue potential, and one
normalized integer lift.

The quotient does not by itself terminate an unbounded mixed-sign lift.  It does show that no
additional chronological word or count ledger is needed: after one invariant residue is fixed, all
remaining numerical freedom is a single primitive integer coordinate.

## Strongly connected counter model

Fix one strongly connected directed control graph `Y` with `q>=1` vertices.  Every directed edge

`e:u->v`

has an integer counter increment `b_e` satisfying `|b_e|<=W`.  The live update is

`c'=c+b_e`.

All guards, zero tests, payment balances and terminal fields affecting future legality are included
in the control vertex.  A change of graph, edge increment or interpretation is an outer reset.

Choose a root `r`.  For each vertex `v`, choose one simple directed path `P_v` from `r` to `v` and
put

`p(v)=drift(P_v)`.

Thus `p(r)=0` and `|p(v)|<=(q-1)W`.  For an edge `e:u->v`, define its exact residue address

`a_e=p(u)+b_e-p(v)`.

Let

`g=gcd{|a_e|:e in E}`,

with `g=0` when every `a_e` is zero.

## AC3sy -- finite edge-address gcd equals the closed-walk gcd -- PROVED

The integer `g` is exactly the gcd of the drifts of all directed closed walks in the component.
Moreover,

`|a_e|<=(2q-1)W`

for every edge, so the gcd is obtained from a finite edge dictionary.

### Proof

For a walk `A=e_1...e_m` from `r` to `v`, summing the edge addresses telescopes:

`drift(A)-p(v)=sum_i a_(e_i)`.

In particular, for a closed walk based at `r`, its drift is a sum of edge addresses.  Hence the gcd
of the edge addresses divides every root-based closed-walk drift.

For a closed walk `C` based at an arbitrary vertex `v`, compare the two `r`-to-`v` walks `P_v` and
`P_v C`.  Their drift difference is `drift(C)`, while each drift minus `p(v)` is a sum of edge
addresses.  Thus `g` divides every closed-walk drift.

Conversely, `a_e` is the drift difference between the two `r`-to-`v` walks `P_u e` and `P_v`.
Append any fixed directed path from `v` back to `r`; `a_e` becomes the difference of two closed-walk
drifts.  Therefore the closed-walk gcd divides every `a_e`.  The two gcds are equal.  The size bound
follows from the path bounds and `|b_e|<=W`. QED.

## AC3sz -- exact control-state residue invariant -- PROVED

If `g>0`, every legal transition preserves

`xi=c-p(v) mod g`.

Equivalently, every two walks with the same initial and final control vertices have counter drifts
congruent modulo `g`.

If `g=0`, the stronger exact invariant

`xi=c-p(v)`

is preserved, and every directed closed walk has zero drift.

### Proof

Across `e:u->v`,

`(c+b_e)-p(v)=[c-p(u)]+a_e`.

AC3sy gives `g|a_e` when `g>0`, proving modular invariance.  When `g=0`, every edge address is zero,
so equality holds over the integers.  The path statement follows by summing along the walk. QED.

## AC3ta -- primitive normalized lift -- PROVED

Assume `g>0` and fix the invariant residue `xi` of one epoch.  Define

`ell=(c-p(v)-xi)/g`.

Then `ell` is an integer and an edge `e` updates it by

`ell'=ell+alpha_e`,

where

`alpha_e=a_e/g`.

The finite increment alphabet `{alpha_e}` has gcd one and satisfies

`|alpha_e|<=(2q-1)W/g`.

Thus all mixed-sign chronology inside the component is represented by the current control vertex
and one primitive integer lift.

### Proof

Integrality follows from AC3sz.  Substitute the counter update and divide the identity in the proof
of AC3sz by `g`.  The gcd of the `alpha_e` values is one by the definition of `g`; the magnitude
bound is AC3sy divided by `g`. QED.

No word, count vector or ordering label remains in the live numerical state.

## AC3tb -- bounded exact-lift stock -- PROVED

Suppose the physical counter is restricted to an interval `[L,U]` of width `R=U-L`.

- If `g>0`, one fixed residue epoch has at most

  `N_lift=q*(floor(R/g)+1)`

  exact states `(v,c)`.
- If `g=0`, one fixed exact invariant has at most `q` exact states.

Consequently every history with at least the corresponding number of transitions repeats one exact
state.  Every cycle-free residual segment is shorter than that stock.

### Proof

For a fixed vertex `v` and residue `xi`, feasible counter values form one arithmetic progression of
step `g` inside an interval of width `R`, so there are at most `floor(R/g)+1`.  Sum over the `q`
vertices.  When `g=0`, the exact invariant forces `c=xi+p(v)`, giving at most one value per vertex.
Pigeonhole gives the recurrence and cycle-free bounds. QED.

This sharpens the naive `q(R+1)` stock whenever `g>1`.

## AC3tc -- mixed-sign SCC residue router -- PROVED UNDER THE SCC-LIFT CONTRACT

Every fixed strongly connected finite-control additive counter component has one exact continuation:

1. `g=0`, giving an exact control-state potential and only zero-drift closed walks;
2. `g>0` with a bounded lift, giving the finite state stock `N_lift` from AC3tb;
3. `g>0` with an unbounded lift whose complete live numerical state is the primitive one-counter
   system `(v,ell)` with finite increment alphabet `{alpha_e}`;
4. or failure of strong connectivity, the fixed-edge law, the complete control-state contract or the
   declared outer-reset boundary.

If positive and negative closed-walk drifts both occur, they survive in alternative 3 as positive
and negative integer lift cycles, but no additional path memory survives the quotient.

### Proof

Apply AC3sy--AC3ta.  If the physical range is bounded, use AC3tb.  Otherwise retain the normalized
lift.  All excluded cases are exactly the hypotheses used to define the component and its edge
addresses. QED.

## Corrected AC4 numerical frontier

Mixed-sign finite-control additive memory is now reduced to a primitive SCC lift.  The remaining
numerical work is execution or cancellation of positive/negative lift cycles, a secondary rank or
finite tickets for zero-sum lift relations, dynamic or unbounded control graphs, nonadditive updates,
omitted guards or balances, and changes of law not declared as outer resets.

## Finite check

`scripts/verify_ac_scc_counter_residue.py` samples strongly connected weighted control graphs and
exact-potential systems.  It checks the edge-address gcd, path and closed-walk congruences, the
`(2q-1)W` address bound, exact `g=0` potentials, primitive normalized increments and the bounded
`q(floor(R/g)+1)` state stock.