# No-Three-in-Line Research Notebook

A rigorous research notebook for attempts toward the classical conjecture

\[
D(n)=2n,
\]

where `D(n)` is the maximum number of points that can be selected from an
`n x n` integer grid with no three collinear.

> **Status:** This repository does **not** contain a complete proof. The
> conjecture remains open as of 24 July 2026. The purpose of the repository is
> to preserve proved lemmas, conditional reductions, failed pathways,
> counterexamples, computational tools, and promising next targets in a form
> suitable for independent checking.

## Repository map

- [`STATUS.md`](STATUS.md): concise status and honesty ledger.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): theorem-by-theorem classification.
- [`proofs/prime-patching-recent-index.md`](proofs/prime-patching-recent-index.md): focused index for the recent matching-reservoir and patch-bank results.
- [`docs/00-problem-and-literature.md`](docs/00-problem-and-literature.md): problem, current literature, and conventions.
- [`docs/01-saturation-and-reservoirs.md`](docs/01-saturation-and-reservoirs.md): two-per-row/column framework, clones, deficits, and secant shadows.
- [`docs/02-reverse-scale-switching.md`](docs/02-reverse-scale-switching.md): descending-scale potential and candidate-only triple barrier.
- [`docs/03-uniform-local-bank.md`](docs/03-uniform-local-bank.md): spread injection and explicit local-bank hypotheses.
- [`docs/04-protected-tomographic-trades.md`](docs/04-protected-tomographic-trades.md): exact line-sum-preserving trades.
- [`docs/05-subgroup-absorbers.md`](docs/05-subgroup-absorbers.md): affine terminal configurations and installed coset-cycle absorbers.
- [`docs/06-block-collateral-energy.md`](docs/06-block-collateral-energy.md): exact one-block collateral identities and block closure.
- [`docs/07-failed-wall-pathway.md`](docs/07-failed-wall-pathway.md): false wall-termination lemma and translated-block counterexample.
- [`docs/08-hyperbola-interleaver.md`](docs/08-hyperbola-interleaver.md): complementary modular hyperbolas, low-syndrome seeds, and Hamiltonian interleavers.
- [`docs/09-orbit-tanner-and-mobius-cycles.md`](docs/09-orbit-tanner-and-mobius-cycles.md): orbit codebooks, Möbius secant matchings, cycle trades, and window products.
- [`docs/10-cross-disciplinary-pathway.md`](docs/10-cross-disciplinary-pathway.md): radar, coding, tomography, and CSP interpretations.
- [`docs/11-open-bottlenecks.md`](docs/11-open-bottlenecks.md): exact remaining lemmas and proposed experiments.
- [`docs/12-failed-claims-ledger.md`](docs/12-failed-claims-ledger.md): corrected, weakened, or refuted claims.
- [`docs/13-carry-cycle-dispersion.md`](docs/13-carry-cycle-dispersion.md): frozen-cycle counterexample and corrected collision-aware bank theorem.
- [`docs/15-degree-constrained-hypergraph-selection.md`](docs/15-degree-constrained-hypergraph-selection.md): clone-space exact selection and local triple-load endpoint.
- [`docs/16-superregular-clone-selection.md`](docs/16-superregular-clone-selection.md): dense superregular perfect-matching spread and two-layer endpoint.
- [`docs/17-pfr-inverse-additive.md`](docs/17-pfr-inverse-additive.md): quotient-set inverse theorems and common-ratio repair banks.
- [`docs/18-pfr-coset-anchor-propagation.md`](docs/18-pfr-coset-anchor-propagation.md): coset absorber banks and alternating anchor propagation.
- [`docs/19-rational-coset-expansion.md`](docs/19-rational-coset-expansion.md): rational-function expansion and the order-two exception.
- [`docs/20-common-ratio-bank-conversion.md`](docs/20-common-ratio-bank-conversion.md): exact rectangle collateral and decoder-or-structure conversion.
- [`docs/21-weighted-quotient-bank.md`](docs/21-weighted-quotient-bank.md): syndrome-weighted quotient extraction and paid-bank lower bounds.
- [`docs/22-incidence-conic-pencil.md`](docs/22-incidence-conic-pencil.md): projective conic-pencil geometry and secant profile.
- [`docs/23-aligned-anchor-carry-cells.md`](docs/23-aligned-anchor-carry-cells.md): aligned-anchor determinant factorization and carry cells.
- [`docs/24-secant-star-carry-dispersion.md`](docs/24-secant-star-carry-dispersion.md): universal product-carry dispersion.
- [`docs/25-perfect-alignment-arithmetic.md`](docs/25-perfect-alignment-arithmetic.md): interpolation-parameter arithmetic and chamber sparsity.
- [`docs/26-same-channel-cross-carries-and-wrap-centers.md`](docs/26-same-channel-cross-carries-and-wrap-centers.md): same-channel carries, rational centers, and chamber bounds.
- [`docs/26-alternating-star-neutralization.md`](docs/26-alternating-star-neutralization.md): two-colour endpoint-permutation repair banks.
- [`docs/27-all-n-prime-patching.md`](docs/27-all-n-prime-patching.md): exact boundary states and prime-gap transfer.
- [`docs/28-one-strip-and-pair-aware-patching.md`](docs/28-one-strip-and-pair-aware-patching.md): one-strip rigidity, blocker matchings, and corner endpoint.
- [`docs/29-general-reservoir-patching.md`](docs/29-general-reservoir-patching.md): arbitrary-reservoir and spread-bank endpoints.
- [`docs/30-deletion-aware-row-lift-banks.md`](docs/30-deletion-aware-row-lift-banks.md): deletion-aware one-strip certificates and row-lift spread.
- [`docs/31-sequential-row-lift-local-lemma.md`](docs/31-sequential-row-lift-local-lemma.md): prefix-aware permutation-layer selection.
- [`docs/32-row-lift-pruning-barriers.md`](docs/32-row-lift-pruning-barriers.md): static terminal loads, conditioned masses, and full-support barrier.
- [`docs/33-off-diagonal-reservoir-obstruction.md`](docs/33-off-diagonal-reservoir-obstruction.md): aligned block obstruction and projection classification.
- [`docs/34-projection-triple-lower-bounds.md`](docs/34-projection-triple-lower-bounds.md): quantitative parallel-line triple forcing.
- [`docs/35-component-clean-row-lift-banks.md`](docs/35-component-clean-row-lift-banks.md): component-clean expectation endpoint and cross-triple cap.
- [`docs/36-monotone-parabolic-reservoirs.md`](docs/36-monotone-parabolic-reservoirs.md): square-root internally clean parabolic matching patches.
- [`docs/37-variable-reservoir-patch-banks.md`](docs/37-variable-reservoir-patch-banks.md): deletion-aware banks whose states use different reservoirs.
- [`docs/38-parabolic-rung-budget.md`](docs/38-parabolic-rung-budget.md): multi-rung coordinate budget and prime-gap exponent conversion.
- [`docs/39-matching-reservoir-cycle-factorization.md`](docs/39-matching-reservoir-cycle-factorization.md): exact path/cycle factorization and deletion marginals.
- [`docs/40-cycle-reservoir-2sat.md`](docs/40-cycle-reservoir-2sat.md): exact 2-SAT selection for cycle-reservoir patches.
- [`docs/41-sheared-parabolic-banks.md`](docs/41-sheared-parabolic-banks.md): sheared internally clean banks with explicit cell/pair spread.
- [`docs/42-width-two-matching-patches.md`](docs/42-width-two-matching-patches.md): complete cross-only width-two classification and finite obstruction.
- [`docs/43-one-rectangle-patch-repair.md`](docs/43-one-rectangle-patch-repair.md): exact alternating-rectangle repair criterion and repaired extensions.
- [`docs/44-multi-rectangle-trade-banks.md`](docs/44-multi-rectangle-trade-banks.md): exact rank-three SAT bank and exhaustive two-switch classification.
- [`docs/45-joint-binary-trade-cnf.md`](docs/45-joint-binary-trade-cnf.md): unified binary rung, cycle, rectangle, and tomographic selection.
- [`docs/46-multistate-trade-banks.md`](docs/46-multistate-trade-banks.md): finite-state forbidden-box CSP with first-moment and local-lemma endpoints.
- [`docs/47-reverse-ordered-parabolic-rungs.md`](docs/47-reverse-ordered-parabolic-rungs.md): reverse-order slope separation and the three-rung clause reduction.
- [`docs/48-matching-density-and-matching-first.md`](docs/48-matching-density-and-matching-first.md): independent-template density barrier and universal matching-first reservoir bank.
- [`docs/49-universal-adjacent-width-two-rungs.md`](docs/49-universal-adjacent-width-two-rungs.md): canonical internally clean patch for every four-edge matching reservoir.
- [`docs/50-width-two-matching-first-spread.md`](docs/50-width-two-matching-first-spread.md): exact width-two spread and external-defect split.
- [`docs/51-matching-block-multistate-rungs.md`](docs/51-matching-block-multistate-rungs.md): equal-margin matching-block state spaces and unary pruning.
- [`docs/52-matching-block-local-loads.md`](docs/52-matching-block-local-loads.md): quantified clean-domain density from local certificate loads.
- [`docs/53-clean-rung-hypergraph-packing.md`](docs/53-clean-rung-hypergraph-packing.md): clean-state packing, degree spread, and transversal cores.
- [`docs/54-full-width-two-block-banks.md`](docs/54-full-width-two-block-banks.md): all 36 width-two geometries and improved clean-rung packing.
- [`docs/55-matching-block-global-endpoint.md`](docs/55-matching-block-global-endpoint.md): seven-profile global first-moment and occurrence endpoints.

## Research discipline

Every mathematical item is tagged as one of:

- **PROVED:** a complete proof is written in the repository.
- **PROVED UNDER HYPOTHESES:** the implication is complete, but a premise is not known in the desired construction.
- **CONDITIONAL:** a reduction or theorem schema whose premise remains open.
- **HEURISTIC:** a proposed mechanism, not a theorem.
- **REFUTED:** a tempting statement accompanied by a counterexample or impossibility proof.

The notebook deliberately keeps failed routes. In a long open problem, knowing
why a route fails is often as useful as a new lemma.

## Principal current pathway

The strongest global synthesis remains the modular-hyperbola, cycle-bank,
weighted-quotient, carry-dispersion, and alternating-neutralization route. Its
main unresolved step is a second-order concentration/termination theorem for
the normalized collateral of the joint alternating bank, followed by a
monotone carry potential or bounded-denominator absorber.

The independent all-`n` prime-patching track now has:

- exact fixed-, variable-, binary-, and multistate reservoir interfaces;
- internally clean row-lift, parabolic, and universal width-two patch families;
- a proof that independent linear-size sheared row/column boxes cannot have
  positive constant matching-admissible density at sublinear width;
- a universal matching-first bank with exact all-rank hypergeometric deletion
  spread for every saturated source;
- equal-margin matching blocks with `binom(r,4)` canonical states and
  `36 binom(r,4)` full width-two states;
- quantified local clean-domain density and failure concentration;
- clean-deletion hypergraph packing and small-transversal alternatives;
- a finite demonstration that the full 36-state family produces two disjoint
  locally clean rungs on stored sides eight through ten;
- an explicit seven-profile global completion inequality and bounded-occurrence
  alternative for external and cross-block triples.

Its remaining bottleneck is a correlated secant-shadow preparation theorem.
At the natural constant-width block scale `r=m^0.475`, one must prove a
polynomial clean-state density, a diffuse clean-deletion hypergraph large enough
to pack about `m^0.525/2` width-two rungs, and PP3ci profile counts—or PP3bl
block occurrences—below their explicit thresholds.

## Running the checks

The scripts require Python 3.10+ and only the standard library.

```bash
python scripts/verify_hyperbola.py --prime 17
python scripts/verify_conic_incidence.py --prime 17
python scripts/verify_no_three_certificate.py certificates/prime-patching-small.json
python scripts/analyze_deletion_aware_one_strip.py certificates/prime-patching-small.json
python scripts/analyze_row_lift_bank.py certificates/prime-patching-small.json --n 3 --rows 1,2,3
python scripts/analyze_parabolic_matching_reservoir.py certificates/prime-patching-small.json --widths 2
python scripts/solve_multistate_trade_bank.py experiments/four-state-trade-bank-n4.json
python scripts/analyze_matching_first_reservoirs.py certificates/prime-patching-small.json --widths 2,3
python scripts/verify_universal_width_two_rung.py --max-side 12
python scripts/analyze_matching_first_width_two.py certificates/prime-patching-small.json
python scripts/analyze_matching_block_states.py certificates/prime-patching-small.json
python scripts/analyze_matching_block_loads.py certificates/prime-patching-small.json
python scripts/analyze_clean_rung_hypergraph.py certificates/prime-patching-small.json
python scripts/analyze_full_width_two_block_bank.py certificates/prime-patching-small.json
```

These programs are sanity checks or finite exhaustive checks, not proofs for
arbitrary `n` unless explicitly paired with a proved finite classification.

## Primary references

- Ghosal, Goenka, Grebennikov, Keevash, Kwan, Pham, *No-(k+1)-in-line problem for k>=3*, arXiv:2607.05255.
- Kovács, Nagy, Szabó, *Randomised algebraic constructions for the no-(k+1)-in-line problem*, arXiv:2508.07632.
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
- prove a quantitative blocker, anchor, or cross-block signature bound for a
  matching block of size `r=m^0.475`;
- construct a source layer whose 36-clean deletion hypergraph has large matching
  number and no small transversal core;
- prepare protected rectangle or tomographic trades around the transversal core;
- improve the conditioning loss in PP3ch or the seven-profile PP3ci endpoint;
- prepare a larger endpoint-adapted rung family correlated through source edges;
- prove the second-order concentration theorem for the alternating neutralization bank;
- construct a monotone carry-signature potential or bounded-denominator absorber;
- build a superregular perfect-matching resampling oracle.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).