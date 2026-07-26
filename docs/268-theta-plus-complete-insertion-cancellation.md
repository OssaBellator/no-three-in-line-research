# Complete insertion cancellation for the enlarged restart potential

The source-host closure PP3axy--PP3azr produces a source-valid first package while
preserving the original allocation-failure credit.  Its current insertion cost may be
large and may involve both permanent blocks of a paired secant switch.

No unary/binary atom localization is needed.  Every incidence created by the first
package in

```text
Theta_E^+=Xi_cell+Lambda_E+Xi_old
```

contains at least one newly inserted source cell.  A second pool-compatible package
moving the complete inserted set destroys the entire first insertion table.  If the
second package is support-free for all three current terms, it creates no replacement
incidence.  The composite change is at most minus the original removal credit.

## 1. Every new current incidence meets the inserted set

Let a source-valid, saturation-preserving, fixed-infrastructure first trade replace
current source cells by a set

```text
D={d_1,...,d_s}
```

of newly inserted source cells.  Let the pool matching change from `E_0` to `E_1`.
Classify a `Theta^+` incidence as **new** when it is present after the trade and was not
present before it, with full multiplicity.

### Proposition PP3azs -- PROVED

Every new incidence in each of the following tables contains at least one member of
`D`:

1. movement/refill candidate-cell excess `Xi_cell`;
2. old-grid endpoint-shadow excess `Xi_old`;
3. active same-slot anchor incidence `Lambda_(E_1)`.

For the anchor term, containment means that either the retained anchor belongs to `D`
or the active controller edge belongs to `D` as a newly inserted source cell.

#### Proof

Both `Xi_cell` and `Xi_old` are fixed-universe pair potentials.  A blocker pair present
after but not before the trade must contain a newly inserted source point.

For an active anchor incidence, suppose its anchor is old and its controller edge is
also an old source cell retained by the trade.  Then the same controller edge and
anchor were present before, and the fixed label/product equation is unchanged, so the
incidence is not new.  Therefore every new anchor incidence has a new anchor or a new
controller edge, hence meets `D`. ∎

This includes incidences using two inserted cells and incidences whose two inserted
cells lie in different permanent blocks or source layers.

## 2. Deleting the inserted set removes the complete first table

Starting from the post-first-trade source, perform any finite sequence of source-valid,
fixed-infrastructure trades that deletes every member of `D`.  Assign each first-step
new incidence to the first later trade deleting one of its members.

### Theorem PP3azt -- PROVED

The sum of the later removal terms in `Xi_cell` and `Xi_old`, together with destroyed
active-anchor incidences, is at least the complete first-step insertion multiplicity in
`Theta^+`.

An incidence that disappears earlier through candidate-entry deletion, controller-edge
deletion, or anchor-table deactivation contributes favourably and does not weaken the
inequality.

#### Proof

By PP3azs, every first-step new incidence contains a point of `D`.  Immediately before
the first later trade deleting one such point, the incidence is either still active and
is counted in that trade's removal term, or has already disappeared favourably.  Assign
it to that first event.  Multiplicity is retained, so distinct candidate cells, labels,
controller edges, or anchor witnesses remain distinct units. ∎

No common-layer or same-block condition is used in this accounting statement.

## 3. Complete zero-current-cost second host

For the current post-first-trade source, partition `D` by:

```text
post-trade permutation layer,
then permanent matching block.
```

In every nonempty block, seek a strictly alternating marked/helper cycle.  Its complete
support table contains:

1. every source-validity and endpoint condition;
2. every `Xi_cell` insertion event;
3. every `Xi_old` insertion event;
4. every unchanged-controller anchor insertion;
5. every positive newly activated controller edge.

### Proposition PP3azu -- PROVED / CONDITIONAL NAMED CURRENT CONVERSION INTERFACES

For a marked block of size `r`, with `Theta(max(r^2,1))` unreserved helpers and
role-domain loss `O(r)`, exactly one of the following occurs.

1. A pool-compatible source-valid cycle moves the whole block and creates zero new
   incidence in every component of `Theta^+`.
2. The rank-at-most-three support table produces an `Omega(r)` current credited
   structure.
3. A source-host branch enters the fixed-template/paired-switch closure
   PP3axy--PP3azr.
4. An explicit conditional Hall, alternating, non-superregular, distinguished-endpoint,
   or role-host interface fails.

#### Proof

`Xi_old` signatures have helper rank at most two by PP3ayd.  The other current and
source events have rank at most three by PP3avb and the complete endpoint normal form.
Apply the buffered role-domain host PP3awo.  Its independent branch gives item 1.
Dense current branches give item 2; dense source branches enter item 3. ∎

Thus the second host is complete for the enlarged potential, not merely for
`Xi_cell`.

## 4. Blockwise helper budget

Let the nonempty marked block sizes be `r_1,...,r_k`, where the number of source layers
is bounded and the permanent blocks are disjoint.

### Proposition PP3azv -- PROVED

One has

```text
sum_j r_j^2 <= (sum_j r_j)^2=s^2.
```

Every permanent pool block of size `R` supplies its own quadratic subreservoir for
`r_j<=W=Theta(sqrt(R))`, and the total helper volume used across all blocks is `O(s^2)`.

#### Proof

The square inequality is elementary.  Trim a larger permanent block to
`Theta(r_j^2)` helpers by PP3awn.  Blockwise cycles preserve all other blocks by
PP3avc. ∎

The number of permanent blocks met by `D` may grow; no constant-block assumption is
needed for the sum-of-squares bound.

## 5. Complete composite payment in Theta plus

Let

```text
R_1^+
```

be the complete first-step removal credit in `Theta_(E_0)^+`, including candidate-cell,
active-anchor, and old-grid endpoint-shadow incidences.

### Theorem PP3azw -- PROVED / CONDITIONAL NAMED CURRENT CONVERSION INTERFACES

Suppose every nonempty block of `D` receives the zero-current-cost cycle in
PP3azu item 1.  Then the complete composite package satisfies

```text
Theta_(E_final)^+(S_final)-Theta_(E_0)^+(S_0)
<= -R_1^+.
```

In particular every source-valid first package with positive current removal credit is
strictly paid, regardless of the size, rank, multiplicity, or cross-block distribution
of its insertion table.

#### Proof

Write the first change as first insertion multiplicity minus `R_1^+`, with the anchor
term interpreted by chronological incidence creation and destruction.  Theorem
PP3azt says the later removals cover the complete first insertion multiplicity.  Every
later insertion term is zero by PP3azu item 1.  Add the chronological changes. ∎

The statement also covers an incidence created by the first trade and removed by an
earlier favourable universe or controller deletion.

## 6. Paired secant-switch application

### Corollary PP3azx -- PROVED / CONDITIONAL NAMED CURRENT CONVERSION INTERFACES

Let a paired secant-switch package from PP3azk--PP3azr be source-valid and move an
original marked repair carrying credit `C>0`.  Then exactly one of the following occurs.

1. Complete blockwise second cycles cancel its entire `Theta^+` insertion table and the
   composite change is at most `-C`.
2. A blockwise second-host table produces a current paid structure.
3. A source-host branch re-enters the already acyclic fixed-template/paired-switch
   closure.
4. An explicit current endpoint-host interface fails.
5. Robust final-state allocation installs the patch before monotone cancellation is
   needed.

#### Proof

The paired package preserves permanent blocks by PP3azk.  Apply PP3azu blockwise and
use PP3azw in the all-independent branch.  The other branches are its listed
alternatives and the robust endpoint PP3azg. ∎

Thus cross-block binary insertion atoms do not require a one-pool `B_4` truncation.

## 7. Current-weight localization is optional

### Corollary PP3azy -- PROVED

After a source-valid first endpoint package is available, the complete insertion
cancellation theorem dominates separate localization into

```text
A_2,
B_3,
B_4,
fixed-cell fan,
path core,
or partner core.
```

Those localizations remain useful when constructing the first source-valid package or
when a second complete-support host fails.  They are not required merely to pay the
first package's current insertion multiplicity.

#### Proof

Theorem PP3azw cancels the whole insertion table before any rank decomposition. ∎

## 8. Revised current call-matrix frontier

### Corollary PP3azz -- PROVED

The paired secant source-host branch now has a direct current endpoint:

```text
source-valid paired package
 -> complete Theta_E^+ insertion cancellation
 -> strict payment,
```

unless a second-host table produces an already typed current/source structure or an
explicit endpoint-host failure.

The remaining call-matrix audit is therefore confined to the **failure alternatives of
the complete second host**, rather than every possible unary/binary insertion weight of
the first package.

The separate global frontier remains the prime-minus-one seed theorem.

The no-three-in-line conjecture remains unproved.
