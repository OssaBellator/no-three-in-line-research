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
- [`docs/02-reverse-scale-switching.md`](docs/02-reverse-scale-switching.md) through [`docs/26-alternating-star-neutralization.md`](docs/26-alternating-star-neutralization.md): switching, algebraic banks, protected trades, absorbers, and alternating neutralisation.
- [`docs/27-all-n-prime-patching.md`](docs/27-all-n-prime-patching.md) through [`docs/55-matching-block-global-endpoint.md`](docs/55-matching-block-global-endpoint.md): boundary, row-lift, parabolic, width-two, variable-reservoir, trade-bank, and matching-block patching.
- [`docs/56-random-matching-block-sparsification.md`](docs/56-random-matching-block-sparsification.md) through [`docs/77-one-sided-slab-cross-macro-separation.md`](docs/77-one-sided-slab-cross-macro-separation.md): random sparsification, square-root macros, source cleaning, weighted event mass, global labels, and slab separation.
- [`docs/78-ore-balanced-global-allocation.md`](docs/78-ore-balanced-global-allocation.md) through [`docs/89-controller-shadow-monotone-termination.md`](docs/89-controller-shadow-monotone-termination.md): complementary-degree allocation, slab-optimal exponents, external-energy closure, controller-aware domains, structural extraction, paid endpoint trades, and termination.
- [`docs/90-superregular-paid-endpoint-trades.md`](docs/90-superregular-paid-endpoint-trades.md) through [`docs/96-shadow-support-permutation-cleaning.md`](docs/96-shadow-support-permutation-cleaning.md): endpoint-host regularisation, permutation local lemmas, transition divisor bounds, two-scale source-valid thinning, protected credit, and zero-cost shadow-support cleaning.
- [`docs/97-zero-unary-shadow-hall-rectangles.md`](docs/97-zero-unary-shadow-hall-rectangles.md) through [`docs/101-dynamic-pool-excess-shadow-potential.md`](docs/101-dynamic-pool-excess-shadow-potential.md): zero-unary Hall endpoints, support cores, source-star correction, line/fan localisation, and pairing-invariant dynamic shadow.
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

The independent prime-patching branch reaches the published prime-gap scale with
the exponent-optimal disjoint square-root-macro balance

```text
macro variables M = m^(1/20+o(1))   = m^0.05
source-pool size R = m^(19/20+o(1)) = m^0.95
macro width W     = m^(19/40+o(1))  = m^0.475
total width T=MW  = m^(21/40+o(1))  = m^0.525.
```

The branch proves:

- universal slab matching-pool supply and exact degree restoration;
- internally no-three square-root macro patches and fixed-rank spread;
- exponent optimality within disjoint square-root macros;
- saturation-compatible use of every final numerical label;
- complementary-degree global allocation criteria;
- controller-aware source safety including unselected active-pool edges;
- `o(1)` incident mass for every remaining external pair/triple class;
- source-endpoint-star or resource-matching structure from positive shadow failure;
- source-valid resource endpoint conversion after two-scale thinning;
- exact elimination of diffuse residual insertion shadow;
- exact Hall rectangles for zero-unary endpoint failure;
- linear unary/binary support-core extraction;
- tomographic recapture-line and binary cell-fan localisation;
- a pairing-invariant excess-shadow potential for dynamic within-pool trades.

For the resource bank, sparse unary endpoint shadow permits thinning to

\[
q=m^\kappa,
\qquad
0<\kappa<\frac1{40},
\]

followed by superregular pruning, permutation-LLL cleaning, divisor
regularisation of anchored transitions, and support-rank thinning. This produces
a saturation-preserving no-three endpoint trade.

Direct recapture and residual unary insertion-shadow cells may be removed from a
single zero-unary host `G_0`. If it has no perfect matching, Hall supplies

\[
|X|+|Y|>q,
\qquad
X\times Y\subseteq E(\overline{G_0}).
\]

A macroscopic rectangle contains a quadratic single-type witness core. A
recapture core yields a linear bank of lines with linear endpoint intersections.
A cubic binary support core yields either a linear endpoint-cell fan or a linear
resource-disjoint conflict bank.

Within a controller pool, endpoint permutations preserve the pool's column and
row sets and hence its complete candidate-cell universe. Every candidate has one
automatic controller-containing axis blocker, so

\[
\Xi(S)=\sum_z\bigl(b_S(z)-1\bigr)
\]

counts exactly the excess nonaxis blockers. Captive source-star centres can
therefore be moved under a fixed candidate-cell potential; their remaining issue
is geometric source admissibility and insertion cost, not controller relabelling.

The remaining bottleneck has five forms:

1. prove the controller-aware global graphs satisfy complementary degree;
2. convert a Hall rectangle or a matchable but non-superregular zero-unary host;
3. convert the rich recapture-line bank;
4. convert the binary endpoint-cell fan or resource-disjoint binary bank;
5. construct source-admissible pool-compatible trades with `Xi` insertion cost
   below the star/resource removal credit.

The focused statements and exact formulas are in
[`proofs/prime-patching-recent-index.md`](proofs/prime-patching-recent-index.md).

## Running the checks

The scripts require Python 3.10+ and use only the standard library.

```bash
python scripts/verify_hyperbola.py --prime 17
python scripts/verify_conic_incidence.py --prime 17
python scripts/verify_no_three_certificate.py certificates/prime-patching-small.json
python scripts/solve_multistate_trade_bank.py experiments/four-state-trade-bank-n4.json
python scripts/check_weighted_slot_mass.py experiments/weighted-slot-mass-example.json
python scripts/check_global_label_ore.py experiments/global-label-ore-example.json
python scripts/analyze_controller_aware_domains.py certificates/prime-patching-small.json --labels 12 --gamma 1/3
python scripts/analyze_endpoint_trade_hosts.py certificates/prime-patching-small.json
python scripts/analyze_endpoint_hall_rectangles.py certificates/prime-patching-small.json
python scripts/analyze_dynamic_cell_shadow.py certificates/prime-patching-small.json --labels 12
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

## Contribution guidance

A useful contribution should do at least one of the following:

- verify or repair a result tagged **PROVED**;
- prove complementary-degree allocation for the controller-aware label graphs;
- convert zero-unary Hall rectangles or non-superregular matchable hosts;
- convert rich recapture-line banks;
- convert binary endpoint-cell fans or resource-disjoint binary banks;
- construct source-admissible pool-compatible trades with negative `Xi` change;
- prove the second-order concentration theorem for the alternating-neutralisation bank;
- construct a monotone carry-signature potential or bounded-denominator absorber;
- build a superregular perfect-matching resampling oracle.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).
