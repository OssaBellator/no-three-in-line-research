# Alternating-core irreducible defect-core overlap

This note continues the canonical irreducible-core result on the same complete
finite payment network.  It does not construct the physical network; it
identifies the exact shared-capacity obstruction that any remaining physical
estimate must exclude or pay.

## Contract

Fix the complete finite integral network and its exact terminal demands.
For a terminal set `S`, let

- `d(S)` be its total demand;
- `F(S)` be the maximum flow when only terminals in `S` are enabled;
- `Delta(S)=d(S)-F(S)` be its unpaid deficit.

All source, intermediate, compatibility, type and terminal addresses used by
the physical state are retained.  Capacities are shared exactly as in the
complete network.

Let `C` be the canonical minimum-cardinality deficient core from the preceding
theorem block and put `delta=Delta(C)>0`.  Hence every proper subset of `C` is
fully payable.

## AC5dr--AC5dv

1. **Proper-set payment.** For every nonempty proper `A subset C`,
   `F(A)=d(A)`.

2. **Exact bipartition overlap.** For every nontrivial disjoint partition
   `C=A disjoint_union B`, define the shared-capacity competition
   ```
   Omega(A,B)=F(A)+F(B)-F(C).
   ```
   Then
   ```
   Omega(A,B)=delta.
   ```
   Indeed, both proper sides are payable while
   `F(C)=d(C)-delta`.

3. **Canonical witness.** If `|C|>=2`, the least balanced complete-address
   bipartition is a finite canonical witness carrying exactly `delta` units of
   competition.  If `|C|=1`, the unique terminal is already a direct local
   shortage witness of size `delta`.

4. **Separability exclusion.** Any physical argument producing one nontrivial
   partition of `C` with additive payment
   `F(C)=F(A)+F(B)` rules out the core.  More generally, an upper bound
   `Omega(A,B)<delta` contradicts deficiency.

5. **Address preservation.** The witness retains every defect
   address and every physical/source/certificate payment address.  Omitted compatibility,
   merged capacity, suppressed type data, changed physical state or independent
   reuse of shared capacity is a reset rather than a paid core.

## Consequence

The remaining frontier is no longer an arbitrary Hall cut.  It is either one
direct singleton shortage or a finite pair of payable terminal families whose
separate optima overlap by exactly the whole deficit.  The next physical step
is therefore to prove additive separability for a canonical split, bound the
overlap below `delta`, or charge that exact overlap to a named finite source.

## Scope

This theorem is conditional on the complete fixed network and exact subset
max-flow values.  It does not prove AC4, AC5, AC6 or the no-three-in-line conjecture.
