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
- [`docs/11-open-bottlenecks.md`](docs/11-open-bottlenecks.md): live research roadmap.
- [`proofs/composite-modulus-theorem-index.md`](proofs/composite-modulus-theorem-index.md): composite-track theorem index.
- [`proofs/composite-modulus-theorem-index-addendum.md`](proofs/composite-modulus-theorem-index-addendum.md): CMR102--CMR384.
- [`proofs/composite-modulus-theorem-index-live.md`](proofs/composite-modulus-theorem-index-live.md): authoritative collision-free range from CMR385 onward.
- [`proofs/composite-modulus-theorem-index-supplement.md`](proofs/composite-modulus-theorem-index-supplement.md): mirrored live range.
- [`tracks/all-n-composite-modulus.md`](tracks/all-n-composite-modulus.md): original composite task track.
- [`tracks/all-n-composite-modulus-progress.md`](tracks/all-n-composite-modulus-progress.md): CM1--CM6 progress and bottlenecks.

### General repair programme

- [`docs/01-saturation-and-reservoirs.md`](docs/01-saturation-and-reservoirs.md) through [`docs/26-alternating-star-neutralization.md`](docs/26-alternating-star-neutralization.md): saturation, repair banks, hyperbola interleaving, inverse-additive structure, carry cells, and alternating neutralization.
- [`docs/12-failed-claims-ledger.md`](docs/12-failed-claims-ledger.md): corrected and refuted claims.

### Composite and prime-power programme

- [`docs/27-composite-modulus-obstructions.md`](docs/27-composite-modulus-obstructions.md) through [`docs/59-prime-power-binary-cluster-sum.md`](docs/59-prime-power-binary-cluster-sum.md): nonlinear prime-power channels, recursive banks, CRT obstructions, divisor collisions, and first-separation summation.
- [`docs/60-prime-power-prefix-star-neutralization.md`](docs/60-prime-power-prefix-star-neutralization.md) through [`docs/88-prime-power-inherited-four-core-cover.md`](docs/88-prime-power-inherited-four-core-cover.md): prefix repair, quotient charging, alternating closure, terminal traps, joint-parent banks, and inherited covers.
- [`docs/89-prime-power-parent-cover-lifting.md`](docs/89-prime-power-parent-cover-lifting.md) through [`docs/113-prime-power-mod-six-height-cleaning.md`](docs/113-prime-power-mod-six-height-cleaning.md): parent lifting, Hall-wall peeling, exchange ancestry, matching-space loads, and exact high-slice cleaning.
- [`docs/114-prime-power-thin-blocker-cover-expansion.md`](docs/114-prime-power-thin-blocker-cover-expansion.md) through [`docs/132-prime-power-exact-band-covering.md`](docs/132-prime-power-exact-band-covering.md): thin blocker signatures, carry cells, line-clean banks, token batching, and exact completion of one intermediate-height band.
- [`docs/133-prime-power-laminar-reintroduction-budget.md`](docs/133-prime-power-laminar-reintroduction-budget.md) through [`docs/139-prime-power-state-cycle-erasure.md`](docs/139-prime-power-state-cycle-erasure.md): laminar and recursive return profiles, harmonic packet completion, nonprefix reset costs, and exact state-cycle erasure.
- [`docs/140-prime-power-edge-incidence-state-expansion.md`](docs/140-prime-power-edge-incidence-state-expansion.md): exact labelled edge incidence, sharp \(O_p(t\log^2t)\) sweep budgets, and polynomial payment for distinct-state expansion.
- [`docs/141-prime-power-packet-recreation-churn-ledger.md`](docs/141-prime-power-packet-recreation-churn-ledger.md): entering-edge support for recreated packet conflicts, equality with leaving-edge churn, and first-dirty scheduling.
- [`docs/142-prime-power-packet-loss-deletion-ancestry.md`](docs/142-prime-power-packet-loss-deletion-ancestry.md): deletion-or-forced-ancestry response for lossy packet resets, the `t(t-1)` deletion budget, and conditional ancestry-width closure.
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
channel ancestry or a larger inherited move.

### Composite prime-power route

The generic recursive first moment, prefix and joint-parent collateral, terminal
contraction, Hall-blocker geometry, universal line-clean repair, exact high-slice
cleaning, and harmonic-packet completion are closed at their stated scales.

For every fixed \(\eta>0\), all relevant intermediate dyadic bands partition
into

\[
P_\eta(t)
\le
\left\lceil\frac{1+\log_2t}{2}\right\rceil
\]

exactly cleanable harmonic packets.

For a full token \(\tau=(b,a,c,\theta)\),

\[
D_\tau^{(2)}
\le
\frac{t^2}{p^{2b}}+I_\tau^{(2)}.
\]

One recursive ancestor or one one-layer whole-parent reset returns at most
\(t/p^b\) token edges. Exact edge-incidence accounting gives

\[
\text{one prefix pass}
\le
(p+1)t h(h-1)
\]

and

\[
\text{prefix pass + packet sweep}
\le
(p+1)t(h-1)\bigl(h+P_\eta(t)\bigr)
=O_p(t\log^2t).
\]

Exact selected-state cycles are erasable. Distinct feasible parent states differ
on at least two entering and two leaving edges, so state-space expansion pays
edge incidence linearly.

A selected conflict recreated under `M -> M'` contains an entering edge of
`M'\setminus M`. The leaving set `M\setminus M'`, returned to the complementary
available host, has equal cardinality; this is the churn quantity used in the
aggregate bounds.

Inside one certificate-directed deletion pass, every lossy packet reset either

1. deletes a nonessential edge of a recreated triple while preserving a perfect
   matching; or
2. exposes a fully forced rank-three certificate with backward CMR217 exchange
   ancestry.

Deletion responses occur at most \(t(t-1)\) times. If `P` is the packet count,
`F` the number of fully forced packet events, and `T` the installation count,

\[
T\le P\bigl(1+t(t-1)+F\bigr).
\]

An incoming ancestry-width bound `w` gives

\[
T\le P\bigl(1+(1+w)t(t-1)\bigr).
\]

The live prime-power frontier is therefore quantitative control or simultaneous
resampling of fully forced exchange ancestry, together with a corresponding
payment for repeated local ancestor resets. Arbitrary side-length coverage
remains necessary afterward.

## Running checks

The scripts require Python 3.10+ and use the standard library unless a search
script explicitly documents an optional solver.

```bash
python scripts/verify_composite_modulus.py --max-modulus 40
python scripts/verify_prime_power_channels.py --max-modulus 125
python scripts/verify_prime_power_first_separation_sum.py --max-modulus 125
python scripts/verify_prime_power_quotient_excess.py
python scripts/verify_prime_power_global_baseline_closure.py
python scripts/verify_prime_power_parent_cover_lifting.py
python scripts/verify_prime_power_exchange_ancestry.py
python scripts/verify_prime_power_band_conflicts.py
python scripts/verify_prime_power_exact_top_slice.py
python scripts/verify_prime_power_line_clean_energy.py
python scripts/verify_prime_power_line_energy_carry.py
python scripts/verify_prime_power_line_energy_tokens.py
python scripts/verify_prime_power_exact_band_covering.py
python scripts/verify_prime_power_harmonic_band_packing.py
python scripts/verify_prime_power_laminar_reintroduction.py
python scripts/verify_prime_power_coarse_reset_profile.py
python scripts/verify_prime_power_full_token_reintroduction.py
python scripts/verify_prime_power_full_token_reset_profile.py
python scripts/verify_prime_power_nonprefix_token_return.py
python scripts/verify_prime_power_harmonic_packet_sweep.py
python scripts/verify_prime_power_state_cycle_erasure.py
python scripts/verify_prime_power_edge_incidence_state_expansion.py
python scripts/verify_prime_power_packet_recreation_churn.py
python scripts/verify_prime_power_packet_loss_ancestry.py
python scripts/verify_prime_power_balanced_law_classification.py
python scripts/verify_prime_seven_balanced_bank.py
python scripts/verify_prime_seven_pair_spectrum.py
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
