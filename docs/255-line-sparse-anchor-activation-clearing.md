# Line-sparse clearing of same-slot anchor activation banks

PP3avn--PP3avu reduce dense restart activation to a retained-anchor star or a
resource-disjoint activation bank.  Each signature in such a bank is one fixed line
through a proposed same-slot movement/refill pair.  This line geometry makes the
clearing host deterministic: for one marked endpoint role, each target line forbids
at most one helper row and at most one helper column.

Thus `L=O(s)` target signatures delete only `O(s)` values from each helper domain,
whereas the critical reservoir has size `Theta(s^2)`.  The target-recreation
constraints cannot themselves destroy the clearing host.

## 1. One-line one-helper principle

Let one current matching block be

```text
E subseteq X x Y,
```

and let `h=(c_h,r_h)` range over its helper edges.  Fix a marked edge
`d=(c_d,r_d)` and a target activation line `ell`.

In a strictly alternating gap, the two replacement source cells involving `h` are
of the forms

```text
(c_d,r_h),
(c_h,r_next),
```

where `r_next` is the row of the next marked edge in the chosen cyclic order.

### Proposition PP3avv -- PROVED

For fixed `d,r_next,ell`:

1. at most one helper edge `h` satisfies `(c_d,r_h) in ell`; and
2. at most one helper edge `h` satisfies `(c_h,r_next) in ell`.

#### Proof

A nonvertical line meets the fixed column `c_d` in at most one row, and a nonhorizontal
line meets the fixed row `r_next` in at most one column.  Same-slot movement/refill
lines have negative slope, hence are neither vertical nor horizontal.  Matching
uniqueness gives at most one helper edge with the required row or column. ∎

## 2. Target-clean gap domains

Let `Lset` be a family of `L` target activation lines.  Fix a cyclic order of `t`
marked anchors in one matching block.  For every marked-to-marked gap, define its
helper domain to contain the helper edges for which neither replacement cell lies on
a line of `Lset`.

### Proposition PP3avw -- PROVED

Every gap domain loses at most `2L` helper values.

Consequently, if the ambient helper reservoir has size `N`, then every gap domain has
size at least

```text
N-2L-t,
```

after excluding all marked edges as well.

#### Proof

Apply PP3avv to every target line and both replacement orientations.  The marked-edge
exclusion costs at most `t`. ∎

At the activation scale

```text
L=O(s),
t<=O(s),
N=Theta(s^2),
```

all gap domains have size `(1-o(1))N` and each role omits at most `kappa s` helpers
for one fixed constant `kappa`.

## 3. Deterministic distinct-helper assignment

### Theorem PP3avx -- PROVED

For sufficiently large `s`, suppose

```text
N-2L-t >= t.
```

Then one may assign pairwise distinct helpers to all `t` cyclic gaps so that no
inserted clearing cell lies on any target activation line.

#### Proof

Process the gaps greedily.  Before the `j`-th choice, at most `j-1<=t-1` helpers have
been used.  Its domain has at least `t` values, so one unused value remains. ∎

For bounded `t`, use the same argument with a fixed finite padding reservoir.  A
fixed-anchor star (`t=1`) is therefore easier than the target bank case even when it
carries `Theta(s)` target lines.

This theorem handles target-line avoidance alone.  Fusion with the current support
table uses the buffered role-domain host PP3awj--PP3awp.

## 4. Fusion with the current restart support table

Target-line avoidance is role-specific domain pruning, not an additional global
hypergraph obstruction.  On the surviving role domains, expose the ordinary current
restart-support table.  It contains source validity, candidate-cell insertion,
unchanged-controller anchor insertion, and new-controller activation outside the
targeted line family.

### Theorem PP3avy -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

For a retained-anchor star or resource-disjoint activation bank of target order,
exactly one of the following occurs.

1. A pool-compatible clearing cycle moves every marked anchor, has zero current
   candidate-cell insertion, activates no positive same-slot entry, and inserts no
   replacement anchor on any targeted activation line.
2. The current restart-support table yields a target canonical structure carrying
   current `Theta_E` credit.

#### Proof

PP3avw gives role domains omitting at most `kappa s` helpers from a quadratic
reservoir.  Apply the buffered role-domain theorem PP3awo to the complete rank-three
restart-support table.  Its role-respecting independent branch gives item 1.  Its
dense branch gives an `Omega(s)` canonical current structure by PP3awm, which is
converted and paid by PP3aug and PP3aqo--PP3aqt. ∎

This separates future-target clearing from current-potential payment.

## 5. Clearing is potential-nonincreasing

### Proposition PP3avz -- PROVED

The clearing cycle in PP3avy item 1 satisfies

```text
Theta_(E')(S')<=Theta_E(S).
```

It destroys every targeted activation signature whose retained anchor is marked and
creates none of those signatures with a replacement anchor.

#### Proof

Current candidate-cell insertion and same-slot activation are zero.  Every removal
term is nonnegative, so PP3ava gives the potential inequality.  Each target signature
contains a moved retained anchor, while PP3avx excludes every replacement from its
line. ∎

The original allocation-failure credit is not spent by this preliminary clearing
step.

## 6. Activation-bank clearing theorem

### Theorem PP3awa -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

Let a failed allocation produce a marked repair `D` with credit `C>0`.  Suppose the
zero-mass activation condition for `D` fails and PP3avs yields a retained-anchor star
or resource-disjoint activation bank `P` of order `Omega(|D|)`.

Then one of the following occurs.

1. A potential-nonincreasing pool-compatible clearing package moves `P`, removes the
   localized activation bank without recreating it, and leaves the original credit
   `C` available for the retried `D`-repair.
2. Before clearing completes, a current canonical credited structure is paid and
   strictly decreases `Theta_E`.
3. The original marked set `D` itself is moved by a current paid structure, directly
   spending its allocation-failure credit.

#### Proof

Apply PP3avy blockwise to `P`, reserving the cells of `D` unless a paid current
structure contains them.  Item 1 follows from PP3avz.  A dense current-support branch
is item 2 after direct payment.  If that branch moves a member of `D`, assign the
original designated incidence to the first such move, giving item 3. ∎

After item 1, the localized target support is absent.  Recompute the activation table
for the retried repair.  Sparse remainder is paid by PP3avo; any new dense remainder
has strictly fewer witnesses in the cleared resource class or enters item 2.

## 7. Restart closure

### Corollary PP3awb -- PROVED / CONDITIONAL ESTABLISHED CONVERSION INTERFACES

The anchor-clearing interface in PP3avt and PP3avu is discharged by
PP3avv--PP3awa together with the buffered role-domain theorem PP3awj--PP3awp.
Therefore the fixed-infrastructure termination theorem PP3avj--PP3avk no longer has a
separate same-slot activation hypothesis.

The remaining work inside the focused chain is a hypothesis audit ensuring that the
cited current canonical conversion theorems preserve designated credit and
source-valid marked endpoints under permanent-block refinement, without circular
reliance on PP3avk.

The no-three-in-line conjecture remains unproved.
