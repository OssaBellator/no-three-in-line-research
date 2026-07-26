# Completed endpoint states absorb binary current multiplicity

The dense current-support row has already lost its raw host, coordinate-cover,
weighted-grid, and fixed-cell multiplicity leaves.  The remaining petal and paired-switch
objectives still list binary candidate-shadow terms after a source-valid endpoint state is
completed.

Those terms depend on pairs of inserted endpoint cells.  Multiplicity may be large, but
the final controller-aware allocation sees only the simple candidate entries lying on the
corresponding secant lines.  A completed state of size `b` determines at most
`binom(b,2)` nonaxis lines.  At every active conditioned-cycle and paired-switch scale,
`b^2=o(R)`, so all binary pair-shadow entries fit inside any fixed positive allocation
margin.

This chapter removes binary `B_3/B_4`, binary centre-core, binary variable-collateral,
and paired-switch binary multiplicity as independent current-row frontiers.  Unary
inserted--retained-source and active-anchor terms remain separate.

## 1. Binary insertion support is a secant-line union

Let `U` be the inserted endpoint-cell set of one completed source-valid state.  Write

```text
b=|U|.
```

For every unordered pair `{u,v} subseteq U`, let `ell(u,v)` be its geometric line.  Axis
lines are assigned to the existing fixed-row/fixed-column support classes.  Let
`L_2(U)` be the set of distinct nonaxis pair lines.

### Proposition PP3bbu -- PROVED

One has

```text
|L_2(U)| <= binom(b,2).
```

Every binary current-potential insertion incidence whose two selected endpoint cells
belong to `U` is supported on one line of `L_2(U)`.

#### Proof

There is at most one line per unordered pair.  A binary insertion incidence is defined
by two selected endpoint cells and one controller candidate cell collinear with them, so
its candidate lies on their pair line.  Axis pairs enter the fixed-axis support classes
and all remaining pairs enter `L_2(U)`. ∎

The statement is about simple support.  Any number of blocker candidates or weighted
incidences may reuse the same line.

## 2. Controller-domain trace of the line union

Use the fixed candidate-cell universe of PP3aux.  A movement candidate for controller
edge `e=(x_e,y_e)` and label `A` is `(x_e,A)`; a refill candidate for label `B` is
`(B,y_e)`.

### Proposition PP3bbv -- PROVED

Viewed as a simple bipartite graph between controller edges and one movement label, or
between controller edges and one refill label, the candidate-entry trace of `L_2(U)` has
maximum degree at most

```text
|L_2(U)|.
```

For every macro and paired label state `(A,B)`, adding all binary pair-shadow entries of
`U` deletes at most

```text
2|L_2(U)| <= 2 binom(b,2)
```

controller values from the refined domain.

#### Proof

PP3agu shows that one nonaxis line meets a prescribed movement row, refill column, or
controller candidate fibre in at most one entry.  Summing over the distinct line union
gives the one-sided degree bound.  A paired domain loses at most one movement-side set
and one refill-side set, so their union has size at most twice the line count. ∎

Candidate multiplicity along one line does not change this deletion count.

## 3. Slab-scale absorption

At every conditioned filler-cycle and paired-switch call used in the complete second
host, the completed local state has size

```text
b=m^(kappa+o(1)),
0<kappa<19/80,
```

while

```text
R=m^(19/20+o(1)).
```

### Proposition PP3bbw -- PROVED

Uniformly over all such completed states,

```text
2 binom(b,2)=o(R).
```

Consequently, if the controller domains before binary pair-shadow insertion have margin

```text
|H_i^base(A,B)| >= (gamma+xi)R
```

for fixed `gamma,xi>0`, then for all sufficiently large `m` the same states remain in
the post-insertion compatibility graph at threshold `gamma R`.

#### Proof

The exponent of `b^2` is strictly below

```text
2(19/80)=19/40,
```

whereas the exponent of `R` is `19/20`.  Hence `b^2/R=o(1)`.  Apply PP3bbv and the
margin calculation of PP3agx. ∎

No first-moment payment of the binary multiplicity is required when the final allocation
margin is available.

## 4. Application to the named binary current classes

### Theorem PP3bbx -- PROVED / CONDITIONAL BASE ALLOCATION CRITERIA

Suppose a completed endpoint state `U` is source-valid and all unary
inserted--retained-source, active-anchor, old-grid unary, and nonbinary deterministic
conditions are already included in the base domains or in a separately named source
objective.  If the base ownership and global label allocation criteria hold with fixed
margin `(gamma+xi)R`, then every binary current-potential incidence created by pairs of
cells of `U` may be inserted without changing the chosen ownership or label matching.
The patch is installed.

The conclusion applies to:

1. rank-three and rank-four binary `Xi` terms `B_3,B_4`;
2. complete two-resource grids and projective candidate covers;
3. fixed-cell binary fans and heavy partner pencils;
4. binary centre-core and bounded-support variable terms in arc/path-petal states; and
5. binary current-potential terms in paired secant-switch product states.

#### Proof

Each listed term is supported by two selected endpoint cells and therefore by
`L_2(U)`.  Propositions PP3bbv--PP3bbw preserve every base-compatible paired domain.
Retain the same balanced ownership and global label matching, then apply PP3ho and
PP3hq. ∎

The theorem is multiplicity-blind: it depends only on the simple pair-line union.

## 5. Revised current-row rank split

### Corollary PP3bby -- PROVED

Inside the slab-optimal complete second-host architecture, binary current multiplicity
is no longer a live frontier after a source-valid endpoint state has been selected.
The remaining current-row terms are confined to:

1. unary inserted--retained-source candidate incidences;
2. active-anchor and old-grid unary incidences;
3. explicit source-validity concentration;
4. failure of the nonbinary base allocation conditions; or
5. a branch outside the active conditioned-state scale.

Thus the finite current frontier is now unary/source/base-domain rather than binary,
host-existential, coordinate, or raw-multiplicity based.

The dense source row and the global prime-minus-one seed theorem remain separate.  The
no-three-in-line conjecture remains unproved.

## 6. Finite diagnostic

Run

```bash
python scripts/check_completed_state_binary_support.py \
  experiments/completed-state-binary-support-example.json
```

The checker constructs every distinct nonaxis pair line of a finite completed endpoint
state, computes its movement/refill candidate traces, verifies the line-degree and paired
domain-loss bounds, and checks whether a supplied fixed allocation margin absorbs the
complete binary pair-shadow support.  It is a finite regression check for the
multiplicity-blind secant accounting.
