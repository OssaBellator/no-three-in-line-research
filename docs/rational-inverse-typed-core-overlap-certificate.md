# Rational-inverse typed irreducible-core overlap

This note continues the canonical typed irreducible-core result on the same
complete finite payment network. It identifies the exact shared-capacity
competition that the remaining arithmetic argument must exclude or pay.

## Contract

For a typed terminal set `S`, let `d(S)` be total owner/charge demand, `F(S)`
the maximum flow with only `S` enabled, and `Delta(S)=d(S)-F(S)`. Retain every
owner or charge type, physical-source address, collateral address and arithmetic
compatibility edge.

Let `C` be the canonical minimum-cardinality deficient typed core and put
`delta=Delta(C)>0`. Every proper subset of `C` is fully payable.

## RI5et--RI5ex

1. Every nonempty proper `A subset C` satisfies `F(A)=d(A)`.
2. Every nontrivial partition `C=A disjoint_union B` has exact competition
   `Omega(A,B)=F(A)+F(B)-F(C)=delta`.
3. If `C` contains both owner and charge addresses, the owner-versus-charge
   split is a canonical typed witness with overlap exactly `delta`. If the core
   is type-homogeneous and non-singleton, use the least balanced complete-address
   split. A singleton is already a direct local typed shortage.
4. Any arithmetic decomposition giving additive collateral payment across one
   retained split excludes the core; an overlap bound below `delta` also
   contradicts deficiency.
5. Suppressing the owner/charge type, merging collateral sources, omitting
   arithmetic compatibility, changing retained owner/coherence/context fields,
   or reusing shared collateral independently is a reset.

## Consequence

A remaining RI obstruction is either one direct typed shortage or two separately
payable typed families whose collateral optima overlap by the entire deficit.
The physical arithmetic task is to separate one canonical split or charge its
exact overlap to a named owner-source account.

## Scope

This theorem is conditional on the complete fixed typed network and exact subset
max-flow values. It does not prove RI6 or the no-three-in-line conjecture.
