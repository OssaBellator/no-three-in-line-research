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

The composite-modulus branch now supplies a concrete prime-power candidate rather than only obstructions.  At \(N=p^k\), valuation-completed reciprocals are full nonlinear permutation channels; every odd-prime line intersection reduces to valuation quadratics with one possible Hensel-tangent cell; and a universal companion layer gives one saturated Hamiltonian alternating cycle.  The current line and one-channel syndrome bounds are

\[
O(\sqrt N+\log N)
\quad\text{and}\quad
O(N^{5/2}+N^2\log N),
\]

respectively.  They are rigorous but too large for the repair endpoint.

### Composite-modulus open lemmas

1. **Exact-real tangent-cell bound.**  Starting from the top-stratum congruence
   \[
   (2AU-C_h)^2\equiv C_h^2-4ABc_h\pmod {p^{k-h}},
   \]
   exploit the exact integer line equation and standard-box bounds to prove a divisor-sensitive bound substantially smaller than the modular square-root count.
2. **Same-channel displacement multiplicity.**  Upgrade the reduced signature
   \[
   uv\equiv-c_r\alpha\beta^{-1}\pmod {p^{k-t}}
   \]
   to a small bound for exact lifted secants, including cross-stratum endpoint pairs.
3. **Companion cross-channel syndrome.**  Classify secants and triples between \(R_{\mathbf c}\) and \(\sigma_p\circ R_{\mathbf c}\), retaining the Hamiltonian row-column graph while reducing total syndrome toward \(O(N\log^C N)\).
4. **Recursive digital lifting.**  Extend the exact binary digit-linear no-three channels at \(N=8,16,32\) to an infinite matrix family, or identify a finite obstruction to such lifting.
5. **Mixed-projection CRT assembly.**  Add signatures that handle triples where different pairs collapse in different CRT factors; local line caps alone cannot exclude these triples.

## Bottleneck 5: computational falsification

The following should be exhaustively tested for small primes:

- classify frozen one-colour cycles and their alternating anchor closures;
- distribution of \(q_s\) for real carry-filtered cycles;
- existence of alternating two-colour closures that remain jointly frozen;
- which CC3 certificate type dominates frozen examples;
- whether two-channel seeds with primitive ratio empirically outperform arbitrary ratios;
- exact tangent-cell populations for completed reciprocals under varied stratum parameters;
- same- and cross-channel displacement multiplicities of companion pairs;
- recursive extensions of the binary digit-linear matrices;
- mixed-projection determinant distributions for CRT products.

## Recommended order of work

1. Prove an exact-real tangent-cell divisor bound for completed reciprocals.
2. Convert the same-stratum secant quadratic into an exact displacement-multiplicity bound and classify cross-stratum secants.
3. Derive the companion cross-channel determinant equation and count its triple syndrome.
4. Search for recursive digit-linear matrices while the prime-power algebra is being sharpened.
5. Extend exact cycle extraction to enumerate collision-free full permutation banks.
6. Enumerate frozen cycles and alternating anchor closures up to at least \(p=101\).
7. Classify short frozen cycles symbolically.
8. Convert the CC3 concentration alternatives into forced opposite-colour expansion.
9. Prove a termination or global-density contradiction for alternating closure.
10. Integrate with descending dyadic scales.
11. Build a mixed-projection-aware CRT assembly theorem or a separate coverage argument for composite \(n\).
