# Allocation-domain bypass for fixed-cell binary fans

The threshold theorem PP3ago--PP3agt treats a fixed-centre binary fan as paid
`Xi` insertion cost.  Large partner multiplicity may then produce a uniform
heavy pencil.  For the final controller-aware allocation, however, the relevant
quantity is not multiplicity.  It is the number of controller-edge--label
entries removed from each domain.

A source-valid endpoint matching containing one fixed centre cell selects at
most `n` partner cells.  Every centre--partner pair determines one nonaxis line.
On the movement side, one such line meets a prescribed final row label in at
most one candidate cell and meets the old column of a prescribed controller
edge in at most one candidate cell.  Thus its movement entries form a matching
between controller edges and movement labels.  The refill statement is
transposed.

Consequently the complete fixed-cell fan created by any residual matching has
maximum controller-edge--label degree at most `n`, regardless of the number of
candidate incidences lying on its lines.  Every refined same-slot domain loses
at most `2n` values.  Since the active endpoint matching size is `o(R)`, any
fixed positive domain-density margin absorbs the entire fan.  This gives a
direct allocation bypass: the endpoint trade need not decrease `Xi` when it
already leaves the controller-aware allocation graphs inside their robust
margin.

## 1. Candidate-entry traces of one secant line

Let the selected controller layer consist of edges

```text
e=(x_e,y_e)
```

partitioned into the macro pools.  A movement entry has candidate cell

```text
z_M(e,A)=(x_e,A),
```

and a refill entry has candidate cell

```text
z_F(e,B)=(B,y_e).
```

Fix two compatible endpoint cells `a,b`.  Their line `ell(a,b)` is nonvertical
and nonhorizontal.

### Proposition PP3agu -- PROVED

For one fixed nonaxis line `ell`:

1. for every movement label `A`, at most one movement candidate entry lies on
   `ell`;
2. for every refill label `B`, at most one refill candidate entry lies on
   `ell`;
3. for every controller edge `e`, at most one movement label and at most one
   refill label give candidate entries on `ell`.

#### Proof

The line meets the horizontal row `A` in at most one point.  If that point is an
integer candidate `(x,A)`, the selected controller matching has at most one edge
in old column `x`, and that edge lies in at most one macro pool.  This proves the
first statement.  The refill statement uses the unique intersection with the
vertical column `B`.

For a fixed controller edge, its movement candidates lie on the old vertical
line `x=x_e`; a nonvertical line meets that line once.  Its refill candidates
lie on the old horizontal line `y=y_e`; a nonhorizontal line meets that line
once. ∎

Thus candidate multiplicity along one geometric line is a matching-type
perturbation of the controller-edge--label incidence graph.

## 2. A residual endpoint matching has degree at most its size

Fix one endpoint centre cell `a`.  Let

```text
M={b_1,...,b_n}
```

be a residual endpoint matching compatible with `a`.  Let `Z_M(a,M)` be the
simple set of movement candidate entries lying on at least one line `a b_j`,
and define `Z_F(a,M)` analogously for refill entries.

### Theorem PP3agv -- PROVED

Viewed as bipartite graphs between controller edges and final labels,

```text
Delta(Z_M(a,M)) <= n,
Delta(Z_F(a,M)) <= n.
```

The inequalities hold on both bipartition sides.  They do not depend on the
weighted fan multiplicities

```text
mu_a(b_j)=|Z(a,b_j)|.
```

#### Proof

For one movement label, every one of the `n` lines contributes at most one
entry by PP3agu.  For one controller edge, every line also contributes at most
one movement entry.  Hence both movement degrees are at most `n`.  Transpose for
refill entries.  Repeated geometric lines only reduce the simple union, so no
distinct-line assumption is required. ∎

When the completed endpoint state is source-valid, the lines are in fact
distinct: two different partners on one line with `a` would give three inserted
collinear cells.

## 3. Exact loss from one refined macro domain

Let

```text
H_i^base(A,B)
```

be the controller-edge domain in macro `i` after all source, anchor, and
insertion exclusions except the fixed-cell fan have been imposed.  Let

```text
H_i^fan(A,B)
```

be the domain after also deleting every value whose movement entry at `A` or
refill entry at `B` belongs to the fan support.

### Proposition PP3agw -- PROVED

For every macro `i` and every final label pair `(A,B)`,

```text
|H_i^base(A,B) \ H_i^fan(A,B)| <= 2n.
```

#### Proof

At label `A`, Theorem PP3agv gives at most `n` newly bad movement controller
edges in the complete controller layer, and hence at most `n` in macro `i`.
At label `B`, it gives at most `n` newly bad refill controller edges.  Their
union removes at most `2n` values from the paired domain. ∎

This is a simple-support bound.  One deleted value may account for arbitrarily
many weighted `Xi` incidences, but it is still only one unavailable domain
value.

## 4. Stability of the compatibility graphs

Fix constants `gamma>0` and `xi>0`.  Define the margin compatibility graph

```text
J_i^base(gamma+xi)
=
{(A,B): |H_i^base(A,B)| >= (gamma+xi)R}.
```

### Theorem PP3agx -- PROVED

If

```text
2n <= xi R,
```

then

```text
J_i^base(gamma+xi) subseteq J_i^fan(gamma)
```

for every macro `i`.

Consequently every balanced ownership and global label matching supported by
the margin graphs remains supported after the complete fixed-cell fan is
inserted.

#### Proof

For every margin-compatible pair, PP3agw gives

```text
|H_i^fan(A,B)|
>=
(gamma+xi)R-2n
>=
gamma R.
```

Therefore the pair remains in the threshold graph used by PP3ho and PP3hq.  The
same ownership map and global matching may be retained. ∎

The statement also applies to the complementary-degree allocation criterion:
a fixed margin in the domain threshold is preserved before the global graph is
formed.

## 5. Slab-scale absorption

At the slab scale,

```text
R=m^(19/20+o(1)).
```

All endpoint and conditioned matching states used in the marked and resource
branches have

```text
n=m^(kappa+o(1))
```

with `kappa<19/80`, and the two-scale resource-bank states use the much smaller
range `kappa<1/40`.

### Corollary PP3agy -- PROVED

At every active scale,

```text
n/R=o(1).
```

Hence for every fixed `xi>0`, the hypothesis `2n<=xi R` holds for all
sufficiently large `m`.

#### Proof

The exponent difference is at most

```text
19/80-19/20=-57/80<0.
```

The two-scale endpoint exponent gives an even larger saving. ∎

Thus even a multiplicity-heavy fan is a vanishing domain perturbation once its
candidate entries are viewed without multiplicity.

## 6. Direct allocation bypass

### Theorem PP3agz -- PROVED / CONDITIONAL DIRECT-COMPLETION INTERFACE

Suppose a source-admissible fixed-centre endpoint trade has been selected and:

1. every source, anchor, and nonfan insertion obstruction is already included in
   `H_i^base(A,B)`;
2. the margin graphs `J_i^base(gamma+xi)` satisfy one of the global allocation
   criteria PP3fy or PP3gl;
3. the local macro width inequality of PP3ho holds;
4. `2n<=xi R`.

Then the complete fixed-cell binary fan, with arbitrary candidate multiplicity,
does not prevent the final controller-aware allocation.  The same balanced
ownership and global label matching remain valid in `J_i^fan(gamma)`, and PP3hq
produces the saturated no-three patch.

#### Proof

The endpoint trade is source-admissible by hypothesis.  PP3agx preserves every
margin-compatible label pair after the fan support is inserted.  Apply the same
global allocation in the post-trade threshold graphs, then use PP3ho and PP3hq.
∎

This is a direct completion theorem, not a monotone-potential step.  It does not
claim that the endpoint trade decreases `Xi`; it shows that no such decrease is
needed when all remaining controller domains have fixed positive slack.

## 7. Revised fixed-cell endpoint

A fixed-cell fan now has two separate completion mechanisms.

1. The paid threshold theorem PP3ago--PP3agt completes through removal credit
   when light partners fit inside the reserved paid budget.
2. The allocation-domain theorem PP3agu--PP3agz ignores multiplicity and
   completes directly whenever the nonfan domains retain a fixed `Omega(R)`
   margin.

The remaining fixed-cell work is therefore only:

- failure of the base domain margin or global allocation criterion;
- source, anchor, or off-fan insertion obstruction;
- a non-superregular or nonmatchable endpoint host before the source-valid trade
  is selected;
- a branch in which neither paid credit nor direct allocation slack is
  available.

Uniform heavy partner multiplicity by itself is no longer an independent
frontier.

## 8. Finite diagnostic

The script

```text
scripts/check_fixed_cell_fan_allocation_bypass.py
```

constructs the line traces of a fixed centre and residual matching, verifies the
controller-edge--label degree bounds, computes the exact loss from every
macro-label-pair domain, and reports whether the stored margin supports direct
allocation.