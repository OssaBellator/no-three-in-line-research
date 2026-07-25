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

The branch proves matching-pool supply, exact degree restoration, internally
no-three square-root macros, fixed-rank spread, exponent optimality, use of every
final numerical label, controller-aware source safety, external weighted-energy
closure, exact Hall and congestion endpoints, endpoint-trade potentials, and
source-valid near-uniform endpoint permutations.

## Four allocation interfaces

The controller-defect scores support four independent ways to use every final
movement and refill label.

1. **One-sided bottleneck/slack:** balanced movement ownership completes when
   its bottleneck is below every refill label's cumulative local slack.
2. **Deterministic two-sided ownership:** assign `W` labels of each type to every
   macro; local Ore completes when `r+s<=W`.
3. **Random two-sided ownership:** per-macro complementary degree with slack
   `m^(23/80+o(1))` gives local perfect matchings.
4. **Random one-sided ownership:** average-refill complementary degree remains
   available with the smaller `sqrt(T log T)` loss.

At threshold `r`, movement ownership is possible exactly when

\[
W|N_M(X)|\ge|X|
\]

for every numerical-label set `X`. Failure returns an explicit all-bad
label-by-macro rectangle. The total same-slot anchor energy is only
`m^(2+o(1))`, so anchor-driven ownership failure reduces to a sublinear
exceptional label cluster or a nearly dead macro column.

## Hall, line, and rectangle endpoint

After deleting direct recapture and residual unary-shadow cells, failure of the
source-safe endpoint graph is exactly a Hall rectangle

\[
|X|+|Y|>q,
\qquad
X\times Y\subseteq E(\overline{G_0}).
\]

Binary conflicts are governed by minimum endpoint-resource congestion. The
fractional cover problem has factor-two rounding and an exact weighted dual.

A recapture-dominated Hall core survives adaptive source-valid thinning. Failed
owner-line improvement gives a positive-density family of target-rich repeated
nonaxis lines. Their two matching traces supply `Omega(q^3)` alternating
rectangle candidates and an `Omega(q)` row/column-disjoint rectangle bank.

## Cross-block state amplification

The two natural rectangle diagonals are not a terminal state space. Pairing two
resource-disjoint rectangles and using only the two cross resource blocks gives
four equal-margin matching states. This bypasses every witness supported only on
the original line and cross diagonals.

The construction generalizes to level-`b` blocks. A level-`b` block has `2b`
resources per side and at least `b` designated credits. Pairing two such blocks
gives `((2b)!)^2` formal cross states. Direct recapture deletes fewer edges than
are required to destroy every perfect matching.

The stronger partition theorem removes the hierarchy's irregularity. If the
non-designated unary endpoint graph has maximum degree `d=o(H)`, colour the
rectangle-interaction graph, whose maximum degree is at most `4d`. Splitting its
independent colour classes into growing groups discards only `o(H)` rectangles.
Every group then has zero non-designated unary edges internally.

After deleting `o(b)` recapture-heavy rectangles from each group, both
directional cross hosts are near-complete superregular. Their product matching
law has fixed-rank probability `O(b^-r)`, and each block retains
`(1-o(1))b` designated credits.

Thus every sublinear unary-degree rectangle bank reduces directly to the paid
spread inequality

\[
K^2\frac{P_b}{b^2}
+
K^3\frac{Q_b}{b^3}
+
\frac1{R_b}
\left(
K\frac{A_b}{b}
+
K^2\frac{B_b}{b^2}
\right)
<1.
\]

Arbitrary signed rectangle signatures, dense finite-state CSPs, bounded local
contradictions, and infinite-depth hierarchy irregularity are no longer
separate obstructions in the sublinear-unary regime.

## Current remaining theorem

The all-`n` branch is reduced to:

1. converting an ownership Hall/slack core, two-sided threshold gap, or the
   simultaneous score concentration surviving all four allocation interfaces;
2. converting a Hall rectangle or matchable but non-superregular zero-unary host
   outside the superregular recapture branch;
3. converting a unary endpoint resource with linear forbidden cross-block degree;
4. converting source or shadow weights concentrated in the growing-block paid
   expression above;
5. converting a linear-congestion original binary-shadow dual packing or
   witness-line pencil;
6. constructing source-admissible pool-compatible trades whose excess-shadow
   insertion cost is below their star/resource removal credit.

The no-three-in-line conjecture remains unproved.

## Recent proof chapters

- `docs/78`--`docs/117`: slab allocation, controller-aware external closure,
  ownership interfaces, endpoint trades, Hall/congestion endpoints, source-valid
  thinning, and incidence localization.
- `docs/118`--`docs/130`: anchor-energy localization, rectangle extraction,
  exact installation, signed Ramsey reduction, support cleaning, and paid
  residual matching.
- `docs/131`--`docs/138`: cross-block supervariables, host regularization,
  multistate Ramsey completion, universal signature bypass, hierarchical and
  growing-depth amplification, and unary-independent superregular grouping.

## Running current checks

The scripts require Python 3.10+ and use only the standard library.

```bash
python scripts/verify_no_three_certificate.py \
  certificates/prime-patching-small.json

python scripts/check_paid_rectangle_selection.py \
  experiments/paid-rectangle-selection-example.json

python scripts/check_homogeneous_binary_signature.py \
  experiments/homogeneous-binary-signature-example.json

python scripts/check_cross_block_supervariable.py \
  experiments/cross-block-supervariable-example.json
```

These are exact finite checks or diagnostics. They are not asymptotic proofs
without the accompanying classification theorems.
