# Inherited-line state obstruction for boundary words

`docs/567` shows that locally legal band offsets need not compose.  This chapter
keeps the exact line history inherited by the next boundary block and determines
the complete bounded-offset path tree for the explicit side-four and side-seven
catalogue.

The block set and its four dihedral variants are those of `docs/561`.  Adjacent
offsets are restricted to `[-24,24]`, exactly as in `docs/567`.

## 1. Canonical inherited-line signature

### Theorem PP3cqp -- PROVED / EXACT LINE-HISTORY STATE

For a placed globally legal prefix with current block origin `o`, let

```text
Sigma(P,o)
```

be the set of primitive integer triples `(A,B,C)`, normalized up to sign, for
all lines

```text
A(x-o_x)+B(y-o_y)+C=0
```

determined by pairs of earlier selected points.  The state consisting of the
current block type and variant, its origin, the selected point set, and
`Sigma(P,o)` decides exactly whether any proposed next block creates a
collinear triple.

#### Proof

A new triple is either internal to the new block, already internal to the old
prefix, or consists of at least one new point and two points from the union.
The first two cases are excluded by the block and prefix hypotheses.  In the
remaining case, testing the new points against the exact pair-line set detects
the triple.  Primitive normalization loses no incidence information. ∎

## 2. Complete bounded-offset path census

### Theorem PP3cqq -- PROVED / FIVE-BLOCK EXTINCTION

For the explicit `P,Q` catalogue and offset radius twenty-four, the numbers of
globally legal placed words with one through five blocks are

```text
8, 282, 74, 4, 0.
```

The four length-four words are the two vertical reflections of

```text
P_1, P_1, P_1, P_1
```

with offset words

```text
(-24,10,-24), (24,-10,24).
```

All 306 possible adjacent-legal extensions of these four survivors create a
collinear triple.

#### Proof

Depth-first extension tests every edge from the exact 282-edge local seam graph.
At each step `PP3cqp` rejects precisely the extensions creating a new triple.
The finite counts and the complete failed extension scan are stored by the
checker. ∎

## 3. Signature growth and controller consequence

### Theorem PP3cqr -- PROVED / ADJACENT STATE IS INSUFFICIENT

The inherited line-signature sizes over the surviving prefixes have ranges

```text
one block:   28..91,
two blocks: 120..378,
three blocks: 276..435,
four blocks: 496.
```

Thus the four surviving four-block words contain thirty-two points and all
`binom(32,2)=496` pair lines are distinct.  No controller whose state records
only the last block and last offset can certify continuation of this catalogue
inside the tested radius.

#### Proof

No three selected points are collinear, so every point pair determines a
different line.  The four-block survivors have identical adjacent block data
throughout, yet all possible fifth steps fail because of inherited lines from
older blocks.  The omitted history is therefore essential. ∎

## 4. Exact diagnostic

Run

```bash
python scripts/check_boundary_inherited_line_states.py
```

The first failed fifth-block extension and its collinear triple are retained as
a reproducible obstruction witness.

## 5. Prime-patching consequence

The explicit four/seven catalogue cannot support a bounded-offset marker word
of five blocks.  Future boundary work must enlarge the offset range, change the
blocks, delete or replace seam points, or prove a compressed invariant for the
growing inherited line set.
