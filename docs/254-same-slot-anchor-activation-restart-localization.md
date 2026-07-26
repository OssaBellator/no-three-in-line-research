# Same-slot anchor activation under pool-compatible restarts

PP3aux--PP3avm reduce restart comparability to one explicit conditional leaf.  A
pool-compatible repair may introduce new controller edges inside the fixed rectangle
`X_i x Y_i`.  The repair is immediately paid when those edges activate with zero
same-slot anchor mass.  This chapter localizes failure of that zero-mass condition.

The activation table is much simpler than the full endpoint table.  Under strict
alternation, a positive activation event uses one or two ordinary helpers.  On a
square-root reservoir, failure of every cheap state therefore forces weighted unary
or binary mass at exactly the scale needed for a target anchor star or a
disjoint-anchor bank.

## 1. Activation cost of one marked block

Fix one pool-compatible marked block `D` of size `s<=W`, a same-block helper reservoir
`H` of size

```text
N=Theta(max(s^2,1)),
```

and fixed numerical label sets.  For one strictly alternating tied cycle state
`sigma`, let

```text
J_act(sigma)
```

be the number of positive same-slot anchor incidences that are newly present because:

1. a newly inserted source point anchors an unchanged controller edge; or
2. a newly inserted controller edge has a retained or newly inserted source anchor.

Every incidence is counted with its full label and anchor multiplicity.

### Proposition PP3avn -- PROVED

Every incidence counted by `J_act` has nonempty ordinary-helper support of rank one or
two.

#### Proof

An inserted anchor against an unchanged controller uses one inserted source cell.  A
new controller edge is one inserted source cell; its anchor is either retained, giving
one selected cell, or inserted, giving two.  Strict alternation contributes one
ordinary helper to every selected cell.  This is the anchor part of PP3avb. ∎

Let `K_1,K_2` be the distinct rank-one and rank-two supports.  Write `mu(K)` for the
number of activation incidences carried by support `K`, and put

```text
W_1=sum_(K in K_1) mu(K),
W_2=sum_(K in K_2) mu(K).
```

## 2. Exact square-root first moment

Choose a uniform `s`-subset of `H`, then any supported cycle ordering law.  Ignoring
ordering restrictions only increases event probabilities.

### Proposition PP3avo -- PROVED

The activation cost satisfies

```text
E J_act
<=
(s/N) W_1
+
((s)_2/(N)_2) W_2.
```

#### Proof

A fixed singleton support is selected with probability `s/N`; a fixed pair support is
selected with probability `(s)_2/(N)_2`.  Conditional ordering can only remove
incidences.  Sum with multiplicity. ∎

Thus if the right side is below the available removal credit `C`, some state has
activation cost below `C` before the other endpoint conditions are imposed.  Fusing
the remaining rank-three support table gives the corresponding paid-state criterion.

## 3. Failure mass at the critical scale

### Theorem PP3avp -- PROVED

Suppose every admissible activation state has

```text
J_act>=C.
```

Then at least one of

```text
W_1 >= C N/(2s),
W_2 >= C (N)_2/(2(s)_2)
```

holds.

At `N=Theta(s^2)`, this becomes

```text
W_1=Omega(Cs)
or
W_2=Omega(Cs^2).
```

#### Proof

The expectation is at least `C`.  Apply PP3avo.  If both displayed bounds failed, the
two expectation terms would sum to less than `C`. ∎

This is an activation-incidence statement, not merely a support-count statement;
large witness multiplicity is retained.

## 4. Weighted singleton localization

### Proposition PP3avq -- PROVED

If `W_1=Omega(Cs)`, then one of the following occurs.

1. One helper singleton carries activation weight at least `C`.
2. There are `Omega(s)` distinct helper singletons carrying positive activation
   weight.

#### Proof

If no singleton has weight at least `C`, at least `W_1/C=Omega(s)` distinct
singletons are needed. ∎

After choosing one witness incidence per positive singleton, the second alternative
is a target-order family of distinct potential new controller edges or inserted
anchors.

## 5. Weighted binary star-or-matching localization

View the rank-two supports as a weighted graph on `H`.

### Proposition PP3avr -- PROVED

If `W_2=Omega(Cs^2)`, then one of the following occurs.

1. One helper pair carries activation weight at least `C`.
2. One helper vertex has weighted degree `Omega(Cs)`.
3. The positive-support graph contains a matching of size `Omega(s)`.

#### Proof

Remove the first alternative and suppose every edge has weight below `C`.  Fix a
small constant `c>0`.  If some weighted degree is at least `cCs`, use item 2.
Otherwise greedily choose a positive edge and delete its two endpoints.  Each chosen
edge deletes less than `2cCs` total incident weight.  Since the initial total weight
is `Omega(Cs^2)`, choosing `c` below the implicit constant forces `Omega(s)` greedy
steps. ∎

The matching gives pairwise helper-disjoint activation signatures.

## 6. Retained-anchor witness refinement

Choose one concrete activation incidence for every support supplied by PP3avq or
PP3avr.  Record its retained anchor when one exists; if both controller and anchor are
inserted, record the second selected-cell resource instead.

### Theorem PP3avs -- PROVED / CONDITIONAL EXISTING RESOURCE REFINEMENTS

After finite orientation, label-role, and controller-role refinement, activation
failure yields one of:

1. one fixed retained source anchor occurring in `Omega(s)` distinct activation
   signatures;
2. an `Omega(s)` family with pairwise distinct retained-anchor resources;
3. one fixed movement/refill label or controller fibre carrying `Omega(Cs)` activation
   weight;
4. an `Omega(s)` resource-disjoint activation bank; or
5. a heavy one-support activation core of weight at least `C`.

#### Proof

Apply star-versus-matching first to the bipartite incidence graph between helper
supports and retained-anchor resources, then to the controller and label resources.
The helper supports are already singleton-disjoint or pairwise disjoint in the
relevant alternatives.  Finite role refinement loses only an absolute factor. ∎

Items 1--3 have the same resource shapes as the fixed-label anchor columns,
transition stars, and controller--anchor banks of PP3akv--PP3alm.  Item 4 is the new
clean activation-bank form.

## 7. Zero-cost anchor clearing

Let `P` be either the fixed anchor from item 1 or the retained-anchor set from item 2
or 4.  Consider a preliminary pool-compatible trade that moves every point of `P`
before retrying the original marked block `D`.

### Proposition PP3avt -- PROVED / CONDITIONAL COMPLETE-SUPPORT HOST

If the preliminary trade has zero candidate-cell insertion, activates no positive
same-slot entry, and inserts no new anchor for the targeted activation signatures,
then:

1. its current restart potential change is nonpositive;
2. all targeted activation signatures using `P` disappear; and
3. retrying the original `D`-trade has strictly smaller activation-support mass.

#### Proof

The preliminary trade has no positive insertion term, while every removal term is
nonnegative, so PP3ava gives nonpositive potential change.  Every targeted incidence
contains a point of `P`; moving all of `P` destroys it.  The final hypothesis prevents
replacement anchors from recreating the same signatures. ∎

Thus activation clearing does not spend the original removal credit `C`.

## 8. Revised restart endpoint

### Corollary PP3avu -- PROVED

The remaining conditional leaf in PP3avd--PP3avk is no longer arbitrary restart
comparability.  It is the following explicit clearing statement:

> For a target-order retained-anchor star or resource-disjoint activation bank,
> construct the zero-cost preliminary trade of PP3avt, or convert failure of that host
> into current `Theta_E` credit.

Sparse activation support is paid directly by PP3avo.  Dense activation support has
only the five localized forms of PP3avs.  The fixed coordinate sets, numerical labels,
candidate-cell universe, random two-sided allocation arithmetic, and integer
termination mechanism require no further change.

The no-three-in-line conjecture remains unproved.
