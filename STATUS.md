# Status and honesty ledger

**Last updated:** 25 July 2026

## External status

The classical no-three-in-line conjecture

$$
D(n)=2n
$$

remains open. This repository does **not** contain a complete proof.

The notebook contains proved lemmas, conditional endpoints, failed claims,
finite diagnostics, and explicit remaining conversion problems. None of the
reductions below should be read as a proof of the conjecture.

## Established platform

The repository has proved or imported exact interfaces for:

- saturated two-per-row/column decomposition into two perfect-matching layers;
- clone-space, permutation, superregular, and alternating-component matching;
- protected rectangle, tomographic, cycle, endpoint, and cross-block trades;
- binary and multistate rank-at-most-three forbidden-box CSPs;
- weighted local-lemma and fixed-rank spread selection;
- Hall, divisor, incidence, Ramsey, and congestion reductions;
- exact finite certificate and regression checking.

The principal non-prime-patching route remains incomplete and still lacks its
second-generation alternating-bank conversion and final carry absorber.

## All-n prime-patching architecture

```text
macro variables M = m^(1/20+o(1))
pool size R       = m^(19/20+o(1))
macro width W     = m^(19/40+o(1))
total width MW    = m^(21/40+o(1)).
```

Matching supply, exact degree restoration, internal macro geometry, fixed-rank
spread, and exponent optimality are proved. Controller-aware domains test
blockers against the full active source. Patch-only cross-macro energy and
ordinary two-slot source-anchor energy are closed.

Any saturation-compatible controller-aware global allocation gives an
`Omega(m^0.525)` patch.

## Direct allocation

Four independent global mechanisms remain available:

1. one-sided movement ownership versus cumulative refill slack;
2. deterministic two-sided ownership with `r+s<=W`;
3. random two-sided local Ore allocation;
4. random one-sided average-refill complementary degree.

Same-slot anchor failure has maximum deficiency

```text
D_anc=O(m^(1/2-zeta+o(1)))=o(T).
```

Dulmage reachability confines every necessary threshold violation to one all-bad
cut. A `d by d` completion matrix of total actual anchor weight `E` has a perfect
completion using only entries at most `E/d`.

Thus the direct route completes if the movement/refill core bottlenecks fit every
macro's controller-degree slack. Remaining direct failure is:

- a nonpositive controller denominator;
- insufficient baseline local Ore slack;
- or anchor energy per necessary core crossing large enough to consume that
  slack.

Diffuse Hall deficiency and scattered exceptional labels are no longer open.

## Hall, rectangle, and ordinary paid branches

After deleting direct recapture and unary-shadow cells, endpoint matching failure
is an exact Hall rectangle.

A recapture-dominated Hall core yields target-rich repeated nonaxis lines,
`Omega(q^3)` alternating rectangle candidates, and an `Omega(q)` pairwise
row/column-disjoint rectangle bank.

In the superregular branch:

- residual perfect matching is closed;
- residual source validity is closed;
- finite-state rectangle installation is exact;
- diffuse paid collateral is closed;
- bounded signed CSP contradictions are bypassed by cross-block amplification.

At secondary exponent `kappa<1/60`, global source-pair and triple terms vanish
even after chromatic scaling. The remaining global rectangle obstruction is
chromatically concentrated unary or binary controller-shadow weight.

## Positive-density and marked unary support

Positive-density hard-unary rectangle support gives one endpoint resource with
many forbidden cross cells. Their retained-source witness pairs yield either:

- a source-star centre;
- or a resource-disjoint credited endpoint bank.

Inside one controller pool, marked filler dilution gives a sharper alternative.
If a credited endpoint has full-pool unary degree `o(N)`, it can be placed in a
source-valid growing filler block. If no credited endpoint is unary-light, then
`Omega(H)` distinct tied resources each have linear unary degree, and Hall extracts
an `Omega(H)` unary-forbidden resource matching.

Raw unary density is therefore not terminal. The unresolved issue is paid
conversion of the resulting star/resource structures.

## Binary dual packings, conditional stars, and paid grids

Binary shadow is governed by minimum endpoint-resource cover congestion. A
linear dual value has support on `Omega(q)` conflicts and yields either:

- a resource-disjoint conflict rectangle bank;
- an unsafe opposite-diagonal unary matching;
- or a small high-price endpoint core carrying `Omega(q)` dual mass.

A weighted resource star is reduced by conditioning on the unique centre cell
selected by a perfect matching.

- A subquadratic star has a sparse partner fibre and completes in a superregular
  host.
- Failed centres return conditional Hall rectangles.
- Linearly many failures yield a cubic binary core or a repeated secondary
  resource.
- A repeated secondary resource becomes a two-choice forbidden matrix.
- Superregular failure forces a complete quadratic two-resource choice grid.

A complete support grid is not itself a paid obstruction. Jointly averaging the
local pair and its residual matching closes the grid whenever average binary
multiplicity plus residual collateral is below the combined removal credit.
Failure forces a quadratic weighted grid, a candidate-rich projective matching
cover, residual concentration, or a non-superregular conditional host.

## Matchable non-superregular hosts

Relative to a fixed perfect matching, allowed edges define an alternating digraph.
Perfect matchings factor over its strongly connected components.

- Forced edges give canonical tight Hall cuts.
- Bounded flexible credited components are paid finite-state banks.
- Maximum mobility gives resource-disjoint alternating-cycle banks.
- Low mobility gives a feedback hub, a cycle-star bank, or a two-hub theta core.

The unresolved component objects are fixed-spine/distinct-signature support cores
or source/shadow cost comparable with cycle credit. Unbounded SCC size itself is
not open.

## Dynamic excess potential and single-cycle fillers

The dynamic potential is

```text
Xi(S)=sum_z (b_S(z)-1).
```

Pool-compatible endpoint permutations preserve the candidate-cell universe and
satisfy an exact insertion-cost-minus-removal-credit identity. Uniform strict
improvement terminates automatically.

For a credited bank of size

```text
H=m^(19/40+o(1))
```

inside a full controller pool of size

```text
N=m^(19/20+o(1)),
```

force one credited endpoint into a filler block of size `b=m^kappa`, with
`kappa<19/80`.

All but `o(H)` credited endpoints are simultaneously light for support-rank-four
anchored pairs, inserted triples of support rank four through six, and anchored
transitions. Adaptive filler size also removes diffuse unary support. Hence a
large resource bank has no independent pool-local source-pair, triple,
transition, or diffuse unary obstruction.

The filler state may be chosen as a uniform single-cycle permutation. Exact
counting gives cylinder probability `1/(b-1)_r` for directed path forests and zero
for every proper directed cycle. It moves every selected endpoint and
identically removes:

- diagonal arcs;
- transpositions;
- directed triangles.

No separately prepared spread host is required in this branch.

The support-ranked `Xi` expression therefore has no rank-one unary term and no
rank-two binary transposition term. The remaining marked loads are rank-two unary
and rank-three/rank-four binary weights.

The transition core is reduced to a linear disjoint-petal sunflower and then to
a free or one-pool credited endpoint bank of size at least `W`. Diffuse
noncentral collateral averages away across its petals.

The fixed-centre rank-two unary core first gives a cheap clean centre segment or
a near-complete incoming/outgoing heavy arc star. That star is already a
fixed-centre one-arc petal bank. Dyadic pigeonholing gives a `W`-sized
comparable-cost subbank, and bounded-support averaging closes diffuse noncentral
collateral. Failure is centre-core or local arc cost at the credit scale, residual
source/host structure, or global unary weight `A_2=Omega(R_*W)`.

The full-pool unary table also has a support conversion. Truncating at
`tau R_*/(4b)` gives a paid marked cycle avoiding all heavy arcs unless one
endpoint has `Omega(N/b)` heavy incident arcs. This is larger than `W` and returns
to the same arc-petal branch.

Rank-three binary `Xi` patterns are directed two-arc paths. Their middle role is
a paid two-resource choice grid. Dense heavy outer support yields a `W`-sized
comparable-cost path-petal bank disjoint outside the centre. Rank-four patterns
reduce through conditioned support avoidance and robust Hall localization to a
paid host, an alternating-component residual host, or a repeated
secondary-resource star feeding the conditional Hall/grid chain.

Full-pool binary truncation removes the remaining aggregate tables as independent
frontiers. Failure of heavy-pattern avoidance forces a fixed-centre rank-three
support degree

```text
Omega(N^2/b)
```

or a fixed-centre rank-four support degree

```text
Omega(N^3/b^2).
```

These rejoin the rank-three and rank-four localization chains.

Thus fixed-axis unary stars, unstructured full-pool `A_2`, `B_3`, and `B_4`
thresholds, weighted rank-three middle rectangles, small-core heavy rank-three
outer families, fixed rank-four multiplicity cores, fixed-cell remote matchings,
and square-root partner stars are no longer independent obstructions.

## What remains conditional

The missing conversion theorem has these structured forms.

1. Convert controller denominator failure, insufficient local Ore slack, or
   weighted anchor energy concentrated in one canonical ownership core.
2. Pay source-star/resource-bank and fixed-centre arc/path-petal trades produced by
   unary support, forced Hall cuts, transitions, and marked `Xi` localization.
3. Convert chromatically concentrated unary or binary controller-shadow weight
   in the global rectangle branch.
4. Convert centre-core/local-credit concentration or the remaining fixed-centre
   source/weight cores.
5. Convert alternating cycle-star/theta support cores or cost at the cycle-credit
   scale.
6. Convert quadratic binary cell fans, weighted two-resource choice grids,
   candidate-rich projective covers, conditional Hall families, or residual paid
   collateral.

## Important cautions

- Unused numerical labels cannot be discarded while preserving saturation.
- Fixed-core domains do not handle unselected active-pool edges.
- The canonical anchor bound controls same-slot anchor weight, not all controller
  defects.
- The single-cycle marked-filler theorem applies to a large credited resource
  bank; one predetermined centre may remain exceptional.
- Moving one selected transition witness removes that certificate incidence but
  need not clear every witness of the same forbidden transition.
- Cheap conditioned centre arcs or chains isolate only their displayed
  deterministic `Xi` terms; residual source and paid terms must still fit the
  relevant completion criterion.
- The reduced support-ranked `Xi` theorem is conditional on its displayed weight
  bounds.
- The robust rank-four Hall theorem localizes matchability failure; it does not
  pay residual source or non-rank-four insertion cost.
- The arc/path-petal theorems close diffuse noncentral collateral but not
  centre-core weight or local cost already at the removal-credit scale.
- The full-pool truncation theorems are conservative heavy-pattern avoidance
  reductions; their hard branches still require the cited fixed-centre
  conversions.
- Finite diagnostics verify identities and examples, not asymptotic conversion.

## Bottom line

There is no complete proof. The branch closes matching supply, optimal macro
width, four allocation interfaces, external weighted geometry, rectangle
extraction, superregular and non-superregular state decompositions, canonical
weighted anchor deficiency, conditional resource stars, diffuse pool-local source
mass, universal marked single-cycle spread, low-rank cyclic `Xi` terms, diffuse
binary dual mass, transition-sunflower localization to credited endpoint banks,
rank-two unary arc-petal localization, rank-three middle/outer localization,
rank-four support localization through robust Hall, and full-pool unary/binary
truncation to fixed-centre cores.

The concentrated local-Ore, paid star/resource/petal, global-shadow,
centre-core/local-credit, cycle-support, and weighted binary-grid cores above
remain open.
