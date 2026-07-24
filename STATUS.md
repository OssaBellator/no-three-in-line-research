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
51. **Exact prime-patching one-strip interface.** Every boundary-only one-strip patch is either a one-point corner splice or a two-edge strip switch; blocker secants through each inserted point form a matching and give an exact deletion-cover criterion.
52. **Pair-aware prime-patching endpoint.** A wider corner host satisfying explicit omitted-cell, old-anchor-pair, and internal-triple local-load bounds contains an exact saturated patch.
53. **Prime-gap transfer.** A proved patch width covering the backward gaps from solved prime-minus-one sizes transfers those solutions to all sufficiently large side lengths.
54. **Arbitrary-reservoir prime-patching endpoint.** The clone-space local-load theorem extends to any deleted saturated reservoir, including old-old replacements and mixed old/new cells, with explicit normalized cell/pair/triple bounds.
55. **Internally clean spread-bank endpoint.** A distribution on internally no-three deficit completions yields a valid patch whenever its selected blocked-cell and retained-anchor-pair expectation is below one.

## What remains conditional

- Uniform scale-sensitive cleaning of switch shadows and anchored pair shadows.
- Product-state conflict regularization for candidate-only triples.
- Carry-sensitive phase codes.
- Orbit Tanner expansion beyond bounded local conflict mass.
- Alternating two-colour carry-core termination and conversion.
- A second-order concentration theorem for the normalized certificate counts of the alternating neutralization bank.
- A monotone carry-complexity potential showing that repeated carry/wrap-center dispersion must terminate or enter an absorbable exception.
- Row-column-preserving absorbers for bounded-denominator perfect-interpolation chambers.
- A superregular resampling oracle or exact conflict-free perfect-matching theorem that upgrades spread to a local-load endpoint.
- Sparse algebraic \(O(1/d)\)-spread when the candidate degree is \(d=o(N)\).
- A prepared prime-minus-one reservoir that either meets the arbitrary-reservoir cell/pair/triple load endpoint or supports an internally no-three spread bank over a width large enough to match an unconditional prime-gap theorem.

## Important refutations

- Dense constant-probability pruning cannot make all candidate-only triple constraints sparse enough.
- A large secant bank does not automatically certify destruction of current defects.
- Wall expansion does not necessarily terminate in an improving synchronized state.
- A single common absorber shift or common slope can be trapped by translated blocks.
- Bounded line occupancy and bounded pair codegree alone do not imply private-repair expansion.
- A carry-filtered cycle need not have an improving cyclic state, an improving full one-colour permutation state, or an improving extracted order-two orbit absorber.
- A spread perfect-matching measure does not by itself inherit the complete-permutation negative-dependency graph.
- Arbitrary pair weights do not admit constant-fraction extraction into one quotient ratio; the positive theorem relies on vertex-induced syndrome weights and saturation.
- Repeating boundary-only one-strip prime patches cannot cover all sizes: exhaustive branching from the unique side-two seed reaches no side-five state.

## Bottom line

There is no complete proof. Carry and wrap-center classification make every first-generation obstruction explicit, and a dominant secant star can be neutralized by an exact two-colour permutation bank. The principal global bottleneck remains second-generation normalized collateral and termination. Independently, the all-`n` prime-patching track now has exact one-strip rigidity plus arbitrary-reservoir local-load and internally clean spread-bank endpoints. It still lacks the prepared prime-minus-one reservoir or bank satisfying either endpoint over a prime-gap-scale width.
