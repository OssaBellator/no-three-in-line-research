# Open bottlenecks and research roadmap

## Bottleneck 1: alternating carry-core conversion

The one-colour carry-cycle dispersion conjecture is refuted by an exact
\(p=11\) chordless four-cycle. The identity matching is the unique minimum over
all fourteen collision-free cycle-block states, even though its shift-by-two
state has constant window product and decomposes into two order-two orbit
absorbers.

The corrected universal result is Theorem CC2 in
`docs/13-carry-cycle-dispersion.md`:

\[
\min_{\pi\in\Omega} C(\pi)
\le
\frac{3T_1}{k}
+\frac{3T_2}{k(k-1)}
+\frac{3T_3}{k(k-1)(k-2)}.
\]

A frozen cycle therefore forces quantitative concentration in one of the three
certificate types.

### Corrected open lemma

Starting from a frozen one-colour cycle, add its opposite-colour secant anchors
and permit matching changes in both colour blocks. Iterate this alternating
closure. Prove that it either yields a decreasing joint state or forces a
global concentration contradiction with the bounded-displacement geometry of
the two hyperbola channels.

The \(p=11\) frozen example is unlocked by an opposite-colour anchor permutation
that reduces total potential from \(16\) to \(6\).

## Bottleneck 2: two-colour concentration conversion

For a frozen block bank, Theorem CC3 gives one of three alternatives:

- a dense one-cell outside secant shadow;
- a dense anchored pair shadow;
- a dense candidate-only triple core.

The next proof must turn each alternative into either:

1. a forced expansion to a block in the opposite channel;
2. a disjoint bank of paid defects;
3. or a contradiction with the line cap and bounded displacement multiplicity
   of the hyperbola universe.

The difficulty is preventing alternating closure from reaching a joint local
minimum supported entirely by candidate-only triples.

## Bottleneck 3: multiscale preservation

A cycle repair at one height band can create defects at lower heights.
Descending-height processing protects higher heights, but the hyperbola cycle
and alternating anchor states need a compatible reverse-scale potential and
admissibility bank.

## Bottleneck 4: all \(n\), not only \(p-1\)

The hyperbola seed naturally lives on \((p-1)\times(p-1)\). A complete proof
needs one of:

- an embedding or patching argument between nearby primes;
- a prime-power or composite-modulus analogue;
- a product construction preserving exact two-per-row/column saturation;
- a separate finite set of exceptional sizes.

The composite-modulus branch now has a complete nonlinear prime-power host,
recursive saturated banks, exact carry signatures, deterministic and random
syndrome estimates, and an executable multiscale repair bank.

For completed reciprocals and their companion layer, the current deterministic
bounds are

\[
\mathcal E=O(N^{3/2}+N\log^3N),
\qquad
T=O_p(N^2\log N).
\]

For the balanced recursive bank at primes \(p\equiv1\pmod4\), CMR67--CMR74 give

\[
\mathbb E T_k
<
4kN^2+\frac{p+2}{3}N^2.
\]

CMR75--CMR78 now neutralize every old binary same-layer star assigned to a
complete p-adic prefix block. The rematching bank preserves saturation, moves
every old block point, and has constant matching spread. CMR79--CMR81 reduce
failed rank-one repair collateral to the quotient secant-incidence energy

\[
\mathcal J_s(S)
=
\sum_{e\in\binom S2}
\sum_{\ell=0}^1 I_{s,\ell}(L_e).
\]

Thus the original vague binary-star bottleneck is closed. The remaining repair
problem is a quotient-incidence and higher-rank charging theorem.

### Composite-modulus open lemmas

1. **Quotient-incidence charging.** Split `J_s` into distinct-projection modular
   triples and repeated-projection carry stars. Charge the first part to the
   quotient syndrome and the second to the displacement/carry cells
   CMR14--CMR22 and CMR58--CMR66. Combine this with the normalized rank-two and
   rank-three collateral from CMR78.
2. **Square-root divisor boundary.** Remove or sum the residual `sqrt(N)` terms
   in CMR61 and CMR64 for nearly singular carries, closing the gap between the
   deterministic energy bound and a near-linear polylogarithmic estimate.
3. **Balanced local laws for all odd primes.** CMR67 gives exact `1/p` cell
   marginals when `p=1 mod 4`. Construct a comparable no-three fibre law for
   `p=3 mod 4`, or replace the reflection argument by a different balanced
   family.
4. **Joint digital construction.** The recorded `64`-point digital layer has no
   second-permutation completion. Search jointly for both layers or replace the
   first layer before attempting a nonlinear lift to `128`.
5. **CRT slope-carry incompatibility.** Control simultaneous vanishing of the
   local signatures `L_u,L_v`, including noncyclic zero-divisor incidences.
6. **Further finite coverage.** Exact saturated constructions are known at
   composite sizes `4,6,8,9,10,12`; `N=14` remains unresolved.

## Bottleneck 5: computational falsification

The following should be exhaustively tested for small primes:

- classify frozen one-colour cycles and their alternating anchor closures;
- distribution of \(q_s\) for real carry-filtered cycles;
- existence of alternating two-colour closures that remain jointly frozen;
- which CC3 certificate type dominates frozen examples;
- exact quotient-incidence and collision-star populations `J_s`;
- normalized rank-two and rank-three prefix-block collateral;
- nearly singular completed-reciprocal divisor collisions;
- balanced no-three fibre families at primes `p=3 mod 4`;
- joint two-layer digital searches;
- mixed-projection determinant distributions for CRT products.

## Recommended order of work

1. Prove the quotient-incidence/carry charging theorem for CMR81.
2. Bound the aggregate rank-two and rank-three prefix collateral in CMR78.
3. Remove the square-root divisor boundary in CMR61 and CMR64.
4. Search for balanced local reciprocal laws at primes `p=3 mod 4`.
5. Build a mixed-projection-aware CRT assembly theorem.
6. Continue exact finite searches at `N=14` and beyond.
7. Search jointly for digital two-layer constructions.
8. Convert the original CC3 concentration alternatives into forced
   opposite-colour expansion.
9. Prove a termination or global-density contradiction for alternating closure.
10. Integrate both prime-field and prime-power repairs with descending scales.
