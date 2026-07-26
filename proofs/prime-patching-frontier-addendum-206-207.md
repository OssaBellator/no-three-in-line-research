# Prime-patching frontier addendum: original-reference, allocation, and marked-support reductions

This addendum continues `proofs/prime-patching-frontier-addendum-193-195.md`
after PP3air. It records the original-reference, controller-domain, captive-star,
initial-allocation, ambient-support, and marked-source reductions in `docs/206`
through `docs/222` without replacing the larger historical ledgers.

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
| PP3amr--PP3amy | The four high-support marked-source classes admit exact support probabilities and localize to target-size fixed-core sunflowers or resource-disjoint signature banks | PROVED / CONDITIONAL RESIDUAL-SLACK AND SOURCE-HOST CONVERSION INTERFACES | `docs/222-marked-high-support-source-signature-localization.md` |

## Original-reference and robust target-cycle endpoint

Fix an original permutation layer `M_0`. A single-cycle seed followed by
fresh-helper moves keeps exactly one nontrivial relative cycle and satisfies

```text
S_(t+1)=S_t+q-1.
```

With

```text
R=m^(19/20+o(1)),
W=sqrt(R)=m^(19/40+o(1)),
```

any divergent `q=o(W)` reaches a `Theta(W)` defect after `O(W/q)=o(W)` steps.
Final binary shadow remains below the reserved `Theta(R)` margin. Final unary
shadow either completes directly or produces another free target-size star.

For every retained-original source `S'` containing the fixed controllers,

```text
B_(S')^+(z;e) subseteq B_S^+(z;e).
```

Thus controller-safe sets expand and same-slot anchor witness sets shrink. Every
original balanced ownership/global matching survives in all retained-original
base states. The current target-cycle state alone completes or yields another
star in the robust branch.

## Captive stars and puncture epochs

A captive star centre may be removed from its controller pool at one-value domain
cost:

```text
|H_punctured| >= |H_original|-1.
```

Every designated star entry survives because it is controlled by the opposite
endpoint. The centre is then free for the marked source-star theorem. For
puncture sets `X_i subseteq E_i`,

```text
|H_(i,A,B)^punctured|
>=
|H_(i,A,B)^original|-|X_i|.
```

An initial margin and allocation certificate survive while
`|X_i|<=xi R/2`. Between punctures the controller universe is fixed and every
strict paid trade decreases an integer potential. Reserve exhaustion records a
chronological macro-local family of `Theta(R)` distinct star centres.

## Initial controller-aware allocation closure

Positive-density blocker shadow gives a target star or `Omega(T)` full resource
bank. Globally vanishing density cannot hide a fixed-label controller-margin
collapse: one fixed macro--label fibre of size `Omega(R)` gives a target star or
`Omega(W)` full resource matching.

Weighted same-slot anchor cores also convert. A physical controller--anchor pair
is counted at most `W D_m` times in slot-expanded energy, so

```text
L_anchor >= E_slot/(W D_m).
```

Every core-energy obstruction at the active threshold exceeds `2D_mW^3` and
therefore contains a target star or endpoint-disjoint anchor bank. A fixed
movement/refill anchor row or column of mass `Omega(R)` has the same endpoint.

If a true ownership row is dead and its controller denominator has margin
`delta R`, then

```text
B_i+U_i(A)>delta R T.
```

The fixed-label anchor term or fixed-macro controller-defect term gives a target
star/bank.

More generally, after denominator collapse has been split off, every score
denominator is at least `delta R`. Failure of the random two-sided local Ore
condition

```text
rho_i(A)+chi_i(B)<=T-h,
h=o(T),
```

forces one score above `(T-h)/2` and hence one numerator summand above

```text
delta R(T-h)/4=Omega(RT).
```

That summand is a fixed-label anchor mass or fixed-macro controller-defect mass,
already converted above. Therefore the random two-sided theorem either completes
the initial numerical allocation or enters an existing geometric conversion.
Nontrivial one-sided ownership Hall bottlenecks, score truncation, capped refill
concentration, and moderate complementary score pairs are no longer independent
numerical frontiers.

## Ambient foreign-support conversion

For a distinct positive binary signature through one retained ambient resource,
the exact conditioned single-cycle probabilities are

```text
rank three: 1/((Q-1)(Q-2)),
rank four:  (q-3)/((Q-1)(Q-2)(Q-3)).
```

Sparse positive support can be avoided regardless of weight or event multiplicity.
Dense rank-three support becomes a graph link with a linear partner star or
linear matching. Dense rank-four support becomes a 3-uniform link with a nested
fixed-partner pencil or a disjoint signature bank of size

```text
Omega(Q/q^(1/3)).
```

For unary support, the exact probability is

```text
1/(Q-1).
```

Failure of support avoidance gives `Omega(Q)` distinct fixed-resource forbidden
cells. Their retained-source witness graph yields a source star or credited
endpoint bank of size `Omega(sqrt(Q))`, which is asymptotically larger than the
adaptive state size under `q^3/Q=o(1)`.

Thus raw unary/binary multiplicity and unstructured ambient support stars are no
longer separate paid frontiers. The remaining objects are fixed-resource pencils,
resource-disjoint banks, residual marked collateral, or explicit host failure.

## High-support marked-source localization

For a positive marked source signature of endpoint rank `h` requiring `r`
prescribed arcs, the exact conditioned probability is

```text
(b-1)_(h-1) / ((N-1)_(h-1) (b-1)_r).
```

This gives

```text
anchored pair: (b-3)/(N-1)_3,
rank-four triple: 1/(N-1)_3,
rank-five triple: (b-4)/(N-1)_4,
rank-six triple: (b-4)(b-5)/(N-1)_5.
```

Sparse positive support is avoidable independently of witness multiplicity.
Dense support gives a simple uniform link. The recursive link theorem supplies a
fixed-core sunflower or resource-disjoint signature bank of size

```text
anchored pair: Omega(N/b^(1/3)),
rank-four triple: Omega(N),
rank-five triple: Omega(N/b^(1/4)),
rank-six triple: Omega(N/b^(2/5)).
```

All four scales are `omega(W)` throughout `0<kappa<19/80`. Together with the
existing unary, transition, and dynamic-`Xi` reductions, the former nine-core
exceptional-centre certificate now reduces to paid completion, residual
credit-scale collateral, or three simple host geometries:

1. a credited endpoint bank;
2. a fixed-resource or nested-resource pencil;
3. a fixed-core source-invalid sunflower with disjoint petals.

## Chord localization retained for paid branches

Normalize a target cycle to loops plus one Hamilton successor cycle. Additional
chords give a feedback hub, rooted chord-cycle star, distinct-signature cycle
bank, or concentrated Hamilton-backbone support. These objects remain relevant
only when robust final allocation is unavailable and one-step paid conversion is
required.

## Revised live frontier

The remaining concentrated cases are now:

1. converting fixed-resource/nested-resource pencils and fixed-core source
   sunflowers through a uniform source-valid host theorem;
2. residual marked source or insertion collateral already at the removal-credit
   scale;
3. a macro-local `Theta(R)` controller-puncture history core;
4. paid conversion of mobility hubs or chord-cycle support when robust final
   allocation is unavailable;
5. branches that cannot use the slab-optimal random two-sided architecture or
   preserve an original reference layer;
6. branches that still require one-step monotone `Xi` descent rather than robust
   final allocation.

Abstract cascade termination, retained-original base erosion, bare target cycles,
ordinary chord geometry in the robust branch, captive centres, controller--
controller stars, positive-density diffuse blocker shadow, weighted same-slot
anchor cores, individual controller-margin collapse, capped fixed-label anchor
columns, dead true ownership rows, nontrivial one-sided ownership Hall bottlenecks,
score truncation, and raw ambient/marked support multiplicity are no longer
separate frontiers.

The no-three-in-line conjecture remains unproved.
