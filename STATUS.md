# Status and honesty ledger

**Last updated:** 24 July 2026

## External status

The classical no-three-in-line conjecture `D(n)=2n` remains open. A July 2026
paper proves the analogous maximum `kn` for every fixed `k>=3` and sufficiently
large `n`, while identifying `k=2` as the exceptional unresolved case.

## What is genuinely proved in this notebook

1. **Saturated decomposition.** A set with exactly two points in every row and column decomposes into two permutation layers.
2. **Clone-host regularity criterion.** Small active-coordinate secant shadow gives a near-complete superregular completion host.
3. **Candidate-only logarithmic obstruction.** A constant-density candidate host contains `Omega(n^4 log n)` collinear candidate triples; first-moment pruning cannot close the problem.
4. **Reverse-scale certified multicover.** Descending dyadic heights gives exact potential destruction under target deletion.
5. **Spread injection lemma.** A dense target-partner graph admits a spread random injection.
6. **Uniform local-bank implication.** Explicit switch-shadow and anchor-load conditions imply negative expected drift.
7. **Protected tomographic trades.** Difference operators produce row/column/direction line-sum-preserving signed trades.
8. **Affine finite-direction construction.** Suitable affine permutations avoid any fixed finite direction set.
9. **Subgroup coset absorbers.** Suitable affine configurations contain many independently switchable protected blocks.
10. **Exact one-block collateral identity.** Average collateral equals external secant shadow divided by absorber order.
11. **Block-shadow closure.** Whole-block reservoir growth produces externally shadow-clean blocks.
12. **Product-state LLL criterion.** Small normalized pair/triple conflict mass gives a block completion.
13. **Complementary hyperbola seed.** Two modular hyperbolas give saturation, line cap four, no monochromatic triples, and bounded displacement multiplicity.
14. **Low-syndrome seed.** Some hyperbola pair has `O(n log n)` triple certificates.
15. **Hamiltonian-cycle criterion.** Hyperbola-layer cycles are controlled by multiplicative order.
16. **Möbius secant matching.** Same-channel secants through an opposite-channel anchor form an involution matching.
17. **Cycle-bank theorem.** Every trapping cycle supports a row-column-preserving cyclic trade bank.
18. **Window-product theorem.** Cycle-state conic coverage equals its distinct cyclic window-product count.
19. **Collision-free carry-cycle bank bound.** Full-permutation state cost is controlled by normalized certificate counts.
20. **Frozen-cycle concentration.** Failure forces a dense cell shadow, anchored-pair shadow, or triple core.
21. **Clone-space exact selection theorem.** Maximum canonical-event load at most `1/24` gives a saturated conflict-free selection.
22. **Concrete endpoint.** A 99%-dense host with bounded local triple incidence contains a saturated no-three set.
23. **Selection failure concentration.** Failure in a near-complete host forces a row or column with `Omega(n^3)` residual triples.
24. **Fixed-rank superregular spread.** Dense superregular perfect matchings are fixed-rank `O(1/N)`-spread.
25. **Clone inheritance.** Two-clone blow-up preserves superregularity.
26. **Two-layer spread.** Dense superregular pairs support two edge-disjoint spread perfect matchings.
27. **Global conflict-mass endpoint.** Small total spread-weighted conflict mass gives a saturated two-layer selection.
28. **Inverse-additive repair banks.** Small quotient sets produce common-ratio rectangle banks and coset absorbers.
29. **Coset and rational propagation.** Structured parameters propagate through opposite-colour anchors and Möbius maps.
30. **Exact common-ratio collateral.** One rectangle switch has an exact weighted secant cost.
31. **Common-ratio decoder-or-structure theorem.** A paid bank improves or produces explicit star/alignment structure.
32. **Uniform conversion inequality.** Sufficient syndrome incidence forces an improving rectangle.
33. **Syndrome-weighted quotient extraction.** Actual triple degrees yield an admissible weighted common-ratio matching.
34. **Paid-bank lower bound.** The extracted bank carries a quantified incidence weight.
35. **Weighted conversion criterion.** Large structured incidence forces improvement or alternating closure.
36. **Projective conic-pencil geometry.** Opposite-channel anchors have an exact modular secant profile.
37. **Aligned-anchor carry signatures.** Nondegenerate signatures are divisor-bounded; degenerate ones are interpolation cells.
38. **Sharp same-channel carry dispersion.** Cross-carry levels have divisor-bounded multiplicity.
39. **Universal star carry dispersion.** Endpoint-disjoint stars occupy many product-carry signatures.
40. **Combined paid-bank transition.** Failure gives improvement, carry dispersion, or perfect alignment.
41. **Perfect-alignment parameter classification.** Zero-leading-carry parameters form an explicit rational grid.
42. **Reduced-denominator chamber criterion.** Perfect alignment is equivalent to wrap-index divisibility.
43. **Denominator-sensitive sparsity.** Positive-density perfect chambers have bounded denominator.
44. **Explicit wrap centers.** Degenerate carry cells are radial about rational centers.
45. **Perfect-wrap factorization.** Recentered chambers satisfy divisor-controlled product equations.
46. **Wrap-center dispersion.** Large aligned classes disperse across centers or have a large common divisor.
47. **Two-forbidden-matching spread.** Permutations avoiding degree-two forbidden positions have constant density and cylinder bounds.
48. **Movable endpoint substar.** A large star contains many movable endpoints of one layer/channel type.
49. **Alternating star neutralization.** Opposite-layer endpoint permutations destroy the original star exactly.
50. **Joint-bank collateral bound.** Remaining expected collateral is controlled by normalized certificate counts.
51. **Exact prime-patching one-strip interface.** Every boundary-only one-strip patch has one of two forced forms and an exact blocker-cover criterion.
52. **Pair-aware prime-patching endpoint.** Explicit corner cell/pair/triple loads suffice for an exact patch.
53. **Prime-gap transfer.** A patch width covering backward gaps from solved prime-minus-one sizes transfers to all large sizes.
54. **Arbitrary-reservoir endpoint.** Clone-space selection handles deleted reservoirs, old-old replacements, and mixed cells.
55. **Internally clean spread-bank endpoint.** Small retained-core cell/pair expectation gives a valid patch.
56. **Deletion-aware one-strip averaging.** Automatic axis blockers are cleared by the forced deletion; surviving certificates have an exact average.
57. **Row-lift reservoir bank.** Deleting `t` old rows gives a `4t`-cell exact completion bank with rank-three spread.
58. **Sequential row-lift local lemma.** Four permutation layers can be exposed sequentially under activated load `1/24`.
59. **Static and conditioned pruning endpoints.** Terminal vertex loads and collision-conditioned event masses give prefix-free sufficient tests.
60. **Full-support row-lift barrier.** One unpruned refill rectangle has `Omega(t^4 log t)` compatible triples, so global first moment cannot scale.
61. **Off-diagonal block obstruction.** Any `4t` points in two aligned off-diagonal `t x t` blocks force a slope-minus-one triple.
62. **Projection classification.** Primitive-direction support dispersion is necessary, and the aligned slope-minus-one block is the unique minimal `2t-1` failure.
63. **Quantitative projection forcing.** Convex line occupancy gives exact lower bounds on triples forced by under-dispersed projections, additive across directions.
64. **Component-clean endpoint.** Independent internally clean movement/refill banks have an exact factored certificate expectation and spread criterion.
65. **Quadratic cross-triple cap.** Two internally no-three components of size `2t` create at most `4t(2t-1)` cross triples.

## What remains conditional

- Uniform scale-sensitive cleaning of switch shadows and anchored pair shadows.
- Product-state conflict regularization for candidate-only triples.
- Carry-sensitive phase codes and orbit Tanner expansion beyond bounded local conflict mass.
- Alternating two-colour carry-core termination and conversion.
- A second-order concentration theorem for the alternating neutralization bank.
- A monotone carry-complexity potential or bounded-denominator chamber absorber.
- A superregular resampling oracle and sparse algebraic `O(1/d)` spread.
- A prime-minus-one reservoir with one of the following at prime-gap-scale width:
  - a sparse row-lift subbank passing PP3p or PP3r;
  - a prefix-structured bank passing PP3l or PP3q;
  - large internally clean component banks passing PP3z or PP3aa;
  - an arbitrary-reservoir host passing the PP2 local-load endpoint.

## Important refutations

- Dense constant-probability pruning cannot remove candidate-only triple accumulation.
- A large secant bank does not automatically certify current-defect destruction.
- Wall expansion and one common shift or slope need not terminate in improvement.
- Bounded occupancy and pair codegree do not imply private-repair expansion.
- One-colour carry-cycle repair can freeze.
- Spread perfect-matching measures do not automatically inherit complete-permutation negative dependency.
- Arbitrary pair weights do not admit constant-fraction extraction into one quotient ratio.
- Repeating boundary-only one-strip patches cannot reach every size.
- The original PP3b boundary-shadow test is vacuous for every saturated seed.
- The unrestricted full row-lift bank is not automatically clean.
- Aligned off-diagonal block doubling is impossible for every width.
- Conditioning the complete small banks to internally clean components does not produce a clean pair at fully deleted widths `3,4,5`.

## Bottom line

There is no complete proof. The principal global bottleneck remains
second-generation alternating-bank collateral and termination. Independently,
the all-`n` prime-patching track now has exact extension interfaces, several
selection endpoints, a concrete row-lift bank, static and sequential pruning
criteria, projection obstructions, and component-clean factorization. The
remaining missing theorem is asymptotic geometric preparation: build a sparse,
spread, internally controlled reservoir over a width large enough for
unconditional prime-gap transfer.