# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This track assumes saturated no-three configurations are eventually available at
prime-minus-one sides and asks for an exact row-column-preserving patch from side
`m` to side `m+t`. The patch must add `2t` net points, leave exactly two points
in every old and new row and column, and create no collinear triple.

The active theorem ledger is
[`proofs/prime-patching-recent-index.md`](../proofs/prime-patching-recent-index.md).

## PP1 — Degree interface

### Status: PROVED

Boundary and arbitrary-reservoir degree states are classified. Matching-edge
deletions and movement/refill insertions restore exact old and new row/column
margins.

## PP2 — Selection interfaces

### Status: PROVED AS IMPLICATIONS

The branch contains clone-space local lemmas, deletion-aware expectations,
finite-state CSPs, 2-SAT/CNF endpoints, weighted local lemmas, spread
perfect-matching selection, alternating-component factorization, and cross-block
state amplification. The unresolved work is structured geometric/weighted
conversion.

## PP3 — Robust seed preparation

### Status: OPEN, reduced to explicit concentration cores

## 1. Slab-optimal architecture

```text
macro count M = m^(1/20+o(1)),
pool size   R = m^(19/20+o(1)),
macro width W = m^(19/40+o(1)),
total width T = MW = m^(21/40+o(1)).
```

This balance is optimal among disjoint source-pool architectures with local width
`O(sqrt(R))`. Balanced label maps restore saturation, and product-space local
lemmas give internally no-three macros with fixed-rank spread.

## 2. Controller-aware safety and external closure

Unselected matching-pool edges remain in the source. Controller-aware candidate
states are tested against the full active source.

At the slab-optimal exponents, every remaining patch-only cross-macro class and
every ordinary two-slot source-anchor class has `o(1)` incident probability mass.
Any saturation-compatible controller-aware allocation completes an
`Omega(m^0.525)` patch.

## 3. Dynamic excess shadow

Every candidate has one automatic controller-containing axis blocker. The
pairing-invariant potential

$$
Xi(S)=sum_z (b_S(z)-1)
$$

counts additional nonaxis blockers. Pool-compatible endpoint trades satisfy an
exact insertion-cost-minus-removal-credit identity, and uniform improvement
terminates automatically.

## 4. Four global allocation interfaces

The controller-defect scores provide four independent completion mechanisms:

1. one-sided movement ownership versus cumulative refill slack;
2. deterministic two-sided ownership with `r+s<=W`;
3. random two-sided local Ore allocation;
4. random one-sided average-refill complementary degree.

The total same-slot anchor mass is `m^(2+o(1))`. At the PP3of threshold, the
anchor-acceptable ownership host has deficiency

```text
D_anc = O(m^(1/2-zeta+o(1))) = o(T).
```

Thus anchor-driven ownership failure is not a middle-density Hall rectangle.

## 5. Canonical weighted anchor deficiency

Take a maximum anchor-acceptable ownership matching in the macro-slot clone
host. Dulmage alternating reachability from the unmatched labels gives one
canonical core `X` with neighbourhood `Y=N(X)` and exact deficiency

```text
|X|-|Y| = d <= D_anc.
```

There is no acceptable edge from `X` to the complement of `Y`. All necessary
threshold violations may be confined to a matching between the `d` unmatched
labels and `d` unmatched slots inside this one all-bad cut.

For any nonnegative `d by d` completion matrix of total actual anchor mass `E`,
the entries of weight at most `E/d` contain a perfect matching. Hence the
movement and refill cores have exact bottleneck weights

```text
U_cap = max(u,E_U/d_U),
V_cap = max(u,E_V/d_V).
```

Insert those caps into the controller-defect scores. If every macro satisfies

```text
(B_i+U_cap)/DA_i + (A_i+V_cap)/DB_i <= W,
```

with positive denominators `DA_i,DB_i`, local bipartite Ore gives every macro
matching and the whole patch completes.

Failure is therefore one of:

- a nonpositive controller denominator;
- insufficient baseline local Ore slack;
- slot-expanded anchor energy per necessary crossing large enough to consume
  that slack.

## 6. Source-valid resource endpoint

Adaptive thinning gives a growing endpoint bank with:

- no unary-invalid arc;
- no anchored transition;
- vanishing high-support source-invalid expectation;
- a fully source-valid derangement with one-cell probability `(1+o(1))/q`.

Source admissibility is closed in the sparse-unary endpoint branch.

## 7. Hall and rectangle extraction

After deleting designated recapture and residual unary-shadow cells, failure of
the source-safe endpoint host is exactly a Hall rectangle.

A recapture-dominated Hall core survives adaptive source-valid thinning. Failed
owner-line improvement gives a positive-density family of target-rich repeated
nonaxis lines. Their owner/replacement and Hall-target traces supply
`Omega(q^3)` alternating rectangle candidates. A four-resource matching extracts
`Omega(q)` pairwise row/column-disjoint blocks.

Rectangle extraction is closed.

## 8. Superregular installation and cross-block amplification

For a small linear rectangle bank in a superregular endpoint host:

- the residual host has a perfect matching;
- the matching may be chosen source-valid and low-cost;
- every local block is an equal-margin finite-state permutation variable;
- all no-three conditions are exact rank-at-most-three bad boxes;
- exact insertion shadow is a unary/binary finite-state cost.

The original two rectangle diagonals are not terminal. Cross-block states and
their growing-block generalization bypass bounded signed contradictions.

Equitable colouring of the hard-unary interaction graph partitions every
zero-density support into growing unary-independent groups. Recapture pruning
makes their directional cross hosts near-complete superregular. At secondary
exponent `kappa<1/60`, the global ordinary rectangle branch has automatic
chromatic source validity and remains only when unary/binary shadow weight is
concentrated at the block-credit scale.

## 9. Positive-density hard unary support

Positive-density hard-unary rectangle support gives one endpoint resource with
linearly many forbidden cross cells. Choose one retained-source witness pair for
each cell.

A second star/matching dichotomy yields either:

1. one source point in polynomially many witness pairs, giving free or dynamic
   star credit when moved;
2. a polynomial vertex-disjoint witness matching, hence a resource-disjoint
   credited endpoint bank;
3. concentrated collateral or source-host failure preventing the corresponding
   trade.

Raw positive-density support is therefore reduced to the same paid
star/resource conversion problem as controller shadow.

## 10. Matchable non-superregular hosts

Fix a perfect matching and orient each allowed matching-index edge `i -> j`.
Every alternative perfect matching factors exactly over strongly connected
components of this alternating digraph.

- Trivial components are forced edges. Their forward/backward reachability
  closures are canonical tight forbidden Hall cuts.
- Bounded flexible credited components are paid finite-state banks.
- In a fully credited large component, maximum mobility is the maximum number of
  vertices covered by vertex-disjoint directed cycles.

A maximum-mobility matching gives a resource-disjoint binary alternating-cycle
bank. If mobility is small, its moved set is a directed feedback hub meeting
every alternating cycle.

Every alternating cycle then has length at most the mobility. Counting and
vertex-capacitated max flow give either:

- a one-hub multistate cycle-star bank with an exact paid averaging criterion;
- or a two-hub family of many theta cycles.

The theta family factors into forward and return path signatures. It gives a
fixed-spine bank, a distinct-signature bank, or an inserted edge/pair/triple
shared by many states. Unbounded SCC size itself is no longer terminal.

## 11. Binary dual rectangle and price cores

Binary shadow is governed by minimum endpoint-resource cover congestion. Its LP
dual assigns conflict weights and endpoint-resource prices.

A linear dual value has `Omega(q)` supported conflicts because every conflict
weight is at most one. A four-resource star/matching reduction gives either a
resource star or a growing resource-disjoint conflict family. Every disjoint
conflict is one diagonal of an alternating rectangle.

- A safe opposite diagonal gives a conflict-avoiding rectangle state.
- An unsafe opposite diagonal gives a unary-forbidden resource matching.

The resource prices sharpen this further. Either there is an
`Omega(sqrt(q))` disjoint conflict matching, or an `O(sqrt(q))` high-price
resource core carries `Omega(q)` dual mass. One resource in the core carries
`Omega(sqrt(q))` incident dual weight.

Diffuse fractional dual mass is closed.

## 12. Pool-compatible dynamic endpoint

Cross-block states work inside one controller pool and preserve the candidate
universe. Diffuse hard-source support, pool-local pair/triple mass, and
unary/binary `Xi` weight give a strict potential decrease.

The global `kappa<1/60` source closure cannot automatically be imported after
pigeonholing to one pool. Pool-local pair/triple masses remain explicit
concentration quantities.

## 13. Current exact bottleneck

The missing conversion theorem is reduced to:

1. convert controller denominator failure, insufficient baseline Ore slack, or
   weighted anchor energy concentrated in one canonical ownership core;
2. pay the star/resource trades produced by positive-density hard unary support
   and forced tight Hall cuts;
3. convert chromatically concentrated unary or binary controller-shadow weight
   in the global rectangle branch;
4. convert pool-local pair/triple mass or unary/binary `Xi` weight, including
   captive-star collateral;
5. convert alternating cycle-star/theta support cores or concentrated
   source-invalid and insertion-shadow mass relative to cycle credit;
6. convert the high-price binary resource core, its weighted resource star, or
   paid collateral on the extracted conflict-rectangle bank.

A successful conversion either gives the global allocation directly or strictly
decreases a nonnegative integer potential.

The branch does not prove the no-three-in-line conjecture.

## PP4 — Prime-gap transfer

### Status: PROVED UNDER PP2--PP3

A fixed positive constant times `m^0.525` patch width covers the published
backward prime-gap scale, with standard constant and rounding slack.

## PP5 — Finite exceptions

### Status: VERIFIER COMPLETE; STORED CERTIFICATES CHECKED FOR `2<=n<=10`

The eventual threshold and finite exception list depend on the missing PP3
conversion theorem.