# Optimal small all-cycle odd shell column

The recorded shell columns generate the even-sum lattice.  Earlier work tested a
unit odd column, which repaired the lattice but increased active controls and did
not reduce startup buffer.  This chapter searches all nonnegative odd columns of
`l_1` norm at most three against the exact twenty-slot target.

The recorded columns and target service are

```text
A=(1,0,1), B=(1,1,0), C=(0,1,1),
T=(12,10,8).
```

## 1. Unique optimal small odd column

### Theorem PP3cwp — PROVED / ALL-CYCLE COLUMN OPTIMUM

Among every nonnegative odd-sum column `D` with `||D||_1<=3` that participates in
an exact nonnegative service solution, the unique column minimizing the number of
active controls is

```text
D=(1,1,1).
```

It gives the exact service identity

```text
2A + 4B + 6D = (12,10,8),
```

using twelve active controls and eight idle slots.  The recorded catalogue alone
needs fifteen active controls, with counts `(5,7,3)`.

#### Proof

The checker enumerates every candidate column, every positive number of uses up
to twenty, and every feasible count of the recorded controls.  Thirteen small odd
columns admit exact service; only `(1,1,1)` attains twelve active controls. ∎

## 2. Zero-buffer schedule

### Theorem PP3cwq — PROVED / PREFIX-FEASIBLE ZERO-RESERVE WORD

The twenty-slot word

```text
DABABBBDDDDDIIIIIIII
```

has the required counts and satisfies every coordinate service inequality at
every prefix with startup buffer `(0,0,0)`.

#### Proof

A finite count-state dynamic program searches only transitions whose cumulative
service dominates the scaled prefix target.  It reconstructs the displayed word,
and direct prefix checking verifies all sixty coordinate inequalities. ∎

## 3. Conditional shell improvement

### Theorem PP3cwr — PROVED UNDER AN ALL-CYCLE CLEAN MACRO

A geometric clean macro with incidence column `(1,1,1)` would simultaneously:

- cross the missing parity coset;
- reduce active controls from fifteen to twelve per twenty slots;
- increase idle capacity from five to eight slots;
- reduce the minimum startup buffer from `2/5` to zero.

#### Proof

Combine `PP3cwp`, `PP3cwq`, and the stored baseline certificate of `docs/517`. ∎

## Remaining source obligation

No recorded geometric clean-macro operation services all three cycle coordinates
once.  The search identifies a sharper source target than a unit odd column, but
does not realize it.
