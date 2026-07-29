# Tree-decomposed Pareto messages for interactions

`docs/482` convolves independent interaction blocks.  Real condensation pieces
may share a small boundary state, so block choices are not fully independent.
This chapter replaces independence by a finite tree decomposition and carries
exact Pareto messages across the separators.

Consider a finite factor tree.  Each local interaction choice has rational
nonnegative output vector, integer work, and a finite assignment on the factor's
boundary variables.  Compatible neighboring factors agree on their shared
separator assignment.

## 1. Exact separator messages

### Theorem PP3cgu -- PROVED / PARETO JUNCTION-TREE RECURRENCE

For every directed factor-tree edge, separator signature `sigma`, and work budget
`B`, store the nondominated omitted-output vectors attainable in the corresponding
subtree with boundary signature `sigma` and work at most `B`.  Combining child
messages by compatible signature matching, exact vector addition, and work
addition computes every message exactly.

#### Proof

Removing one tree edge separates the factor tree into independent subproblems
conditioned on the separator signature.  Every feasible subtree plan decomposes
uniquely into one local choice and compatible child plans, so the recurrence
enumerates all attainable vectors.  Induction from the leaves proves exactness. ∎

## 2. Safe signature-aware pruning

### Theorem PP3cgv -- PROVED / TREEWIDTH-LOCAL DOMINANCE

Within the same separator signature, a partial message vector dominated
coordinatewise by another vector using no more work may be deleted.  It can never
participate in a globally nondominated completion.  No such pruning is valid
across different separator signatures unless their future compatibility sets are
also identical.

#### Proof

Every continuation compatible with one message of a fixed signature is
compatible with the other.  Adding the same nonnegative continuation preserves
coordinatewise dominance and the work inequality.  Different signatures may
permit different continuations, so the argument does not cross signatures. ∎

The message-state growth is exponential only in the separator width, not in the
total number of blocks.

## 3. Minimum-work and reconstruction certificate

### Theorem PP3cgw -- PROVED / TREE-DECOMPOSED TOLERANCE CERTIFICATE

At the root, the least budget whose Pareto message contains a vector below the
requested tolerance is the exact minimum work.  Stored predecessor pointers
reconstruct a compatible global interaction plan.  The complete root messages
for all lower budgets form a matching impossibility certificate.

#### Proof

The root message contains exactly all globally attainable nondominated vectors
by `PP3cgu`.  Every attainable vector is dominated by a root-frontier vector, so
feasibility is equivalent to the presence of one vector below tolerance.  The
first feasible budget is minimal, and predecessor pointers reverse the exact
message recurrence. ∎

## 4. Stored exact fixture

The audit `scripts/check_tree_decomposed_interaction_pareto.py` uses a three-factor
chain with binary interfaces and nine compatible full plans.  Exact message
entry counts after the three factors are `3,6,9`.  For tolerance
`(8/5,5/4)`, every budget-three frontier vector violates at least one coordinate.
Budget four has the unique feasible plan

```text
B -- F -- I
```

with omitted output `(3/2,6/5)`.  The message recurrence agrees with exhaustive
enumeration at every budget from zero through eight.

## 5. Prime-patching consequence

Higher-order condensation interactions can now be split along small geometric
interfaces rather than treated as one monolithic automaton.  Exact Pareto
messages preserve all multioutput tradeoffs, while separator width controls the
combinatorial cost of the global certificate.
