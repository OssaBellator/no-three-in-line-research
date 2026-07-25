# No-Three-in-Line Research Notebook

A rigorous research notebook for attempts toward the classical conjecture

\[
D(n)=2n,
\]

where `D(n)` is the maximum number of points in an `n x n` integer grid with no
three collinear.

> **Status:** The conjecture remains open as of 25 July 2026.  This repository
> does not contain a complete proof.  It records proved lemmas, conditional
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
- complementary-degree global allocation criteria;
- controller-aware source safety against the full active source;
- `o(1)` weighted mass for all remaining external pair/triple classes;
- blocker-star or resource-bank structure from positive controller shadow;
- source-valid endpoint trades after two-scale thinning;
- exact zero-unary Hall rectangles and support-core localization;
- binary-shadow congestion covers and exact LP duals;
- owner-line assignment energy and grid-rich pencil extraction;
- a pairing-invariant excess-shadow potential for dynamic pool trades;
- direct global allocation from explicit controller-defect Ore scores.

## Current direct endpoint

For macro movement/refill defect counts `a_i(A),b_i(B)` and same-slot anchor
counts `u_i(A,B)`, the branch defines normalized nondegree scores
`rho_i(A),kappa(B)`.

Global allocation follows when every incompatible triple satisfies

\[
\rho_i(A)+\kappa(B)
\le
T-8\sqrt{T\log T}.
\]

A fixed labelwise domain margin together with

```text
Xi_i=o(RT),
max_A U_i(A)=o(RT),
max_B average_i V_i(B)=o(RT)
```

already implies this condition.  Thus diffuse excess shadow is sufficient; a
direct failure must concentrate in a nearly dead label, one macro with
`Omega(RT)` excess shadow, or a same-slot anchor row/average-column.

## Current Hall and binary endpoint

All unary recapture and insertion-shadow cells are removed from a source-safe
endpoint graph `G_0`.  Failure of a perfect matching is exactly a forbidden Hall
rectangle

\[
|X|+|Y|>q,
\qquad
X\times Y\subseteq E(\overline{G_0}).
\]

Binary conflicts can be converted into unary deletions.  Their correct cost is
minimum endpoint-resource congestion, not raw conflict count.  The fractional
congestion problem has factor-two rounding and an exact weighted dual.

A single nonaxis witness line has a congestion-one cover.  However, a linear bank
of linear-rich distinct lines cannot be solved by deleting all but one cell on
each trace.  If

\[
S=\sum_\lambda(|P_\lambda|-1),
\]

then every such simple cover satisfies

\[
|C|
\ge
\frac{S^2}{S+r(r-1)}.
\]

Consequently a linear rich-line bank forces linear unary congestion.  It must be
handled by moving the owner lines, not by naive line-by-line deletion.

## Current remaining theorem

The all-`n` branch is reduced to:

1. regularising the five explicit direct-allocation concentrations;
2. converting a Hall rectangle or matchable but non-superregular zero-unary host;
3. converting the second-generation grid-rich owner-line pencil;
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
  line-supported covers, survivor-congestion barriers, controller-defect Ore
  scores, and diffuse-shadow direct allocation.

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
```

These are exact finite checks or diagnostics.  They are not asymptotic proofs
without the accompanying classification theorems.