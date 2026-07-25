# Shared-token phase contraction

AC3h reduces a failed paid-ticket assignment to a support-compatible
family of reopenings which all use one capacity token in one geometric
role.  The token pays only once, so the members of that family cannot be
counted as independently paid.  This note gives an exact no-recycling
interface for roles whose remaining coupling is one bounded phase
variable.

The result is deliberately conditional on a checkable geometric
contract.  It does not assert that every role in the alternating closure
has this form.  Proving that finite role dictionary remains part of AC3.

## Separable phase roles

Fix a paid capacity token \(\pi\), one role label \(\lambda\), and a
support-compatible reopening family \(\mathcal J\).  The token--role
fibre is **separable phase-realized** when the following data and
properties are available.

1. There is one nonempty common phase alphabet
   \[
   \mathcal A=\mathcal A_{\pi,\lambda},
   \qquad
   a=|\mathcal A|.
   \]
2. Every reopening \(j\in\mathcal J\) has a finite private state set
   \(\mathcal X_j\) and a legal relation
   \[
   R_j\subseteq\mathcal A\times\mathcal X_j.
   \]
3. The private geometric supports are pairwise disjoint.  Once one
   common phase \(\alpha\) is fixed, choices
   \((\alpha,x_j)\in R_j\) for all \(j\) install jointly.  All
   row/column collisions, paid-certificate overlap, cross-created
   certificates, and protected-bank interactions have already been
   placed in the AC3h support-conflict graph.
4. Installing such a joint state closes every represented reopening.
   The shared token \(\pi\) is destroyed or discharged once, rather than
   once per member.

Define the extendable-phase message of \(j\) by

\[
M_j=
\{\alpha\in\mathcal A:
 \text{some }x\in\mathcal X_j
 \text{ has }(\alpha,x)\in R_j\}.
\]

The whole fan has common message

\[
M(\mathcal J)=\bigcap_{j\in\mathcal J}M_j.
\]

This is the star specialization of the variable-separator message in a
factor-incidence tree: all factors meet at the common phase and have
otherwise private variables.

## AC3p -- exact fan contraction

### Theorem AC3p -- PROVED

For every finite separable phase-realized fan:

1. a joint legal state exists if and only if
   \[
   \boxed{M(\mathcal J)\ne\varnothing;}
   \]
2. there is a subfamily
   \(\mathcal J_0\subseteq\mathcal J\) satisfying
   \[
   \boxed{
   |\mathcal J_0|
   \leq
   a-|M(\mathcal J)|,
   \qquad
   \bigcap_{j\in\mathcal J_0}M_j=M(\mathcal J);
   }
   \]
3. in particular, an infeasible fan has an infeasible witness on at
   most \(a\) reopenings.

Thus arbitrary fan multiplicity cannot create an arbitrarily large
feasibility obstruction.  It either admits one joint product state, or
contracts to a bounded exceptional core.

### Proof

If a joint state exists, its common phase belongs to every \(M_j\), so
it belongs to their intersection.  Conversely, take
\(\alpha\in M(\mathcal J)\).  For each \(j\), choose
\(x_j\in\mathcal X_j\) with \((\alpha,x_j)\in R_j\).  Separability makes
these choices jointly installable.

For every phase
\(\alpha\in\mathcal A\setminus M(\mathcal J)\), choose one reopening
\(j(\alpha)\) for which \(\alpha\notin M_{j(\alpha)}\), and let
\(\mathcal J_0\) be the set of chosen reopenings.  It uses at most one
representative for each excluded phase, proving the cardinality bound.
Every phase in \(M(\mathcal J)\) belongs to every message, while every
phase outside it is rejected by its chosen representative.  Hence the
two intersections are equal. \(\square\)

The contraction preserves the exact feasible common-phase set.  It
does not discard the collateral contributed by the other private
supports; that numerical issue is handled next.

## Additive collateral interface

Suppose a common phase \(\alpha\) has a certified fixed collateral
bound \(f(\alpha)\geq0\).  Give every local legal state a certified
private bound

\[
c_j(\alpha,x)\geq0.
\]

Assume the separability contract certifies joint collateral at most

\[
f(\alpha)+
\sum_{j\in\mathcal J}c_j(\alpha,x_j).
\]

Put

\[
c_j^\star(\alpha)
=
\min\{
c_j(\alpha,x):
(\alpha,x)\in R_j
\},
\]

with \(c_j^\star(\alpha)=+\infty\) when
\(\alpha\notin M_j\), and define

\[
\boxed{
B(\mathcal J)
=
\min_{\alpha\in M(\mathcal J)}
\left(
f(\alpha)+
\sum_{j\in\mathcal J}c_j^\star(\alpha)
\right).
}
\]

Set \(B(\mathcal J)=+\infty\) when the common message is empty.

### Corollary AC3p.1 -- PROVED

The best certified joint-state collateral is exactly the displayed
minimum of the additive bounds.  If the shared token carries current
destroyed-incidence weight \(w(\pi)>0\), every joint state discharges it,
and

\[
\boxed{B(\mathcal J)<w(\pi),}
\]

then some joint state strictly lowers the corresponding potential.

If the sufficient inequality fails while
\(M(\mathcal J)\ne\varnothing\), the obstruction is the explicit finite
phase profile

\[
\boxed{
f(\alpha)+
\sum_{j\in\mathcal J}c_j^\star(\alpha)
\geq w(\pi)
\quad
\text{for every }\alpha\in M(\mathcal J).
}
\]

### Proof

For fixed \(\alpha\), private states have no remaining coupling, so
choosing a local minimizer independently for every \(j\) realizes the
sum of the certified local minima.  Minimize over the common feasible
phases.  The strict comparison with the once-destroyed paid weight gives
the improving state.  Failure of the strict comparison means the
quantity at every feasible phase is at least \(w(\pi)\). \(\square\)

This corollary does not call the last profile an improvement.  It is the
precise phase-by-phase collateral concentration which the AC1/AC2
arithmetic labels must classify or pay.

## AC3q -- finite phase-loss tickets

Consider reopenings in one fixed token--role fibre arriving in an order
\(j_1,j_2,\ldots\).  Record

\[
M_0=\mathcal A,
\qquad
M_t=M_{t-1}\cap M_{j_t},
\]

and define

\[
\boxed{
\Xi_{\rm phase}(t)=a-|M_t|.
}
\]

### Theorem AC3q -- PROVED

The phase potential is integer-valued, nondecreasing, and lies in
\([0,a]\).  A strict message loss

\[
M_t\subsetneq M_{t-1}
\]

increases it by at least one.  Consequently one token--role fibre has
at most \(a\) strict phase-loss events.

If \(M_t=\varnothing\), the reopenings seen so far contain an infeasible
subfamily of size at most \(a\).  If
\(M_t=M_{t-1}\), then

\[
\boxed{M_{t-1}\subseteq M_{j_t},}
\]

so the new reopening is message-redundant: it removes no common phase
and cannot consume another feasibility ticket.  For every
\(\alpha\in M_t\), it can instead be completed privately and included
in the aggregate collateral calculation of AC3p.1.

### Proof

Intersection can only delete phases.  Every strict inclusion deletes
at least one, so \(a-|M_t|\) strictly increases and can do so at most
\(a\) times.  The empty-message witness is AC3p.  Finally,
\(M_{t-1}\cap M_{j_t}=M_{t-1}\) is equivalent to
\(M_{t-1}\subseteq M_{j_t}\); the definition of \(M_{j_t}\) supplies a
private extension for each surviving common phase. \(\square\)

If every token has at most \(T\) phase-realized roles and every such
alphabet has size at most \(a_{\max}\), the total strict phase-loss
ticket budget over a unit-token set \(\mathcal P^\ast\) is therefore

\[
\boxed{
R_{\rm phase}
\leq
a_{\max}T|\mathcal P^\ast|.
}
\]

This total bound applies when the closure retains the historical
intersection \(M_t\) monotonically for each token--role fibre.  A
transition which enlarges \(M_t\) is a genuine support reopening, not a
phase-loss event, and must be paid separately by AC3e; AC3q does not
hide such resets.  With this persistence contract and
\(a_{\max}=p^{o(1)}\), the display has the required subpolynomial
per-token scale for AC3b--AC3e.  Message-redundant reopenings are also
not hidden inside the budget: they must be installed jointly under
AC3p.1, returned as its explicit collateral profile, or delegated by a
terminal arithmetic label.

## AC3r -- composition with the Hall output

### Corollary AC3r -- PROVED

Apply AC3h to a high-reuse token and one of its same-role label classes.
For every conflict threshold \(\Gamma\), at least one of the following
holds:

1. one reopening has more than \(\Gamma\) same-fibre support conflicts;
2. the selected role is not yet proved separable phase-realized and is
   returned to the finite role-dictionary obligation;
3. a support-compatible phase-realized fan has a joint improving state
   certified by
   \(B(\mathcal J)<w(\pi)\);
4. it has an infeasible exceptional core of size at most
   \(a=|\mathcal A_{\pi,\lambda}|\);
5. it returns the explicit phase-collateral profile of AC3p.1.

Along a sequential closure which preserves the historical common
message, conclusions 3--5 are supplemented by the exact audit that only
strict phase losses consume tickets, with at most \(a\) such losses in
the fibre.  Any message enlargement is explicitly returned to AC3e as
a separately paid reopening.

### Proof

AC3h supplies either conclusion 1 or a support-compatible same-token,
same-role fan.  If the role has not met the separability contract, this
is conclusion 2.  Otherwise apply AC3p and AC3p.1.  A nonempty common
message gives either conclusion 3 or 5; an empty message gives
conclusion 4.  AC3q proves the sequential ticket assertion.
\(\square\)

## Remaining role-dictionary obligation

AC3p--AC3r close the abstract no-recycling combinatorics for every
separable phase-realized shared-token role.  The geometry must still
prove that each actual role returned by AC3h is one of:

1. separable phase-realized with a \(p^{o(1)}\)-sized alphabet and an
   additive collateral certificate;
2. anchor-realized, entering AC3k--AC3o;
3. terminally labelled by a carry, bounded denominator, rational
   quotient, or finite exceptional state.

[`alternating-core-canonical-role-dictionary.md`](alternating-core-canonical-role-dictionary.md)
proves AC3s--AC3u for canonical phase-block certificate tokens.  Their
common scope has rank at most three.  Literal-invariant roles compress
to at most seven nonzero mismatch states; exact-phase roles use at most
\(h^3-1\) states, and failure of compression returns two same-mismatch
phases together with one local legality or cost discrepancy.  The
scope-completeness and additive-collateral hypotheses are discharged by
AC3v--AC3w in
[`alternating-core-primal-conflict-completion.md`](alternating-core-primal-conflict-completion.md):
project every exact factor and constraint scope onto its repair
envelopes.  AC3x sends a dense canonical graph to a paid finite
structural label.

AC3y--AC3z in
[`alternating-core-phase-sensitivity-localization.md`](alternating-core-phase-sensitivity-localization.md)
replace the raw exact alphabet by its coordinate observational quotient
and replace every multi-block sensitivity witness by a one-block
derivative.  A proposed arithmetic chart either determines all
relations and costs or exposes an explicit same-chart derivative.

AC3aa--AC3ac in
[`alternating-core-orbit-literal-charts.md`](alternating-core-orbit-literal-charts.md)
resolve this audit for canonical O1/OP1a checks.  The exact chart
isolates only active hard and soft phase literals.  Its thresholded
version keeps hard relations exact and charges less than \(2\tau\) for
one light-coordinate collateral derivative, while a large exact O1
channel is proved to be a genuine \(h\)-label obstruction.  The
AC3ad--AC3af continuation in
[`alternating-core-literal-star-router.md`](alternating-core-literal-star-router.md)
closes any target bucket already localized to the current context by
exact drift and a rank-two residual matching/transversal audit.  The
remaining geometric check is therefore context localization of the
global hard/heavy literal family and structured classification of its
paid depth-two or residual-disjoint output.

The important remaining numerical case is no longer an unbounded fan.
It is the finite phase-collateral profile in AC3p.1.  Repeated factors
which preserve the common message cannot masquerade as fresh progress.

`scripts/verify_ac_shared_token_phase.py` exhausts small message
families, checks the bounded core and phase-loss potential, and compares
the additive message formula with brute-force private-state products.
`scripts/verify_ac_orbit_literal_charts.py` separately checks the exact
canonical charts, thresholded derivative bounds, and O1 lower bound.
`scripts/verify_ac_literal_star_router.py` checks the localized
hard/soft bucket drift, rigid residual coordinates, and quantitative
paid matching alternative.
