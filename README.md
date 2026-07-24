# No-Three-in-Line Research Notebook

A rigorous research notebook for attempts toward the classical conjecture

\[
D(n)=2n,
\]

where `D(n)` is the maximum number of points that can be selected from an
`n x n` integer grid with no three collinear.

> **Status:** This repository does **not** contain a complete proof. The
> conjecture remains open as of 25 July 2026. The notebook preserves proved
> lemmas, conditional reductions, failed pathways, counterexamples,
> computational tools, and concrete next targets for independent checking.

## Repository map

- [`STATUS.md`](STATUS.md): current status and honesty ledger.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): repository-wide theorem classification.
- [`proofs/prime-patching-recent-index.md`](proofs/prime-patching-recent-index.md): focused PP2--PP3 theorem chain for the all-`n` branch.
- [`tracks/all-n-prime-patching.md`](tracks/all-n-prime-patching.md): current prime-size patching roadmap.
- [`docs/00-problem-and-literature.md`](docs/00-problem-and-literature.md): problem, literature, and conventions.
- [`docs/01-saturation-and-reservoirs.md`](docs/01-saturation-and-reservoirs.md): two-per-row/column framework and secant shadows.
- [`docs/02-reverse-scale-switching.md`](docs/02-reverse-scale-switching.md) through [`docs/07-failed-wall-pathway.md`](docs/07-failed-wall-pathway.md): switching, local banks, trades, absorbers, and failed wall expansion.
- [`docs/08-hyperbola-interleaver.md`](docs/08-hyperbola-interleaver.md) through [`docs/13-carry-cycle-dispersion.md`](docs/13-carry-cycle-dispersion.md): modular hyperbolas, Möbius cycles, Tanner interpretations, and carry-cycle concentration.
- [`docs/15-degree-constrained-hypergraph-selection.md`](docs/15-degree-constrained-hypergraph-selection.md) through [`docs/21-weighted-quotient-bank.md`](docs/21-weighted-quotient-bank.md): clone-space selection, superregular spread, inverse-additive structure, and paid rectangle banks.
- [`docs/22-incidence-conic-pencil.md`](docs/22-incidence-conic-pencil.md) through [`docs/26-alternating-star-neutralization.md`](docs/26-alternating-star-neutralization.md): conic incidence, carry cells, perfect alignment, wrap centres, and alternating repair.
- [`docs/27-all-n-prime-patching.md`](docs/27-all-n-prime-patching.md) through [`docs/55-matching-block-global-endpoint.md`](docs/55-matching-block-global-endpoint.md): boundary, row-lift, parabolic, width-two, variable-reservoir, trade-bank, and matching-block patching.
- [`docs/56-random-matching-block-sparsification.md`](docs/56-random-matching-block-sparsification.md) through [`docs/71-global-slot-occurrence-endpoint.md`](docs/71-global-slot-occurrence-endpoint.md): random pool sparsification, square-root macro construction, source cleaning, conditional spread, and global occurrence budgets.
- [`docs/72-same-edge-anchor-domain-pruning.md`](docs/72-same-edge-anchor-domain-pruning.md) through [`docs/77-one-sided-slab-cross-macro-separation.md`](docs/77-one-sided-slab-cross-macro-separation.md): refined anchor-safe domains, weighted event mass, grouped completion energy, coordinate correction, global label allocation, and slab separation.
- [`docs/78-ore-balanced-global-allocation.md`](docs/78-ore-balanced-global-allocation.md) through [`docs/88-endpoint-derangement-first-moment.md`](docs/88-endpoint-derangement-first-moment.md): complementary-degree allocation, slab-optimal exponents, patch and anchor energy closure, controller-aware domains, blocker-resource extraction, and paid endpoint-permutation trades.
- [`docs/12-failed-claims-ledger.md`](docs/12-failed-claims-ledger.md): corrected, weakened, and refuted claims.

## Research discipline

Every mathematical item is tagged as one of:

- **PROVED:** a complete proof is written in the repository.
- **PROVED UNDER HYPOTHESES:** the implication is complete, but a premise remains open.
- **CONDITIONAL:** a reduction or theorem schema with an unresolved premise.
- **HEURISTIC:** a proposed mechanism, not a theorem.
- **REFUTED:** a tempting statement with a counterexample or impossibility proof.

Failed routes remain in the notebook because they often isolate the exact
structure a successful proof must exploit.

## Principal current pathways

### Modular-hyperbola and alternating-neutralisation route

The strongest repository-wide synthesis combines modular hyperbolas, Möbius
cycle banks, weighted quotient extraction, carry dispersion, and alternating
endpoint neutralisation. Its main unresolved step is a second-order
concentration/termination theorem for the joint alternating bank, followed by a
monotone carry potential or bounded-denominator absorber.

### All-`n` prime-patching route

The independent prime-patching branch reaches the published prime-gap scale
internally with the exponent-optimal disjoint square-root-macro balance

```text
macro variables M = m^(1/20+o(1))  = m^0.05
source-pool size R = m^(19/20+o(1)) = m^0.95
macro width W     = m^(19/40+o(1)) = m^0.475
total width T=MW  = m^(21/40+o(1)) = m^0.525.
```

The branch proves:

- universal slab matching-pool supply from every saturated source;
- exact equal-margin restoration;
- internally no-three square-root macro patches by a product-space local lemma;
- conditioned fixed-rank spread `O(R^-q)`;
- exponent optimality of the `M,R,W` balance within disjoint square-root macros;
- saturation-compatible use of all final numerical labels;
- complementary-degree global allocation criteria, weaker than separate `T/2` minimum degrees;
- controller-aware unary source safety that includes unselected active-pool edges;
- `o(1)` incident mass for every patch-only cross-macro event;
- `o(1)` incident mass for every ordinary two-slot source-anchor event;
- blocker-star or resource-matching structure from positive controller-shadow failure;
- exact removal-credit minus insertion-cost identities for endpoint-permutation trades;
- a spread-derangement first-moment endpoint for source validity and collateral.

A key correction is that fixed-core safe domains do not automatically handle
blocker pairs using unselected matching-pool edges. The correct domain allows a
candidate value only when every blocker pair through its inserted cells contains
the selected controller edge, which is deleted.

The weighted rank-two/rank-three completion-energy side is now closed at the
slab-optimal scale. The remaining bottleneck is one controller-shadow conversion
theorem:

1. prove the controller-aware global label graphs satisfy the complementary-degree allocation criterion; or
2. convert the forced blocker star or resource matching into a source-admissible endpoint, rectangle, or tomographic trade whose inserted shadow is below its paid removal credit.

The focused theorem statements and exact formulas are in
[`proofs/prime-patching-recent-index.md`](proofs/prime-patching-recent-index.md).

## Running the checks

The scripts require Python 3.10+ and use only the standard library.

```bash
python scripts/verify_hyperbola.py --prime 17
python scripts/verify_conic_incidence.py --prime 17
python scripts/verify_no_three_certificate.py certificates/prime-patching-small.json
python scripts/analyze_deletion_aware_one_strip.py certificates/prime-patching-small.json
python scripts/analyze_row_lift_bank.py certificates/prime-patching-small.json --n 3 --rows 1,2,3
python scripts/analyze_parabolic_matching_reservoir.py certificates/prime-patching-small.json --widths 2
python scripts/solve_multistate_trade_bank.py experiments/four-state-trade-bank-n4.json
python scripts/analyze_full_width_two_block_bank.py certificates/prime-patching-small.json
python scripts/check_weighted_slot_mass.py experiments/weighted-slot-mass-example.json
python scripts/analyze_same_edge_anchor_domains.py certificates/prime-patching-small.json --labels 12 --gamma 1/3 --epsilon 1/6 --output /tmp/refined-labels.json
python scripts/check_oversampled_label_matching.py /tmp/refined-labels.json
python scripts/check_global_label_ore.py experiments/global-label-ore-example.json
```

These programs are sanity checks or finite exhaustive checks, not proofs for
arbitrary `n` unless paired with a proved finite classification.

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

- verify or repair a result tagged **PROVED**;
- prove complementary-degree allocation for the controller-aware label graphs;
- bound or regularise the noncontroller blocker shadow of slab matching pools;
- convert the blocker-star or resource-matching alternative by an endpoint,
  rectangle, cycle, or tomographic trade;
- improve the spread-derangement collateral bound on the extracted endpoint rectangle;
- prove the second-order concentration theorem for the alternating-neutralisation bank;
- construct a monotone carry-signature potential or bounded-denominator absorber;
- build a superregular perfect-matching resampling oracle.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).
