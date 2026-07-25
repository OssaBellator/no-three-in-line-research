# Thresholded payment of fixed-cell binary fans

The complete-grid candidate-fan theorem PP3afh--PP3afm leaves a fixed centre
cell `a` with a linear partner fibre.  Each partner `b` may create several
distinct blocker candidates, with multiplicity

```text
mu_a(b)=|Z(a,b)|.
```

Raw multiplicity is too coarse.  A residual perfect matching contains only
`q-1` cells after fixing `a`, so all partner states below the threshold

```text
theta=tau R_a/[2(q-1)]
```

consume at most `tau R_a/2` in total.  Delete only the partners above that
threshold.  If the remaining host is matchable, the whole fixed-cell fan is
paid inside the reserved slack.  If the deletion destroys matching in a
superregular host, robust Hall forces a linear secondary-resource pencil made
entirely of uniformly credit-scale partners.

Because candidate classes are matchings in a complete choice grid, candidate
sets of different partners in one fixed row or column are disjoint.  The heavy
pencil therefore carries a genuinely large bank of distinct candidate
incidences rather than repeated notation for the same blockers.

## 1. Weighted partner fibre

Fix a centre cell `a` in a complete two-resource choice grid.  Let

```text
H_a=(L_a,R_a;E_a),
|L_a|=|R_a|=n=q-1,
```

be the residual endpoint host after the two resources of `a` are removed.
For every residual cell `b in E_a`, let

```text
mu(b)=|Z(a,b)|
```

be the number of distinct controller candidate cells blocked by the pair
`{a,b}`.  Put `mu(b)=0` when the pair has no binary insertion shadow.

Let the trade have guaranteed removal credit `C_a>0`, and suppose the other
source and paid terms leave a normalized slack `tau`, with

```text
0<tau<=1.
```

Define

```text
theta=tau C_a/(2n)
```

and the heavy partner support

```text
H_theta={b in E_a: mu(b)>theta}.
```

## 2. Light partners fit inside half the slack

### Proposition PP3ago -- PROVED

Every perfect matching `M` of

```text
H_a\H_theta
```

has total fixed-cell fan cost at most

```text
sum_{b in M} mu(b)
<=
n theta
=
tau C_a/2.
```

#### Proof

The residual perfect matching contains exactly `n` cells.  Every retained cell
has multiplicity at most `theta` by definition.  Sum the `n` bounds. ∎

This estimate is deterministic and does not require independence or a weighted
matching distribution.

## 3. Paid light-fan completion

Let `Y_a` be the residual source-invalid event count and let `J_a^off` be every
insertion cost not belonging to the fixed-cell fan.  Suppose a spread matching
law on `H_a\H_theta` satisfies

```text
E Y_a
+
E J_a^off/C_a
<
1-tau/2.
```

### Theorem PP3agp -- PROVED / CONDITIONAL PAID INTERFACE

If `H_a\H_theta` has the required spread perfect-matching law, then some
residual matching is source-valid and the complete trade has insertion cost
below `C_a`.  Hence the paid potential strictly decreases.

#### Proof

Use the nonnegative objective

```text
Y_a
+
J_a^off/C_a
+
[sum_{b in M}mu(b)]/C_a.
```

The first two terms have expectation below `1-tau/2`.  Proposition PP3ago
bounds the final term deterministically by `tau/2`.  A strict version of the
hypothesis makes the total expectation below one.  Since `Y_a` is integer, a
state with objective below one is source-valid and has total insertion cost
below `C_a`. ∎

Thus a hard fixed-cell fan must prevent matching after deletion of the heavy
partners, or already fail through source/off-fan collateral.

## 4. Robust Hall forces a heavy resource pencil

Assume the original residual host `H_a` is `(epsilon,delta)`-superregular on
both sides, with `0<epsilon<delta`.  Let

```text
Delta_theta
```

be the maximum typed-resource degree of the heavy graph `H_theta`.

### Theorem PP3agq -- PROVED FROM PP3aci

If

```text
Delta_theta
<
epsilon(delta-epsilon)n,
```

then `H_a\H_theta` has a perfect matching.  Consequently, if heavy deletion
destroys every perfect matching, then

```text
Delta_theta
>=
epsilon(delta-epsilon)n.
```

#### Proof

Apply the robust Hall deletion lemma PP3aci to the superregular host `H_a` and
the deletion graph `H_theta`. ∎

Failure therefore gives one secondary endpoint resource incident with a linear
number of heavy partners, each satisfying

```text
mu(b)>tau C_a/(2n).
```

Call this a **uniform heavy partner pencil**.

## 5. Candidate incidences are genuinely distinct

In a complete two-resource grid, Proposition PP3afh says that for fixed centre
`a`, the candidate sets

```text
Z(a,b), b in E_a,
```

are pairwise disjoint as `b` varies along the partner choice row or column.

### Corollary PP3agr -- PROVED

Let `P` be a uniform heavy partner pencil of size `h`.  Then the union of its
candidate sets contains more than

```text
h theta
=
h tau C_a/(2n)
```

distinct candidate cells.

In the robust-Hall branch `h>=epsilon(delta-epsilon)n`, so the pencil contains
more than

```text
[epsilon(delta-epsilon)tau/2] C_a
```

distinct candidate incidences.

#### Proof

Each partner contributes more than `theta` candidate cells.  Pairwise
disjointness allows their cardinalities to add.  Insert the Hall lower bound
for `h`. ∎

This is a credit-scale candidate bank attached to one fixed centre cell and one
secondary partner resource.

## 6. Dyadic strengthening

When candidate multiplicities vary over many scales, partition the heavy
partners into dyadic levels

```text
2^j theta < mu(b) <= 2^(j+1)theta.
```

### Proposition PP3ags -- PROVED

A uniform heavy pencil of size `h` has a dyadic subpencil `P_j` such that

```text
sum_{b in P_j}mu(b)
>=
[sum_{b in P}mu(b)]/[1+log_2(mu_max/theta)].
```

All partners in `P_j` have multiplicities within a factor two, and their
candidate sets remain pairwise disjoint.

#### Proof

Pigeonhole the total multiplicity among the nonempty dyadic levels.  Candidate
disjointness is inherited under restriction. ∎

At polynomial scales the logarithmic loss is `m^(o(1))`, so a credit-scale
heavy pencil yields a comparable-cost candidate bank.

## 7. Revised fixed-cell fan endpoint

### Corollary PP3agt -- PROVED

A complete-grid fixed-cell binary fan has one of the following forms.

1. Heavy partners can be deleted while retaining a spread perfect matching;
   the remaining light fan costs at most `tau C_a/2` and the paid first moment
   completes.
2. Heavy deletion yields a conditional Hall or endpoint-host failure.
3. A secondary endpoint resource carries a linear uniform heavy partner
   pencil.
4. That pencil carries a credit-scale bank of distinct candidate incidences,
   with a factor-two dyadic subbank after only a logarithmic loss.
5. Residual source or off-fan insertion cost is already at the removal-credit
   scale.

Unstructured fixed-cell candidate multiplicity is therefore no longer an
independent frontier.  The hard object is a uniform heavy partner pencil,
conditional Hall structure, or foreign paid/source concentration.

## 8. Finite diagnostic

The script

```text
scripts/check_thresholded_fixed_cell_fan.py
```

computes the threshold, deletes heavy partner cells, enumerates residual
perfect matchings, verifies the deterministic light-cost budget, and reports
`paid_light_completion` or `heavy_hall_star` together with the maximum heavy
resource degree.
