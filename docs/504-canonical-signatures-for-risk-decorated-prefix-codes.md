# Canonical signatures for risk-decorated prefix codes

`docs/498` generates unordered prefix-tree shapes without duplicates.  A code
search must also place risk classes on the leaves.  This chapter canonicalizes
the decorated tree under every local symmetry that preserves the outgoing
symbol survivals.

A leaf has a risk-class label.  At an internal node, children whose edge symbols
have the same survival probability may be permuted; children in different
survival classes remain ordered.

## 1. Recursive decorated signatures

### Theorem PP3ciq -- PROVED / SURVIVAL-PRESERVING CANONICAL FORM

Assign each leaf its risk label.  Recursively replace every internal node by the
tuple of child signatures, sorting only within equal-survival edge classes.  Two
risk-decorated prefix trees have the same resulting signature if and only if
they are related by survival-preserving local child permutations and
permutations of equal-risk bank labels.

#### Proof

The forward implication follows because the permitted permutations do not
change any sorted child multiset.  Conversely, equality of root signatures
pairs equal child signatures within each survival class; induction supplies the
required child isomorphisms and leaf-label permutations. ∎

## 2. Isomorph-free decorated dynamic programming

### Theorem PP3cir -- PROVED / DECORATED ORBIT RECURRENCE

For every risk multiplicity vector, recursively combining canonical child
signatures and discarding duplicate parent signatures enumerates each decorated
code orbit exactly once.  Any Bellman value depending only on leaf risks and
symbol survivals is constant on an orbit and may be evaluated once per
signature.

#### Proof

`PP3ciq` makes signatures complete orbit invariants.  Every decorated tree has a
root split into smaller decorated trees, so recursive generation is exhaustive.
Duplicate signatures are precisely duplicate orbits.  Survival products and
leaf risks are invariant under the permitted symmetries. ∎

## 3. Optimal orbit filtering and lifting

### Theorem PP3cis -- PROVED / CANONICAL OPTIMUM CERTIFICATE

Storing every generated signature, its child split, its exact Bellman value, and
one labeled lift gives a finite certificate for all optimal decorated orbits.
Failure localizes to a missing split, duplicate signature, invalid symmetry,
incorrect leaf multiplicity, or overloaded lifted leaf.

#### Proof

The stored recurrence proves exhaustive orbit generation, while direct leaf
checks verify every lifted code and its value. ∎

## 4. Stored exact fixture

The audit `scripts/check_risk_decorated_prefix_signatures.py` uses equal binary
symbol survivals `1/2`, four low-risk leaves of risk one, and two high-risk
leaves of risk two.  The 42 ordered six-leaf shapes and 15 high-risk placements
produce 630 ordered decorated trees.  Canonicalization collapses them to 41
orbits with value histogram

```text
8:2, 16:16, 32:18, 64:5.
```

Exactly two orbits are optimal; together they have six ordered lifts.

## 5. Prime-patching consequence

Risk placement and tree-shape search can now be performed simultaneously
without revisiting symmetric decorated schedules.  This reduces the finite
repair-word oracle before any geometric embedding constraints are imposed.
