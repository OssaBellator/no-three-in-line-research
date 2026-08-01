# Binary odd shell-column frontier

The recorded shell columns are

```text
A=(1,0,1), B=(1,1,0), C=(0,1,1),
```

and span the even-coordinate-sum lattice. This chapter audits the binary odd
columns and, more generally, every nonnegative odd column of `l_1` norm at most
three against the stored twenty-slot target `(12,10,8)`.

## 1. Complete binary odd catalogue

### Theorem PP3cwp -- PROVED / BINARY ODD-COLUMN CLASSIFICATION

The binary odd columns are exactly

```text
(1,0,0), (0,1,0), (0,0,1), (1,1,1).
```

Adding any one completes the parity quotient. In particular, the columns
`A,B,(1,1,1)` have determinant one, so the symmetric all-cycle action completes
the full integer service lattice.

#### Proof

Odd Hamming weight in three binary coordinates is one or three. Direct
determinant evaluation gives absolute determinant one for the displayed basis.
∎

## 2. Exact service frontier

### Theorem PP3cwq -- PROVED / TARGET-SERVICE OPTIMIZATION

For target service `(12,10,8)`, each unit odd column gives minimum sixteen active
controls. For

```text
D=(1,1,1),
```

the nondominated `(D uses,total active controls)` solutions are

```text
(2,14), (4,13), (6,12).
```

The last solution is

```text
2A + 4B + 0C + 6D = (12,10,8).
```

Among all thirteen feasible nonnegative odd columns of `l_1` norm at most three,
`D` is the unique column attaining twelve active controls. The recorded even-
column baseline needs fifteen controls.

#### Proof

Enumerate every candidate column, every positive use count, and all nonnegative
coefficients of `A,B,C`. Remove dominated use/cost pairs. ∎

## 3. Zero-buffer conditional schedule

### Theorem PP3cwr -- PROVED AS A CONDITIONAL TARGET / ZERO-RESERVE ALL-CYCLE WORD

The twenty-slot word

```text
DABABBBDDDDDIIIIIIII
```

uses counts `(A,B,C,D,I)=(2,4,0,6,8)`, gives exact target service, and satisfies
every coordinate service inequality at every prefix with startup buffer
`(0,0,0)`.

Thus a geometric clean macro realizing `D` would cross the missing lattice
coset, save three active controls per period, increase idle capacity from five to
eight, and remove the stored `2/5` startup reserve.

#### Proof

A finite count-state dynamic program retains only prefixes whose cumulative
service dominates the proportional target. It reconstructs the displayed word;
direct checking verifies all sixty prefix inequalities. ∎

No such all-cycle clean macro is present in the source catalogue. This identifies
the exact preferred missing action without promoting the shell row.
