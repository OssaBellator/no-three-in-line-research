# Prime-patching frontier addendum: fixed restarts, exact widths, and source-host credit

This addendum continues `proofs/prime-patching-frontier-addendum-206-207.md` after
PP3auw.  It records the restart-comparability, exact-width, and assembly-audit
reductions in `docs/252` through `docs/261`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3aux--PP3avf | Fixed slab coordinates and labels preserve the candidate-cell potential; controller re-pairing is comparable when every newly activated same-slot entry starts at zero anchor mass | PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES | `docs/252-fixed-pool-label-universal-restart-potential.md` |
| PP3avg--PP3avm | Under activation-safe paid conversion, repeated fixed-infrastructure allocation failures strictly decrease the current nonnegative integer potential and terminate | PROVED / CONDITIONAL ESTABLISHED CONVERSION INTERFACES | `docs/253-monotone-fixed-infrastructure-allocation-termination.md` |
| PP3avn--PP3avu | Failure of cheap same-slot anchor activation forces `Omega(Cs)` unary mass or `Omega(Cs^2)` binary mass and localizes to a heavy support, retained-anchor star, or target resource-disjoint activation bank | PROVED / CONDITIONAL ANCHOR-CLEARING INTERFACE | `docs/254-same-slot-anchor-activation-restart-localization.md` |
| PP3avv--PP3awb | Every target activation line removes at most two helpers from one cyclic gap; a quadratic reservoir gives a target-clean pool-compatible clearing trade or a current paid canonical structure | PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES | `docs/255-line-sparse-anchor-activation-clearing.md` |
| PP3awc--PP3awi | The focused dependencies admit an acyclic order from slab geometry to fixed-attempt extraction, local conversion, activation clearing, and finally integer termination | PROVED | `docs/256-acyclic-fixed-infrastructure-dependency-audit.md` |
| PP3awj--PP3awp | A buffered independent helper set handles role-specific `O(s)` deletions for every `1<=s<=W`; failure still yields an `Omega(s)` canonical structure | PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES | `docs/257-buffered-role-domain-square-root-host.md` |
| PP3awq--PP3awz | Slab constants amplify the leading width coefficient arbitrarily; heterogeneous full-scale macros give every exact width in a fixed `m^(21/40)` band, and a shifted-prime choice avoids the small-width regime | PROVED / CONDITIONAL ESTABLISHED PRIME-PATCHING INTERFACES AND SHORT-INTERVAL INPUT | `docs/258-constant-amplified-exact-width-prime-transfer.md` |
| PP3axa--PP3axh | Fixed-label and fixed-macro potential credit attaches to current source cells, survives puncturing, and is removed exactly once under permanent-block refinement | PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES | `docs/259-designated-credit-permanent-block-audit.md` |
| PP3axi--PP3axp | The geometry, allocation, conversion, restart, and exact-width chain consolidates into one master patch lemma with a finite named hypothesis list | PROVED / CONDITIONAL NAMED LOCAL AND SOURCE-HOST INTERFACES | `docs/260-master-exact-width-prime-patching-lemma.md` |
| PP3axq--PP3axx | Source-validity and transition certificates are host credit, not automatic current-potential credit; one bank clears line-sparsely, while arbitrary regeneration reduces to cumulative rich-line conversion or robust final completion | PROVED / CONDITIONAL CUMULATIVE SOURCE-HOST CLOSURE | `docs/261-source-certificate-versus-potential-credit-audit.md` |

## Fixed restart infrastructure

Freeze the slab coordinate sets and numerical labels:

```text
(X_i,Y_i)_(i in [M]),
Aset,
Bset.
```

The movement/refill candidate-cell universe depends only on those sets.  Its
excess-shadow potential

```text
Xi_cell(S)=sum_(z in V_cell)(b_S(z)-1)
```

is fixed under pool-compatible controller re-pairing.  The active same-slot anchor
table changes with the matching, but consecutive states are comparable when inserted
anchors create no incidence for unchanged controllers and every new controller edge
starts with zero anchor mass.  The current restart potential is

```text
Theta_E(S)=Xi_cell(S)+Lambda_E(S).
```

Activation failure is rank one or two.  Dense failure yields a retained-anchor star or
resource-disjoint activation bank; each target line removes only `O(1)` values from a
single cyclic role, so a target bank deletes only `O(s)` values from a
`Theta(s^2)` helper reservoir.

## Scale-uniform role domains

Permanent-block refinement may create any marked block size `1<=s<=W`, and target-line
pruning gives different helper domains for different roles.  Let every role omit at
most `kappa s` values.  An independent buffer of size

```text
b=ceil((kappa+1)s)
```

contains at least `s` allowed helpers for every role, so Hall supplies distinct role
representatives.  If no such buffer exists, rank-at-most-three subset counting gives

```text
Omega(s^2) rank-two support
or
Omega(s^3) rank-three support,
```

and hence an `Omega(s)` canonical structure.  Larger permanent pools may be trimmed to
a `Theta(s^2)` subreservoir.  This closes the previously unstated role-domain and
small-block versions of the critical helper theorem.

## Potential-credit integrity

Fixed-label blocker fibres, fixed-label anchor columns, fixed-macro defect cores, and
resource-disjoint banks all refine to actual current source cells.  Every designated
candidate-shadow or active-anchor incidence contains one marked source endpoint.
After partitioning by permanent matching blocks, assign each record to the first block
that deletes one of its marked endpoints or its active controller.  It is then removed
exactly once, or earlier by a favourable candidate/controller-entry deletion.

Thus current potential credit survives:

```text
layer refinement,
controller puncturing,
bank truncation,
cross-block partition,
and sequential pool-compatible cycles.
```

## Exact-width and prime-gap bookkeeping

PP3gr gives

```text
MW=(a gamma sqrt(b)/16+o(1))m^(21/40),
ab<1.
```

For any prescribed leading coefficient `K_0`, choose

```text
b=(gamma/(32K_0))^2,
a=1/(2b).
```

Then `ab=1/2` and the leading coefficient is `K_0`.  A target full-scale width is
partitioned among `Theta(M)` macros whose widths differ by at most one and remain
`Theta(W)`.  Heterogeneous hypergeometric ownership has the same local Ore proof and
sublinear slack.

For a target side `n`, put `x=n+1` and

```text
y=x-x^(21/40).
```

A prime in `[y-y^(21/40),y]` gives a required patch width between
`x^(21/40)` and `x^(21/40)+y^(21/40)`, hence in a fixed constant-factor full-scale
band.  The all-`n` transfer therefore does not require small-width patches or an
unspecified `Omega` coefficient.

## Source-host credit correction

Current potential credit and source-host credit are different.

- A candidate-shadow or active-anchor incidence is a summand of `Theta_E` and pays
  directly when its marked endpoint is deleted.
- A unary source certificate, anchored pair, inserted triple, or transition
  certificate only obstructs source validity of a proposed state.  Moving its witness
  may clear the host but does not by itself decrease `Theta_E`.

One target source-certificate bank may be cleared by the same line-sparse buffered
role-domain method while leaving the original allocation-failure credit untouched.
However, repeated source-bank regeneration can accumulate target no-recreation lines.
After total line count `L_total`, each future role loses at most

```text
2L_total+O(s)
```

helpers.  The quadratic host remains automatic while `L_total=O(s)`.  At
`L_total=Theta(s^2)`, the current argument reaches the existing rich-line/grid-pencil
barrier rather than a proven current-potential decrease.

Robust final-state allocation supplies a separate valid exit when the complete
source-valid composite path has final new-point square `o(R)` and final unary support
fits the retained margin.

## Master conditional patch statement

The consolidated exact-width patch theorem now has a finite, honest input list:

```text
fixed slab geometry and uniform completion energy,
heterogeneous controller-aware allocation,
current potential-support conversion and payment,
scale-uniform role-domain hosts,
designated-potential-credit integrity,
source-certificate host closure,
zero-mass activation,
and fixed-infrastructure restart comparison.
```

Under those named local and source-host interfaces, every sufficiently large saturated
source on `[m]^2` extends by every exact width in a fixed positive constant-factor band
around `m^(21/40)`.  Together with prime-minus-one seeds and the exponent-`21/40`
backward-prime interval theorem, this would imply the all-`n` conclusion.

## Revised live frontier

The remaining concentrated tasks are now:

1. **cumulative source-certificate rich-line closure:** convert an
   `Omega(s^2)` cumulative nonaxis line family into current `Theta_E` payment, a
   bounded composite source-valid path, or robust final completion;
2. **remaining current call-matrix audit:** verify every conditional current-potential
   conversion with its exact pool size, marked size, layer, puncture, role-domain, and
   source-validity hypotheses;
3. **prime-minus-one seeds:** prove or import a saturated no-three construction on
   `[p-1]^2` for every sufficiently large prime;
4. after an asymptotic theorem, make thresholds effective and cover the finite initial
   range.

Restart comparability, activation clearing, role-domain Hall, designated-potential
credit, the slab leading constant, exact full-scale widths, and small-width avoidance
are no longer independent frontiers.

The no-three-in-line conjecture remains unproved.
