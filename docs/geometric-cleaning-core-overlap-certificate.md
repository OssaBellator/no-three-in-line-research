# Geometric-cleaning irreducible cause-core overlap

This note continues the canonical irreducible cause-core result on the same
complete finite cleaning network. It identifies the exact shared-capacity
competition that any remaining geometric estimate must exclude or pay.

## Contract

For a cause set `S`, let `d(S)` be total cause demand, `F(S)` the maximum
physical/remedy/height flow with only causes in `S` enabled, and
`Delta(S)=d(S)-F(S)`. Retain every physical-source, remedy, height and cause
address and every compatibility edge.

Let `C` be the canonical minimum-cardinality deficient cause core and put
`delta=Delta(C)>0`. Every proper subset of `C` is fully payable.

## GC2ka--GC2ke

1. Every nonempty proper `A subset C` satisfies `F(A)=d(A)`.
2. Every nontrivial partition `C=A disjoint_union B` has exact competition
   `Omega(A,B)=F(A)+F(B)-F(C)=delta`.
3. If `|C|>=2`, the least balanced complete-address split is a canonical
   remedy-height competition witness of size `delta`; a singleton core is a
   direct local cause shortage.
4. Any geometric decomposition producing additive payment across one split, or
   an overlap upper bound below `delta`, rules out the core.
5. Omitted remedy or height edges, merged physical sources, nonlinear height
   costs not represented in the state, changed cleaning state or independent
   reuse of shared capacity is a reset.

## Consequence

The remaining GC obstruction is either one direct cause shortage or two
separately payable cause families whose physical/remedy/height optima overlap by
exactly the whole deficit. The next geometric task is to separate a canonical
split or charge the exact overlap to a named physical source or height account.

## Scope

This theorem is conditional on the complete fixed network and exact subset
max-flow values. It does not prove GC5 or the no-three-in-line conjecture.
