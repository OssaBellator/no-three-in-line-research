# Minimal Hall cores and second-order paid reuse

AC3f--AC3h reduce failure of the reopening ticket assignment to a paid
capacity token used by many same-role reopenings.  The resulting fan is
still paid only once.  This note extracts more information from the
Hall-deficient component itself: after passing to an inclusion-minimal
deficient family, every payment token is reused, and the labelled
eligibility graph has a forced amount of second-order collision mass.

Work in the unit-token graph obtained by splitting every paid resource
\(\pi\) into its \(c_\pi\) capacity copies as in AC3f.  Let
\(\mathcal J\) be the reopening vertices and \(\mathcal P^\ast\) the
capacity tokens.  A reopening \(j\) has a nonempty eligibility set
\(A_j\subseteq\mathcal P^\ast\).  Assume

\[
|A_j|\geq L
\]

for every reopening.  Each eligibility incidence \((j,\tau)\) has one
of at most \(T\) geometric role labels.

## AC3i -- the minimal deficient core has forced role collisions

Suppose Hall fails.  Choose an inclusion-minimal nonempty family
\(\mathcal X\subseteq\mathcal J\) with

\[
|N(\mathcal X)|<|\mathcal X|.
\]

Put

\[
m=|\mathcal X|.
\]

For \(\tau\in N(\mathcal X)\) and a role label \(\lambda\), define

\[
d_{\tau,\lambda}
=
\bigl|
\{j\in\mathcal X:
 \tau\in A_j,\quad
 \operatorname{lab}(j,\tau)=\lambda\}
\bigr|.
\]

Let

\[
\mathcal C
=
\sum_{\tau,\lambda}
\binom{d_{\tau,\lambda}}2
\]

be the role-pure token collision mass.  Define

\[
B=T(m-1),
\qquad
E_0=Lm,
\]

and write

\[
E_0=qB+r,
\qquad
0\leq r<B.
\]

Finally put

\[
\boxed{
\mathfrak C_T(L,m)
=
B\binom q2+rq.
}
\]

### Theorem AC3i -- PROVED

The minimal deficient core satisfies

\[
\boxed{
m\geq2,
\qquad
|N(\mathcal X)|=m-1.
}
\]

For every \(j\in\mathcal X\),

\[
\boxed{
N(\mathcal X\setminus\{j\})=N(\mathcal X).
}
\]

Consequently every capacity token in \(N(\mathcal X)\) is eligible for
at least two reopenings of \(\mathcal X\), and \(L\leq m-1\).

The labelled second-order mass obeys the exact universal bound

\[
\boxed{
\mathcal C\geq\mathfrak C_T(L,m).
}
\]

For two distinct reopenings define their same-token, same-role
codegree by

\[
c(j,k)
=
\bigl|
\{\tau:
 \tau\in A_j\cap A_k,\quad
 \operatorname{lab}(j,\tau)
 =
 \operatorname{lab}(k,\tau)\}
\bigr|,
\]

and define the role-collision load at \(j\) by

\[
\kappa(j)
=
\sum_{\tau\in A_j}
\left(
d_{\tau,\operatorname{lab}(j,\tau)}-1
\right).
\]

Then

\[
\boxed{
\sum_{\{j,k\}\subseteq\mathcal X}c(j,k)=\mathcal C,
\qquad
\sum_{j\in\mathcal X}\kappa(j)=2\mathcal C.
}
\]

In particular, some reopening and some reopening pair satisfy

\[
\boxed{
\kappa(j)
\geq
\left\lceil
\frac{2\mathfrak C_T(L,m)}m
\right\rceil,
}
\]

\[
\boxed{
c(j,k)
\geq
\left\lceil
\frac{\mathfrak C_T(L,m)}{\binom m2}
\right\rceil.
}
\]

When \(L\geq T\), the convenient coarse estimate

\[
\boxed{
\mathcal C
\geq
\frac{Lm}{2}
\left(
\frac{Lm}{T(m-1)}-1
\right)
}
\]

also holds.  Hence some reopening has

\[
\boxed{
\kappa(j)
\geq
L
\left(
\frac{Lm}{T(m-1)}-1
\right).
}
\]

In particular \(L\geq2T\) forces \(\kappa(j)>L\).

### Proof

A one-vertex family cannot be deficient because every reopening has a
nonempty eligibility set.  Thus \(m\geq2\).  Minimality says that every
proper subfamily satisfies Hall.  For \(j\in\mathcal X\),

\[
|N(\mathcal X\setminus\{j\})|
\geq m-1.
\]

This neighbourhood is contained in \(N(\mathcal X)\), while deficiency
gives \(|N(\mathcal X)|\leq m-1\).  Both inequalities are equalities,
proving the first two boxes.

If a token \(\tau\) were adjacent only to \(j\), it would disappear from
\(N(\mathcal X\setminus\{j\})\), contradicting equality of the two
neighbourhoods.  Thus every token has degree at least two.  Every
reopening sees only the \(m-1\) tokens in the core neighbourhood, so
\(L\leq m-1\).

Let \(E\) be the number of eligibility incidences in the core.  The
minimum-degree hypothesis gives \(E\geq Lm=E_0\).  The incidences occupy
at most \(B=T(m-1)\) token--role bins; pad with empty bins if fewer
labels occur.  Among \(B\) nonnegative integer bin loads with fixed sum
\(E_0=qB+r\), the sum of \(\binom d2\) is minimized when \(r\) bins have
load \(q+1\) and the rest have load \(q\).  Indeed, moving one incidence
from a bin at least two larger than another strictly decreases the
pair count.  The minimum is

\[
r\binom{q+1}2+(B-r)\binom q2
=
B\binom q2+rq.
\]

The minimum is nondecreasing with the total number of incidences, so
the actual loads with \(E\geq E_0\) prove
\(\mathcal C\geq\mathfrak C_T(L,m)\).

Every role-pure collision consists of one unordered reopening pair and
one common token, proving the codegree identity.  Counting the same
collision at its two reopening endpoints proves the load identity.
Averaging gives the two displayed maxima.

For the coarse estimate, Cauchy--Schwarz over the \(B\) token--role bins
gives

\[
\mathcal C
=
\frac12\left(\sum_{\tau,\lambda}d_{\tau,\lambda}^2-E\right)
\geq
\frac12\left(\frac{E^2}{B}-E\right).
\]

When \(L\geq T\), one has \(E_0>B\), so the final expression is
increasing for \(E\geq E_0\).  Substitute \(E_0=Lm\) and
\(B=T(m-1)\).  The collision-load estimate follows from
\(\max_j\kappa(j)\geq2\mathcal C/m\).  If \(L\geq2T\), then

\[
\frac{Lm}{T(m-1)}>2,
\]

so the final lower bound is strictly greater than \(L\).
\(\square\)

## AC3j -- square-root routing of the collision load

Fix any reopening \(j\) and abbreviate

\[
\kappa=\kappa(j).
\]

A token incident with \(j\) is **colliding** when its token--role bin
contains another reopening.

### Theorem AC3j -- PROVED

For every integer \(D\geq1\), one of the following holds.

1. **Shared-token fan.**  One capacity token \(\tau\) is used in the
   same role as at \(j\) by more than \(D\) other reopenings.
2. **Role-pure resource star.**  For one role label \(\lambda\), the
   reopening \(j\) is incident with at least
   \[
   \boxed{
   \left\lceil\frac{\kappa}{DT}\right\rceil
   }
   \]
   distinct colliding capacity tokens carrying label \(\lambda\).

If capacity tokens come from underlying charging resources of capacity
at most \(\rho\), the second outcome contains at least

\[
\boxed{
\left\lceil
\frac1\rho
\left\lceil\frac{\kappa}{DT}\right\rceil
\right\rceil
}
\]

distinct underlying resources.  When those resources are current
syndrome incidences or original certificates, this is a genuinely paid
role-pure star.  Finite exceptional-state resources remain explicitly
classified as such.

In particular, put

\[
s=
\left\lfloor
\sqrt{\frac{\kappa}{T}}
\right\rfloor.
\]

When \(s\geq1\), either one same-role token is shared with more than
\(s\) other reopenings, or one reopening role contains at least \(s\)
distinct colliding capacity tokens, and hence at least
\(\lceil s/\rho\rceil\) underlying charging resources.

### Proof

For a token \(\tau\in A_j\), its contribution to \(\kappa\) is

\[
d_{\tau,\operatorname{lab}(j,\tau)}-1.
\]

If the first outcome fails, every positive contribution is at most
\(D\).  Therefore at least \(\lceil\kappa/D\rceil\) distinct tokens
make a positive contribution.  Pigeonholing their labels among at most
\(T\) roles gives at least
\(\lceil\kappa/(DT)\rceil\) tokens in one role.

At most \(\rho\) capacity copies can come from one underlying charging
resource, proving the resource count.  For the final statement take
\(D=s\).  Since \(s^2\leq\kappa/T\),

\[
\frac{\kappa}{sT}\geq s,
\]

so the paid-star alternative has at least \(s\) capacity tokens.
\(\square\)

## Interface to the remaining geometry

AC3i--AC3j replace an arbitrary Hall-deficient bipartite graph by two
explicit second-order outputs.

- A shared-token fan is exactly the AC3h input.  Applying its support
  conflict threshold gives either a second-order installation overload
  or a broad support-compatible same-token, same-role fan.  AC3p--AC3r
  contract the latter to one common phase message whenever its role is
  separable phase-realized: it has a joint state or an infeasible core
  of at most the phase-alphabet size, and only strict phase losses
  consume tickets.
- A role-pure resource star has one reopened object incident with many
  distinct underlying resources, up to the explicit capacity loss
  \(\rho\).  For current syndrome or certificate resources this is
  genuine paid input for the AC1 anchor-link, carry/denominator, BDA, or
  rational-quotient classifiers; exceptional-state resources retain
  their finite classification.

Thus the remaining no-recycling theorem no longer has to interpret an
arbitrary Hall witness.  It must classify only a same-token role fan or
one role-pure current-incidence concentration at a single reopening.
For the same-token branch, the remaining work is the finite geometric
role dictionary and the explicit phase-collateral profile, not generic
fan feasibility.

`scripts/verify_ac_minimal_deficiency.py` exhaustively checks all
minimal deficient unit-token cores through five reopenings, exhausts
all role assignments through three reopenings and representative
assignments thereafter, verifies the balanced-bin collision bound, and
checks both the threshold and square-root routing alternatives.
