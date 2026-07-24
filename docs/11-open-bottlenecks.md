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

CMR75--CMR78 neutralize every old binary same-layer star assigned to a complete
p-adic prefix block. The rematching bank preserves saturation, moves every old
block point, and has constant matching spread. CMR79--CMR81 reduce failed
rank-one repair collateral to the quotient secant-incidence energy

\[
\mathcal J_s(S)
=
\sum_{e\in\binom S2}
\sum_{\ell=0}^1 I_{s,\ell}(L_e).
\]

CMR82--CMR84 now split this energy exactly into

\[
\mathcal J_s(S)
=
2\left(\binom{2N}{2}-N(t-1)\right)
+
\mathcal M_s(S)
+
\mathcal C_s(S),
\]

where `M_s` is a weighted three-distinct-point quotient modular-syndrome energy
and `C_s` is a repeated-projection carry-direction energy over exactly
`N(t-1)` same-layer fibre pairs.

Thus the original binary-star bottleneck and its rank-one reduction are closed.
The remaining repair theorem must charge the two excess energies, sharpen the
universal endpoint baseline in CMR80, and control higher-rank matching
collateral.

### Composite-modulus open lemmas

1. **Quotient excess-energy charging.** Bound `M_s` by quotient syndrome with
   inherited line-signature multiplicity, and bound `C_s` using the primitive
   carry directions from CMR84 together with CMR14--CMR22 and CMR58--CMR66.
2. **Endpoint-baseline sharpening.** CMR79 allows `t` lifts in every successful
   endpoint rectangle, but the two forbidden matchings remove the old selected
   cells from the actual rank-one candidate set. Quantify this saving before
   inserting `J_s` into CMR81.
3. **Higher-rank prefix collateral.** Sum the normalized `T_2/(t)_2` and
   `T_3/(t)_3` terms in CMR78 or convert their concentration into a paid
   opposite-layer bank.
4. **Square-root divisor boundary.** Remove or sum the residual `sqrt(N)` terms
   in CMR61 and CMR64 for nearly singular carries.
5. **Balanced local laws for all odd primes.** Construct a comparable no-three
   fibre law for `p=3 mod 4`, or replace the reflection argument by a different
   balanced family.
6. **Joint digital construction.** Search jointly for both layers or replace the
   obstructed `64`-point first layer before attempting a lift to `128`.
7. **CRT slope-carry incompatibility.** Control simultaneous vanishing of
   `L_u,L_v`, including noncyclic zero-divisor incidences.
8. **Further finite coverage.** Exact saturated constructions are known at
   composite sizes `4,6,8,9,10,12`; `N=14` remains unresolved.

## Bottleneck 5: computational falsification

The following should be exhaustively tested for small primes:

- classify frozen one-colour cycles and their alternating anchor closures;
- distribution of \(q_s\) for real carry-filtered cycles;
- existence of alternating two-colour closures that remain jointly frozen;
- which CC3 certificate type dominates frozen examples;
- exact `M_s` and `C_s` populations by scale and line signature;
- savings from removing the two forbidden endpoint matchings;
- normalized rank-two and rank-three prefix-block collateral;
- nearly singular completed-reciprocal divisor collisions;
- balanced no-three fibre families at primes `p=3 mod 4`;
- joint two-layer digital searches;
- mixed-projection determinant distributions for CRT products.

## Recommended order of work

1. Prove the quotient excess-energy charging theorem for `M_s` and `C_s`.
2. Sharpen the endpoint baseline in CMR80.
3. Bound the aggregate rank-two and rank-three prefix collateral in CMR78.
4. Remove the square-root divisor boundary in CMR61 and CMR64.
5. Search for balanced local reciprocal laws at primes `p=3 mod 4`.
6. Build a mixed-projection-aware CRT assembly theorem.
7. Continue exact finite searches at `N=14` and beyond.
8. Search jointly for digital two-layer constructions.
9. Convert the original CC3 concentration alternatives into forced
   opposite-colour expansion.
10. Prove a termination or global-density contradiction for alternating closure.
11. Integrate both prime-field and prime-power repairs with descending scales.
