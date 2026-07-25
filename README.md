# No-Three-in-Line Research Notebook

A rigorous research notebook for attempts toward the classical conjecture

\[
D(n)=2n,
\]

where \(D(n)\) is the maximum number of points that can be selected from an
\(n\times n\) integer grid with no three collinear.

> **Status:** This repository does **not** contain a complete proof. The
> conjecture remains open as of 25 July 2026. The notebook preserves proved
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

- [`docs/01-saturation-and-reservoirs.md`](docs/01-saturation-and-reservoirs.md) through [`docs/06-block-collateral-energy.md`](docs/06-block-collateral-energy.md): saturation, reverse-scale repair, spread banks, tomographic trades, absorbers, and exact block collateral.
- [`docs/08-hyperbola-interleaver.md`](docs/08-hyperbola-interleaver.md) through [`docs/13-carry-cycle-dispersion.md`](docs/13-carry-cycle-dispersion.md): complementary hyperbolas, orbit/cycle banks, and the corrected frozen-cycle theorem.
- [`docs/15-degree-constrained-hypergraph-selection.md`](docs/15-degree-constrained-hypergraph-selection.md) and [`docs/16-superregular-clone-selection.md`](docs/16-superregular-clone-selection.md): clone-space exact selection, dense spread matchings, and global conflict-mass endpoints.
- [`docs/17-pfr-inverse-additive.md`](docs/17-pfr-inverse-additive.md) through [`docs/26-alternating-star-neutralization.md`](docs/26-alternating-star-neutralization.md): inverse-additive structure, quotient banks, carry cells, wrap centers, and alternating repair.
- [`docs/12-failed-claims-ledger.md`](docs/12-failed-claims-ledger.md): corrected and refuted claims.

### Composite and prime-power programme

- [`docs/27-composite-modulus-obstructions.md`](docs/27-composite-modulus-obstructions.md) through [`docs/33-prime-power-companion-compatible-blocks.md`](docs/33-prime-power-companion-compatible-blocks.md): composite obstructions, nonlinear full channels, tangent cells, displacement, and companion-compatible blocks.
- [`docs/34-prime-power-block-bank-collateral.md`](docs/34-prime-power-block-bank-collateral.md) through [`docs/45-prime-power-companion-global-syndrome.md`](docs/45-prime-power-companion-global-syndrome.md): recursive quotient banks, determinant carries, terminal spread, and quadratic-order syndrome bounds.
- [`docs/46-crt-local-arc-obstruction.md`](docs/46-crt-local-arc-obstruction.md) through [`docs/59-prime-power-binary-cluster-sum.md`](docs/59-prime-power-binary-cluster-sum.md): CRT taxonomy, digital obstruction, divisor collisions, first-separation summation, and binary-star localization.
- [`docs/60-prime-power-prefix-star-neutralization.md`](docs/60-prime-power-prefix-star-neutralization.md) through [`docs/70-prime-power-alternating-pencil-certificates.md`](docs/70-prime-power-alternating-pencil-certificates.md): prefix repair, quotient charging, higher-rank collateral, descending invariance, child pencils, and frozen rank certificates.
- [`docs/71-prime-power-balanced-law-classification.md`](docs/71-prime-power-balanced-law-classification.md) through [`docs/73-prime-seven-pair-spectrum.md`](docs/73-prime-seven-pair-spectrum.md): reciprocal-law classification and balanced recursive banks at powers of seven.
- [`docs/74-prime-power-global-baseline-alternating-closure.md`](docs/74-prime-power-global-baseline-alternating-closure.md) through [`docs/79-four-endpoint-trap-counterexample.md`](docs/79-four-endpoint-trap-counterexample.md): global-baseline compression, target-load descent, exact terminal boards, and the abstract four-core trap.
- [`docs/80-prime-five-four-core-escape.md`](docs/80-prime-five-four-core-escape.md) through [`docs/88-prime-power-inherited-four-core-cover.md`](docs/88-prime-power-inherited-four-core-cover.md): exact root escapes, joint-parent banks, closure envelopes, sharp derangement laws, and inherited terminal covers.
- [`docs/89-prime-power-parent-cover-lifting.md`](docs/89-prime-power-parent-cover-lifting.md) through [`docs/95-prime-power-iterated-hall-wall-peeling.md`](docs/95-prime-power-iterated-hall-wall-peeling.md): parent-cover lifting, the \(2/11\) batch deficit, envelope expansion, line signatures, Hall walls, and iterative peeling.
- [`docs/96-prime-power-essential-edge-factorization.md`](docs/96-prime-power-essential-edge-factorization.md) through [`docs/101-prime-power-exact-top-height-slice.md`](docs/101-prime-power-exact-top-height-slice.md): half-degree flexibility, exchange ancestry, local loads, bounded dyadic conflicts, odd-line deletion resilience, and exact top-slice cleaning.
- [`docs/102-prime-power-near-transversal-line-resilience.md`](docs/102-prime-power-near-transversal-line-resilience.md) through [`docs/113-prime-power-mod-six-height-cleaning.md`](docs/113-prime-power-mod-six-height-cleaning.md): line-deletion reserves, target-specific Hall blockers, refined high-slice cleaning, fan obstructions, and Hall-width reduction.
- [`docs/114-prime-power-thin-blocker-cover-expansion.md`](docs/114-prime-power-thin-blocker-cover-expansion.md) through [`docs/123-prime-power-mixed-fan-factorial-carry.md`](docs/123-prime-power-mixed-fan-factorial-carry.md): thin blocker extraction, first-separation signatures, carry cells, witness routing, and mixed-fan factorial carries.
- [`docs/124-prime-power-paid-mixed-ratio-bank.md`](docs/124-prime-power-paid-mixed-ratio-bank.md) through [`docs/130-prime-power-token-reintroduction-ledger.md`](docs/130-prime-power-token-reintroduction-ledger.md): paid ratio banks, line-clean completions, heavy-cell continuation, dispersed-token packing, and dynamic token-edge inventory.
- [`docs/131-prime-power-line-clean-line-energy.md`](docs/131-prime-power-line-clean-line-energy.md) and [`docs/132-prime-power-line-energy-to-carry-cells.md`](docs/132-prime-power-line-energy-to-carry-cells.md): frozen line energy, dyadic localization, matching-vertex walls, and full-prefix carry cells.
- [`docs/130-prime-power-universal-line-clean-blocker-bank.md`](docs/130-prime-power-universal-line-clean-blocker-bank.md) through [`docs/132-prime-power-exact-band-covering.md`](docs/132-prime-power-exact-band-covering.md): universal sharp-blocker banks, deep-token universe elimination, tunable batching, and exact completion of one intermediate-height band.
- [`docs/133-prime-power-coarse-reset-reintroduction-profile.md`](docs/133-prime-power-coarse-reset-reintroduction-profile.md): exact coarse-reset host churn, one-pass \(O_p(t\log^2t)\) token-return mass, and reset-multiplicity reduction.
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
clone-space or conflict-free exact-selection theorem. Exact terminal traps show
that normalized local dynamics alone is insufficient; an escape must use
channel ancestry or a larger joint move.

### Composite prime-power route

Start from completed-reciprocal full channels and their companion layer. The
generic first-separation and prefix-collateral sums are closed at
quadratic-polylogarithmic scale. Balanced recursive banks exist for all
\(p\equiv1\pmod4\) and, through a non-reciprocal factorization, for every power
of seven.

Every globally nonimproving alternating closure contracts to an inherited
four-endpoint core. Parent lifting, Hall-wall peeling, and matching-space local
loads reduce the nonroot obstruction to candidate-only triples in primitive
height bands.

For a band

\[
H\le\max(|u|,|v|)<2H,
\]

the conflict degree is below \(3t^2\) and pair codegree is at most \(t/H\).
For every fixed \(\eta>0\), the duplicated-row Joos--Mubayi--Smith covering
model gives an **exact** target-specific parent permutation avoiding any one
band \(H\ge t^\eta\), for all sufficiently large \(t\). At the very top,

\[
H\ge0.42t,
\]

matching-space local-lemma arguments give exact cleaning with linear
protected-line reserves. The remaining intermediate-height problem is to
schedule all \(O(\log t)\) bands without accumulating a forbidden logarithmic
conflict degree or recreating previously cleaned bands.

Thin Hall blockers now have a complete local signature route. Universal
line-clean banks turn frozen blockers into line energy, matching-vertex walls,
heavy prefix cells, or dispersed tokens. Deep token universes can be removed in
simultaneous batches, with a tunable cubic-root tradeoff between heavy load and
batch capacity.

For a repeated absolute token \(\tau=(b,c,\theta)\), executable endpoint
deletions satisfy

\[
D_\tau\le \frac{t^2}{p^b}+I_\tau.
\]

A one-pass descending prefix schedule now has the explicit coarse-return bound

\[
I_\tau^{\rm coarse}\le\frac{2bt}{p^b},
\qquad
\sum_\tau I_\tau^{\rm coarse}
\le(p+1)t\,h(h-1).
\]

For arbitrary histories, unbounded return forces repeated rematching of one of
finitely many compatible ancestor slots. Witness certificates already open
executable prefix continuations. The remaining dynamic obstruction is repeated
ancestor-reset payment together with the width of fully forced exchange
ancestry and multi-band scheduling. Arbitrary composite assembly still needs a
separate coverage mechanism.

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
python scripts/verify_prime_power_parent_cover_lifting.py
python scripts/verify_prime_power_batch_parent_lifting.py
python scripts/verify_prime_power_envelope_expansion.py
python scripts/verify_prime_power_parent_line_signatures.py
python scripts/verify_prime_power_parent_hall_walls.py
python scripts/verify_prime_power_parent_wall_peeling.py
python scripts/verify_prime_power_iterated_hall_peeling.py
python scripts/verify_prime_power_essential_edges.py
python scripts/verify_prime_power_exchange_ancestry.py
python scripts/verify_prime_power_parent_local_load.py
python scripts/verify_prime_power_band_conflicts.py
python scripts/verify_prime_power_odd_line_resilience.py
python scripts/verify_prime_power_exact_top_slice.py
python scripts/verify_prime_power_heavy_cell_continuation.py
python scripts/verify_prime_power_dispersed_token_ledger.py
python scripts/verify_prime_power_token_reintroduction_ledger.py
python scripts/verify_prime_power_line_clean_energy.py
python scripts/verify_prime_power_line_energy_carry.py
python scripts/verify_prime_power_universal_line_clean.py
python scripts/verify_prime_power_dispersed_token_universe.py
python scripts/verify_prime_power_tunable_token_batching.py
python scripts/verify_prime_power_exact_band_covering.py
python scripts/verify_prime_power_coarse_reset_profile.py
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
