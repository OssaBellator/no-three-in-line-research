# Sharp three-matching Hall reserve threshold

`docs/616` treats two matching-shaped forbidden families in residual `K_{4,4}`.
A real conditional host may also have a matching-shaped host-defect family.  This
chapter combines a sharp six-resource completion theorem with two quantitative
ways to extract the required matching-shaped restrictions.

## 1. Six residual resources suffice, sharply

### Theorem PP3cwg -- PROVED / THREE-MATCHING RESERVE LEMMA

Let `L` and `R` have six vertices each.  Let

```text
F = M_partner union M_source union M_host union {e},
```

where each `M_*` is a partial matching and `e` is one arbitrary edge.  Then
`K_{6,6}-F` has a perfect matching.  Five residual resources are insufficient.

#### Proof

A Hall failure on six resources requires a complete forbidden rectangle of one
of the dimensions

```text
1x6, 2x5, 3x4, 4x3, 5x2, 6x1.
```

Three matchings have maximum degree three, and `e` raises the degree to four at
only one left and one right vertex.  The outer four rectangles require degree at
least five.  A `3x4` rectangle requires three left vertices of degree four, and
a `4x3` rectangle requires three right vertices of degree four.  None is
possible.

For sharpness, in `K_{5,5}` forbid a `K_{3,3}` decomposed into the three cyclic
perfect matchings.  Its three left vertices retain only the other two right
neighbours.  ∎

## 2. Reserve extraction from bad vertices

### Theorem PP3cwh -- PROVED / EXACT BAD-VERTEX FORMULA

Suppose a local pair has consumed two resources per side from a host with `m`
resources per side.  Let `b_L,b_R` be the numbers of remaining resources whose
degree exceeds one in any restricted partner, source, or host-defect family.
Then six good residual resources per side can be selected whenever

```text
m >= 8 + max(b_L,b_R).
```

#### Proof

There are `m-2` unused resources.  Removing all bad vertices leaves every
restriction of maximum degree at most one, hence a partial matching.  Six good
resources remain on each side exactly when

```text
m-2-b_L >= 6,
m-2-b_R >= 6.
```

These inequalities are equivalent to the displayed formula.  ∎

## 3. Reserve extraction from degree bounds

### Theorem PP3cwi -- PROVED / FORTY-FOUR-RESOURCE PIPELINE

For `k` forbidden families of maximum degree `Delta`, an `r`-resource reserve on
which every family is a partial matching exists whenever

```text
N >= r(1+2k*C(Delta,2))
```

unused resources remain per side.  In particular, for the three partner, source,
and host-defect families with degree at most two, forty-two residual resources
suffice to extract the sharp six-resource core.  Thus forty-four resources per
side before selecting the local pair suffice, and the core survives one further
blocked cell by `PP3cwg`.

#### Proof

On one side, join two resources when they share a neighbour in any forbidden
family.  The collision graph has at most `kN*C(Delta,2)` edges, so the standard
independence bound gives an independent set of size at least

```text
N/(1+2k*C(Delta,2)).
```

Choose `r` independent left resources and repeat on the right; independence makes
every restricted family a partial matching.  Substitute `k=3`, `r=6`,
`Delta=2`.  ∎

## Consequence

The Hall obligation is now numerical and sharp at the finite core.  The
asymptotic conditional host must either bound the union of bad vertices strongly
enough for `PP3cwh`, or provide degree at most two and forty-two residual
resources for `PP3cwi`.  Neither estimate is currently available, so the Hall
row remains unpromoted.
