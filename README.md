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
- exact rank-at-most-three rectangle and multistate CSPs;
- signed Ramsey regularization and diffuse paid selection;
- cross-block and hierarchical state amplification beyond every original
  two-state rectangle signature.

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
`m^(2+o(1))`, so anchor-driven ownership failure reduces to a sublinear
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

## Cross-block and hierarchical endpoint

The two natural rectangle diagonals are not a terminal state space. Pair two
resource-disjoint rectangles and use only the two cross resource blocks. This
gives four equal-margin perfect-matching states and avoids every witness supported
only on the original rectangle diagonals.

Under sublinear non-designated unary endpoint degree:

- almost the entire rectangle bank pairs into source-safe four-state
  supervariables;
- each supervariable moves both designated owners and retains at least two
  removal-credit units;
- ternary bad boxes have vanishing density;
- fixed-colour Ramsey reduces every dense finite-state CSP to a constant valid
  state or a bounded local contradiction;
- diffuse unary/binary state cost and diffuse residual matching cost give a
  strict paid improvement.

The construction iterates. A level-`b` block has `2b` resources on each side and
`b` designated credits. Pairing two level-`b` blocks gives `((2b)!)^2` cross
states. Direct recapture deletes at most `b` edges per directional `K_(2b,2b)`,
whereas at least `2b` deletions are required to destroy every perfect matching.
With unary maximum degree `d`, each block has at most `4d` bad partners,
independently of `b`.

Therefore every bounded-depth signed contradiction is bypassed under sparse
unary degree. The remaining sparse-unary object is a possible infinite-depth
hierarchy of locally feasible blocks whose paid cost stays concentrated at every
fixed level.

## Current remaining theorem

The all-`n` branch is reduced to:

1. converting an ownership Hall/slack core, two-sided threshold gap, or the
   simultaneous score concentration surviving all four allocation interfaces;
2. converting a Hall rectangle or matchable but non-superregular zero-unary host
   outside the superregular recapture branch;
3. converting a unary endpoint resource with linear forbidden cross-block degree;
4. converting locally impossible hierarchical state sets or unary, binary, and
   residual weighted shadow concentrated at block-credit scale;
5. ruling out or converting an infinite-depth feasible cross-block hierarchy for
   which no fixed level has diffuse paid completion;
6. converting a linear-congestion original binary-shadow dual packing or
   witness-line pencil;
7. constructing source-admissible pool-compatible trades whose excess-shadow
   insertion cost is below their star/resource removal credit.

The no-three-in-line conjecture remains unproved.

## Recent proof chapters

- `docs/78`--`docs/101`: slab allocation, controller-aware external closure,
  endpoint trades, Hall rectangles, and dynamic excess shadow.
- `docs/102`--`docs/117`: binary congestion, rich-line energy and barriers,
  ownership Hall/slack, four allocation interfaces, near-uniform source validity,
  and incidence localization.
- `docs/118`--`docs/130`: anchor-energy localization, rectangle extraction,
  exact installation, superregular residual completion, signed Ramsey reduction,
  support cleaning, and paid residual matching.
- `docs/131`--`docs/135`: cross-block supervariables, sparse-unary host
  regularization, multistate Ramsey completion, universal signature bypass, and
  hierarchical amplification.

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
