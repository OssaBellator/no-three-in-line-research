# Signature recurrence and protected correction banks

OP3j turns every paid geometric factor fan into a nonempty set of
product- or anchor-specific cross-carry signatures.  The unresolved
cross-round question was whether the same finite signature could be
returned indefinitely without increasing the structured-core
potential.

This note gives the exact lossless answer available before additional
arithmetic is used.

1. First exposure defines a monotone state-qualified signature ledger.
2. If the ledger does not grow at the current decoder snapshot, a
   fixed signature receives a paid high-reuse class at that same
   snapshot.
3. A bounded-support high-reuse class either deepens an
   action-literal kernel or contains a paid family of pairwise
   support-disjoint corrections.
4. The two orientations of those disjoint corrections project the
   complete canonical phase CSP to an exact rank-at-most-three CNF.
5. Its rank-at-most-two part is completed by 2-SAT.  Failure returns
   an explicit contradictory implication chain.
6. Every remaining rank-three clause is a named transversal through
   three correction supports.

Corrections from different decoder snapshots are never combined.  The
persistent ledger records the pair consisting of the full current phase
assignment and the carry signature.  Thus recurrence either grows a
finite state-qualified ledger or returns compatible correction centres
generated against one common current assignment.

The rank separation is also necessary.  Alternating choices can logically
anticorrelate a dense family of blockers, but bounded signature
multiplicity and a connected trade space do not by themselves imply
that a rank-three selection instance is satisfiable.

## OP3k -- first-exposure and paid-reuse ledger

Fix one decoder snapshot \(\omega\), and consider the ordered
factor-fan centres in one paid OP3j output,

\[
(\mathcal S_i,g_i),
\qquad
i=1,\ldots,R,
\]

where \(\mathcal S_i\) is the nonempty set of carry signatures exposed
by centre \(i\), and \(g_i>0\) is its retained correction gain.  A
cross-carry signature includes its anchor and channel data; signatures
with different geometric provenance are not identified.

Put

\[
\mathcal U=\bigcup_{i=1}^R\mathcal S_i,
\qquad
B=|\mathcal U|,
\qquad
I=\sum_{i=1}^R|\mathcal S_i|.
\]

For \(\sigma\in\mathcal U\), define its exposure degree and split
payment by

\[
d_\sigma
=
|\{i:\sigma\in\mathcal S_i\}|,
\qquad
w_\sigma
=
\sum_{i:\sigma\in\mathcal S_i}
\frac{g_i}{|\mathcal S_i|}.
\]

Call centre \(i\) **fresh within the output** when it contains a
signature absent from all earlier centres in this ordering.  Otherwise
it is wholly recurrent within the output.

### Theorem OP3k -- PROVED

The signature ledger has the following exact properties.

1. The split payment is lossless:
   \[
   \boxed{\sum_{\sigma\in\mathcal U}w_\sigma
   =\sum_{i=1}^R g_i.}
   \]
   Consequently some signature has
   \[
   \boxed{
   w_\sigma
   \geq
   \frac{\sum_i g_i}{B}.
   }
   \]
2. There are at most \(B\) fresh centres.  Every other centre uses
   only previously exposed signatures.
3. For every positive integer \(\mu\), either
   \[
   \boxed{
   B\geq\left\lceil\frac I\mu\right\rceil
   }
   \]
   or some signature satisfies
   \[
   \boxed{d_\sigma\geq\mu+1.}
   \]
4. If every centre exposes at least \(L\) signatures, then the first
   box strengthens to
   \[
   B\geq\left\lceil\frac{RL}{\mu}\right\rceil.
   \]
   In particular, if all signatures lie in a fixed active universe
   \(\Sigma_{\rm act}\), then
   \[
   RL>\mu|\Sigma_{\rm act}|
   \]
   forces a signature of degree at least \(\mu+1\).

### Proof

Each centre distributes exactly \(g_i\) among its
\(|\mathcal S_i|\) incidences, proving the payment identity.
Pigeonholing its total over the \(B\) signatures gives the paid
high-reuse class.

Charge every fresh centre to its first new signature.  Distinct fresh
centres receive distinct first-exposure charges, so there are at most
\(B\) of them.

If every signature has degree at most \(\mu\), double-counting the
event-signature incidences gives

\[
I=\sum_{\sigma\in\mathcal U}d_\sigma\leq\mu B.
\]

This proves conclusion 3.  The lower bound \(I\geq RL\) proves
conclusion 4. \(\square\)

The split-payment statement is deliberately snapshot-local.  Its
corrections are simultaneously defined against \(\omega\), so the paid
class can be passed to OP3l without transporting a correction across a
phase change.

### Corollary OP3k.1 -- state-qualified cross-round ledger

Let \(\Omega\) be the finite phase-state space and let
\(\Sigma_{\rm act}\) be the finite active carry-signature universe.
Maintain the persistent token ledger

\[
\mathcal L\subseteq\Omega\times\Sigma_{\rm act}.
\]

At a decoder snapshot \(\omega\), an exposed signature \(\sigma\)
contributes the token \((\omega,\sigma)\).  A nonimproving factor-fan
round has one of the following exact outcomes.

1. It exposes a token outside \(\mathcal L\), so
   \(|\mathcal L|\) strictly increases.
2. Every exposed token is already in \(\mathcal L\).  Apply OP3k to
   the centres of this one current OP3j output; one current signature
   class carries at least
   \[
   \frac{\sum_i g_i}{|\mathcal U|}
   \]
   of its split payment and all its corrections share the same
   current snapshot \(\omega\).

There are at most

\[
\boxed{|\Omega|\,|\Sigma_{\rm act}|}
\]

rounds of the first type.

### Proof

The token universe has the displayed cardinality, and a round of the
first type inserts at least one previously absent token.  In a round
of the second type, do not combine historical centres: apply the
snapshot-local payment identity of OP3k only to the current centre
family. \(\square\)

This is the required monotone bookkeeping.  Qualifying by \(\omega\)
is essential: a repeated raw carry signature at a different phase
assignment does not define a compatible binary switch.

### Corollary OP3k.2 -- finite descent to a named output

Put

\[
B_{\rm tok}
=
|\Omega|\,|\Sigma_{\rm act}|.
\]

Suppose every nonterminal decoder round either:

1. decreases the integer syndrome potential \(\Phi\) by at least one;
2. leaves \(\Phi\) fixed and inserts a new state-signature token; or
3. leaves \(\Phi\) fixed with no new token and immediately passes its
   current paid class to OP3l--OP4c.

Treat every OP3l action kernel, OP4b contradictory chain, OP4c
rank-three transversal, and wide OP3j action CSP as a named terminal
delegation.  Before reaching zero syndrome or one of these
delegations, the decoder has at most

\[
\boxed{
(B_{\rm tok}+1)\Phi_0+B_{\rm tok}-|\mathcal L_0|
}
\]

nonterminal rounds.

### Proof

Use \(\Xi=|\mathcal L|\) in OP3b.  It lies between zero and
\(B_{\rm tok}\).  Rounds of type 1 strictly lower \(\Phi\), rounds of
type 2 strictly increase \(\Xi\), and a round of type 3 exits to one of
the listed interfaces instead of continuing.  OP3b gives the displayed
bound. \(\square\)

This is a termination theorem to an explicit interface, not a proof
that every interface is absorbable.

## OP3l -- high-reuse support extraction

Fix one current decoder snapshot \(\omega\), one OP3j output generated
at that snapshot, and one signature.  Let \(\mathcal I\) be its
distinct correction centres exposing that signature.  Centre \(i\)
has nonempty correction support \(E_i\), its current split weight
\(w_i>0\), and

\[
|E_i|\leq s.
\]

Put

\[
\lambda
=
\max_v|\{i:v\in E_i\}|.
\]

The support-intersection graph joins \(i,j\) when
\(E_i\cap E_j\ne\varnothing\).

### Theorem OP3l -- PROVED

The recurrent class has the following exact alternatives and
extraction bound.

1. If \(\lambda>\ell\), some phase variable belongs to at least
   \(\ell+1\) recurrent corrections.  If every alphabet has size at
   most \(h\), at least
   \[
   \boxed{
   \left\lceil\frac{\ell+1}{h-1}\right\rceil
   }
   \]
   of those corrections install the same noncurrent action literal.
2. If \(\lambda\leq\ell\), the recurrent class contains a
   pairwise support-disjoint subfamily \(\mathcal J\) with
   \[
   \boxed{
   \sum_{i\in\mathcal J}w_i
   \geq
   \frac1{s\ell}
   \sum_{i\in\mathcal I}w_i.
   }
   \]

### Proof

The first assertion is the definition of \(\lambda\), followed by
pigeonholing the at most \(h-1\) noncurrent target labels.

For the second assertion, a support \(E_i\) meets at most

\[
\sum_{v\in E_i}(\lambda-1)
\leq s(\ell-1)
\]

other supports.  Thus the intersection graph has maximum degree at
most \(s(\ell-1)\) and has a greedy proper colouring with at most

\[
s(\ell-1)+1\leq s\ell
\]

colours.  Each colour class has pairwise disjoint supports.  The
heaviest class carries at least the displayed fraction of the total
weight. \(\square\)

The first output rejoins the action-literal-kernel branch of OP3h.
The second output is a protected correction bank: because every centre
was generated at the same \(\omega\), its components can be
independently left in their common current orientation or switched to
their correction orientation.

## Protected binary correction banks

Let \(\omega\) be the current phase assignment.  For
\(i=1,\ldots,m\), let

\[
\rho_i:E_i\longrightarrow\mathcal A
\]

be a correction with

\[
\rho_i(v)\ne\omega(v)
\quad(v\in E_i),
\qquad
E_i\cap E_j=\varnothing
\quad(i\ne j).
\]

Introduce an orientation variable \(x_i\in\{0,1\}\).  Orientation zero
keeps \(\omega\) on \(E_i\), and orientation one installs \(\rho_i\).
All variables outside \(\bigcup_iE_i\) remain fixed.

Retain the complete canonical factor family from OP1a, including every
external factor preserved by OP2n.  A factor \(Q\) forbids one partial
assignment \(\alpha_Q\) on a scope \(S_Q\) of size at most three.

For one factor, inspect each protected support it meets.

- If a fixed outside variable disagrees with \(\alpha_Q\), the factor
  can never be violated and contributes no clause.
- If different variables of one \(E_i\) require different
  orientations, the factor can never be violated and contributes no
  clause.
- Otherwise every met support \(E_i\) has one required orientation
  \(\varepsilon_i(Q)\).  Add the clause
  \[
  \boxed{
  \bigvee_{i:S_Q\cap E_i\ne\varnothing}
  (x_i\ne\varepsilon_i(Q)).
  }
  \]
- If a violated factor is supported wholly outside the bank, this is
  the empty clause.

Write \(\Psi(\omega,\{\rho_i\})\) for the conjunction of all resulting
clauses, retaining the source-factor identity on every clause.

## OP4a -- exact protected-bank projection

### Theorem OP4a -- PROVED

For every orientation \(x\in\{0,1\}^m\), the following are equivalent.

1. The corresponding protected-bank phase state violates no canonical
   factor.
2. The orientation \(x\) satisfies
   \(\Psi(\omega,\{\rho_i\})\).

Moreover:

- every clause has width at most three;
- a width-three clause comes from a rank-three factor meeting exactly
  three protected supports, once in each support;
- every satisfying orientation preserves the active row and column
  sets of the orbit construction.

### Proof

Fix a factor \(Q\).  Outside the protected supports its phase values
are fixed.  Inside a support \(E_i\), every variable has exactly its
current value in orientation zero and its correction value in
orientation one.  Hence \(Q\) is violated precisely when all fixed
outside values match \(\alpha_Q\) and every support it meets takes its
unique compatible orientation.  The displayed clause is the negation
of exactly that conjunction.

Conjoining over every factor proves the equivalence.  A factor has at
most three variables, so it meets at most three protected supports.
If it meets three, each of its three variables lies in a different
support.  Finally, every orbit phase selects the same active rows and
columns, so changing any collection of block phases preserves
saturation. \(\square\)

This theorem does not ignore collateral.  Its equivalence requires the
complete factor family on the fixed outside state; OP2n is precisely
the interface that retains those external factors.

## OP4b -- rank-two completion and exceptional chains

### Theorem OP4b -- PROVED

Suppose no canonical factor meets three distinct protected supports.
Then \(\Psi\) is a 2-CNF formula and can be decided in time linear in
its implication graph.

Exactly one of the following occurs.

1. The formula is satisfiable, and the returned orientation gives a
   saturated no-three phase state within the protected bank.
2. The formula contains an empty clause, identifying a bad factor
   fixed outside the bank.
3. Some orientation literal \(x_i=\varepsilon\) and its negation lie
   in one strongly connected component.  Directed implication paths
   in both directions give an explicit contradictory order-two chain,
   with every edge labelled by its source geometric factor.

### Proof

OP4a gives width at most two under the hypothesis.  Apply the standard
implication-graph criterion for 2-SAT.  A satisfiable formula gives the
phase state by OP4a.  An empty clause is already false.  Otherwise
unsatisfiability is equivalent to one variable and its negation lying
in the same strongly connected component.  Paths in both directions
inside that component retain the clause labels and form the claimed
certificate. \(\square\)

This is an exact completion theorem, not a small-load condition.
Arbitrarily many blockers are allowed when their alternating
requirements are logically compatible.

## OP4c -- the rank-three transversal boundary

### Theorem OP4c -- PROVED

Every width-three clause of \(\Psi\) retains:

1. its original rank-three geometric factor;
2. the three protected correction supports it meets;
3. the unique forbidden orientation on each support.

Thus the remaining protected-bank instance is an exact 3-CNF whose
rank-three clauses are explicit correction transversals.  A
satisfying assignment is a valid completion by OP4a, but satisfiability
cannot follow from support disjointness and bounded signature
multiplicity alone.

### Proof

The provenance statement is part of the OP4a construction.  A
width-three clause can only arise when a scope of size at most three
meets three different supports, so it has exactly one variable in each
support and one required orientation per support.

For the final warning, take three one-variable binary corrections and
include one canonical rank-three factor forbidding each of their eight
orientation assignments.  The projected formula consists of the eight
width-three clauses and excludes every state.  All correction supports
are disjoint. \(\square\)

The eight-clause example is an abstract canonical phase instance, not
a claim that every orbit geometry realizes it.  Its role is to prove
that the next positive theorem must use the carry, coset, or
denominator labels on the transversals.

## Cross-round interface after OP3k--OP4c

For the factor-fan output of OP3j, put

\[
L
=
\left\lceil
\frac{t}{h^2q(q+1)\Delta_p^\star}
\right\rceil.
\]

Across decoder rounds, Corollary OP3k.1 gives either growth of the
monotone state-qualified signature ledger or a current paid
high-reuse signature class.  No corrections from different snapshots
are mixed.  On the current bounded-support high-reuse class, OP3l
gives either:

1. a deeper repeated action-literal kernel; or
2. a paid support-disjoint protected bank.

OP4a projects the latter without loss.  OP4b either completes its
rank-two part or returns a labelled contradictory implication chain.
OP4c returns every genuinely rank-three residual as an explicit
three-support geometric transversal.

[`orbit-phase-implication-bridge.md`](orbit-phase-implication-bridge.md)
continues both outputs.  OP4d compresses a rank-two contradiction to a
source-labelled implication bicycle.  OP4e audits rather than assumes
the rational quotient law and then applies the one-colour,
order-two-template, or larger-ratio classification.  OP4f returns a
switch-disjoint rank-three matching or a bounded switch kernel whose
conditioned residuals are all OP4b instances.

[`orbit-phase-geometric-labels.md`](orbit-phase-geometric-labels.md)
and
[`orbit-phase-paid-edge-density.md`](orbit-phase-paid-edge-density.md)
continue the rank-two side through OP4g--OP4i.  Every source factor now
has an exact rational/carry record, whole-bicycle literal compatibility
is decided exactly, and factor-conservative fixed-edge payment is
routed to complete rational density, one-sided completion deficits,
heavy source reuse, or carry growth.

[`orbit-phase-rank-three-router.md`](orbit-phase-rank-three-router.md)
and
[`orbit-phase-blocker-ledger.md`](orbit-phase-blocker-ledger.md)
continue the rank-three side through OP4j--OP4k.  Exact
profile/signature records enter a role-tagged state-qualified ledger.
A no-growth matching is localized to one current-old blocker fibre of
at most \(\Delta_p\) point-disjoint factors; externally certified
weight above its finite capacity forces a heavy factor or a new token.

Therefore repeated carry signatures are no longer an anonymous
failure of monotonicity or an excuse to combine incompatible
historical corrections.  At most
\[
|\Omega|
\bigl(
|\Sigma_{\rm fan}|+|\Sigma_3|
\bigr)
\]
role-tagged ledger-growth rounds occur before a current recurrent class
must be processed.  OP4k.3 gives the corresponding OP3b finite-descent
bound after replacing the fan-only token capacity by this combined
capacity.  The remaining frontier consists of five named arithmetic
outputs:

1. high-overlap action-literal kernels;
2. OP4m heavy paid current factors or recurrent role-tagged defect
   signatures;
3. OP4i complete dense fixed-edge RI5 inputs, one-sided completion
   deficits, or its heavy-factor/carry-growth alternatives;
4. OP4k bounded current recurrent rank-three blocker fibres;
5. the wide-support action CSPs already separated by OP3j.

To finish OP2--OP5, these outputs must be shown to expand, to force a
new ledger signature, or to enter one of the classified absorber
interfaces.  No claim that this final arithmetic classification is
already proved is made here.

`scripts/verify_phase_signature_recurrence.py` exhausts small
signature ledgers, state-qualified snapshot traces, and bounded support
systems, checks the paid colour-class extraction, compares
protected-bank projection with direct source-factor evaluation,
compares the implication solver with all assignments on thousands of
2-CNF formulas, retains explicit contradictory paths, and checks both
satisfiable and infeasible rank-three banks.

`scripts/verify_phase_blocker_ledger.py` exhausts the rank-three
role-tagged ledger extension and its divisor-capacity recurrence gate.
