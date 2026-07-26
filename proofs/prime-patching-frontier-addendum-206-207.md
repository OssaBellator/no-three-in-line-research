# Prime-patching frontier addendum: original-reference and initial-allocation reductions

This addendum continues `proofs/prime-patching-frontier-addendum-193-195.md`
after PP3air. It records the original-reference, controller-domain, captive-star,
controller-puncture, blocker-density, anchor-core, and ownership reductions in
`docs/206` through `docs/218` without replacing the larger historical ledgers.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3ais--PP3aix | Fresh-helper single-cycle moves increase original-reference defect by exactly `q-1`, preserve one defect cycle, and leave a linear untouched-original helper reservoir | PROVED / CONDITIONAL FRESH-HELPER MARKED INTERFACE | `docs/206-original-reference-single-cycle-defect-growth.md` |
| PP3aiy--PP3aje | The canonical cascade reaches a `Theta(W)` alternating cycle within `O(W/q)=o(W)` generations | PROVED / CONDITIONAL FRESH-HELPER CASCADE INTERFACE | `docs/207-target-scale-alternating-cycle-cascade-endpoint.md` |
| PP3ajf--PP3ajl | A target Hamilton-cycle host localizes to a chord hub, rooted cycle star, distinct-signature bank, concentrated backbone support, or bare two-state core | PROVED / CONDITIONAL ALTERNATING-HOST INTERFACE | `docs/208-hamilton-defect-cycle-chord-localization.md` |
| PP3ajm--PP3ajr | Retained-original controller-aware domains expand under deletion and preserve every original ownership/global-matching certificate | PROVED / CONDITIONAL DIRECT-ALLOCATION INTERFACE | `docs/209-retained-original-controller-domain-monotonicity.md` |
| PP3ajs--PP3ajx | Under the initial robust certificate, the current target-cycle state completes or yields another free target-size star; chord geometry is unnecessary in the robust branch | PROVED / CONDITIONAL INITIAL ROBUST-CERTIFICATE INTERFACE | `docs/210-robust-target-cycle-absorption.md` |
| PP3ajy--PP3akd | A captive controller star has a controller-preserving free-partner bank or a controller--controller star | PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE | `docs/211-captive-controller-star-partner-bank.md` |
| PP3ake--PP3akj | Removing one captive centre from its controller pool costs one domain value, preserves all designated star entries, and frees the centre | PROVED / CONDITIONAL MARKED-HOST OR INITIAL ROBUST-CERTIFICATE INTERFACE | `docs/212-one-controller-puncture-free-star-conversion.md` |
| PP3akk--PP3akp | Repeated punctures form finite fixed-universe potential epochs until completion, explicit obstruction, or a macro-local `Theta(R)` puncture-history core | PROVED / CONDITIONAL CONVERSION INTERFACE | `docs/213-controller-puncture-reserve-termination.md` |
| PP3akq--PP3aku | Positive-density initial movement/refill blocker shadow converts to stars or a recapture-free resource bank | PROVED / CONDITIONAL COMBINED CONVERSION INTERFACE | `docs/214-initial-blocker-density-conversion-closure.md` |
| PP3akv--PP3alb | Slot-expanded anchor-core energy above `D_mW^3` yields a target-size source star or endpoint-disjoint controller--anchor bank | PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE | `docs/215-anchor-core-energy-resource-conversion.md` |
| PP3alc--PP3alh | A fixed movement/refill label with `Omega(R)` unsafe controllers yields a target star or full fixed-label resource bank; individual margin collapse is converted | PROVED / CONDITIONAL CONVERSION INTERFACE | `docs/216-fixed-label-blocker-fibre-conversion.md` |
| PP3ali--PP3alm | Fixed-label same-slot anchor mass `Omega(R)` yields a target star or anchor endpoint bank; capped-refill anchor concentration is converted | PROVED / CONDITIONAL CONVERSION INTERFACE | `docs/217-fixed-label-anchor-column-conversion.md` |
| PP3aln--PP3alt | A completely dead true ownership row forces `Omega(RT)` anchor-row or fixed-macro refill-defect mass and hence a target star or resource bank | PROVED / CONDITIONAL CONVERSION INTERFACE | `docs/218-fully-blocked-ownership-row-conversion.md` |

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

any divergent `q=o(W)` reaches `S_t=(alpha+o(1))W` after `O(W/q)=o(W)`
steps. For `alpha<min{sqrt(xi/8),xi/4}`, binary final shadow is below
`xi R/4`; final unary support either completes directly or yields a free star
larger than `W`.

For every retained-original source `S'` containing the fixed controllers,

```text
B_(S')^+(z;e) subseteq B_S^+(z;e).
```

Thus controller-safe sets expand and same-slot anchor witness sets shrink. Every
original balanced ownership/global matching survives in all retained-original
base states. The current target-cycle state alone therefore completes or yields
another target-size star in the robust branch.

## Captive stars and puncture epochs

A captive star of degree `C` has either `C/4` free partners in one permutation
layer or `C/2` controller partners. More strongly, puncturing the centre removes
only that controller value and leaves every designated star entry present:

```text
|H_punctured| >= |H_original|-1.
```

The centre is then free for the marked source-star theorem. For puncture sets
`X_i subseteq E_i`,

```text
|H_(i,A,B)^punctured|
>=
|H_(i,A,B)^original|-|X_i|.
```

An initial margin and allocation certificate survive while
`|X_i|<=xi R/2`. Between punctures the controller universe is fixed and every
strict paid trade decreases an integer potential. Reserve exhaustion records a
chronological macro-local family of `Theta(R)` distinct star centres.

## Initial blocker-density and fixed-label margin closure

Positive-density initial movement/refill blocker shadow gives either a source
star with `Omega(W)` partners or an `Omega(T)` full resource bank. Both enter the
free/punctured-star, recapture-free, ambient-support, or final-state conversion
chains.

The globally vanishing-density regime cannot hide an individual controller-margin
collapse. In one fixed macro--label fibre, a blocker pair witnesses at most one bad
entry. Hence `a_i(A)=Omega(R)` or `b_i(B)=Omega(R)` yields a blocker star of degree
`W` or an `Omega(W)` resource matching with distinct controllers and no
controller/blocker overlap.

## Anchor-core conversion

In the canonical anchor deficiency core, one physical controller--anchor pair is
counted at most

```text
W D_m
```

times in the slot-expanded energy. Therefore

```text
L_anchor >= E_slot/(W D_m)
```

distinct physical pairs occur. If

```text
E_slot>2D_mW^3,
```

there is a source star of degree `W` or an endpoint-disjoint anchor bank of size
`W`. At the active threshold

```text
u=m^(-1/40+zeta)RT,
```

one has

```text
u/(D_mW^3)=m^(1/40+zeta-o(1))->infinity.
```

Thus every weighted anchor-core obstruction from the local Ore theorem crosses
the star-or-bank threshold.

For one fixed refill label `B`, the product equation determines the movement
label uniquely from a controller--anchor pair. Hence

```text
sum_iV_i(B)=Omega(R)
```

already contains a target star or endpoint-disjoint anchor bank. The same holds
for a fixed movement anchor row. Capped-refill anchor concentration is therefore
converted whenever the movement bottleneck is below `T`.

## Fully blocked ownership rows

If movement label `A` has no compatible refill label in macro `i` and its
movement denominator has margin `delta R`, summing the exact nonedge certificate
gives

```text
B_i+U_i(A)>delta R T.
```

The anchor term is a fixed-label anchor fibre. If `B_i=Omega(RT)`, the four-resource
hypergraph of refill label, controller, and blocker endpoints has either a source
star with approximately `W` partners or an `Omega(W)` full resource matching.
Thus the true ownership bottleneck `r_own=T` is converted.

The truncated score value `r_score=T` alone is not enough to infer a dead true
row; its remaining task is to localize the numerator or denominator that caused
score truncation.

## Chord localization retained for paid branches

Normalize a target cycle to loops plus one Hamilton successor cycle. Additional
chords give either a feedback hub of size `2e+1`, a rooted chord-cycle star, a
distinct-signature cycle bank, or concentrated Hamilton-backbone support. These
objects remain relevant when robust final allocation is unavailable and one-step
paid conversion is required.

## Revised live frontier

The remaining concentrated cases are now:

1. a nontrivial movement ownership Hall bottleneck at a threshold strictly below
   `T`, or score truncation without a true dead row;
2. macro-total controller/excess-shadow mass below the fixed-macro
   positive-density scale;
3. uniform preparation of fresh-helper, partner-bank, punctured-centre,
   anchor-bank, and resource-bank source-valid hosts;
4. a macro-local `Theta(R)` controller-puncture history core;
5. paid conversion of mobility hubs or chord-cycle support when robust final
   allocation is unavailable;
6. branches that cannot preserve an original reference layer;
7. branches that still require one-step monotone `Xi` descent.

Abstract cascade termination, retained-original base erosion, bare target cycles,
ordinary chord geometry in the robust branch, captive centres, controller--
controller stars, positive-density diffuse blocker shadow, weighted same-slot
anchor cores, individual controller-margin collapse, capped fixed-label anchor
columns, and fully dead true ownership rows are no longer separate frontiers.

The no-three-in-line conjecture remains unproved.
