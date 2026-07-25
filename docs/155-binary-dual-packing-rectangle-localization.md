# Binary dual packings localize to resource stars or rectangle banks

PP3lf leaves a linear-congestion fractional binary-conflict packing. The dual
weights are normalized by endpoint-resource prices of total mass one. This
normalization bounds every individual conflict weight by one, so total dual
weight `Omega(q)` has support on `Omega(q)` distinct conflicts.

Each binary conflict uses four endpoint resources. A hypergraph star/matching
dichotomy then gives either a high-degree endpoint resource or a growing family
of resource-disjoint conflicts. Every resource-disjoint conflict is one diagonal
of an alternating rectangle. If the opposite diagonal is safe, it gives an exact
conflict-avoiding state; if not, the unsafe cross cells form a unary resource
matching.

## 1. Individual dual weights are bounded

Use the dual variables from PP3le:

```text
y_B >= 0 for binary conflicts B,
lambda_v >= 0 for endpoint resources v,
sum_v lambda_v <= 1.
```

For every endpoint cell `a`, dual feasibility gives

$$
sum_{B containing a} y_B <= lambda_left(a)+lambda_right(a).
$$

### Proposition PP3wi -- PROVED

Every conflict weight satisfies

$$
0 <= y_B <= 1.
$$

Consequently, if

$$
sum_B y_B >= rho q,
$$

then at least `rho q` distinct binary conflicts have positive dual weight.

#### Proof

Choose either cell `a` of conflict `B`. Then

$$
y_B
<= sum_{B' containing a} y_B'
<= lambda_left(a)+lambda_right(a)
<= sum_v lambda_v
<= 1.
$$

The support-cardinality statement follows because each positive term is at most
one. ∎

Thus a linear dual value cannot be carried by finitely many weighted conflicts.

## 2. Four-resource star or matching

Represent every binary conflict `{a,b}` by the four endpoint resources used by
the two compatible cells. These four resources are distinct.

### Theorem PP3wj -- PROVED

Let `h` be the number of supported conflicts. For every integer `L>=1`, one of
the following holds.

1. Some endpoint resource belongs to at least `L` supported conflicts.
2. There is a family of at least
   
   $$
   h/(4L)
   $$
   
   supported conflicts whose four-resource sets are pairwise disjoint.

#### Proof

Take a maximal resource-disjoint conflict family of size `m`. If
`m>=h/(4L)`, use it. Otherwise the `4m` resources used by the maximal family
meet every supported conflict. Since they cover `h` conflicts, one resource is
incident with more than `L` of them. ∎

With `h>=rho q` and `L=ceil(sqrt(q))`, the dual packing contains either a
`sqrt(q)` resource star or an `Omega(sqrt(q))` resource-disjoint conflict
matching.

## 3. Every disjoint conflict is an alternating rectangle

Let one resource-disjoint conflict be

```text
a = (ell_1,r_1),
b = (ell_2,r_2),
```

with `ell_1 != ell_2` and `r_1 != r_2`. Define the opposite cells

```text
c = (ell_1,r_2),
d = (ell_2,r_1).
```

### Proposition PP3wk -- PROVED

The two diagonals

```text
state 0 = {a,b},
state 1 = {c,d}
```

use the same two left and two right resources. Hence each is a perfect matching
on those four resources, and switching between them preserves every row and
column margin.

For a resource-disjoint family of conflicts, the resulting rectangle supports
are pairwise resource-disjoint.

#### Proof

This is the standard alternating rectangle identity PP3ax. Resource-disjoint
conflicts use disjoint resource quadruples, so their rectangles are disjoint. ∎

State zero contains the original binary-shadow pair. State one avoids that pair
completely.

## 4. Safe opposite diagonals give a rectangle bank

### Proposition PP3wl -- PROVED

Suppose both opposite cells `c,d` of every rectangle in a selected subfamily lie
in the source-safe endpoint host. Then the state-one diagonals form a
resource-disjoint conflict-avoiding matching bank.

After fixing a residual matching on all unreserved resources, all remaining
no-three interactions among the rectangle choices are exact bad boxes of rank at
most three, and all insertion-shadow terms are exact unary/binary state costs.

#### Proof

PP3wk gives equal margins and resource disjointness. The selected state omits the
conflict pair `{a,b}`. Exact finite-state geometry and cost follow from
PP3om--PP3oq. ∎

The paid rectangle selection, cross-block amplification, and chromatic block
criteria therefore apply to this bank without a new matching formalism.

## 5. Unsafe opposite diagonals give unary structure

Suppose a rectangle has no source-safe opposite-diagonal state. Then at least one
of `c,d` is unary-forbidden or absent from the endpoint host. Choose one such
cell.

### Proposition PP3wm -- PROVED

Across a resource-disjoint conflict family, the chosen unsafe opposite cells use
pairwise distinct left and right resources. Hence they form a unary-forbidden
resource matching.

If a positive fraction of the conflict rectangles are unsafe, this matching has
the same growing order as the rectangle family and feeds directly into:

- endpoint-host Hall localization;
- hard-unary source-star/resource localization PP3wc--PP3wh;
- or the direct unary-support trade endpoints PP3kd--PP3kn.

#### Proof

Every chosen cell lies inside its conflict rectangle's four-resource support.
Those supports are pairwise disjoint by PP3wk. ∎

Thus failure of the safe rectangle state is itself a structured unary endpoint,
not a loss of the dual-packing information.

## 6. Revised linear-congestion binary endpoint

### Corollary PP3wn -- PROVED

A binary dual packing of value `Omega(q)` yields one of:

1. a polynomial endpoint-resource star of binary conflicts;
2. a polynomial resource-disjoint alternating-rectangle bank with safe
   conflict-avoiding states;
3. a polynomial unary-forbidden resource matching on opposite rectangle cells;
4. concentrated source geometry or insertion cost preventing paid installation
   of the safe rectangle states.

Therefore the linear-congestion dual packing is no longer an arbitrary
fractional object. Its resource-disjoint part rejoins the rectangle/cross-block
machinery, while its unsafe part rejoins the hard-unary star/resource branch.
The remaining original-binary obstruction is the high endpoint-resource star or
paid collateral on the extracted rectangle bank.