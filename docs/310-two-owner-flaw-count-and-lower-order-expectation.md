# Two-owner Hamilton flaws are a lower-order exceptional family

The complete targeting theorem in `docs/307` splits bad triples into two-owner
and three-owner flaws.  This chapter counts the two-owner atomic family.  It is
large enough to create genuine targetability gaps for the support-three kernel,
but asymptotically smaller than the generic three-owner family.

Write `n=2m` and `J(x)=n-1-x`.

## 1. Explicit orbit coordinates

For a signed pair assignment from source pair `i` to target pair `j`, the two
orientation values select

```text
O_0(i,j) = {
  (i,j), (Ji,Jj), (Jj,i), (j,Ji)
},

O_1(i,j) = {
  (i,Jj), (Ji,j), (j,i), (Jj,Ji)
}.
```

### Proposition PP3bkm -- PROVED

For fixed source pair `i`, fixed orientation, and one fixed cell role in the
four-point orbit, varying the target pair `j` moves that cell on one horizontal
or vertical grid line.  The same statement holds with source and target roles
interchanged.

#### Proof

Inspect the displayed coordinates.  In every cell role, one coordinate is one
of `i,Ji` and is fixed, while the other is one of `j,Jj` and varies.  Or the two
coordinate roles are exchanged. ∎

## 2. Cubic count of atomic two-owner flaws

Let `F_2(m)` be the number of compatible atomic two-owner collinear-triple flaws
in the signed Hamilton probability space.  The atomic flaw records its two
signed pair assignments as in `docs/309`.

### Theorem PP3bkn -- PROVED

For every `m>=4`,

```text
F_2(m) <= 96 m^2(m-1) <= 96m^3.
```

#### Proof

In a two-owner triple, one owner contributes two cells and is therefore
uniquely designated as the repeated owner.

Choose its signed assignment in at most

```text
2m(m-1)
```

ways: source pair, distinct target pair, and orientation.  Choose the two cells
from its four-cell orbit in at most `C(4,2)=6` ways.  They determine a line `L`.

A compatible flaw cannot use a horizontal or vertical `L`, because every signed
Hamilton selected set has exactly two cells in each row and column.  Thus `L`
is nonaxis.

Choose the singleton owner's source pair in `m` ways and choose one of its eight
signed cell roles: two orientations times four orbit positions.  By PP3bkm,
as its target varies that cell moves along one axis-parallel line.  A nonaxis
line `L` intersects that parameter line in at most one point, so at most one
target pair can complete the collinearity.

Multiplication gives

```text
2m(m-1) * 6 * m * 8 = 96m^2(m-1).
```

Matching, nonloop, Hamilton-cycle, and target-uniqueness requirements only
remove choices. ∎

The bound is intentionally elementary and not optimized.

## 3. Linear expected count

### Corollary PP3bko -- PROVED

Under the uniform signed Hamilton measure, the expected number `Z_2` of atomic
two-owner bad triples satisfies

```text
E Z_2 <= 48m = 24n.
```

In particular,

```text
E Z_2 = O(n).
```

#### Proof

Every compatible two-owner atomic flaw has probability

```text
p_2(m)=1/[4(m-1)(m-2)]
```

by PP3bki.  Hence PP3bkn gives

```text
E Z_2
 <= 96m^2(m-1) / [4(m-1)(m-2)]
 = 24m^2/(m-2)
 <= 48m
```

for `m>=4`. ∎

## 4. Defect-scale decomposition

### Corollary PP3bkp -- PROVED / FRONTIER REFINED

The `Theta(n log n)` expected-defect barrier in the uniform signed Hamilton
measure is not caused by two-owner flaws.  Those contribute only `O(n)` in
expectation.  The logarithmic factor is carried by the strongly generic
three-owner family from PP3bje.

#### Proof

PP3bko gives the two-owner upper bound.  PP3bje gives `Theta(n log n)` expected
strongly generic three-owner triples. ∎

This separation matches the repair architecture:

```text
two-owner exceptional flaws: support-one orientation flips;
three-owner generic flaws:    support-three successor rotations.
```

The finite atomic-flaw audit records the exact two-owner flaw counts

```text
m=4: 16,
m=5: 144,
m=6: 256,
```

all far below the cubic bound.  The next asymptotic bottleneck is therefore the
collateral behavior and causal structure of the three-owner rotations, not the
existence or abundance of a repair for two-owner flaws.
