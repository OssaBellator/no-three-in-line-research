# No-Three-in-Line Research Notebook

A rigorous research notebook for attempts toward the classical conjecture

\[
D(n)=2n,
\]

where `D(n)` is the maximum number of points in an `n x n` integer grid with no
three collinear.

> **Status:** The conjecture remains open as of 25 July 2026. This repository
> does not contain a complete proof. It records proved lemmas, conditional
> reductions, failed pathways, finite checks, and explicit next targets.

## Start here

- [`STATUS.md`](STATUS.md): current honesty ledger.
- [`tracks/all-n-prime-patching.md`](tracks/all-n-prime-patching.md): all-`n`
  prime-patching roadmap.
- [`proofs/prime-patching-recent-index.md`](proofs/prime-patching-recent-index.md):
  active PP3 theorem frontier.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): repository-wide theorem
  classification.
- [`docs/12-failed-claims-ledger.md`](docs/12-failed-claims-ledger.md): corrected
  and refuted statements.

Every mathematical statement is labelled **PROVED**, **PROVED UNDER
HYPOTHESES**, **CONDITIONAL**, **HEURISTIC**, or **REFUTED**.

## All-n prime-patching route

The branch `research/all-n-prime-patching` uses the slab-optimal square-root-macro
architecture

```text
macro variables M = m^(1/20+o(1))   = m^0.05
source-pool size R = m^(19/20+o(1)) = m^0.95
macro width W     = m^(19/40+o(1))  = m^0.475
total width T=MW  = m^(21/40+o(1))  = m^0.525.
```

The branch proves:

- universal matching-pool supply and exact degree restoration;
- internally no-three square-root macros and fixed-rank spread;
- exponent optimality within disjoint `O(sqrt(R))` macro architectures;
- saturation-compatible use of every final numerical label;
- controller-aware source safety against the full active source;
- `o(1)` weighted mass for all remaining external pair/triple classes;
- blocker-star or resource-bank structure from positive controller shadow;
- source-valid endpoint trades after adaptive thinning;
- exact zero-unary Hall rectangles and support-core localization;
- binary-shadow congestion covers and exact LP duals;
- a pairing-invariant excess-shadow potential for dynamic pool trades;
- controller-defect Ore scores and four global label-allocation interfaces;
- exact capacitated ownership Hall cores and refill-slack obstructions;
- rich-line energy reduction to one common nonaxis carrier.

## Four allocation interfaces

The controller-defect scores support four independent ways to use every final
movement and refill label.

1. **One-sided bottleneck/slack:** balanced movement ownership completes when
   its minimum bottleneck is at most every refill label's cumulative local slack.
2. **Deterministic two-sided ownership:** assign `W` labels of each type to every
   macro; local Ore completes when the two global nondegree thresholds satisfy
   `r+s<=W`.
3. **Random two-sided ownership:** per-macro complementary degree with slack
   `m^(23/80+o(1))` gives local perfect matchings after two balanced random
   partitions.
4. **Random one-sided ownership:** the earlier average-refill complementary-degree
   theorem remains available with the smaller `sqrt(T log T)` ownership loss.

At threshold `r`, movement ownership is possible exactly when

\[
W|N_M(X)|\ge|X|
\]

for every numerical-label set `X`. Failure returns an explicit all-bad
label-by-macro rectangle. Sparse exceptional macro-label pairs are therefore
routable rather than terminal.

## Hall, binary, and rich-line endpoints

All unary recapture and insertion-shadow cells are removed from a source-safe
endpoint graph `G_0`. Failure of a perfect matching is exactly a forbidden Hall
rectangle

\[
|X|+|Y|>q,
\qquad
X\times Y\subseteq E(\overline{G_0}).
\]

Binary conflicts can be converted into unary deletions. Their correct cost is
minimum endpoint-resource congestion, not raw conflict count. The fractional
congestion problem has factor-two rounding and an exact weighted dual.

A linear bank of linear-rich distinct witness lines cannot be solved by deleting
all but one cell on every trace. Adaptive thinning instead produces a fully
source-valid derangement with one-cell probabilities `(1+o(1))/q` while
preserving a dense Hall target core.

The owner-line potential then either strictly decreases or the incidence system
is near extremal. Szemerédi--Trotter converts the latter case into one nonaxis
geometric line carrying

\[
\Omega(q^{1/3})
\]

resource-disjoint owner/replacement endpoint cells and their candidate points.

## Current remaining theorem

The all-`n` branch is reduced to:

1. converting an ownership Hall/slack core, two-sided threshold gap, or the
   simultaneous score concentration surviving all four allocation interfaces;
2. converting a Hall rectangle or matchable but non-superregular zero-unary host
   outside the recapture-line case;
3. converting the common nonaxis line matching produced by the rich-line chain;
4. converting a linear-congestion binary dual packing or witness-line pencil;
5. constructing source-admissible pool-compatible trades whose excess-shadow
   insertion cost is below their star/resource removal credit.

The no-three-in-line conjecture remains unproved.

## Recent proof chapters

- `docs/78`--`docs/89`: complementary allocation, slab-optimal exponents,
  external-energy closure, controller-aware domains, structural extraction,
  endpoint trades, and termination.
- `docs/90`--`docs/101`: source-valid endpoint regularization, Hall rectangles,
  support cores, source-star correction, and dynamic excess shadow.
- `docs/102`--`docs/107`: binary congestion covers, rich-line energy,
  survivor-congestion barriers, controller-defect Ore scores, and diffuse-shadow
  allocation.
- `docs/108`--`docs/113`: exceptional-label routing, exact ownership Hall cores,
  two-sided ownership, bottleneck/refill slack, random local Ore, and global
  defect-mass slack.
- `docs/114`--`docs/117`: mass-sensitive derangement energy, adaptive near-uniform
  source validity, incidence multiplicity, and dense-Hall-core thinning.

## Running current checks

The scripts require Python 3.10+ and use only the standard library.

```bash
python scripts/verify_no_three_certificate.py \
  certificates/prime-patching-small.json

python scripts/check_global_label_ore.py \
  experiments/global-label-ore-example.json

python scripts/check_binary_shadow_cover.py \
  experiments/binary-shadow-cover-example.json

python scripts/check_rich_line_energy.py \
  experiments/rich-line-energy-example.json

python scripts/check_witness_line_survivors.py \
  experiments/witness-line-survivor-example.json

python scripts/check_controller_defect_ore.py \
  experiments/controller-defect-ore-example.json

python scripts/check_exceptional_label_ownership.py \
  experiments/exceptional-label-ownership-example.json

python scripts/check_exceptional_label_ownership.py \
  experiments/exceptional-label-ownership-hall-example.json

python scripts/check_two_sided_label_ownership.py \
  experiments/two-sided-label-ownership-example.json
```

These are exact finite checks or diagnostics. They are not asymptotic proofs
without the accompanying classification theorems.
