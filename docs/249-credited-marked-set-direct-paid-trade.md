# Credited marked sets admit direct zero-cost paid trades

The preceding complete-support theorems were often phrased as preparation for a
second trade that cancels the insertion table of an earlier endpoint move.  The same
host theorem applies directly to a credited set of **current source cells**.

If the marked cells carry designated blocker credit, a support-free alternating
cycle deletes every marked cell, creates zero new candidate-shadow incidence, and is
therefore paid immediately by the full designated credit.  No preliminary
source-admissible endpoint trade is required.  Failure of the support-free branch
produces the same target canonical structures already handled by the conversion
chains.

## 1. Credited marked sets

Let `S` be the current saturated no-three source.  Let `D subseteq S` be a set of
distinct marked source cells.  Suppose a family `C` of candidate-shadow incidences is
designated so that every incidence in `C` contains at least one member of `D`.
Write

```text
c(D)=|C|
```

with full multiplicity.

### Proposition PP3auc -- PROVED

Every source trade deleting all cells of `D` has removal term at least `c(D)`, unless
a favourable candidate-universe deletion removes an incidence earlier.  In the latter
case that incidence already contributes nonpositively to the chronological potential.

#### Proof

An active designated incidence contains a marked source cell and disappears when the
first such cell is deleted.  Its complete candidate-entry multiplicity is then counted
in the removal term.  If its candidate entry has already been deleted, entrywise
telescoping PP3aqu--PP3ara supplies the favourable contribution instead. ∎

Thus designated credit need not be stable beyond the actual current trade.

## 2. One-layer direct payment

Assume `D` lies in one current permutation layer and has size `s<=W`.  Form the
complete controller-blind rank-three support table for strictly alternating cycles on
`D` and ordinary helpers.

### Theorem PP3aud -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

Exactly one of the following occurs.

1. There is a helper block of size `s` such that, after puncturing selected
   controllers, the strictly alternating cycle:
   - deletes every cell of `D`;
   - is source-valid;
   - preserves saturation and all allocation certificates;
   - has insertion cost zero; and
   - satisfies

     ```text
     Delta Xi<=-c(D).
     ```

2. The complete support table yields an `Omega(s)` canonical star, matching,
   endpoint bank, transition sunflower, anchor bank, fixed-core petal bank, or
   `A_2/B_3/B_4` structure.

#### Proof

Apply PP3atz to the marked block `D`.  In the independent branch, every marked edge
is moved because the selected state is one nontrivial cycle.  Its insertion cost is
zero by PP3aty, while PP3auc gives removal at least `c(D)`.  The dense branch is the
second alternative. ∎

When `c(D)>=s`, the direct trade decreases the potential by at least the marked-set
size.

## 3. Two-layer direct payment

For an arbitrary marked set `D`, decompose the current source as

```text
S=P_0 dot-union P_1,
D_a=D cap P_a.
```

### Theorem PP3aue -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

Let `s=|D|<=W`.  Exactly one of the following occurs.

1. At most two zero-insertion layer cycles delete all of `D` and the complete package
   satisfies

   ```text
   Delta Xi<=-c(D).
   ```

2. One layer produces a canonical converted structure of size at least

   ```text
   Omega(max(|D_0|,|D_1|))=Omega(s).
   ```

3. One occupied layer has a near-complete genuinely reserved-coordinate cover.

#### Proof

Apply PP3aud in each occupied layer.  If both layers give cycles, assign every
designated incidence to the first layer cycle deleting one of its marked endpoints,
exactly as in PP3asn.  The total removal is at least `c(D)` and all later insertion
costs are zero.  Otherwise one layer gives the converted object; the larger layer has
size at least `s/2`.  Coordinate failure has the PP3atc form. ∎

Cross-layer designated incidences require no separate localization.

## 4. Repeated-centre stars

Suppose one source point `p` is contained in `C` designated incidences with distinct
partner resources.

### Proposition PP3auf -- PROVED / CONDITIONAL BOUNDED COMPLETE-SUPPORT INTERFACE

Moving the single marked cell `p` by a bounded zero-cost complete-support cycle gives

```text
Delta Xi<=-C,
```

unless the bounded host produces an already converted terminal source or insertion
pencil.

#### Proof

Take `D={p}` in PP3auc and use the bounded marked host PP3aqh--PP3aqt, together with
selected-controller puncturing if `p` is active. ∎

Thus source stars need not first be transformed into a large endpoint-disjoint bank
when their centre itself may be moved.

## 5. Canonical credited structures close directly

### Corollary PP3aug -- PROVED / CONDITIONAL EXISTING REFINEMENT INTERFACES

Every target-order credited structure produced by the frontier chain has a direct
paid endpoint:

1. a repeated source centre is paid by PP3auf;
2. an endpoint-disjoint credited bank or chronological resource matching is paid by
   PP3aue;
3. an anchor or retained-witness bank is first refined to credited source endpoints
   and then paid by PP3aue;
4. a fixed-core sunflower or terminal source pencil is converted to a star or
   credited endpoint bank by PP3anu--PP3aoc;
5. an insertion pencil is cancelled by PP3aqa--PP3aqt.

The alternative in every case is another target canonical structure or a
near-complete coordinate cover.

#### Proof

Apply the cited conversion theorem for the indicated structure, followed by PP3aud,
PP3aue, or PP3auf. ∎

## 6. The first endpoint trade is not a separate host frontier

### Corollary PP3auh -- PROVED

Once a target credited source structure has been extracted, obtaining a separate
source-admissible saturated "first endpoint trade" is no longer an independent
problem.  The credited structure itself is the marked input to the complete-support
cycle theorem and is either:

1. spent by a direct zero-insertion paid trade;
2. converted into another target canonical structure; or
3. blocked by a near-complete genuinely global coordinate cover.

The no-three and saturation obligations of the direct trade are already included in
the exhaustive normal form PP3atv--PP3aty.

## 7. Revised conversion frontier

### Corollary PP3aui -- PROVED

For the post-allocation repair process, canonical stars, banks, matchings, anchor
cores, support pencils, mobility cycles and chord cycles no longer require an
additional first-trade existence theorem.  They directly yield strict potential
progress or another target converted object.

The remaining concentrated problems are now:

1. the initial macro-patch allocation/completion theorem before a credited repair
   structure is available;
2. a genuinely near-complete exogenous coordinate cover; and
3. any branch not governed by the controller-aware random two-sided allocation and
   dynamic-potential architecture.

The no-three-in-line conjecture remains unproved.
