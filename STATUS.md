# Status and honesty ledger

**Last updated:** 25 July 2026

## External status

The classical no-three-in-line conjecture

$$
D(n)=2n
$$

remains open. This repository does **not** contain a complete proof.

A July 2026 result proves the corresponding eventual maximum `kn` for every
fixed `k>=3`; the saturated `k=2` case addressed here remains exceptional.

## Established platform

The notebook contains proved lemmas or exact conditional endpoints for:

- saturated two-per-row/column decomposition into two perfect-matching layers;
- clone-space, permutation, superregular, and alternating-component matching;
- protected rectangle, tomographic, cycle, subgroup, endpoint, and cross-block
  trades;
- binary and multistate rank-at-most-three forbidden-box CSPs;
- weighted local-lemma, fixed-rank spread, Ramsey, Hall, divisor, and incidence
  endpoints;
- exact finite certificate verification and small exhaustive diagnostics.

The principal non-prime-patching route still lacks its second-generation
alternating-bank concentration/termination theorem and final carry absorber.

## All-n prime-patching track

### Slab-optimal macro architecture

```text
macro variables M = m^(1/20+o(1))   = m^0.05
pool size R       = m^(19/20+o(1))  = m^0.95
macro width W     = m^(19/40+o(1))  = m^0.475
total width MW    = m^(21/40+o(1))  = m^0.525.
```

Matching supply, degree restoration, internal macro geometry, fixed-rank spread,
and exponent optimality are proved. Controller-aware domains test blockers
against the full active source. Every remaining patch-only cross-macro class and
ordinary two-slot source-anchor class has `o(1)` incident probability mass.

Any saturation-compatible controller-aware global allocation therefore gives an
`Omega(m^0.525)` patch.

### Dynamic excess potential

Every candidate has one automatic controller-containing axis blocker. The
pairing-invariant excess potential

$$
Xi(S)=sum_z (b_S(z)-1)
$$

counts additional nonaxis blockers. Pool-compatible endpoint trades satisfy an
exact insertion-cost-minus-removal-credit identity. Uniform improving trades
terminate automatically.

## Direct allocation: canonical weighted anchor cores

Four independent allocation interfaces remain available:

1. one-sided movement ownership versus cumulative refill slack;
2. deterministic two-sided ownership with `r+s<=W`;
3. random two-sided local Ore allocation;
4. random one-sided average-refill complementary degree.

Same-slot divisor energy gives a much sharper failure object. At the PP3of
threshold, the acceptable ownership host has maximum deficiency

```text
D_anc = O(m^(1/2-zeta+o(1))) = o(T).
```

A maximum acceptable matching leaves only `D_anc` unmatched labels and slots.
Dulmage alternating reachability confines all necessary threshold violations to
one completely unacceptable label-by-slot cut. For a `d by d` completion matrix
of total actual anchor weight `E`, the entries of weight at most `E/d` already
contain a perfect matching.

Thus movement and refill ownerships have explicit core bottlenecks `E_U/d_U` and
`E_V/d_V`. If those increments fit inside every macro's baseline controller Ore
slack, all local owned-label graphs have perfect matchings and the global patch
completes. Failure is now one of:

- a nonpositive controller denominator;
- insufficient baseline local Ore slack;
- slot-expanded anchor energy per necessary core crossing large enough to consume
  that slack.

A diffuse Hall deficiency, scattered exceptional assignments, and
middle-density anchor ownership failure are no longer open cases.

## Source-valid endpoint and rectangle branches

Adaptive endpoint thinning produces a growing bank with:

- no unary-invalid arc;
- no anchored transition;
- vanishing high-support source-invalid expectation;
- a fully source-valid derangement with one-cell probability `(1+o(1))/q`.

A recapture-dominated Hall core yields target-rich repeated lines,
`Omega(q^3)` alternating rectangle candidates, and an `Omega(q)` pairwise
row/column-disjoint rectangle bank.

In the superregular branch, residual matching, residual source validity, exact
rank-at-most-three finite-state geometry, and diffuse paid selection are closed.
Cross-block states and equitable colouring absorb every zero-density hard-unary
support and every bounded signed rectangle-CSP obstruction.

At secondary exponent `kappa<1/60`, the global ordinary rectangle branch has
automatic chromatic source validity. It remains only when unary or binary shadow
weight is concentrated at the chromatic credit scale.

## Positive-density hard unary support

Positive-density hard-unary rectangle support yields one endpoint resource with
linearly many forbidden cross cells. The retained-source witness pairs then give
one of:

1. a source-star centre clearing polynomially many unary witnesses when moved;
2. a polynomial vertex-disjoint witness matching, hence a resource-disjoint
   credited endpoint bank;
3. insertion collateral or source-host failure preventing the corresponding
   star/resource trade.

Raw positive-density support is therefore no longer terminal. It rejoins the
same paid star/resource conversion problem as controller shadow and forced Hall
cuts.

## Matchable non-superregular hosts

Relative to any perfect matching, orient every allowed matching-index edge
`i -> j`. Perfect matchings factor exactly over strongly connected components of
this alternating digraph.

- A trivial component is a forced matching edge. Its forward and backward
  reachability closures give canonical tight forbidden Hall cuts.
- Bounded flexible credited components are paid finite-state banks.
- In a fully credited large component, maximum mobility is the maximum number of
  vertices covered by vertex-disjoint directed cycles.

A maximum-mobility matching yields a resource-disjoint binary alternating-cycle
bank. If mobility is small, the moved set is a directed feedback hub meeting
every alternating cycle. Counting and vertex-capacitated max flow then produce:

- a one-hub multistate cycle-star bank;
- or a two-hub theta-cycle core.

The theta family decomposes into forward/return path signatures. Remaining
failure is a fixed-spine or distinct-signature support core, an inserted
cell/pair/triple shared by many states, or source/shadow cost comparable with the
cycle credit.

Unbounded SCC size and unstructured non-superregularity are no longer separate
open parameters.

## Binary dual packing and price cores

Binary shadow is governed by minimum endpoint-resource cover congestion. A
linear dual value has support on `Omega(q)` distinct conflicts because every
individual dual conflict weight is at most one.

A resource star/matching reduction gives either:

- a growing endpoint-resource star;
- a resource-disjoint family of binary conflicts, each defining an alternating
  rectangle;
- or a unary-forbidden resource matching on unsafe opposite rectangle cells.

Using dual prices more sharply gives either an `Omega(sqrt(q))`
resource-disjoint conflict matching or an `O(sqrt(q))` high-price endpoint core
carrying `Omega(q)` dual mass. One resource in that core carries
`Omega(sqrt(q))` incident dual weight.

Diffuse fractional dual mass is no longer an open case.

## Pool-compatible dynamic trades

Cross-block states work inside one controller pool and preserve the complete
candidate-cell universe. Diffuse hard-source support, pool-local pair/triple
mass, and unary/binary `Xi` weight give a strict dynamic decrease.

The global `kappa<1/60` source-mass closure cannot automatically be imported
after pigeonholing to one pool. Pool-local pair/triple quantities remain explicit
hypotheses and possible concentration certificates.

## What remains conditional

The remaining conversion theorem has these structured forms.

1. Convert controller denominator failure, insufficient baseline Ore slack, or
   weighted anchor energy concentrated in one canonical ownership core.
2. Pay the source-star or resource-bank trades produced by positive-density hard
   unary support and forced tight Hall cuts.
3. Convert chromatically concentrated unary or binary controller-shadow weight
   in the global rectangle branch.
4. Convert pool-local pair/triple mass or unary/binary `Xi` weight, including
   captive-star collateral.
5. Convert alternating cycle-star/theta support cores or concentrated
   source-invalid and insertion-shadow mass relative to cycle credit.
6. Convert the high-price binary resource core, its weighted resource star, or
   paid collateral on the extracted conflict-rectangle bank.

## Important cautions

- Unused numerical labels cannot be discarded and compressed while preserving
  saturation.
- Fixed-core domains do not handle unselected active-pool edges.
- The anchor-core bottleneck bounds actual same-slot anchor weight, not all
  controller defects.
- The mobility cycle-bank theorem currently uses a fully credited component;
  arbitrary partial credit requires weighted assignment bookkeeping.
- Pool-local source mass remains an explicit dynamic-trade hypothesis.
- Finite diagnostics validate identities and expose obstructions; they do not
  prove the asymptotic conversion theorem.

## Bottom line

There is no complete proof. The branch closes matching supply, optimal macro
width, four allocation interfaces, external weighted geometry, source-valid
near-uniform endpoint trades, rectangle extraction, superregular and
non-superregular state decompositions, canonical weighted anchor deficiency,
zero-density unary support, and diffuse binary dual mass. The concentrated
weighted star/resource, cycle-support, price-core, local-Ore, and dynamic-`Xi`
cases above remain open.