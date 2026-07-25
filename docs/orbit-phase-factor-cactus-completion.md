# Exact completion on factor-incidence cacti

OP2c handles cactus topology after every check has been contracted to a
binary edge. The same block decomposition works before contraction, even
when a check has high arity, provided the factor-incidence graph itself
is a cactus.

Let every variable \(v\) have a finite nonempty current domain
\(\mathcal A_v\). A check \(C\) forbids one tuple

\[
f_C\in\prod_{v\in N(C)}\mathcal A_v^{\rm original}.
\]

For an assignment \(a_v\), call the incidence \(Cv\) a mismatch when
\(a_v\neq f_C(v)\). The check is satisfied exactly when at least one of
its incidences is a mismatch.

The factor-incidence graph is a cactus when every incidence edge belongs
to at most one simple cycle. Its blocks are bridges and alternating
variable--check cycles.

## OP2d -- factor-cactus message reduction

### Theorem OP2d -- PROVED

Let

\[
h=\max_v|\mathcal A_v|
\quad\text{and}\quad
I=\sum_C|N(C)|.
\]

For every canonical phase CSP whose factor-incidence graph is a cactus,
satisfiability and a satisfying assignment can be decided in

\[
\boxed{O(h^3 I)}
\]

time.

If the instance is unsatisfiable, the algorithm returns one of two exact
separator certificates:

1. a variable articulation whose allowed-label message is empty; or
2. the final/root check separator whose full attainable mismatch-bit
   aggregate does not contain \(1\).

The second certificate says that every extension of the processed
incidences agrees with the forbidden tuple at that check. It is a
two-state check saturation, not an unclassified high-arity core.

### Messages

Root the block--cut forest. A message through a variable articulation
\(v\) is a subset of \(\mathcal A_v\). A message through a check
articulation \(C\) is a subset of \(\{0,1\}\), where the bit records the
OR of mismatch indicators contributed by the processed side.

Messages from distinct child blocks combine exactly as follows:

- at a variable, intersect the allowed-label sets;
- at a check, take their OR-convolution
  \[
  S_1\vee\cdots\vee S_k
  =
  \{s_1\vee\cdots\vee s_k:s_i\in S_i\}.
  \]

The empty child aggregate is \(\mathcal A_v\) at a variable and
\(\{0\}\) at a check.

### Bridge blocks

For a bridge \(vC\), a processed variable side sends to \(C\) the set of
bits

\[
\{[a\neq f_C(v)]:a\text{ is allowed on the variable side}\}.
\]

In the reverse direction, suppose the processed check side can
contribute a bit in \(S_C\). It sends to \(v\) exactly the labels \(a\)
for which

\[
s\vee[a\neq f_C(v)]=1
\]

for some \(s\in S_C\). Here the check is complete on the processed side,
so requiring the final bit to equal one is exact.

### Cycle blocks

Write an alternating cycle as

\[
v_0,C_0,v_1,C_1,\ldots,v_{k-1},C_{k-1},v_0.
\]

Every internal variable \(v_i\) has a domain \(D_i\) after intersecting
its child messages. Every internal check \(C_i\) has an attainable child
bit set \(S_i\). Across \(C_i\), two adjacent labels are compatible
precisely when

\[
\exists s\in S_i:\quad
s\vee[a_i\neq f_{C_i}(v_i)]
\vee[a_{i+1}\neq f_{C_i}(v_{i+1})]=1.
\]

Thus the induced relation is universal when \(1\in S_i\); otherwise it
forbids only the canonical pair of matching labels.

If the boundary is a variable, fix one of its labels and run path
dynamic programming around the cycle, retaining it exactly when the
closing relation can be met. If the boundary is a check, run the same
path dynamic program across the other checks and return the attainable
OR bits contributed by the two boundary incidences. Stored predecessors
recover all internal labels.

### Correctness and complexity

Deleting a leaf block separates it from the remaining instance at one
articulation. A variable label is the complete interface across a
variable separator. Across a check separator, the processed part can
affect the rest only through whether it has already supplied a mismatch,
so one bit is the complete interface. Intersection and OR-convolution
therefore lose no compatibility information.

The bridge rules enumerate all assignments on their one incidence. The
cycle recurrence enumerates all assignments in cyclic order and applies
the exact canonical relation at every check. Induction up the block--cut
tree proves that every message is precisely the set of extendable
boundary states. At a root variable, a nonempty final label set is
equivalent to satisfiability. At a root check, the final OR-set must
contain \(1\).

A bridge costs \(O(h)\). For a cycle, fixing a boundary label and
scanning consecutive label pairs costs \(O(h^2)\) per incidence; trying
at most \(h\) boundary labels gives \(O(h^3)\) per incidence. Blocks
partition the incidence edges, proving the displayed bound. Reversing
stored predecessors constructs an assignment within the same bound.
\(\square\)

## Consequence for OP2

OP2d strictly extends the binary contracted-cactus endpoint: arity-three
and larger checks are harmless whenever their full incidence topology is
a cactus. After exact preprocessing, the remaining arithmetic Tanner
problem can be restricted to:

- a variable-label saturation;
- a two-state check saturation that must be paid or absorbed; or
- a noncactus factor block, equivalently a block containing at least two
  independent incidence cycles.

`scripts/verify_phase_factor_cactus.py` exhaustively compares the message
calculus with brute force on binary-domain flowers consisting of one
four-variable check and two binary petal checks.
