# Status and honesty ledger

**Last updated:** 27 July 2026

## External status

The classical no-three-in-line problem remains unresolved: no side length is
known for which the maximum is strictly below `2n`. Exact `2n` configurations
are known for every `2 <= n <= 66`, and also for `n=68` and `n=70`.

The analogous no-`(k+1)`-in-line problem is now resolved for every fixed
`k>=3` and sufficiently large `n`: the maximum is exactly `kn`. This does not
settle the exceptional `k=2` case studied in this repository.

## What this branch genuinely proves

Detailed theorem statements and locations are maintained in `proofs/` and the
track ledgers. The principal proved endpoints are:

1. **Saturated decomposition and exact product encodings.** Every saturated
   state decomposes into two permutation layers. Fixed-phase and full-selector
   product existence reduce to exact finite CSP/SAT systems, and alternating
   cycles connect all degree-two states in one product host.
2. **Exact small factor-independent products.** The branch proves
   `2x3 -> 6`, `2x4 -> 8`, `2x5 -> 10`, and `2x6 -> 12` for every saturated
   no-three factor of the indicated inner side.
3. **Low-syndrome doubling seed.** Every saturated side-`n` factor has a
   factor-compatible side-`2n` saturated state with `O(n log n)` bad triples.
   Exact closure still requires repair or absorption.
4. **Paired asymptotic repair reduction.** The audited rectangle-label repair
   path closes all active local interfaces and is effective for every
   `N >= 10^2874`.
5. **Optimality within the current divisor family.** The universal
   Euler-product exponent family cannot lower the integral decimal cutoff below
   `10^2874` under the current retained-order inequalities.
6. **Finite side-seven selector census.** In the `(5,2)` radius-three,
   support-twenty layer:
   - all selectors of multiplicity at least three are classified;
   - `37,600` are infeasible and one multiplicity-four selector is constructive;
   - multiplicity-two cases `0` through `319` add `640` exact rejections;
   - the committed cache therefore contains `38,240` infeasible selectors,
     one constructive selector, and `33,619` unclassified selectors;
   - the certified rejection search uses `2,899,564,230` bottom-CSP nodes.
7. **Low-multiplicity certificate reduction.** For one fixed top order, bottom
   infeasibility is equivalent to covering all `5,040` bottom permutations by
   collinear abstract triples. Generic dictionary and greedy-subcover generators
   are committed.
8. **Produced-base recursion barriers.** Affine-column all-transposition
   templates are impossible at bases 8, 10, and 12, even with arbitrary row
   labeling and arbitrary spanning degree-two selection.
9. **First complete non-affine double-coset obstruction.** At side ten, the
   opposite-pair transposition double coset is infeasible in orientations `cc`
   and `cf`, covering `16,000` exact geometries and `266,447,755` search nodes.
10. **Global matching and spread endpoints.** Dense superregular hosts support
    spread two-layer selections and conflict-free selection under explicit
    total or local conflict-load hypotheses.
11. **Hyperbola and carry structure.** The branch proves complementary
    hyperbola seeds, common-ratio extraction, carry dispersion, perfect-alignment
    classification, wrap-center factorization, and first-generation alternating
    neutralization.
12. **Terminal repair integration.** Hall-core failure, maximal deficiency,
    terminal cycle escape, causal descent, trajectory reset, and paired-label
    terminal return are integrated into one audited repair tree.

## Current exact finite boundary

The side-seven support-twenty cache contains `71,860` selectors. The committed
classification is:

- `38,240` certified infeasible;
- `1` constructive;
- `33,619` unclassified.

The unresolved set is exactly:

- `3,520` multiplicity-two signatures containing `7,040` selectors;
- `26,579` multiplicity-one signatures/selectors.

The next canonical multiplicity-two case is `320`. A durable batch for cases
`320` through `399` is running and is not counted until all transcripts are
promoted to replay verifiers.

## What remains conditional or open

- A structural finite-range bridge covering every order below `10^2874`.
- Infinite exact product closure or arithmetic coverage of every side length.
- A recursive product theorem at a produced base such as side ten or twelve.
- Completion of the side-ten opposite-pair `fc` and `ff` double-coset searches,
  followed by the two larger transposition double cosets.
- A global repair/resampling theorem coordinating many product fibres.
- An exact conflict-free perfect-matching/cover theorem with the required local
  load endpoint in sparse or structured hosts.
- Second-generation collateral concentration for the hyperbola pathway.
- A monotone alternating carry-complexity potential or a bounded-denominator
  chamber absorber.
- Completion of the side-seven multiplicity-two and multiplicity-one census.
- Compact independently replayed proof objects replacing large raw DFS
  transcripts at low multiplicity.

## Important refutations and barriers

- Bounded line occupancy and bounded pair codegree alone do not imply private
  repair expansion.
- Triple-count descent, and its natural pair-energy refinement, are not monotone
  on alternating-cycle state spaces.
- Global coarse/fine orientation and phase choices are not universal product
  constructions.
- Identity/reversal and affine block maps are not factor-independent beyond the
  proved small templates.
- The arbitrary-map one-inner-layer family has no template at bases 3, 6, 7,
  or 8.
- Affine-column recursion fails in the all-transposition class at bases 8, 10,
  and 12.
- Representative left-coset searches are not complete double-coset
  obstructions; only mechanically exhausted double-coset families are promoted.
- The current universal divisor-exponent family is exhausted at decimal cutoff
  `10^2874`; further progress needs a different inequality or structural bridge.

## Bottom line

There is no complete proof of the classical no-three-in-line conjecture and no
all-side product theorem. The branch contains exact finite classifications,
small factor-independent product closures, a proved asymptotic repair reduction
above `10^2874`, and several independently replayable obstruction theorems. The
active fronts are finite-range coverage, low-multiplicity certificate
compression, genuinely non-affine recursive templates, global resampling, and
hyperbola/carry termination or absorption.
