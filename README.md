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

For a rectangle bank of size `H`, let the non-designated unary endpoint support
have density `o(1)`. Deleting `o(H)` high-interaction rectangles leaves
sublinear interaction degree. Equitable colouring then partitions all but
`o(H)` rectangles into growing unary-independent groups. After pruning
recapture-heavy resources, the directional cross hosts are near-complete
superregular and have fixed-rank `O(b^-r)` spread.

At secondary exponent `kappa<1/60`, the chromatically scaled source-pair and
inserted-triple terms vanish automatically. The global ordinary rectangle branch
therefore reduces to the shadow-only quantities

```text
k*A = Omega(H^2)

or

k^2*B = Omega(H^3),
```

where `k` is the equitable-colouring count of the hard-unary rectangle
interaction graph.

## Pool-compatible dynamic trades

The same cross-block construction works inside one controller pool and preserves
the complete candidate-cell universe. It therefore satisfies the exact dynamic
identity

\[
\Xi(S')-\Xi(S)=\mathcal I_\Xi-\mathcal C_\Xi.
\]

Diffuse hard source support and diffuse pool-local pair, triple, unary-
`Xi`, and binary-`Xi` weights give a strict pool-compatible decrease. Unlike the
global rectangle branch, pool-local pair and triple masses remain explicit
hypotheses; they are not automatically closed by the global `kappa<1/60`
argument.

## Matchable non-superregular hosts

Fix any perfect matching and orient each allowed matching-index edge `i -> j`.
Every alternative perfect matching factors over the strongly connected
components of this alternating digraph.

- Nontrivial components are exact disjoint finite-state variables. Their
  no-three constraints have rank at most three and their insertion cost has rank
  at most two.
- A trivial component is exactly a forced reference edge.
- Every forced edge is the private edge of a Hall-tight set.
- Its forward and backward reachability closures give canonical completely
  forbidden cuts.

Bounded credited flexible components form paid finite-state banks with one
guaranteed credit per component. Dense binary component interactions Ramsey-
regularize to a constant state or a bounded signed contradiction. Forced edges
are not a new diffuse graph obstruction: they mark a hard-unary Hall rectangle,
a small endpoint cluster, or a small complementary capacity core.

## Current remaining theorem

The all-`n` branch is reduced to:

1. converting an ownership Hall/slack core, two-sided threshold gap, or the
   simultaneous score concentration surviving all four allocation interfaces;
2. converting positive-density hard-unary support and its Hall/line/resource
   cores, including canonical forced-edge cuts;
3. converting chromatically concentrated unary or binary controller-shadow
   weight at scales `H^2/k` and `H^3/k^2` in the global rectangle branch;
4. converting pool-local pair/triple mass or unary/binary `Xi` weight at the same
   chromatic scales, including captive-star collateral;
5. converting unbounded alternating SCCs or concentrated bounded-component
   geometry and cost;
6. converting a linear-congestion original binary-shadow dual packing or
   witness-line pencil.

The no-three-in-line conjecture remains unproved.

## Recent proof chapters

- `docs/78`--`docs/117`: slab allocation, controller-aware external closure,
  ownership interfaces, endpoint trades, Hall/congestion endpoints, source-valid
  thinning, and incidence localization.
- `docs/118`--`docs/142`: anchor-energy localization, rectangle extraction,
  cross-block amplification, equitable-colour paid selection, chromatic source
  closure, and dynamic-`Xi` block trades.
- `docs/143`--`docs/146`: alternating-SCC factorization, forced-edge tight Hall
  certificates, canonical reachability cuts, and bounded-component paid banks.

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

python scripts/check_alternating_scc_decomposition.py \
  experiments/alternating-scc-example.json
```

These are exact finite checks or diagnostics. They are not asymptotic proofs
without the accompanying classification theorems.
