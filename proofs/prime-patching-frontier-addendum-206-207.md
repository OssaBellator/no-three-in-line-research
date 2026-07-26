# Prime-patching frontier addendum: original-reference, allocation, and complete marked-support reductions

This addendum continues `proofs/prime-patching-frontier-addendum-193-195.md`
after PP3air.  It records the original-reference, controller-domain,
initial-allocation, ambient-support, marked-source, complete helper-support, and
petal-conditioned reductions in `docs/206` through `docs/229` without replacing
the larger historical ledgers.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3ais--PP3aix | Fresh-helper single-cycle moves increase original-reference defect by exactly `q-1`, preserve one defect cycle, and leave a linear untouched-original helper reservoir | PROVED / CONDITIONAL FRESH-HELPER MARKED INTERFACE | `docs/206-original-reference-single-cycle-defect-growth.md` |
| PP3aiy--PP3aje | The canonical cascade reaches a `Theta(W)` alternating cycle within `O(W/q)=o(W)` generations | PROVED / CONDITIONAL FRESH-HELPER CASCADE INTERFACE | `docs/207-target-scale-alternating-cycle-cascade-endpoint.md` |
| PP3ajf--PP3ajl | A target Hamilton-cycle host localizes to a chord hub, rooted cycle star, distinct-signature bank, concentrated backbone support, or bare two-state core | PROVED / CONDITIONAL ALTERNATING-HOST INTERFACE | `docs/208-hamilton-defect-cycle-chord-localization.md` |
| PP3ajm--PP3ajr | Retained-original controller-aware domains expand under deletion and preserve every original ownership/global-matching certificate | PROVED / CONDITIONAL DIRECT-ALLOCATION INTERFACE | `docs/209-retained-original-controller-domain-monotonicity.md` |
| PP3ajs--PP3ajx | Under the initial robust certificate, the current target-cycle state completes or yields another free target-size star | PROVED / CONDITIONAL INITIAL ROBUST-CERTIFICATE INTERFACE | `docs/210-robust-target-cycle-absorption.md` |
| PP3ajy--PP3akd | A captive controller star has a controller-preserving free-partner bank or a controller--controller star | PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE | `docs/211-captive-controller-star-partner-bank.md` |
| PP3ake--PP3akj | Removing one captive centre from its controller pool costs one domain value, preserves all designated star entries, and frees the centre | PROVED / CONDITIONAL MARKED-HOST OR INITIAL ROBUST-CERTIFICATE INTERFACE | `docs/212-one-controller-puncture-free-star-conversion.md` |
| PP3akk--PP3akp | Repeated punctures form finite fixed-universe potential epochs until completion, explicit obstruction, or a macro-local `Theta(R)` puncture-history core | PROVED / CONDITIONAL CONVERSION INTERFACE | `docs/213-controller-puncture-reserve-termination.md` |
| PP3akq--PP3aku | Positive-density initial movement/refill blocker shadow converts to stars or a recapture-free resource bank | PROVED / CONDITIONAL COMBINED CONVERSION INTERFACE | `docs/214-initial-blocker-density-conversion-closure.md` |
| PP3akv--PP3alb | Slot-expanded anchor-core energy above `D_mW^3` yields a target-size source star or endpoint-disjoint controller--anchor bank | PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE | `docs/215-anchor-core-energy-resource-conversion.md` |
| PP3alc--PP3alh | A fixed movement/refill label with `Omega(R)` unsafe controllers yields a target star or full fixed-label resource bank | PROVED / CONDITIONAL CONVERSION INTERFACE | `docs/216-fixed-label-blocker-fibre-conversion.md` |
| PP3ali--PP3alm | Fixed-label same-slot anchor mass `Omega(R)` yields a target star or anchor endpoint bank | PROVED / CONDITIONAL CONVERSION INTERFACE | `docs/217-fixed-label-anchor-column-conversion.md` |
| PP3aln--PP3alt | A dead true ownership row forces `Omega(RT)` anchor-row or fixed-macro defect mass and hence a target star or resource bank | PROVED / CONDITIONAL CONVERSION INTERFACE | `docs/218-fully-blocked-ownership-row-conversion.md` |
| PP3alu--PP3alz | Uniform denominator margin plus random two-sided local Ore either completes the initial allocation or forces an `Omega(RT)` converted score numerator | PROVED / CONDITIONAL COMBINED CONVERSION INTERFACE | `docs/219-random-two-sided-score-mass-conversion.md` |
| PP3ama--PP3amj | Ambient rank-three/rank-four binary multiplicity is bypassed by positive-support avoidance; dense support becomes fixed-resource pencils or disjoint link banks | PROVED / CONDITIONAL RESIDUAL-SLACK AND ENDPOINT-HOST INTERFACES | `docs/220-ambient-binary-positive-support-link-decomposition.md` |
| PP3amk--PP3amq | Ambient unary multiplicity is bypassed by exact support avoidance; dense support yields a source star or credited witness bank of size `Omega(sqrt(Q))` | PROVED / CONDITIONAL RESIDUAL-SLACK AND ENDPOINT-HOST INTERFACES | `docs/221-ambient-unary-positive-support-conversion.md` |
| PP3amr--PP3amy | The four high-support marked-source classes admit exact support probabilities and localize to target-size fixed-core sunflowers or resource-disjoint signature banks | PROVED / CONDITIONAL RESIDUAL-SLACK AND SOURCE-HOST INTERFACES | `docs/222-marked-high-support-source-signature-localization.md` |
| PP3amz--PP3anf | A sunflower-transversal helper law annihilates one fixed/nested pencil or disjoint signature bank and gives exact helper-and-arc cylinder probabilities | PROVED / CONDITIONAL RESIDUAL-LOAD INTERFACE | `docs/223-sunflower-transversal-single-cycle-host.md` |
| PP3ang--PP3anm | A constant collection of optional-core pencils and empty-core disjoint banks is avoided simultaneously with target expectation `O(b^2/N)=o(1)` | PROVED / CONDITIONAL RESIDUAL-LOAD INTERFACE | `docs/224-simultaneous-finite-sunflower-host.md` |
| PP3ann--PP3ant | A maximal residual-support-independent helper set either has the required size or produces a fixed core with `N^(1-o(1))` variable extensions | PROVED / CONDITIONAL EXTERNAL-HOST INTERFACE | `docs/225-maximal-independent-helper-core-localization.md` |
| PP3anu--PP3aoc | Terminal high-support source pencils are converted: anchored pairs yield credited anchor banks, while inserted-triple pencils are impossible by unique completion | PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE | `docs/226-terminal-source-pencil-closure.md` |
| PP3aod--PP3aoj | Every nonzero canonical source or Xi event has nonempty helper support; an independent block has zero source violations and zero insertion cost, while terminal insertion pencils rejoin existing petal/grid/fan chains | PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES | `docs/227-complete-canonical-support-capture.md` |
| PP3aok--PP3aoq | After fixing one arc/path/fan petal, every nonlocal event has residual helper support; an independent completion leaves only a finite local-core objective | PROVED / CONDITIONAL INDEPENDENT-COMPLETION AND PETAL INTERFACES | `docs/228-petal-conditioned-complete-support-capture.md` |
| PP3aor--PP3aox | A spanning path has at most ten local insertion atoms; one helper bridges a disconnected rank-four petal, and failed local payment yields a credit-scale `A_2`, `B_3`, or `B_4` pencil | PROVED / CONDITIONAL EXISTING INSERTION-PENCIL INTERFACES | `docs/229-one-helper-bridge-local-cost-atomization.md` |

## Original-reference and robust target-cycle endpoint

Fix an original permutation layer `M_0`.  A single-cycle seed followed by
fresh-helper moves keeps one nontrivial relative cycle and satisfies

```text
S_(t+1)=S_t+q-1.
```

With

```text
R=m^(19/20+o(1)),
W=sqrt(R)=m^(19/40+o(1)),
```

any divergent `q=o(W)` reaches a `Theta(W)` defect after `O(W/q)=o(W)`
steps.  Final binary shadow remains below the reserved `Theta(R)` margin.  Final
unary shadow either completes directly or produces another free target-size star.

Controller-safe domains expand when noncontroller original points are deleted.
Every original balanced ownership and global matching therefore survives in all
retained-original base states.  Bare target cycles and ordinary chord geometry
are not robust-domain endpoints.

## Initial controller-aware allocation closure

Positive-density blocker shadow, one collapsed movement/refill label, weighted
same-slot anchor energy, a fixed-label anchor row or column, or a dead true
ownership row all yield a target star or credited endpoint bank.

After denominator collapse is split off, every controller-defect score denominator
is at least `delta R`.  Failure of the random two-sided condition

```text
rho_i(A)+chi_i(B)<=T-h,
h=o(T),
```

forces one numerator summand above

```text
delta R(T-h)/4=Omega(RT).
```

That summand is a fixed-label anchor mass or a fixed-macro controller-defect mass,
already converted.  Hence nontrivial one-sided Hall bottlenecks, score truncation,
capped refill concentration, and moderate complementary scores are no longer
independent numerical frontiers.

## Exact positive-support avoidance

For one conditioned ambient resource, distinct positive binary signatures have
probabilities

```text
rank three: 1/((Q-1)(Q-2)),
rank four:  (q-3)/((Q-1)(Q-2)(Q-3)),
```

and a unary signature has probability `1/(Q-1)`.  Sparse support is avoided
regardless of weight or event multiplicity.  Dense support becomes a simple
fixed-resource pencil or a resource-disjoint link bank.

For a marked source signature of endpoint rank `h` requiring `r` arcs, the exact
probability is

```text
(b-1)_(h-1) / ((N-1)_(h-1)(b-1)_r).
```

The four high-support source classes therefore localize to fixed-core sunflowers
or disjoint signature banks at scales `omega(W)`.

## Uniform sunflower and pencil hosts

For one fixed-core petal system, choose `b-1` distinct petals and one helper from
each.  Every target signature is absent, and a residual pattern using `t` helper
indices and `r` arcs has exact probability

```text
[(b-1)_t/(H)_t]
[product 1/|P_j|]
[1/(b-1)_r].
```

A constant number of exceptional classes can be handled simultaneously.  Omit
one optional helper from every nonempty fixed core.  Every remaining empty-core
family is a matching of support sets of size at least two, so a uniform marked
block selects a target support with total expectation

```text
O(b^2/N)=o(1).
```

Thus fixed/nested pencils and extracted fixed-core source sunflowers are not
separate host obstructions under residual slack.

## Complete residual-support reduction

Let `H_all(c)` contain every nonempty helper support of every positive canonical
source-invalid or insertion signature after the marked centre is fixed.  Take a
maximal independent helper set.

If it has size at least `b-1`, then every single-cycle state on that block has

```text
source-invalid count = 0,
insertion cost = 0.
```

The only formal zero-helper insertion classes are a diagonal unary arc and a
transposition, both absent from a single cycle.

If the maximal independent set is too small, bounded support rank gives one fixed
core with at least

```text
(N-b)/sum_(r<k_0) binom(b-2,r)
```

variable extensions.  With adaptive `b=N^(o(1))`, this is `N^(1-o(1)`.
Diffuse residual support and support-free insertion weight therefore disappear.

The terminal source pencils are closed: anchored-pair pencils give credited
anchor banks, while inserted-triple pencils are impossible by unique completion.
The terminal insertion pencils are exactly the existing `A_2`, `B_3`, and `B_4`
fixed-centre objects.

## Petal-conditioned zero-collateral completion

Condition on a compatible local arc forest `F` with at most four arcs and five
fixed endpoint indices.  Contracting the fixed paths gives exactly

```text
(b-|F|-1)!
```

single-cycle completions.  Every nonlocal canonical event has a nonempty residual
helper support.  An independent residual helper block therefore removes all
nonlocal source and insertion collateral, leaving only a finite local-core table.

If `F` is one spanning path, the local table is deterministic.  Every compatible
arc on the fixed vertices is either already a path arc or closes a forbidden
proper cycle.

For a directed path of `r<=4` arcs, the selected local insertion atoms are

```text
r A_2 atoms,
r-1 B_3 atoms,
binom(r,2)-(r-1) B_4 atoms.
```

The total counts for `r=1,2,3,4` are `1,3,6,10`.  If local cost reaches the
removal credit, one atom has at least a `1/10` share of that credit.

A disconnected rank-four partner petal is bridged by one helper:

```text
a->b->x->c->d
```

or its reverse component order.  If no clean paid bridge exists, pigeonholing the
two orientations and ten atom roles yields a credit-scale fixed-axis unary,
fixed-centre path, or centre-arc partner pencil.  Thus diffuse residual collateral
and a mixed finite local table are no longer separate petal endpoints.

## Revised live frontier

The remaining concentrated cases are now:

1. payment or conversion of a **single credit-scale local `A_2`, `B_3`, or `B_4`
   atom** inside the explicit arc-petal, path/grid, or partner/fan chains when
   robust final allocation is unavailable;
2. second-generation terminal pencils produced after conditioning a local petal,
   which re-enter the same three insertion geometries;
3. external controller-pool, distinguished-endpoint, Hall, alternating, or other
   endpoint-host failure;
4. a macro-local `Theta(R)` controller-puncture history core;
5. paid mobility-hub or chord-cycle conversion in branches that cannot use robust
   final allocation;
6. branches that cannot use the slab-optimal random two-sided architecture or
   preserve an original reference layer;
7. branches that still require one-step monotone `Xi` descent rather than paid
   multi-step or robust final-state completion.

Abstract cascade termination, retained-original base erosion, bare target cycles,
ordinary chord geometry in the robust branch, captive centres, controller--
controller stars, numerical ownership arithmetic, raw support multiplicity,
fixed-core source sunflowers, diffuse residual support, support-free insertion
weight, high-support source terminal pencils, diffuse petal collateral, and mixed
finite local-core tables are no longer separate frontiers.

The no-three-in-line conjecture remains unproved.