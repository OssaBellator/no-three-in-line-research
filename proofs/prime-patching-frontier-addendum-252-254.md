# Prime-patching frontier addendum: fixed restarts and anchor activation

This addendum continues `proofs/prime-patching-frontier-addendum-206-207.md` after
PP3auw.  It records the restart-comparability reductions in `docs/252` through
`docs/256`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3aux--PP3avf | Fixed slab coordinates and labels preserve the candidate-cell potential; controller re-pairing is comparable when every newly activated same-slot entry starts at zero anchor mass | PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES | `docs/252-fixed-pool-label-universal-restart-potential.md` |
| PP3avg--PP3avm | Under the activation-safe paid-repair interface, repeated fixed-infrastructure allocation attempts strictly decrease the current nonnegative integer potential and terminate in a successful patch | PROVED / CONDITIONAL ESTABLISHED CONVERSION INTERFACES | `docs/253-monotone-fixed-infrastructure-allocation-termination.md` |
| PP3avn--PP3avu | Failure of cheap same-slot anchor activation forces `Omega(Cs)` unary mass or `Omega(Cs^2)` binary mass and localizes to a heavy support, retained-anchor star, or target resource-disjoint activation bank | PROVED / CONDITIONAL ANCHOR-CLEARING INTERFACE | `docs/254-same-slot-anchor-activation-restart-localization.md` |
| PP3avv--PP3awb | Every target activation line removes at most two helpers from one cyclic gap; a quadratic reservoir gives a target-clean pool-compatible clearing trade or a current paid canonical structure | PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES | `docs/255-line-sparse-anchor-activation-clearing.md` |
| PP3awc--PP3awi | The focused proof dependencies admit an acyclic order from slab geometry to fixed-attempt extraction, local conversion, activation clearing, and finally integer termination | PROVED | `docs/256-acyclic-fixed-infrastructure-dependency-audit.md` |

## Fixed restart infrastructure

Freeze the slab coordinate sets and numerical labels:

```text
(X_i,Y_i)_(i in [M]),
Aset,
Bset.
```

The movement/refill candidate-cell universe depends only on those sets, not on the
current perfect matching between each `X_i` and `Y_i`.  Its excess-shadow potential

```text
Xi_cell(S)=sum_(z in V_cell)(b_S(z)-1)
```

is fixed through every pool-compatible repair.

The active same-slot anchor table does depend on the current matching.  Comparability
uses zero-mass activation:

1. inserted anchors create no positive entry for unchanged controllers; and
2. every new controller edge starts with zero same-slot anchor mass.

Under those rules

```text
Theta_E(S)=Xi_cell(S)+Lambda_E(S)
```

is comparable across consecutive controller pairings.

## Pool-compatible restart termination

Partition every marked source set by the permanent matching blocks

```text
E_1,...,E_M,E_*,Q.
```

Process each block by a tied cycle using helpers from the same block.  Every pool
remains a perfect matching between the same fixed coordinate sets, and

```text
sum_j |D_j|^2 <= |D|^2.
```

Patch-only completion energy is unchanged, and the ordinary two-slot source-anchor
estimate is uniform over every saturated repaired source.

An activation-safe fixed-infrastructure attempt has exactly two outcomes:

```text
macro patch installed,
or
Theta_(E')(S')<Theta_E(S).
```

Nonnegative integer descent rules out infinitely many failures.

## Dense activation localization and clearing

For a marked block of size `s`, helper reservoir `N=Theta(s^2)`, and available credit
`C`, failure of every cheap activation state forces

```text
W_1 >= C N/(2s)
or
W_2 >= C (N)_2/(2(s)_2),
```

hence `Omega(Cs)` unary mass or `Omega(Cs^2)` binary mass.  Weighted
star/matching refinement gives a retained-anchor star or resource-disjoint activation
bank of target order.

Each target signature is one fixed negative-slope line.  For one cyclic gap, one line
forbids at most one helper row and one helper column.  Therefore `L=O(s)` target lines
remove at most `2L=O(s)` values from a helper domain of size `Theta(s^2)`.
Distinct target-clean helpers can be assigned greedily.

Fusing the remaining current support table yields either:

1. a potential-nonincreasing clearing trade that moves all target anchors and creates
   no replacement witness; or
2. a current canonical credited structure that pays directly.

Thus the activation-clearing leaf is reduced to the existing current conversion
interfaces rather than a new restart object.

## Acyclic dependency order

The focused proof order is

```text
slab geometry and uniform completion energy
 -> fixed-attempt allocation extraction
 -> local support conversion and direct payment
 -> pool-compatible activation clearing
 -> fixed-infrastructure integer termination.
```

No local conversion theorem assumes repeated-attempt termination.  Pool-compatible
block refinement is postprocessing of an already extracted marked source set, so it
does not introduce a backward dependency.

## Revised live frontier

There is no remaining independent combinatorial restart frontier inside the focused
slab-optimal chain.  The current work is an exact hypothesis audit and assembly task:

1. verify pool size, marked size, source-validity, and role-domain hypotheses at every
   conditional conversion call;
2. consolidate the chain into one formal prime-patching lemma;
3. verify the starting prime-order construction and quantitative prime-gap transfer;
4. prove the patch-width iteration covers every sufficiently large integer; and
5. handle the finite initial range.

The no-three-in-line conjecture remains unproved.
