# Status and honesty ledger

**Last updated:** 24 July 2026

## External status

The classical no-three-in-line conjecture \(D(n)=2n\) remains open. A July 2026 paper proves the analogous maximum \(kn\) for every fixed \(k\ge3\) and sufficiently large \(n\), while identifying \(k=2\) as the exceptional unresolved case.

## What is genuinely proved in this notebook

1. **Saturated decomposition.** A set with exactly two points in every row and column decomposes into two permutation layers.
2. **Clone-host regularity criterion.** Small active-coordinate secant shadow gives a near-complete superregular completion host.
3. **Candidate-only logarithmic obstruction.** A constant-density candidate host contains \(\Omega(n^4\log n)\) collinear candidate triples; first-moment pruning cannot close the problem.
4. **Reverse-scale certified multicover.** Descending dyadic heights avoids the protected-long-line problem and gives exact potential destruction under target deletion.
5. **Spread injection lemma.** A dense target-partner graph with \(t\ll p\) admits a \(K/p\)-spread random injection by greedy exposure.
6. **Uniform local-bank implication.** Explicit switch-shadow and anchor-load conditions imply negative expected drift.
7. **Protected tomographic trades.** Difference operators produce finite row/column/direction line-sum-preserving signed trades.
8. **Affine finite-direction construction.** For suitable arithmetic moduli, two affine permutations give a saturated configuration avoiding any fixed finite direction set.
9. **Subgroup coset absorbers.** Suitable affine configurations contain linearly many independently switchable blocks preserving protected toroidal line sums.
10. **Exact one-block collateral identity.** For absorber order \(h\le H\), a high line meets a block at most once and average collateral equals external secant shadow divided by \(h\).
11. **Block-shadow closure.** Whole-block reservoir growth makes every reservoir block externally shadow-clean without row/column deficits.
12. **Product-state LLL criterion.** A full-product block completion exists when normalized pair/triple conflict mass per block is small.
13. **Complementary hyperbola seed.** \(H_a\cup H_b\) has two points per row/column, at most four per line, no monochromatic triples, and bounded displacement multiplicity.
14. **Low-syndrome seed.** Some pair of hyperbola channels has \(O(n\log n)\) triple certificates.
15. **Hamiltonian-cycle criterion.** The union graph cycles are controlled by the multiplicative order of \(b/a\).
16. **Möbius secant matching.** For a fixed opposite-channel anchor, same-channel secant pairs form a projective involution matching.
17. **Cycle-bank theorem.** Every trapping cycle supports a \(k\)-state row-column-preserving cyclic matching trade.
18. **Window-product theorem.** Each cycle state lies in a number of modular hyperbolas equal to its distinct cyclic window-product count.
19. **Collision-free carry-cycle bank bound.** Every carry-filtered cycle has a collision-aware full-permutation state whose cost is bounded by normalized one-, two-, and three-cell certificate counts.
20. **Frozen-cycle concentration.** Failure of every cycle-block state forces a dense one-cell shadow, anchored-pair shadow, or candidate-only triple core.
21. **Clone-space exact selection theorem.** A uniformly random perfect matching on two row and column clones avoids unavailable cells, duplicate cells and all lifted collinear triples whenever the maximum local canonical-event probability load is at most \(1/24\).
22. **Concrete endpoint.** For \(n\ge100\), a candidate host with at most \(n/100\) unavailable cells and at most \(n^3/200\) residual collinear triples incident with each row or column contains a saturated no-three-in-line configuration.
23. **Selection failure concentration.** Failure in a near-complete candidate host forces some row or column to support \(\Omega(n^3)\) residual collinear triples.
24. **Fixed-rank superregular spread.** A uniformly random perfect matching of a dense superregular pair is \(O(1/N)\)-spread for every fixed rank, by six-cycle switchings.
25. **Clone inheritance.** The two-clone blow-up of a superregular pair remains superregular with explicit parameter loss.
26. **Two-layer spread.** Dense superregular pairs support a spread distribution on two edge-disjoint perfect matchings, giving exact row and column degree two.
27. **Global conflict-mass endpoint.** A dense superregular host contains a saturated conflict-free two-layer selection whenever the total spread-weighted conflict mass is below one.
28. **Inverse-additive repair banks.** Small quotient sets and many low-complexity windows produce linear common-ratio rectangle banks; near-minimal quotient sets complete to subgroup-coset absorbers.
29. **Coset and rational propagation.** Structured cycle parameters propagate to opposite-colour anchor structure, while full subgroup cosets of order at least three expand under the normalized Möbius map.
30. **Exact common-ratio collateral.** The cost of one same-ratio rectangle switch is exactly its two weighted secant loads plus the occupancy of its switched-pair line.
31. **Common-ratio decoder-or-structure theorem.** A paid common-ratio bank either contains an improving rectangle, a dense channel-pair secant star, or a large aligned multiplicative anchor class.
32. **Uniform conversion inequality.** If total current defect incidence exceeds \(2m\Theta+2q\Lambda\), where \(\Theta\) is switched-cell secant load and \(\Lambda\) aligned-anchor multiplicity, one rectangle strictly lowers the triple potential.
33. **Syndrome-weighted quotient extraction.** If \(|X/X|\le K|X|\), actual point triple degrees produce an admissible common-ratio matching carrying at least \(H/(6K)\) vertex-incidence weight.
34. **Paid-bank lower bound.** After correcting for pair-overlap, the extracted bank has \(D\ge H/(6K)-\beta|X|/2\); in a \(q\)-channel universe, \(D\ge H/(6K)-(q-1)|X|\).
35. **Weighted conversion criterion.** Sufficiently large structured syndrome incidence forces an improving rectangle or one of the explicit alternating-closure structures.
36. **Projective conic-pencil geometry.** The hyperbola channels form a two-base-point conic pencil; every opposite-channel anchor has \(1+\chi(1-b/a)\) tangents and exactly \((p-4-\chi(1-b/a))/2\) secants containing two affine points of the other channel.

## What remains conditional

- Uniform scale-sensitive cleaning of switch shadows and anchored pair shadows.
- Product-state conflict regularization for candidate-only triples.
- Carry-sensitive phase codes.
- Orbit Tanner expansion beyond bounded local conflict mass.
- Alternating two-colour carry-core termination and conversion.
- An alternating closure inequality controlling the secant-star load \(\Theta\) and aligned-anchor multiplicity \(\Lambda\).
- Classification of the Euclidean carry filter inside the projective conic involution orbits.
- A superregular resampling oracle or exact conflict-free perfect-matching theorem that upgrades spread to a local-load endpoint.
- Sparse algebraic \(O(1/d)\)-spread when the candidate degree is \(d=o(N)\).

## Important refutations

- Dense constant-probability pruning cannot make all candidate-only triple constraints sparse enough.
- A large secant bank does not automatically certify destruction of current defects.
- Wall expansion does not necessarily terminate in an improving synchronized state.
- A single common absorber shift or common slope can be trapped by translated blocks.
- Bounded line occupancy and bounded pair codegree alone do not imply private-repair expansion.
- A carry-filtered cycle need not have an improving cyclic state, an improving full one-colour permutation state, or an improving extracted order-two orbit absorber.
- A spread perfect-matching measure does not by itself inherit the complete-permutation negative-dependency graph.
- Arbitrary pair weights do not admit constant-fraction extraction into one quotient ratio; the positive theorem relies on vertex-induced syndrome weights and the sparse inadmissibility graph supplied by saturation.

## Bottom line

There is no complete proof. The weighted-bank bottleneck is closed for weights arising from current triple degrees, and low-quotient-complexity high-syndrome cores supply paid admissible common-ratio banks. The projective conic geometry now gives an exact modular secant baseline for every anchor. The remaining geometric bottleneck is to exploit the non-projectively-invariant Euclidean carry filter and prove that alternating red/blue closure cannot sustain the resulting secant-star or aligned-anchor concentrations indefinitely.
