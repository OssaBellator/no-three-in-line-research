# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This branch is independent of the other all-`n` strategies. It assumes a
saturated no-three-in-line theorem is eventually proved on `(p-1)x(p-1)` grids
for all sufficiently large primes `p`, and asks how to extend such a
construction to nearby side lengths.

Prime-gap information alone is not sufficient: embedding a `2m`-point solution
into an `n x n` grid leaves `2(n-m)` missing points. The essential theorem is an
exact extension absorber.

Detailed statements and proofs are in
[`docs/27-all-n-prime-patching.md`](../docs/27-all-n-prime-patching.md).
Small exact computations are recorded in
[`experiments/prime-patching-small.md`](../experiments/prime-patching-small.md).

## PP1 — Boundary extension interface

### Status: PROVED for saturation; geometry separated into PP2

Let `S_m` be a saturated no-three-in-line configuration on `[m]^2`. For
`t>=1`, define the enlarged grid `[m+t]^2`.

The row-column bookkeeping is now exact:

- for `t>=2`, any two edge-disjoint permutation graphs on the new `t x t`
  corner add exactly `2t` points without changing the old core;
- for `t=1`, deleting one old point `(x,y)` and inserting
  `(x,m+1)`, `(m+1,y)`, and `(m+1,m+1)` adds two points and preserves every
  row and column degree;
- a proposed patch is geometrically valid exactly when it avoids old-pair
  secants, old-anchor/new-pair triples, and internal new-point triples.

The last three conflict classes are the PP2 problem, not part of the solved
saturation interface.

## PP2 — Secant-shadow patching lemma

### Status: OPEN

There should be functions `w(m)` and `f(t)` such that, whenever `t<=w(m)`, one
can choose or prepare a reservoir in `S_m` with the following property:

- delete at most `f(t)` reservoir blocks;
- insert a row-column-preserving completion involving the `t` new rows and
  `t` new columns;
- create no collinear triple with retained old points;
- internally avoid all triples among new and replacement points.

The desired width should be at least polylogarithmic in `m`; an `m^theta` width
would also be useful if matched by a proven prime-gap theorem.

A finite warning is now explicit: for the recorded `n=3` seed, the exact
boundary-only `3 -> 4` search is exhausted through deletion budget four, while
an unrestricted two-deletion patch succeeds using an interior replacement
cell. This refutes that naive boundary-only model for that seed, not PP2 in
general.

## PP3 — Robust seed preparation

### Status: OPEN

Prove that the prime-minus-one construction can be chosen with a boundary or
distributed absorber reservoir satisfying PP2, rather than as an arbitrary
saturated configuration. The reservoir should have:

- low secant shadow into future rows and columns;
- many interchangeable row-column states;
- bounded interaction with the core construction;
- compatibility with deleting a variable number `t` of blocks.

This may require reserving rows and columns before the main prime-grid repair
process.

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

Once PP4 covers all `n>=n_0`, provide exact constructions or certified
computational solutions for every `n<n_0` not already covered.

`scripts/verify_no_three_certificate.py` checks machine-readable coordinate
files using exact integer determinants, exact bounds, distinctness, point count,
and two points in every row and column. The file
[`certificates/prime-patching-small.json`](../certificates/prime-patching-small.json)
contains verified saturated no-three-in-line configurations for every
`n=2,...,10`.

The missing PP5 work is the eventual threshold and the complete certificate set
below it; the current finite set is a regression corpus and genuine partial
coverage, not a closure of PP5.

## Computational falsification

`scripts/search_boundary_extension.py` exhaustively searches small patches with
a chosen deletion budget. It distinguishes:

- `found`, with a complete coordinate certificate;
- `exhausted`, a genuine negative result within the stated search model;
- `cutoff`, an explicitly inconclusive resource limit.

The `--boundary-only` mode can be compared with unrestricted replacement to
search for cores requiring interior changes. The exact `n=2` through `n=10`
chain and the finite exhausted searches are recorded in the experiment note.

## Candidate absorber designs

- boundary ladders using alternating cycles in the row-column graph;
- subgroup-coset blocks reserved across several outer strips;
- recursive two-row/two-column extension gadgets;
- Hall-type completion in a near-complete new-row/new-column host;
- tomographic trades that free selected old rows and columns before extension.

## Completion criterion

This branch is complete only when PP2 and PP3 provide an exact extension width
large enough for PP4, followed by a verified PP5 certificate set for the
remaining side lengths. The current branch closes PP1, the logical and
prime-gap parts of PP4, the PP5 verification machinery, and the cases
`2<=n<=10`; it does not prove the no-three-in-line conjecture.
