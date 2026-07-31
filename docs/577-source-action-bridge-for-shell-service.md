# Source-action bridge for shell service

`docs/523` begins with three unit service vectors.  `docs/571` derives canonical
`A/B/C` debt coordinates for the order-optimized period.  This chapter proves
that these are the same action coordinates and transfers the exact startup
certificates between the two shell stages.

## 1. Canonical incidence from the source actions

Let

```text
A=(1,0,0), B=(0,1,0), C=(0,0,1).
```

### Theorem PP3crb -- PROVED / SOURCE ACTION IDENTITY

The action-to-debt incidence matrix forced by the unit service definitions of
`docs/523` is the identity matrix.  In particular, the source action `A` is
exactly the canonical `A`-debt service vector used in `docs/571`.

#### Proof

Each named action supplies one unit to its own coordinate and zero to the other
two.  Writing these vectors as incidence rows gives the identity. ∎

## 2. Transfer of the phase certificate

### Theorem PP3crc -- PROVED / THREE-PERIOD SOURCE BRIDGE

For the source period `ABC` with target `(1/3,1/3,1/3)`, the three cyclic phases
have startup buffers

```text
(0,1/3,2/3),
(2/3,0,1/3),
(1/3,2/3,0).
```

These are exactly the buffers obtained in the canonical debt coordinates.

#### Proof

The coordinates and service vectors agree by `PP3crb`, so the prefix-deficit
formula is unchanged.  Direct evaluation gives the three vectors. ∎

## 3. Transfer to the optimized multiset

### Theorem PP3crd -- PROVED / ACTION-ALIGNED FIVE-PERIOD OPTIMUM

In the same coordinates, the multiset `A,A,B,B,C` has thirty distinct orders.
Ten attain minimum `l_1` startup reserve `6/5`; the lexicographic optimum
`ABABC` has buffer `(0,2/5,4/5)`.

#### Proof

Enumerate the multiset orders and apply the same prefix-deficit formula with
target `(2/5,2/5,1/5)`.  The action-level identity ensures that no extra
incidence assumption is introduced. ∎

## 4. Exact diagnostic

Run

```bash
python scripts/check_shell_source_action_bridge.py
```

## 5. Prime-patching consequence

The abstract periodic shell stages now share one source-derived action
coordinate system.  The unresolved step is to identify these three debts with
the actual clean-macro resources of the geometric construction.
