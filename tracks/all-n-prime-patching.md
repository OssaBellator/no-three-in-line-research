# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This track assumes saturated no-three configurations are eventually available at
prime-minus-one sides and asks for an exact row-column-preserving patch from side
`m` to side `m+t`. The patch must add `2t` net points, leave exactly two points in
every old and new row and column, and create no collinear triple.

The active theorem ledger is
[`proofs/prime-patching-recent-index.md`](../proofs/prime-patching-recent-index.md),
with the fixed-centre transition addendum in
[`proofs/prime-patching-transition-index.md`](../proofs/prime-patching-transition-index.md).

## PP1 — Degree interface

### Status: PROVED

Boundary and arbitrary-reservoir degree states are classified. Matching-edge
deletions and movement/refill insertions restore exact old and new row/column
margins.

## PP2 — Selection interfaces

### Status: PROVED AS IMPLICATIONS

The branch contains clone-space local lemmas, exact permutation laws,
superregular matching distributions, finite-state CSPs, alternating-component
factorization, cross-block amplification, weighted first moments, and
local-lemma selection. The unresolved work is structured geometric and paid
conversion.

## PP3 — Robust seed preparation

### Status: OPEN, reduced to explicit concentration cores

## 1. Slab-optimal architecture

```text
macro count M = m^(1/20+o(1))
pool size   R = m^(19/20+o(1))
macro width W = m^(19/40+o(1))
total width T = MW = m^(21/40+o(1)).
```

This balance is optimal among the disjoint source-pool architectures developed in
the notebook. Balanced label maps restore saturation, and product-space local
lemmas give internally no-three macros with fixed-rank spread.

## 2. Controller-aware safety and external closure

Unselected matching-pool edges remain in the source. Controller-aware domains
therefore test every blocker against the full active source.

At the slab-optimal exponents, patch-only cross-macro energy and ordinary
two-slot source-anchor energy are `o(1)`. Any saturation-compatible
controller-aware label allocation gives an `Omega(m^0.525)` patch.

## 3. Dynamic excess potential

Every candidate cell has one automatic axis blocker containing its controller.
The pairing-invariant excess potential

$$
\Xi(S)=\sum_z(b_S(z)-1)
$$

counts additional nonaxis blockers. Pool-compatible endpoint trades preserve the
candidate universe and satisfy an exact insertion-cost-minus-removal-credit
identity. Uniform strict improvement terminates automatically.

## 4. Four global allocation interfaces

The controller-defect scores support four independent completion mechanisms:

1. one-sided movement ownership versus cumulative refill slack;
2. deterministic two-sided ownership with `r+s<=W`;
3. random two-sided local Ore allocation;
4. random one-sided average-refill complementary degree.

Same-slot anchor mass is `m^(2+o(1))`. At the PP3of threshold, the acceptable
ownership host has deficiency

```text
D_anc=O(m^(1/2-zeta+o(1)))=o(T).
```

## 5. Canonical weighted anchor deficiency

Dulmage alternating reachability confines all necessary threshold violations to
one canonical all-bad label-by-slot cut of deficiency `d<=D_anc`.

For a nonnegative `d by d` completion matrix of total actual anchor weight `E`,
the entries of weight at most `E/d` contain a perfect matching. Thus movement and
refill cores have exact bottlenecks

```text
U_cap=max(u,E_U/d_U),
V_cap=max(u,E_V/d_V).
```

If these increments fit every macro's controller-degree slack, local bipartite
Ore completes all macro matchings. Remaining direct failure is:

- a nonpositive controller denominator;
- insufficient baseline local Ore slack;
- or weighted anchor energy per necessary crossing large enough to consume the
  slack.

## 6. Hall and rectangle extraction

After deleting direct recapture and residual unary-shadow cells, endpoint matching
failure is an exact Hall rectangle.

A recapture-dominated Hall core yields a positive-density family of target-rich
nonaxis lines. Their owner/replacement and Hall-target traces supply
`Omega(q^3)` alternating rectangle candidates, and a four-resource matching
extracts an `Omega(q)` row/column-disjoint rectangle bank.

Rectangle extraction is closed.

## 7. Superregular installation and cross-block amplification

For a small linear rectangle bank in a superregular endpoint host:

- the residual host has a perfect matching;
- the residual matching may be chosen source-valid and low-cost;
- all remaining geometry is an exact rank-at-most-three finite-state CSP;
- insertion shadow is an exact unary/binary state cost.

Cross-block states bypass every obstruction supported only on the original two
rectangle diagonals. Equitable colouring and recapture pruning absorb every
zero-density hard-unary support. At secondary exponent `kappa<1/60`, global
source-pair and triple terms vanish even after chromatic scaling. The global
rectangle branch remains only under chromatically concentrated unary or binary
controller-shadow weight.

## 8. Positive-density unary support

Dense hard-unary rectangle support produces a fixed endpoint resource with many
forbidden cross cells. Their retained-source witness pairs give either:

1. a source-star centre carrying polynomial removal credit;
2. a resource-disjoint credited endpoint bank;
3. paid collateral or source-host failure preventing the corresponding trade.

Raw support density is no longer terminal.

## 9. Matchable non-superregular hosts

Fix a perfect matching and orient every allowed index edge `i -> j`. Perfect
matchings factor exactly over the strongly connected components.

- Trivial components are forced edges with canonical tight Hall cuts.
- Bounded flexible credited components are paid finite-state banks.
- Maximum mobility gives resource-disjoint alternating-cycle banks.
- Low mobility gives a feedback hub, a one-hub cycle-star, or a two-hub theta
  support core.

Unbounded SCC size itself is no longer an obstruction. Remaining failure is a
fixed-spine/distinct-signature support concentration or source/shadow cost at the
cycle-credit scale.

## 10. Binary dual packing and price cores

Binary shadow is governed by minimum endpoint-resource cover congestion. A linear
dual value has `Omega(q)` supported conflicts and yields either:

- a resource-disjoint alternating-rectangle bank;
- a unary-forbidden matching on unsafe opposite diagonals;
- or an `O(sqrt(q))` high-price endpoint-resource core carrying `Omega(q)` dual
  mass.

Diffuse fractional dual mass is closed.

## 11. Conditional binary resource stars

A perfect matching selects exactly one cell at a fixed endpoint resource. Hence a
binary resource star is an exact conditional family: fix the centre cell `a`,
delete only its partner fibre `P(a)`, and match the residual host.

In a superregular host:

- subquadratic star support gives a fibre of size `o(q)` and completes;
- failed centres yield explicit conditional Hall rectangles;
- linearly many failed centres give a cubic binary core or a repeated secondary
  resource;
- a repeated secondary resource is a two-choice forbidden matrix;
- failure of this matrix forces a complete quadratic two-resource choice grid.

## 12. Paid two-resource choice grids

For every compatible local pair `s=(a,b)`, delete its four used resources and
choose a spread residual perfect matching. Averaging the local pair and residual
matching together gives strict improvement whenever

```text
average local blocker multiplicity
+ average residual collateral
< combined removal credit.
```

Thus a complete support grid with one blocker per state is harmless whenever the
move has more than unit combined credit.

Persistent failure forces a quadratic weighted grid at the credit scale. For a
fixed controller candidate, the local states it blocks form a matching between
the two choice sets, so weighted failure also requires a candidate-rich
projective cover, a rich candidate matching, residual concentration, or a
non-superregular conditional host.

## 13. Marked filler dilution inside one controller pool

A credited resource bank inside one pool has size

```text
H=m^(19/40+o(1)),
```

while the full controller pool has size

```text
N=m^(19/20+o(1)).
```

Force one credited endpoint into a marked filler block of size
`b=m^(kappa+o(1))`, where `kappa<19/80`, and choose the other endpoints from the
full pool.

Summed marked-load estimates show that all but `o(H)` credited endpoints are
simultaneously light for support-rank-four anchored pairs, inserted triples of
support rank four through six, and anchored transitions.

For unary source obstruction, the marked expectation is

```text
O(d_U(c)/N+theta b).
```

Choose `b` adaptively so `theta b->0`. If one credited endpoint has
`d_U(c)=o(N)`, it is unary-light. If none does, Hall extracts an `Omega(H)`
unary-forbidden resource matching.

## 14. Universal single-cycle marked states

On the selected `b` endpoint indices, choose one uniform directed Hamilton cycle
and use its successor map as the endpoint permutation.

For every prescribed compatible rank-`r` arc forest,

```text
Pr(F subseteq pi)=1/(b-1)_r,
```

while every proper directed cycle has probability zero. Hence the state:

- moves every selected endpoint;
- has no diagonal arc;
- has no transposition;
- has no directed triangle;
- supplies the fixed-rank spread law without superregular preparation.

Combining this exact law with marked dilution gives a fully source-valid state
through every source-light credited endpoint. The prepared-spread-host hypothesis
is removed.

## 15. Reduced marked and unmarked Xi weights

The single-cycle state kills rank-one unary `Xi` weight and rank-two binary
transposition weight identically. The remaining marked loads are

```text
M_A^cyc(c)=O(D_A,2(c)/N),
```

```text
M_B^cyc(c)=O(D_B,3(c)/N^2+D_B,4(c)b/N^3).
```

The remaining unmarked terms are

```text
U_A^cyc=O(A_2b/N^2),
```

```text
U_B^cyc=O(B_3b/N^3+B_4b^2/N^4).
```

If the summed marked load is `o(H)` and the unmarked load is `o(1)`, almost every
credited endpoint supports a source-valid strict `Xi` decrease.

## 16. Fixed captive-centre certificates

A predetermined captive star centre can remain exceptional even when almost every
resource-bank endpoint is good. Under the single-cycle state law, failure forces
one of nine explicit support cores:

- unary source degree;
- transition degree;
- anchored-pair degree;
- rank-four, rank-five, or rank-six triple degree;
- rank-two unary `Xi` weight;
- rank-three or rank-four binary `Xi` weight.

Rank-one unary state cost and rank-two binary transposition cost are no longer
frontiers.

## 17. Transition sunflower conversion

The transition-degree core is now reduced by `docs/167`--`docs/170`.

- The middle transition relation has size `o(N^2)`.
- Either a support-ranked clean-chain average gives a paid completion, or the
  outer role becomes a bounded-choice near-complete star.
- The role-star contains `Omega(N)` witness petals that share only the fixed
  centre and are otherwise disjoint in endpoint and source resources.
- Pigeonholing the two source layers and the `M+1` free/controller-pool classes
  gives a free or one-pool credited endpoint bank of size

```text
Omega(N/M)=m^(9/10-o(1)).
```

This contains the target bank size `W=m^(19/40+o(1))`. A transition sunflower is
therefore no longer an independent support frontier: it rejoins the existing paid
source-star/resource-bank conversion branch. The remaining transition-specific
failure is weighted source or `Xi` concentration on the clean-chain bank.

The finite layer/pool bookkeeping is checked by
`scripts/check_transition_sunflower_bank.py`.

## 18. Current exact bottleneck

The missing conversion theorem is reduced to:

1. controller denominator failure, insufficient local Ore slack, or weighted
   anchor energy in one canonical ownership core;
2. paid conversion of source-star/resource banks produced by unary support,
   forced Hall cuts, and fixed-centre transition sunflowers;
3. chromatically concentrated unary or binary controller-shadow weight in the
   global rectangle branch;
4. marked endpoint `Xi`-load cores, full-pool `Xi` thresholds, weighted
   clean-chain concentration, or one of eight nontransition fixed-centre support
   cores;
5. alternating cycle-star/theta support cores or cost comparable with cycle
   credit;
6. quadratic binary cell fans, weighted two-resource choice grids,
   candidate-rich projective covers, conditional Hall families, or residual paid
   collateral.

A successful conversion gives the allocation directly or strictly decreases a
nonnegative integer potential.

The branch does not prove the no-three-in-line conjecture.

## PP4 — Prime-gap transfer

### Status: PROVED UNDER PP2--PP3

A fixed positive constant times `m^0.525` patch width covers the published
backward prime-gap scale with standard constant and rounding slack.

## PP5 — Finite exceptions

### Status: VERIFIER COMPLETE; STORED CERTIFICATES CHECKED FOR `2<=n<=10`

The eventual threshold and finite exception list depend on the missing PP3
conversion theorem.
