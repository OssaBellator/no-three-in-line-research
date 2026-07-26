# Prime-patching frontier addendum: original-reference cascade termination

This addendum continues `proofs/prime-patching-frontier-addendum-193-195.md`
after PP3air. It records the original-reference, target-cycle, controller-domain,
captive-star, controller-puncture, and initial blocker-density reductions in
`docs/206` through `docs/214` without replacing the larger historical ledgers.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3ais--PP3aix | A fresh-helper single-cycle move increases original-reference defect by exactly `q-1`, preserves the number of defect cycles, keeps later centres free, and leaves a linear untouched-original helper reservoir | PROVED / CONDITIONAL FRESH-HELPER MARKED INTERFACE | `docs/206-original-reference-single-cycle-defect-growth.md` |
| PP3aiy--PP3aje | A canonical cascade reaches a `Theta(W)` single alternating defect cycle within `O(W/q)=o(W)` generations; before that it completes or exposes a marked-host/base-allocation obstruction | PROVED / CONDITIONAL FRESH-HELPER CASCADE INTERFACE | `docs/207-target-scale-alternating-cycle-cascade-endpoint.md` |
| PP3ajf--PP3ajl | A target-scale Hamilton defect-cycle host has either a sublinear chord feedback hub, a rooted chord-cycle star, a distinct-signature cycle bank, concentrated backbone support/cost, or the bare two-state oscillation core | PROVED / CONDITIONAL ALTERNATING-HOST INTERFACE | `docs/208-hamilton-defect-cycle-chord-localization.md` |
| PP3ajm--PP3ajr | Controller-aware domains expand when noncontroller original points are deleted; every original ownership/global matching certificate survives in all retained-original cascade states | PROVED / CONDITIONAL DIRECT-ALLOCATION INTERFACE | `docs/209-retained-original-controller-domain-monotonicity.md` |
| PP3ajs--PP3ajx | Under the initial robust allocation certificate, the current target-cycle state either completes or yields another free target-size star; chord geometry is unnecessary in the robust branch | PROVED / CONDITIONAL INITIAL ROBUST-CERTIFICATE INTERFACE | `docs/210-robust-target-cycle-absorption.md` |
| PP3ajy--PP3akd | A captive controller-shadow star has either a controller-preserving free-partner credited bank or a controller--controller star | PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE | `docs/211-captive-controller-star-partner-bank.md` |
| PP3ake--PP3akj | Removing one captive centre from its controller pool costs one domain value, preserves every designated star entry, and turns the centre into a free marked endpoint for paid or direct conversion | PROVED / CONDITIONAL MARKED-HOST OR INITIAL ROBUST-CERTIFICATE INTERFACE | `docs/212-one-controller-puncture-free-star-conversion.md` |
| PP3akk--PP3akp | Repeated controller punctures decompose into finite fixed-universe monotone epochs until completion, an explicit obstruction, or a macro-local `Theta(R)` puncture-history core | PROVED / CONDITIONAL CONVERSION INTERFACE | `docs/213-controller-puncture-reserve-termination.md` |
| PP3akq--PP3aku | Positive-density initial movement/refill blocker shadow reduces to converted free/punctured stars or a recapture-free resource bank; remaining failure is host/support/reserve/ownership structure | PROVED / CONDITIONAL COMBINED CONVERSION INTERFACE | `docs/214-initial-blocker-density-conversion-closure.md` |

## Original-reference and target-cycle endpoint

Fix an original permutation layer `M_0` and write the current relative permutation
as

```text
sigma_t=pi_0^{-1} o pi_t.
```

Its nontrivial cycles are the alternating cycles of `M_0 triangle M_t`. A
single-cycle seed followed by fresh-helper moves keeps exactly one nontrivial
cycle and satisfies

```text
S_(t+1)=S_t+q-1.
```

With

```text
R=m^(19/20+o(1)),
W=sqrt(R)=m^(19/40+o(1)),
```

any divergent `q=o(W)` reaches `S_t=(alpha+o(1))W` after `O(W/q)=o(W)` steps.
For `alpha<min{sqrt(xi/8),xi/4}`, binary final shadow is below `xi R/4`; final
unary support either completes directly or yields a free star larger than `W`.

## Retained-original monotonicity and robust absorption

For `S' subseteq S` containing the fixed controllers,

```text
B_(S')^+(z;e) subseteq B_S^+(z;e),
```

so movement/refill safe sets expand and same-slot anchor witness sets shrink.
Every original balanced ownership and global matching therefore survives in all
retained-original base states.

At the target-cycle boundary, the current Hamilton state alone either completes
or yields another free target-size star. The bare two-state cycle, sparse chord
hub, rooted chord-star, distinct-signature cycle bank, and Hamilton-backbone
multiplicity are not separate robust-domain obstructions. Their remaining role is
one-step paid conversion or replacement of a missing initial certificate.

## Captive stars: partners and one-controller puncture

A captive star of degree `C` has either `C/4` free partners in one permutation
layer or `C/2` controller partners. More strongly, remove the centre `p` from its
controller pool and delete only entries controlled by `p`. Every designated star
entry remains because a noncontroller blocker pair containing `p` cannot be
controlled by `p`.

For each macro-label pair,

```text
|H_punctured| >= |H_original|-1.
```

Relative to the punctured infrastructure, `p` is free. Its entire star credit is
available to the marked source-star theorem, while the direct route charges one
punctured value plus the final support of a `q`-point state. For `q=o(W)`, final
unary failure yields a new `omega(W)` star.

Thus a controller--controller star is not intrinsically captive.

## Puncture epochs and reserve endpoint

For puncture sets `X_i subseteq E_i`, fix the universe `V_X` between punctures and
use its integer potential `Psi_X`. Strict paid trades decrease `Psi_X`; each
puncture adds one new point to some `X_i`. Before `beta R` punctures occur in any
macro, there are only finitely many epochs and each epoch contains finitely many
paid trades.

Cumulatively,

```text
|H_(i,A,B)^punctured|
>=
|H_(i,A,B)^original|-|X_i|.
```

An initial margin `gamma+xi` and original ownership/global matching survive every
history with `|X_i|<=xi R/2`. Reserve exhaustion records a chronological
macro-local family of `Theta(R)` distinct controller-star centres rather than
another isolated captive star.

## Initial movement/refill blocker-density closure

There are `2MTR` typed movement/refill controller entries. If a fixed positive
fraction are bad, PP3hx--PP3hy gives exactly one of:

1. a source star with `Omega(W)` distinct partners and `Omega(m)` bad-entry
   incidences;
2. an `Omega_delta(T)` resource matching with distinct typed labels, distinct
   controllers, endpoint-disjoint blocker pairs, and no controller/blocker
   overlap.

The star branch is converted by the free-centre, partner-bank, or one-controller
puncture chains. The resource branch is converted by credited-line
self-recapture thinning, the recapture-free endpoint, adaptive ambient support
thinning, or final-state direct allocation.

Consequently positive-density initial blocker shadow now yields one of:

1. strict paid improvement;
2. robust direct completion;
3. a new free target-size or super-target star;
4. a positive-density ambient unary/rank-three/rank-four foreign support core;
5. an explicit source, transition, anchor, Hall, alternating, distinguished-host,
   or endpoint-host obstruction;
6. controller-puncture reserve exhaustion;
7. failure of the initial ownership/global-allocation certificate.

Diffuse positive-density blocker shadow is impossible.

## Chord localization retained for the paid branch

Normalize a target cycle to loops plus one Hamilton successor cycle. Additional
off-diagonal host edges are chords.

- `e=o(L)` gives a feedback hub of size at most `2e+1=o(L)`.
- `e=Omega(L)` gives either `Omega(sqrt(L))` chords through one endpoint or
  `Omega(sqrt(L))` distinct-tail/distinct-head chord states.
- Repeated support is localized to Hamilton-backbone arcs, pairs, triples, or
  paid-cost classes.

## Revised live frontier

The remaining concentrated cases are now:

1. the **initial** same-slot anchor, ownership-Hall, capped refill, and macro
   excess-shadow concentrations;
2. the genuinely `o(1)` movement/refill blocker-density regime, where a
   quantitative complementary-degree theorem is still needed;
3. uniformly preparing fresh-helper, partner-bank, punctured-centre, and
   resource-bank source-valid hosts;
4. a macro-local `Theta(R)` controller-puncture history core;
5. paid conversion of mobility hubs or chord-cycle support when robust final
   allocation is unavailable;
6. branches that cannot preserve an original reference layer;
7. branches that still require one-step monotone `Xi` descent.

Abstract cascade termination, retained-original base erosion, the bare target
cycle, ordinary chord geometry in the robust branch, an unspecified captive
centre, a single controller--controller star, and positive-density diffuse
movement/refill blocker shadow are no longer separate frontiers.

The no-three-in-line conjecture remains unproved.
