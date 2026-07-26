# Current-reference epochs remove historical original-layer dependence

PP3ais--PP3aix use one fixed original permutation layer to make a fresh-helper
cascade monotone.  The invariant is needed only while one cascade is running.  A
historical layer need not survive all previous paid trades.

At the beginning of an epoch, decompose the **current** saturated source into two
permutation layers and choose either layer as the epoch reference.  Run the canonical
single-cycle cascade relative to that layer.  Controller membership is handled by
select-first, puncture-second: across a target-size epoch only `O(W)=o(R)` selected
indices are punctured.  After the epoch is completed by a paid saturated package,
re-decompose the new current source and reset the reference.

## 1. Current-source reference layers

Let `S` be any current saturated source.  Fix a decomposition

```text
S=M_0 dot-union M_1
```

into two permutation layers, supplied by PP3asl.  During one epoch keep `M_1` fixed
and modify `M_0` by tied endpoint permutations.

### Proposition PP3ato -- PROVED

All relative-permutation identities PP3ais--PP3aiu hold with `M_0` equal to this
current epoch layer.  They do not require `M_0` to be a layer of the historically
initial source.

#### Proof

The proofs of PP3ais--PP3aiu use only two permutations on the same current row and
column resources: the fixed reference permutation and the current modified
permutation.  No earlier source state occurs in any identity. ∎

Thus a seed creates one relative defect cycle, and every fresh-helper move enlarges
that cycle by exactly `q-1`.

## 2. Controller-blind fresh helpers

At one generation, let `D_t` be the current relative defect in the active layer.
Choose one centre in `D_t` and `q-1` helper rows outside `D_t`.  Construct the joint
support table without treating controller membership as a forbidden singleton, as in
PP3ast.

### Proposition PP3atp -- PROVED

If the chosen marked/helper block is independent in the controller-blind support
table, puncturing the selected active controllers and then applying the single-cycle
move preserves:

1. source validity and zero encoded insertion support;
2. the fixed complementary layer `M_1`;
3. the relative-cycle growth law PP3aiu; and
4. every allocation certificate with fixed positive `R`-scale margin.

#### Proof

Selected-controller puncturing preserves support independence and loses at most one
value per selected index by PP3asu--PP3asw.  The tied cycle then acts only inside the
active layer and obeys PP3aiu by PP3ato.  Domain-margin preservation is PP3asv. ∎

The old hypothesis that every fixed controller belongs to the reference layer is
therefore unnecessary for epoch growth.

## 3. Total puncture cost of a target epoch

Suppose the seed has size `q` and every later generation adds `q-1` fresh rows.  Let
`S_t` be the defect size after `t` moves.

### Proposition PP3atq -- PROVED

The set of all indices ever selected during the epoch has size exactly `S_t`, and

```text
S_t=q+(t-1)(q-1).
```

Consequently, an epoch stopped at `S_t<=CW` punctures at most `CW` distinct controller
indices.

#### Proof

The seed selects `q` new defect rows.  Every later move selects one old defect centre
and `q-1` previously fixed helpers; only the helpers are new selected indices.  The
sets of fresh helpers are disjoint because selected helpers become defective and are
never eligible again.  Sum the increments. ∎

At `W=sqrt(R)`, the total puncture loss is `O(W)=o(R)`, so all fixed positive macro
and ownership margins survive the complete epoch.

## 4. Linear fresh-helper supply without an original layer

Let `B` be the genuinely global reserved-coordinate set in the active layer.  Assume
`|B|=o(m)` and the current defect has size `O(W)=o(m)`.

### Proposition PP3atr -- PROVED

The active layer contains

```text
m-|B|-|D_t|=(1-o(1))m
```

rows still agreeing with the epoch reference and available before local support
selection.  Controller density does not reduce this count because selected
controllers are punctured afterwards.

#### Proof

A row disagrees with the reference exactly when it belongs to `D_t`.  Remove the
global reservations and the defect rows.  PP3atp handles controller membership after
selection. ∎

Thus every generation has a linear ambient fresh-helper pool unless a near-complete
global coordinate cover or a concentrated rank-three support certificate occurs.

## 5. Reference reset after a paid package

Suppose the epoch ends in a source-admissible saturation-preserving package with
strict negative potential change.  Let `S^+` be its final source.

### Theorem PP3ats -- PROVED

The next epoch may choose an arbitrary permutation layer of a fresh decomposition

```text
S^+=M^+_0 dot-union M^+_1
```

as its new reference.  No relative defect, untouched-original set, or controller
classification from the previous epoch is needed in the next epoch.

#### Proof

PP3ath supplies the fresh decomposition.  The relative permutation for the next
epoch is defined from `M^+_0` and its subsequent modifications only.  At epoch start
the active layer equals its reference, so its relative defect is empty and every
unreserved row is fresh.  Candidate-universe and potential progress from the previous
package are properties of the actual current source, not of the discarded reference
labelling. ∎

Resetting the reference does not undo the strict potential decrease already obtained.

## 6. Epochwise cascade theorem

### Theorem PP3att -- PROVED / CONDITIONAL JOINT LOCAL NORMAL FORM

Consider a sequence of cascade epochs.  Assume in every epoch:

1. the current source is saturated and no-three;
2. genuinely global reservations occupy `o(m)` coordinates in the chosen active
   layer;
3. local source, transition, anchor, endpoint, and insertion restrictions have the
   finite rank-three normal form;
4. the epoch stops by defect size `O(W)` and is completed by one of the established
   paid or direct saturated packages.

Then every epoch has exactly one of the following outcomes.

1. It reaches its prescribed target defect and completes with strict potential
   progress.
2. It produces a target-order canonical star, matching, endpoint bank, transition
   sunflower, anchor bank, or fixed-core petal structure.
3. It exposes a genuinely global near-complete coordinate cover or a restriction
   outside the local normal form.

Historical preservation of one original permutation layer is not an additional
alternative.

#### Proof

Choose a current reference by PP3ato.  Use PP3atp--PP3atr for every fresh-helper
move.  The exact growth law reaches the target in `O(W/q)` generations by PP3aiy--
PP3aje.  Complete the package and reset by PP3ats. ∎

The total selected-controller puncturing inside one epoch is `O(W)=o(R)` by PP3atq.

## 7. Reference-free endpoint

### Corollary PP3atu -- PROVED

For the post-allocation source-trade architecture, preservation of a historically
original reference layer is no longer an independent frontier.  A fixed reference is
required only within one fresh-helper epoch and can be regenerated from the current
saturated source after every completed package.

The remaining alternatives are:

1. a genuinely global condition outside the finite local normal form;
2. a near-complete coordinate cover in every usable current layer;
3. failure to obtain a source-admissible saturated first trade; or
4. failure of the separate initial macro-allocation architecture before the endpoint
   trade process begins.

The no-three-in-line conjecture remains unproved.
