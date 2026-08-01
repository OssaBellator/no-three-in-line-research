# Binary odd shell-column frontier

The recorded shell columns and target service are

```text
A=(1,0,1), B=(1,1,0), C=(0,1,1),
T=(12,10,8).
```

They generate the even-coordinate-sum lattice.  This chapter searches every
nonnegative odd column of `l_1` norm at most three and audits its exact service
and prefix-buffer performance.

## 1. Unique optimal small odd column

### Theorem PP3cwp -- PROVED / ALL-CYCLE COLUMN OPTIMUM

Thirteen nonnegative odd columns of norm at most three participate in an exact
nonnegative service solution.  The unique column minimizing active controls is

```text
D=(1,1,1).
```

It completes the integer service lattice and gives

```text
2A+4B+6D=(12,10,8),
```

using twelve active controls and eight idle slots.  The recorded catalogue alone
needs fifteen active controls, with counts `(5,7,3)`.

#### Proof

Enumerate every odd candidate column of norm at most three, every positive use
count through twenty, and every nonnegative count of `A,B,C`.  Only `D` attains
twelve active controls.  The determinant of `A,B,D` has absolute value one.  ∎

## 2. Exact service frontier and zero buffer

### Theorem PP3cwq -- PROVED / PREFIX-FEASIBLE ZERO-RESERVE WORD

For the binary odd column `D`, the nondominated `(D uses,total active controls)`
frontier is

```text
(2,14), (4,13), (6,12).
```

The twenty-slot word

```text
DABABBBDDDDDIIIIIIII
```

uses counts `(A,B,C,D,I)=(2,4,0,6,8)`, gives exact target service, and satisfies
every coordinate service inequality at every prefix with startup buffer
`(0,0,0)`.

#### Proof

Exact coefficient enumeration gives the frontier.  A finite count-state dynamic
program retains only prefixes whose cumulative service dominates the
proportional target and reconstructs the displayed word.  Direct checking
verifies all sixty prefix inequalities.  ∎

## 3. Conditional shell improvement

### Theorem PP3cwr -- PROVED UNDER AN ALL-CYCLE CLEAN MACRO

A geometric clean macro with incidence `(1,1,1)` would:

- cross the missing parity coset;
- reduce active controls from fifteen to twelve per twenty slots;
- increase idle capacity from five to eight slots; and
- reduce the stored startup buffer from `2/5` to zero.

No such all-cycle clean macro is present in the source catalogue.  The exact
preferred action is identified, but its geometric realization and collateral
cost remain open.
