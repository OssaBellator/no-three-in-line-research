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
47. **Two-forbidden-matching spread.** Permutations avoiding a position set of row/column degree at most two have constant density and \(128/(t)_r\) cylinder bounds.
48. **Movable endpoint substar.** A star of \(M\) endpoint-disjoint pairs contains at least \(M/(2q)\) movable endpoints in one permutation layer and channel.
49. **Alternating star neutralization.** Permuting those endpoints within their rows and columns destroys the dominant original star while preserving saturation and layer disjointness.
50. **Joint-bank collateral bound.** The remaining expected collateral is controlled by normalized one-, two-, and three-anchor certificate counts.
51. **Four-orientation mixed-radix saturation.** Independent alternating-cycle phases give two disjoint permutation layers for every global coarse/fine digit orientation.
52. **General product determinant classification.** Every mixed-radix product triple satisfies one four-term coarse/hybrid/fine determinant identity, yielding exactly four cross-block multiplicity types.
53. **Weighted direction resonance.** Type-\((2,2)\) product triples are exactly weighted parallelisms between one coarse secant and one fine secant.
54. **Factor-product host codegrees.** Every product-host line has at most \(4\min(m,n)\) points, and every pair has at most \(4\min(m,n)-2\) possible third points.
55. **Exact phase SAT reduction.** For fixed factors and orientation, no-three phase selection is equivalent to an explicit width-three CNF with \(2mc\) variables.
56. **Full product-host saturation.** Every spanning degree-two subgraph of the four-regular factor-product host is saturated and decomposes into two permutation layers.
57. **Exact full-selector SAT reduction.** No-three degree-two product-host selection is equivalent to an explicit width-three CNF with one variable per host cell.
58. **Alternating-cycle repair connectivity.** Any two degree-two states in one product host are connected by executable alternating-cycle trades that preserve saturation and factor compatibility.
59. **Fixed-area carry concentration.** In a no-three set of \(s\) points, every fixed nonzero signed determinant has at most \(2s(s-1)\) ordered realizations; this gives \(4n(2n-1)\) ordered fine triples at one nonzero ordinary product-carry level.
60. **Complete projection-fibre concentration.** After fixing one complete ordered factor projection, the full mixed-radix collinearity equation has at most quadratic multiplicity in the other factor, simultaneously controlling both hybrid terms and the fine determinant.
61. **Sharp type-\((2,2)\) multiplicity.** Weighted parallel factor secants have only linear multiplicity in the opposite factor; unordered resonant signatures are at most \(mn(2\min(m,n)-1)\).
62. **Exact alternating-cycle collateral.** The triple-potential change of one cycle toggle splits exactly into one-moving, two-moving, and internal-cycle certificate terms.
63. **Finite repair-barrier census.** In the canonical crossed \(2\times3\) host, ten one-defect states require a temporary increase to two defects before reaching either no-three state.
64. **Composite batch compression.** Any finite sequence of alternating-cycle trades compresses to one balanced endpoint trade, and every exact side-six or side-nine trap found has an improving composite support of at most eight cells per sign.
65. **Quantitative unmodified \(2\times5\) obstruction.** Every degree-two state in every global unmodified \(2\times5\) host has at least two bad triples; ordinary `cc` hosts have at least seven.
66. **Blockwise digit-map saturation.** Arbitrary fine-digit permutations inside individual coarse row and column blocks preserve the simple four-regular host and all degree-two saturation conclusions.
67. **Exact side-ten blockwise product.** One blockwise reversal applied to a \(2\times5\) product yields twenty no-three points in the \(10\times10\) grid.
68. **Canonical unsatisfiable line core.** One unmodified crossed \(2\times5\) host has a deletion-minimal 35-line core relative to the exact degree-two clauses.
69. **One-inner-layer twisted products.** Fixing one inner permutation while retaining both outer layers gives an explicit \(O(mn)\) saturated blockwise product family.
70. **Complete reversal census.** Among all sixteen identity/reversal assignments at \(2\times5\), exactly the four varying in both row and column blocks succeed; each rescues 9 of 32 inner factors across 13 factor/orientation hosts.
71. **Complete normalized non-affine census.** Allowing arbitrary second-block permutations gives seven no-three parameter states, five scalar configurations, and an explicit non-affine escape for the canonical side-five factor.
72. **Affine double-coset classification at five.** \(S_5\) is the disjoint union of \(\operatorname{AGL}(1,5)\) and one 100-element non-affine double coset; every admissible side-five factor layer lies in the latter.
73. **Universal special product closure at five.** Every saturated no-three side-five factor, and either of its two permutation layers, composes with the saturated side-two factor to the same exact saturated no-three side-ten configuration after suitable blockwise affine maps.
74. **Affine normalization theorem.** The complete four-block affine one-inner-layer family reduces to identity first blocks and relative affine second-block maps.
75. **Affine one-layer obstruction at six and seven.** Exhaustive searches of 414,720 and 35,562,240 normalized states find no no-three affine one-inner-layer product at either base side.
76. **Double-coset template closure.** Any successful normalized one-layer template transports to its entire map-group double coset; double-coset coverage of admissible factor layers is a sufficient factor-independent closure criterion.
77. **Full permutation gauge normalization.** Arbitrary four-block one-inner-layer states normalize exactly to identity first block maps, without an affine hypothesis.
78. **Complete small arbitrary-map census.** The normalized one-layer family has exact success/configuration counts \((16,9),(0,0),(4,4),(8,5)\) at base sides two through five.
79. **Full-symmetric template universality.** With arbitrary block permutations, one successful normalized template transports every fine permutation and therefore every saturated factor layer.
80. **Universal special product closure at four.** Every saturated no-three side-four factor composes with side two to the exact saturated no-three side-eight template.
81. **Rectangle perfect-matching normal form.** Every arbitrary-map one-inner-layer state is a perfect matching of four-corner rectangles; every bad triple is diagonal or transversal.
82. **Rectangle conflict bounds.** One rectangle has at most \(16n(n-1)^2\) diagonal-conflict partners and one compatible pair has at most \(64n(n-2)^2\) transversal completions.
83. **Complete unrestricted one-layer boundary through eight.** Templates exist at bases 2, 4, and 5 and are impossible at bases 3, 6, 7, and 8, even with arbitrary block maps.
84. **Full four-layer normal form.** Arbitrary block-map hosts have block permutations \(Q^jTH^sP^i\) and depend on the inner factor only through the cycle type of its relative permutation.
85. **Universal special product closure at three.** Every saturated side-three factor composes with side two to the exact saturated no-three side-six full-selector template.
86. **One-outer-layer reduction and obstruction.** One-outer-layer states are two independently relabelled factors of one relative cycle type, and all 60,544 such side-six states fail.
87. **Full-selector transfer matrix.** A relative \(L\)-cycle has exactly \(2+2\cdot4^L+(4+2\sqrt3)^L+(4-2\sqrt3)^L\) abstract degree-two selector states, with counts multiplying over cycles.
88. **Exact side-six selector populations.** Relative types `(6)`, `(4,2)`, and `(3,3)` have 181,122, 325,620, and 298,116 abstract selector states respectively.
89. **Unique affine mixed side-six template.** Among 20,736 affine full-selector hosts, exactly one is feasible: the 6-cycle type in `ff`, producing an exact side-twelve certificate.
90. **Six-cycle side-six closure class.** All 84 ordered saturated side-six factors whose relative permutation is a 6-cycle transport to the same side-twelve no-three configuration.
91. **Four-plus-two side-six closure class.** All 16 ordered saturated side-six factors whose relative permutation has cycle type `(4,2)` transport to one exact `cc` side-twelve certificate.
92. **Three-plus-three side-six closure class.** All 16 ordered saturated side-six factors whose relative permutation has cycle type `(3,3)` transport to one exact crossed side-twelve certificate.
93. **Universal special product closure at six.** Every saturated no-three side-six factor composes with side two to an exact saturated no-three side-twelve configuration.

## What remains conditional

- Uniform scale-sensitive cleaning of switch shadows and anchored pair shadows.
- Product-state conflict regularization for candidate-only triples.
- An infinite family of successful full-selector cycle types or another controlled product family yielding multiplicative closure.
- A full-selector classification at base side seven and larger.
- A recursive product theorem at a produced base such as side ten or twelve.
- A global product repair or resampling theorem that coordinates many projection fibres and distinguishes feasible hosts from structured infeasible cores.
- Arithmetic coverage derived from an infinite closure or extension theorem.
- Orbit Tanner expansion beyond bounded local conflict mass.
- Alternating two-colour carry-core termination and conversion.
- A second-order concentration theorem for the normalized certificate counts of the alternating neutralization bank.
- A monotone carry-complexity potential showing that repeated carry/wrap-center dispersion must terminate or enter an absorbable exception.
- Row-column-preserving absorbers for bounded-denominator perfect-interpolation chambers.
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
- Arbitrary pair weights do not admit constant-fraction extraction into one quotient ratio; the positive theorem relies on vertex-induced syndrome weights and saturation.
- Global coarse/fine radix orientation plus independent alternating-cycle phases does not universally produce a no-three product; one \(2\times3\) factor pair defeats all 64 orientation/phase states.
- Even arbitrary degree-two selection in the four unmodified global product hosts is not universal: exhaustive search finds no model for any ordered \(2\times5\) or \(5\times2\) factor-pair instance.
- Triple-count descent on alternating cycles is not monotone: a crossed side-six host has ten one-defect traps although it contains no-three states.
- Lexicographically refining triple count by the natural pair-line energy still leaves four exact bad local minima in that host.
- The parity-reflection lift is not a universal doubling theorem: exhaustive search finds no reflected no-three permutation for base sides 3, 4, 6, 7, or 8.
- Identity/reversal block maps alone are not factor-independent: the complete census succeeds for only 9 of 32 layer-unordered side-five factors.
- Normalized affine second-block maps do not rescue the canonical side-five full-selector host.
- The complete affine one-inner-layer family has no no-three state at base sides six or seven, even when the inner permutation is arbitrary.
- The complete arbitrary-map one-inner-layer family has no template at bases 3, 6, 7, or 8.
- No one-outer-layer side-six template exists for any of the relative types `(6)`, `(4,2)`, or `(3,3)`.
- The all-affine full-selector family has no side-six template for relative types `(4,2)` or `(3,3)`; their successful universal templates require more general block maps.

## Bottom line

There is no complete proof. The product branch now contains factor-independent closure theorems \(2\times3\to6\), \(2\times4\to8\), \(2\times5\to10\), and \(2\times6\to12\). The arbitrary-map one-inner-layer family is completely classified through base eight and cannot iterate the side-four closure to sixteen. The full selector is reduced to relative cycle type and an exact transfer system, and all side-six relative classes are now solved. No infinite multiplicative closure or arithmetic coverage theorem follows: the next product targets are larger-base cycle-type templates, a recursive closure at side ten or twelve, or a general repair/resampling theorem. The main hyperbola pathway still requires second-generation collateral concentration, followed by monotone termination or bounded-denominator absorption.
