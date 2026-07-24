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
syndrome estimates, and two executable multiscale repair banks.

For completed reciprocals and their companion layer, the deterministic bounds
are

\[
\mathcal E=O(N^{3/2}+N\log^3N),
\qquad
T=O_p(N^2\log N).
\]

For the corrected balanced recursive bank at primes
\(p\equiv1\pmod4\), CMR67--CMR74 give

\[
\mathbb E T_k
<
4(k-1)N^2+\frac{p+3}{3}N^2.
\]

CMR75--CMR84 construct full prefix-block rematching banks, neutralize every old
binary same-layer star assigned to a block, and decompose failed rank-one
collateral into endpoint, modular-third-point, and repeated-projection terms.
CMR85--CMR89 remove the endpoint baseline and prove total expected rank-one
collateral

\[
O_p(N^2\log^2N).
\]

CMR90--CMR92 close the normalized higher-rank terms universally:

\[
\sum_{a,\ell}\frac{T_2}{(t)_2}<2N^2,
\qquad
\sum_{a,\ell}\frac{T_3}{(t)_3}<\frac{N^2}{3p}.
\]

CMR93--CMR95 prove fine-to-coarse invariance of every unprocessed quotient
charge. CMR96--CMR101 add a recursive-compatible reciprocal node bank and cancel
all triples wholly inside one rigidly translated child subtree.

CMR102 shows that direct descent of the remaining weak node-rank-one class to
the ordinary finer prefix bank is impossible. CMR103--CMR106 replace it by the
support-pruned vertical pencil

\[
\mathcal V_\Omega(A)
=
\sum_{(\xi,\eta)\text{ supported}}W(\xi,\eta).
\]

CMR107--CMR109 close the pencil-mass problem as a dichotomy. A concentrated
one- or two-point pencil exposes an alternating endpoint bank of size at least
seven. If no such bank exists, the total expected weak pencil collateral over
all nodes at one depth is less than

\[
240N^2.
\]

CMR110 improves every degree-two forbidden matching bank from the original
constant `128` to

\[
|\Omega(F)|\ge\frac{t!}{72},
\qquad
\Pr(Q\subseteq\pi)\le\frac{72}{(t)_r}.
\]

CMR111 makes the extraction quantitative: the star size is proportional to the
pencil mass. CMR112 proves that if the extracted bank is frozen, then one of its
three normalized collateral ranks satisfies

\[
\frac{T_r}{(t)_r}\ge\frac{t}{216}.
\]

Thus local-bank construction, quotient charging, endpoint removal, higher-rank
prefix collateral, internal child-core cancellation, and vertical-pencil
concentration are closed. The remaining recursive problem is the same
alternating concentration-conversion problem as on the main branch, now attached
to an explicit p-adic node, scale, and star size.

### Composite-modulus open lemmas

1. **Alternating pencil concentration conversion.** Starting from the CMR112
   rank-`1/2/3` certificate, force either a decreasing joint parent/endpoint
   state, a paid quotient or carry defect, or expansion to an opposite-layer
   node bank.
2. **Termination after coarse repairs.** CMR93 protects unprocessed coarser
   quotients, but a later coarse repair may recreate fine stars. Prove that the
   reintroduced fine mass is paid by the coarse potential decrease or by a
   lexicographic scale budget.
3. **Sharper modular quotient syndrome.** Improve the current
   `O_p(sm^2)` bound for `Z_s`, or exploit inherited primitive line signatures to
   beat the raw factor `3t^2` in CMR86.
4. **Square-root divisor boundary.** Remove or sum the residual `sqrt(N)` terms
   in CMR61 and CMR64 for nearly singular carries.
5. **Balanced local laws for all odd primes.** Construct a comparable saturated
   no-three fibre law for `p=3 mod 4`, or prove an obstruction within the
   completed-reciprocal family.
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
- which CMR112/CC3 certificate rank dominates frozen child-pencil banks;
- whether opposite-layer node expansion unlocks concentrated pencil examples;
- fine mass recreated by one coarse prefix repair;
- inherited line-signature multiplicities inside `M_s`;
- nearly singular completed-reciprocal divisor collisions;
- balanced no-three fibre laws at primes `p=3 mod 4`;
- joint two-layer digital searches;
- mixed-projection determinant distributions for CRT products.

## Recommended order of work

1. Convert the CMR112 rank-`1/2/3` alternatives into forced opposite-layer or
   paid-defect expansion.
2. Build a lexicographic termination potential for the resulting alternating
   node closures.
3. Quantify fine-star recreation under the full prefix-rematching bank.
4. Sharpen the modular quotient syndrome and inherited line-signature
   multiplicity.
5. Remove the square-root divisor boundary in CMR61 and CMR64.
6. Classify balanced local reciprocal laws at primes `p=3 mod 4`.
7. Build a mixed-projection-aware CRT assembly theorem.
8. Continue exact finite searches at `N=14` and beyond.
9. Search jointly for digital two-layer constructions.
10. Integrate both prime-field and prime-power repairs with descending scales.
