# Status and honesty ledger

**Last updated:** 24 July 2026

## External status

The classical no-three-in-line conjecture \(D(n)=2n\) remains open. A July 2026
paper proves the analogous maximum \(kn\) for every fixed \(k\ge3\) and
sufficiently large \(n\), while identifying \(k=2\) as the exceptional
unresolved case.

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
32. **Uniform conversion inequality.** If total current defect incidence exceeds \(2m\Theta+2q\Lambda\), one rectangle strictly lowers the triple potential.
33. **Syndrome-weighted quotient extraction.** If \(|X/X|\le K|X|\), actual point triple degrees produce an admissible common-ratio matching carrying at least \(H/(6K)\) vertex-incidence weight.
34. **Paid-bank lower bound.** In a \(q\)-channel universe, the extracted bank has \(D\ge H/(6K)-(q-1)|X|\).
35. **Weighted conversion criterion.** Sufficiently large structured syndrome incidence forces an improving rectangle or one of the explicit alternating-closure structures.
36. **Projective conic-pencil geometry.** Every opposite-channel anchor has an exact modular tangent/secant profile governed by \(\chi(1-b/a)\).
37. **Aligned-anchor carry signatures.** Nondegenerate signatures have only \(p^{o(1)}\) real solutions, while degenerate signatures are exact affine-interpolation cells.
38. **Sharp same-channel carry dispersion.** A same-channel real secant star has divisor-bounded multiplicity at each exact cross-carry level.
39. **Universal star carry dispersion.** Any endpoint-disjoint secant star, including a cross-channel star, occupies at least its edge count divided by \(p^{o(1)}\) product-carry signatures.
40. **Combined paid-bank transition.** A failed paid bank produces an improvement, product/coordinate carry dispersion, or a perfect affine-alignment population.
41. **Perfect-alignment parameter classification.** Zero-leading-carry parameters form an explicit finite rational grid; the two endpoint parameters are inadmissible.
42. **Reduced-denominator chamber criterion.** Perfect alignment at parameter \(t'/q\) occurs exactly when both relevant wrap indices are divisible by \(q\).
43. **Denominator-sensitive sparsity.** A denominator-\(q\) perfect chamber contains at most \(4p/q\) base points; positive-density chambers therefore have bounded denominator.
44. **Explicit wrap centers.** Every degenerate scalar carry cell is radial about one rational center \(pS/d\), while every nondegenerate cell meets one hyperbola channel at most twice.
45. **Perfect-wrap factorization.** After recentering a degenerate chamber, its points satisfy a divisor-controlled integer product equation.
46. **Wrap-center dispersion.** A large perfect-alignment class either occupies many rational centers or has multipliers with a large common divisor relative to their size.
47. **Two-forbidden-matching spread.** Permutations avoiding a position set of row/column degree at most two have density at least \(1/72\) and \(72/(t)_r\) cylinder bounds for \(t\ge7\).
48. **Movable endpoint substar.** A star of \(M\) endpoint-disjoint pairs contains at least \(M/(2q)\) movable endpoints in one permutation layer and channel.
49. **Alternating star neutralization.** Permuting those endpoints within their rows and columns destroys the dominant original star while preserving saturation and layer disjointness.
50. **Joint-bank collateral bound.** The remaining expected collateral is controlled by normalized one-, two-, and three-anchor certificate counts.
51. **All-modulus affine saturation.** For every modulus, two affine permutation channels with distinct offsets use every row and column exactly twice, including nonunit strata.
52. **Affine real-lift classification.** The affine determinant is exactly \(-N\) times a carry determinant, and every affine modular channel has a real collinear triple for \(N\ge5\).
53. **Affine pair graph and codegree classification.** Unit offset gives one alternating Hamiltonian cycle, but one corresponding-column displacement repeats linearly many times.
54. **Composite hyperbola collapse families.** Odd squarefree, odd prime-power, and power-of-two unit hyperbolas have explicit large real-line collapses.
55. **Composite lift and CRT limitations.** Real collinearity always implies modular primitive-fibre collinearity, while coordinatewise CRT products contain mixed-projection triples.
56. **Completed reciprocal full channels.** At every prime power, valuation-stratum inversion gives a nonlinear valuation-preserving involution covering every row and column.
57. **Prime-power tangent-cell classification.** Odd-prime line intersections reduce to valuation quadratics with one possible Hensel-tangent cell and a height-sensitive exact-real cap.
58. **Universal companion layer.** Every prime-power permutation channel has a disjoint companion layer with one alternating Hamiltonian cycle.
59. **Prime-power displacement structure.** Completed-reciprocal secants have exact valuation, quadratic, block, and carry classifications; bounded raw multiplicity is impossible but the repetitions are localized.
60. **Recursive prime-power banks.** Every quotient state has exact fibre lifts, contraction recovers the smaller host, and the restricted conic bank excludes fibre-internal triples with explicit spread.
61. **All-prime terminal family.** Completed inverse permutations and their nonsquare-parameter spread family give companion-compatible no-three terminal states for every prime.
62. **Quadratic-order deterministic syndrome.** One completed-reciprocal layer has harmonic energy \(O(N^{3/2}+N\log^3N)\) and at most \(O(N^2\log N)\) real triples.
63. **Quadratic-order companion syndrome.** For fixed odd prime base, the full two-layer companion host has \(O_p(N^2\log N)\) same-/cross-layer triples.
64. **Recursive harmonic dispersion.** The recursive bank has expected one-layer harmonic energy \(O(N\log^3N)\), including with a no-three terminal base.
65. **Digital completion obstruction.** The recorded 64-point digit-linear layer has no second-permutation no-three completion, by an exact integer covering certificate.
66. **Corrected CRT taxonomy.** Saturated prime-factor pairs cannot be modular arcs; local-line slope carries and collision directions must both be tracked.
67. **Finite composite coverage.** Exact saturated configurations are recorded at \(N=4,6,8,9,10,12\); one-layer digital channels are recorded through \(N=64\).
68. **Recursive first-separation summation.** Balanced reciprocal banks at \(p\equiv1\pmod4\) have expected syndrome \(O_p(N^2\log N)\), and the logarithmic mass is confined to binary same-layer stars.
69. **Prefix-star neutralization.** Complete prefix rematching banks destroy every assigned binary star, remove the endpoint baseline, and have quadratic normalized rank-two/rank-three collateral.
70. **Stable quotient charging.** Fine-to-coarse repairs preserve every later quotient charge; rank-one collateral sums to \(O_p(N^2\log^2N)\) in expectation.
71. **Recursive-compatible node bank.** One reciprocal node can be changed while preserving saturation; invariant triples wholly inside child subtrees cancel exactly.
72. **Vertical child-pencil dichotomy.** The remaining external child load is either \(O(N^2)\) per depth after normalization or exposes an explicit alternating endpoint bank.
73. **Quantitative frozen-bank certificate.** Child-pencil mass controls the extracted star size, and a frozen bank forces normalized rank-\(1/2/3\) concentration at least \(t/216\).
74. **Balanced reciprocal-law classification.** Exact cell balance inside the completed-reciprocal family exists precisely for primes \(p\equiv1\pmod4\); reweighting cannot solve \(p\equiv3\pmod4\).
75. **Prime-seven balanced factorization.** Seven integer no-three permutations partition the \(7\times7\) grid and generate saturated recursive banks for every \(N=7^k\).
76. **Prime-seven spectral syndrome.** A sharpened factorization has pair-difference multiplicity at most three and expected syndrome below \((36/7)(k-1)N^2+(29/9)N^2\).
77. **Global-baseline alternating compression.** A fixed global comparison baseline transfers target destruction to every nonimproving child state and gives cube-root closure compression.
78. **Sharp small matching threshold.** Every degree-two forbidden endpoint board of size at least four has a perfect matching, while size three can fail.
79. **Geometric outcomes are executable.** Disjoint defects and heavy outside lines produce further alternating banks; no repeated-charge ledger is needed for either class.
80. **Target-load closure.** Separating endpoint-board size from certified target load removes the parent-excess barrier and contracts every positive load to a four-endpoint, one-target bank.
81. **Full-load two-layer conversion.** Ordered rematching of the two permutation layers destroys every triple in a vertex-disjoint family.
82. **Exact terminal-board profile.** Every normalized four-endpoint board has 2--9 states with sharp rank-one, rank-two, and rank-three atoms \(3/4,2/3,1/2\).
83. **Four-core cycle certificate.** Any positive global saturated minimum generates a finite cycle of four-point trades.
84. **Balanced local defect flow.** Around every four-core cycle, each grid triple is created and removed equally often, and all changes touch moved cells.

## What remains conditional

- Uniform scale-sensitive cleaning of switch shadows and anchored pair shadows.
- Product-state conflict regularization for candidate-only triples.
- Exclusion of balanced four-endpoint defect-flow cycles using first-separation, quotient, or carry signatures.
- A lexicographic potential paying for fine stars recreated by later coarse repairs.
- A superregular resampling oracle or exact conflict-free perfect-matching theorem.
- Removal or absorption of the square-root divisor-collision boundary.
- Non-reciprocal balanced grid factorizations beyond the prime seven.
- A joint digital two-layer construction replacing the obstructed CMR12 completion route.
- A CRT slope-carry incompatibility or absorption theorem.
- Coverage of arbitrary composite side lengths.

## Important refutations

- Dense constant-probability pruning cannot make all candidate-only triple constraints sparse enough.
- A large secant bank does not automatically certify destruction of current defects.
- Wall expansion does not necessarily terminate in an improving synchronized state.
- A single common absorber shift or common slope can be trapped by translated blocks.
- Bounded line occupancy and bounded pair codegree alone do not imply private-repair expansion.
- A carry-filtered cycle need not have an improving cyclic state or extracted order-two absorber.
- A spread perfect-matching measure does not by itself inherit the complete-permutation negative-dependency graph.
- Affine modular permutations cannot be a direct no-three channel for \(N\ge5\).
- Prime-field hyperbola line caps do not survive natural composite unit-hyperbola substitution.
- A unit-group channel is not a full permutation channel.
- The known 64-point digital layer cannot be completed by any second permutation.
- A saturated odd-prime CRT factor cannot satisfy the modular-arc premise of the simple direction-separation theorem.
- The weak recursive-compatible child load is not the ordinary finer-prefix collateral: a parent-node move changes its row residue class.
- No balanced weighting of completed-reciprocal maps exists when \(p\equiv3\pmod4\).
- A degree-two forbidden endpoint board need not have a perfect matching at size three.

## Bottom line

There is no complete proof. On the composite prime-power route, every globally
nonimproving alternating closure now contracts to one exact terminal object: a
four-endpoint board destroying one specified triple. Any positive global
minimum must therefore support a finite balanced cycle of such trades. The
principal missing theorem is a first-separation or carry-signature obstruction
to that cycle, followed by a scale budget for fine structures recreated by
coarse repairs and a coverage mechanism for arbitrary side lengths.
