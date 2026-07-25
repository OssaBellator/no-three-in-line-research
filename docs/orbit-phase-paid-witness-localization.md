# Paid localization of correction conflicts

OP3f returns a quantitatively paid family of high-degree corrections,
and OP3e supplies a variable or factor witness for every conflict edge.
High degree alone is not yet an arithmetic object: its witnesses could
be spread over many variables and many checks.  This note performs the
exact finite localization step.

For bounded correction supports, every high-degree centre has one of
three explicit certificates:

1. many neighbors overlap it at one variable;
2. many support-disjoint neighbors couple to it through one factor; or
3. many distinct coupling factors form a fan through one variable of
   the centre.

The third output is necessary: neither a shared-support star nor a
single-factor star follows from degree alone.  Bounded phase alphabets
refine the first two outputs to a repeated action literal and the third
to a repeated forbidden literal.  A weighted organizer retains a fixed
fraction of the OP3f payment on one certificate type, while explicitly
returning corrections with large support as a separate paid output.

The remaining structural frontier is genuinely arithmetic: classify
the carry, coset, and denominator labels on these repeated-literal
kernels and factor fans.  OP4o later supplies one-centre descent for
every nonempty current paid kernel or wide family, so this
classification is needed for simultaneous completion rather than
basic progress.

## Witness partition around one correction

Retain the current assignment \(\omega\), a finite family
\(\mathcal I\) of nontrivial corrections, and the scope-complete graph
\(G_{\rm corr}\) from OP3e.  Write

\[
E_i=E(\rho_i)\ne\varnothing.
\]

Treat every hard check and every weighted soft-check occurrence as a
factor.  Fix total orders on variables, factors, and corrections.
For a centre \(i\), partition its neighbors as follows.

1. If \(E_i\cap E_j\ne\varnothing\), assign \(j\) to
   \[
   O_i(x),
   \qquad
   x=\min(E_i\cap E_j).
   \]
2. Otherwise OP3e supplies at least one factor meeting both supports.
   Assign \(j\) to
   \[
   P_i(Q),
   \qquad
   Q=\min\{R:S_R\cap E_i\ne\varnothing,\
                 S_R\cap E_j\ne\varnothing\}.
   \]

The sets \(O_i(x)\), \(x\in E_i\), and the nonempty sets \(P_i(Q)\)
are disjoint and partition \(N(i)\).  For every nonempty \(P_i(Q)\),
root \(Q\) at

\[
r_i(Q)=\min(E_i\cap S_Q).
\]

The deterministic choices are only bookkeeping.  Any fixed choices
give the same bounds.

## OP3g -- local kernel-or-fan trichotomy

Fix integers \(s\geq1\), \(t\geq2\), and \(D\geq1\) satisfying

\[
\boxed{D>s\,t(t-1).}
\]

### Theorem OP3g -- PROVED

If

\[
|E_i|\leq s,
\qquad
d_i\geq D,
\]

then at least one of the following holds.

1. **Variable-overlap star.**  Some \(x\in E_i\) has
   \[
   \boxed{|O_i(x)|\geq t.}
   \]
2. **Single-factor star.**  Some factor \(Q\) meeting \(E_i\) has
   \[
   \boxed{|P_i(Q)|\geq t.}
   \]
   Every correction in this bucket is support-disjoint from \(i\).
3. **Variable-rooted factor fan.**  Some \(x\in E_i\) is the root of
   at least \(t\) distinct factors \(Q\) with
   \[
   P_i(Q)\ne\varnothing.
   \]
   Choosing one member of each \(P_i(Q)\) gives \(t\) distinct
   support-disjoint neighbor corrections, each coupled to \(i\)
   through its named factor.

### Proof

Suppose conclusions 1 and 2 both fail.  Since there are at most \(s\)
overlap buckets,

\[
\sum_{x\in E_i}|O_i(x)|
\leq
s(t-1).
\]

At least

\[
D-s(t-1)
\]

neighbors therefore lie in factor buckets.  Each nonempty factor
bucket has size at most \(t-1\), so the number \(q\) of distinct
nonempty factor buckets satisfies

\[
q(t-1)
\geq
D-s(t-1).
\]

The threshold hypothesis gives

\[
D-s(t-1)
>
s(t-1)^2,
\]

and hence

\[
q>s(t-1).
\]

Every one of these \(q\) factors has one root in \(E_i\).  There are at
most \(s\) possible roots, so some root receives more than \(t-1\)
distinct factors.  This is conclusion 3.

The factor buckets partition the nonoverlap neighbors.  Thus selecting
one member from each chosen bucket gives distinct neighbors, and their
supports are disjoint from \(E_i\) by construction. \(\square\)

The strict threshold is useful and honest.  With \(s=1\), one centre
can meet arbitrarily many support-disjoint neighbors through distinct
rank-two factors, one neighbor per factor.  Its degree is large while
every overlap and single-factor bucket has size at most one; the fan
output cannot be omitted.

## Literal refinement of the three certificates

For each variable \(x\), put

\[
h_x=|\mathcal A_x|.
\]

Every \(x\in E_j\) carries the noncurrent action literal

\[
(x,\rho_j(x)),
\qquad
\rho_j(x)\ne\omega_x.
\]

For a factor \(Q\), define the number of action literals on its scope by

\[
A(Q)
=
\sum_{y\in S_Q}(h_y-1).
\]

### Lemma OP3h -- PROVED

Each OP3g certificate has the following canonical refinement.

1. A variable-overlap star \(O_i(x)\) of size at least \(t\) contains
   at least
   \[
   \boxed{\left\lceil\frac{t}{h_x-1}\right\rceil}
   \]
   neighbors which all install the same action literal \((x,b)\).
2. A single-factor star \(P_i(Q)\) of size at least \(t\) contains at
   least
   \[
   \boxed{\left\lceil\frac{t}{A(Q)}\right\rceil}
   \]
   neighbors with one common action literal \((y,b)\) on \(S_Q\).
3. A variable-rooted fan of at least \(t\) distinct factors contains
   at least
   \[
   \boxed{\left\lceil\frac{t}{h_x}\right\rceil}
   \]
   factors whose forbidden tuples all use one common literal
   \((x,a)\).

If every alphabet has size at most \(h\) and every factor has rank at
most \(r\), the three displayed lower bounds are respectively at least

\[
\left\lceil\frac{t}{h-1}\right\rceil,
\qquad
\left\lceil\frac{t}{r(h-1)}\right\rceil,
\qquad
\left\lceil\frac{t}{h}\right\rceil.
\]

### Proof

In conclusion 1 of OP3g, every neighbor in \(O_i(x)\) changes \(x\)
to one of exactly \(h_x-1\) noncurrent phases.  Pigeonhole gives the
first bound.

For every \(j\in P_i(Q)\), choose the least

\[
y\in E_j\cap S_Q
\]

and record \((y,\rho_j(y))\).  There are exactly \(A(Q)\) possible
variable/noncurrent-phase pairs on \(S_Q\), proving the second bound.

Every factor in a fan rooted at \(x\) contains \(x\).  Its forbidden
literal there is one of the \(h_x\) pairs

\[
(x,a),
\qquad
a\in\mathcal A_x.
\]

Pigeonhole proves the third bound.  The uniform estimates follow from
\(h_x\leq h\) and \(|S_Q|\leq r\). \(\square\)

The first two outputs are action-literal kernels among correction
candidates.  The third is a canonical factor-literal star with a named
neighbor correction behind every factor.  Alignment with the current
phase is not asserted; that is now an explicit arithmetic condition to
be proved from the carry decoration rather than assumed.

## OP3i -- paid global organizer

Give every improving correction its gain

\[
g_i=-\Delta_i>0.
\]

Let

\[
\mathcal H_D=\{i:d_i\geq D\},
\qquad
W_D=\sum_{i\in\mathcal H_D}g_i.
\]

Fix \(s,t,D\) with \(D>s\,t(t-1)\).  Call a high-degree correction
**wide** when \(|E_i|>s\).  Classify every nonwide member of
\(\mathcal H_D\) by the first applicable OP3g conclusion in the order
variable star, factor star, factor fan.

### Theorem OP3i -- PROVED

Assume \(W_D>0\).  At least one of the following paid outputs holds.

1. Wide high-degree corrections carry gain greater than
   \[
   \boxed{\frac{W_D}{2}.}
   \]
2. One of the three localized OP3g certificate classes carries gain at
   least
   \[
   \boxed{\frac{W_D}{6}.}
   \]

Consequently, apply OP3f at threshold \(D\) to a correction family of
total gain \(G\).  One of the following holds:

1. an executable correction batch has gain at least
   \[
   \boxed{\frac{G}{2D};}
   \]
2. wide high-degree corrections carry gain greater than
   \[
   \boxed{\frac G4;}
   \]
3. one fixed localized certificate type carries gain greater than
   \[
   \boxed{\frac G{12}.}
   \]

Every centre counted in conclusion 3 retains its individual gain and
comes with the literal-refined certificate of OP3h.

### Proof

If the wide corrections carry more than \(W_D/2\), conclusion 1 holds.
Otherwise the bounded-support high-degree corrections carry at least
\(W_D/2\).  OP3g classifies all of them into three classes, so one
class carries at least one third of that amount, namely \(W_D/6\).

For the consequence, use the executable-batch output of OP3f if it
occurs.  Otherwise OP3f gives

\[
W_D>\frac G2.
\]

The first alternative above then carries more than \(G/4\).  In the
second alternative, its class carries at least \(W_D/6>G/12\).
OP3h refines every certificate without changing the gain attached to
its centre. \(\square\)

## Interface after OP3g--OP3i

The high-conflict return is no longer an unorganized graph.

1. Large correction supports remain visible as a paid wide-support
   output.
2. Bounded corrections return a paid family of repeated action-literal
   kernels or variable-rooted factor-literal fans.
3. Every single-factor or fan incidence retains the exact hard/soft
   factor occurrence and a distinct neighbor correction witness.
4. The generic loss from OP3f through localization is at most a factor
   \(6\) relative to the high-degree payment, or \(12\) relative to the
   total individual gain.

[`orbit-phase-carry-fan-router.md`](orbit-phase-carry-fan-router.md)
performs that inspection for the geometric factor-fan class.
OP1b--OP1e turn its repeated block variable into an actual point-star
and then into divisor-controlled product or cross-carry signature
growth.  OP3j preserves the \(G/12\) centre payment.
[`orbit-phase-signature-recurrence.md`](orbit-phase-signature-recurrence.md)
then proves the first-exposure/high-reuse dichotomy, extracts
support-disjoint recurrent correction banks at one common current
snapshot unless an action kernel deepens, and projects those banks
exactly to rank-at-most-three CNF.  Its state-qualified ledger never
combines historical corrections from different phase assignments.
The remaining structured outputs are the action-literal correction
kernels, wide action CSPs, contradictory implication chains, and
explicit rank-three carry transversals.  OP4o later shows that every
nonempty current paid action-kernel or wide class already contains an
executable improving centre; their unresolved role is the stronger
simultaneous completion or absorber classification.

[`orbit-phase-implication-bridge.md`](orbit-phase-implication-bridge.md)
refines the last two outputs.  It retains a bounded source-labelled
bicycle for every rank-two contradiction, gates the rational
order-two classification on an explicit quotient identity, and turns
rank-three clauses into either a switch-disjoint matching or a bounded
conditioned 2-SAT kernel.

`scripts/verify_phase_paid_witness_localization.py` exhausts small
canonical support/factor systems, checks the local trichotomy and every
literal refinement, verifies the weighted organizer, and retains a
factor-fan example showing why the third conclusion is necessary.
