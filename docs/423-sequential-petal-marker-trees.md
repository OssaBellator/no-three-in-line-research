# Sequential petal-marker trees and prefix-defect witnesses

`docs/417` shows that independent marker channels tensorize when their choices
can be viewed simultaneously.  A geometric repair word is more naturally built
sequentially: after each local move, only the surviving prefixes can be extended.
This chapter gives the exact tree formulation.  It preserves the product-degree
gain and localizes every failure to one short low-branching prefix.

The statements are general.  They do not construct the required prime-patching
marker words.

## 1. Sequential marker trees

For every source `x`, let `T_x` be a finite rooted tree of common depth `k`.
A node at depth `i-1` represents a surviving repair prefix after the first
`i-1` marker decisions.  Suppose every such node has at least

```text
q_i>=1
```

children.  Every leaf `ell` is mapped to a final clean target

```text
tau(x,ell).
```

Put

```text
Q=product_(i=1)^k q_i.
```

For a target `y`, define its leaf ambiguity

```text
A(y)=#{(x,ell):tau(x,ell)=y}.
```

### Theorem PP3bzh -- PROVED / SEQUENTIAL MARKER-TREE LOAD

If

```text
A(y)<=h
```

for every target, then the policy that chooses a leaf uniformly in `T_x`
has reverse-column load at most

```text
h/Q.
```

In particular, the optimum supported load satisfies

```text
lambda_*<=h/Q.
```

#### Proof

Every source tree has at least `Q` leaves.  The contribution of one source-leaf
pair to its target column is at most `1/Q`.  A target has at most `h` such
preimages, so its total column load is at most `h/Q`. ∎

Thus the multiplicative marker gain does not require simultaneous choices.  It
is enough that each surviving prefix has the prescribed number of extensions.

## 2. Safe-leaf conditioning

Let `G_x` be the leaves whose complete words pass all safety and cleanliness
tests.  Suppose

```text
|G_x|>=p |Leaves(T_x)|
```

for every source, where `p>0`.  Define the safe ambiguity

```text
A_G(y)=#{(x,ell):ell in G_x and tau(x,ell)=y}.
```

### Theorem PP3bzi -- PROVED / SAFE SEQUENTIAL MARKER CONDITIONING

If `A_G(y)<=h_G` for every target, then the policy uniform on `G_x` has load at
most

```text
h_G/(pQ).
```

Consequently strict contraction follows whenever

```text
h_G<pQ.
```

#### Proof

Each safe row has at least `pQ` leaves.  Every safe source-leaf pair contributes
at most `1/(pQ)` to its target, and at most `h_G` safe pairs reach one target. ∎

This is the sequential counterpart of the conditioning loss in `PP3byr`.

## 3. Prefix-defect localization

For one source, prune the tree to prefixes that extend to at least one safe
leaf.  Let

```text
N_i
```

be the number of surviving prefixes at depth `i`; thus `N_0=1` and
`N_k=|G_x|`.  For a surviving prefix `u` at depth `i-1`, let `b_i(u)` be the
number of its children that still extend to a safe leaf.

### Theorem PP3bzj -- PROVED / LOW-BRANCHING PREFIX WITNESS

Fix `0<p<=1`.  If

```text
|G_x|<pQ,
```

then for some level `i` and some surviving prefix `u` at depth `i-1`,

```text
b_i(u)<p^(1/k) q_i.
```

Equivalently, if every surviving prefix has at least

```text
p^(1/k) q_i
```

safe-extending children at level `i`, then `|G_x|>=pQ`.

#### Proof

If every surviving prefix at level `i-1` had at least
`p^(1/k)q_i` surviving children, then

```text
N_i>=p^(1/k)q_i N_(i-1).
```

Multiplying over all levels gives

```text
N_k>=p product_i q_i=pQ,
```

contrary to the hypothesis. ∎

A failed multimarker construction therefore produces a concrete short prefix
at which too many continuations die.  The next geometric audit can classify
those prefixes instead of treating safety loss as one opaque global density.

## 4. Revised boundary-recleaning frontier

The sunflower branch now has an executable three-part interface.

1. Build a short repair-prefix tree.
2. Prove a local extension count at every live prefix.
3. Bound the final tuple ambiguity, preferably by retaining one intrinsic petal
   marker.

If the product bound fails, `PP3bzj` identifies the first scale at which the
word construction loses the required branching.

## 5. Exact diagnostic

Run

```bash
python scripts/check_sequential_petal_marker_trees.py
```

The checker constructs exact three-level marker trees, verifies the sharp full
and conditioned loads, and checks every prefix-defect inequality by rational
arithmetic.

The next theorem identifier after this chapter is `PP3bzk`.
