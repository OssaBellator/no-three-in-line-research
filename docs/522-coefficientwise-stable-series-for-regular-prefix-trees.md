# Coefficientwise-stable series for regular prefix trees

`docs/516` gives a threshold polynomial for one fixed multiplicity vector.  This
chapter counts every legal prefix-tree size at once and shows that each
coefficient stabilizes after a finite depth.

Let a deterministic binary automaton have states `Q`, transition `delta`, and
accepting states `F`.  An ordered full binary prefix tree is legal when every leaf
word finishes in `F`.

## 1. Depth-truncated generating recurrence

### Theorem PP3cks -- PROVED / REGULAR PREFIX-TREE POLYNOMIAL

Let `F_{q,D}(z)` count legal ordered full binary trees rooted at automaton state
`q`, with height at most `D`, by number of leaves.  With `a_q=1` for `q in F` and
zero otherwise,

```text
F_{q,0}(z)=a_q z,
F_{q,D}(z)=a_q z
           +F_{delta(q,0),D-1}(z) F_{delta(q,1),D-1}(z).
```

The coefficient of `z^K` is the exact number of legal ordered `K`-leaf prefix
trees in the depth cap.

#### Proof

A legal tree is either a single accepted leaf or an internal root with one legal
zero-child tree and one legal one-child tree.  Ordered child choices multiply;
the two cases add. ∎

## 2. Coefficient stabilization

### Theorem PP3ckt -- PROVED / FINITE-DEPTH STABILIZATION

For every `K>=1`, the coefficient `[z^K]F_{q,D}` is independent of `D` once
`D>=K-1`.  Hence the coefficientwise limit

```text
F_q(z)=lim_(D->infinity) F_{q,D}(z)
```

is well defined and satisfies the same algebraic system

```text
F_q=a_q z+F_{delta(q,0)}F_{delta(q,1)}.
```

#### Proof

A full binary tree with `K` leaves has height at most `K-1`: every internal vertex
on a deepest root-to-leaf path has a sibling subtree containing a distinct leaf.
Thus no `K`-leaf object first appears after depth `K-1`. ∎

## 3. Decorated and thresholded coefficients

### Theorem PP3cku -- PROVED / MULTIVARIATE LEGAL-CODE SERIES

Replacing the leaf term `a_q z` by a finite sum of variables for allowed risk
classes, threshold levels, or marker types gives a multivariate version of the
same recurrence.  Any requested multiplicity coefficient is therefore computed
and reconstructed by a finite product-state dynamic program; a zero coefficient
is an exact infeasibility certificate.

#### Proof

Leaf decorations affect only the leaf monomial.  Internal composition remains a
product, so coefficient extraction tracks the exact multiset split.  Stabilization
continues to hold coefficientwise by total leaf degree. ∎

## 4. Stored exact fixture

The audit `scripts/check_regular_prefix_shape_series.py` counts prefix trees whose
leaf words avoid `000`.  The stabilized ordered shape counts for one through ten
leaves are

```text
1,1,2,4,9,21,51,127,323,835.
```

For every `K<=10`, the audit confirms stabilization exactly at depth at most
`K-1`.

## 5. Prime-patching consequence

Regular marker legality now has a reusable generating object rather than a
separate search for each number of banks.  Finite multiplicity questions become
coefficient extraction from a coefficientwise-stable algebraic system.
