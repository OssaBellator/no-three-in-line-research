# Prefix dual grading and the geometric-risk interface

`docs/564` treated the factorized equation

```text
T=z(1+T+uT^2)
```

as if its node-graded interpretation invalidated the leaf grading in the original
automaton system.  That conclusion is too strong.  The equation has two
compatible interpretations connected by a size-preserving encoding.  This
chapter reconciles them and retains the exact structural-risk dynamic program.

## 1. Original leaf grading remains valid

### Theorem PP3cqg -- PROVED / DUAL GRADING RECONCILIATION

In the original automaton equations of `docs/528`, `z` marks leaves of the legal
full binary tree.  After elimination, the same equation is the ordinary
unary-binary-tree equation in which `z` marks total nodes of an encoded Motzkin
tree.  The two sizes agree:

```text
original leaf count = encoded total-node count.
```

#### Proof

Before elimination, the leaf alternative contributes `z` and an internal binary
node contributes the product of its two state-series, so `z` is unambiguously a
leaf marker.  Eliminating the trailing-zero states gives
`T=z+zT+zT^2`.  Reading its three terms as encoded leaf, unary node, and binary
node gives a recursive unary-binary encoding.  Each encoded constructor exposes
exactly one distinguished original leaf—the factor `z`—and recurses on the
remaining legal state-zero subtrees.  Induction gives the size identity. ∎

The encoded object `U(L)` has two encoded nodes and one encoded leaf, but it
corresponds to an original legal tree with two leaves.  It therefore does not
refute original leaf grading.

## 2. Correct bivariate profile interpretation

### Theorem PP3cqh -- PROVED / SIZE-PRESERVING MOTZKIN PROFILE

Let `n` be either the original leaf count or, equivalently, the encoded total-node
count.  If the encoding has `j` binary nodes, then it has

```text
encoded unary nodes = n-1-2j,
encoded leaves      = j+1,
```

and the exact coefficient is

```text
(n-1)! / ((n-1-2j)! j! (j+1)!).
```

At `n=30,j=9`, the original tree has thirty leaves, while the encoding has thirty
total nodes, eleven unary nodes, nine binary nodes, and ten encoded leaves.  The
family size remains `168212023980`.

#### Proof

The unary-binary encoding is counted by Lagrange inversion.  Its edge count is
`n-1=a+2j`, and its degree balance gives `j+1` encoded leaves.  Apply the size
identity from `PP3cqg`. ∎

## 3. Structural versus geometric risk

### Theorem PP3cqi -- PROVED / ENCODED RISK TYPE SEPARATION

The unary-to-unary edge count reconstructed in `docs/564` is an exact structural
risk on the Motzkin encoding.  At size `30` and binary count `9`, its aggregate
is

```text
638045608200,
```

with mean `110/29`.  It cannot be substituted for a prime-patching support,
source, or collision incidence risk without an explicit decoder from encoded
nodes and edges to geometric cells and events.

#### Proof

The dynamic program enumerates the encoded unary-binary constructors and its
risk distribution sums to the bivariate profile.  Its type mentions only
encoded root classes.  The patch risks mention geometric resources, so a typed
map is necessary before their totals can be identified. ∎

## 4. Corrected earlier text

This tranche clarifies `docs/528`, `docs/534`, `docs/552`, and `docs/564`: the
original series is leaf-graded; the eliminated unary-binary encoding is
node-graded; their size parameters coincide.

## 5. Exact diagnostic

Run

```bash
python scripts/check_prefix_grading_propagation.py
```

## 6. Prime-patching consequence

The prefix counting results and their original leaf interpretation survive.  The
risk DP is also valid, but its unary/binary statistics belong to the encoding.
The next genuine frontier remains the first exact geometric decoder from that
encoding to support-chord and source incidences.
