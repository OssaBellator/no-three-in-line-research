# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This branch is independent of the other all-`n` strategies. It assumes a
saturated no-three-in-line theorem is eventually proved on `(p-1)x(p-1)` grids
for all sufficiently large primes `p`, and asks how to extend such a
construction to nearby side lengths.

Prime-gap information alone is not sufficient: embedding a `2m`-point solution
into an `n x n` grid leaves `2(n-m)` missing points. The essential theorem is an
exact extension absorber.

Detailed statements and proofs are in:

- [`docs/27-all-n-prime-patching.md`](../docs/27-all-n-prime-patching.md);
- [`docs/28-one-strip-and-pair-aware-patching.md`](../docs/28-one-strip-and-pair-aware-patching.md);
- [`docs/29-general-reservoir-patching.md`](../docs/29-general-reservoir-patching.md).

Small exact computations are recorded in:

- [`experiments/prime-patching-small.md`](../experiments/prime-patching-small.md);
- [`experiments/general-reservoir-loads.md`](../experiments/general-reservoir-loads.md).

## PP1 — Boundary extension interface

### Status: PROVED for saturation; geometry separated into PP2

The row-column bookkeeping is now exact:

- for `t>=2`, two edge-disjoint permutation graphs on the new `t x t` corner
  add exactly `2t` points without changing the old core;
- for `t=1`, every boundary-only degree state is one of exactly two forms:
  a one-point corner splice or a two-edge strip switch;
- the complete `t=1` list has only `2m^2-m` forced candidates;
- geometric validity is exactly the avoidance of old-pair secants,
  old-anchor/new-pair triples, and internal new-point triples.

## PP2 — Secant-shadow patching lemma

### Status: OPEN, with exact host and bank endpoints

There should be functions `w(m)` and `f(t)` such that, whenever `t<=w(m)`, one
can choose or prepare a reservoir in `S_m` that supports an exact
row-column-preserving completion without creating any triple.

The following parts are now proved:

- secants through any external point form a matching on the old configuration;
- a one-strip patch is valid exactly when its one- or two-point deletion set
  covers every inserted-point blocker matching and every mixed inserted pair
  avoids retained old anchors;
- for a wider corner, a pair-aware clone-space local lemma gives an exact
  sufficient inequality in the maximum omitted-cell, old-anchor-pair, and
  internal-triple loads;
- the clone-space theorem now applies to arbitrary deleted reservoirs, including
  old-old replacement cells and mixed old/new cells;
- for active clone size `N>=200`, the bounds
  `u_*<=N/200`, `pi_*<=N^2/1600`, and `tau_*<=N^3/3200` suffice;
- failure under this endpoint forces one of those three local loads to be large;
- alternatively, an internally no-three completion bank succeeds whenever its
  cell and pair spread make the total retained-core certificate expectation
  less than one.

The exact selection step is therefore closed in two forms:

1. prepare a candidate host satisfying the cell/pair/triple local-load bounds;
2. prepare an internally no-three spread bank satisfying the external
   cell/pair expectation bound.

The missing work is the geometric preparation theorem producing one of these
inputs for a useful width.

## PP3 — Robust seed preparation

### Status: OPEN; naive one-strip recursion REFUTED

A prepared reservoir should have low old-pair shadow, low old-anchor pair load,
controlled internal direction families, interchangeable row-column states, and
compatibility with a variable deletion budget.

Finite exhaustive results show why this cannot be omitted:

- among all labeled saturated no-three states, only `1/2` at `n=3`, `4/11` at
  `n=4`, and `9/32` at `n=5` admit a boundary-only one-strip extension;
- branching over every one-strip state from the unique `n=2` seed reaches
  `2` states at `n=3`, `1` at `n=4`, and none at `n=5`;
- every stored certificate with `3<=n<=10` is boundary-only one-strip blocked;
- unrestricted interior replacement nevertheless extends the stored chain
  through `n=10`;
- every stored seed has all `2n` noncorner future boundary cells on an old
  secant, so the strong one-strip averaging criterion fails immediately.

Thus a universal repetition of the two one-strip moves is refuted. Wider
boundary ladders, distributed absorbers, internally clean spread banks, and
interior tomographic trades remain viable.

## PP4 — Prime-gap transfer theorem

### Status: PROVED UNDER PP2–PP3

Let `P` be a set of solved side lengths. If every sufficiently large `n` has
some `m in P` with

\[
0\le n-m\le w(m),
\]

then the prepared-seed extension theorem implies `D(n)=2n` for every
sufficiently large `n`.

For `P={p-1:p prime}`, a short-interval theorem placing a prime in
`[x-x^theta,x]` is matched by any proved width `w(m)>=C m^theta` with fixed
`C>1`. Consequently:

- the published Baker–Harman–Pintz exponent `theta=0.525` requires
  `w(m)>=C m^0.525`, or more simply `m^(0.525+epsilon)`;
- Runbo Li's arXiv preprint claims `theta=0.52`, which may be used only as a
  preprint input;
- a merely polylogarithmic width does not currently give an unconditional
  all-`n` transfer.

No prime-gap input completes this branch while PP2 and PP3 remain open.

## PP5 — Finite exceptions

### Status: VERIFIER COMPLETE; CERTIFICATES VERIFIED FOR `2<=n<=10`

`scripts/verify_no_three_certificate.py` checks machine-readable coordinates
using exact integer determinants, exact bounds, distinctness, point count, and
two points in every row and column. The current certificate corpus covers
`n=2,...,10`.

The missing PP5 work is the eventual threshold and the complete certificate set
below it.

## Computational tools

- `scripts/search_boundary_extension.py`: general prescribed-degree extension
  CSP with explicit `found`, `exhausted`, and `cutoff` outcomes;
- `scripts/analyze_one_strip_extensions.py`: complete `t=1` boundary-only
  analyzer using the two-state classification;
- `scripts/analyze_one_strip_seed_loads.py`: exact PP3b averaging profiler;
- `scripts/enumerate_one_strip_seeds.py`: exhaustive labeled seed graph for
  small sides;
- `scripts/analyze_corner_patch_loads.py`: exact wider-corner cell/pair/triple
  load profiler;
- `scripts/analyze_reservoir_patch_loads.py`: exact arbitrary-deficit clone and
  coordinate load profiler;
- `scripts/analyze_patch_bank.py`: finite internally clean bank verifier and
  cell/pair spread analyzer;
- `scripts/verify_no_three_certificate.py`: exact finite certificate verifier.

## Candidate absorber designs still viable

- boundary ladders spanning several new rows and columns;
- subgroup-coset blocks reserved across several outer strips;
- Hall-type completion after structured shadow cleaning;
- internally no-three spread banks on prepared reservoir states;
- tomographic trades that free selected old rows and columns before extension;
- distributed reservoirs designed during the prime-grid repair process.

## Completion criterion

This branch is complete only when PP2 and PP3 provide an exact extension width
large enough for PP4, followed by a verified PP5 certificate set for the
remaining side lengths. The current branch closes PP1, arbitrary-reservoir and
spread-bank PP2 endpoints, the logical and prime-gap parts of PP4, and finite
verification machinery; it does not prove the no-three-in-line conjecture.
