# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This track assumes saturated no-three configurations are eventually available at
prime-minus-one sides and asks for an exact row-column-preserving patch from side
`m` to side `m+t`. The patch must add `2t` net points, leave exactly two points in
every old and new row and column, and create no collinear triple.

The active theorem ledger is
[`proofs/prime-patching-recent-index.md`](../proofs/prime-patching-recent-index.md).

## PP1 — Degree interface

### Status: PROVED

Boundary and arbitrary-reservoir degree states are classified. Matching-edge
deletions and movement/refill insertions restore exact old and new row/column
margins.

## PP2 — Selection interfaces

### Status: PROVED AS IMPLICATIONS

The branch contains clone-space local lemmas, permutation and superregular
matching distributions, exact finite-state CSPs, alternating-component
factorization, cross-block amplification, weighted first moments, and local-lemma
selection. The unresolved work is structured geometric and paid conversion.

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
\Xi(S)=\sum_z (b_S(z)-1)
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

The remaining binary geometry is a quadratic cell fan, complete choice grid,
conditional Hall family, or paid/source concentration.

## 12. Marked filler dilution inside one controller pool

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
simultaneously light for:

- support-rank-four anchored pairs;
- inserted triples of support rank four, five, and six;
- anchored transitions.

For unary source obstruction, the marked expectation is

```text
O(d_U(c)/N + theta b).
```

Choose `b` adaptively so `theta b->0`. If one credited endpoint has
`d_U(c)=o(N)`, the marked block is fully source-valid. If none does, Hall extracts
an `Omega(H)` unary-forbidden resource matching, returning to the source-star or
resource-bank trade branch.

Pool-local pair, triple, transition, and diffuse unary mass are therefore not
separate resource-bank obstructions.

## 13. Marked and unmarked Xi weights

Decompose unary Xi weight into endpoint-support ranks `A_1,A_2` and binary Xi
weight into `B_2,B_3,B_4`.

For a marked endpoint `c`, the exact paid loads are

```text
M_A(c)=K[D_A,1(c)/b + D_A,2(c)/N],
```

```text
M_B(c)=K^2[
 D_B,2(c)/(bN)
 + D_B,3(c)/N^2
 + D_B,4(c)b/N^3].
```

The corresponding unmarked terms are

```text
U_A=K[A_1/N+A_2b/N^2],
```

```text
U_B=K^2[B_2/N^2+B_3b/N^3+B_4b^2/N^4].
```

If the summed marked load is `o(H)` and the unmarked load is `o(1)`, almost every
credited endpoint supports a source-valid strict Xi decrease.

## 14. Fixed captive-centre certificates

A predetermined captive star centre can remain exceptional even when almost every
resource-bank endpoint is good. Its failure is now finite and quantitative.

Negating the marked paid first moment forces one of eleven explicit support cores:

- unary source degree;
- transition degree;
- anchored-pair degree;
- rank-four, rank-five, or rank-six triple degree;
- rank-one or rank-two unary Xi weight;
- rank-two, rank-three, or rank-four binary Xi weight.

The rank-one unary Xi term is local state cost; rank-two binary Xi is a two-index
transposition core; higher binary ranks re-enter the resource-star, conditional
Hall, and choice-grid reductions.

## 15. Current exact bottleneck

The missing conversion theorem is reduced to:

1. controller denominator failure, insufficient local Ore slack, or weighted
   anchor energy in one canonical ownership core;
2. paid conversion of source-star/resource banks produced by unary support and
   forced Hall cuts;
3. chromatically concentrated unary or binary controller-shadow weight in the
   global rectangle branch;
4. marked endpoint Xi-load cores, full-pool Xi thresholds, or one of the eleven
   fixed-centre support cores;
5. alternating cycle-star/theta support cores or cost comparable with cycle
   credit;
6. quadratic binary cell fans, complete two-resource choice grids, conditional
   Hall families, or paid collateral on their rectangle states.

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
