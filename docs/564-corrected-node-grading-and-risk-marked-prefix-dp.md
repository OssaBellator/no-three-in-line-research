# Dual grading and risk-marked prefix dynamic program

The prefix-tree chapters use the eliminated equation

```text
T=z(1+T+uT^2).
```

This equation has two compatible combinatorial readings.  In the original
automaton system, `z` marks leaves of a legal full binary tree.  In the
factorized equation, `z` marks total nodes of a unary-binary encoding.  The
encoding is size-preserving: original leaves equal encoded nodes.  This chapter
records that reconciliation and adds one independently enumerated structural
risk coordinate on the encoding.

## 1. Dual grading reconciliation

### Theorem PP3cpo -- PROVED / ORIGINAL-LEAF AND ENCODED-NODE GRADING

The original leaf grading in `docs/528` is valid.  The object `U(L)` is an
encoded unary-binary tree with two encoded nodes and one encoded leaf; under the
elimination bijection it represents an original legal tree with two leaves.
Thus

```text
original leaves = encoded total nodes,
```

while encoded leaves are a different statistic.

#### Proof

The pre-elimination automaton equation contributes `z` exactly at an original
leaf and multiplies child series at an internal binary node.  Elimination yields
`z+zT+zT^2`; its three terms define encoded leaf, unary, and binary constructors.
Each encoded constructor contributes the one exposed original leaf represented
by its factor `z`, so induction proves the size identity. ∎

## 2. Encoded profile interpretation

### Theorem PP3cpp -- PROVED / SIZE-PRESERVING UNARY-BINARY PROFILE

Let `n` be original leaves, equivalently encoded total nodes, and let `j` be
encoded binary nodes.  Then

```text
encoded unary nodes = n-1-2j,
encoded leaves      = j+1,
```

and the exact profile coefficient is

```text
c_(n,j)=(n-1)!/((n-1-2j)! j! (j+1)!).
```

All coefficient formulas, ratio identities, and Gaussian profile results remain
valid with this dual interpretation.

#### Proof

In a rooted unary-binary encoding, the edge count is both `n-1` and `a+2j`, and
degree balance gives one more encoded leaf than binary node.  Lagrange inversion
counts the same encoded class, while `PP3cpo` identifies its size with original
leaf count. ∎

## 3. Exact unary-run risk recurrence

### Theorem PP3cpq -- PROVED / PROFILE-SLICED ENCODED UNARY-RUN RISK DP

Mark each edge joining an encoded unary parent to an encoded unary child as one
unit of structural risk.  A finite dynamic program indexed by

```text
(encoded total nodes, encoded binary nodes, root type, risk)
```

counts the exact risk distribution and reconstructs a deterministic witness.

For original leaf count and encoded total size `30`, with `9` encoded binary
nodes, the family size is

```text
168212023980.
```

The exact risk distribution for risks zero through ten is

```text
367479684,
4491418360,
20211382620,
44097562080,
51447155760,
33242777568,
11872420560,
2261413440,
212007510,
8314020,
92378.
```

Its aggregate risk is `638045608200`, so the exact mean is `110/29`.  At least
`153857776072` objects have risk at most five, and the checker reconstructs an
explicit risk-zero encoding with thirty nodes, nine binary nodes, eleven unary
nodes, and ten encoded leaves.

#### Proof

An encoded leaf initializes the table.  Adding an encoded unary root increments
risk precisely when its child root is unary.  Adding an encoded binary root
convolves two ordered child tables.  The constructors are disjoint and exhaustive,
so coefficient induction proves exactness.  Stored predecessors give a witness. ∎

## 4. Stored exact audit

Run

```bash
python scripts/check_node_graded_prefix_risk_dp.py
```

The checker verifies the dual grading, profile mass, full risk distribution,
aggregate moment, and reconstructed witness.

## 5. Prime-patching consequence

The prefix frontier has one genuinely reconstructed structural risk total on the
size-preserving encoding.  It is not yet the geometric support/source risk needed
by the patch.  The exact DP, profile cross-check, and witness extraction supply
the mechanism for adding true risk coordinates once their typed geometric
definitions are available.
