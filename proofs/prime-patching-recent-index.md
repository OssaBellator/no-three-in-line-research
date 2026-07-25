# Recent prime-patching theorem index

This focused index records the active square-root-macro, controller-aware
allocation, and endpoint-trade frontier on
`research/all-n-prime-patching`.

The earlier boundary, row-lift, parabolic, width-two, matching-block, and
constant-width diagnostic chains remain in `docs/27` through `docs/60` and in the
repository-wide theorem ledger.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3gj--PP3gm | Complementary-degree global allocation and random balanced ownership | PROVED / FROM PERMUTATION CONCENTRATION | `docs/78-ore-balanced-global-allocation.md` |
| PP3gn--PP3gq | Slab separation of repeated-type mixed triples | PROVED | `docs/79-slab-mixed-type-localization.md` |
| PP3gr--PP3gu | Slab-optimal exponent balance and rank-two mass reduction | PROVED / CONDITIONAL COMPLETION INTERFACE | `docs/80-slab-macro-exponent-rebalancing.md` |
| PP3gv--PP3gy | Optimal macro-count and residual exponent barriers | PROVED | `docs/81-square-root-macro-architecture-optimality.md` |
| PP3gz--PP3hf | Gcd/divisor bounds close patch-only cross-macro energy | PROVED | `docs/82-slab-patch-triple-energy.md` |
| PP3hg--PP3hl | Congruence/divisor-square bounds close ordinary source-anchor energy | PROVED | `docs/83-slab-source-anchor-pair-energy.md` |
| PP3hm--PP3hq | Controller-aware safe domains and corrected completion interface | PROVED / CONDITIONAL ON DENSITY | `docs/84-controller-aware-safe-macro-domains.md` |
| PP3hr--PP3hv | Positive controller shadow forces blocker star or disjoint blocker bank | PROVED | `docs/85-controller-shadow-star-matching-dichotomy.md` |
| PP3hw--PP3hz | Resource-disjoint label/controller/blocker extraction | PROVED | `docs/86-controller-shadow-resource-matching.md` |
| PP3ia--PP3id | Endpoint-permutation trade and exact shadow-change identity | PROVED / CONDITIONAL IMPROVEMENT | `docs/87-controller-shadow-endpoint-permutation-trades.md` |
| PP3ie--PP3ii | Spread derangement first moment and collateral endpoint | PROVED | `docs/88-endpoint-derangement-first-moment.md` |
| PP3ij--PP3im | Fixed-infrastructure potential and monotone termination | PROVED / CONDITIONAL ON CONVERSION | `docs/89-controller-shadow-monotone-termination.md` |
| PP3in--PP3ir | Superregular source-safe endpoint host and paid matching theorem | PROVED | `docs/90-superregular-paid-endpoint-trades.md` |
| PP3is--PP3iw | Endpoint-host pruning and support-rank thinning | PROVED | `docs/91-endpoint-host-regularization.md` |
| PP3ix--PP3jb | Permutation LLL removes low-support cycles and transitions | PROVED / FROM STANDARD LLL | `docs/92-low-support-permutation-local-lemma.md` |
| PP3jc--PP3jh | Divisor factorization regularizes anchored transitions | PROVED | `docs/93-anchored-transition-divisor-regularization.md` |
| PP3ji--PP3jn | Two-scale thinning closes endpoint source validity | PROVED | `docs/94-two-scale-endpoint-source-validity.md` |
| PP3jo--PP3js | Designated-credit recapture avoidance and residual-shadow endpoint | PROVED | `docs/95-designated-credit-recapture-avoidance.md` |
| PP3jt--PP3jx | Shadow-support cleaning and zero-cost endpoint criterion | PROVED | `docs/96-shadow-support-permutation-cleaning.md` |
| PP3jy--PP3kc | Zero-unary host, exact Hall rectangle, and superregular zero-cost endpoint | PROVED / FROM SR1 | `docs/97-zero-unary-shadow-hall-rectangles.md` |
| PP3kd--PP3kh | Exceptional-resource pruning and linear support-core extraction | PROVED | `docs/98-shadow-support-core-regularization.md` |
| PP3ki--PP3kn | Free source-star endpoint conversion and captive-centre split | PROVED / CONDITIONAL ON HOST | `docs/99-source-endpoint-star-conversion.md` |
| PP3ko--PP3kt | Hall witness colouring, tomographic lines, and binary fan localization | PROVED | `docs/100-hall-rectangle-and-binary-fan-localization.md` |
| PP3ku--PP3kz | Pairing-invariant excess-shadow potential and dynamic termination | PROVED / CONDITIONAL ON CONVERSION | `docs/101-dynamic-pool-excess-shadow-potential.md` |
| PP3la--PP3lf | Binary congestion cover, factor-two rounding, Hall inheritance, and LP dual | PROVED / FROM SR1 | `docs/102-binary-shadow-congestion-covers.md` |
| PP3lg--PP3ll | Owner-line assignment energy and grid-rich pencil extraction | PROVED / CONDITIONAL ON UNIFORM CONVERSION | `docs/103-rich-line-endpoint-energy.md` |
| PP3lm--PP3lq | Congestion-one line covers and witness-line overlap | PROVED | `docs/104-line-supported-binary-covers.md` |
| PP3lr--PP3lw | Survivor-load conservation, rich-line cover barrier, fractional dual, and rounding | PROVED | `docs/105-witness-line-survivor-congestion.md` |
| PP3lx--PP3mb | Controller-defect nondegree scores and direct Ore completion | PROVED | `docs/106-controller-defect-ore-scores.md` |
| PP3mc--PP3mf | Diffuse-shadow direct allocation and five concentration alternatives | PROVED | `docs/107-diffuse-shadow-direct-allocation.md` |

## Current scale

The slab-optimal architecture is

```text
macro variables M = m^(1/20+o(1))   = m^0.05
source-pool size R = m^(19/20+o(1)) = m^0.95
macro width W     = m^(19/40+o(1))  = m^0.475
total width T=MW  = m^(21/40+o(1))  = m^0.525.
```

Matching supply, degree restoration, internal macro geometry, fixed-rank spread,
patch-only cross-macro energy, and ordinary two-slot source-anchor energy are
closed.  If the controller-aware global graphs satisfy PP3gl, PP3hq immediately
gives the full patch.

## Direct allocation endpoint

For macro cell defects `a_i(A),b_i(B)` and same-slot anchor counts `u_i(A,B)`, the
PP3ly nondegree bounds define complementary scores `rho_i(A)` and `kappa(B)`.
Global allocation follows whenever every incompatible triple satisfies

```text
rho_i(A)+kappa(B) <= T-8*sqrt(T log T).
```

Fixed labelwise margin together with

```text
Xi_i=o(RT),
max_A U_i(A)=o(RT),
max_B average_i V_i(B)=o(RT)
```

already implies this condition.  Therefore diffuse controller shadow is closed;
a direct failure forces a nearly dead label, macro-scale excess-shadow
concentration, or same-slot anchor row/average-column concentration.

## Hall and binary endpoint

Unary failure is exactly a Hall rectangle in the zero-unary host.  Binary shadow
may be converted into unary deletion with resource congestion controlled by the
fractional cover number `tau^*(B)`.

A single rich witness line has a congestion-one cover.  However, PP3ls proves
that a linear bank of linear-rich **distinct geometric lines** forces linear
unary congestion under the one-survivor deletion pattern.  Thus the rich-line
branch must move the owner lines; it cannot be solved by deleting almost every
cell on every trace.

The owner-line first moment decreases the incidence potential when

```text
K*W_mu/q < H_0.
```

Failure produces a quadratic grid-rich owner/replacement core and a linear
compatible matching of second-generation rich lines.

## Remaining theorem

The branch is reduced to the following structured cases:

1. regularise the five direct-allocation concentrations in PP3mf;
2. convert a Hall rectangle or matchable but non-superregular zero-unary host;
3. convert the second-generation grid-rich owner-line pencil;
4. convert a linear-congestion binary dual packing or witness-line pencil;
5. construct source-admissible pool-compatible endpoint trades with
   `Xi` insertion cost below star/resource removal credit.

Diffuse weighted residuals, external completion energy, source validity of the
resource endpoint, isolated rich fibres, raw binary-fan size, naive rich-line
covering, controller relabelling, and termination are no longer separate open
problems.

The no-three-in-line conjecture remains unproved.