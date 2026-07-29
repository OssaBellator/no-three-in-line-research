# Acyclic marker automata for stopping words

`docs/441` realizes each stopping codeword as a chain of local marker kernels.
Different stopping classes may nevertheless share prefixes, suffixes, or
intermediate marker states. This chapter replaces a disjoint word family by a
finite acyclic marker automaton and records the exact path-sum load certificate.

## 1. Automaton data

Let `A=(V,E)` be a finite directed acyclic graph. A root `r` carries base
reverse load `lambda_r`. Every edge `e=(u,v)` is a local marker kernel with
certified reverse-load factor `q_e`. The target of the edge intrinsically
records the next automaton state `v`.

For every state define, in topological order,

```text
B(v)=lambda_v+sum_(u->v) B(u) q_(u,v),
```

where `lambda_v=0` away from the roots.

### Theorem PP3ccb -- PROVED / ACYCLIC PATH-SUM IDENTITY

For every state `v`,

```text
B(v)=sum_(P:r->v) lambda_r product_(e in P) q_e,
```

where the sum includes the length-zero path when `v` is a root.

#### Proof

Induct in topological order. Every nontrivial path ending at `v` has a unique
last edge `u->v`; removing it gives a path ending at `u`. The recurrence
therefore partitions the complete path family by its last edge. ∎

## 2. Kernel composition

### Theorem PP3ccc -- PROVED / AUTOMATON LOAD BOUND

Assume every local edge kernel obeys its factor `q_e` and every intermediate
target recovers its state label. Then the reverse load entering state `v` is at
most `B(v)`. If accepting terminal labels are mutually recoverable, the
combined stopping kernel has load at most

```text
max_(t terminal) B(t).
```

#### Proof

At a state `v`, contributions from different predecessor states are the only
ones that may merge. The state label prevents all other merges. Applying the
local factor on each incoming edge and summing gives the defining recurrence for
`B(v)`. Distinct recoverable terminal labels combine by a maximum rather than a
sum. ∎

## 3. Localized failure

### Theorem PP3ccd -- PROVED / BAD-TRANSITION CERTIFICATE

If an observed terminal load exceeds the automaton certificate, then at least
one of the following is witnessed:

1. a local edge kernel exceeds its declared factor;
2. an intermediate state label is not recoverable; or
3. two declared terminal labels collide.

In particular, when labels are checked syntactically, every excess load returns
one explicit bad transition.

#### Proof

The contrapositive is `PP3ccc`. ∎

## Frontier consequence

Shared stopping words no longer require duplicating their common marker moves.
A finite DAG dynamic program certifies the complete shared implementation, while
any failure localizes to one automaton edge or one lost state tag.
