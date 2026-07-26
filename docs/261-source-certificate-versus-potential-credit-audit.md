# Source-certificate credit versus current potential credit

The complete restart-support table contains two logically different kinds of positive
events.

1. **Current-potential events:** candidate-cell blocker incidences and active same-slot
   anchor incidences counted by `Theta_E`.
2. **Source-host events:** unary retained-pair, anchored-pair, inserted-triple, and
   transition certificates that obstruct source validity of a proposed endpoint state.

A current-potential incidence is direct payment for the fixed-infrastructure integer
potential.  A source-host certificate is not.  Moving its retained witness helps
construct a source-valid composite trade, but does not by itself imply a decrease of
`Theta_E`.

This distinction is required in PP3avd, PP3avy, PP3axg, and the master package
PP3axi--PP3axp.

## 1. Two typed credits

A **potential credit unit** is a designated incidence counted in either

```text
Xi_cell(S)
```

or

```text
Lambda_E(S).
```

A **host credit unit** is a designated positive source-invalid or transition
certificate for one proposed marked state.

### Proposition PP3axq -- PROVED

Deleting the marked source endpoint of a potential credit unit contributes directly
to the removal term in `Theta_E`.  Deleting the retained witness of a host credit unit
only removes that source-validity certificate from the proposed state table.

#### Proof

The first assertion is PP3axa--PP3axf.  The second follows from the definitions of the
source and transition support tables: those certificates are not summands of
`Xi_cell` or `Lambda_E`. ∎

The two units may be carried by the same source point, but their accounting roles are
different.

## 2. Transition sunflowers carry host credit

PP3aad attaches one selected transition-certificate incidence to every witness anchor
in a transition sunflower bank.

### Proposition PP3axr -- PROVED

The removal count in PP3aad is host credit, not current `Theta_E` credit, unless the
same anchor independently belongs to a designated candidate-shadow or active-anchor
incidence.

#### Proof

The record removed in PP3aad is

```text
z_i collinear with the two inserted cells of a proposed transition.
```

It is a source-validity certificate for a hypothetical marked state.  Neither
`Xi_cell` nor `Lambda_E` counts arbitrary transition triples.  Therefore its deletion
has no automatic sign in the `Theta_E` identity. ∎

This does not invalidate PP3aad; it corrects the interface at which the bank is used.

## 3. The same issue for source-support pencils

### Proposition PP3axs -- PROVED

A dense unary source support, anchored source pair, inserted source triple, or
fixed-core source pencil supplies direct current payment only after one of the
following additional steps.

1. It is refined to actual candidate-shadow or active-anchor incidences.
2. It is used to construct a source-valid composite trade whose final candidate
   insertion cost is below the original allocation-failure credit.
3. Robust final-state allocation bypasses all transient insertion cost as in
   PP3ahv--PP3aia.

#### Proof

The listed source certificates are absent from `Theta_E`.  Item 1 changes their type to
the potential-credit records audited in PP3axa--PP3axh.  Item 2 preserves the original
potential credit until a source-valid realization is found.  Item 3 uses the final
source rather than dynamic potential descent. ∎

Thus the phrase "converted and paid" must specify which one of these three mechanisms
is used.

## 4. Corrected fixed-attempt support alternative

Let a failed allocation produce an original marked set `D` carrying current potential
credit `C>0`.  While seeking a source-valid zero-insertion realization of `D`, the
complete support table may produce a source-certificate bank `P`.

### Theorem PP3axt -- PROVED

The correct alternatives are:

1. a source-valid realization of `D` has current insertion/activation cost below `C`
   and gives strict `Theta_E` progress;
2. a current-potential support branch gives a separately paid current structure;
3. a source-certificate bank `P` is extracted and must be cleared or absorbed without
   spending the original credit `C`;
4. robust final-state completion applies to a bounded composite path.

#### Proof

Split the complete support table according to PP3axq.  Potential-support branches use
PP3axa--PP3axh.  Source-support branches use PP3axs.  The original marked incidence
credit remains designated until a source-valid trade deletes its marked endpoint or a
favourable entry deletion removes it earlier. ∎

Item 3 is a host-construction branch, not an integer-potential descent step.

## 5. One localized source-certificate bank can be cleared

Every selected source certificate in the canonical endpoint normal form determines a
fixed line containing its retained witness and one or two proposed inserted cells.

### Proposition PP3axu -- PROVED

Every positive noncontroller source-certificate line used in the canonical support
table is nonvertical and nonhorizontal in the endpoint role in which its witness is
cleared.

#### Proof

For a unary retained-pair certificate, a vertical or horizontal blocker through the
candidate cell is the unique axis pair containing its controller and is deleted by the
controller-aware move; it is not a positive noncontroller event.  For an anchored pair,
inserted triple, or transition certificate, two distinct selected endpoint cells lie
on the certificate line.  A tied permutation uses distinct old columns and distinct
old rows, so those two cells cannot lie on a common vertical or horizontal line. ∎

### Theorem PP3axv -- PROVED / CONDITIONAL EXISTING CURRENT CONVERSION INTERFACES

Let `P` be a target-order retained-witness bank for `L=O(s)` fixed source-certificate
lines in one permanent matching block.  Then exactly one of the following occurs.

1. A pool-compatible preliminary cycle moves every witness in `P`, is
   `Theta_E`-nonincreasing, and inserts no replacement witness on any targeted line.
2. The current potential-support table produces a current credited structure and
   strict `Theta_E` progress.
3. A new source-certificate support bank of target order is produced.

#### Proof

By PP3axu, each target line removes at most two helpers from one cyclic gap.  Apply the
buffered role-domain theorem PP3awo to the remaining current support table.  Its
independent branch is item 1 by the same argument as PP3avz.  A dense potential branch
is item 2.  A dense source-validity branch is item 3. ∎

Item 1 clears the selected bank while leaving the original allocation-failure credit
available for retry.

## 6. Cumulative target-line budget

A sequence of source-bank clearings may introduce new retained witnesses and new
certificate lines.  To prevent recreation, one may keep all previously cleared lines
in the role-domain exclusion list.

### Proposition PP3axw -- PROVED

After clearing line families of total size `L_total`, every future cyclic gap loses at
most

```text
2L_total+O(s)
```

helper values to the cumulative no-recreation rules.

As long as

```text
L_total=O(s),
```

PP3awo continues to provide a quadratic role-domain host.

#### Proof

Apply the one-line one-helper principle PP3avv to every retained target line and add
the ordinary marked and reserved exclusions. ∎

When `L_total` reaches order `s^2`, line avoidance can consume a positive fraction of
the complete quadratic reservoir.  The existing line-sparse theorem alone no longer
closes the process.

## 7. Corrected restart interface

### Corollary PP3axx -- PROVED

The fixed-infrastructure integer termination theorem is valid under one additional
named interface:

> **Source-certificate host closure.**  Repeated source-support branches generated
> while realizing one current credited repair either terminate after `O(s)` cumulative
> target lines, enter a current-potential paid branch, or convert an `Omega(s^2)`
> cumulative rich-line family into a current paid structure or robust final
> completion.

Without this interface, PP3avd and PP3avy establish local source-bank clearing but do
not yet prove strict `Theta_E` descent after every failed allocation attempt.

The master theorem PP3axm must therefore list source-certificate host closure among its
conditional local interfaces.  Restart comparability, role-domain Hall, activation
clearing, designated-credit integrity, and prime-gap bookkeeping remain valid.

The next frontier is the cumulative rich-line conversion at the `s^2` threshold.  It
should connect PP3axw to the existing rich-line, endpoint-energy, and line-supported
cover theorems PP3ia--PP3jj and PP3ko--PP3lt.

The no-three-in-line conjecture remains unproved.
