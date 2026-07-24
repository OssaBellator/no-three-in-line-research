# No-Three-in-Line Research Notebook

A rigorous research notebook for attempts toward the classical conjecture

\[
D(n)=2n,
\]

where \(D(n)\) is the maximum number of points that can be selected from an
\(n\times n\) integer grid with no three collinear.

> **Status:** This repository does **not** contain a complete proof. The
> conjecture remains open as of 24 July 2026. The notebook preserves proved
> lemmas, conditional reductions, failed pathways, counterexamples,
> computational certificates, and precise next targets.

## Repository map

- [`STATUS.md`](STATUS.md): current honesty ledger.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): global theorem index.
- [`proofs/composite-modulus-theorem-index.md`](proofs/composite-modulus-theorem-index.md): composite-track theorem index.
- [`proofs/composite-modulus-theorem-index-addendum.md`](proofs/composite-modulus-theorem-index-addendum.md): current CMR102+ addendum.
- [`tracks/all-n-composite-modulus.md`](tracks/all-n-composite-modulus.md): original composite task track.
- [`tracks/all-n-composite-modulus-progress.md`](tracks/all-n-composite-modulus-progress.md): CM1–CM6 progress and bottlenecks.

### General repair programme

- [`docs/01-saturation-and-reservoirs.md`](docs/01-saturation-and-reservoirs.md): saturation, clones, deficits, and secant shadows.
- [`docs/02-reverse-scale-switching.md`](docs/02-reverse-scale-switching.md): descending-scale potential and batch repair.
- [`docs/03-uniform-local-bank.md`](docs/03-uniform-local-bank.md): spread injection and local-bank hypotheses.
- [`docs/04-protected-tomographic-trades.md`](docs/04-protected-tomographic-trades.md): exact line-sum-preserving trades.
- [`docs/05-subgroup-absorbers.md`](docs/05-subgroup-absorbers.md): affine configurations and coset absorbers.
- [`docs/06-block-collateral-energy.md`](docs/06-block-collateral-energy.md): exact block collateral and closure.
- [`docs/08-hyperbola-interleaver.md`](docs/08-hyperbola-interleaver.md): complementary hyperbolas and Hamiltonian interleavers.
- [`docs/09-orbit-tanner-and-mobius-cycles.md`](docs/09-orbit-tanner-and-mobius-cycles.md): orbit codebooks, secant matchings, and cycle trades.
- [`docs/13-carry-cycle-dispersion.md`](docs/13-carry-cycle-dispersion.md): frozen-cycle counterexample and corrected bank theorem.
- [`docs/15-degree-constrained-hypergraph-selection.md`](docs/15-degree-constrained-hypergraph-selection.md): clone-space exact selection endpoint.
- [`docs/16-superregular-clone-selection.md`](docs/16-superregular-clone-selection.md): dense matching spread and global conflict mass.
- [`docs/17-pfr-inverse-additive.md`](docs/17-pfr-inverse-additive.md) through [`docs/21-weighted-quotient-bank.md`](docs/21-weighted-quotient-bank.md): inverse-additive structure and paid common-ratio banks.
- [`docs/22-incidence-conic-pencil.md`](docs/22-incidence-conic-pencil.md) through [`docs/26-alternating-star-neutralization.md`](docs/26-alternating-star-neutralization.md): carry cells, perfect alignment, wrap centers, and alternating repair banks.
- [`docs/12-failed-claims-ledger.md`](docs/12-failed-claims-ledger.md): corrected and refuted claims.

### Composite and prime-power programme

- [`docs/27-composite-modulus-obstructions.md`](docs/27-composite-modulus-obstructions.md): affine saturation, universal affine obstruction, composite hyperbola collapses, and CRT limitations.
- [`docs/28-prime-power-completed-reciprocals.md`](docs/28-prime-power-completed-reciprocals.md) through [`docs/33-prime-power-companion-compatible-blocks.md`](docs/33-prime-power-companion-compatible-blocks.md): nonlinear full channels, tangent cells, displacement equations, top-digit blocks, and companion-compatible banks.
- [`docs/34-prime-power-block-bank-collateral.md`](docs/34-prime-power-block-bank-collateral.md) through [`docs/38-prime-power-recursive-determinant-carries.md`](docs/38-prime-power-recursive-determinant-carries.md): all-stratum product banks, terminal obstruction, recursive quotient lifts, and determinant carries.
- [`docs/39-crt-mixed-collision-factorization.md`](docs/39-crt-mixed-collision-factorization.md) through [`docs/43-prime-power-terminal-spread-family.md`](docs/43-prime-power-terminal-spread-family.md): CRT mixed collisions, tangent spacing, harmonic energy, and all-prime terminal families.
- [`docs/44-prime-power-global-energy-bound.md`](docs/44-prime-power-global-energy-bound.md) and [`docs/45-prime-power-companion-global-syndrome.md`](docs/45-prime-power-companion-global-syndrome.md): quadratic-order one- and two-layer syndrome bounds.
- [`docs/46-crt-local-arc-obstruction.md`](docs/46-crt-local-arc-obstruction.md) through [`docs/52-crt-slope-carry-signatures.md`](docs/52-crt-slope-carry-signatures.md): corrected CRT taxonomy, restricted recursive banks, exact average roots, recursive dispersion, digital obstruction, and slope-carry signatures.
- [`docs/53-prime-power-divisor-collision-energy.md`](docs/53-prime-power-divisor-collision-energy.md) through [`docs/59-prime-power-binary-cluster-sum.md`](docs/59-prime-power-binary-cluster-sum.md): divisor-collision reduction, singular sums, first-separation summation, and binary-cluster localization.
- [`docs/60-prime-power-prefix-star-neutralization.md`](docs/60-prime-power-prefix-star-neutralization.md) through [`docs/67-prime-power-child-core-cancellation.md`](docs/67-prime-power-child-core-cancellation.md): prefix repair, quotient charging, higher-rank collateral, descending invariance, and recursive-compatible node banks.
- [`docs/68-prime-power-child-translation-pencils.md`](docs/68-prime-power-child-translation-pencils.md) through [`docs/70-prime-power-alternating-pencil-certificates.md`](docs/70-prime-power-alternating-pencil-certificates.md): child pencils, diffuse-or-alternating extraction, and frozen rank certificates.
- [`docs/71-prime-power-balanced-law-classification.md`](docs/71-prime-power-balanced-law-classification.md) through [`docs/73-prime-seven-pair-spectrum.md`](docs/73-prime-seven-pair-spectrum.md): reciprocal-law obstruction and balanced recursive banks at every power of seven.
- [`docs/74-prime-power-global-baseline-alternating-closure.md`](docs/74-prime-power-global-baseline-alternating-closure.md) and [`docs/75-degree-two-small-matching-existence.md`](docs/75-degree-two-small-matching-existence.md): global-baseline closure compression and the sharp size-four matching threshold.
- [`docs/76-prime-power-paid-geometry-to-alternating-banks.md`](docs/76-prime-power-paid-geometry-to-alternating-banks.md) through [`docs/78-prime-power-four-endpoint-core.md`](docs/78-prime-power-four-endpoint-core.md): geometric continuation, target-load descent, exact four-board atoms, and balanced terminal defect-flow cycles.
- [`docs/79-four-endpoint-trap-counterexample.md`](docs/79-four-endpoint-trap-counterexample.md): an exact potential-one terminal two-cycle and the corrected inherited-escape target.
- [`proofs/composite-finite-constructions.md`](proofs/composite-finite-constructions.md): exact saturated constructions at \(N=4,6,8,9,10,12\).

## Research discipline

Every mathematical item is tagged as one of:

- **PROVED:** a complete proof is written in the repository.
- **PROVED UNDER HYPOTHESES:** the implication is complete, but a premise remains open.
- **CONDITIONAL:** a reduction or theorem schema with an unresolved premise.
- **HEURISTIC:** a proposed mechanism rather than a theorem.
- **REFUTED:** a tempting statement accompanied by a counterexample or exact obstruction.

The notebook deliberately retains failed routes. In an open problem, an exact
obstruction is often as valuable as a positive lemma.

## Principal current pathways

### Prime-field repair

Start from complementary modular hyperbolas, encode row-column-preserving
changes through orbit or rectangle banks, use inverse-additive extraction and
carry classification, neutralize dominant secant stars, and finish with a
clone-space or superregular exact-selection theorem. Exact terminal traps show
that normalized local dynamics alone is insufficient; an escape must use
channel ancestry or a larger joint move.

### Composite prime-power route

Start from completed-reciprocal full channels and their companion layer. Use
the recursive all-stratum fibre bank, prefix-star repair, and child-pencil
alternating banks. The generic first-separation and prefix-collateral sums are
closed at quadratic-polylogarithmic scale. Balanced recursive banks exist for
all \(p\equiv1\pmod4\) and, through a non-reciprocal factorization, for every
power of seven.

Every globally nonimproving alternating closure contracts to a four-endpoint
board destroying one specified triple. Exact four-core traps exist in general,
so the principal missing theorem is an **inherited escape** using prefix node,
scale, quotient state, opposite-layer ancestry, or carry signatures. Arbitrary
composite assembly additionally requires a separate coverage mechanism.

## Running checks

The scripts require Python 3.10+ and use the standard library unless a search
script explicitly documents an optional solver.

```bash
python scripts/verify_composite_modulus.py --max-modulus 40
python scripts/verify_prime_power_channels.py --max-modulus 125
python scripts/verify_prime_power_first_separation_sum.py --max-modulus 125
python scripts/verify_prime_power_quotient_excess.py
python scripts/verify_prime_power_higher_rank_prefix.py
python scripts/verify_prime_power_child_translation_pencils.py
python scripts/verify_prime_power_child_pencil_dichotomy.py
python scripts/verify_prime_power_alternating_pencil_certificates.py
python scripts/verify_prime_power_global_baseline_closure.py
python scripts/verify_prime_power_paid_geometry_conversion.py
python scripts/verify_prime_power_target_load_closure.py
python scripts/verify_prime_power_four_endpoint_core.py
python scripts/verify_prime_power_balanced_law_classification.py
python scripts/verify_prime_seven_balanced_bank.py
python scripts/verify_prime_seven_pair_spectrum.py
python scripts/verify_prime_power_cross_stratum_sum.py --max-modulus 125
python scripts/verify_digital_64_completion_obstruction.py
python scripts/verify_composite_finite_extensions.py
```

These programs are sanity checks and exact finite certificates, not proofs for
arbitrary \(n\) unless the corresponding document supplies the general proof.

## Primary references

- Ghosal, Goenka, Grebennikov, Keevash, Kwan, Pham, *No-\((k+1)\)-in-line problem for \(k\ge3\)*, arXiv:2607.05255.
- Kovács, Nagy, Szabó, *Randomised algebraic constructions for the no-\((k+1)\)-in-line problem*, arXiv:2508.07632.
- Reiher, Schoen, *Note on the Theorem of Balog, Szemeredi, and Gowers*, arXiv:2308.10245.
- Gowers, Green, Manners, Tao, *Marton's Conjecture in abelian groups with bounded torsion*, arXiv:2404.02244.
- Nenadov, Pham, *Spread blow-up lemma with an application to perturbed random graphs*, arXiv:2410.06132.
- Glock, Joos, Kim, Kühn, Lichev, *Conflict-free hypergraph matchings*, arXiv:2205.05564.
- Joos, Mubayi, Smith, *Conflict-free Hypergraph Matchings and Coverings*, arXiv:2407.18144.
- Lu, Szekely, *A new asymptotic enumeration technique: the Lovasz Local Lemma*, arXiv:0905.3983.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).
