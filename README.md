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
- [`tracks/all-n-composite-modulus.md`](tracks/all-n-composite-modulus.md): original composite task track.
- [`tracks/all-n-composite-modulus-progress.md`](tracks/all-n-composite-modulus-progress.md): current CM1–CM6 progress and bottlenecks.

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
- [`docs/53-prime-power-divisor-collision-energy.md`](docs/53-prime-power-divisor-collision-energy.md) through [`docs/56-prime-power-cross-stratum-sum.md`](docs/56-prime-power-cross-stratum-sum.md): divisor-collision reduction, critical cells, singular sums, and the unconditional \(O(N^2\log N)\) one-channel syndrome.
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
clone-space or superregular exact-selection theorem. The principal missing
step is a global second-generation concentration or termination theorem.

### Composite prime-power route

Start from completed-reciprocal full channels and their companion layer. Use
the recursive all-stratum fibre bank and all-prime conic terminal family.
Deterministic one- and two-layer syndromes are now \(O(N^2\log N)\) for fixed
prime base, and recursive marginals have expected harmonic energy
\(O(N\log^3N)\). The principal missing step is a global first-separation
decoder that converts local `O(1/p)` anti-concentration into an exact no-three
state. Arbitrary composite assembly additionally requires CRT slope-carry
incompatibility or absorption.

## Running checks

The scripts require Python 3.10+ and use the standard library unless a search
script explicitly documents an optional solver.

```bash
python scripts/verify_composite_modulus.py --max-modulus 40
python scripts/verify_prime_power_channels.py --max-modulus 125
python scripts/verify_prime_power_global_energy.py
python scripts/verify_prime_power_companion_global.py
python scripts/verify_prime_power_restricted_bank.py
python scripts/verify_prime_power_recursive_harmonic.py --samples 100
python scripts/verify_prime_power_cross_stratum_sum.py --max-modulus 125
python scripts/verify_crt_slope_carry.py
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
