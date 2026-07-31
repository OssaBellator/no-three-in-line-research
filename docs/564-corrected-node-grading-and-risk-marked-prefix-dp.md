# Corrected node grading and risk-marked prefix dynamic program

The prefix-tree chapters use

```text
T=z(1+T+uT^2).
```

They repeatedly describe `z` as marking leaves.  That interpretation is not
compatible with the recurrence: every root, including a unary or binary root,
contributes one factor of `z`.  This chapter corrects the grading and then adds
one independently enumerated structural risk coordinate.

## 1. Leaf grading is false

### Theorem PP3cpo -- REFUTED / LEAF-GRADED INTERPRETATION

In `T=z(1+T+uT^2)`, the variable `z` does not mark leaves.  The object `U(L)`—a
unary root over one leaf—has `z`-degree two but only one leaf.

#### Proof

The leaf contributes the outer `z` in the constant term.  Applying the unary
constructor multiplies by another `z`, producing degree two without adding a
leaf. ∎

Thus the word “leaves” in the size interpretations of `docs/528`, `docs/534`,
and `docs/540` must be replaced by “total nodes”.

## 2. Corrected profile interpretation

### Theorem PP3cpp -- PROVED / NODE-GRADED UNARY-BINARY PROFILE

Let `n` be total nodes and `j` binary nodes.  Then

```text
a=n-1-2j
```

is the number of unary nodes, the number of leaves is `j+1`, and the exact
profile coefficient remains

```text
c_(n,j)=(n-1)!/(a! j! (j+1)!).
```

All coefficient formulas, ratio identities, and Gaussian profile results remain
valid after this grading correction, with `n` interpreted as total nodes.

#### Proof

In a rooted unary-binary tree, the edge count is both `n-1` and
`a+2j`, giving the first relation.  The standard degree balance gives one more
leaf than binary node.  Lagrange inversion counts the same node-graded class and
therefore gives the displayed coefficient. ∎

## 3. Exact unary-run risk recurrence

### Theorem PP3cpq -- PROVED / PROFILE-SLICED UNARY-RUN RISK DP

Mark each edge joining a unary parent to a unary child as one unit of structural
risk.  A finite dynamic program indexed by

```text
(total nodes, binary nodes, root type, risk)
```

counts the exact risk distribution and reconstructs a deterministic witness.

For total size `30` and `9` binary nodes, the family size is

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
explicit risk-zero tree with thirty total nodes, nine binary nodes, eleven unary
nodes, and ten leaves.

#### Proof

A leaf initializes the table.  Adding a unary root preserves leaf and binary
counts, increments total nodes and unary count, and adds one risk precisely when
the child root is unary.  Adding a binary root convolves two ordered child
tables and adds one binary node.  These constructors are disjoint and exhaustive,
so coefficient induction proves exactness.  Stored predecessor choices give a
witness. ∎

## 4. Stored exact audit

Run

```bash
python scripts/check_node_graded_prefix_risk_dp.py
```

The checker verifies the grading counterexample, the corrected profile mass, the
full risk distribution, its aggregate moment, and the reconstructed witness.

## 5. Prime-patching consequence

The prefix frontier now has one genuinely reconstructed aggregate risk total,
rather than a stipulated multiplier.  It is a structural unary-run risk, not yet
the geometric support/source risk needed by the patch.  Nevertheless the exact
DP, profile cross-check, and witness extraction supply the required mechanism for
adding the true risk coordinates once their local definitions are available.
