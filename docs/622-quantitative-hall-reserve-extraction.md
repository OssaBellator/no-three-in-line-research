# Quantitative Hall reserve extraction

`docs/616` proves robust completion in residual `K_{4,4}` for two matching-shaped
forbidden families.  A real conditional host may also contribute a matching-
shaped host-defect family.  This chapter combines quantitative extraction with
the sharp reserve threshold for three families plus one arbitrary blocked cell.

## 1. Multi-family collision extraction

### Theorem PP3cwg -- PROVED / MATCHING-SHAPED RESERVE EXTRACTION

Let `F_1,...,F_k` be forbidden bipartite graphs on equal resource sets of size
`N`, each of maximum degree at most `Delta`.  Put

```text
b = C(Delta,2).
```

For any target reserve size `r`, if

```text
N >= r(1+2kb),
```

there are `r` left and `r` right resources on which every restricted `F_i` is a
partial matching.

#### Proof

On the left resources, join two vertices when they share a right neighbour in
some `F_i`.  There are at most `kNb` collision edges.  The standard independence
bound gives

```text
alpha >= N^2/(N+2kNb) = N/(1+2kb) >= r.
```

Choose `r` independent left resources.  On the right, join two vertices when
they occur in the same neighbourhood of one selected left resource in some
family.  There are at most `krb` collision edges, so

```text
alpha >= N^2/(N+2krb) >= r
```

under the same threshold.  Independence on both sides means no restricted
family repeats a left or right endpoint.  ∎

## 2. Sharp six-resource completion threshold

### Theorem PP3cwh -- PROVED / THREE-MATCHING HALL THRESHOLD

On six residual resources per side, the complement of

```text
M_partner union M_source union M_host union {e}
```

has a perfect matching whenever the three `M_*` are partial matchings and `e` is
one arbitrary edge.  Five residual resources are insufficient.

#### Proof

A Hall failure on six resources requires a complete forbidden rectangle of one
of the dimensions

```text
1x6, 2x5, 3x4, 4x3, 5x2, 6x1.
```

Three matchings have maximum degree three, and `e` can raise the degree to four
at only one left and one right vertex.  None of the six rectangles is possible:
the outer four require degree at least five, while `3x4` or `4x3` requires three
vertices of degree four on one side.

For sharpness, in `K_{5,5}` forbid a `K_{3,3}` decomposed into its three cyclic
perfect matchings.  The three selected left vertices then have only two
neighbours.  ∎

## 3. Numerical conditional-host pipeline

### Theorem PP3cwi -- PROVED UNDER DEGREE BOUNDS / FORTY-FOUR-RESOURCE PIPELINE

For three forbidden families of maximum degree two, forty-two residual resources
per side suffice to extract six resources on which all three restrictions are
partial matchings.  If two resources per side have already been consumed by the
local choice, forty-four available resources per side suffice before
conditioning.  The extracted core survives one further blocked cell.

#### Proof

In `PP3cwg`, take `k=3`, `r=6`, `Delta=2`, so `b=1` and

```text
N >= 6(1+6)=42.
```

Apply `PP3cwh` to the extracted six-by-six core.  ∎

## Consequence

The Hall obligation is now numerical and sharp at the finite core: prove a
residual pool of at least forty-two resources and degree at most two for the
partner, source, and host-defect families, or provide a better extraction using
more structure.  No asymptotic PP3 theorem currently supplies those estimates,
so the Hall row remains unpromoted.
