# Bounded-denominator irreducible restoration-core overlap

This note continues the canonical irreducible-core result on the same complete
finite payment network. It does not construct the physical network; it
identifies the exact shared-capacity obstruction that any remaining physical
estimate must exclude or pay.

## Contract

Fix the complete finite integral network and its exact terminal demands. For a
terminal set `S`, let `d(S)` be its total demand, `F(S)` the maximum flow when
only terminals in `S` are enabled, and `Delta(S)=d(S)-F(S)` its unpaid deficit.
All physical-potential, source-potential, arithmetic-compatibility and
restoration addresses are retained.

Let `C` be the canonical minimum-cardinality deficient core from the preceding
theorem block and put `delta=Delta(C)>0`. Hence every proper subset of `C` is
fully payable.

## BDA5fc--BDA5fg

1. For every nonempty proper `A subset C`, `F(A)=d(A)`.
2. For every nontrivial partition `C=A disjoint_union B`, define
   `Omega(A,B)=F(A)+F(B)-F(C)`. Then `Omega(A,B)=delta`.
3. If `|C|>=2`, the least balanced complete-address bipartition is a canonical
   finite restoration-competition witness of size `delta`. If `|C|=1`, the
   unique restoration address is a direct local shortage witness.
4. Any arithmetic argument producing one split with additive payment
   `F(C)=F(A)+F(B)`, or merely `Omega(A,B)<delta`, excludes the core.
5. Omitted gain fields, compatibility edges, merged potential sources, changed
   denominator states or independent reuse of primitive-potential capacity is a
   reset rather than a paid core.

## Consequence

The remaining arithmetic obstruction is either one direct restoration shortage
or two separately payable restoration families whose primitive-potential
optima overlap by exactly the whole deficit. The next step is to prove
additive separability for a canonical split, bound this overlap below `delta`,
or charge it to a named finite potential source.

## Scope

This theorem is conditional on the complete fixed network and exact subset
max-flow values. It does not prove BDA6 or the no-three-in-line conjecture.
