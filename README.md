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
- source-valid endpoint trades after adaptive near-uniform thinning;
- exact zero-unary Hall rectangles and support-core localization;
- binary-shadow congestion covers and exact LP duals;
- a pairing-invariant excess-shadow potential for dynamic pool trades;
- four controller-aware global label-allocation interfaces;
- exact capacitated ownership Hall/slack cores;
- divisor-energy localization of same-slot anchor ownership failures;
- target-rich common-line families and linear alternating-rectangle banks;
- superregular residual matching and source-valid installation;
- exact rank-at-most-three rectangle CNFs and quadratic shadow costs;
- signed Ramsey regularization of dense binary rectangle interactions;
- diffuse paid rectangle selection and low-cost residual matching.

## Four allocation interfaces

The controller-defect scores support four independent ways to use every final
movement and refill label.

1. **One-sided bottleneck/slack:** balanced movement ownership completes when
   its minimum bottleneck is at most every refill label's cumulative local slack.
2. **Deterministic two-sided ownership:** assign `W` labels of each type to every
   macro; local Ore completes when `r+s<=W`.
3. **Random two-sided ownership:** per-macro complementary degree with slack
   `m^(23/80+o(1))` gives local perfect matchings after two balanced random
   partitions.
4. **Random one-sided ownership:** average-refill complementary degree remains
   available with the smaller `sqrt(T log T)` ownership loss.

At threshold `r`, movement ownership is possible exactly when

\[
W|N_M(X)|\ge|X|
\]

for every numerical-label set `X`. Failure returns an explicit all-bad
label-by-macro rectangle. The total same-slot anchor energy is only
`m^(2+o(1))`, so anchor-driven ownership failure reduces further to a sublinear
exceptional label cluster or a nearly dead macro column.

## Hall, line, and rectangle endpoint

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

A recapture-dominated Hall core survives adaptive source-valid thinning. Failed
owner-line improvement gives a positive-density family of target-rich repeated
nonaxis lines. Pairing the owner/replacement and Hall-target traces gives
`Omega(q^3)` alternating rectangles, from which `Omega(q)` pairwise
row/column-disjoint blocks are extracted.

## Superregular paid rectangle endpoint

In the superregular branch:

- a small linear rectangle reservation leaves a residual perfect matching;
- the residual matching can be chosen source-valid and low-cost;
- each rectangle is a two-state `2 by 2` permutation block;
- all remaining geometric conditions form an exact binary rank-at-most-three
  CNF;
- exact insertion shadow is a unary/binary pseudo-Boolean cost.

After unit preprocessing and ternary thinning, fixed-colour Ramsey gives a
growing homogeneous binary signature. Its paid capacity is exact:

- if `(1,1)` is allowed, the all-cross state is valid and directly protects one
  designated credit per rectangle;
- if `(1,1)` is forbidden but `(0,0)` is allowed, every valid homogeneous
  assignment has at most one cross-oriented rectangle;
- if both diagonal pairs are forbidden, three rectangles already form an
  unsatisfiable core.

Dense all-cross conflict is geometric: a rich cross line, a line pencil, or a
complete fixed-anchor secant design. Sparse unary/binary all-cross support and
weighted diffuse collateral contain a growing zero- or low-cost subbank.

## Current remaining theorem

The all-`n` branch is reduced to:

1. converting an ownership Hall/slack core, two-sided threshold gap, or the
   simultaneous score concentration surviving all four allocation interfaces;
2. converting a Hall rectangle or matchable but non-superregular zero-unary host
   outside the superregular recapture branch;
3. converting a credit-poor homogeneous rectangle signature, rich cross line or
   pencil, complete fixed-anchor secant design, or constant-size signed
   contradiction;
4. converting linear unary, quadratic binary, or residual weighted shadow
   concentration at rectangle-credit scale;
5. converting a linear-congestion original binary-shadow dual packing or
   witness-line pencil;
6. constructing source-admissible pool-compatible trades whose excess-shadow
   insertion cost is below their star/resource removal credit.

The no-three-in-line conjecture remains unproved.

## Recent proof chapters

- `docs/78`--`docs/89`: complementary allocation, slab-optimal exponents,
  external-energy closure, controller-aware domains, structural extraction,
  endpoint trades, and termination.
- `docs/90`--`docs/101`: source-valid endpoint regularization, Hall rectangles,
  support cores, source-star correction, and dynamic excess shadow.
- `docs/102`--`docs/113`: binary congestion, rich-line energy and barriers,
  controller-defect scores, exceptional-label routing, ownership Hall/slack, and
  four allocation interfaces.
- `docs/114`--`docs/117`: near-uniform source-valid derangements,
  Szemerédi--Trotter line-family localization, and dense-Hall-core thinning.
- `docs/118`--`docs/123`: anchor-energy Hall localization, common-line rectangle
  extraction, exact rectangle installation, superregular residual completion,
  paid selection, and clause-core regularization.
- `docs/124`--`docs/130`: signed Ramsey reduction, designated cross credit,
  cross-conflict line/pencil localization, homogeneous paid capacity, shadow
  support cleaning, and paid residual matching.

## Running current checks

The scripts require Python 3.10+ and use only the standard library.

```bash
python scripts/verify_no_three_certificate.py \
  certificates/prime-patching-small.json

python scripts/check_binary_shadow_cover.py \
  experiments/binary-shadow-cover-example.json

python scripts/check_rich_line_energy.py \
  experiments/rich-line-energy-example.json

python scripts/check_exceptional_label_ownership.py \
  experiments/exceptional-label-ownership-example.json

python scripts/check_two_sided_label_ownership.py \
  experiments/two-sided-label-ownership-example.json

python scripts/check_paid_rectangle_selection.py \
  experiments/paid-rectangle-selection-example.json

python scripts/check_homogeneous_binary_signature.py \
  experiments/homogeneous-binary-signature-example.json
```

These are exact finite checks or diagnostics. They are not asymptotic proofs
without the accompanying classification theorems.
