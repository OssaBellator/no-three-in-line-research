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

Starting from a frozen one-colour carry cycle, add its opposite-colour secant
anchors and permit matching changes in both colour blocks. Iterate this
alternating closure. Prove that it either yields a decreasing joint state or
forces a global concentration contradiction with the bounded-displacement
geometry of the two hyperbola channels.

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

CMR113--CMR115 completely classify exact balanced laws inside the
completed-reciprocal local family. Cell balance forces a uniform shift for each
coefficient, and the two endpoint shifts require opposite quadratic characters.
Consequently such a balanced no-three law exists exactly for
\(p\equiv1\pmod4\). At primes \(p\equiv3\pmod4\), changing the weights on the
same reciprocal maps cannot work.

CMR116--CMR119 give a non-reciprocal escape at the prime seven: seven integer
no-three permutations partition the entire \(7\times7\) grid, producing a
saturated balanced recursive bank at every \(N=7^k\). CMR120--CMR122 sharpen
its pair spectrum and prove

\[
\mathbb E T_k
<
\frac{36}{7}(k-1)N^2+\frac{29}{9}N^2.
\]

CMR123--CMR127 compress the alternating closure while retaining one fixed global
comparison baseline. A low-excess globally nonimproving bank either exposes
disjoint defects, exposes an outside line core, or contains a cubic-root smaller
alternating bank. CMR128 proves that the smaller bank only needs size four:
every degree-two forbidden board of size at least four has a perfect matching,
and size three can fail.

Thus an uncharged alternating expansion chain reaches an absolute bank size
below `2160` after `O(log log t)` levels. Heavy outside lines are paid by the
outside triple potential through

\[
|\{L:|L\cap X|>2s\}|
\le
\frac{\Phi(X)}{\binom{2s+1}{3}}.
\]

Local-bank construction, quotient charging, endpoint removal, higher-rank
prefix collateral, child-core cancellation, vertical-pencil concentration, and
unbounded alternating expansion are therefore closed. The remaining recursive
problem is repeated-charge accounting across many starting nodes and scales,
plus the absolute endpoint-bank core below `2160`.

### Composite-modulus open lemmas

1. **Repeated-charge accounting.** Sum the CMR125 excess, disjoint-defect, and
   heavy-line alternatives over all starting prime-power nodes without charging
   the same triple or line signature repeatedly.
2. **Bounded alternating core.** Resolve, enumerate, or structurally absorb the
   endpoint-bank residual class below `2160`.
3. **Termination after coarse repairs.** CMR93 protects unprocessed coarser
   quotients, but a later coarse repair may recreate fine stars. Prove that the
   reintroduced fine mass is paid by the coarse potential decrease or by a
   lexicographic scale budget.
4. **Non-reciprocal balanced prime families.** Extend the prime-seven grid
   factorization to `p=11,19,...`, or prove structural obstructions to a
   factorization into `p` integer no-three permutations.
5. **Sharper modular quotient syndrome.** Improve the current
   `O_p(sm^2)` bound for `Z_s`, or exploit inherited primitive line signatures to
   beat the raw factor `3t^2` in CMR86.
6. **Square-root divisor boundary.** Remove or sum the residual `sqrt(N)` terms
   in CMR61 and CMR64 for nearly singular carries.
7. **Joint digital construction.** Search jointly for both layers or replace the
   obstructed `64`-point first layer before attempting a lift to `128`.
8. **CRT slope-carry incompatibility.** Control simultaneous vanishing of
   `L_u,L_v`, including noncyclic zero-divisor incidences.
9. **Further finite coverage.** Exact saturated constructions are known at
   composite sizes `4,6,8,9,10,12`; `N=14` remains unresolved.

## Bottleneck 5: computational falsification

The following should be exhaustively tested for small primes:

- classify frozen one-colour cycles and their alternating anchor closures;
- distribution of \(q_s\) for real carry-filtered cycles;
- existence of alternating two-colour closures that remain jointly frozen;
- overlap multiplicities of CMR125 disjoint-defect and heavy-line payments;
- exact bounded-core behaviour for endpoint banks below `2160`;
- fine mass recreated by one coarse prefix repair;
- exact no-three grid factorizations and pair spectra at `p=11,19,...`;
- inherited line-signature multiplicities inside `M_s`;
- nearly singular completed-reciprocal divisor collisions;
- joint two-layer digital searches;
- mixed-projection determinant distributions for CRT products.

## Recommended order of work

1. Build a no-double-charge ledger for the CMR125 defect and line alternatives.
2. Reduce or enumerate the absolute endpoint-bank core below `2160`.
3. Quantify fine-star recreation under the full prefix-rematching bank.
4. Search for non-reciprocal balanced grid factorizations at the next
   `p=3 mod 4` primes.
5. Sharpen the modular quotient syndrome and inherited line-signature
   multiplicity.
6. Remove the square-root divisor boundary in CMR61 and CMR64.
7. Build a mixed-projection-aware CRT assembly theorem.
8. Continue exact finite searches at `N=14` and beyond.
9. Search jointly for digital two-layer constructions.
10. Integrate both prime-field and prime-power repairs with descending scales.
