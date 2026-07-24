# Disjoint-arm action projection and scope-complete collateral

OP2l--OP2m turn a failed target phase into one of three concrete
objects: a bounded transversal correction, a paid depth-two literal
kernel, or a large family of residual-disjoint blocker arms.  Two
formal obligations remain before any of these objects can be used in a
decoder:

1. external checks affected by the auxiliary phase changes must be
   retained exactly; and
2. several individually improving corrections may be batched only when
   no hard constraint or soft potential factor couples their supports.

This note closes both obligations.  A disjoint-arm family projects
exactly to another canonical action CSP.  Hard checks remain canonical
nogoods, while soft checks remain a weighted canonical multiset plus
one fixed contribution.  For arbitrary correction candidates, a primal
conflict graph built from their complete supports and every hard or
soft check scope makes joint legality and potential drift exactly
additive on independent sets.

The remaining frontier is geometric rather than bookkeeping: classify
the paid high-degree part of that conflict graph, or prove that it has a
large independent family.

## OP2n -- exact action CSP on residual-disjoint arms

Let \(\omega\) be the current phase assignment.  Fix a centre variable
\(v\), a target phase \(a\ne\omega_v\), and activated blockers

\[
C_1,\ldots,C_m\in\mathcal B_\omega(v,a)
\]

whose residual scopes

\[
R_i=S_{C_i}\setminus\{v\}
\]

are pairwise disjoint.  Choose one action variable

\[
x_i\in R_i
\]

from each arm.  The \(x_i\) are distinct.  Put

\[
A=\{x_1,\ldots,x_m\},
\qquad
\mathcal D_x=\mathcal A_x\setminus\{\omega_x\}
\quad(x\in A).
\]

Every action domain is nonempty in the OP2g irreducible core.  Fix all
nonaction variables by

\[
\eta_v=a,
\qquad
\eta_y=\omega_y
\quad
(y\notin A\cup\{v\}).
\]

Thus an action assignment

\[
b\in\prod_{x\in A}\mathcal D_x
\]

produces the full phase state \(\eta\cup b\).

Let \(\mathcal H\) be a family of hard canonical checks and let
\(\mathcal S\) be a multiset of soft canonical checks with weights
\(w_Q\geq0\).  Residualize any check \(Q\) as follows.

1. If some fixed variable \(y\in S_Q\setminus A\) satisfies
   \[
   \eta_y\ne f_Q(y),
   \]
   mark \(Q\) permanently satisfied.
2. If some action variable \(x\in S_Q\cap A\) has
   \[
   f_Q(x)\notin\mathcal D_x,
   \]
   mark \(Q\) permanently satisfied.
3. Otherwise restrict \(f_Q\) to
   \[
   T_Q=S_Q\cap A.
   \]
   If \(T_Q=\varnothing\), mark \(Q\) forced violated.  If
   \(T_Q\ne\varnothing\), retain the canonical action check
   \[
   Q_A=(T_Q,f_Q|_{T_Q}).
   \]

For hard checks, duplicate and subsumed residuals may subsequently be
removed by OP2g.  For soft checks, identical residuals may be merged by
adding their weights, but a strict extension is not deleted: both
weighted potential factors remain part of the exact value.

### Theorem OP2n -- PROVED

The action projection has all of the following properties.

1. For every original check \(Q\) and every action assignment \(b\),
   \[
   \boxed{
   \mathbf1_{\{(\eta\cup b)|_{S_Q}=f_Q\}}
   =
   \begin{cases}
   0,&Q\text{ is permanently satisfied},\\
   1,&Q\text{ is forced violated},\\
   \mathbf1_{\{b|_{T_Q}=f_Q|_{T_Q}\}},
      &Q_A\text{ is retained}.
   \end{cases}
   }
   \]
2. If no hard check is forced violated, \(\eta\cup b\) is hard-legal
   exactly when \(b\) satisfies every retained hard action check.
3. Let
   \[
   F=
   \sum_{\substack{Q\in\mathcal S\\
                    Q\text{ forced violated}}}w_Q.
   \]
   Then the exact soft potential is
   \[
   \boxed{
   \Phi(\eta\cup b)
   =
   F+
   \sum_{\substack{Q\in\mathcal S\\Q_A\text{ retained}}}
   w_Q\mathbf1_{\{b|_{T_Q}=f_Q|_{T_Q}\}}.
   }
   \]
   In particular,
   \[
   \boxed{
   \Phi(\eta\cup b)-\Phi(\omega)
   =
   F+\Phi_A(b)-\Phi(\omega).
   }
   \]
4. Every selected blocker \(C_i\) is permanently satisfied and
   disappears from both projected families.
5. Every retained action check has rank at most the original check
   rank.  For OP1 checks it therefore has rank at most three.

Hence a residual-disjoint blocker family does not create a new type of
selection problem.  Choosing one action variable per arm converts all
external feasibility and collateral exactly into another canonical
rank-at-most-three phase instance on the noncurrent action domains.

### Proof

If a fixed literal disagrees with \(f_Q\), every extension of \(\eta\)
already satisfies \(Q\).  If an action forbidden value is absent from
its action domain, no permitted action can match that literal, so \(Q\)
is again permanently satisfied.

In the remaining case every fixed literal matches and every action
forbidden value is available.  The full state violates \(Q\) exactly
when all action variables in \(T_Q\) take their forbidden values.  If
there are no such variables, all literals are fixed matches and the
check is forced violated.  Otherwise this is precisely violation of
the retained canonical action check.  This proves the first assertion.

Apply the first assertion to every hard check to obtain exact legality.
Multiplying it by \(w_Q\) and summing over the soft multiset gives the
potential identity.  Merging identical soft residuals by weight
addition preserves that sum.

For a selected blocker \(C_i\), alignment gives

\[
f_{C_i}(x_i)=\omega_{x_i}.
\]

But

\[
\omega_{x_i}\notin\mathcal D_{x_i},
\]

so residualization rule 2 marks \(C_i\) permanently satisfied.
Restriction cannot increase scope size, proving the rank assertion.
\(\square\)

Every action state changes O1 orbit-block phases and therefore
preserves the same active row and column sets.  OP2n does not assert
that its action CSP is automatically satisfiable or improving.  It
makes that question exact and sends it back through OP2g--OP3c without
discarding external checks.

## Exact collateral of one arbitrary correction

Retain a current hard-legal assignment \(\omega\).  A correction
\(\rho\) has support

\[
E(\rho)=\{x:\rho_x\ne\omega_x\}.
\]

Outside \(E(\rho)\), put \(\rho_x=\omega_x\).  Define the affected
hard and soft families by

\[
\mathcal H[E]
=
\{Q\in\mathcal H:S_Q\cap E\ne\varnothing\},
\qquad
\mathcal S[E]
=
\{Q\in\mathcal S:S_Q\cap E\ne\varnothing\}.
\]

### Lemma OP3d -- PROVED

The correction is hard-legal if and only if it violates no check in
\(\mathcal H[E(\rho)]\).  Its exact soft drift is

\[
\boxed{
\Delta_\rho\Phi
=
\sum_{Q\in\mathcal S[E(\rho)]}
w_Q
\left(
\mathbf1_{\{\rho|_{S_Q}=f_Q\}}
-
\mathbf1_{\{\omega|_{S_Q}=f_Q\}}
\right).
}
\]

No check outside the displayed affected families changes status.

### Proof

A check whose scope misses \(E(\rho)\) sees the same phase on every
incident variable under \(\rho\) and \(\omega\).  Its status is
unchanged.  Every hard check outside \(\mathcal H[E]\) remains
satisfied because \(\omega\) is hard-legal.  Summing the status
differences of the affected soft checks gives the drift identity.
\(\square\)

OP3d is the required audit for both OP2l transversal corrections and
OP2n action assignments.  The centre, every auxiliary variable, and
every external check meeting any of them are included.

## OP3e -- scope-complete primal graph for corrections

Let \(\mathcal I\) be a finite family of individually hard-legal
corrections.  Write

\[
E_i=E(\rho_i),
\qquad
\Delta_i=\Delta_{\rho_i}\Phi.
\]

Construct a graph \(G_{\rm corr}\) on \(\mathcal I\).  Distinct
corrections \(i,j\) are adjacent when at least one of the following
holds:

1. their supports overlap:
   \[
   E_i\cap E_j\ne\varnothing;
   \]
2. some hard or soft check \(Q\) meets both supports:
   \[
   S_Q\cap E_i\ne\varnothing,
   \qquad
   S_Q\cap E_j\ne\varnothing.
   \]

Thus every factor spanning two or three corrections induces a clique
on those corrections.

### Theorem OP3e -- PROVED

For every independent set \(J\subseteq\mathcal I\):

1. the supports \(E_i\), \(i\in J\), are pairwise disjoint, so the
   joint assignment
   \[
   \rho_J
   =
   \omega\ \text{with every }\rho_i|_{E_i}\text{ installed}
   \]
   is well-defined;
2. \(\rho_J\) is hard-legal; and
3. the exact potential drift is additive:
   \[
   \boxed{
   \Phi(\rho_J)-\Phi(\omega)
   =
   \sum_{i\in J}\Delta_i.
   }
   \]

In particular, any independent family of individually improving
corrections is a jointly improving row-column-preserving batch.
No current defect or external collateral factor is counted twice.

### Proof

Support-overlap edges prove the first assertion.  Fix any hard or soft
check \(Q\).  If its scope met two supports from \(J\), those
corrections would be adjacent by rule 2.  Hence \(Q\) meets at most one
installed support.

If \(Q\) meets no support, its joint status is its current status.  If
it meets exactly \(E_i\), every incident phase under \(\rho_J\) is the
same as under the individual correction \(\rho_i\): variables in
\(E_i\) use \(\rho_i\), while all other variables of \(Q\) retain
\(\omega\).  Thus its joint status equals its status under
\(\rho_i\).

Every hard check is therefore current-satisfied or satisfied by the
unique individual correction it meets, proving joint legality.  For
soft checks, partition the changed factors by that unique correction
and apply OP3d.  Their signed weights sum to
\(\sum_{i\in J}\Delta_i\).

If one current defect could be destroyed by two corrections, its scope
would meet both supports and create an edge.  The same is true for a
collateral factor affected by two corrections, proving the accounting
statement. \(\square\)

The cross-factor edges are necessary.  Disjoint supports alone do not
give additivity: a rank-two check forbidding \((1,1)\) is unchanged when
either coordinate is changed alone from \((0,0)\), but is created when
both coordinates are changed together to \(1\).

## OP3f -- weighted batch extraction or paid high conflict

Suppose every candidate correction is individually improving and put

\[
g_i=-\Delta_i>0,
\qquad
G=\sum_{i\in\mathcal I}g_i.
\]

Let \(d_i\) be the degree of \(i\) in \(G_{\rm corr}\).

### Theorem OP3f -- PROVED

There is an independent correction batch \(J\) with

\[
\boxed{
\sum_{i\in J}g_i
\geq
\sum_{i\in\mathcal I}\frac{g_i}{d_i+1}.
}
\]

Consequently, if the correction graph has maximum degree \(\Gamma\),
some executable batch retains at least

\[
\boxed{\frac{G}{\Gamma+1}}
\]

of the total individual gain.

At every integer threshold \(D\geq1\), one of the following paid
outputs holds:

1. an executable independent batch has gain at least
   \[
   \boxed{\frac{G}{2D};}
   \]
2. candidates of degree at least \(D\) carry total individual gain
   greater than
   \[
   \boxed{\frac G2.}
   \]

Every edge incident to the second output has an explicit witness: one
shared support variable, or one named hard/soft check whose scope meets
both corrections.  Hence the high-conflict return preserves current
paid gain and concrete canonical incidence; it is not an unweighted
dense graph.

### Proof

Choose a uniformly random ordering of \(\mathcal I\) and retain a
candidate when it occurs before every neighbor.  Two adjacent vertices
cannot both be retained, so the result is independent.  Candidate \(i\)
is earliest in its closed neighborhood with probability
\(1/(d_i+1)\).  The expected retained gain is therefore

\[
\sum_i\frac{g_i}{d_i+1}.
\]

Some ordering attains at least its expectation, proving the first box.
The maximum-degree assertion follows immediately.

For the threshold statement, let

\[
L=\{i:d_i<D\},
\qquad
H=\{i:d_i\geq D\}.
\]

If \(H\) carries gain greater than \(G/2\), conclusion 2 holds.
Otherwise \(L\) carries gain at least \(G/2\).  The induced graph on
\(L\) has maximum degree at most \(D-1\), so a greedy proper coloring
uses at most \(D\) colors.  One color class is independent and carries
gain at least \(G/(2D)\).  OP3e makes it an executable batch with
exactly that gain.

The edge definition itself supplies the stated witnesses. \(\square\)

## Interface after OP2n and OP3d--OP3f

The two formerly informal collateral steps are now finite and
checkable.

1. A large residual-disjoint blocker family becomes an exact canonical
   action CSP.  Selected blockers disappear, while every external hard
   or soft check is retained with its exact status and weight.
2. A bounded transversal correction is audited on its full support by
   OP3d.
3. Several corrections may be combined only through the scope-complete
   graph of OP3e.
4. OP3f either extracts a quantitatively paid improving batch or returns
   more than half of the gain on high-conflict candidates with explicit
   variable/check witnesses.

The remaining OP2--OP3 geometry is now one precise classification
problem: a paid high-degree correction must be routed, by its edge
witnesses, to a carry/coset/denominator kernel or a new
residual-disjoint family.  No further generic additivity, payment, or
external-collateral lemma is missing.

[`orbit-phase-paid-witness-localization.md`](orbit-phase-paid-witness-localization.md)
performs the next finite routing step.  OP3g--OP3i separate paid wide
supports and localize bounded high-degree corrections to
variable-overlap stars, single-factor stars, or variable-rooted factor
fans, with repeated-literal refinements and explicit global payment.
Only the arithmetic classification of the resulting carry-decorated
kernels and fans remains.

`scripts/verify_phase_external_collateral.py` exhausts small action
projections against the original canonical checks, verifies hard
legality and weighted soft-potential identities, checks joint
additivity on every independent correction family, retains the
cross-factor counterexample, and exhausts the weighted batch bounds on
small graphs.
