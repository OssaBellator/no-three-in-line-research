# No-Three-in-Line Research Notebook

A rigorous research notebook for attempts toward the classical conjecture

\[
D(n)=2n,
\]

where `D(n)` is the maximum number of points that can be selected from an
`n x n` integer grid with no three collinear.

> **Status:** This repository does **not** contain a complete proof. The
> conjecture remains open as of 24 July 2026. The notebook preserves proved
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
- [`docs/22-incidence-conic-pencil.md`](docs/22-incidence-conic-pencil.md) through [`docs/26-alternating-star-neutralization.md`](docs/26-alternating-star-neutralization.md): conic incidence, carry cells, perfect alignment, wrap centers, and alternating repair.
- [`docs/27-all-n-prime-patching.md`](docs/27-all-n-prime-patching.md) through [`docs/55-matching-block-global-endpoint.md`](docs/55-matching-block-global-endpoint.md): boundary, row-lift, parabolic, width-two, variable-reservoir, trade-bank, and matching-block patching.
- [`docs/56-random-matching-block-sparsification.md`](docs/56-random-matching-block-sparsification.md) through [`docs/71-global-slot-occurrence-endpoint.md`](docs/71-global-slot-occurrence-endpoint.md): random pool sparsification, square-root macro construction, source cleaning, conditional spread, and global occurrence budgets.
- [`docs/72-same-edge-anchor-domain-pruning.md`](docs/72-same-edge-anchor-domain-pruning.md) through [`docs/77-one-sided-slab-cross-macro-separation.md`](docs/77-one-sided-slab-cross-macro-separation.md): refined anchor-safe domains, weighted event mass, grouped completion energy, coordinate correction, global label allocation, and slab separation.
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

### Modular-hyperbola and alternating-neutralization route

The strongest repository-wide synthesis combines modular hyperbolas, Möbius
cycle banks, weighted quotient extraction, carry dispersion, and alternating
endpoint neutralization. Its main unresolved step is a second-order
concentration/termination theorem for the joint alternating bank, followed by a
monotone carry potential or bounded-denominator absorber.

### All-`n` prime-patching route

The independent prime-patching branch now reaches the published prime-gap scale
internally.

At the balanced exponents

```text
macro variables M = m^(23/80+o(1)) = m^0.2875
source-pool size R = m^(19/40+o(1)) = m^0.475
macro width W = Theta(sqrt(R))      = m^0.2375
total width T=MW                    = m^0.525.
```

The branch proves:

- universal matching-pool supply from every saturated source;
- exact equal-margin restoration;
- internally no-three square-root macro patches by a product-space local lemma;
- conditioned fixed-rank spread `O(R^-q)`;
- fixed-pair source cleaning through dense edge domains;
- exact same-edge anchor factorization and label-dependent domain pruning;
- a weighted global local-lemma endpoint charging incident probability mass;
- grouped pair/triple completion-energy formulas;
- saturation-compatible global ownership of all final new labels;
- universal one-sided slab separation removing one high-probability cross-macro direction.

A key correction is also recorded: unused numerical candidate labels are not
free. Selecting `W<L` coordinates from an `L`-coordinate interval leaves the
other final rows and columns unsaturated, and arbitrary compression need not
preserve collinearity. The valid replacement assigns **all** `T=MW` final new
rows and columns globally among the macros.

The remaining bottleneck is now quantitative:

1. prove a balanced global refined-label ownership and perfect matching, or
   exploit the resulting boundary-shadow, Hall, exact bad-incidence, and
   divisor-energy concentration with protected trades;
2. after source cleaning and slab cancellation, prove grouped ordinary-anchor
   and residual cross-macro event mass at most `1/48-o(1)` at every slot.

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
- prove balanced global refined-label allocation at the macro scale;
- bound grouped pair/triple completion energy below the weighted slot threshold;
- regularize a boundary-shadow, Hall, bad-incidence, or divisor-energy concentration;
- build protected rectangle, cycle, or tomographic trades around the concentrated core;
- prove the second-order concentration theorem for the alternating-neutralization bank;
- construct a monotone carry-signature potential or bounded-denominator absorber;
- build a superregular perfect-matching resampling oracle.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).