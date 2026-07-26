# Prime-patching frontier addendum: fixed restarts and anchor activation

This addendum continues `proofs/prime-patching-frontier-addendum-206-207.md` after
PP3auw.  It records the restart-comparability reductions in `docs/252` through
`docs/254`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3aux--PP3avf | Fixed slab coordinates and labels preserve the candidate-cell potential; controller re-pairing is comparable when every newly activated same-slot entry starts at zero anchor mass | PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES | `docs/252-fixed-pool-label-universal-restart-potential.md` |
| PP3avg--PP3avm | Under the activation-safe paid-repair interface, repeated fixed-infrastructure allocation attempts strictly decrease the current nonnegative integer potential and terminate in a successful patch | PROVED / CONDITIONAL ESTABLISHED CONVERSION INTERFACES | `docs/253-monotone-fixed-infrastructure-allocation-termination.md` |
| PP3avn--PP3avu | Failure of cheap same-slot anchor activation forces `Omega(Cs)` unary mass or `Omega(Cs^2)` binary mass and localizes to a heavy support, retained-anchor star, or target resource-disjoint activation bank | PROVED / CONDITIONAL ANCHOR-CLEARING INTERFACE | `docs/254-same-slot-anchor-activation-restart-localization.md` |

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

is therefore fixed through every pool-compatible repair.

The active same-slot anchor table does depend on the current matching.  Do not count
all inactive latent pairings.  Instead require:

1. inserted anchors create no positive entry for unchanged controllers; and
2. every new controller edge has zero same-slot anchor mass at activation.

Under those rules the current potential

```text
Theta_E(S)=Xi_cell(S)+Lambda_E(S)
```

is comparable across consecutive controller pairings and strictly decreases whenever
a credited repair has zero candidate-cell insertion.

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

Thus the complete helper demand remains square-root critical.  Patch-only completion
energy is unchanged, and the ordinary two-slot source-anchor estimate is uniform over
every saturated repaired source.

Conditional on activation-safe paid conversion, a fixed-infrastructure attempt has
exactly two outcomes:

```text
macro patch installed,
or
Theta_(E')(S')<Theta_E(S).
```

Nonnegative integer descent then rules out infinitely many failed attempts.

## Dense activation endpoint

For a marked block of size `s`, helper reservoir `N=Theta(s^2)`, and available credit
`C`, let `W_1,W_2` be the weighted rank-one and rank-two activation-support masses.
If every state has activation cost at least `C`, then

```text
W_1 >= C N/(2s)
or
W_2 >= C (N)_2/(2(s)_2).
```

Hence

```text
W_1=Omega(Cs)
or
W_2=Omega(Cs^2).
```

Weighted star/matching localization produces one of:

1. a one-support activation core of weight at least `C`;
2. a target family of distinct singleton supports;
3. a helper star of weighted degree `Omega(Cs)`;
4. a target matching of disjoint helper pairs;
5. after witness refinement, one retained-anchor star or a resource-disjoint
   activation bank.

## Revised live frontier

The sole concentrated restart leaf is now:

> Given a target retained-anchor star or resource-disjoint activation bank, construct
> a pool-compatible zero-cost preliminary trade that moves those anchors, creates no
> new targeted activation witness, and therefore clears the bank without spending the
> original allocation-failure credit.

Equivalent closure is acceptable if failure of that clearing host directly produces
current `Theta_E` credit.

After this leaf is discharged, the fixed-infrastructure integer termination theorem
is available.  A final proof audit must then verify that every earlier conditional
conversion invokes the clearing theorem with matching pool, layer, and scale
hypotheses before the slab patch result is inserted into the global prime-gap
induction.

The no-three-in-line conjecture remains unproved.
