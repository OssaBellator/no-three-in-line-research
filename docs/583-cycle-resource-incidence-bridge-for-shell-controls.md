# Cycle-resource incidence bridge for shell controls

`docs/577` aligned the abstract source actions `A,B,C` with canonical unit debt
coordinates.  The earlier shell schedule in `docs/517` uses three actual stored
cycle inequalities rather than identity resources.  This chapter derives the
exact incidence map between those descriptions.

The cycle requirements are

```text
x1+x2 >= 3/5,
x2+x3 >= 1/2,
x3+x1 >= 2/5.
```

## 1. Source action to cycle-resource map

### Theorem PP3crt -- PROVED / FULL-RANK SHELL INCIDENCE

In cycle coordinates, the three unit source actions have service vectors

```text
x1 -> (1,0,1),
x2 -> (1,1,0),
x3 -> (0,1,1).
```

Thus the action-to-cycle incidence matrix is

```text
H=((1,1,0),
   (0,1,1),
   (1,0,1)),
```

with determinant two.  The map is full rank.

#### Proof

Each column records exactly which of the three displayed inequalities contains
the corresponding control variable.  Direct determinant evaluation gives two. ∎

## 2. Twenty-slot schedule bridge

### Theorem PP3cru -- PROVED / STORED BUFFER TRANSFER

For the stored period

```text
213121212122233IIIII,
```

the maximum cycle deficits are `(0,0,2/5)`.  The action-coordinate startup
buffer `(2/5,0,0)` maps through `H` to the cycle reserve

```text
(2/5,0,2/5),
```

which covers every deficit and reproduces the all-prefix certificate of
`docs/517`.

#### Proof

The checker accumulates the three action counts at every prefix, applies `H`, and
subtracts the target rates.  Matrix multiplication gives the mapped buffer. ∎

## 3. Three-slot phase table in cycle coordinates

### Theorem PP3crv -- PROVED / PHASE-BUFFER CONJUGACY

For the period containing one copy of each source action, the cycle target is
`(2/3,2/3,2/3)`.  The three cyclic phases have exact cycle-prefix buffers

```text
(0,2/3,1/3),
(1/3,0,2/3),
(2/3,1/3,0).
```

Hence the canonical action model and the stored cycle model are related by one
explicit source-derived incidence map, not by an arbitrary fixture.

#### Proof

Apply `H` to the three phased source-action words and evaluate the finite prefix
deficit formula. ∎

## 4. Exact audit and remaining gap

Run

```bash
python scripts/check_shell_cycle_resource_bridge.py
```

The bridge is exact for the stored `docs/517` cycle system.  Those cycle
inequalities are still not identified with coordinate-level clean-macro shell
resources of the eventual prime-patching construction.
