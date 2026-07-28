# Pair-safe frustration strict descent through `m=9`

`docs/326` defines the cycle frustration index `lambda(rho)` as the minimum
number of violated one-XOR owner-pair constraints over all orientation vectors
on a pair-safe Hamilton cycle `rho`.  This chapter audits whether successor
rotations can decrease that cycle-level potential while retaining pair safety.

The result is finite and reoptimizes the complete orientation vector after each
cycle move.  No asymptotic local action, charge bound, or no-three seed theorem
is claimed.

## 1. Pair-safe successor graph

The vertices are pair-safe directed Hamilton cycles on `m` owners.  For every
three-owner source set `T`, rotate the three outgoing targets in cyclic order as
in PP3bjg.  Retain the directed edge

```text
rho -> rho^T
```

only when the target cycle is also pair-safe.

The potential on this graph is

```text
lambda(rho)
 = minimum number of violated signed parity edges over all orientations.
```

A strict-descent rotation satisfies

```text
lambda(rho^T) < lambda(rho).
```

## 2. Exact one-step descent

### Theorem PP3bni -- VERIFIED FINITELY / ONE-STEP STRICT DESCENT

For every `5<=m<=9`, every pair-safe Hamilton cycle with positive frustration
index has a pair-safe successor rotation of strictly smaller frustration index.
Thus the maximum distance to a lower `lambda` level is exactly one on every
positive level in the audited range.

The exact directed counts are:

| `m` | pair-safe cycles | positive-`lambda` cycles | pair-safe rotations | strict-descent rotations | minimum descents from one positive cycle |
|---:|---:|---:|---:|---:|---:|
| 5 | 24 | 2 | 240 | 20 | 10 |
| 6 | 120 | 8 | 2,400 | 148 | 18 |
| 7 | 720 | 56 | 25,200 | 1,624 | 25 |
| 8 | 4,560 | 1,018 | 239,040 | 34,102 | 19 |
| 9 | 37,440 | 5,752 | 3,009,600 | 292,584 | 28 |

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_parity_frustration_descent.cpp \
  -o /tmp/check_hamilton_parity_frustration_descent
/tmp/check_hamilton_parity_frustration_descent
```

The checker reconstructs every Hamilton cycle, its exact geometric pair
relations, and its frustration index.  It enumerates every successor rotation,
keeps pair-safe targets, and checks that every positive-frustration source has
an immediate lower target.  All counts are compared with hard-coded regression
values. ∎

The large minimum number of descending choices is finite evidence of robust
cycle-level mobility, but the table does not imply a positive asymptotic
density of useful rotations.

## 3. Every optimal violated edge can be targeted

Fix an orientation attaining `lambda(rho)`.  A violated signed edge `uv` is an
owner pair using its unique forbidden relative parity.

### Theorem PP3bnj -- VERIFIED FINITELY / TARGETED CORE EDGE DESCENT

For every `5<=m<=9`, every pair-safe cycle `rho`, every orientation attaining
`lambda(rho)>0`, and every parity edge violated by that orientation, there is a
strict-descent pair-safe successor rotation whose source triple contains `u` or
`v`.

Hence the move changes at least one directed assignment supporting the selected
violated owner-pair constraint.  The minimum number of such targeted descending
rotations over all audited choices is:

| `m` | optimal violated-edge checks | minimum targeted descents |
|---:|---:|---:|
| 5 | 48 | 9 |
| 6 | 272 | 14 |
| 7 | 2,752 | 20 |
| 8 | 97,224 | 13 |
| 9 | 1,001,344 | 19 |

#### Verification

For every minimum orientation, the checker lists its violated parity edges.
For each edge it filters the strict-descent rotations to source triples meeting
an endpoint and verifies that the filtered set is nonempty.  The displayed
minimum and total check counts are stored in
`experiments/hamilton-parity-frustration-descent-audit.json`. ∎

This is stronger than an untargeted cycle-level descent statement: no optimal
violated edge is forced to remain untouched in the finite range.

## 4. Finite cycle-coordinate termination

### Corollary PP3bnk -- VERIFIED FINITELY / REOPTIMIZED TERMINATION

For `m<=9`, start from a pair-safe Hamilton cycle and repeatedly choose a
strict-descent rotation from PP3bni, reoptimizing the orientation vector after
each move.  The process reaches a parity-satisfiable pair-safe cycle in at most

```text
lambda(rho_0)
```

moves.  By PP3bng this is at most three moves through `m=9`.

#### Proof

The nonnegative integer `lambda` decreases by at least one at each step.  The
finite maximum is three by the exact frustration audit. ∎

The reoptimization clause is essential.  The corollary does not construct a
bounded-Hamming orientation update, preserve a chosen clean fibre measure, or
control predecessor charge.

## 5. Revised frustration frontier

The finite cycle graph has no positive-frustration local minimum through
`m=9`, and every edge of every minimum frustration core can be hit by a
descending move.  The next tasks are now sharply separated:

1. prove an asymptotic pair-safe strict-descent theorem for `lambda`;
2. couple a descending cycle rotation to exact fibre regeneration or a bounded
   sign update without losing the descent;
3. bound merged predecessor charge for a distribution over the many descending
   rotations;
4. show that targeting one violated owner pair also decreases an atomic
   three-owner flaw potential after collateral is included;
5. determine whether the minimum number of descending rotations remains
   polynomially large or can collapse at larger `m`.

The finite one-step theorem is evidence for these interfaces, not a substitute
for them.