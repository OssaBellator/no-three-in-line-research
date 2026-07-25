# Transition middle projective covers

PP3aae shows that, after injective predecessor and successor designs are fixed,
every noncollision pair of local outer states is a clean five-index chain unless
its middle transition

```text
p -> c -> s
```

is blocked by a retained source anchor. The blocking relation is not arbitrary.
For one nonaxis retained anchor, the exact product equation defines a partial
matching between the predecessor-middle set and the successor-middle set.

Consequently a large no-chain product requires many distinct retained anchors.
The only exceptions are the at most two axis-degenerate anchors already isolated
in PP3zj; together they account for only `O(N)` middle pairs.

## 1. Anchor-coloured middle relations

Fix the endpoint pool coordinates

```text
(x_i,y_i),   i in V,
```

and a captive centre `c`. Let `P,S subseteq V\{c}` be predecessor and successor
middle sets.

For a retained source anchor `z=(u,v)`, define

```text
M_z={(p,s) in P x S:
     the inserted cells p->c and c->s are collinear with z}.
```

The exact factorization is

```text
(u-x_p)(v-y_s)=(u-x_c)(v-y_c).
```

Let `Z_nax` be the anchors for which the right-hand side is nonzero.

## 2. One nonaxis anchor colours a matching

### Proposition PP3aam -- PROVED

For every `z in Z_nax`, the bipartite graph `M_z` between `P` and `S` has maximum
degree at most one. Hence

```text
|M_z| <= min(|P|,|S|).
```

#### Proof

Fix `p`. Since the right-hand side is nonzero, `u!=x_p` for every pair in `M_z`,
and the factorization determines `y_s` uniquely. The pool has distinct old-row
coordinates, so at most one `s` works.

The transposed argument fixes `s` and determines `x_p` uniquely. ∎

Thus one retained nonaxis anchor colours a projective partial matching, not a
dense rectangle.

## 3. Axis-degenerate contribution

### Proposition PP3aan -- PROVED FROM PP3zj

The retained anchors with

```text
(u-x_c)(v-y_c)=0
```

contribute at most

```text
2N
```

ordered middle pairs in total.

#### Proof

This is the zero-product part of PP3zj. Saturation leaves at most the two relevant
axis anchors, and each determines at most one full row or one full column of the
middle relation, hence at most `N` pairs. ∎

## 4. Distinct-anchor lower bound

Let `E_mid` be a set of forbidden middle pairs after deleting index-collision
pairs. Assign each pair one retained source anchor witnessing it.

### Theorem PP3aao -- PROVED

The number of distinct nonaxis retained anchors used by `E_mid` is at least

```text
(|E_mid|-2N)_+ / min(|P|,|S|).
```

In particular, if every noncollision pair in `P x S` is forbidden, then the
number of distinct nonaxis anchors is at least

```text
(
 |P||S|-3(|P|+|S|)-2N
)_+
/
min(|P|,|S|).
```

#### Proof

Discard the at most `2N` axis-degenerate pairs from PP3aan. Every remaining
anchor class has size at most `min(|P|,|S|)` by PP3aam. Divide. The second display
uses the collision bound PP3aad. ∎

When `|P|` and `|S|` have the same order and their product dominates `N`, a
complete no-chain product therefore uses linearly many distinct retained anchors
at that order.

## 5. Slab-scale consequences

Recall

```text
N=m^(19/20+o(1)).
```

### Corollary PP3aap -- PROVED

Suppose

```text
|P|=m^(alpha+o(1)),
|S|=m^(beta+o(1)),
```

with `alpha<=beta`, `alpha+beta>19/20`, and no clean chain exists. If both choice
families admit injective designs, then at least

```text
m^(beta+o(1))
```

distinct nonaxis retained source anchors are required, unless the middle product
is already reduced by the collision or axis terms.

In the balanced square-root case

```text
|P|,|S|=m^(1/2+o(1)),
```

the no-chain core requires

```text
m^(1/2+o(1))
```

distinct nonaxis retained anchors.

#### Proof

The numerator in PP3aao has order `m^(alpha+beta)` because this exponent exceeds
`19/20`, while the denominator has order `m^alpha`. ∎

## 6. Revised no-chain endpoint

A large no-chain middle product now has one of the following exact forms.

1. **Projective anchor cover:** many distinct retained source anchors, each
   colouring a partial matching between `P` and `S`.
2. **Axis degeneration:** one of at most two axis anchors contributes a single
   full row or column, with total support `O(N)`.
3. **Choice Hall concentration:** one outer choice family fails the injective
   extraction and returns to the matching-star alternative PP3aah.
4. **Small state side:** one of `P,S` has the square-root or smaller size forced by
   PP3aaf.
5. **Clean-chain paid branch:** a nonforbidden noncollision pair exists and PP3zu
   selects its residual single-cycle completion.

The middle transition obstruction is therefore a projective matching cover by a
large retained-anchor bank, not a generic dense relation. Its next conversion may
use source-anchor removal credit, a resource-disjoint anchor extraction, or the
existing paid star/resource machinery.
