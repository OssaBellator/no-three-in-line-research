# Side-twelve all-transposition affine-column obstruction

PX970--PX972 close the complete affine-column recursive subfamily at produced
base side ten. The other principal produced base is side twelve, obtained by the
factor-independent `2 x 6 -> 12` theorem PX60. Any rectangle-state decomposition
of a recursive output again has all-transposition relative type, now

\[
(2,2,2,2,2,2).
\]

This chapter closes the corresponding affine-column `12 -> 24` target while
allowing arbitrary row labeling and arbitrary spanning degree-two selection.

## 1. Search family

Use

\[
H_{2^6}=(1,0,3,2,5,4,7,6,9,8,11,10)
\]

and the affine group on `Z/12Z`,

\[
A_{12}
=
\{x\mapsto ax+b\pmod {12}:
  a\in\{1,5,7,11\},\ b\in\mathbb Z/12\mathbb Z\}.
\]

It has order `48`. For each orientation and each pair

\[
(T,Q)\in A_{12}^2,
\]

the row-pattern search absorbs every `P in S_12` and enumerates every spanning
degree-two selector exactly. Thus the census contains

\[
4\cdot48^2=\boxed{9216}
\]

column geometries.

## 2. Complete exact census

### Theorem PX973 -- PROVED FINITE

No affine-column geometry for the side-twelve all-transposition relative class
contains a no-three spanning degree-two state, even when `P` and the selector are
arbitrary.

The deterministic node census is:

| Orientation | `(T,Q)` pairs | Search nodes | Maximum nodes in one geometry |
|---|---:|---:|---:|
| `cc` | 2,304 | 30,052,757 | 215,309 |
| `cf` | 2,304 | 56,638,188 | 323,178 |
| `fc` | 2,304 | 30,488,889 | 259,065 |
| `ff` | 2,304 | 58,535,712 | 405,180 |
| **Total** | **9,216** | **175,715,546** | **405,180** |

### Proof

Apply the generic exact row-pattern solver PX972 with base `n=12`. For fixed
`(T,Q,theta)`, the first twelve scalar rows have fixed abstract patterns. The
remaining twelve rows receive the unused patterns in arbitrary order, exactly
representing every `P`. Each row chooses two of its four incident columns.

The solver maintains column degrees, rejects exactly on zero integer
determinants, and prunes only when the remaining fixed rows and unused patterns
cannot fill some column to degree two. A depth-24 leaf is accepted only when all
24 columns have degree two. Every affine pair is searched in one of twenty-four
contiguous 96-pair intervals in each orientation. The displayed sums and maxima
combine all intervals without overlap. No interval produces `FOUND`. \(\square\)

## 3. Produced-base recursion boundary

### Corollary PX974 -- PROVED REDUCTION

Neither of the two largest currently produced exact bases, side ten and side
twelve, can be recursively doubled in the all-transposition class by keeping
both column labelings affine and placing all nonlinearity in `P` or the selector.

Specifically:

- PX970 rules out the affine-column `10 -> 20` target;
- PX973 rules out the affine-column `12 -> 24` target.

Therefore a produced-base iteration theorem must introduce genuinely non-affine
column structure, a larger map group with useful non-affine double cosets, or the
general repair/resampling mechanism.

### Proof

Both targets lie in the all-transposition class by PX65. The row-pattern searches
already include every row permutation and every selector, so after PX970 and
PX973 the only fixed-template degrees of freedom not exhausted are non-affine
column labelings or a larger structured family. The low-syndrome repair route is
the remaining non-template alternative. \(\square\)

## 4. Computational comparison

### Corollary PX975 -- PROVED FINITE OBSERVATION

The complete affine-column side-twelve census uses `175,715,546` search nodes,
only about `1.06` times the side-ten total `165,874,408`, despite the larger row
assignment and selector spaces. Thus the row-pattern normal form continues to
control the factorial `P` degree of freedom effectively at side twelve.

This observation supports broader structured-map censuses, but it does not imply
that arbitrary non-affine column searches are feasible.

## 5. Verification

```bash
python scripts/verify_product_transposition_class_twelve.py
```

The verifier compiles the generic solver, partitions each orientation into
exact 96-pair intervals, rejects any constructive output, and asserts all four
aggregate node totals and maxima.
