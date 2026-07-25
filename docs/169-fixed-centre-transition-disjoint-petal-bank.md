# Fixed-centre transition stars yield disjoint witness petals

PP3zj--PP3zv correctly identify the local nature of the remaining transition
obstruction. Only one predecessor--middle pair and one successor--outer pair occur
around the fixed captive centre in a single-cycle state. A failed clean-chain bank
therefore gives a near-complete transition role-star, not a simultaneous system of
predecessor assignments.

The role-star nevertheless contains much more independence than PP3zo records.
After choosing one retained source witness for every forbidden transition, there
are `Omega(N^2)` witness records. Saturation and the one-witness-per-middle
uniqueness bound every noncentral old row or column to `O(N)` records. A greedy
resource matching therefore extracts `Omega(N)` petals that share only the fixed
centre and are otherwise disjoint in all endpoint and source resources.

This converts the bounded-choice transition support into a genuine fixed-centre
sunflower bank for the existing paid star/resource machinery.

## 1. Witness records in a predecessor role-star

Use one controller pool of size

```text
N=m^(19/20+o(1))
```

and fix the captive centre index `c`. Consider the predecessor-role alternative of
PP3zm; the successor alternative is transposed.

For all but `o(N)` middle indices `p`, at least

```text
(1-o(1))N
```

predecessors `r` give a source-invalid transition

```text
r->p->c.
```

Discard the one possible axis-heavy middle from PP3zn. For every remaining
forbidden ordered pair `(r,p)`, choose one retained nonaxis source point

```text
z=(u,v)
```

on the line through the two inserted endpoint cells of the transition. Call

```text
(r,p,z)
```

a **witness record**.

### Proposition PP3zw -- PROVED

The predecessor role-star contains

```text
Omega(N^2)
```

distinct witness records. For fixed `p` and fixed retained source point `z`, there
is at most one predecessor `r` in a witness record.

#### Proof

There are `N-o(N)` eligible middle indices and each has `(1-o(1))N` forbidden
predecessors, giving `Omega(N^2)` ordered pairs `(r,p)`. Appending one chosen
witness preserves distinctness because the ordered pair is part of the record.

The fixed-`p,z` uniqueness is PP3zn: for a nonaxis witness, the exact product
equation determines the old column of `r`, and the pool has distinct old columns.
The discarded axis-heavy middle is the only exception. ∎

Thus every retained source point occurs in at most `N` witness records.

## 2. Typed resource support of one record

Write the pool matching point of index `i` as

```text
(x_i,y_i).
```

Associate to a witness record `(r,p,z)` with `z=(u,v)` the typed resource set

```text
R(r,p,z)={
  old column x_r,
  old row    y_r,
  old column x_p,
  old row    y_p,
  source column u,
  source row    v
}.
```

Repeated resources inside one record are kept only once. The fixed centre
resources `x_c,y_c` are deliberately omitted: every petal shares that same centre.

### Proposition PP3zx -- PROVED

Every typed old row or old column outside the fixed centre belongs to at most

```text
4N
```

witness-record resource sets.

#### Proof

Fix an old column `a`.

As a pool endpoint column, `a` equals `x_i` for at most one pool index `i`. Records
with `r=i` number at most `N`, and records with `p=i` number at most `N`. Hence the
endpoint roles contribute at most `2N` records.

As a source-anchor column, saturation gives exactly two retained source points in
column `a`. By PP3zw, each fixed source point occurs in at most one record for
each middle `p`, hence in at most `N` records. The anchor role therefore
contributes at most `2N` more records.

The total is at most `4N`. The row argument is identical, using the distinct pool
old rows and the two retained source points in every old row. ∎

This bound includes all cross-collisions between endpoint resources and anchor
resources.

## 3. Greedy disjoint-petal extraction

Form a hypergraph whose vertices are the typed old row and column resources and
whose hyperedges are the sets `R(r,p,z)`. Every hyperedge has size at most six.

### Theorem PP3zy -- PROVED

The predecessor role-star contains a family of

```text
Omega(N)
```

witness records

```text
(r_i,p_i,z_i)
```

such that their resource sets `R(r_i,p_i,z_i)` are pairwise disjoint.

Equivalently, the corresponding forbidden transitions share only the fixed centre
`c`; outside `c` they use pairwise distinct:

- predecessor endpoint rows and columns;
- middle endpoint rows and columns;
- retained-anchor rows and columns.

#### Proof

By PP3zw the hypergraph has `Omega(N^2)` edges. By PP3zx its maximum vertex degree
is at most `4N`, and every edge has size at most six.

Choose one edge greedily and delete every edge meeting it. One selected edge
deletes at most

```text
6*4N=24N
```

edges. The process therefore selects `Omega(N^2)/(24N)=Omega(N)` pairwise
disjoint hyperedges. ∎

The same conclusion holds for a successor-role star, with petals

```text
(c,s_i,t_i,z_i).
```

## 4. Exact role of the fixed-anchor fan

PP3zo gives one retained source anchor occurring in

```text
Omega(N^2/m)=m^(9/10-o(1))
```

distinct middle-index records. That algebraic fan remains useful, but it is not
needed for the disjoint-petal extraction: PP3zy uses the full quadratic witness
population and the saturation resource bounds.

The two structures are complementary.

1. The PP3zo fan provides one explicit product-correspondence fibre.
2. The PP3zy sunflower provides linearly many resource-disjoint alternatives
   outside the fixed captive centre.

A conversion may exploit whichever side gives the stronger removal credit or
smaller insertion collateral.

## 5. Revised fixed-centre transition endpoint

### Corollary PP3zz -- PROVED

The anchored-transition alternative in the nine-core captive-centre certificate
has one of the following forms.

1. **Paid clean-chain completion:** the support-ranked average PP3zu is below the
   exact removal credit, giving a strict source-valid single-cycle trade.
2. **Weighted clean-chain concentration:** deterministic source invalidity,
   additional-arc source mass, or `Xi` insertion cost on the clean-chain bank
   reaches the removal-credit scale.
3. **Disjoint-petal predecessor sunflower:** there are `Omega(N)` forbidden
   transitions `r_i->p_i->c` whose endpoint and retained-anchor resources are
   pairwise disjoint outside `c`.
4. **Disjoint-petal successor sunflower:** the transposed family
   `c->s_i->t_i` exists.

In alternatives 3 and 4, the sunflower also contains the fixed-anchor algebraic
fan of PP3zo somewhere in the full role-star.

Therefore the generic transition-degree core, the sparse middle relation, and the
two-valued outer table are no longer separate frontiers. The remaining transition
conversion is paid concentration on the clean-chain bank or a fixed-centre
sunflower trade with linearly many disjoint petals.
