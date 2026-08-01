# Binary odd shell-column frontier

The recorded shell columns are

```text
A=(1,0,1), B=(1,1,0), C=(0,1,1),
```

and span the even-coordinate-sum lattice.  This chapter audits every nonzero
binary column of odd coordinate sum as a candidate new clean-macro action.

## 1. Complete binary odd catalogue

### Theorem PP3cwp -- PROVED / BINARY ODD-COLUMN CLASSIFICATION

The binary odd columns are exactly

```text
(1,0,0), (0,1,0), (0,0,1), (1,1,1).
```

Adding any one completes the parity quotient.  In particular, the columns
`A,B,(1,1,1)` have determinant one, so the symmetric all-cycles action completes
the full integer service lattice.

#### Proof

Odd Hamming weight in three binary coordinates is one or three.  Direct
determinant evaluation gives absolute determinant one for the displayed basis.
∎

## 2. Exact service frontier

### Theorem PP3cwq -- PROVED / TARGET-SERVICE OPTIMIZATION

For target cycle service `(12,10,8)`, each unit odd column requires at least two
uses and gives minimum sixteen active controls.  For

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

The recorded even-column baseline uses fifteen controls, so a unit-cost `D`
action can improve throughput by three controls per twenty-slot target period.

#### Proof

Enumerate all nonnegative integer coefficients of `A,B,C,D` that equal the target
and remove dominated use/cost pairs.  ∎

## 3. Geometric target

### Theorem PP3cwr -- PROVED AS A CONDITIONAL TARGET / SYMMETRIC ODD ACTION

Among binary odd columns, `(1,1,1)` is the unique throughput-improving candidate
for the stored target.  A geometric clean macro realizing it would both cross
the missing lattice coset and improve the unit-cost service count.

No such macro is currently present in the source catalogue, and its startup
buffer and collateral costs have not been audited.  The result therefore
identifies the exact next shell action rather than promoting the shell row.
