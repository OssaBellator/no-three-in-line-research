# Sharp three-matching Hall reserve threshold

`docs/616` treats two matching-shaped forbidden families in residual `K_{4,4}`.
A real conditional host may also have a matching-shaped host-defect family.  This
chapter gives the sharp reserve needed for three such families plus one arbitrary
blocked cell.

## 1. Six residual resources suffice

### Theorem PP3cwg -- PROVED / THREE-MATCHING RESERVE LEMMA

Let `L` and `R` have six vertices each.  Let

```text
F = M_partner union M_source union M_host union {e},
```

where each `M_*` is a partial matching and `e` is one arbitrary edge.  Then
`K_{6,6}-F` has a perfect matching.

#### Proof

Suppose not.  Hall gives `S subseteq L`, `|S|=s`, with
`|N(S)|<=s-1`.  Put `T=R\N(S)`.  Then

```text
|T| >= 6-s+1
```

and the complete rectangle `S x T` lies in `F`.

The union of three partial matchings has degree at most three.  Adding `e` can
raise the degree to four at only one left and one right vertex.  The minimum
Hall-rectangle dimensions are

```text
1x6, 2x5, 3x4, 4x3, 5x2, 6x1.
```

The first, second, fifth, and sixth require degree at least five somewhere.  A
`3x4` rectangle requires three left vertices of degree four, and a `4x3`
rectangle requires three right vertices of degree four.  Both exceed the single
exception supplied by `e`.  Contradiction.  ∎

## 2. Five residual resources are insufficient

### Theorem PP3cwh -- PROVED / SHARP FIVE-RESOURCE OBSTRUCTION

The six-resource conclusion is sharp.  In `K_{5,5}`, choose three left vertices
and three right vertices and forbid their complete `K_{3,3}`.  This forbidden
rectangle is the union of three perfect matchings on those triples.  The selected
three left vertices then have only the other two right vertices as neighbours,
so Hall fails.

#### Proof

Decompose `K_{3,3}` into the three cyclic matchings
`j=i`, `j=i+1`, and `j=i+2 mod 3`.  The displayed set of three left vertices has
neighbourhood size two in the complement.  ∎

## 3. Conditional-host consequence

### Theorem PP3cwi -- PROVED UNDER MATCHING-SHAPED RESTRICTIONS / EIGHT-RESOURCE CONDITION

After a local pair consumes two endpoint resources on each side, conditional
completion is guaranteed if:

1. at least six resources remain on each side;
2. the restricted partner fibre is a partial matching;
3. the restricted source exclusions are a partial matching;
4. the restricted host defects are a partial matching; and
5. at most one further residual cell is blocked.

Equivalently, this finite interface requires at least eight resources per side
before selecting the local pair.

The missing asymptotic statement is now precise: the superregular conditional
host must expose six unused resources and convert each of the three restricted
forbidden families into a partial matching.
