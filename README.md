# No-Three-in-Line Research Notebook

A rigorous research notebook for attempts toward the classical conjecture

\[
D(n)=2n,
\]

where \(D(n)\) is the maximum number of points that can be selected from an \(n\times n\) integer grid with no three collinear.

> **Status:** This repository does **not** contain a complete proof. The conjecture remains open as of 24 July 2026. The purpose of this repository is to preserve proved lemmas, conditional reductions, failed pathways, counterexamples, computational tools, and promising next targets in a form suitable for independent checking.

## Repository map

- [`STATUS.md`](STATUS.md): concise status and honesty ledger.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): theorem-by-theorem classification.
- [`docs/00-problem-and-literature.md`](docs/00-problem-and-literature.md): problem, current literature, and conventions.
- [`docs/01-saturation-and-reservoirs.md`](docs/01-saturation-and-reservoirs.md): two-per-row/column framework, clones, deficits, and secant shadows.
- [`docs/02-reverse-scale-switching.md`](docs/02-reverse-scale-switching.md): descending-scale potential and batch repair.
- [`docs/03-uniform-local-bank.md`](docs/03-uniform-local-bank.md): spread injection and explicit local-bank hypotheses.
- [`docs/04-protected-tomographic-trades.md`](docs/04-protected-tomographic-trades.md): exact line-sum-preserving trades.
- [`docs/05-subgroup-absorbers.md`](docs/05-subgroup-absorbers.md): affine terminal configurations and installed coset-cycle absorbers.
- [`docs/06-block-collateral-energy.md`](docs/06-block-collateral-energy.md): exact one-block collateral identities and block closure.
- [`docs/07-failed-wall-pathway.md`](docs/07-failed-wall-pathway.md): false wall-termination lemma and translated-block counterexample.
- [`docs/08-hyperbola-interleaver.md`](docs/08-hyperbola-interleaver.md): complementary modular hyperbolas, low-syndrome seeds, and Hamiltonian interleavers.
- [`docs/09-orbit-tanner-and-mobius-cycles.md`](docs/09-orbit-tanner-and-mobius-cycles.md): orbit codebooks, Möbius secant matchings, cycle trades, and window products.
- [`docs/10-cross-disciplinary-pathway.md`](docs/10-cross-disciplinary-pathway.md): radar, coding, tomography, and CSP interpretations.
- [`docs/11-open-bottlenecks.md`](docs/11-open-bottlenecks.md): exact remaining lemmas and proposed experiments.
- [`docs/12-failed-claims-ledger.md`](docs/12-failed-claims-ledger.md): claims that were corrected, weakened, or refuted.
- [`docs/13-carry-cycle-dispersion.md`](docs/13-carry-cycle-dispersion.md): frozen-cycle counterexample and corrected collision-aware bank theorem.
- [`docs/15-degree-constrained-hypergraph-selection.md`](docs/15-degree-constrained-hypergraph-selection.md): clone-space exact selection theorem and local triple-load endpoint.
- [`docs/16-superregular-clone-selection.md`](docs/16-superregular-clone-selection.md): six-cycle spread proof, dense superregular perfect-matching spread, and two-layer global conflict endpoint.
- [`docs/17-pfr-inverse-additive.md`](docs/17-pfr-inverse-additive.md): quotient-set inverse theorems, subgroup completion, and common-ratio repair banks.
- [`docs/18-pfr-coset-anchor-propagation.md`](docs/18-pfr-coset-anchor-propagation.md): coset absorber banks and alternating anchor propagation.
- [`docs/19-rational-coset-expansion.md`](docs/19-rational-coset-expansion.md): rational-function expansion of multiplicative cosets and the order-two exception.
- [`docs/20-common-ratio-bank-conversion.md`](docs/20-common-ratio-bank-conversion.md): exact rectangle collateral and decoder-or-structure conversion.
- [`docs/21-weighted-quotient-bank.md`](docs/21-weighted-quotient-bank.md): syndrome-weighted admissible quotient extraction and paid-bank lower bounds.
- [`docs/22-incidence-conic-pencil.md`](docs/22-incidence-conic-pencil.md): projective conic-pencil construction, exact opposite-channel secant profile, and ratio normal form.
- [`docs/23-aligned-anchor-carry-cells.md`](docs/23-aligned-anchor-carry-cells.md): aligned-anchor determinant factorization, signature divisor bounds, and perfect-interpolation cells.
- [`docs/24-secant-star-carry-dispersion.md`](docs/24-secant-star-carry-dispersion.md): universal product-carry dispersion for endpoint-disjoint stars in every channel pair.
- [`docs/25-perfect-alignment-arithmetic.md`](docs/25-perfect-alignment-arithmetic.md): exact interpolation-parameter arithmetic and bounded-denominator chamber sparsity.
- [`docs/26-same-channel-cross-carries-and-wrap-centers.md`](docs/26-same-channel-cross-carries-and-wrap-centers.md): exact same-channel cross carries, rational wrap centers, and chamber divisor bounds.
- [`docs/26-alternating-star-neutralization.md`](docs/26-alternating-star-neutralization.md): two-colour endpoint-permutation banks that neutralize the dominant secant star.
- [`docs/27-composite-modulus-obstructions.md`](docs/27-composite-modulus-obstructions.md): all-modulus affine saturation, universal affine triple obstruction, composite hyperbola collapses, and CRT lift limitations.
- [`scripts/verify_hyperbola.py`](scripts/verify_hyperbola.py): checks modular-hyperbola line bounds and displacement multiplicities for small primes.
- [`scripts/verify_conic_incidence.py`](scripts/verify_conic_incidence.py): checks projective secant involutions and exact tangent/secant counts for all ratios and anchors.
- [`scripts/verify_aligned_carry.py`](scripts/verify_aligned_carry.py): checks the aligned-anchor determinant, factorization, and interpolation identities.
- [`scripts/verify_carry_closure.py`](scripts/verify_carry_closure.py): checks same-channel cross carries, scalar wrap cells, rational centers, and chamber bounds.
- [`scripts/verify_perfect_alignment.py`](scripts/verify_perfect_alignment.py): checks the zero-leading-carry classification and reduced-denominator chamber bounds.
- [`scripts/verify_absorber.py`](scripts/verify_absorber.py): checks subgroup absorber states and protected line sums.
- [`scripts/search_cycle_trades.py`](scripts/search_cycle_trades.py): extracts cross-channel syndrome graphs and Möbius cycles.
- [`scripts/verify_carry_cycle_bound.py`](scripts/verify_carry_cycle_bound.py): verifies the frozen carry cycle and two-colour anchor release.
- [`scripts/verify_composite_modulus.py`](scripts/verify_composite_modulus.py): checks affine saturation/obstructions, composite hyperbola collapses, lift direction, and CRT mixed projections.

## Research discipline

Every mathematical item is tagged as one of:

- **PROVED:** a complete proof is written in this repository.
- **PROVED UNDER HYPOTHESES:** the implication is complete, but one or more hypotheses are not known to hold in the desired construction.
- **CONDITIONAL:** a reduction or theorem schema whose premise remains open.
- **HEURISTIC:** a proposed mechanism, not a theorem.
- **REFUTED:** a tempting statement accompanied by a counterexample.

The notebook deliberately keeps failed routes. In a long open problem, knowing exactly why a route fails is often as valuable as a new lemma.

## Principal current pathway

The strongest current synthesis is:

1. Start from two complementary modular hyperbola permutations \(H_a\cup H_b\), viewed as two members of a projective conic pencil.
2. Use their line cap, bounded displacement multiplicity, \(O(n\log n)\) triple syndrome, and exact opposite-channel secant profile.
3. Encode row-column-preserving changes through multiplicative orbit blocks or cycle trades.
4. Represent cross-channel bad triples as properly edge-coloured secant graphs whose colour classes are carry-filtered submatchings of projective involutions.
5. Peel leaves; every residual core contains a Möbius cycle.
6. Use collision-aware full permutation banks on cycle blocks.
7. Apply inverse-additive theorems: small quotient sets yield common-ratio rectangle banks and subgroup-coset absorbers.
8. Weight quotient extraction by actual triple degrees, producing a paid admissible common-ratio bank.
9. Convert the bank: either one rectangle improves, or failure yields a channel-pair secant star or an aligned multiplicative anchor class.
10. Apply carry classification. Every endpoint-disjoint star disperses through divisor-controlled product-carry signatures; aligned anchors disperse through nondegenerate coordinate-carry signatures or enter perfect affine-interpolation chambers.
11. Apply perfect-alignment arithmetic and wrap-center factorization. Positive-density perfect chambers have bounded rational denominator and divisor-controlled occupancy at each rational center.
12. Neutralize a dominant secant star by moving one endpoint from many star pairs through a constant-spread opposite-layer permutation bank.
13. Analyze only the second-generation normalized certificate counts created by this joint bank.
14. Prove a monotone alternating-closure potential, or construct finite-denominator absorbers for the remaining perfect chambers.
15. Finish in a near-complete candidate host using the clone-space degree-constrained local-load theorem.
16. In dense superregular candidate hosts, use spread perfect-matching measures; the missing upgrade is a local dependency/resampling theorem.

The original one-colour **carry-cycle dispersion lemma is refuted** by an exact \(p=11\) frozen cycle. The weighted quotient-bank bottleneck is closed. Both structural branches of a failed paid bank now reduce to explicit carry-signature growth or divisor-controlled perfect alignment. A dominant first-generation star can also be removed exactly by an alternating endpoint-permutation bank. The main geometric target is therefore a second-order concentration/termination theorem for the normalized collateral of that joint bank.

The independent composite-modulus track now proves that affine permutation channels saturate every modulus but cannot be no-three for \(N\ge5\); natural unit hyperbolas also have explicit squarefree and prime-power line collapses. Any direct all-\(n\) algebraic host must therefore be nonlinear, cover nonunits, and overcome mixed CRT projection triples.

## Running the checks

The scripts require Python 3.10+ and only the standard library.

```bash
python scripts/verify_hyperbola.py --prime 17
python scripts/verify_conic_incidence.py --prime 17
python scripts/verify_aligned_carry.py --prime 17
python scripts/verify_carry_closure.py --prime 17
python scripts/verify_perfect_alignment.py --prime 17
python scripts/verify_absorber.py --n 30 --h 5 --m 7
python scripts/search_cycle_trades.py --prime 17 --a 1 --b 3
python scripts/verify_carry_cycle_bound.py
python scripts/verify_composite_modulus.py --max-modulus 40
```

These programs are sanity checks, not proofs for arbitrary \(n\).

## Primary references

- Ghosal, Goenka, Grebennikov, Keevash, Kwan, Pham, *No-\((k+1)\)-in-line problem for \(k\ge3\)*, arXiv:2607.05255.
- Kovács, Nagy, Szabó, *Randomised algebraic constructions for the no-\((k+1)\)-in-line problem*, arXiv:2508.07632.
- Reiher, Schoen, *Note on the Theorem of Balog, Szemeredi, and Gowers*, arXiv:2308.10245.
- Gowers, Green, Manners, Tao, *Marton's Conjecture in abelian groups with bounded torsion*, arXiv:2404.02244.
- Raghavan, *Improved Bounds for the Freiman-Ruzsa Theorem*, arXiv:2512.11217.
- Nenadov, Pham, *Spread blow-up lemma with an application to perturbed random graphs*, arXiv:2410.06132.
- Pham, Sah, Sawhney, Simkin, *A Toolkit for Robust Thresholds*, arXiv:2210.03064.
- Glock, Joos, Kim, Kühn, Lichev, *Conflict-free hypergraph matchings*, arXiv:2205.05564.
- Joos, Mubayi, Smith, *Conflict-free Hypergraph Matchings and Coverings*, arXiv:2407.18144.
- Lu, Szekely, *A new asymptotic enumeration technique: the Lovasz Local Lemma*, arXiv:0905.3983.
- Ceko, Pagani, Tijdeman, *Algorithms for linear time reconstruction by discrete tomography II*, arXiv:2010.07862.

## Contribution guidance

A useful contribution should do at least one of the following:

- verify or repair a proof tagged **PROVED**;
- produce a small counterexample to a conditional lemma;
- prove a quantified shadow/codegree bound;
- prove the second-order concentration theorem for the alternating neutralization bank;
- construct a monotone carry-signature potential for alternating closure;
- construct absorbers for bounded-denominator perfect-interpolation chambers;
- build a superregular perfect-matching resampling oracle or conflict-free exact-cover theorem;
- extend dense \(O(1/N)\)-spread to sparse algebraic hosts with \(O(1/d)\)-spread;
- classify frozen cycles and alternating anchor closures;
- construct a nonlinear full permutation channel over a broad composite-modulus class with a genuine real line cap.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).
