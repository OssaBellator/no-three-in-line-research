# Triadic shell odd-action target

The recorded shell actions are

```text
x1=(1,0,1), x2=(1,1,0), x3=(0,1,1).
```

They are exactly the vertex-incidence columns of the three edges of a triangle.
This interpretation identifies the geometric type of operation required to
escape the index-two lattice.

## 1. Pair-supported parity

### Theorem PP3cwp -- PROVED / HANDSHAKE PARITY FOR PAIR-SUPPORTED SHELL MOVES

Every signed composition of pair-supported cycle actions has even total
coordinate sum.

#### Proof

Each pair-supported action is an edge-incidence vector and therefore has two
unit incidences.  A signed integer combination has total coordinate sum twice
the signed edge multiplicity.  Equivalently, the recorded incidence matrix has
determinant two and image equal to the even-sum lattice. ∎

## 2. Smallest positive odd primitive

### Theorem PP3cwq -- PROVED / TRIADIC ALL-CYCLE COLUMN

Among binary nonnegative odd columns, the only possibilities are the three unit
vectors and

```text
u=(1,1,1).
```

The coordinatewise-positive choice `u` serves the stored target `(12,10,8)` with
only twelve active controls:

```text
2 x1 + 4 x2 + 0 x3 + 6 u = (12,10,8).
```

By comparison, any unit odd column needs sixteen active controls in its best
nonnegative exact service.

#### Proof

Enumerate the four binary odd vectors.  Invert the recorded incidence matrix for
each possible positive odd-action count and retain nonnegative integer action
counts.  The displayed solution is optimal for `u`; each unit-vector optimum is
sixteen. ∎

## 3. Geometric source obligation

### Theorem PP3cwr -- PROVED / ODD ACTION MUST BE VERTEX-UNPAIRED OR TRIADIC

No operation assembled solely from pair-supported clean-macro incidences can
realize `u`.  Any realization must introduce an unpaired cycle endpoint or one
primitive simultaneously incident with all three cycle resources.

#### Proof

`u` has odd coordinate sum, contradicting `PP3cwp` for every pair-supported
composition. ∎

## Consequence

The preferred missing shell primitive is now explicit: an all-cycle triadic
operation, not another pairwise attenuation column.  Its arithmetic would improve
the stored fifteen-control service to twelve controls, but no geometric
clean-macro realization is known.
