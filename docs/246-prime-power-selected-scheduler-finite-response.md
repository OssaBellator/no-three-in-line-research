# The selected minimum scheduler has a finite response ledger

CMR1070--CMR1093 give every dirty selected minimum a target-hypergraph bank and
direct geometric execution.  CMR1094--CMR1133 remove routing recurrence, bound
protected growth and minimum losses, normalize fixed-core reopening, and compress
rolled-back banks to finite missing-edge covers.

This chapter combines those results into one cycle-erased finite-response theorem.
It does **not** prove that the final terminal blocker inventory is impossible.  It
shows that local target geometry, routing changes, same-value rollbacks, protected
resets, and fixed-core reopenings cannot support an unbounded selected-minimum
history.

Fix an ambient prime-power parent side

\[
N=p^h.
\]

A **canonical episode** starts from one actual minimum state of the current
host-representable family, analyses one dirty target configuration, executes one
of its full-parent response banks through complete host normalization, and ends at
the first restriction, protected growth, contraction, structural owner exit,
strict improvement, or permanent blocker-cover update.

Exact duplicate bank attempts, same-value expansions which roll back to the same
host, reconditioning of an already stored core while its anchor survives, and
repetition of an already selected routing or cross-skeleton class are erased.

## 1. Every dirty minimum supplies a canonical response bank

### Theorem CMR1134 -- PROVED

Let `S` be a dirty minimum.  For every `q>=2` and `R>=3`, the target hypergraph of
`S` supplies at least one of:

1. `q` physically disjoint targets and one degree-two Hall escape destroying at
   least `ceil(q/2)` of them;
2. one selected cell contained in at least
   \[
   \left\lceil\frac{\Phi(S)}{3(q-1)}\right\rceil
   \]
   targets;
3. a loaded target line;
4. a simultaneous common-layer or cross-layer secant-star bank.

### Proof

Apply CMR1070--CMR1085. ∎

The construction depends only on the selected minimum and fixed canonical tie
breaking.

## 2. A bank is executable or has a permanent missing-edge cover

### Theorem CMR1135 -- PROVED

For every finite response bank from CMR1134 at the current normalized host, at
least one of the following holds.

1. One target-destroying bank state is feasible.
2. The infeasible bank states have a missing-edge cover `C` of size at most
   `2N^2`, disjoint from the stored minimum anchor.

While `C` remains absent, the complete covered subbank remains infeasible.  If
cover edges return while the anchor survives, all returned cover edges are deleted
again simultaneously.

### Proof

If a feasible state exists, use it.  Otherwise apply CMR1126--CMR1130 to the
complete infeasible bank. ∎

Thus bank cardinality is irrelevant to the rollback response.

## 3. Every feasible target-destroying state has the minimum trichotomy

### Theorem CMR1136 -- PROVED

Executing a feasible or newly enabled target-destroying bank state through the
canonical host normalization reaches at least one of:

1. strict physical-potential improvement;
2. a same-value minimum which omits a designated target cell, giving a permanent
   two-label target-cell cut inside the current restriction segment;
3. a positive-gap robust episode which creates at least `D+g` new triples when it
   destroys target load `D` with gap `g>=1`;
4. exact rollback, added-edge minimum-core contraction, lost-anchor witness,
   structural owner exit, or envelope expansion.

### Proof

Use CMR982--CMR997 and CMR950--CMR957. ∎

Rollback without another listed output is erased from the canonical history.

## 4. Robust episodes consume protected or structural currency

### Theorem CMR1137 -- PROVED

A positive-gap robust episode from CMR1136 reaches at least one of:

1. positive protected growth in one or both layers;
2. a loaded old target line with explicit majority-layer absorption;
3. a simultaneous common-layer or cross-layer star execution;
4. a large protected core and exact selected-skeleton product descent;
5. a same-value target-cell cut;
6. blocker-cover update, anchor loss, contraction, strict factor/wall descent,
   envelope expansion, finite base handling, or strict improvement.

### Proof

Apply CMR1006--CMR1069, CMR1038--CMR1053, and CMR1126--CMR1133. ∎

There is no remaining anonymous robust-surplus branch.

## 5. Fixed cores recondition or pay loss

### Theorem CMR1138 -- PROVED

If an episode begins from a target or interface already contracted into the
induced minimum objective, every attempted escape reaches one of:

1. reconditioning and exact recontraction while the stored lifted anchor survives;
2. same-value rollback of the added batch;
3. strict improvement;
4. one canonical missing edge of the stored lifted anchor;
5. added-edge minimum-core contraction; or
6. strict structural exit.

### Proof

Apply CMR1110--CMR1117. ∎

Immediate reconditioning and same-host rollback are idempotent and erased.

## 6. Finite currency stocks

Use the parameter-free quantities

\[
\mathfrak O_{\min}(N,h)
=
(h+1)(2N+1)\mathcal A(N),
\]

\[
\mathfrak P_{\min}(N,h)
=
(h+1)(2N+1)
\sum_{m=1}^{N}2m(2m^2+m+1),
\]

\[
\mathfrak D_{\min}(N,h)
=
(h+1)(2N+1)
\sum_{m=1}^{N}2m^2(2m^2+m+1),
\]

\[
\mathfrak L(N,h)
=
(h+1)(2N+1)
\sum_{m=1}^{N}
(2m^2+m+1)(2m+1)(2m^2-2m),
\]

and

\[
\mathfrak B(N,h)
=
2N^2\mathfrak O_{\min}(N,h).
\]

For a coarse contracted-rank stock put

\[
\mathfrak C(N,h)=\mathfrak P_{\min}(N,h).
\]

### Theorem CMR1139 -- PROVED

Along one selected minimum closure branch:

1. structural owner stages are bounded by `mathfrak O_min`;
2. fresh protected edges by `mathfrak P_min`;
3. fresh structural deletion roots by `mathfrak D_min`;
4. canonical lost-minimum witnesses by `mathfrak L`;
5. fresh blocker-cover edges by `mathfrak B`;
6. total owner-labelled contracted rank by `mathfrak C`.

### Proof

The first five bounds are CMR1098--CMR1106 and CMR1132.  At a side-`m` selected
owner, total contracted rank is at most the current two-layer state cardinality
`2m`; sum over the same owner-stage, wall-tree, and envelope stocks used for
`mathfrak P_min`. ∎

These are deliberately coarse polynomial bounds.

## 7. Every nontrivial canonical episode spends one currency

### Theorem CMR1140 -- PROVED

Exclude strict improvement and finite base termination.  Every non-erased
canonical episode decreases at least one of the following remaining stocks:

1. unused structural owner stages;
2. unused protected capacity;
3. unused fresh deletion-root stock;
4. unused minimum-loss witness stock;
5. unused blocker-cover edge stock;
6. unused contracted-rank stock.

Consequently the number of nonimproving canonical episodes before a terminal
structural or blocker endpoint is at most

\[
\boxed{
\mathfrak E(N,h)
=
\mathfrak O_{\min}
+
\mathfrak P_{\min}
+
\mathfrak D_{\min}
+
\mathfrak L
+
\mathfrak B
+
\mathfrak C.
}
\]

### Proof

CMR1135 spends blocker stock unless a state executes.  CMR1136 spends loss,
contraction, owner, or improvement currency unless it enters a robust episode.
CMR1137 spends protected, loss, blocker, contraction, or structural currency.
CMR1138 spends loss, contraction, or structural currency unless its operation is
idempotent and erased.  Host restrictions spend fresh deletion edges; strict child,
wall, and envelope changes spend owner stages.  Sum the finite stocks from
CMR1139. ∎

The bound counts a shortest canonical response history, not every redundant
algorithmic attempt.

## 8. Selected-scheduler endpoint

### Corollary CMR1141 -- PROVED

For a fixed prime-power parent, the selected minimum scheduler cannot have an
unbounded local response history generated by routing changes, protected resets,
same-value rollbacks, target-cell handoffs, fixed-core reopenings, or repeated
candidate-bank enumeration.

After at most `mathfrak E(N,h)` nonimproving canonical episodes, it reaches at
least one of:

1. strict physical-potential improvement;
2. finite base handling;
3. a terminal host with a permanent missing-edge blocker cover for every selected
   target-response bank;
4. a terminal loaded-line, Hall, prefix, carry, or protected-core certificate in a
   strict residual factor;
5. completion of the finite structural descent tree.

The remaining prime-power frontier is no longer a recurrence problem.  It is the
**terminal obstruction theorem**: show that a terminal blocker/line/core
certificate in the final residual factor forces a clean state, strict minimum
decrease, or one of the already finite prime-field/thin-regime base cases.
Prime-field transfer and arbitrary side-length CRT assembly remain separate.

### Proof

Combine CMR1134--CMR1140. ∎

No all-`n` theorem is claimed.  The alternative routing and finite-stock arithmetic
are checked in
[`scripts/verify_prime_power_selected_scheduler_response.py`](../scripts/verify_prime_power_selected_scheduler_response.py).
