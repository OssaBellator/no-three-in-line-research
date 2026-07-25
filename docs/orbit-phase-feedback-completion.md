# Exact completion at bounded distance from a factor cactus

OP2d solves a canonical phase CSP when its whole factor-incidence graph
is a cactus. A noncactus block need not yet require arithmetic
expansion: a bounded set of variable nodes may carry all of its excess
cycle topology.

Let every variable \(v\) have a finite nonempty current domain
\(\mathcal A_v\), and let every check \(C\) forbid one canonical tuple
\(f_C\) on its incident variables. Write

\[
h=\max_v |\mathcal A_v|,
\qquad
I=\sum_C |N(C)|.
\]

## OP2e -- bounded variable-feedback completion

### Theorem OP2e -- PROVED

Suppose that deleting a set \(S\) of \(f\) variable nodes from the
factor-incidence graph leaves a cactus. Then satisfiability and a
satisfying assignment can be decided in

\[
\boxed{O\!\left(h^f(h^3 I+I)\right)
      =O(h^{f+3}I)}
\]

time. In particular, every fixed-\(f\) class is exactly completable.

If the instance is unsatisfiable, the algorithm returns an explicit
family, indexed by the at most \(h^f\) assignments to \(S\), in which
every member is one of:

1. a fully fixed check equal to its forbidden tuple;
2. a unary domain exhausted by its forbidden label; or
3. an OP2d variable- or check-separator saturation certificate.

Thus bounded excess-cycle topology is an exact finite interface, not an
unclassified phase-decoder obstruction.

### Conditioning rule

Enumerate

\[
\alpha\in\prod_{v\in S}\mathcal A_v.
\]

For each check \(C\):

- if some \(v\in C\cap S\) has
  \(\alpha(v)\ne f_C(v)\), then \(C\) is already satisfied and is
  deleted;
- otherwise all fixed incidences agree with the forbidden tuple, so
  \(C\) becomes the canonical check on \(N(C)\setminus S\) that forbids
  \(f_C|_{N(C)\setminus S}\);
- if no incidence remains in the second case, the branch is
  infeasible;
- a remaining unary check deletes its one forbidden label from the
  variable domain, and an empty resulting domain makes the branch
  infeasible.

After unary propagation, every surviving check still forbids exactly
one tuple on its current variables.

### Correctness

For a fixed \(\alpha\), the first rule deletes exactly the checks that
already contain a mismatch. When every fixed incidence is a match, a
remaining check is satisfied exactly when its unfixed incidences do not
all equal the restricted forbidden tuple. The reduced branch is
therefore equisatisfiable with the original instance subject to
\(a|_S=\alpha\).

Its factor-incidence graph is a subgraph of the graph obtained by
deleting \(S\). Every subgraph of a cactus is a cactus, so OP2d decides
the branch exactly and reconstructs all unfixed labels when it is
satisfiable. Adding \(\alpha\) gives a satisfying assignment of the
original instance. Conversely, every original assignment restricts to
one enumerated \(\alpha\), so if all branches are infeasible no
satisfying assignment exists.

There are at most \(h^f\) branches. Conditioning and unary
preprocessing cost \(O(I)\) per branch, while OP2d costs \(O(h^3I)\).
This proves the displayed bound. \(\square\)

## Consequence for the OP2 docket

The topological residual requiring a genuinely new expansion argument
can now be assumed to have **unbounded variable-deletion distance from
the factor-cactus class**. A theta block, a collection of cactus blocks
joined through finitely many phase variables, or any other fixed
feedback-variable core is already covered by exact enumeration plus the
OP2d separator calculus.

This conclusion does not assert that the required feedback set is
uniformly bounded in the arithmetic construction. Producing such a
bound, or proving expansion when no such bound exists, remains part of
OP2.

`scripts/verify_phase_feedback.py` exhaustively checks the first
noncactus test family: binary canonical constraints on a three-path
theta graph. It compares conditioning on one feedback variable with
brute force for all \(4^6\) choices of the six forbidden binary tuples.
The enumeration also records the sharper small-alphabet fact that every
one of these full-domain binary theta instances is satisfiable.
