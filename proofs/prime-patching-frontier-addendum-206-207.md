# Prime-patching frontier addendum: original-reference cascade termination

This addendum continues `proofs/prime-patching-frontier-addendum-193-195.md`
after PP3air. It records the original-reference, target-cycle, controller-domain,
captive-partner, and controller-puncture reductions in `docs/206` through
`docs/213` without replacing the larger historical ledgers.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3ais--PP3aix | A fresh-helper single-cycle move increases original-reference defect by exactly `q-1`, preserves the number of defect cycles, keeps all later centres free, and leaves a linear untouched-original helper reservoir | PROVED / CONDITIONAL FRESH-HELPER MARKED INTERFACE | `docs/206-original-reference-single-cycle-defect-growth.md` |
| PP3aiy--PP3aje | A canonical cascade reaches a `Theta(W)` single alternating defect cycle within `O(W/q)=o(W)` generations; before that it completes or exposes a marked-host/base-allocation obstruction | PROVED / CONDITIONAL FRESH-HELPER CASCADE INTERFACE | `docs/207-target-scale-alternating-cycle-cascade-endpoint.md` |
| PP3ajf--PP3ajl | A target-scale Hamilton defect-cycle host has either a sublinear chord feedback hub, a rooted chord-cycle star, a distinct-signature cycle bank, concentrated backbone support/cost, or the bare two-state oscillation core | PROVED / CONDITIONAL ALTERNATING-HOST INTERFACE | `docs/208-hamilton-defect-cycle-chord-localization.md` |
| PP3ajm--PP3ajr | Controller-aware domains expand when noncontroller original points are deleted; every original ownership/global matching certificate survives in all retained-original cascade states | PROVED / CONDITIONAL DIRECT-ALLOCATION INTERFACE | `docs/209-retained-original-controller-domain-monotonicity.md` |
| PP3ajs--PP3ajx | Under the initial robust allocation certificate, the current target-cycle state either completes or yields another free target-size star; chord geometry is unnecessary in the robust branch | PROVED / CONDITIONAL INITIAL ROBUST-CERTIFICATE INTERFACE | `docs/210-robust-target-cycle-absorption.md` |
| PP3ajy--PP3akd | A captive controller-shadow star has either a controller-preserving free-partner credited bank or a controller--controller star; an unspecified captive centre is eliminated | PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE | `docs/211-captive-controller-star-partner-bank.md` |
| PP3ake--PP3akj | Removing one captive centre from its controller pool costs one domain value, preserves every designated star entry, and turns the centre into an ordinary free marked endpoint for paid or direct conversion | PROVED / CONDITIONAL MARKED-HOST OR INITIAL ROBUST-CERTIFICATE INTERFACE | `docs/212-one-controller-puncture-free-star-conversion.md` |
| PP3akk--PP3akp | Repeated controller punctures decompose into finite fixed-universe monotone epochs until completion, an explicit host/allocation obstruction, or a macro-local `Theta(R)` puncture-history core | PROVED / CONDITIONAL CONVERSION INTERFACE | `docs/213-controller-puncture-reserve-termination.md` |

## Exact original-reference coordinate

Fix the original matching layer

```text
M_0={(i,pi_0(i)):i in [m]}
```

and write the current layer as `M_t={(i,pi_t(i))}`. The relative permutation is

```text
sigma_t=pi_0^{-1} o pi_t.
```

Its nontrivial cycles are exactly the alternating cycles of
`M_0 triangle M_t`, and their total row-length is

```text
S_t=|{i:pi_t(i) != pi_0(i)}|.
```

A seed single-cycle move on `q` untouched original rows creates one defect cycle.
Every later fresh-helper move splices `q-1` singleton rows into that cycle, so

```text
S_(t+1)=S_t+q-1.
```

The number of nontrivial cycles remains one. Every defect point is outside the
fixed controller infrastructure, and a linear untouched-original helper
reservoir remains while `S_t=o(m)`.

## Target-scale finite horizon

Put

```text
R=m^(19/20+o(1)),
W=sqrt(R)=m^(19/40+o(1)).
```

For any divergent `q=o(W)`, the first crossing of `alpha W` occurs after

```text
O(W/q)=o(W)
```

steps, with `S_t=(alpha+o(1))W`. For

```text
0<alpha<min{sqrt(xi/8),xi/4},
```

all final binary shadow uses less than `xi R/4`. Final unary support either fits
the remaining margin or produces a free source-star centre of degree

```text
C > 3 xi R/(8S_t)>W.
```

Thus an abstract unbounded cascade is replaced by a finite target-scale endpoint.

## Retained-original domain monotonicity

For `S' subseteq S` containing all fixed controller edges,

```text
B_(S')^+(z;e) subseteq B_S^+(z;e).
```

Movement/refill controller-safe sets expand, while same-slot anchor witness sets
shrink. Hence

```text
H_(i,A,B)^ctrl(S)
subseteq
H_(i,A,B)^ctrl(S')
```

and the threshold graphs satisfy the same inclusion. Every balanced ownership and
global matching chosen for the original source remains valid for every retained-
original base source later in the cascade.

Consequently a dynamic retained-original base failure is impossible once the
initial robust controller-aware certificate exists. The only later margin loss is
the final support of genuinely new points.

## Robust absorption of the target cycle

At the target boundary, the current Hamilton state is already source-valid. Under
the inherited initial base certificate, it satisfies exactly one of:

1. final unary support plus `S_t(S_t-1)` fits the reserved margin, and direct
   allocation completes;
2. unary support destroys the margin and yields another free star larger than
   `W`;
3. the initial controller-aware margin/global-allocation certificate was absent;
4. the source-valid marked path could not be prepared.

Therefore the bare two-state oscillation, sparse-chord mobility hub, rooted
chord-cycle star, distinct-signature cycle bank, and Hamilton-backbone
multiplicity are not independent robust-domain obstructions. They remain useful
only for one-step paid conversion or when replacing a missing robust allocation
certificate.

## Captive stars: partner conversion and one-point puncture

Let a fixed controller point `p` have `C` distinct blocker partners. The
controller-preserving split PP3ajy--PP3akd gives either:

1. at least `C/4` free partners in one permutation layer, forming a credited
   endpoint bank; or
2. at least `C/2` controller partners.

There is now a stronger fallback. Remove `p` from its controller pool and delete
only candidate entries controlled by `p`. Every designated star entry survives,
because a noncontroller blocker pair containing `p` cannot be controlled by
`p`. For every macro-label pair,

```text
|H_punctured| >= |H_original|-1.
```

Relative to the punctured infrastructure, `p` is free. The full star credit is
therefore available to the marked source-star amortisation theorem, while the
robust route charges only one punctured value plus the final support of a
`q`-point state. If `q=o(W)`, final unary failure yields a new star of degree
`omega(W)`.

Thus even a controller--controller star is not intrinsically captive. Its centre
can be freed at one-value domain cost.

## Puncture epochs and reserve endpoint

For puncture sets `X_i subseteq E_i`, keep the candidate universe `V_X` fixed
between punctures and use the integer potential `Psi_X`. Every strict paid trade
inside one epoch decreases `Psi_X`; a puncture adds one new controller point to
some `X_i`.

Before a prescribed reserve `beta R` is exhausted in any macro, only finitely
many punctures are possible and every epoch contains finitely many paid trades.
Hence an infinite moving-controller process is impossible before one reaches:

1. completion/readiness;
2. an explicit source, transition, anchor, Hall, alternating, endpoint-host, or
   initial-allocation obstruction; or
3. a macro with `Theta(R)` distinct punctured controller centres.

Cumulatively,

```text
|H_(i,A,B)^punctured|
>=
|H_(i,A,B)^original|-|X_i|.
```

Therefore an initial margin `gamma+xi` and original ownership/global matching
survive throughout every reserve with `|X_i|<=xi R/2`. Reserve exhaustion records
a chronological macro-local family of `Theta(R)` distinct controller-star
centres, rather than another isolated captive star.

## Chord localization retained for the paid branch

Normalize a target cycle to loops plus one Hamilton successor cycle. Additional
off-diagonal host edges are chords.

- `e=o(L)` chords give an explicit feedback hub of size at most `2e+1=o(L)`.
- `e=Omega(L)` gives either `Omega(sqrt(L))` chords through one endpoint or
  `Omega(sqrt(L))` distinct-tail/distinct-head chord states.
- Repeated support is localized to Hamilton-backbone arcs, pairs, triples, or
  paid-cost classes.

This geometry remains the correct endpoint when direct final allocation is not
available and a monotone paid move is still required.

## Revised live frontier

The remaining concentrated cases are now:

1. proving the **initial** controller-aware margin/global-allocation theorem,
   equivalently controlling its movement/refill blocker, same-slot anchor,
   ownership-Hall, and capped refill concentrations;
2. uniformly preparing fresh-helper, partner-bank, and punctured-centre
   source-valid hosts through transition, anchor, Hall, alternating, and
   distinguished-endpoint constraints;
3. a macro-local `Theta(R)` controller-puncture history core if repeated captive
   centres consume a positive controller reserve;
4. paid conversion of sparse mobility hubs, rooted chord-cycle stars,
   distinct-signature cycle banks, or concentrated backbone support when no
   robust final allocation is available;
5. branches that cannot preserve an original reference layer or cannot choose
   untouched helpers;
6. branches that still require one-step monotone `Xi` descent.

Abstract cascade termination, retained-original base erosion, the bare target
cycle, ordinary chord geometry in the robust branch, an unspecified captive
centre, and a single controller--controller star are no longer separate
frontiers.

The no-three-in-line conjecture remains unproved.
