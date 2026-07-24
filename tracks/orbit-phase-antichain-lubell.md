# Lubell bound for irreducible canonical phase checks

OP2g reduces the canonical forbidden partial assignments to an
antichain under extension.  That irreducibility has an exact weighted
size bound, including nonuniform current phase domains.

Let \(V\) be a set of \(n\) variables with nonempty domains
\(\mathcal A_v\).  A realizable canonical nogood \(C\) consists of a
scope \(S_C\subseteq V\) and one forbidden label
\(f_C(v)\in\mathcal A_v\) for each \(v\in S_C\).  Order nogoods by
extension:

\[
C\preceq C'
\quad\Longleftrightarrow\quad
S_C\subseteq S_{C'}
\ \text{and}\
f_{C'}|_{S_C}=f_C.
\]

## OP2h -- canonical Lubell inequality

### Theorem OP2h -- PROVED

If a family \(\mathcal C\) of nonempty realizable canonical nogoods is
an antichain, then

\[
\boxed{
\sum_{C\in\mathcal C}
\frac1{
\binom n{|S_C|}
\prod_{v\in S_C}|\mathcal A_v|
}
\leq1.
}
\]

For a common alphabet of size \(h\), if \(M_k\) checks have arity \(k\),
then

\[
\boxed{
\sum_{k=1}^n
\frac{M_k}{\binom nk h^k}
\leq1.
}
\]

After OP2g, the sum starts at \(k=2\); for the rank-at-most-three OP1
checks,

\[
\boxed{
\frac{M_2}{\binom n2 h^2}
+
\frac{M_3}{\binom n3 h^3}
\leq1.
}
\]

### Proof

Choose independently:

1. a uniformly random full assignment
   \(a\in\prod_v\mathcal A_v\);
2. a uniformly random ordering of the \(n\) variables.

Reveal \(a\) in that order.  The restrictions to the first
\(k=0,\ldots,n\) variables form a maximal chain in the partial-assignment
poset.  A fixed nogood \(C\) of arity \(k\) lies on the chain exactly
when its scope is the first \(k\)-set and the full assignment agrees
with its labels.  This has probability

\[
\frac1{\binom nk}
\prod_{v\in S_C}\frac1{|\mathcal A_v|}.
\]

An antichain meets every maximal chain at most once.  The expected
number of its members on the random chain is therefore at most one.
Linearity of expectation gives the first box; the other displays are
specializations. \(\square\)

## Consequence for the OP2 frontier

The inequality is sharp: all realizable nogoods of any one fixed arity
form an antichain and have total Lubell mass one.  Thus OP2g cannot by
itself force a subcubic number of rank-three checks.  It does, however,
give a normalized global budget that every irreducible arithmetic
Tanner core must obey.  In particular, any proposed expansion or
local-load argument may charge a check by

\[
\left(
\binom n{|S_C|}
\prod_{v\in S_C}|\mathcal A_v|
\right)^{-1}
\]

without hidden multiplicity from subsumed patterns.

This identifies a real limitation as well as progress: antichain
preprocessing removes redundancy, but new arithmetic input is necessary
to turn the unit Lubell budget into private checks or a structured
absorber.

## OP2i -- Lubell load localization

Give each irreducible check its OP2h weight

\[
w(C)
=
\frac1{
\binom n{|S_C|}
\prod_{v\in S_C}|\mathcal A_v|
}.
\]

For a variable and a phase literal define

\[
\lambda(v)=\sum_{C:v\in S_C}w(C),
\qquad
\lambda(v,a)
=
\sum_{\substack{C:v\in S_C\\f_C(v)=a}}w(C).
\]

### Theorem OP2i -- PROVED

If every check has arity at most \(r\), then

\[
\boxed{
\sum_{v\in V}\lambda(v)
=
\sum_{C\in\mathcal C}|S_C|w(C)
\leq r,
}
\]

and

\[
\boxed{
\sum_{a\in\mathcal A_v}\lambda(v,a)=\lambda(v).
}
\]

Consequently, for every \(\theta>0\), the heavy-variable kernel

\[
H_\theta=\{v:\lambda(v)\geq\theta\}
\]

satisfies, together with the heavy-literal set

\[
L_\theta
=
\{(v,a):\lambda(v,a)\geq\theta\},
\]

the bounds

\[
\boxed{
|H_\theta|\leq r/\theta,
\qquad
|L_\theta|\leq r/\theta.
}
\]

Every variable outside \(H_\theta\) has normalized incident check load
less than \(\theta\).  Moreover, some variable \(v\) and one of its
phases \(a\) satisfy

\[
\boxed{
\lambda(v)\leq\frac rn,
\qquad
\lambda(v,a)\leq\frac r{n|\mathcal A_v|}.
}
\]

For a common \(h\)-phase alphabet and rank-two/three checks, the exact
load formula is

\[
\lambda(v)
=
\frac{M_2(v)}{\binom n2h^2}
+
\frac{M_3(v)}{\binom n3h^3},
\]

so \(|H_\theta|\leq3/\theta\).

### Proof

Double-count weighted check--variable incidences:

\[
\sum_v\lambda(v)=\sum_C|S_C|w(C).
\]

OP2h gives \(\sum_Cw(C)\leq1\), and
\(|S_C|\leq r\), proving the first box.  Partitioning the checks
incident with \(v\) according to their forbidden label at \(v\) gives
the literal identity.  The total of all literal loads is therefore also
at most \(r\).  Each heavy variable or heavy literal contributes at
least \(\theta\) to its corresponding sum, proving both kernel bounds.
Finally, averaging the variable loads gives a variable with load at most
\(r/n\), and averaging its load among its
\(|\mathcal A_v|\) literals gives the last assertion. \(\square\)

The constants are sharp at the normalized scale: the complete layer of
all arity-\(r\) canonical assignments has Lubell mass one,
\(\lambda(v)=r/n\), and, for a common alphabet,
\(\lambda(v,a)=r/(nh)\).

OP2i supplies a bounded-kernel/low-load dichotomy for the irreducible
core.  At any fixed threshold, every normalized heavy variable lies in
an explicitly enumerable set of at most \(r/\theta\) variables; every
remaining variable is already below the chosen local-load threshold.
It does not claim that this load remains unchanged after conditioning
on the kernel, so arithmetic expansion is still needed to control the
conditioned residual or classify the heavy kernel.

## OP2j -- exact conditioning amplification

Fix a variable set \(H\subseteq V\) of size \(f\) and an assignment
\(\alpha\) on \(H\).  Condition every canonical nogood on \(\alpha\):
a check is deleted if one of its fixed literals disagrees with
\(\alpha\), and otherwise its literals in \(H\) are removed.  An empty
survivor is an immediate contradiction certificate.  In the remaining
case, delete duplicate and subsumed residual checks as in OP2g and call
the resulting antichain \(\mathcal C_\alpha\).

For a surviving original check \(C\), put

\[
k=|S_C|,
\qquad
j=|S_C\cap H|,
\qquad
D=C|_{V\setminus H}.
\]

Define

\[
\boxed{
\Lambda_H(C)
=
\frac{\binom nk}{\binom{n-f}{k-j}}
\prod_{v\in S_C\cap H}|\mathcal A_v|.
}
\]

### Theorem OP2j -- PROVED

Before duplicate/subsumption deletion, the residual check has exactly

\[
\boxed{
w_{V\setminus H}(D)=\Lambda_H(C)\,w_V(C).
}
\]

Consequently,

\[
\boxed{
\sum_{D\in\mathcal C_\alpha}w_{V\setminus H}(D)
\leq
\sum_{\substack{C\in\mathcal C\\C\text{ survives }\alpha}}
\Lambda_H(C)w_V(C),
}
\]

and, for every \(v\notin H\),

\[
\boxed{
\lambda_\alpha(v)
\leq
\sum_{\substack{C\text{ survives }\alpha\\v\in S_C}}
\Lambda_H(C)w_V(C).
}
\]

If all original checks have rank at most \(r\), the amplified source
sum is partitioned by at most

\[
\boxed{
P(f,r)=
\sum_{j=0}^{\min\{f,r-1\}}\binom fj
}
\]

intersection patterns \(S_C\cap H\).  Therefore residual Lubell mass
\(M_\alpha\) forces one fixed kernel-intersection pattern to carry at
least \(M_\alpha/P(f,r)\) amplified source mass.

For checks disjoint from \(H\),

\[
\Lambda_H(C)
=
\frac{\binom nk}{\binom{n-f}k}
\leq
\left(\frac n{n-f-r+1}\right)^r
\]

whenever \(n-f\geq r\).  Thus bounded conditioning changes the
disjoint-check mass by \(1+O_r(f/n)\); any much larger amplification
must come from checks meeting the heavy kernel.

### Proof

The original and residual weights are

\[
w_V(C)
=
\frac1{\binom nk
\prod_{v\in S_C}|\mathcal A_v|},
\qquad
w_{V\setminus H}(D)
=
\frac1{\binom{n-f}{k-j}
\prod_{v\in S_C\setminus H}|\mathcal A_v|}.
\]

Their ratio is exactly \(\Lambda_H(C)\).  Every canonical residual check
has at least one surviving ancestor.  Choose one; its exact identity
proves the first two inequalities, while summing only checks containing
\(v\) proves the load inequality.

A nonempty residual has \(j\leq r-1\), so its kernel intersection is one
of the \(P(f,r)\) subsets.  Pigeonholing the amplified source sum, which
is at least \(M_\alpha\), proves the pattern localization.  Finally,

\[
\frac{\binom nk}{\binom{n-f}k}
=
\prod_{i=0}^{k-1}\frac{n-i}{n-f-i}
\]

and \(k\leq r\) gives the displayed disjoint-check bound. \(\square\)

OP2j identifies the only conditioning hazard left after OP2i.  Either
the low-load residual remains quantitatively low, or one explicit
intersection pattern with the bounded heavy kernel carries the
amplified obstruction.  Unary or empty residuals continue through the
exact OP2g propagation interface.

`scripts/verify_phase_antichain_lubell.py` exhaustively checks small
binary and nonuniform-domain antichains and verifies equality for every
complete fixed-rank layer.  It also checks the variable/literal
double-count identities, every rational heavy-kernel threshold in the
test range, the sharp complete-layer loads, and the exact
conditioning-amplification formula after residual canonicalization.
