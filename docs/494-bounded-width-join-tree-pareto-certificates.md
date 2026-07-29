# Bounded-width join-tree Pareto certificates

`docs/488` gives separator-indexed Pareto messages on a width-one factor chain.
The same principle extends to any finite join tree of bounded bags, allowing
several shared interaction states to be remembered simultaneously.

Let a join tree have bags `B_t`, local finite choices, and separator
`S_(t,p)=B_t intersect B_p` on every parent edge.  Each complete compatible
plan has integer work and a nonnegative rational error vector.

## 1. Exact join-tree recurrence

### Theorem PP3chm -- PROVED / SEPARATOR-INDEXED JOIN MESSAGES

For every directed tree edge `t->p`, separator assignment `sigma`, and work
budget `b`, store the nondominated error vectors of all plans in the subtree of
`t` whose restriction to `S_(t,p)` is `sigma`.

A bag message is obtained by enumerating its local assignment, joining child
messages with matching separator restrictions, adding work and error vectors,
and deleting dominated vectors within each fixed `(sigma,b)` class.  The root
messages are exactly the global Pareto frontiers.

#### Proof

The running-intersection property makes the separator assignment the complete
compatibility information between a subtree and its complement.  Every global
plan decomposes uniquely into one local bag choice and compatible child plans.
Conversely, matching messages glue to a global plan.  Induction over the join
tree proves exactness. ∎

## 2. Safe pruning and width control

### Theorem PP3chn -- PROVED / BOUNDED-WIDTH MESSAGE CERTIFICATE

Dominance pruning is safe only among messages with the same separator
assignment and no greater work.  With alphabet size `q`, treewidth `w`, maximum
budget `B`, and at most `F` retained vectors per signature and budget, every
message table has at most

```text
q^w (B+1) F
```

entries.  Thus fixed width and bounded Pareto frontiers reduce global
enumeration to finite local joins.

#### Proof

A dominated vector remains dominated after adding the same nonnegative
continuation.  Different separator signatures may have different compatible
continuations and therefore cannot be compared.  The table-size bound counts
all signatures, budgets, and retained vectors. ∎

## 3. Minimum-work reconstruction

### Theorem PP3cho -- PROVED / JOIN-TREE TOLERANCE WITNESS

For coordinatewise tolerance `tau`, the minimum work is the least root budget
whose frontier contains `e<=tau`.  Stored bag choices and child-message
backpointers reconstruct a complete compatible plan.  The preceding root
frontiers certify impossibility at every smaller budget.

#### Proof

`PP3chm` makes the root frontier exact.  Feasibility and minimality therefore
reduce to scanning budgets in increasing order.  Backpointers reverse the
joins. ∎

## 4. Stored exact fixture

The audit `scripts/check_width_two_interaction_join_tree.py` uses bags
`(a,b,c)` and `(b,c,d)` with two-bit separator `(b,c)`, hence treewidth two.
All 16 global binary assignments are recovered exactly from four separator
signatures.

The Pareto frontier sizes at budgets zero through four are

```text
1,2,3,2,1.
```

Tolerance `(1,1)` is impossible at work three and has the unique work-four
plan `(a,b,c,d)=(1,1,1,1)`.

## 5. Prime-patching consequence

Higher-order resolvent interactions can now be certified whenever their
compatibility graph has a small join-tree width.  The calculation remembers
only separator states and exact local Pareto vectors rather than all global
interaction choices.
