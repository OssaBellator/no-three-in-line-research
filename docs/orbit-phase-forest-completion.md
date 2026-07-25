# Exact completion for acyclic phase-factor graphs

OP1a turns every realizable collinear triple into one canonical forbidden
partial assignment on at most three orbit-block variables.  This note
solves the entire acyclic part of that labelled CSP.

Let each variable \(v\) have a finite alphabet \(\mathcal A_v\) with
\(|\mathcal A_v|\geq2\).  A check \(C\) has a scope of at least two
variables and forbids exactly one assignment on that scope.  The incidence
graph has variable nodes, check nodes, and an edge for every variable in a
check.

## OP2a -- phase forests are satisfiable

### Theorem OP2a -- PROVED

If the incidence graph is a forest, there is an assignment avoiding every
check.  Such an assignment is found by leaf elimination.

### Proof

If checks remain, some variable has incidence degree at most one.  Indeed,
if every variable and every check had degree at least two, every nonempty
component of the incidence forest would have minimum degree two, which is
impossible for a finite tree.  Checks have degree at least two by
hypothesis, so a leaf node can be chosen on the variable side.

If the variable \(v\) is isolated, delete it and assign it arbitrarily
after solving the remaining forest.  Otherwise let \(C\) be its unique
incident check.  Delete \(v\) and the entire check \(C\), then solve the
remaining forest inductively.

When extending the assignment back to \(v\), inspect the already assigned
variables of \(C\).  If they do not match the unique forbidden pattern,
any label of \(v\) satisfies \(C\).  If they do match, exactly one label of
\(v\) completes the forbidden pattern; choose a different label, which
exists because \(|\mathcal A_v|\geq2\).  No other check contains \(v\), so
the extension preserves all previously satisfied checks. \(\square\)

### Algorithmic bound

Maintaining variable incidence degrees and a leaf queue gives a linear-time
algorithm in the total check incidence.  The reverse assignment pass is
linear for the same reason.

## Consequence for OP2--OP4

After removing unrealizable triples and preprocessing unary checks, every
unsatisfied phase CSP has one of two obstructions:

1. a variable has all of its labels forbidden by unary checks; or
2. the residual incidence graph contains a cycle.

Thus a generic acyclic Tanner component is not a structured exception and
needs no expansion theorem or absorber.  OP2 may restrict its arithmetic
work to cyclic cores.  In particular, the mandatory degree-two cycle
examples are not artifacts of peeling: cycles are the first incidence
topology on which the forest completion proof stops.

Unary preprocessing is essential.  Two unary checks can forbid both
labels of a binary variable even though their incidence graph is a tree.
Real orbit blocks must either rule out such unary saturation geometrically
or pass it directly to a local absorber.

`scripts/verify_phase_forest.py` exhaustively checks all binary forbidden
patterns on factor paths of up to five checks and retains unary saturation
as a negative regression.
