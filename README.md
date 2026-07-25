# No-Three-in-Line Research Notebook

A rigorous research notebook for attempts toward the classical conjecture

$$
D(n)=2n,
$$

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
closure, exact Hall/congestion endpoints, endpoint-trade potentials, and
source-valid near-uniform endpoint permutations.

## Direct allocation and canonical anchor cores

Four independent allocation mechanisms remain available:

1. one-sided ownership bottleneck versus cumulative refill slack;
2. deterministic two-sided ownership with `r+s<=W`;
3. random two-sided local Ore allocation;
4. random one-sided average-refill complementary degree.

Same-slot divisor energy now gives more than Hall-set localization. At the PP3of
threshold, the acceptable ownership host has deficiency

```text
D_anc = O(m^(1/2-zeta+o(1))) = o(T).
```

A maximum acceptable ownership leaves only `D_anc` unmatched labels and slots.
Dulmage alternating reachability confines all necessary violations to one
completely unacceptable cut

```text
X x (slots outside N(X)).
```

For a `d by d` completion matrix of total actual anchor weight `E`, the entries
of weight at most `E/d` already contain a perfect matching. Thus the movement and
refill cores have exact bottlenecks `E_U/d_U` and `E_V/d_V`.

If those bottleneck increments fit inside every macro's baseline controller Ore
slack, all local owned-label graphs have perfect matchings and the global patch
completes. Failure is now a controller denominator, insufficient baseline slack,
or weighted anchor energy per necessary core crossing.

## Hall, line, rectangle, and cross-block endpoint

After deleting direct recapture and residual unary-shadow cells, failure of the
source-safe endpoint graph is exactly a Hall rectangle. Binary conflicts are
governed by minimum endpoint-resource congestion, whose fractional cover problem
has factor-two rounding and an exact weighted dual.

A recapture-dominated Hall core survives adaptive source-valid thinning. Failed
owner-line improvement gives target-rich repeated nonaxis lines, `Omega(q^3)`
alternating rectangle candidates, and an `Omega(q)` row/column-disjoint rectangle
bank.

The two natural rectangle diagonals are not a terminal state space. Cross-block
states, equitable colouring, recapture pruning, and superregular spread matching
absorb every zero-density hard-unary support and every bounded signed rectangle
CSP obstruction.

At secondary exponent `kappa<1/60`, the global ordinary rectangle branch has
automatic chromatic source validity and reduces to chromatically concentrated
unary or binary shadow weight.

## Positive-density hard unary support

A dense hard-unary rectangle-interaction graph gives one endpoint resource with
linearly many forbidden cross cells. Their retained-source witness pairs satisfy
a second star/matching dichotomy:

- one source point witnesses many cells, giving free or dynamic star credit;
- or a large vertex-disjoint witness matching yields a resource-disjoint credited
  endpoint bank.

Thus raw positive-density unary support rejoins the existing star/resource trade
problem. The remaining issue is paid insertion collateral or failure of the
source-admissible trade host.

## Matchable non-superregular hosts

Fix any perfect matching and orient each allowed matching-index edge `i -> j`.
Every alternative perfect matching factors exactly over the strongly connected
components of this alternating digraph.

- Trivial components are forced edges and have canonical tight Hall cuts.
- Bounded flexible credited components are paid finite-state banks.
- In a fully credited large component, maximum mobility is the maximum number of
  vertices covered by disjoint directed cycles.

A maximum-mobility matching gives a resource-disjoint binary alternating-cycle
bank. If its moved set is small, that set is a directed feedback hub meeting every
alternating cycle. One hub then lies on many cycles, and vertex-capacitated max
flow gives either:

- a large one-hub multistate cycle-star bank; or
- a two-hub core with many theta cycles.

The two-hub family decomposes into forward/return path signatures. It gives a
fixed-spine bank, a distinct-signature state bank, or an inserted cell/pair/triple
shared by many cycle states. Unbounded SCC size itself is no longer the open
parameter.

## Binary dual price cores

A linear binary-congestion dual packing has total weight `Omega(q)`. Every
individual conflict weight is at most one, so its support contains `Omega(q)`
conflicts.

The resource-disjoint part yields alternating conflict rectangles. Safe opposite
diagonals feed the existing rectangle machinery; unsafe opposite cells form a
unary resource matching.

Using the dual prices more sharply gives either:

- an `Omega(sqrt(q))` resource-disjoint conflict matching; or
- an `O(sqrt(q))` high-price endpoint-resource core carrying `Omega(q)` dual
  weight, including one resource with `Omega(sqrt(q))` incident dual mass.

Diffuse fractional dual mass is therefore closed.

## Pool-compatible dynamic trades

Cross-block states also work inside one controller pool and preserve the complete
candidate-cell universe, so they satisfy the exact dynamic identity

$$
Xi(S')-Xi(S)=I_Xi-C_Xi.
$$

Diffuse pool-local source mass and diffuse unary/binary `Xi` weights give a
strict decrease. Pool-local pair and triple masses remain explicit hypotheses;
the global `kappa<1/60` closure cannot be imported automatically after
pigeonholing to one pool.

## Current remaining theorem

The all-`n` branch is reduced to:

1. converting controller denominator failure, insufficient baseline Ore slack,
   or weighted anchor energy concentrated in one canonical ownership core;
2. paying the star/resource trades produced by positive-density hard unary
   support and forced tight Hall cuts;
3. converting chromatically concentrated unary or binary controller-shadow
   weight in the global rectangle branch;
4. converting pool-local pair/triple mass or unary/binary `Xi` weight, including
   captive-star collateral;
5. converting alternating cycle-star/theta support cores or concentrated
   source-invalid and insertion-shadow mass relative to cycle credit;
6. converting the high-price binary resource core, weighted resource star, or
   paid collateral on the extracted conflict-rectangle bank.

The no-three-in-line conjecture remains unproved.

## Recent proof chapters

- `docs/78`--`docs/117`: slab allocation, controller-aware external closure,
  ownership interfaces, endpoint trades, Hall/congestion endpoints, source-valid
  thinning, and incidence localization.
- `docs/118`--`docs/142`: anchor-energy localization, rectangle extraction,
  cross-block amplification, chromatic paid selection, source closure, and
  dynamic-`Xi` block trades.
- `docs/143`--`docs/149`: alternating-SCC factorization, forced-edge Hall cuts,
  bounded component banks, maximum mobility, cycle stars, and theta states.
- `docs/150`--`docs/156`: canonical weighted anchor deficiency cores, core-aware
  Ore completion, dense hard-unary star/resource localization, and binary dual
  rectangle/price-core reductions.

## Running current checks

The scripts require Python 3.10+ and use only the standard library.

```bash
python scripts/verify_no_three_certificate.py \
  certificates/prime-patching-small.json

python scripts/check_cross_block_supervariable.py \
  experiments/cross-block-supervariable-example.json

python scripts/check_alternating_scc_decomposition.py \
  experiments/alternating-scc-example.json

python scripts/check_alternating_mobility.py \
  experiments/alternating-mobility-star-example.json

python scripts/check_anchor_deficiency_core.py \
  experiments/anchor-deficiency-core-example.json
```

These are exact finite checks or diagnostics. They are not asymptotic proofs
without the accompanying classification theorems.