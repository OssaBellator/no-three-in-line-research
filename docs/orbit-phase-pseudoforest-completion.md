# Exact completion for phase pseudoforests

The forest theorem OP2a leaves a cycle as the first possible topological
core.  For canonical phase checks, however, one cycle is still harmless.
This note extends exact completion from forests to pseudoforests.

Let every variable \(v\) have a finite alphabet \(\mathcal A_v\) with
\(|\mathcal A_v|\geq2\).  Every check has scope at least two and forbids
exactly one assignment on its scope.  The incidence graph is the bipartite
graph on variables and checks.

## OP2b -- phase pseudoforests are satisfiable

### Theorem OP2b -- PROVED

If every connected component of the incidence graph has at most one
cycle, then there is an assignment avoiding every check.  An assignment
can be found in time linear in the total check incidence.

### Proof

Repeatedly choose a variable of current incidence degree at most one.  If
it is isolated, delete it and remember it for later.  If its unique
incident check is \(C\), delete both the variable and the whole check
\(C\), and remember the pair \((v,C)\).  Deletion preserves the
pseudoforest property.

When no such variable remains, every remaining variable and every
remaining check has degree at least two.  A nonempty connected
pseudoforest on \(n\) nodes has at most \(n\) edges.  The degree lower
bound gives at least \(2n\) total degree, hence at least \(n\) edges.
Equality holds throughout.  Thus every remaining node has degree exactly
two and every component is an alternating simple cycle.  In particular,
every remaining check has scope two.

Consider one such cycle, written

\[
v_0,C_0,v_1,C_1,\ldots,v_{m-1},C_{m-1},v_0.
\]

Choose the label of \(v_0\) different from its forbidden label in
\(C_{m-1}\).  This already satisfies the closing check \(C_{m-1}\),
regardless of \(v_{m-1}\).  Traverse \(C_0,\ldots,C_{m-2}\).  Once
\(v_i\) is assigned, the check \(C_i\) forbids at most one label of
\(v_{i+1}\); choose another one.  This assigns and satisfies the whole
cycle.

Finally restore the deleted variables in reverse order.  An isolated
variable receives an arbitrary label.  For a recorded pair \((v,C)\),
all other variables of \(C\) have already been assigned.  If their labels
do not equal the forbidden partial assignment, any label for \(v\)
works.  If they do, exactly one label of \(v\) is forbidden, and a
different label exists.  At the time of deletion \(C\) was the only
remaining check containing \(v\), so this extension cannot spoil a check
already restored.

Each incidence is examined only a constant number of times when degrees,
cycle order, and the reverse assignments are maintained explicitly.
\(\square\)

## Exact residual obstruction

After unrealizable checks are discarded and unary checks are processed,
an unsatisfiable canonical phase CSP must therefore contain a component
with cyclomatic number at least two:

\[
|E|-|V_{\rm var}|-|V_{\rm check}|+1\geq2.
\]

This is strictly stronger than the forest/cycle boundary in OP2a.  OP2
needs arithmetic expansion only on multiply-cyclic cores, or on a unary
saturation returned by preprocessing.

The threshold is real.  Two binary variables with four parallel checks
forbidding the four possible ordered pairs are unsatisfiable.  Its
incidence graph has cyclomatic number three, so it lies outside the
pseudoforest theorem.

`scripts/verify_phase_pseudoforest.py` exhaustively checks binary cycle
patterns through length seven, a unicyclic component with a ternary leaf
check, and the multiply-cyclic unsatisfiable regression.
