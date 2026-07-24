# Open bottlenecks and research roadmap

## Bottleneck 1: alternating carry-core conversion

The one-colour carry-cycle dispersion conjecture is refuted by an exact \(p=11\) chordless four-cycle. The identity matching is the unique minimum over all fourteen collision-free cycle-block states, even though its shift-by-two state has constant window product and decomposes into two order-two orbit absorbers.

The corrected universal result is Theorem CC2 in `docs/13-carry-cycle-dispersion.md`:

\[
\min_{\pi\in\Omega} C(\pi)
\le
\frac{3T_1}{k}
+\frac{3T_2}{k(k-1)}
+\frac{3T_3}{k(k-1)(k-2)}.
\]

A frozen cycle therefore forces quantitative concentration in one of the three certificate types.

### Corrected open lemma

Starting from a frozen one-colour cycle, add its opposite-colour secant anchors and permit matching changes in both colour blocks. Iterate this alternating closure. Prove that it either yields a decreasing joint state or forces a global concentration contradiction with the bounded-displacement geometry of the two hyperbola channels.

The \(p=11\) frozen example is unlocked by an opposite-colour anchor permutation that reduces total potential from \(16\) to \(6\).

## Bottleneck 2: two-colour concentration conversion

For a frozen block bank, Theorem CC3 gives one of three alternatives:

- a dense one-cell outside secant shadow;
- a dense anchored pair shadow;
- a dense candidate-only triple core.

The next proof must turn each alternative into either:

1. a forced expansion to a block in the opposite channel;
2. a disjoint bank of paid defects;
3. or a contradiction with the line cap and bounded displacement multiplicity of the hyperbola universe.

The difficulty is preventing alternating closure from reaching a joint local minimum supported entirely by candidate-only triples.

## Bottleneck 3: multiscale preservation

A cycle repair at one height band can create defects at lower heights. Descending-height processing protects higher heights, but the hyperbola cycle and alternating anchor states need a compatible reverse-scale potential and admissibility bank.

## Bottleneck 4: all \(n\), not only \(p-1\)

The hyperbola seed naturally lives on \((p-1)\times(p-1)\). A complete proof needs one of:

- an embedding/patching argument between nearby primes;
- a prime-power or composite-modulus analogue;
- a product construction preserving exact two-per-row/column saturation;
- a separate finite set of exceptional sizes.

## Bottleneck 5: computational falsification

The following should be exhaustively tested for small primes:

- classify frozen one-colour cycles and their alternating anchor closures;
- distribution of \(q_s\) for real carry-filtered cycles;
- existence of alternating two-colour closures that remain jointly frozen;
- which CC3 certificate type dominates frozen examples;
- whether two-channel seeds with primitive ratio empirically outperform arbitrary ratios.

## Recommended order of work

1. Extend exact cycle extraction to enumerate collision-free full permutation banks.
2. Enumerate frozen cycles and alternating anchor closures up to at least \(p=101\).
3. Classify short frozen cycles symbolically.
4. Convert the CC3 concentration alternatives into forced opposite-colour expansion.
5. Prove a termination or global-density contradiction for alternating closure.
6. Integrate with descending dyadic scales.
7. Address composite \(n\).
